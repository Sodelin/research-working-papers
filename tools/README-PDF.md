# Portable source PDF

`build_source_pdf.py` makes a literal source reading copy of the rare-event calibration manuscript. Markdown and TeX are visible rather than typeset. A short notice lists the ASCII substitutions for the handful of mathematical symbols; the source body and attribution remain available at the pinned GitHub URL in the PDF. The script refuses unhandled non-ASCII characters and refuses to use a working source that differs from its selected commit.

The released copy was generated using PyFPDF 1.7.2, whose PyPI source archive SHA-256 was `125840783289e7d12552b1e86ab692c37322e7a65b96a99e0ea86cca041b6779`. Its extracted text was checked with pypdf 6.21.4, whose pure-Python wheel SHA-256 was `33e4fb41ca352810eb4e9838aa0d82d6888a5f8bf682f43e99cce5faa666255c`. These are separate dependencies and are not included in the repository. The build here used the standard built-in Courier font.

With those packages available, run:

```sh
python -B tools/build_source_pdf.py --source-revision 4a790cc4fe8e1efa4dd95f2ab4bce33591bc9664 calibration-working-source.pdf
```

The checked-out manuscript must match that commit. PyFPDF writes the creation time into the PDF, so a later rebuild need not have the same file hash. Compare extracted source text after the documented substitutions as well as the manuscript's SHA-256; a successful conversion does not validate the argument.
