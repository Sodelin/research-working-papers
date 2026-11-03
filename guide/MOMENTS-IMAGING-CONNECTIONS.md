# Exact identification, noisy observations and the remaining imaging task

The retained work supplies three different things: an exact positive-moment component, a source-specific Fourier–Poisson decision baseline, and a compatible-set interface for scientific targets. Their useful next tasks differ. None is a full solution of noisy crystallographic reconstruction, a validated molecular-presence claim or a new general theory of moments.

This synthesis is authored by Codex/OpenAI. Sodelin is the organizer; original mathematical sources retain their own attribution, including the stated AI authorship and review status. No independent human specialist review is claimed.

| Retained result | Concrete use | Relevant external task | Remaining bridge or question |
| --- | --- | --- | --- |
| Positive sparse moments | Exclude an atomic law with more support values than a specified positive target law using a finite exact moment menu | Finite-mixture identification and moment-based source discrimination | Derive one fixed pushforward law for the scientific rows; then quantify stability under actual observation error, with explicit separation and weight assumptions |
| Binary Fourier–Poisson baseline | Separate an irreducible exact-intensity ambiguity floor from additional counting-noise error | The information-theoretic Poisson-noise direction in Bendory–Edidin–Gonzalez, Section 6.2(3) | Sharper, loss-sensitive and preferably matching photon-budget bounds; ambiguity-floor asymptotics; computational cost treated separately |
| Diffraction compatible sets | Certify only targets shared by all physically admitted states compatible with the data/error contract | Reliable molecular attribution with nuisance parameters and imperfect templates | Recover actual arrays, column provenance and admissibility rules, then justify uncertainty and computation; the abstract implication does not supply those inputs |

## What the positive-moment component establishes

For a finite probability law τ with r distinct strictly positive support nodes and strictly positive weights, the historically checked component states that equality of any 2r+1 distinct natural-exponent moments with another such finite positive law σ forces support-cardinality(σ) ≤ r. Nodes need not lie below one. Equal image values must first be grouped; zero-mass inputs are omitted. A positive-mass node at zero does not satisfy the positive-node interface.

The five-exponent special case is {0,1,3,6,10}. In a physical row indexed by k with exponent k choose 2, these are levels k=1,…,5. It is invalid to replace the actual index conversion by consecutive exponents or to count source configurations as distinct scalar nodes. The further equality-of-measures consequence is a guide derivation, not a separately named audited endpoint. The four selected Lean modules have historical scoped serial-elaboration evidence; no fresh compiler or full build-closure audit ran here.

The fixed-law adapter is substantive. A finite PMF p on I and a positive-on-support scalar map x give grouped weights W(s)=Σ_{i:x(i)=s}p(i), with all moments taken under this same pushforward law. Fixing p while changing x between rows does not suffice. The retained finite control has first moment 3/4 in one row and third moment 1/8 in another, violating the common-law requirement E[X³]≥E[X]³=27/64. It is an interface counterexample, not a demonstrated physical model failure. Typed composition of the source-specific positive-support/grouping ingredients with the abstract moment component remains uncompiled.

Exact identification also differs from robust support counting. The retained example compares δ_(1/2) with the equal mixture at 1/2±d. Every fixed finite moment vector converges as d→0 although the latent measures have total variation one and different support counts. If each independently drawn latent P is observed through one Bernoulli trial, both examples induce the same law. Two trials on that same latent draw yield distinct laws, but uniform fixed-sample support-count testing still requires a separation condition. The source's elementary two-point family has sample order d⁻⁴ for a fixed target error; that is not a theorem for arbitrary mixtures or biological experiments.

