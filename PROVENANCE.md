# Source and release notes

This public reading selection was assembled on 3 November 2026 from the existing Terra manuscript owner's local Git commit `052d3eeb8015fb1285840312e7cce62b1cd3b152`. The owner retains the research and manuscript source. The initial import commit `3218297` in this repository preserves the selected files byte-for-byte; later commits record presentation changes and the release index. The source Git commit identifies a local workspace, not a public upstream URL.

| Reading edition | Selected source path at `052d3ee` | SHA-256 at import |
| --- | --- | --- |
| MSci portable manuscript | `research/corpus-portfolio/college-packet-v2/manuscripts/msci/MANUSCRIPT.md` | `10f67326d0bae07147f9a84a4bc508dd6332cc6a18661d55f989b902172cd9a0` |
| Rare-event calibration | `research/manuscripts/rare-event-calibration/MANUSCRIPT.md` | `d5b3ee3e2b503712a090df83b2bf0f6717eec7afdb386e341f5a2b30189100fc` |
| Product coins | `research/manuscripts/product-coin-guard/MANUSCRIPT.md` | `674e7326ff452ba9f68114bbc4d7494d7c64d28db89068a8c2b6cdd79c8f7b21` |
| Three-lineage forests | `research/manuscripts/cap-three-kernels/MANUSCRIPT.md` | `3051a77009a7cc5a396338d94c3a5f49a33e6f473b052690ac2c1a6f6925f237` |
| Fixed-cell law | `research/manuscripts/g6-fixed-cell-law/MANUSCRIPT.md` | `82cf53e8dda6f62d6f390d457d5868bea25d4dd4cdc00705d45c6dcb8ecb5bab` |

The MSci portable edition includes 42 evidence notes and one figure. Its source manifest names the earlier manuscript-assembly epoch `f33ec4716ea7e4f8551d640e86494395a42fe086`; the copy was taken from `052d3ee`. Its portable manuscript differs from the owner's 75,969-byte source manuscript (SHA-256 `d51e9852b6aee26f6b9dd7c8e23e8a6d00bd2eafa563c6cd2328cbb19cc3cec8`) in packaging and link adaptations. The original proof and review appendices retain their source attribution and stated status. The full historical dependency closure is not included.

At this release, display-math delimiters in the four short manuscripts were adapted for GitHub rendering; the fixed-cell paper's unavailable local-only links were replaced by its available public source-package link and an explicit description of the omitted evidence row. The earlier versions remain in import commit `3218297`. No new proof, formal check, empirical validation or independent review is asserted by this release. Existing source papers and primary literature are cited where used; no new license is asserted for third-party materials.

The nine-entry [research connection guide](guide/CONNECTIONS.md) and its
[machine-readable selection](guide/connections.json) were adapted from the
research-connections owner's local commit `5b3c52e` on 3 November 2026.
The original `connections.json` had SHA-256
`9ca8f63557f80b2ace327f7ced4ec94db476bba576ba9be7cfe28f2448663001`.
The public adaptation selects nine of its ten entries, removes local-only
paths and outreach metadata, and adds direct public project-source links.
The source's associated guide remains with its original owner. This is a
navigation and communication record, not a new proof or novelty audit.

The [public problem-record links](guide/PUBLIC-RECORDS.md) are a nine-entry
selection based on the theorem guide's local commit
`501730afc601aa196ff4c7b84e96105a63199668`,
`docs/VIBEMATHED-RECONCILIATION.md` (SHA-256
`af49dbc3895ac8a0f2abab8b387b655b31132e349b4aa7daa280f871465b894b`).
The linked pages are maintained by VibeMathed; all nine returned HTTP 200 on
3 November 2026. This selection does not reproduce the site's data set or
establish review, priority or completeness.

The two complete sequence reading bodies were copied byte-for-byte from the
scientific-library owner's local commit
`21222b5515f3bd3f3345d02f172ae95027535954`, under
`research/programme-hand-library/sources/sequence/`. The source library has no
verified public remote. `Thue-Morse-Hand-Proofs.md` has SHA-256
`e81fc46687a4de968f67242421daeb3d9761960b1363dedc55abe4a357bd8e35`;
`Pattern-Hierarchies-and-Selected-Digit-Proofs.md` has SHA-256
`f9c3201ca6cbc8cb2ea50b39b509a49e66acdec1b7dbf8793f945a7731cf779e`.
The source's `READING-EDITION-STATUS.md` gives their historical AI-review and
recovery limits; the [public reading notes](manuscripts/sequence/README.md)
carry those limits and the correction regarding Cloitre v2. No checker or
original review receipt is invented, and no new build or review is claimed.

The [twelve-chapter working programme guide](guide/programme/README.md) and
dated 118-card navigation catalogue were adapted from the scientific-library
owner's local commit `21222b5515f3bd3f3345d02f172ae95027535954`. The
[manifest](guide/programme/SOURCE-MANIFEST.json) records original and adapted
text hashes and citation-availability counts. This adaptation changes display
delimiters, makes available source links public, marks omitted local sources,
and uses the chosen public name. It does not reproduce private source packets,
prove the statements, perform a Lean build or close G3 or G4. Sixty available
G3 source bodies had matching Git blob identities against the cited public
Research Commons tree before their links were installed. A subsequent source
reconciliation matched six additional local source bodies to public Git blobs
at Research Commons commit `27b143c73a4ac272b560b2974d83ff96df738531` and
restored those six citations. Seventeen local-source references remain marked
unavailable in this edition.

The [quantum connection map](guide/QUANTUM-CONNECTIONS.md) was adapted from
the research-connections owner's local commit
`6bda163527d08c1fe8f623c03657f7d1a50aaa83`, `research/quantum-connections.md`
(SHA-256 `209cbf9aabdfe7dd87bfba82250bc13862d498eaed74bdc10e6c8a87fdac4a59`).
The adaptation substitutes the project's chosen public name; the result and
open-bridge descriptions are unchanged. It is a reading guide, not a new
correctness, physical-admission or novelty review.
