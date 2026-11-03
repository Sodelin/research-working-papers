# Finite sampling: ancestry, rare routes and diversity need different evidence

The retained work gives useful answers to three sampling questions: what a finite ancestry record leaves undetermined, when more copies cannot overcome a rare route, and what collision measurements say about diversity. The common lesson is operational: specify the actual observation and target before treating more data as more identifying information.

This Codex/OpenAI assessment reads five selected guides and two exact historical cross-G review bodies. Original mathematical contributors and AI-review attribution remain. No new model, training, empirical dataset, compiler, solver or owner job ran. Formal receipts and guide-derived unreviewed consequences keep their separate status.

## A finite past is not its infinite continuation

The finite-gARG source constructs two compatible infinite completions of every input under its stated type assumptions. They preserve and reflect the finite graph's edges **and old-node ancestry** but disagree on the whole-population specieslike predicate. The observation is a finite graph; the target depends on an infinite genealogical continuation. The construction proves a deterministic decoder obstruction across those compatible histories. It does not prove equal DNA-sequence likelihoods, assign probabilities to futures or establish a universally accepted biological species definition.

The owner-map construction is another interface: one copy-transmission graph can support different organism histories, and edge-image equality need not lift a multi-edge ancestry path. Accurate copy IDs, organism ownership and path lifting are separate information. Its delayed-split sampling theorem uses a particular history family and an accurate owner-bit oracle; it does not infer that oracle from DNA or identify every pedigree.

An adapter to tree-sequence software must preserve those distinctions. Official tskit documentation makes individual association optional/null and represents genome ancestry through node/interval-edge tables. A valid table file therefore need not contain a complete organism pedigree or an infinite future. Time orientation, units, owner completeness and ancestry/path semantics require explicit checking. The documented representation is an implementation candidate, not an existing verified theorem adapter. [Official data model](https://tskit.dev/tskit/docs/stable/data-model.html).

## More blocks help under a declared dependence model

The finite-family source uses disjoint parental couples, distinct parental symbols at each block, independent fair inheritance across children and blocks, and exact child-symbol equality. Connecting children that match at least once gives a simple component estimator with a stated exact family-recovery probability. That target is a sampled one-generation family partition, not a complete pedigree.

The dependence control repeats each child's single fair inheritance bit at every block. Every block still has the same full within-block law across children as the independent model, but extra blocks provide no new independent information. Monotonicity of the component graph alone survives; the independent-block probability improvement does not. Mutation, ordinary nucleotide collisions, shared parents and observation error are excluded by the exact model, so real recombination cannot be equated to independent blocks without an adapter.

The prescribed three-taxon coalescent law similarly separates exact-law identification from finite evidence. Its strict mode gap is 1−c; a coordinate error smaller than half that gap preserves the answer. Every finite topology sample can still have overlapping support when c>0. Concentration needs independent correctly observed gene trees, not merely the deterministic margin theorem.

McNulty's v2 gives a different positive sampling guarantee: independent true gene trees under its fixed species-tree MSC model form a bipartition cover with prescribed probability once its balanced-recursion sample condition holds. A cover retains the true splits as candidates; it is not by itself full tree reconstruction or infinite specieslike classification. Its discussion proposes using partial topology information to sharpen bounds. No source-preserving reduction solving that refinement is supplied here. [Primary Theorem 2.9 and discussion](https://arxiv.org/html/2604.09509v2).

## Rare-route information saturates across finite copy allocations

The cross-G source constructs a positive tree/rare-reticulation family with a different split target. A fixed positive pre-hybrid waiting interval allows coalescence to bound the expected number of live ancestors at the rare route, uniformly over every finite number of initial copies. Its bound is

`E K(h) ≤ C_h=1/(1−exp(−ρh/2))`.

The resulting full-genealogy TV distance is at most εC_h under independent routing and ε under common routing. The constant is source-dependent and diverges as h approaches zero. The readout does not reveal population IDs or hidden routing coins. Conditioning on “no rare route” may bias the earlier genealogy; the proof uses a pathwise coupling rather than assuming an unchanged conditional law.

For the named known pair, an early-MRCA event gives a matching rare-route scale and passive locus cost of order ε^−1 at fixed confidence. This is not the same experiment as a small perturbation inside a full-support law, whose testing cost can scale differently. It is not a general optimal sequential solver or a lower bound that survives every arbitrary sequence-readout channel.

A separate same-registry controlled pair makes an ideal original-hybrid forcing action legal in both sources. At fixed source parameters/confidence, it changes this known-pair cost from passive order ε^−1 to forced order one. That is a useful experimental-design comparison **if** the ideal actuator and readout exist. It does not demonstrate an ancestral laboratory actuator, an arbitrary-source G7 optimum or a full reticulate-base robust-fibre classification. The latter remains an explicit extension question in the source history.

## A collision probability is not automatically a latent class count

For iid true class labels with weights w, pair collision probability is p₂=Σw_i², and D₂=1/p₂ is inverse-Simpson diversity. It equals richness only for equal weights. A designated draw's partner probability among N−1 others is `q_N=1−Σw_i(1−w_i)^(N−1)`. The retained example gives two distinct weight vectors with the same q₃ but different p₂. Independent blocks returning only that one partner flag then have identical observation laws; observing true pair equality instead directly identifies p₂.

A calibrated bound on the variability of size-biased class weights sharpens a nonasymptotic interval for p₂. Confidence-set projection can combine uncertain calibration and sampling error, with abstention when the feasible set is empty or a threshold is unresolved. It controls unconditional wrong-label probability under its stated events, not error conditional on choosing to report a label.

Kazdan and coauthors' preprint already states the exact partner formula and explicitly notes the need for semantic-similarity calibration. The retained work does not refute that distinction or the paper's controlled training experiments. Its contribution is a scope-aware inference/counterexample interface, not a newly discovered occupancy formula. [Primary Appendix D and Remark 5.3](https://arxiv.org/html/2603.06603v1).

For a nontransitive similarity relation, the relevant triple is a shared-anchor two-edge star, not a triangle. Its reciprocal pair probability is an operational relation statistic, not automatically latent class diversity. The latent-channel construction further shows that identical complete embedding laws can hide different class diversities. A separate guide-derived assay-efficiency example has the same read-label law with different cell-level proportions. These examples require independent review and actual channel calibration before biological or training conclusions.

Likewise, matching gradients at one parameter value does not ensure that deleting examples preserves later optimization or the minimizer. A downstream guarantee needs an error bound over the optimizer states used, not only a collision or similarity certificate. No new model test is authorized or performed by this connection.

## Concrete next interfaces

The [receiver register](FINITE-SAMPLING-REGISTER.json) separates finite-history completion, owner/block recovery, known-pair rare-route cost and calibrated diversity. A practical consumer must identify which quantity it needs, the actual joint observation, independence/dependence, hidden labels, readout errors and any actuator. Statistical law identification, deterministic completion ambiguity and optimization preservation are different acceptance tests.

Current gaps include a verified tree-sequence/owner adapter, dependence and inferred-tree error, arbitrary-reticulate copy-uniform extensions, semantic/assay calibration and source-faithful downstream-loss control. Suitable independent proof/priority review and accurate formal/native integration remain.


The [programme chapter](programme/06-INFINITE-ANCESTRY-AND-POPULATIONS.md) gives related selected finite-ancestry and sampling statements. This reading guide adapts the source recorded in [provenance](../PROVENANCE.md); it is not an independent proof audit.
