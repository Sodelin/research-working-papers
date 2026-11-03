# Reaction observations: what conservation, timing and hidden history identify

The retained reaction work gives exact special cases for a published partial-observation direction and explicit reasons why those cases do not solve arbitrary hidden reaction networks. Its main uses are choosing preparations/readouts that can distinguish sources, describing observational equivalence, and checking that an inference claim uses the right initial-state and stopping quantifiers.

This Codex/OpenAI synthesis reads four selected guides, the complete original pointwise-quantifier checkpoint and selected opening/proof sections of two specialization manuscripts. Historical mathematical acceptance is attributed AI hand review, not independent human review or a compiled stochastic proof. No reaction model, solver, compiler or owner job ran here.

## The external direction and the exact special case

Faul, Hoessly and Xia's reaction-SDE article explicitly names partial species observation and discrete-time data as further directions. Its Section 6 also distinguishes identifiability from successful parameter estimation. The retained results are restricted contributions to that direction, not a general solution. [Primary conclusion](https://www.cambridge.org/core/journals/european-journal-of-applied-mathematics/article/identifiability-of-sdes-for-reaction-networks/7D2B84958974B0400D0DAC737FF823F2).

The two-species specialization allows finitely many unit-transfer reactions with nonnegative finite intensity polynomials P(a,b),Q(a,b), no duplicate source/direction reactions and one common rate bank. A known controlled total C=a+b makes the hidden coordinate reconstructible. Each experiment starts at (C/2,C/2), stops the observed coordinate on leaving (C/4,3C/4), and holds it thereafter. Exact stopped path laws are the data.

Under that source contract, matching one total means both polynomial differences are divisible by a+b−C. A panel of distinct totals imposes the product of those factors. If both sources have molecularity degree at most D≥1, D distinct totals are worst-case sufficient and fewer do not uniformly suffice. For a nonempty target with r active **total degrees**, the retained positive-support argument supplies a specified 2r+1-total certificate against all finite-degree rivals. Here r is not the number of reactions, and a total experiment is not one noisy trajectory.

The separate two-time hand theorem retains the same scalar positivity and stop/hold protocol and uses the **exact joint law** at Δ and 2Δ. Its extraction of the killed transition kernel and scalar spectral argument transport the same fibre conclusion. Two independent marginals, two realized measurements or an unmonitored diffusion that can leave and re-enter the interval are different observations. Classical scalar spectral identification retains its prior attribution; no new general hidden-state spectral algorithm is claimed.

## Hidden species can be identifiable, exchangeable or invisible

The controlled-total argument works because the hidden coordinate is reconstructed. Three-species conservation leaves more freedom. The retained examples separate several outcomes:

- In a known three-reaction catalytic graph with unknown hidden initial abundance, observed-path quadratic and cross variations plus a law-level localized drift identify the three rates and hidden start under the specified stop. These are exact continuous-law functionals, not numerical derivatives of one noisy trace.
- In a neutral family, equal visible-to-hidden couplings leave the hidden exchange rate arbitrary. Unequal couplings identify the labelled rates when hidden initial masses differ; equal hidden masses leave a label swap. The explicit inversions divide by a quantity proportional to the squared coupling difference and cannot be used on its zero stratum.
- In a distinct balanced tied-rate family, hidden exchange rates do not affect the observed drift or variance at all. One fixed same-family pair matches every known-total/initial-state panel. Adding a joint second-species record can distinguish that family, but this is not a universal minimum-measurement theorem.

The target matters. For arbitrary jump sizes, drift and covariance may agree for different positive reaction-rate lists. Thus identifying a scalar diffusion-law class need not identify its reaction graph or individual rates. Changing from diffusion approximations to discrete jump trajectories also changes the inference contract.

## Preserve the actual stop and the full observed history

The stopped-likelihood source gives a useful pairwise criterion: if one full stopped path law has density Z relative to another, equal observed laws mean its conditional expectation given the actual observation is one. A pairwise mixture yields a domination-free version. These are measure identities, not an algorithm for conditional densities of arbitrary unknown hidden sources.

A retained example has equal visible laws but mutually singular labelled full diffusion laws. It demonstrates why an all-rival method cannot simply require a shared full-law density. Separately, an independent hidden-block construction reduces equality of the held visible path laws to equality of the hidden block's fixed-start exit-survival response over the declared horizon. The hidden chemical source supplies that exit clock. Classifying all finite admitted hidden blocks with the same killed-semigroup response remains a precise missing supplier; no finite-rank, hidden-size or all-start oracle is supplied.

Stopping at hidden full-state exit and stopping on a visible interval are different experiments. The visible coordinate can also be non-Markov in some retained examples, while being Markov in the conservation-reconstructed or balanced cases. A scalar Markov theorem therefore needs an actual source-specific justification.

## A potential quantifier correction is a separate review item

The publisher's Definition 3.2 uses every initial state, while its generator comparison concerns coefficients over open sets. The retained [pointwise checkpoint](https://github.com/Sodelin/Research-Commons/blob/27b143c73a4ac272b560b2974d83ff96df738531/research/2026-10-22-dot-reaction-partial-observation/POINTWISE-QUANTIFIER-CHECK.md) supplies positive rate vectors (2,1,1) and (1,2,2) for three reactions with intensity difference `a(a+b−1)`. On the conserved line a+b=1 their stopped laws coincide under the source's local uniqueness argument, although the generators differ elsewhere. This is a potential issue for the literal pointwise implication, not a rejection of the valid all-start-family generator criterion. The source has limited coordinating AI hand review, no acknowledged erratum or author resolution. [Primary definition and Proposition 7.1](https://www.cambridge.org/core/journals/european-journal-of-applied-mathematics/article/identifiability-of-sdes-for-reaction-networks/7D2B84958974B0400D0DAC737FF823F2).

A separate cone-quantifier diagnostic and the guide's parameter-family extension have weaker review status and must not borrow that checkpoint's acceptance. Conservation ambiguity itself has prior literature. Browning and coauthors also analyze partially observed near-linear SDEs through moment recurrences and explicitly discuss initial conditions; that is related prior work with its own model assumptions. [Primary abstract](https://arxiv.org/abs/2503.19241v3).

## Concrete receiver and next obligations

An experimental-design consumer can use the [receiver register](REACTION-OBSERVATION-REGISTER.json) to identify whether it has controlled known totals, reconstructible hidden state, an exact joint law, a known graph or a restricted hidden family. It can then select a supported fibre/certificate statement and keep unsupported conclusions unknown.

A practical implementation still needs a finite-data observation model, calibrated stopping/preparation, dependence and measurement error, effective representation of law functionals, source/parameter admission and checked numerical code. The external Julia/JuMP/Gurobi source described in the retained guide is neither a deployed phone Rust solver nor an implementation of these hidden-stop results. Its source rights and availability need separate verification before reuse.

These are source-backed special cases, obstructions and review questions. They establish no kinetic measurements, clinical effects, general hidden-network solution, external expert acceptance or new build.


The [programme chapter](programme/08-SOURCE-AND-OBSERVATION-ADAPTERS.md) gives related selected source statements and named components. This reading guide is an adaptation of the source recorded in [provenance](../PROVENANCE.md); it is not an independent proof audit.
