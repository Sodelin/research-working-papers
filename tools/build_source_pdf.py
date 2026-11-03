#!/usr/bin/env python3
"""Create a portable, literal source reading copy of the calibration paper.

Requires PyFPDF 1.7.2. This deliberately keeps Markdown and TeX visible;
it does not claim typesetting or mathematical verification.
"""
from hashlib import sha256
from pathlib import Path
import argparse
import subprocess

from fpdf import FPDF

ROOT = Path(__file__).resolve().parent.parent
SOURCE = Path('manuscripts/calibration/MANUSCRIPT.md')
SUBSTITUTIONS = {
    '·': ' | ', '≥': '>=', '≤': '<=', '₀': '_0', 'ₑ': '_e',
    'α': 'alpha', 'β': 'beta', '∎': '[end of proof]', '−': '-',
}


def ascii_source(text):
    """Make the few non-ASCII mathematical characters explicit in plain text."""
    result = ''.join(SUBSTITUTIONS.get(char, char) for char in text)
    result.encode('ascii')  # Refuse to silently drop an unhandled character.
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('--source-revision', default='HEAD', help='commit containing the exact manuscript source')
    args = parser.parse_args()
    raw = (ROOT / SOURCE).read_bytes()
    digest = sha256(raw).hexdigest()
    revision = subprocess.check_output(
        ['git', 'rev-parse', '--verify', f'{args.source_revision}^{{commit}}'], cwd=ROOT, text=True
    ).strip()
    committed = subprocess.check_output(['git', 'show', f'{revision}:{SOURCE}'], cwd=ROOT)
    if raw != committed:
        raise ValueError('working manuscript differs from the selected source revision')
    source_url = f'https://github.com/Sodelin/research-working-papers/blob/{revision}/{SOURCE}'
    notice = (
        'PORTABLE WORKING SOURCE COPY\n'
        'This copy keeps Markdown and TeX as literal source text. It is not\n'
        'typeset mathematics or a new proof, peer review, or journal publication.\n'
        'Characters are written as follows: >=, <=, _0, _e, alpha, beta,\n'
        'and [end of proof]. The exact original is at the link below.\n'
        f'Source SHA-256: {digest}\n'
        f'Source: {source_url}\n\n'
        '--- BEGIN MANUSCRIPT SOURCE ---\n\n'
    )
    pdf = FPDF(format='A4', unit='mm')
    pdf.set_title('Distinguishing an impossible event from a rare event - working source copy')
    pdf.set_subject('Literal source reading copy, with Markdown and TeX retained')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(15, 15, 15)
    pdf.add_page()
    pdf.set_font('Courier', size=8)
    pdf.multi_cell(0, 4.2, notice + ascii_source(raw.decode('utf-8')))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(args.output), 'F')
    print(f'Wrote {args.output}; source commit {revision}; SHA-256 {digest}')


if __name__ == '__main__':
    main()
