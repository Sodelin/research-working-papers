#!/usr/bin/env python3
"""Make Unicode source PDFs with exact Markdown and font licenses attached.

Markdown, TeX and image references remain literal; this is not a typesetter.
Requires PyFPDF, pypdf and fontTools. See README-PORTABLE-BUNDLE.md for pinned inputs.
"""
from argparse import ArgumentParser
from hashlib import sha256
from io import BytesIO
from pathlib import Path
import json
import subprocess

from fontTools.ttLib import TTFont
from fpdf import FPDF
import fpdf.fpdf as fpdf_core
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parent.parent
SOURCES = {
    'msci': 'manuscripts/msci/MANUSCRIPT.md',
    'calibration': 'manuscripts/calibration/MANUSCRIPT.md',
    'product-coin': 'manuscripts/product-coin/MANUSCRIPT.md',
    'cap-three': 'manuscripts/cap-three/MANUSCRIPT.md',
    'g6-fixed-cell': 'manuscripts/g6-fixed-cell/MANUSCRIPT.md',
    'thue-morse': 'manuscripts/sequence/Thue-Morse-Hand-Proofs.md',
    'pattern-hierarchies': 'manuscripts/sequence/Pattern-Hierarchies-and-Selected-Digit-Proofs.md',
}
FONT_HASHES = {
    'NotoSans-Regular.ttf': '478c558ea716033cd60c03438f628dfa75694dcf6b5f6d505a2f05fd2b4f3823',
    'NotoSansMath-Regular.ttf': '3f495fe933c06786e4d5f6d86b8ee70b6753a68ee3b9d87528726de0f6e2c47d',
    'NotoSans-OFL.txt': 'cee9892f9f0cc8fe882c9e9537ee6a89621d86ee7ceaf70b02e2b2b1c25c061a',
    'OFL.txt': 'c9c63b8ed6cf76b2ce0c58b241acfc1195c2c928334c989c7047cbdac58773d9',
}


def digest(data):
    return sha256(data).hexdigest()


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('output_dir', type=Path)
    parser.add_argument('--fonts-dir', type=Path, required=True)
    parser.add_argument('--source-revision', default='HEAD')
    parser.add_argument('--only', nargs='+', choices=tuple(SOURCES))
    args = parser.parse_args()
    revision = subprocess.check_output(
        ['git', 'rev-parse', '--verify', f'{args.source_revision}^{{commit}}'], cwd=ROOT, text=True
    ).strip()
    fonts = {}
    for name, expected in FONT_HASHES.items():
        data = (args.fonts_dir / name).read_bytes()
        if digest(data) != expected:
            raise ValueError(f'font or license hash differs: {name}')
        fonts[name] = data
    cmaps = {
        'sans': TTFont(args.fonts_dir / 'NotoSans-Regular.ttf').getBestCmap(),
        'math': TTFont(args.fonts_dir / 'NotoSansMath-Regular.ttf').getBestCmap(),
    }
    fpdf_core.FPDF_CACHE_MODE = 1
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for slug in args.only or SOURCES:
        path = Path(SOURCES[slug])
        raw = (ROOT / path).read_bytes()
        if raw != subprocess.check_output(['git', 'show', f'{revision}:{path}'], cwd=ROOT):
            raise ValueError(f'working source differs from selected commit: {path}')
        source = raw.decode('utf-8')
        missing = sorted({c for c in source if not c.isspace() and not any(ord(c) in m for m in cmaps.values())})
        if missing:
            raise ValueError(f'font glyphs unavailable for {path}: {missing!r}')
        source_url = f'https://github.com/Sodelin/research-working-papers/blob/{revision}/{path}'
        notice = (
            'PORTABLE WORKING SOURCE COPY\n'
            'The complete original Markdown is attached to this PDF. Markdown, TeX and image\n'
            'references below remain literal; equations and images are not typeset here.\n'
            'Font licenses are attached. This is not a new proof, review or journal publication.\n'
            f'Source SHA-256: {digest(raw)}\nSource: {source_url}\n\n'
            '--- BEGIN MANUSCRIPT SOURCE ---\n\n'
        )
        pdf = FPDF(format='A4', unit='mm')
        pdf.set_title(f'{slug} - portable working source copy')
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_margins(15, 15, 15)
        pdf.add_page()
        pdf.add_font('sans', '', str(args.fonts_dir / 'NotoSans-Regular.ttf'), uni=True)
        pdf.add_font('math', '', str(args.fonts_dir / 'NotoSansMath-Regular.ttf'), uni=True)

        def write_line(line):
            current = None
            chunk = []
            for char in line:
                face = 'sans' if char.isspace() or ord(char) in cmaps['sans'] else 'math'
                if face != current and chunk:
                    pdf.set_font(current, size=8)
                    pdf.write(4.0, ''.join(chunk))
                    chunk = []
                current = face
                chunk.append(char)
            if chunk:
                pdf.set_font(current, size=8)
                pdf.write(4.0, ''.join(chunk))
            pdf.ln(4.0)

        for line in (notice + source).split('\n'):
            write_line(line)
        generated = pdf.output(dest='S').encode('latin-1')
        writer = PdfWriter()
        writer.append(PdfReader(BytesIO(generated)))
        writer.add_attachment('original-manuscript.md', raw)
        writer.add_attachment('NotoSans-OFL.txt', fonts['NotoSans-OFL.txt'])
        writer.add_attachment('NotoSansMath-OFL.txt', fonts['OFL.txt'])
        output = args.output_dir / f'{slug}-working-source.pdf'
        with output.open('wb') as stream:
            writer.write(stream)
        data = output.read_bytes()
        reader = PdfReader(BytesIO(data))
        if reader.attachments['original-manuscript.md'][0] != raw:
            raise ValueError(f'original source attachment differs: {path}')
        if (reader.attachments['NotoSans-OFL.txt'][0] != fonts['NotoSans-OFL.txt'] or
                reader.attachments['NotoSansMath-OFL.txt'][0] != fonts['OFL.txt']):
            raise ValueError('embedded font license differs from selected source')
        extracted = ''.join(page.extract_text() or '' for page in reader.pages)
        if ''.join(source.split()) not in ''.join(extracted.split()):
            raise ValueError(f'extracted source text differs: {path}')
        item = {'slug': slug, 'source': path.as_posix(), 'source_sha256': digest(raw),
                'pdf': output.name, 'pdf_sha256': digest(data), 'bytes': len(data), 'pages': len(reader.pages)}
        manifest.append(item)
        print(json.dumps(item, ensure_ascii=False))
    (args.output_dir / 'MANIFEST.json').write_text(
        json.dumps({'source_commit': revision, 'files': manifest}, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8',
    )


if __name__ == '__main__':
    main()
