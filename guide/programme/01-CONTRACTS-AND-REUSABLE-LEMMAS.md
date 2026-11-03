# Contracts and reusable arguments

This is the shared vocabulary of the reading edition. A result uses only the contracts it explicitly names. “Source” never means an arbitrary table of normalized probabilities.

## C1. One physical source

A comparison fixes a target source $T,\theta_T$. A rival has its own finite graph, original-ID map and tuple $N,\theta_N$. Each tuple is fixed across **all** its rows, retained samples, randomizations and controls. The two tuples need not agree. A construction whose graph or parameters change separately with the row is not a fitting source.

The original ancestry class is finite, rooted, binary, acyclic, cut-child, root = lowest stable ancestor, and outer-labelled planar, with parallel arc occurrences allowed. Its actual positive lengths and natural coins are strict. Other chapters explicitly relax or change these conditions. In particular, this class does **not** imply that every blob is a simple one-hybrid cycle. The admitted three-port, two-hybrid atom is a counterexample to that implication.

Natural **I** routing draws a fresh parent for each current lineage at a hybrid. Natural **COMMON** routing draws one parent per hybrid and locus, shared by its current lineages. A merger creates one current lineage: its two old leaves do not route separately later. Subtrees already formed remain opaque under every later operation.

## C2. Measurements are different contracts

* A complete topology is a rooted labelled tree after ancestral completion.
* An exit forest is the partial genealogy at a named population boundary. It is observable only when a proved decoder supplies it.
* A full calendar genealogy records merger ages in common calendar units. Its law is stronger than an unranked topology or a fixed time-bin law.
* A gene-quartet concordance factor is an **unrooted**, one-copy four-taxon law. Rooted comb contrasts can disappear on unrooting.
* A displayed-resolution distance averages the specified **distinct displayed resolutions** under its stated convention. It is not automatically a switching-probability average, concordance factor, sequence distance or likelihood.
* Exact population laws, finite samples and noisy/coarsened laws have different conclusions. Equality tests in a mathematical theorem are not automatically executable comparisons on arbitrary real oracles.

One copy of a taxon passing alone through a descendant component is the identity on its **topology**. This does not identify its route, sequence substitutions, population label or branch length. A component with several retained taxa is one joint kernel; replacing it by a product of single-taxon kernels is usually false.

## L1. Kingman restriction and semigroup

With $m$ current roots, each unordered pair merges at the same rate. Restrict a live forest to retained leaves, discarding empty trees. Invisible mergers do not change its restricted state; visible pair-merger rates are exactly the rates of the smaller process. Thus restriction intertwines the edge generators and hence their finite-time kernels. Equivalently use the exchangeable pair-clock coupling and treat every event leaving the restricted forest unchanged as silent, including a retained block merging with a wholly discarded block.

For the same generator $Q$, $e^{sQ}e^{tQ}=e^{(s+t)Q}$. If pair survival is $x=e^{-s}$, two consecutive ordinary edges compose by multiplying survivals. This identity requires no input at the suppressed vertex. It does not permit moving a routing event through an edge or combining different population generators without proof.

## L2. Label equivariance and opaque grafting

Relabel roots by a bijection, transporting distinguished starting ports, source labels and all other source data with them. Pair clocks are carried to pair clocks, I-routing choices to the corresponding current owners, and a COMMON site retains its **same** shared bit. Merger and graft operations commute with this bijection. Therefore the entire transported programme commutes with relabelling. This is not fixed-source symmetry under exchanging arbitrary taxa at different initial locations. For raw states, all fields must be transported, including inactive optional fields; an encode/decode operation defined only on reachable codes is not an inverse on arbitrary raw codes.

Consequently, once fresh roots enter one population, with no other retained input joining the region, its natural label-blind continuation is exchangeable on those roots, even if it contains routing. More general controls require an equivariant programme and the complete sufficient retained register, with the same conditional freshness premises. Arbitrary named-root forcing need not be invariant. This is a forward symmetry, not an inverse decoder or de Finetti representation.

Formal source-label transport and a fixed-source invariance are different statements. The inspected checked endpoints `SourceCopyCarrierTransport.mapLabels_joinPruned` and `actual_initial_copy_carrier_diagram` supply transport. The later G3 current-root note supplies the additional actual-choice coupling at **hand-proof** level; its newly proposed Lean endpoints are uncompiled.

## L3. Projectivity through a whole source

Apply L1 on each population and L2 at each routing, merger, control and graft boundary. Their chronological composition commutes with pruning. Completion and the permitted readout also commute. Thus sampling more and jointly hiding fixed copies gives the same retained law as sampling those copies alone, using the same graph, parameters and old register. See G2 for the exact checked scope. Never prune separately inside correlated same-locus records and then pretend their product is the joint law.

## L4. Finite-cut kernels

A finite descendant region with one upward cut port induces an actual stochastic kernel: sum its internal histories and stop at the port. Include the finite top edge and any word on it. At a hybrid child port, stop **before** the hybrid routes. The resulting kernels are normalized, projective and label-equivariant. In natural unmarked sources, disjoint descendant regions have independent private randomness. If permitted controls share a once-drawn register, the corresponding independence is conditional on that complete register; a fixed parameter tuple alone does not give unconditional independence. Positive paths with no merger give strictly positive no-merger probabilities at each finite cap. This proves properties of an existing source; it does not realize every abstract kernel satisfying those properties.

## L5. Cap-three coordinates

For an exchangeable, projective kernel on fresh roots let $d$ be pair separation, $n$ three-root separation, $c$ the probability of one specified cherry plus singleton, and $t$ one specified complete rooted triple. Restriction and normalization give

$$
n+3c+3t=1,\qquad d=n+2c,
\qquad c=(d-n)/2,\qquad t=(n-3d+2)/6.
$$

