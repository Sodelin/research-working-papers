#!/usr/bin/env python3
"""Build small, source-pinned HTML abstract pages with only the standard library."""
from hashlib import sha256
from html import escape
from pathlib import Path
import argparse
import re
import subprocess

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://sodelin.github.io/research-working-papers'
REPO = 'https://github.com/Sodelin/research-working-papers'
MANUSCRIPTS = ('msci', 'calibration', 'product-coin', 'cap-three', 'g6-fixed-cell')
SEQUENCE = {
    'thue-morse': {
        'path': 'manuscripts/sequence/Thue-Morse-Hand-Proofs.md',
        'paragraphs': (
            'For the Thue–Morse word, this reading edition presents proofs of three first-occurrence formulas for longest monochromatic arithmetic progressions of differences 2^m+1 and 2^m−1. It also connects a separate matching-height construction to juggling and derives an exact average-height formula.',
            'The mathematical exposition is by dot (OpenAI). A separate Lean package and historical build and audit reports cover the named first-occurrence statements; the later juggling and average-height consequences are hand results. Internal AI hand review is not independent human peer review, and historical priority remains open.',
        ),
    },
    'pattern-hierarchies': {
        'path': 'manuscripts/sequence/Pattern-Hierarchies-and-Selected-Digit-Proofs.md',
        'paragraphs': (
            'This reading edition presents exact phase-recovery and factor-count results for a grouped binary substitution family, together with complexity, critical-exponent and branching comparisons for a distinct selected-binary-digit family.',
            'The mathematical exposition is by dot (OpenAI), with reported AI hand review and no Lean claim for this edition. Cloitre’s revised paper already supplied an all-level factor-complexity recurrence and seed; comparison with earlier work and independent specialist review remain open.',
        ),
    },
}
SLUGS = MANUSCRIPTS + tuple(SEQUENCE)
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--only', nargs='+', choices=SLUGS, help='rebuild selected pages; the sitemap always lists all pages')
args = parser.parse_args()
revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()

for slug in args.only or SLUGS:
    sequence = SEQUENCE.get(slug)
    path = Path(sequence['path']) if sequence else Path('manuscripts') / slug / 'MANUSCRIPT.md'
    raw = (ROOT / path).read_bytes()
    text = raw.decode('utf-8')
    title = next(line[2:].strip() for line in text.splitlines() if line.startswith('# '))
    if sequence:
        paragraphs = sequence['paragraphs']
        heading = 'Reading summary'
        source_description = 'This page summarizes the public source'
    else:
        abstract = text.split('## Abstract', 1)[1].split('\n## ', 1)[0].strip()
        paragraphs = [re.sub(r'\s+', ' ', part).strip() for part in re.split(r'\n\s*\n', abstract)]
        heading = 'Abstract'
        source_description = 'This page presents the abstract from public source'
    if not paragraphs or any(not part for part in paragraphs):
        raise ValueError(f'abstract not found: {path}')
    source_url = f'{REPO}/blob/{revision}/{path.as_posix()}'
    canonical = f'{SITE}/papers/{slug}.html'
    title_html = escape(title, quote=True)
    abstract_html = '\n'.join(f'<p>{escape(part)}</p>' for part in paragraphs)
    description = escape(paragraphs[0][:220], quote=True)
    digest = sha256(raw).hexdigest()
    pdf_link = (
        f'<p><a href="{REPO}/releases/download/v0.25.0/calibration-working-source.pdf">'
        'Download the portable source PDF</a> (literal Markdown and TeX).</p>'
        if slug == 'calibration' else ''
    )
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_html} | Research working papers</title>
<meta name="description" content="{description}"><meta name="citation_title" content="{title_html}">
<link rel="canonical" href="{canonical}">
<style>body{{font:1.05rem/1.65 system-ui,sans-serif;color:#20263a;background:#faf9fd;margin:0}}main{{max-width:48rem;margin:3rem auto;padding:0 1.3rem}}a{{color:#5638a4}}.status{{background:#f0ecfa;border-left:4px solid #7457bd;padding:1rem}}small{{overflow-wrap:anywhere}}</style>
</head><body><main><p><a href="{SITE}/">← All working papers</a></p><article>
<h1>{title_html}</h1><div class="status"><strong>Working research material.</strong> Sodelin organizes and shares this AI-assisted project. Contributions, scientific authorship and rights for eventual publications remain open. Source-specific AI attribution and verification limits are in the manuscript; the work has not received independent human specialist review.</div>
<h2>{heading}</h2>{abstract_html}
{pdf_link}
<p><a href="{source_url}">Read the full working manuscript and its evidence</a></p>
<p><a href="{REPO}/blob/{revision}/PROVENANCE.md">Source and release provenance</a></p>
<small>Manuscript source SHA-256: {digest}. {source_description} commit {revision}.</small>
</article></main></body></html>\n'''
    out = ROOT / 'docs' / 'papers' / f'{slug}.html'
    out.write_text(page, encoding='utf-8')
    print(f'{slug}: {len(raw)} source bytes, SHA-256 {digest}')

urls = [SITE + '/'] + [f'{SITE}/papers/{slug}.html' for slug in SLUGS]
entries = ''.join(f'  <url><loc>{escape(url)}</loc></url>\n' for url in urls)
(ROOT / 'docs' / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + entries + '</urlset>\n', encoding='utf-8'
)
(ROOT / 'docs' / 'robots.txt').write_text(
    f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n', encoding='utf-8'
)
