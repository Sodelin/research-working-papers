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

The owner's exact manuscript and front-matter bodies at `052d3ee` are also
available in [the preserved source edition](source-editions/msci-052d3ee/README.md).
Their recorded SHA-256 values match the original Git bodies; this is a version
and attribution record, not an additional paper or a new verification.

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

The [quantum decoding and estimation map](guide/QUANTUM-LOSS-CONNECTIONS.md)
was adapted from research-connections commit
`141a14cd13e33601fdfccc70d7ae9b21394cac94`,
`research/quantum-loss-connections.md` (SHA-256
`cee28571c4119ec91bff1b2fd98b2d25f899e2909a8eee9c29a07812b0a9500f`).
The adaptation uses the chosen public name and links the companion map; the
scope and source-review boundaries are preserved. The counterexample, actual
square-root application and AI review were separately read from their public
source URLs and matched the hashes recorded in the map.

The [binary morphism stability connection](guide/AVOIDANCE-CONNECTION.md)
was adapted from research-connections commit
`8a57cbeac0c15c8af7305fd06721f9a797686f78`,
`research/avoidance-connection.md` (SHA-256
`38d4e610d4239754c587204a9711b3941538464984b4e67c742d41a6658df17a`).
The public adaptation removes outreach bookkeeping and leaves the stated
result, attribution and review boundaries intact. The hand proof and its
AI review are linked at immutable public source versions.

The [selected-digit connection map](guide/SELECTED-DIGIT-CONNECTIONS.md) is
the unchanged authored source at research-connections commit
`1dc99837e863f5d8e5e4b3f2c7e29549b4ff1737`,
`research/selected-digit-connections.md` (SHA-256
`e4b3dbfadacd093a70c4aaf3f94b2edb2eb6c5b058256d3d985a18d4cb66490d`).
Its separate AI-review, historical-priority and noncomputable-parameter
boundaries are part of the reading selection, not new independent checks.

The [G1](guide/G1-EVIDENCE.md) and [G2](guide/G2-EVIDENCE.md) evidence notes
are public reading adaptations of manuscript owner Terra's dated portfolio rows
`c4f81bb3713827169fac506aaf0a86fe49682a29:research/corpus-portfolio/G1-EVIDENCE-JOIN.md`
(SHA-256 `f1bcd43dcafc19a374ea15b12f49aaee869565536f01b30c54d2a39584d039c7`)
and `c36d2a5b617668d3e545f5c87ef95cd7d98bfd17:research/corpus-portfolio/G2-EVIDENCE-JOIN.md`
(SHA-256 `96807cb6b297cf172a92d8f0b3a2d22be356902540715bf3914372d4d8789460`).
The adaptation links two exact public Lean endpoint bodies, marks five local
references unavailable, dates the old publication statements, and adds only
anonymous byte-identity observations. It does not establish their imported
proof closures or validate the biological source model.

The G1 note was subsequently updated from Terra's evidence successor
`d0ec8140980e1ffc51229de354e34a0f3a45cdb3:research/corpus-portfolio/G1-EVIDENCE-JOIN.md`
(SHA-256 `d3840992d84e87d16aa50020ebf265a94f19688a1f0cb00f6cfc940f98c981c2`).
Terra reports inspecting the public serial receipt and matching its named
source-hash field to the selected endpoint; underlying object/log/axiom and
imported-closure evidence remains uninspected. This edition did not reacquire
the receipt or run Lean.

The [fixed-code Collatz](guide/COLLATZ-CODING.md) and [controlled-state](guide/CONTROLLED-STATE.md) maps
are adapted from research-connections source commits
`ae316fa1449f9d1ad234aca8f3f87f3c2d7b98d6:research/collatz-coding-connection.md`
(SHA-256 `5e697308fab43b4d76f1126b733901ed2227946d5ce49ad4f97758dd9d1186af`)
and `521fc72bc19107c8d561d52504362b60a58a57ca:research/controlled-state-connections.md`
(SHA-256 `f55fdd4eac9e1d5984c299a961fb84bdd9bdb525159a99cb757c4cd3b287fccb`).
The adaptation clarifies a displayed arithmetic expression and removes
operational bookkeeping; claims, attribution and review limits are unchanged.

The five `docs/papers/` abstract pages were generated by
`tools/build_abstract_pages.py` from the source manuscripts at public commit
`ad7640d714d4e085804156ffef2f5cbc9bec05d0`. Each page identifies its exact
source-body SHA-256, links the complete manuscript and preserves the unresolved
authorship and independent-review boundaries. They support public discovery;
no indexing or citation-database inclusion is asserted.

The [statistical resources](guide/STATISTICAL-RESOURCES.md) and [grouped phase](guide/GROUPED-PHASE.md)
maps derive from research-connections source commits
`bd5131afd4b7ceaf07406f950d7d546f156539d3:research/statistical-resource-connections.md`
(SHA-256 `0175d51745ed9666516f87911ccbec8f1276836765703899698ddf1443ca846e`)
and `fbd549a8a8dc83ee93c91b0b90bfcbb8d88754ad:research/grouped-phase-connection.md`
(SHA-256 `14cd45475bed1ffaaace00544d575d9fea3f5c726be6ea65041abf4296f79384`).
The only adaptation adds a working relative link to the selected-digit map.
Original mathematical scope, attribution and review boundaries are retained.

The [quantum oracle resource guide](guide/QUANTUM-ORACLE-RESOURCES.md)
derives from research-connections source
`6192fccc6ca21980d55edec65c9e3a4ab1a70549:research/quantum-oracle-connection.md`
(SHA-256 `923d2acd25b6e8f6d38292dccff3ac2d2569d80456d01cd3c6dd1d314a9bc0c7`).
The public adaptation uses Sodelin's chosen public identifier in place of the
source first name. The scientific scope, external attributions, conditions and
review boundaries are unchanged. Anonymous source-body checks on 3 November
2026 matched the three hashes recorded in the guide.

The [restricted causal-oracle guide](guide/RESTRICTED-CAUSAL-CONNECTIONS.md)
is an exact copy of research-connections source
`b7a867176a91879db34e5f0dc2d6a1fceeda2663:research/restricted-causal-connections.md`
(SHA-256 `f5fe461b3ec35818e74277a2de2ede0bfbddca2aebd88c2c545f149911678b5f`).
It preserves the prior-work credit, k=0 target correction and minimax, statistical,
formal and specialist-review limits. Anonymous public source-body reads on 3
November 2026 matched the four hashes recorded in the guide.

The [matching and juggling guide](guide/JUGGLING-MATCHING-CONNECTIONS.md)
derives from research-connections source
`4abb4a8b3357c47ad086f9cce358a9024a11e7c6:research/juggling-matching-connections.md`
(SHA-256 `7b771f1908fa6a5b41c580f50b3350be608cb783454e603f26ae17286350cc02`).
The public adaptation omits the source final paragraph containing contact and
outreach bookkeeping; the mathematical scope, prior sources, attribution and
review boundaries remain. The linked public hand edition was anonymously fetched
on 3 November 2026 and matched the recorded SHA-256
`e81fc46687a4de968f67242421daeb3d9761960b1363dedc55abe4a357bd8e35`.
