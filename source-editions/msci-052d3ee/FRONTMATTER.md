# Two-site identification in a fixed three-taxon pulse model

**Working manuscript for discussion — 31 October 2026.** This edition assembles two existing mathematical components for review. A predecessor working copy is public on GitHub; this local successor is not a submitted preprint or a peer-reviewed paper. The original proof text is attributed to **dot (OpenAI), 5 October 2026**, in the retained sources. Sodelin organizes and shares the working manuscript to seek collaborators and learn biology or bioinformatics; this posting role does not establish authorship of the underlying scientific ideas. Human scientific authorship, contribution statements, rights and the final author list remain open. Full Pro supplied the initial editorial organization and source binding; Terra prepared this navigation successor. No new scientific result is claimed.

## Abstract

In a specified three-taxon multispecies-coalescent-with-introgression model, how much sequence information suffices to identify its parameters? The retained hand proofs treat a known species backbone, one directed pulse, six completely observed, phased, labelled haploid samples and a known homogeneous JC clock. Under strict event ordering, positive finite rates and the stated rate ties, nine pair-character expectations obtained from two homologous sites determine all nine parameters. The construction first identifies the root time and rate, then resolves the pulse and ancestral onset through pair-law monotonicity and a global single-crossing argument. A second proof establishes a nonsingular nine-feature Jacobian throughout the strict parameter domain, including coincident-rate cases, and states an all-compatible-source interval inclusion for uncertain target moments. These conclusions distinguish exact identifiability from numerical conditioning, finite-data accuracy and biological model adequacy. The retained proof bodies and historical reviews are AI-authored and have not received independent human review. The reported Lean check establishes injectivity of the analytic formulas. A formal connection between the constructed stochastic process, the shared-genealogy observations and those formulas remains incomplete; the separate Jacobian and interval statements also lack complete Lean verification.

## 1. Research question and contribution boundary

Different demographic parameters may produce indistinguishable observations. An identifiability result must specify both the family of possible histories and the observations being compared. Here the question is deliberately restricted: whether the exact two-site locus law distinguishes admitted parameter vectors **within one fixed directed pulse family**. The result does not identify an arbitrary phylogenetic network, infer the pulse direction, or test whether that family generated a biological dataset.

The contribution assembled here is the source-specific nine-feature identification argument and its Jacobian companion. Classical pair-law analysis, Laplace transforms, root-pair inversion and interval methods retain the attribution in the original sources. This edition does not establish historical priority. The bibliography in the appendices is inherited from the source authors; a current literature and rights review remains to be completed.