This distinction connects to existing mixture-estimation research without claiming a new solution of it. Vinayak, Kong, Valiant and Kakade study estimation of the latent distribution from grouped binomial observations under earth-mover loss. Their objective differs from exact support-count certification. Their paper supplies relevant statistical prior work, not an automatic observation model or theorem for the retained scientific sources. [Primary PMLR record](https://proceedings.mlr.press/v97/vinayak19a.html).

## The Fourier–Poisson connection is specific and useful

Bendory, Edidin and Gonzalez explicitly identify optimal expected error under Poisson noise as a future research direction; the paper credits the questions in that section to an anonymous referee's remarks. The retained baseline addresses one declared binary finite-group version of that direction; this source comparison does not establish present-day open status or priority. [Primary paper, Section 6.2](https://arxiv.org/html/2301.10647v2#S6.SS2).

Let G be a finite abelian grid of size N≥1, X a nonempty subset of {−1,+1}^G, and Γ a declared finite group preserving X, Hamming distances and each **labelled** Fourier intensity. Set p_x(k)=|DFT(x)(k)|²/N², summing to one. Independent counts obey K_k∼Poisson(Bp_x(k)), with full detector, known exposure and zero background. Actions are all declared orbits X/Γ, loss is normalized orbit Hamming distance, and randomized actions are allowed. Detector rotations that merely permute labelled bins need a different declared convention.

The retained result distinguishes R_B, the count-experiment minimax expected loss, from R_∞, the worst exact-intensity-fibre minimax radius. R_B≥R_∞ for every budget: identical intensity vectors induce identical count laws. Half a fibre diameter is a lower bound rather than a universal formula for a multi-orbit radius.

If M is the number of distinct intensities and Δ_N their minimum squared Hellinger separation, finite maximum-likelihood selection followed by a fibre minimax action gives

`0 ≤ R_B−R_∞ ≤ min{1,(M−1) exp(−BΔ_N/2)}`.

For distinct binary intensity vectors the source's integer-autocorrelation argument gives Δ_N≥4/N³. Since M≤2^N, the retained sufficient budget is

`B ≥ (N³/2)[N log 2 + log(1/δ)]`, for excess risk at most δ∈(0,1).

When M=1 the excess is zero. This already supplies a uniform polynomial sufficient budget under the stated model; “prove that some polynomial budget exists” is therefore not an unresolved achievement here. It does not establish optimal expected error or an efficient reconstruction. The catalogue search can be exponential. Neither computational efficiency nor a matching N⁴ lower bound follows. The argument uses classical Fourier, affinity and finite-testing tools, with no historical invention claim.

For the full cyclic binary model at N=12 with translation, reversal and global sign treated as equivalences, the guide's retained exhaustive finite control finds an exact ambiguity floor 1/12. This is a finite source calculation, not a general floor classification or a physical measurement. A further odd-order improvement is a guide-derived corollary awaiting independent review; it is not required for the baseline above and is not silently promoted to a checked Lean result.

The next useful research deliverable is a precisely stated sharper loss-sensitive excess-risk bound, with corresponding lower bounds or a documented gap, under a chosen sequence of classes X_N and groups Γ_N. A tractable reconstruction implementation is a separate deliverable, requiring representation and resource evidence. A realistic detector, background or exposure model is yet another adapter. No new proof or model run is requested by identifying these tasks.

## Compatible-set certification does not substitute for physical inputs

For observed bins y, molecular templates S, nuisance matrix N=[1,h] and admitted physical states θ=(a,ν), the declared map is F(θ)=Sa+Nν. If the true state belongs to C_ε(y)={θ:‖y−F(θ)‖≤ε} and the target image H(C_ε(y)) is a nonempty singleton, that target is certified. Empty compatibility is an admission/model/computation failure; it does not choose a label. A fitted AIC score alone is not this certificate.

Unrestricted Euclidean nuisance elimination projects **both** observations and every template off col(N). Constrained or coupled nuisance coefficients make unrestricted projection a relaxation. Separate per-channel nuisance witnesses need not have one common joint witness. Strict wrong-label-distance inequalities certify exclusion; equality requires checking attainment. Solver failure or timeout is UNKNOWN, not infeasibility.

The retained Bradford-study audit lacks fit-ready observation and helium vectors, actual template intensity columns, the fit grid/mask, column-to-geometry mapping, complete selection rules and a calibrated error model. The reported `4merE` table and `4merI` narrative/supplement readings remain distinct provenance branches, rather than an established scientific error. No fit, author contact or new physical conclusion occurred in this assessment. The framework makes the missing evidence precise; it does not establish molecular presence from labels or pictures.

## Evidence and completion criteria

The original Fourier dossier was anonymously fetched in this assessment: HTTP 200, 13,163 bytes, SHA-256 `5d2bd1cf8f300caefa6f8780ca23d2ef824d5529a64697803f64d6d4ff2c5465`, identical to the selected local source. Embedded document targets were not followed. The [reading copy](sources/FOURIER-POISSON-READING.md) omits the original navigation block, including two link values whose target visibility was not established; the mathematical body remains unchanged. Availability is not correctness, a blanket license or human review. Its attribution and source-specific hand-review limits remain.

The selected moment component has a [public source certificate](https://github.com/Sodelin/Research-Commons/blob/514648b697aeed8f46582109cfeefcd7707cd738/research/2026-10-15-common-moment-checked-component/CM-T02-CERTIFICATE-001.json); the [conditional diffraction certificate](https://github.com/Sodelin/Research-Commons/blob/6a7d50f699245c87727961f59808c1ec0c9adfe5/research/2026-10-16-ge-diffraction-certification/CONDITIONAL-CERTIFICATE-01.md) gives the physical-interface assumptions. Their availability is not a new proof audit. The local source assessment distinguishes its reads from historical finite controls and compiler evidence; the source identities are recorded in the collection provenance. No new arithmetic-control replay, scientific solver, Lean build, dataset processing or empirical validation occurred.

For any proposed further manuscript or funded project, completion should mean: an exact source model and target/loss; a reviewed claim with classical suppliers and prior cases credited; a proof or checked certificate for each new bridge; honest computational/precision/resource limits; public source and attribution selection; and an accountable collaboration with explicit publication and compensation terms. None of those outcomes is promised by a possible future result.
