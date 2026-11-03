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
dated navigation catalogue (118 source cards, 115 in this selection) were adapted from the scientific-library
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

The current chapter 8 adaptation omits one inherited external link whose
target visibility and sharing status were not established. Its original source
hash remains in the manifest; the adapted hash reflects this omission. Earlier
public Git versions still contain the inherited link. This correction does not
determine whether its target was accessible or whether any disclosure occurred.

A later selection omits source entries and direction rows subject to specific
action boundaries, and uses the chosen public identifier in the catalogue.
Earlier public Git versions and a previously archived snapshot predate this
selection and remain accessible; this edit does not alter those copies.

The updated public selection at `1ff385fdef402388ad2cf260ea79f9041ed4c8d4`
was independently archived as
[`swh:1:dir:0c63904e4fd1d640eaf0030e685b6e23b6e87e1a`](https://archive.softwareheritage.org/swh:1:dir:0c63904e4fd1d640eaf0030e685b6e23b6e87e1a/).
The archive's directory identifier matches that Git tree, and the archived
catalogue bytes match the selected edition. The source snapshot does not carry
the older Git history. An archive identifier is not a DOI, a journal submission
or a proof review.

The [moments and imaging guide](guide/MOMENTS-IMAGING-CONNECTIONS.md) adapts
the research-connections owner's local source commit
`abebf7cc27b183bf4c2f12e2701299a43e69f8c3`,
`research/moments-and-imaging-connections.md` (SHA-256
`5dad189577b0aa76a32cf71ee68a49cc09e8d74240b24b91f7ff315ec36987a5`).
The adaptation adds public source links, credits the paper's referee remark,
replaces a local-only evidence-record link, and omits local coordination and
an unrelated source-review note. The [Fourier source reading
copy](guide/sources/FOURIER-POISSON-READING.md) retains the mathematical body
of the original public dossier (SHA-256
`5d2bd1cf8f300caefa6f8780ca23d2ef824d5529a64697803f64d6d4ff2c5465`)
while omitting its navigation block with two external links of unverified target
visibility. It marks the historical opening statement superseded by the source's
own later polynomial-budget section. The original and two other selected public
component sources returned HTTP 200; their identities do not establish their
correctness or a human review.

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

The [exponential decision guide](guide/EXPONENTIAL-DECISION-CONNECTIONS.md)
derives from research-connections source
`7b51d2864acadac23e21b1fa96d53960ba6c18b7:research/exponential-decision-connections.md`
(SHA-256 `d8652c609d893608f15f04f65e2dee3cd440c7631be018391155954bbf525d55`).
The public adaptation omits the final operational ownership sentence. Its
mathematical contracts, original Codex attribution, prior-work credit,
conditional hypotheses and review boundaries remain. On 3 November 2026 the
linked source theorem returned HTTP 200 with the recorded 16,000-byte SHA-256
`b9f799edd2317efc79a13b4ef8a7cdc706ade985b1abea63ebbff141376fb0b6`.

The quantum-loss guide now links the 2026 Barnum–Knill erratum
([DOI](https://doi.org/10.1063/5.0325563)) and the authors' [revised preprint](https://arxiv.org/abs/quant-ph/0004088v2)
as a review lead. Publisher metadata was retrieved through Crossref on 3
November 2026. The exact relation to the separately credited Albarelli–Branford–Rubio
application has not been audited; no invalidation or fresh proof review is claimed.


The [state, ancestry and memory guide](guide/STATE-REPRESENTATION-CONNECTIONS.md)
adapts research-connections source
`23dc93a3be163d699c733b5ef1e2640a42516368:research/state-representation-transfer-boundaries.md`
(SHA-256 `efc20a3d0433e8eed9c3fb2b32a74722470d57c6fbc69ca00756898a0fc704ce`).
It replaces local source paths and operational notes with pinned public evidence,
adds primary background references and preserves original mathematical scopes,
attribution and independent-review gaps. The four linked CA and pruning/rank
source bodies matched their retained source bytes on 3 November 2026; the
materials source identity is recorded in the note. No source check constitutes
a new Lean run, physical validation or independent mathematical review.

The [memory-descriptor reading copy](guide/sources/MEMORY-DESCRIPTORS-READING.md)
preserves the mathematical body of dot/OpenAI's source from Research Commons
`27b143c73a4ac272b560b2974d83ff96df738531`,
`research/2026-10-15-connection-dossiers/memory-augmented-descriptors.md`
(17,152 bytes; SHA-256 `a040f778f5e0765704874db231cfb276086e9e25a912ce96447a8ac1949690cc`).
It omits the final navigation block containing two document-link values
of unknown target visibility, normalizes final blank lines and adds an explanatory
preamble; its mathematical body and original attribution remain. The independently fetched
`memory-sampled-cadence-test.md` at that revision matched its retained 13,316
bytes and SHA-256 `8b6601a760c45ccac2e9a104499a0e74464abeea26b99f339a3b8e902c972348`.
These are identity observations, not a new proof audit or a statement about the
visibility of the omitted link targets.


The [sequence and alignment](guide/SEQUENCE-ALIGNMENT-CONNECTIONS.md) and
[physics task](guide/PHYSICS-TASK-CONTRACTS.md) guides adapt research-connections
commit `68efbc98905dabef02c36ce8c50af8ada423f79d`, respectively
`research/sequence-alignment-connections.md` (SHA-256
`dd4253dc80e94c786db42c4165256483a8be6b1e47bc098e82044a188ba542d8`) and
`research/physics-task-contracts.md` (SHA-256
`382653608438097cc7ad7296028ca3a473bf073ca99ef01a5fe2f88cbaf039fc`).
The adaptation replaces local evidence references with public links and removes
operational bookkeeping; existing mathematical scope and attribution remain.
The primary Best–Peres question, Li–Ren–Wen record and Escudero Gutiérrez–Lee–Zur
Corollary 4.4 were read in their linked versions; no full-proof audit is claimed.

The [phase-control note](guide/NOISY-SEQUENCE-PHASE.md) adapts the theorem-guide
source `17cb7c4577ab91f067babbe4335f3f349c3d1048:research/noisy-sequence-phase.md`
(SHA-256 `495cfab4a3f1cdf60aacc9c80ff9a3747577e5589e83d515e54ace1f14f70831`).
It retains the finite phase-control discussion and replaces local links with
public sources; its unrelated bioinformatics comparison and local operational
notes are omitted. The source's historical calculations and tests were not rerun.

The [statistical decision guide](guide/STATISTICAL-DECISION-CONTRACTS.md)
adapts research-connections source
`6ca521c721febdf534f0060dbdc792e55abe61eb:research/statistical-decision-boundaries.md`
(SHA-256 `4b7666bdcc5433dc0c6787284949a5839ee8f224a2aad8f2c248361301158f22`),
replacing local evidence and operational notes with public references. The
independent-seed and compact-certificate bodies linked in that guide returned
HTTP 200 on 3 November 2026 and matched their reported hashes. Source identity
is not independent proof review, a complete rights audit or biological validation.


The [phylogenetic observation guide](guide/PHYLOGENETIC-OBSERVATION-CONNECTIONS.md)
adapts research-connections source
`242e01863de82b6275ce1ff5a9ca5b9b347d091d:research/phylogenetic-observation-connections.md`
(SHA-256 `3bd596e24c858c93a9f1b511e2c01e0ed039da9e17ae6f494751e14860da2b43`).
The adaptation replaces local ownership/operational notes with links to existing
public sources. The public MSci qualification, pulse-obstruction and model-
convention bodies matched the selected v0.17.0 Git bodies and the three hashes
in the source assessment. The analytic injectivity receipt covers only the named
formula result; the process/observation bridge, Jacobian and interval claims
remain outside it. No Lean or biological execution was performed here.


The public version 0.20.0 source snapshot at Git commit
`33567ffa15772cdc1c1a5c26f7a273b960ad4406` is independently archived as
[`swh:1:dir:d5a5d7c8e76c4f28cfd5d1e7c9673fc9e6930059`](https://archive.softwareheritage.org/swh:1:dir:d5a5d7c8e76c4f28cfd5d1e7c9673fc9e6930059/).
Software Heritage reported a full successful snapshot visit. Its inner
directory matches the exact Git tree, and the archived phylogenetic guide
matched its public source SHA-256 `ce35d53997318d4ce29eec6d55f9d006651f74d18f4f6954995edf8a32159f79`.
This is a persistent source identifier, not a DOI, journal submission or review.


The [G3 recognition](guide/G3-RECOGNITION-CONNECTIONS.md) and
[G4 finite-observation](guide/G4-FINITE-OBSERVATION-CONNECTIONS.md) guides adapt
research-connections sources:

- `8b86af83c6879fba57a60bda6509eeab66f44535:research/g3-recognition-connections.md`
  (SHA-256 `a2732692ea5b7c02fe72b69fc23ed11d74b3a1123f3fd097bc75e19acff15ff5`);
- `d3438fe07cd22d8707df5fa4187a874b16870b31:research/g4-finite-observation-connections.md`
  (SHA-256 `90623b341efb3f7cc98f9b9f9d0d193fb1c932ad7290897bd5d10e111392711f`).

Their method/observation JSON registers adapt the corresponding same-commit
source JSON files with original SHA-256
`310e88971eea8662fbf2b7a7bb6f3e4dbff2b60d4c196c3e7cdf7b963e11d181`
and `5e85e7142b6cd5af109f2472f79e6b019b8f154fb4b16510af8c3ee5ddf4a04b`.
Adaptations use the chosen public identifier in schema names, explain local
source-guide labels, replace operational notes with public source navigation,
and explicitly preserve the coefficient correction and the acceptance's
attributed AI-review involvement. No method outcome was promoted from UNKNOWN.
The original termination and natural-BOTH acceptance bodies returned HTTP 200;
the latter matched the source selection. No new proof or compiler run occurred.


The [G6 robust-certification guide](guide/G6-ROBUST-CERTIFICATION-CONNECTIONS.md)
adapts research-connections source
`495d2be726b8cc4f43c98bb2fabaebea717a57cb:research/g6-robust-certification-connections.md`
(SHA-256 `31aee5f5e37ab7c54a6b6d6ce18a15b2b52e4e82a8d422858722dd429cdac541`),
and its six contract records adapt the same-commit JSON source
(SHA-256 `023120200f31ca6199db221af4b844185ba9a38b101c158a23b65a73ae284ba2`).
The adaptation adds a pinned review link and its original AI attribution,
replaces internal operational wording, and uses the chosen public identifier
in the JSON schema name. The six contract records remain unchanged. The
review body matched its retained source SHA-256 on 3 November 2026. No new
model, compiler, solver or human review was performed.


The [experimental-design guide](guide/EXPERIMENTAL-DESIGN-CONNECTIONS.md)
adapts research-connections source
`56bb40a62727ecc82f6e6f88875788b4642081ff:research/experimental-design-connections.md`
(SHA-256 `3e25761517bfe4bb1fcc9ad2bef601ac0a264383b2bb64fae7ffcb19ce149b0d`)
and its six receiver contracts adapt the same-commit JSON source
(SHA-256 `d0cdbef5e070493d9872538cd40ec255739657160f5bcf3ae71b365d45829243`).
The adaptation adds the pinned AI hand-review link and the classical covering-
array attribution stated in the cited primary source, replaces internal
operational wording, and changes only the schema identifier in the JSON.
The six source-level contracts remain unchanged. The review body matched its
retained source SHA-256 on 3 November 2026. This is not a new proof, compiler
run, source-law validation or human specialist review.


The [root-blob question guide](guide/ROOT-BLOB-QUESTIONS.md) adapts
research-connections source
`8b2eee7a8358afb6bdd29c216a57b5b1f796807f:research/root-blob-open-problem-connection.md`
(SHA-256 `ba57d6ad2de0b6eae85bd215298cffe86fbc5165212b3c8013cf7d71b072fb4b`).
The same-commit two-question JSON source has SHA-256
`ae6dc67018d7f32f6e1a9fdb69aeada295c579a724314b6adb9f90f6433df065`; its
question records remain unchanged, with only the chosen public schema identifier
substituted. The adaptation adds the coordinating dot/OpenAI review link and
replaces operational wording. The proof, AI review and definition-reconciliation
bodies returned HTTP 200 and matched their retained hashes on 3 November 2026.
The cited external questions were checked in their specified versions; no new
proof, compiler run, human review or global current-status audit is asserted.


### RNA, reaction observations and lineage inference

The [RNA-CLASS-INFERENCE.md](guide/RNA-CLASS-INFERENCE.md) reading adaptation uses research-connections source `eb0d417d3a209e8d4e0eca102fce5f4644373434:research/rna-class-inference-connections.md` (SHA-256 `542252cafbb7a971ea34f4800563ac185be52b41d0ec85d0264a938ecd0c97dc`) and its [RNA-EXTENSION-REGISTER.json](guide/RNA-EXTENSION-REGISTER.json) register from `research/rna-extension-register.json` (SHA-256 `ac144803065c3ab9ea84caef149201c214457f8c7d97dec011a33fbf3ba49220`). The adaptation updates the register link, adds the related public programme chapter and removes internal coordination wording; the JSON records are unchanged except for the public schema identifier.

The [REACTION-OBSERVATIONS.md](guide/REACTION-OBSERVATIONS.md) reading adaptation uses research-connections source `cabeac7f62c4277290bf66f4a226644d975daf65:research/reaction-observation-connections.md` (SHA-256 `2091511188b306c109c2200b9c1c259ddfea1dbaf39a75221de47b51998bf058`) and its [REACTION-OBSERVATION-REGISTER.json](guide/REACTION-OBSERVATION-REGISTER.json) register from `research/reaction-observation-register.json` (SHA-256 `1b8baf94bc32f63d9f6990b7ea3f4c8e4632d448fb0cb522b656f8d058ded63f`). The adaptation updates the register link, adds the related public programme chapter and removes internal coordination wording; the JSON records are unchanged except for the public schema identifier.

The [LINEAGE-INFERENCE.md](guide/LINEAGE-INFERENCE.md) reading adaptation uses research-connections source `423c338a5556844ccb9de88c9f5c10059357dc46:research/lineage-inference-connections.md` (SHA-256 `5078a567a983e9240d2a8f2f012604bc059738583a62fc5fc4cae3d752424fe9`) and its [LINEAGE-INFERENCE-REGISTER.json](guide/LINEAGE-INFERENCE-REGISTER.json) register from `research/lineage-inference-register.json` (SHA-256 `0d7f0a9add9f0137ec0e57eacc32b7e9218558b9000e8ad46434a27faff5955b`). The adaptation updates the register link, adds the related public programme chapter and removes internal coordination wording; the JSON records are unchanged except for the public schema identifier.

The adaptation also adds direct public source links. On 3 November 2026, the reaction pointwise checkpoint and parent-retaining lineage witness returned HTTP 200 and matched the retained source hashes `b22f65bdc0e4b49710dea5fc0c82b07addf0102520e32de6b985b5cdc41223af` and `7252189e0e13d1d68252d84629fa2800de0c64ac4cd8acabb7375822351ec1f6`. The RNA admission register and lineage refinement source returned HTTP 200; no retained-byte match is claimed for those two reads. The source owner reported scoped source and AI-review reading, not independent human review or a new scientific execution. These editions retain the specific model, source and review limitations in their texts.

The [finite-sampling guide](guide/FINITE-SAMPLING.md) adapts research-connections source `30e85f34fc0ad447b244c7242eba4f2411115732:research/finite-sampling-connections.md` (SHA-256 `ac35fb55a7115af3f34cfc117d6352b00664f6ec6571e3e77337daeb8276ba15`), and the [receiver register](guide/FINITE-SAMPLING-REGISTER.json) adapts its same-commit JSON (SHA-256 `c29b6d59e7a928988f5040778d0050fc9733bd17d5943f720c14247790083625`). The adaptation updates the register link, adds the public programme chapter and removes internal coordination wording; receiver records are unchanged except the public schema identifier. Source-specific reviews, dependence, observation and actuator assumptions remain; no new execution or biological validation is claimed.

The v0.25.0 `calibration-working-source.pdf` is a portable source reading copy, not typeset mathematics. It was generated from `4a790cc4fe8e1efa4dd95f2ab4bce33591bc9664:manuscripts/calibration/MANUSCRIPT.md`, SHA-256 `fb4e44f614f7a449dddae51a206092ecf6e656d012bb72b896e1cc2a604628a1`. Markdown and TeX remain literal; the few non-ASCII symbols are spelled out as indicated in the PDF. The three-page artifact is 5,766 bytes, SHA-256 `bbd1ab5c1b76c3a034732d535160c33d74826637b299b7120af0151299262f68`. Independent text extraction recovered the entire transformed source after whitespace normalization. This is a format and completeness check, not a new mathematical verification. See [build notes](tools/README-PDF.md).


### Observation transfers, demographic laws and cellular measurements

The [FINITE-OBSERVATION-TRANSFERS.md](guide/FINITE-OBSERVATION-TRANSFERS.md) reading adaptation uses research-connections source `d49264eecc9f4b1510534cc3828d0303c065a4cb:research/finite-observation-transfer-limits.md` (SHA-256 `f59ee76d6b1574fe994234c1f716081cc02e3437834ae49a50a776786e8c8209`); its [FINITE-OBSERVATION-TRANSFER-REGISTER.json](guide/FINITE-OBSERVATION-TRANSFER-REGISTER.json) adapts `research/finite-observation-transfer-register.json` at the same commit (SHA-256 `baf88296c07233ac30e06c2094850eec5305fbdb82904d4fa4842ad2b5c798bd`). The adaptation updates register links, substitutes a public programme reference for any local-only path, adds selected source-review links, and removes internal operational wording where applicable. JSON records are unchanged apart from the public schema identifier.

The [DEMOGRAPHIC-LAWS.md](guide/DEMOGRAPHIC-LAWS.md) reading adaptation uses research-connections source `a10aa1fbe27f6930b6016a398dfc8e5bbd766413:research/demographic-law-connections.md` (SHA-256 `1b46ef10a1d2fcf029bb4650e6190ae055cd1060b4e57ebb3f2886812e0a95ab`); its [DEMOGRAPHIC-LAW-REGISTER.json](guide/DEMOGRAPHIC-LAW-REGISTER.json) adapts `research/demographic-law-register.json` at the same commit (SHA-256 `5e3750e5f127f40ed4f7ce368275f73202255c3cb8777703e654d79f5374bcea`). The adaptation updates register links, substitutes a public programme reference for any local-only path, adds selected source-review links, and removes internal operational wording where applicable. JSON records are unchanged apart from the public schema identifier.

The [CELLULAR-MEASUREMENTS.md](guide/CELLULAR-MEASUREMENTS.md) reading adaptation uses research-connections source `14e87e7c3eefbb4c3ae3ab61d3bb0e83a699c8aa:research/cellular-measurement-connections.md` (SHA-256 `e53551d30e84f0d933fba91ab23c7c5ae325e517d9750311e1cfffd08944ee37`); its [CELLULAR-MEASUREMENT-REGISTER.json](guide/CELLULAR-MEASUREMENT-REGISTER.json) adapts `research/cellular-measurement-register.json` at the same commit (SHA-256 `38796813eec5dd785c0790023ef021cd9250c9e082617a11c62e869241c7a38d`). The adaptation updates register links, substitutes a public programme reference for any local-only path, adds selected source-review links, and removes internal operational wording where applicable. JSON records are unchanged apart from the public schema identifier.

All 24 selected retained guide/review bodies in the three supplied evidence records matched their recorded SHA-256 identities locally. The four-normal, three-copy and global-alignment historical AI reviews were fetched anonymously and matched their respective retained bodies; identity is not a new proof audit. No new scientific execution, model test, specialist review or data validation is claimed.


The [ARG reconstruction guide](guide/ARG-RECONSTRUCTION.md) adapts research-connections source `e719f193730b1562947aa852b6dffe754d88e01a:research/arg-reconstruction-connections.md` (SHA-256 `ccfc4a7a9728c0108938952ac92257875ef29952cd07566430f041f62ef07df9`); its [receiver register](guide/ARG-RECONSTRUCTION-REGISTER.json) adapts the same-commit JSON (SHA-256 `abe0d601634da3fee29c93a7691c18b21986cd93fe8351631be9e9d537741ebe`). The adaptation adds selected original source links and a public programme reference, omits internal operational wording and changes the public schema identifier, while preserving the seven receiver records and restricted recurrent-parenthood selection. All seven selected retained guide/review bodies matched their recorded hashes locally. The linked statement review, Big-ARG source contract and owner-IAP body returned HTTP 200 and matched their retained source hashes. These checks establish identities, not an independent proof audit, model execution or empirical validation.


The [infinite-populations guide](guide/INFINITE-POPULATIONS.md) adapts research-connections source `88255e774e2659af7034273ba3a542b1ba5ac745:research/infinite-population-connections.md` (SHA-256 `a8c306e2be653ef5d86388bc326a91e0adad7cdddbdd715c120eb1930a843de6`); its [receiver register](guide/INFINITE-POPULATION-REGISTER.json) adapts the same-commit JSON (SHA-256 `f9937c9a7484d4dd97cf6efd09a806f3ff47db5f769a4bd159e357c45df01f10`). The adaptation adds public AI-review and selected source links, a programme reference and register link, omits internal contact wording, and changes the schema identifier while preserving eight receiver records. All seven selected guide/review/source bodies matched their recorded hashes locally; the linked capped-host AI review and founder source also matched via anonymous public reads. Identity checking is not a new proof audit or compiler run.