[Durden and Sullivant's Theorem 5.1](https://arxiv.org/pdf/1705.06993v1#page=16) gives an earlier identification result from two expected k-mer distances in a tree/coalescent setting. For lengths one and two, those distances and the root-pair moments used here have an invertible algebraic relationship under the conventions in the [source comparison](DURDEN-SULLIVANT-COMPARISON.md). For contemporaneous samples their species-path length is twice the root age used here, conditional on the retained AC pair marginal. In another three-species model, [Zhu and Yang](https://doi.org/10.1093/molbev/msab009) report four-parameter identification by full likelihood with two sites per locus and one sequence per species; they distinguish pooled-site methods, which can lose information. Their [comparison](ZHU-YANG-COMPARISON.md) records the model and reading limits. Neither predecessor alone establishes the present six-sample pulse-family result.

[Kubatko and colleagues](https://doi.org/10.1016/j.jtbi.2024.111927) study speciation-time identifiability on fixed species trees with a shared population size. [Kong and colleagues](https://doi.org/10.1093/sysbio/syae054) develop a quartet site-pattern composite-likelihood method for network estimation under JC69 and a constant population size. They report a reticulation-time non-identifiability under their common-inheritance model and constrain the event age in their parameterization. The present model uses independent choices for current B blocks, two samples per species and two sites sharing a genealogy. These differences do not by themselves settle the relationship between the results; the [source comparison](KUBATKO-KONG-SITE-PATTERN-COMPARISON.md) records the reading and remaining model-mapping limits.

Other studies compare introgression directions rather than identifying parameters within one stipulated direction. [Yang and Flouri](https://doi.org/10.1093/molbev/msac083) describe a two-species case in which opposite directions can share a pair-coalescence-time law with one sequence per species, and report distinguishability with multiple sequences in their stated setting. [Thawornwattana and colleagues](https://doi.org/10.1093/molbev/msad178) study pair-time information about direction in a two-species model and separately simulate larger species sets. Their arrows denote forward-time gene flow. The respective [sampling comparison](YANG-FLOURI-2022-COMPARISON.md) and [direction comparison](THAWORNWATTANA-COMPARISON.md) record the scope and remaining model mappings; these results do not make the fixed-direction theorem a direction estimator.

For related three-taxon scenarios, [Hibbins and Hahn](https://doi.org/10.1534/genetics.118.301831) develop topology-conditioned divergence tests for timing and direction, including forward C-to-B introgression. [Pang and Zhang](https://doi.org/10.1093/sysbio/syad077) compare ghost and opposite ingroup directions using selected topology, pooled-site and pair-time summaries. Their cross-scenario questions and data differ from the present two-site parameter result. The [Hibbins–Hahn comparison](HIBBINS-HAHN-2019-COMPARISON.md) records the selected article text and incomplete model/time-unit crosswalk; the [Pang–Zhang comparison](PANG-ZHANG-2024-COMPARISON.md) records unresolved sampling and timing mappings.

Several network results use different observables or targets. [Yu, Degnan and Nakhleh](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1002660) study gene-tree topology probabilities and report that additional samples resolve parameter identifiability in a particular two-reticulation example involving extinction. The [comparison](NETWORK-COALESCENT-PRIOR-WORK.md#yu-degnan-and-nakhleh-2012-sampling-and-topology-probabilities) records its different model, a selected author-listed supplement passage and the limits of that evidence. [Zhu and Degnan](https://pubmed.ncbi.nlm.nih.gov/27780899/) study gene-tree topology distributions and exhibit cases where additional sampled lineages distinguish networks. [Allman and colleagues (2024)](https://link.springer.com/article/10.1007/s11538-024-01339-4) find that some three-cycle numerical parameters remain unidentifiable from quartet gene-tree concordance factors even with at least two samples per taxon; the [comparison](ALLMAN-ET-AL-2024-QUARTET-COMPARISON.md) records the different observable and the unresolved model crosswalk.

[Currie and colleagues](https://arxiv.org/abs/2606.26673v1) report numerical-parameter non-identifiability within a fixed three-leaf triangle model under a single-site JC distribution without coalescence. Their model and observations differ from the six-copy, shared-genealogy two-site family here; the [comparison](NETWORK-COALESCENT-PRIOR-WORK.md#currie-and-colleagues-2026-three-leaf-triangles-without-coalescence) records the limited parameter check and unresolved model mapping. Their result does not by itself establish or refute the present claim.

[Cummings and colleagues](https://arxiv.org/abs/2608.03544v1) study five-taxon concordance factors under a network coalescent, with some generic conclusions and explicitly qualified computational distinctions; their scopes and access limits are in the [comparison](NETWORK-COALESCENT-PRIOR-WORK.md). [Allman, Baños and Rhodes](https://doi.org/10.1007/s00285-022-01734-2) obtain a generic topology result under a network coalescent from sequence-derived logDet distances, suppressing 2- and 3-cycles and omitting 4-cycle directions from the identified object. Their linked-site variant pools single-site frequencies rather than using the present within-locus product; see the [source note](ALLMAN-BANOS-RHODES-2022-COMPARISON.md). A 2026 [preprint by Brits and colleagues](https://arxiv.org/abs/2607.12919v3) reports a topology result at every point of a restricted level-1 parameter space, modulo a stated triangle ambiguity. Its displayed-tree model does not include incomplete lineage sorting, and its separate tree-versus-network result is version-sensitive as recorded in the [comparison](BRITS-2026-COMPARISON.md). These results do not by themselves establish the present fixed-family numerical-parameter claim. Wider prior literature remains to be checked.

A separately retained [bounded observation bridge](BOUNDED-OBSERVATION-REUSE.md) relates finite-length JC sequence-law equality to equality of marginal timed-genealogy laws for a broader bounded pulse-network class. Its stated length is a general upper bound, not the two-site bound or a parameter-identification theorem. Its review records a scoped hand acceptance by Dot; it is not an independent human review or Lean verification.

## 2. Model, observations and notation

The species backbone is known to be `((A,B),C)`. There is one **backward B-to-C** pulse. Each species supplies two contemporaneous, phased, labelled haploid samples, with complete observation of the stated locus columns across all six sequences. The strict domain is

$$
0<h<t_1<t_0,\qquad 0<g<1,\qquad
r_A,r_B,r_C,r_{AB},r_R>0.
$$

The three event times are `h,t1,t0`, the pulse probability is `g`, and the five rates are `rA,rB,rC,rAB,rR`: nine parameters in total. In the source's diploid convention, `theta_P = 4 N_P mu` and `r_P = 2/theta_P`, where `N_P` is population size and `mu` is the mutation rate; there is no additional unknown mutation-rate multiplier. Each unordered pair of current ancestral blocks in population `P` merges at rate `r_P` in mutation-scaled time. Thus `k` current blocks in that population have combined merger rate `k(k-1)r_P/2`. [Kingman's single-population coalescent](https://www.ccg.unam.mx/~vinuesa/tlem/pdfs/Kingman_1982_Coalescent.pdf) provides the unit-rate partition-process background and a restriction property for smaller samples. Extending that property through this model's population changes and pulse requires a separate argument; the [source comparison](PAIR-PROJECTION-LUMPABILITY.md) records that boundary.

At age `h`, each current B block independently moves to C with probability `g`; existing C blocks stay in C. A previously merged block receives one routing choice. [Fogg and colleagues](https://academic.oup.com/sysbio/article/72/5/1171/7187011) distinguish independent, common and correlated inheritance; the [source comparison](PULSE-INHERITANCE-SOURCE-COMPARISON.md) explains the assumption used here. The backward B-to-C pulse represents forward C-to-B introgression and has zero duration. [Flouri and colleagues](https://pmc.ncbi.nlm.nih.gov/articles/PMC7086182/) describe same-age introgression nodes in a broader MSci setting; the comparison records the limits of this correspondence. At `t1`, A and remaining B blocks enter AB; at `t0`, AB and C enter the root population. B has rate `rB` on both `(0,h)` and `(h,t1)`; C has rate `rC` on both `(0,h)` and `(h,t0)`. These are separate ties: `rB` and `rC` may differ. The root process continues until all sampled lineages have merged. Population histories and routing flags are marginalized.

![Schematic of the backward B-to-C pulse, the A/B and root joins, and the separately tied B and C rates.](MODEL-SCHEMATIC.svg)

*Figure 1.* The fixed population history, viewed backward in time. Each current B block independently follows the pulse arrow with probability `g` or stays in B with probability `1-g`; existing C blocks remain in C. Lines represent populations, not a realized gene tree, and their lengths are schematic. The model-to-source and observation correspondences remain verification obligations.

The stationary homogeneous [Jukes–Cantor clock](https://evoluscope.fr/phylographe/biblio/JukesCantor1969.pdf) and its scale are known. In mutation-scaled time its rate matrix has diagonal entries `-1` and off-diagonal entries `1/3`, with an independently uniform root state at each site. Two sites within a locus evolve conditionally independently on the **same genealogy**; the observation model includes no within-locus genealogy switch. Different loci are independent replicates under the same parameters. Missing sites, sequencing error, ascertainment, alignment uncertainty, selection and duplication/loss are not modeled. These conditions are assumptions of the theorem, not observations established by this manuscript. The [source comparison](MODEL-CONVENTIONS-COMPARISON.md) distinguishes the selected normalization and pulse process from the foundational references.

For a selected sample pair `XY`, let `T_XY` denote its coalescence age and set `c=8/3`. The raw moments are

$$
m_{XY}(k)=\mathbb E[e^{-ckT_{XY}}],\qquad k=1,2.
$$

For nucleotide symbols, set `chi(A)=chi(C)=1` and `chi(G)=chi(T)=-1`. Here these letters denote bases, not the taxon names. For the selected two sample sequences, define `Z_XY,k = product_(s=1,...,k) chi(X_s)chi(Y_s)`, where `X_s,Y_s` are their bases at site `s`. The source's JC observation bridge gives `E[Z_XY,k]=m_XY(k)`. The shifted feature `(1+Z_XY,k)/2` is Bernoulli. The selected raw moment vector is

$$
F=(AC1,AC2,CC1,BC1,BC2,AB1,AB2,AA1,BB1).
$$

“Two sites” means two homologous columns across all six sequences. It is a sufficient observation length, not a claim of minimality or reliable estimation from one locus. Products of separately averaged site probabilities do not preserve the required shared-genealogy dependence.

[Appendix B](MANUSCRIPT.md#appendix-b-original-jacobian-and-interval-inclusion-proof) uses `a=t1`, `T=t0`, `rD=rAB` and `R=rR`. Its physical duration coordinates are `u=t1-h` and `v=t0-t1`. This is a notation crosswalk, not a different model.

### Forward pair transforms

The retained [forward interface](https://github.com/Sodelin/Research-Commons/blob/ddcb0be5339cee2bf3e26651ca13f11db185a448/research/2026-10-05-dot-msci-330-feature-forward-interface-1039z/COROLLARY.md) gives the following pair-coalescence transforms for the same source. Write $\mathcal L_{XY}(z)=\mathbb E[e^{-zT_{XY}}]$, so that the raw moments above are $m_{XY}(k)=\mathcal L_{XY}(ck)$. For $z\geq0$, define

$$
\begin{aligned}
E_x&=e^{-zx}, & S(r,\ell)&=e^{-r\ell},\\
H_z(r,\ell)&=\frac{r}{r+z}\bigl(1-e^{-(r+z)\ell}\bigr),
& R_z&=\frac{r_R}{r_R+z}.
\end{aligned}
$$

Here $H_z(r,\ell)$ is the transform contribution from a rate-$r$ merger within an interval of length $\ell$. Set $u=t_1-h$, $v=t_0-t_1$, and abbreviate

$$
b_h=S(r_B,h),\quad b_u=S(r_B,u),\quad d_v=S(r_{AB},v),\quad
c_{uv}=S(r_C,u+v),\quad a_1=S(r_A,t_1),\quad c_0=S(r_C,t_0).
$$

The six transforms are

$$
\begin{aligned}
\mathcal L_{AC}(z)&=E_{t_0}R_z,\\
\mathcal L_{AB}(z)&=(1-g)E_{t_1}H_z(r_{AB},v)
  +\bigl[g+(1-g)d_v\bigr]E_{t_0}R_z,\\
\mathcal L_{BC}(z)&=gE_hH_z(r_C,u+v)
  +\bigl[1-g+gc_{uv}\bigr]E_{t_0}R_z,\\
\mathcal L_{AA}(z)&=H_z(r_A,t_1)+a_1E_{t_1}H_z(r_{AB},v)
  +a_1d_vE_{t_0}R_z,\\
\mathcal L_{CC}(z)&=H_z(r_C,t_0)+c_0E_{t_0}R_z,\\
\mathcal L_{BB}(z)&=H_z(r_B,h)+b_h\Bigl\{
  (1-g)^2E_hH_z(r_B,u)+g^2E_hH_z(r_C,u+v)\\
 &\qquad +(1-g)^2b_uE_{t_1}H_z(r_{AB},v)\\
 &\qquad +\bigl[(1-g)^2b_ud_v+g^2c_{uv}+2g(1-g)\bigr]E_{t_0}R_z
  \Bigr\}.
\end{aligned}
$$

For BB, the first term covers merger before the pulse. Conditional on survival to the pulse, the two still-distinct B blocks both stay, both route, or split with respective weights $(1-g)^2$, $g^2$, and $2g(1-g)$. A split pair cannot meet before the root in this fixed backbone. The separate B and C rate ties across the pulse apply to their respective routes; the C-route interval extends from $h$ to $t_0$. All displayed denominators are positive on the stated domain, including when rates coincide. The [source comparison](FORWARD-SOURCE-CORRESPONDENCE.md) records the inherited formulas and the separate, still-open formal connection to the six-sample process and observation law.

## 3. Main mathematical results

**Global identification, at the retained source scope.** If two admitted parameter vectors have the same nine raw moments, they are equal. Equality of their complete two-site locus laws therefore implies parameter equality. Coincident rates do not require an exceptional stratum. [Appendix A](MANUSCRIPT.md#appendix-a-original-global-identification-proof) contains the complete hand proof and its inherited pair-law, projectivity and channel dependencies.

The reconstruction proceeds in six stages: recover the root time and rate from `AC1,AC2`; recover the C rate from `CC1`; use the BC ratio to identify the pulse time and amplitude; use the two AB moments to identify the ancestral onset and rate; and recover the A and B rates from their first moments. The AB step uses a global single-crossing argument. A local Jacobian check or a finite numerical experiment alone would not supply that global conclusion.

**Nonsingular Jacobian.** In parameter order `(T,R,rC,h,g,a,rD,rA,rB)`, the feature Jacobian is block lower triangular with block sizes `2,1,2,2,1,1`. [Appendix B](MANUSCRIPT.md#appendix-b-original-jacobian-and-interval-inclusion-proof) proves strictly positive diagonal determinants on the strict domain. Combined with global injectivity, this yields an analytic inverse on the image. It gives neither a uniform condition-number bound near the domain boundary nor feasibility of arbitrary moment vectors.

**Conservative interval inclusion.** Use the physical coordinate order `x=(h,u,v,rA,rB,rC,rD,R,g)`, with `a=h+u` and `T=h+u+v`. Let `C` be a closed convex box in these `x` coordinates, wholly inside the strict physical domain. Let `O` be an uncertain raw-moment box in the stated `F` output order, `q in C` a rational point, `Fq` a certified enclosure of `F(q)`, and `J` an entrywise enclosure of **`D_x F` over every point of `C`**, with columns ordered as `x`. For any fixed rational matrix `Y`, compute the following using **outward interval arithmetic**:

$$
K(C,O)=q-Y(Fq-O)+(I-YJ)(C-q).
$$

The displacement `C-q` and the columns of `J` use the same `x` coordinates; the preceding recovery-order `D_y F` must be transformed before it can serve as this enclosure. Every `x in C` satisfying `F(x) in O` belongs to `C intersect K(C,O)`. This is an inclusion of all compatible sources, not an existence certificate or a promise of contraction. Returning `C` unchanged is always a sound no-op fallback. With nonempty `Fq`, `O` and `J`, the exact intersection of the represented sets `C` and the `Y=0` expression equals `C` for any sound scalar backend. That set equality does not by itself prove that a particular intersection operation returns the same encoded object. With empty inputs, the result depends on the backend's conventions; the [zero-preconditioner audit](FINITE-ZERO-PRECONDITIONER.md) gives the conditions and finite-backend examples. Other boxes in a global cover cannot be discarded because one box contracted. The appendix states the derivative-enclosure and implementation obligations separately from the mathematical inclusion. The [IBEX comparison](IBEX-CONTRACTOR-COMPARISON.md) relates this inclusion to filtering; it does not establish every condition of that documentation's abstract contractor definition or an IBEX implementation.

The expression follows a parametric Krawczyk enclosure pattern. [Hansen and Sengupta](https://link.springer.com/article/10.1007/BF01933165) present a nonparametric enclosure attributed to [Krawczyk's earlier work](https://link.springer.com/article/10.1007/BF02234767) and then a distinct successive interval-Newton method. The [1981 source comparison](HANSEN-SENGUPTA-1981-COMPARISON.md) records the relation to the uncertain-target expression and the limits of the extracted-text reading. [Goldsztejn's comparison](https://arxiv.org/pdf/0811.2984v1) presents a related parametric operator with inverse-midpoint preconditioning; the present all-compatible-source inclusion follows from the pointwise identity in Appendix B for any fixed `Y`. The [source comparison](GOLDSZTEJN-COMPARISON.md) distinguishes that operator from the paper's Hansen–Sengupta theorem and its separate existence condition.

## 4. What finite data and software would still require

Exact expectations must be estimated from independent loci. For a fixed number `m >= 1` of preselected loci, let `Y_{ell,j}` be the shifted Bernoulli feature for locus `ell` and coordinate `j`, and write `mu_j=E[Y_{ell,j}]` and `bar Y_j=m^{-1} sum_ell Y_{ell,j}`. The nine coordinates within a locus may be dependent. Under the fixed common model and independent-locus assumptions, [Hoeffding's inequality](https://doi.org/10.1080/01621459.1963.10500830) and a union bound give, for `r>0`,

$$
\Pr\!\left(\max_{1\le j\le9}|\overline Y_j-\mu_j|>r\right)
\le 18e^{-2mr^2}.
$$

For a predeclared `delta` in `(0,1)`, if an outcome-independent choice of `r` satisfies `18 exp(-2mr^2) <= delta`, the nine intervals `I_j=[bar Y_j-r, bar Y_j+r] intersect [0,1]` cover all shifted means with probability at least `1-delta`. Since `F_j=2 mu_j-1` and the raw moments lie in `[0,1]` under the stated model, the corresponding input to the raw-moment contractor above is `O_j=(2 I_j-1) intersect [0,1]`. The shifted intervals and raw-moment intervals use different scales. Under the stated model, an empty `O_j` means the simultaneous coverage event has failed; it is not by itself proof that a scientific assumption is false.

The [retained confidence contract](PHASED-CONFIDENCE-REUSE.md) combines that event with a deterministic cover that preserves every compatible source in a predeclared compact physical domain containing the true parameter. Under its stated model, design and validation assumptions, the resulting cover contains the true parameter with probability at least `1-delta`. This is an unconditional guarantee under those assumptions, not coverage conditional on releasing a narrow result. A full-range confidence box and an unchanged source cover can be valid uninformative fallbacks.

The statistical statement is conditional on a fixed sampling design and complete extraction; it does not establish orthology, phasing, independence, mutation-rate calibration, absence of within-locus recombination or model fit. An invalid or unverified output is not a certificate. This edition supplies no numerical separation margin, useful locus count or empirical fit, and implements no inverse.

[Huang and colleagues](https://pubmed.ncbi.nlm.nih.gov/34143216/) studied phase-resolution strategies in simulations including a three-species introgression model and reported setting-dependent effects on parameter estimates. Their MSci simulations used 500-site loci and a different inference procedure; the [source comparison](HUANG-ET-AL-PHASING-COMPARISON.md) records the design and limits. Their results illustrate why the stated phasing assumption matters, but do not establish this manuscript's nine-feature conclusion for uncertain-phase data.

In related simulations, [Cheng and colleagues](https://doi.org/10.1093/sysbio/syag023) report that imposing one population size across species with unequal true sizes can bias gene-flow estimates. Their data and inference targets differ from the present fixed-family, two-site statement; the [comparison](CHENG-2026-TAXON-SAMPLING-COMPARISON.md) records their sampling and model scope. The result illustrates why admission of the demographic assumptions must be assessed separately from identifiability within them.

In a separate study, [Thawornwattana and colleagues](https://doi.org/10.1093/molbev/msaf121) report substantial bias in some parameters when migration is assigned to the wrong lineage in their four-species simulations. Their Bayesian full-likelihood analysis and longer loci differ from the present setting; the [comparison](THAWORNWATTANA-COMPARISON.md) records the study design and limits. The example does not quantify misspecification bias for this theorem's moment features.

A [retained historical synthetic check](HISTORICAL-SYNTHETIC-CHECK.md) reports applying a separate existing inverse to one generated 1,024-locus, six-copy example. Its known source was retained in the final cover, but the output remained `UNKNOWN` and no physical-coordinate width decreased. The finite simulator's exact independent-sampling law was not certified. One synthetic realization neither estimates coverage nor establishes biological adequacy, and this edition did not rerun it.

The contractor also needs a verified source-specific forward and derivative enclosure, outward arithmetic, an auditable preconditioner and preservation of the complete compatible-source cover. A narrow local box or nominal Newton solution is insufficient to establish a global accuracy claim. No numerical engine is executed by assembling this edition.

## 5. Evidence, attribution and limitations

The existing Research Commons card **CB-MSCI-003** records a completed scoped hand result and expressly does **not** assert complete kernel verification. The guide's **XR-MSCI-TWOSITE**, **XR-MSCI-JACOBIAN** and **XR-MSCI-CONTRACT** entries separate the exact theorem, Jacobian and conditional contractor. Their statuses are retained, not reassigned here. The historical proof headers still say “candidate”; they are preserved byte-for-byte alongside the separately dated review records and later register status.

The accompanying historical AI reviews are source records, not external journal review or a new independent correctness review by this editor. The guide reports bounded rational controls; their historical and guide-replay epochs are separate. The existing compiler owner now reports a Lean-checked **analytic formula** result: equality of the specified nine formula values implies equality of the nine admitted parameters. The [qualification record](LEAN-ANALYTIC-QUALIFICATION-20261031.md) identifies the exact selected sources, checked statement, standard axioms and reported audit limits, including the earlier two-provider execution overlap. The six-sample stochastic process and same-genealogy JC observation have not yet been formally connected to those formulas; the separate full Jacobian and interval statements also remain outside that result. This edition reruns no symbolic, Lean, Rust or biological computation and does not claim a completed Lean proof of the full biological-model theorem.

Two later scoped AI source/hand reviews by dot examined parts of the same-record genealogy selection and the conditional two-site mutation and averaging construction. They reported no mismatch within the supplied sources and stated premises; the [observation record](JC-LOCUS-BRIDGE.md#dots-r22-conditional-jc-source-review) identifies the reviewed bodies and remaining helper, physical-model and compiler gaps. These are not independent human reviews or a complete proof of the observation correspondence.

Further scoped AI source reviews found no mathematical mismatch, under their stated premises, in a fixed-phase first-merger and continued-trace join, in retaining the first-interval record with its matching pulse suffix, and in the almost-sure pulse-time/fifth-boundary identity on the selected record. The later joint-output argument also received a scoped source review. The [recorded-history note](JC-LOCUS-BRIDGE.md#first-join-needs-the-event-history) distinguishes these conditional arguments from constructing a timed genealogy and identifying the physical pulse. Their candidate Lean files and dependencies have not been checked by the compiler owner; these reviews do not establish the complete model or replace human expert review.

A scoped source-to-text consistency review was completed for the predecessor edition at commit `38f4f693b5c200f237f1d56d20ae80d5b7370528`. This successor retains the original proof and review bodies and adds source-backed context and forward formulas; the predecessor review does not cover those later additions. Scientific expert review, a current prior-art assessment, author/rights decisions and publication formatting remain open. The [source package](../PACKAGES.json) records the exact source bytes, hashes, original URLs and discovery IDs. No research data, private runtime records, credentials or original media are included.

## 6. Reading and source order

This principal text is also included at the start of the [combined manuscript](MANUSCRIPT.md). Follow the appendices for the retained sources:

| Source | What it contains |
| --- | --- |
| [Appendix A: global-identification proof](MANUSCRIPT.md#appendix-a-original-global-identification-proof) | The fixed-family, nine-feature hand argument and its inherited dependencies. |
| [Appendix B: Jacobian and interval-inclusion proof](MANUSCRIPT.md#appendix-b-original-jacobian-and-interval-inclusion-proof) | The derivative argument and conditional inclusion for uncertain targets. |
| [Appendix C: historical review of A](MANUSCRIPT.md#appendix-c-historical-review-of-appendix-a) | The source review's stated scope and limitations. |
| [Appendix D: historical review of B](MANUSCRIPT.md#appendix-d-historical-review-of-appendix-b) | The source review's stated scope and limitations. |

Each appendix preserves its original source, including its title, headings and historical status. The historical AI review records are not separate human reviews. The original provider and literature links remain in each proof. This is one assembled reading edition of existing work, not two new discoveries or a complete bioinformatics pipeline.

## References

- Elizabeth S. Allman, Hector Baños and John A. Rhodes. “Identifiability of species network topologies from genomic sequences using the logDet distance.” *Journal of Mathematical Biology* 84, 35 (2022), [doi:10.1007/s00285-022-01734-2](https://doi.org/10.1007/s00285-022-01734-2).
- Elizabeth S. Allman, Hector Baños, Marina Garrote-Lopez and John A. Rhodes. “Identifiability of Level-1 Species Networks from Gene Tree Quartets.” *Bulletin of Mathematical Biology* 86, 110 (2024), [doi:10.1007/s11538-024-01339-4](https://doi.org/10.1007/s11538-024-01339-4).
- Jari Brits, Niels Holtgrefe, Leo van Iersel and Samuel Martin. “On Tree-Network Distinguishability and Full Identifiability of Phylogenetic Networks.” [arXiv:2607.12919v3](https://arxiv.org/abs/2607.12919v3), 2026.
- Sirui Cheng, Tomáš Flouri, Tianqi Zhu and Ziheng Yang. “The Impact of Incomplete Taxon Sampling on Inference of Gene Flow by Bayesian and Summary Methods Using Genomic Sequence Data.” *Systematic Biology* 75(6), 1097–1119, 2026. [doi:10.1093/sysbio/syag023](https://doi.org/10.1093/sysbio/syag023).
- Joseph Cummings, Maize Curiel, Bryan Currie, Bryson Kagy, Udani Ranasinghe and John A. Rhodes. “Identifiability of phylogenetic networks and quintet concordance factors.” [arXiv:2608.03544v1](https://arxiv.org/abs/2608.03544v1), 2026.
- Bryan Currie, Aviva K. Englander, Jose A. Esparza-Lozano, Elizabeth Gross, Max Hill, Colby Long, Devon Olds, Kawika O'Connor, Udani Ranasinghe and Christin Sum. “Semialgebraic Conditions for Identifying Triangles in Phylogenetic Networks.” [arXiv:2606.26673v1](https://arxiv.org/abs/2606.26673v1), 2026.
- Chris Durden and Seth Sullivant. “Identifiability of Phylogenetic Parameters from k-mer Data Under the Coalescent.” *Bulletin of Mathematical Biology* 81, 431–451 (2019), [doi:10.1007/s11538-018-0399-1](https://doi.org/10.1007/s11538-018-0399-1). The compared preprint is [arXiv:1705.06993v1](https://arxiv.org/abs/1705.06993v1).
- Tomáš Flouri, Xiyun Jiao, Bruce Rannala and Ziheng Yang. “A Bayesian Implementation of the Multispecies Coalescent Model with Introgression for Phylogenomic Analysis.” *Molecular Biology and Evolution* 37(4), 1211–1223, 2020. [doi:10.1093/molbev/msz296](https://doi.org/10.1093/molbev/msz296); [supplement correction](https://doi.org/10.1093/molbev/msac245), 2022.
- John Fogg, Elizabeth S. Allman and Cécile Ané. “PhyloCoalSimulations: A Simulator for Network Multispecies Coalescent Models, Including a New Extension for the Inheritance of Gene Flow.” *Systematic Biology* 72(5), 1171–1179, 2023. [doi:10.1093/sysbio/syad030](https://doi.org/10.1093/sysbio/syad030).
- Alexandre Goldsztejn. “Sensitivity Analysis Using a Fixed Point Interval Iteration.” [arXiv:0811.2984v1](https://arxiv.org/abs/0811.2984v1), 2008.
- Eldon Hansen and Saumyendra Sengupta. “Bounding solutions of systems of equations using interval analysis.” *BIT Numerical Mathematics* 21, 203–211, 1981. [doi:10.1007/BF01933165](https://link.springer.com/article/10.1007/BF01933165).
- Mark S. Hibbins and Matthew W. Hahn. “The Timing and Direction of Introgression Under the Multispecies Network Coalescent.” *Genetics* 211(3), 1059–1073, 2019. [doi:10.1534/genetics.118.301831](https://doi.org/10.1534/genetics.118.301831).
- Wassily Hoeffding. “Probability Inequalities for Sums of Bounded Random Variables.” *Journal of the American Statistical Association* 58(301), 13–30, 1963. [doi:10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830).
- Jun Huang, Jeremy Bennett, Tomáš Flouri, Adam D. Leaché and Ziheng Yang. “Phase Resolution of Heterozygous Sites in Diploid Genomes is Important to Phylogenomic Analysis under the Multispecies Coalescent Model.” *Systematic Biology* 71(2), 334–352, 2022. [doi:10.1093/sysbio/syab047](https://doi.org/10.1093/sysbio/syab047).
- Thomas H. Jukes and Charles R. Cantor. “[Evolution of Protein Molecules](https://evoluscope.fr/phylographe/biblio/JukesCantor1969.pdf).” In H. N. Munro, ed., *Mammalian Protein Metabolism*, vol. III, 21–132, 1969.
- J. F. C. Kingman. “[The Coalescent](https://www.ccg.unam.mx/~vinuesa/tlem/pdfs/Kingman_1982_Coalescent.pdf).” *Stochastic Processes and their Applications* 13, 235–248, 1982.
- Sungsik Kong, David L. Swofford and Laura S. Kubatko. “Inference of Phylogenetic Networks From Sequence Data Using Composite Likelihood.” *Systematic Biology* 74(1), 53–69, 2025. [doi:10.1093/sysbio/syae054](https://doi.org/10.1093/sysbio/syae054).
- R. Krawczyk. “Newton-Algorithmen zur Bestimmung von Nullstellen mit Fehlerschranken.” *Computing* 4, 187–201, 1969. [doi:10.1007/BF02234767](https://link.springer.com/article/10.1007/BF02234767).
- Laura Kubatko, Alexander Leonard and Julia Chifman. “Identifiability of speciation times under the multispecies coalescent.” *Journal of Theoretical Biology* 595, 111927, 2024. [doi:10.1016/j.jtbi.2024.111927](https://doi.org/10.1016/j.jtbi.2024.111927).
- Xiao-Xu Pang and Da-Yong Zhang. “Detection of Ghost Introgression Requires Exploiting Topological and Branch Length Information.” *Systematic Biology* 73(1), 207–222, 2024. [doi:10.1093/sysbio/syad077](https://doi.org/10.1093/sysbio/syad077).
- Yuttapong Thawornwattana, Jun Huang, Tomáš Flouri, James Mallet and Ziheng Yang. “Inferring the Direction of Introgression Using Genomic Sequence Data.” *Molecular Biology and Evolution* 40(8), msad178, 2023. [doi:10.1093/molbev/msad178](https://doi.org/10.1093/molbev/msad178).
- Yuttapong Thawornwattana, Tomáš Flouri, James Mallet and Ziheng Yang. “Inference of Gene Flow between Species from Genomic Data When the Mode, Direction, and Lineages are Misspecified.” *Molecular Biology and Evolution* 42(6), msaf121, 2025. [doi:10.1093/molbev/msaf121](https://doi.org/10.1093/molbev/msaf121).
- Ziheng Yang and Tomáš Flouri. “Estimation of Cross-Species Introgression Rates Using Genomic Data Despite Model Unidentifiability.” *Molecular Biology and Evolution* 39(5), msac083, 2022. [doi:10.1093/molbev/msac083](https://doi.org/10.1093/molbev/msac083).
- Yun Yu, James H. Degnan and Luay Nakhleh. “The Probability of a Gene Tree Topology within a Phylogenetic Network with Applications to Hybridization Detection.” *PLOS Genetics* 8(4), e1002660, 2012. [doi:10.1371/journal.pgen.1002660](https://doi.org/10.1371/journal.pgen.1002660).
- Sha Zhu and James H. Degnan. “Displayed Trees Do Not Determine Distinguishability Under the Network Multispecies Coalescent.” *Systematic Biology* 66, 283–298 (2017), [doi:10.1093/sysbio/syw097](https://doi.org/10.1093/sysbio/syw097).
- Tianqi Zhu and Ziheng Yang. “Complexity of the simplest species tree problem.” *Molecular Biology and Evolution* 38(9), 3993–4009, 2021. [doi:10.1093/molbev/msab009](https://doi.org/10.1093/molbev/msab009).

This list covers the external articles and preprints cited in the principal text. Public project sources are linked in the text, and the retained appendices contain their own original provider and method references; this list is not an exhaustive prior-art assessment.