For an ordinary edge of survival $x$,
$$
n=x^3,\quad c_x=(x-x^3)/2,\quad
t_x=(1-x)^2(2+x)/6.
$$

For serial kernels $d$ and $n$ multiply: all initial roots must remain separate in both stages. With $e=t-t_{\rm ord}(d)=(n-d^3)/6$,
$$
e_{12}=d_2^3e_1+d_1^3e_2+6e_1e_2.
$$

These two coordinates determine the cap-three exchangeable projective kernel, so such kernels commute through cap three. They do not determine the full level-four forest law.

## L6. Cut-cohort exchangeability (CE)

Retain one copy each of distinct taxa $x,y$ below a single upward cut, no other taxon below it, and any copies outside. The cut returns either $\{x,y\}$ or $\{(x,y)\}$. Both are invariant under transposing $x,y$. The future is label-equivariant by L2. Hence the complete topology law, and any legitimately decoded exit law, is invariant in I and COMMON. In particular, for an outside $z$,
$$
P(((x,z),y))=P(((y,z),x)).
$$

For contemporaneous tips in a defined common calendar, the same proof preserves merger-node ages and ranks: both unmerged roots cross the cut at the same boundary age, and a merged cherry keeps its merger age under exchange. This separate conditional extension does not cover arbitrary route-decorated, population-labelled, substitution or unequal-tip-time measurements. Claude's r2 section2/section7 endpoints require this repair; the book uses the accepted untimed endpoint unless the extra calendar contract is explicitly supplied. [Independent source-use-site review, sections1–2](https://github.com/Sodelin/Research-Commons/blob/73e34a9bb3f083abffecf2bec40b64e0e14c33b6/research/2026-10-31-cut-cohort-source-review/REVIEW.md).

An unrestricted all-law converse is open; accidental triple ties defeat only a tie-only classifier. In I mode the cut pair can even be the least likely rooted triple. CE alone transfers no equality between different sources' COMMON laws. With COMMON inheritance and ordinary topology readout, condition on all natural site bits. In every displayed tree the cut pair traverses a common positive cut edge before meeting an outside taxon. If its separation probability is d, the triple law is (1−2d/3,d/3,d/3), so the within-pair gap is at least1−q_e>0, with q_e<1 that actual edge's survival. Averaging preserves the bound. These untimed/mode-specific conclusions are independently hand accepted in [the review, sections3–4](https://github.com/Sodelin/Research-Commons/blob/73e34a9bb3f083abffecf2bec40b64e0e14c33b6/research/2026-10-31-cut-cohort-source-review/REVIEW.md), not Lean endpoints.

## L7. Positive finite moments

Let $\mu=\sum_j w_j\delta_{x_j}$, $w_j>0$, on a **positive scalar** x, and let p be a nonzero **univariate polynomial**, nonnegative on that domain. If $\int p\,d\mu=0$, every supported $x_j$ is a root: the summands are nonnegative and their sum is zero. A nonzero univariate polynomial has finitely many roots. A supplied observable annihilator can therefore restrict actual bank survivals to a finite grid. This finite-root conclusion does not hold for arbitrary multivariate polynomials. The hard interface is acquiring that annihilator from the permitted input and turning grid support into an actual shared physical source bound.

For distinct integer exponents $a_1<\cdots<a_s$, a nonzero generalized polynomial $\sum c_i x^{a_i}$ has at most $s-1$ positive roots **counted with multiplicity**. Divide by the lowest power, which changes no positive zero; differentiation removes the constant term. Rolle with multiplicities and induction give r−1≤s−2. Negative powers may first be cleared on the positive domain. This is the sparse positive-grid bound used by the supplied-certificate branch. It is not a bound on arbitrary signed measures or unknown word length without its physical counting supplier.

## L8. Compactness, closure and attainment

A fixed finite graph with parameters in a closed interior slab has compact continuous image. If every successively accurate finite joint test fits within **one uniform graph/parameter budget**, a convergent subsequence fits all coordinates exactly. Without that uniform budget, only closure or escaping witnesses follow. Approximation clouds, projectivity and positivity of formal tables do not repair this missing quantifier.

## L9. Exact finite linear policy reduction

When legal responses are affine functions f_j(z)=a_j·z+b_j of one finite base vector z∈R^D, take ranks of their **linear coefficient vectors**, retaining known constants. If a=Σλ_ja_j, reconstruct f(z)=Σλ_jf_j(z)+b−Σλ_jb_j; a zero-slope reply is known already. Under reset and deletion-closed path costs, omit that physical query and simulate the policy internally. Each retained query increases slope rank, so at most D remain, without an extra affine-constant dimension. This is the finite-depth supplier for G7; it does not apply unchanged to noisy observations or costs depending on omitted physical actions.

## L10. Statistical transfer by coupling

If two sources' replies can be coupled equal at each of d stages, with conditional failure≤ε while the transcripts still agree, uniformly over the relevant reachable histories, their whole transcript TV is≤1−(1−ε)^d≤dε. This finite-depth estimate alone is insufficient for an infinite or unbounded stopping rule; a separate stopping/tail argument is needed, with suitable tail or uniform-integrability assumptions one possible route. Local agreement of individual row marginals does not establish agreement of adaptive joint histories.

## Sources and status

L1-L3 are the source-specific G2 proof ingredients plus classical Kingman symmetry. L4-L6 are the retained cut-kernel, current-root and Claude CE hand sources. L5 is elementary algebra from their stated interface. L7-L10 are shared arguments whose source contracts are checked separately in G3/G4, G7 and the transfer chapter. Exact source pins and formal endpoints are indexed in [the canonical catalogue](CANONICAL-CATALOGUE.md) and the chapters; the book does not claim a new formal build.
