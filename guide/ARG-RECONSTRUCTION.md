# ARG reconstruction, simulation cost and ancestry transport

The retained work can specify which ancestral-recombination information an implementation preserves, construct a particular marked stochastic history, and state when a genome-to-organism map preserves an ancestry property. It also connects expected simulation costs to classical probability formulas. These are distinct contributions: none alone reconstructs an organism pedigree from sampled DNA or solves every ARG inference problem.

This Codex/OpenAI assessment reads three selected guides and scoped original contract, statement-review, owner and ancestry sources. It does not rerun scientific controls, Lean, simulation or inference. The feedback selection here is its conditional recurrent-parenthood theorem; the finite-population epigenetic and cultural extensions are not selected for this reading note.

## A real external question about shared ancestry representations

[Wong et al., *A general and efficient representation of ancestral recombination graphs*, Appendix E](https://www.pure.ed.ac.uk/ws/portalfiles/portal/458588307/iyae100.pdf) distinguish local trees derived from a known ARG from ARGs inferred from separately estimated local trees. They ask how sharing some internal nodes affects the complexity of reconciling neighboring trees through subtree-prune-and-regraft operations. The selected appendix passages were inspected here. This is a question in that version, not a claim that a current exhaustive literature search establishes it is still open.

The retained extraction and normal-form results address representation contracts that matter before such an algorithm: persistent identities, sample support, retained paths and precise simplification. They do not solve the partially shared-label SPR complexity problem. Nor does linear-looking memoization bookkeeping for one rootward extraction give a complexity bound for stitching inferred trees into an ARG. This is a concrete connection to the paper's computational direction with the missing algorithmic step identified.

## A marked stochastic history needs more than a count chain

The retained [Big-ARG source contract](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/e2502c82ab9a77c00543932f775a71e5374221f7/research/wong/continuation-2026-09-27/source-audit/APPENDIX-B-CONTRACT.md) uses split rate `bk` and merger rate `a k(k-1)/2`, with `a>0`, `b≥0`, absorption at one and normalized parameter `θ=2b/a`. Its chosen coordinate model uses uniform continuous interior cuts. Conditional lineage and pair selection, fresh identities, interval inheritance, recorded dates and actual stopping must be connected to the count/clock law. Merely appending unused random marks would not establish that the output graph used them.

The guide reports a later construction of this stopped marked law for every finite positive initial count. The empty future tail after the stop has no extra events; one initial lineage stops immediately. This is a mathematical recording result, not a production parser or a newly executed simulator. A count law and its dates do not uniquely determine all labelled marks without the actual kernel assumptions.

The source contract also explains why a split followed by immediate reunion needs distinct lineage identities even when its event endpoints coincide. Merging endpoint-pair annotations can erase the cut. A normalized single-event inverse with distinct parent endpoints and an inverse for identity-preserving raw records therefore have different domains. Deleting empty ancestral material or changing to discrete-link cuts is not a free optimization: it changes the process until a relevant observation-preserving coupling is proved. The Little-ARG absorption and Big/Little common-observable comparison remain separate.

## Which graph do local arrays reconstruct?

For a finite acyclic interval graph with unique local parents, the retained sample-rootward scanner returns the active parent edges reached from designated samples. It recovers **every** active edge precisely when every such edge has a sample descendant. An unrelated active edge beside an isolated sample demonstrates why the extra support condition matters under the literal sample-tracing interpretation. The exact [historical statement review](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/e2502c82ab9a77c00543932f775a71e5374221f7/research/wong/completion/verification/deterministic65/SOL2-REVIEW.md) identifies that scope mismatch; it is not an author-acknowledged correction or a fresh whole-paper audit here.

The extraction counters are bounded by writes plus sample-list length under their stated cache conditions. They do not prove constant-time full scans, allocation bounds, across-coordinate amortization or tskit conformance. Persistent node IDs also carry information that independently renamed or suppressed local trees lose. A relation-level inverse does not automatically recover raw event clocks, metadata or exact interval-file bytes.

MRCA truncation removes more than unsupported ancestry: it removes edges into common ancestors above the relevant local MRCA. Existence/uniqueness of that MRCA needs nonempty samples, unique local parents and an existing common ancestor; the total construction has explicit empty, singleton and no-common-ancestor cases. The later contraction preserves its specified sample/MRCA paths. Its branching guarantee concerns incident **nonsample** nodes, so sampled ancestors may remain unary and unused catalogue IDs may remain isolated.

Canonical interval storage has its own fixed-point theorem. That does not establish idempotence of the complete truncation/contraction/storage pipeline. These distinctions make the retained work useful as a specification and source of conformance tests for a future engine, while leaving implementation, exact codec transport and broader simplification equivalence unproved.

## Cost formulas have classical suppliers

[Durrett, Section 3.4 and Theorem 3.10](https://sites.math.duke.edu/~rtd/Gbook/PM4DNA_0317.pdf) uses recombination birth rate `kρ/2` and coalescence death rate `k(k-1)/2`, credits Griffiths for the stopping-time integral, and derives state-occupation quantities. Those rate and theorem passages were inspected here. Translating to the retained process requires `ρ=θ=2b/a` and physical time scaled by `1/a`.

The recorded two-lineage mean becomes `2(e^θ-1-θ)/(aθ²)`, with limit `1/a` at zero. [Griffiths's 2006 lecture notes, ARG section](https://sites.math.duke.edu/~rtd/CPSS2006/griffiths.pdf) give the recombination-count integral through the grand first common ancestor and fixed-parameter large-sample behavior. The retained guide uses this prior to obtain total-jump counts, including `E[J_2]=2e^θ-1`. This is an explicit connection to established work, not a new generic cost formula claimed for the project.

The retained general-start series and its boundary justification remain guide deductions awaiting independent review; finite upper-ceiling controls are stopped models, not proofs of the unbounded process. Almost-sure finite events, finite expected physical time, expected event count and measured implementation time are different claims. Neither fixed-parameter asymptotics nor one loose drift bound supplies a uniform joint bound over sample size and recombination rate.

The Wong paper's brief cost sentence and displayed rates motivate a rate-normalization question. Under the specified expected-total-jump interpretation, substituting its split parameter changes the exponent in the retained comparison. Its cost variable, asymptotic quantifier and cited convention still need specialist interpretation. The original B07 source-clarification status is preserved; this is not an established erratum or a resolution of Little-ARG cost.

## Transferring an ancestry predicate to organisms

A genome history and an organism pedigree are different graphs. The retained [owner theorem](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/e2502c82ab9a77c00543932f775a71e5374221f7/research/wong/continuation-2026-09-27/bridge/ROBUST-IAP.md) needs an onto owner map with finite fibres and an appropriate ancestry relationship; those premises are not inferred by the map itself. Its robust IAP version permits finitely many wrong **ancestry answers per representative**, possibly with different finite error sets and no common numerical bound. Finiteness/cofiniteness is then preserved through saturated owner preimages.

This tolerance is not a bound on the number of edited immediate-parent edges: deleting one edge of an infinite chain can alter infinitely many transitive ancestry answers. The weakened theorem transfers IAP only, without automatically transferring convexity, connectivity, reflection or maximality. A finite sampled ARG cannot be onto an infinite biosphere. Erasing coordinates also allows graph paths that switch loci, rather than following one inherited segment throughout. These are concrete admission requirements for an ancestry-analysis receiver, not a species-assignment procedure.

The related recurrent-parenthood theorem applies to a finite set of demes with finite generation prefixes, continuing occupancy, one-generation parent edges, local parent coverage and universal bounded-lag within-deme dissemination. Under those strong conditions, an infinite organism set has IAP exactly when it is eventually contained in one recurrent strongly connected component. It is a project-posed application to [Alexander's IAP framework](https://arxiv.org/html/2602.05274v1), not an attributed solution of an external conjecture.

The dissemination premise rules out lineage extinction and fails almost surely in the ordinary independent two-parent finite-population sampling example described by the source. The written conditional-probability recurrence adapter is separate from the historical selected Lean endpoints. Recurrent contacts concern arbitrarily late generations; finite observed windows cannot establish them without an admitted stochastic model. This supplies a conditional structural theorem and a test of its applicability, not an empirical classifier or a blanket biological claim.

## Evidence and next bounded work

Seven receiver contracts accompany this note. The guide reports 77 retained project-source hashes matching a historical receipt and 415 selected axiom reports; these overlap other project modules and are not 77 distinct ARG discoveries. This assessment read selected contracts/reviews, not the full proof closure, objects or an independent kernel run. The feedback theorem and its uncompiled adapters retain their own separate status.

The next useful implementation or scientific work would specify a shared observable for Big/Little comparison, an exact extraction/export codec, a supported-data contract for tree reconciliation, or a justified genome-owner observation law. Independent specialist review is needed before promoting the source-interpretation questions or guide-derived cost reasoning.


The [receiver register](ARG-RECONSTRUCTION-REGISTER.json) states the seven input/output boundaries. Related selected source statements appear in the [ancestry programme chapter](programme/06-INFINITE-ANCESTRY-AND-POPULATIONS.md); this is an adaptation of the source identified in [provenance](../PROVENANCE.md), not a fresh proof audit.
