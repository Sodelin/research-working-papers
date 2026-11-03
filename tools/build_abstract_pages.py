#!/usr/bin/env python3
"""Build small, source-pinned HTML abstract pages with only the standard library."""
from hashlib import sha256
from html import escape
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://sodelin.github.io/research-working-papers'
REPO = 'https://github.com/Sodelin/research-working-papers'
SLUGS = ('msci', 'calibration', 'product-coin', 'cap-three', 'g6-fixed-cell')
revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()

for slug in SLUGS:
    path = Path('manuscripts') / slug / 'MANUSCRIPT.md'
    raw = (ROOT / path).read_bytes()
    text = raw.decode('utf-8')
    title = next(line[2:].strip() for line in text.splitlines() if line.startswith('# '))
    abstract = text.split('## Abstract', 1)[1].split('\n## ', 1)[0].strip()
    paragraphs = [re.sub(r'\s+', ' ', part).strip() for part in re.split(r'\n\s*\n', abstract)]
    if not paragraphs or any(not part for part in paragraphs):
        raise ValueError(f'abstract not found: {path}')
    source_url = f'{REPO}/blob/{revision}/{path.as_posix()}'
    canonical = f'{SITE}/papers/{slug}.html'
    title_html = escape(title, quote=True)
    abstract_html = '\n'.join(f'<p>{escape(part)}</p>' for part in paragraphs)
    description = escape(paragraphs[0][:220], quote=True)
    digest = sha256(raw).hexdigest()
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_html} | Research working papers</title>
<meta name="description" content="{description}"><meta name="citation_title" content="{title_html}">
<link rel="canonical" href="{canonical}">
<style>body{{font:1.05rem/1.65 system-ui,sans-serif;color:#20263a;background:#faf9fd;margin:0}}main{{max-width:48rem;margin:3rem auto;padding:0 1.3rem}}a{{color:#5638a4}}.status{{background:#f0ecfa;border-left:4px solid #7457bd;padding:1rem}}small{{overflow-wrap:anywhere}}</style>
</head><body><main><p><a href="{SITE}/">← All working papers</a></p><article>
<h1>{title_html}</h1><div class="status"><strong>Working research material.</strong> Sodelin organizes and shares this AI-assisted project. Contributions, scientific authorship and rights for eventual publications remain open. Source-specific AI attribution and verification limits are in the manuscript; the work has not received independent human specialist review.</div>
<h2>Abstract</h2>{abstract_html}
<p><a href="{source_url}">Read the full working manuscript and its evidence</a></p>
<p><a href="{REPO}/blob/{revision}/PROVENANCE.md">Source and release provenance</a></p>
<small>Manuscript source SHA-256: {digest}. This page presents the abstract from public source commit {revision}.</small>
</article></main></body></html>\n'''
    out = ROOT / 'docs' / 'papers' / f'{slug}.html'
    out.write_text(page, encoding='utf-8')
    print(f'{slug}: {len(raw)} source bytes, SHA-256 {digest}')
