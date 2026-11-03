# Portable working-manuscript source PDFs

The seven PDFs in the v0.28.0 bundle are portable reading copies of the selected public manuscript bodies. They preserve the original Unicode characters and include the exact original Markdown as an attachment inside each PDF. Markdown, TeX and image references remain literal: equations and figures are not typeset or embedded in the page view. The full source and its supporting files remain available through each PDF's pinned source link. The PDFs are working research, not journal submissions or new proof checks.

In particular, the MSci PDF uses the 76,244-byte public portable reading manuscript, not the separate 75,969-byte original source edition. The release manifest identifies the exact source body for every PDF.

Each PDF also attaches the SIL Open Font License notices for Noto Sans and Noto Sans Math. The bundle includes the same notices as ordinary files, together with `MANIFEST.json`, which records each source hash, PDF hash, byte length and page count.

## Building

`build_portable_pdfs.py` uses PyFPDF 1.7.2, pypdf 6.21.4 and fonttools 4.68.0. A clean Python environment can install those exact versions using `python -m pip install fpdf==1.7.2 pypdf==6.21.4 fonttools==4.68.0`. This release used the PyPI source archive or pure-Python wheels with SHA-256 values respectively `125840783289e7d12552b1e86ab692c37322e7a65b96a99e0ea86cca041b6779`, `33e4fb41ca352810eb4e9838aa0d82d6888a5f8bf682f43e99cce5faa666255c`, and `d76f8fdcb6936f5e1045a0c9dd721a4bf11112e60d1e243bfa1d39f06a8b3104`.

Supply these exact, separately downloaded font files in `--fonts-dir`:

- [`NotoSans-Regular.ttf`](https://raw.githubusercontent.com/notofonts/notofonts.github.io/28b15b4b43b7bed62b5cf6e6b0b5ff5846270535/fonts/NotoSans/hinted/ttf/NotoSans-Regular.ttf), SHA-256 `478c558ea716033cd60c03438f628dfa75694dcf6b5f6d505a2f05fd2b4f3823`.
- [`NotoSansMath-Regular.ttf`](https://raw.githubusercontent.com/google/fonts/dbd1ab6e65dc59bcda3ca8de9fd372f58f98e0af/ofl/notosansmath/NotoSansMath-Regular.ttf), SHA-256 `3f495fe933c06786e4d5f6d86b8ee70b6753a68ee3b9d87528726de0f6e2c47d`.
- [`NotoSans-OFL.txt`](https://raw.githubusercontent.com/google/fonts/dbd1ab6e65dc59bcda3ca8de9fd372f58f98e0af/ofl/notosans/OFL.txt), SHA-256 `cee9892f9f0cc8fe882c9e9537ee6a89621d86ee7ceaf70b02e2b2b1c25c061a`.
- [`OFL.txt`](https://raw.githubusercontent.com/google/fonts/dbd1ab6e65dc59bcda3ca8de9fd372f58f98e0af/ofl/notosansmath/OFL.txt), SHA-256 `c9c63b8ed6cf76b2ce0c58b241acfc1195c2c928334c989c7047cbdac58773d9`.

The selected manuscript sources must match the pinned revision. With the fonts and dependencies available:

```sh
python -B tools/build_portable_pdfs.py OUTPUT_DIRECTORY --fonts-dir FONT_DIRECTORY --source-revision efff63beebe800802ee98a59e4dd7ef8850e0020
```

The script checks glyph coverage, checks each original attachment byte-for-byte, and uses pypdf to verify that the source text can be extracted in full after whitespace normalization. These are source and text-completeness checks, not mathematical verification or a complete visual-layout audit. A later rebuild may have a different binary hash; use the released manifest for the exact artifacts.
