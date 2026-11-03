# Two observations do not make hidden probabilities deterministic

**Working expository manuscript · 3 November 2026**

This note explains an existing AI-assisted project counterexample for
discussion. It is an abstract probability example, not a new biological
finding, a submitted preprint or a claim of historical novelty. Sodelin is
organizing the research and seeking collaboration; the human contribution
record, authorship and rights for an eventual publication remain open.

## Abstract

A small number of observations may be linear functions of a full probability
law while being nonlinear functions of the parameters of an independent
product law. We give two simple expected observations that constrain every
one of arbitrarily many Bernoulli probabilities to lie strictly between zero
and one. Thus a bound on the number of informative affine observations cannot
by itself be used as a bound on the number of non-deterministic factors in a
fitting product law. The example does not contradict a policy theorem whose
conclusion concerns queries rather than factors.

## 1. Two observations of three independent coins

Let `B₁`, `B₂` and `B₃` be independent Bernoulli variables with
probabilities `p₁`, `p₂` and `p₃`, and put `N = B₁ + B₂ + B₃`. Consider
the expected count and expected number of pairs:

\[
  f_1=\mathbb E[N]=p_1+p_2+p_3,\qquad
  f_2=\mathbb E\!\binom{N}{2}=p_1p_2+p_1p_3+p_2p_3.
\]

Both are linear in the **full joint law** of the three bits. The second is
not linear in the individual product parameters. Suppose a product law has
`f₁ = 3/2` and `f₂ = 37/50`. The probabilities `(3/5, 2/5, 1/2)` supply
one such law.

**Proposition.** Every product law with these two observations has all three
probabilities strictly between zero and one. Its parameter fibre is a regular
circle contained in the interior of the cube.

**Proof.** From the two observations,

\[
  \sum_i p_i^2=f_1^2-2f_2=\frac{77}{100},\qquad
  \sum_i\left(p_i-\frac12\right)^2=\frac1{50}.
\]

Consequently `|pᵢ − 1/2| ≤ 1/√50 < 1/2` for each `i`; none of the three
coins is deterministic. The equations describe the intersection of a sphere
of positive radius about `(1/2,1/2,1/2)` with the plane
`p₁+p₂+p₃=3/2`. That intersection is a circle, entirely inside the cube.
The two gradient rows are `(1,1,1)` and `(3/2−p₁,3/2−p₂,3/2−p₃)` on the
fibre. If they were dependent, all `pᵢ` would equal `1/2`, contradicting
the positive radius. Thus the fibre is regular. ∎

An unrestricted joint law can match the same two expectations using only
three outcomes: assign probabilities `6/25`, `1/50` and `37/50` to `000`,
`100` and `110`, respectively. It is not a product law: its second bit is
one only when the first is one, although each of those bits has a positive
probability of either value. A support bound for an arbitrary joint law
therefore does not establish a deterministic-coordinate bound for an
independent product law.

## 2. Arbitrarily many fixed product factors

For any integer `n ≥ 3`, take independent Bernoulli variables with
probabilities `p₁,…,pₙ`, and set

\[
  f_1=\frac n2,\qquad
  f_2=\frac{n(n-1)}8-\frac1{100}.
\]

The same identity gives `Σᵢ(pᵢ − 1/2)² = 1/50`, so every `pᵢ` is strictly
between zero and one. The choice `p₁=3/5`, `p₂=2/5` and all remaining
probabilities `1/2` shows the constraints are attainable for every such
`n`. There are still only two expected features, but all `n` fixed product
positions remain non-deterministic. The target values and the number of
positions vary with `n`; this is not a single fixed target requiring an
unbounded architecture.

## 3. Why this does not refute the policy result

The existing G7 rank argument concerns the number of **informative exact-law
queries** under its particular affine-response, reset and deletion-closed
cost assumptions, with the same unknown source retained across calls. A
response whose linear coefficient is dependent on
earlier coefficients can be reconstructed from previous exact replies and
known offsets, allowing the query to be simulated. That operation is different
from changing the underlying independent factors to deterministic values.
Neither the example above nor the query bound establishes a biological
observation menu, a source-size cutoff or an unrestricted network theorem.

The guide records a related original-family Lean endpoint whose hypothesis
is a correct total policy for every admitted source and whose conclusion is a
bounded plan. The recorded endpoint also has finite-carrier and source
assumptions; it does not supply general source admission, a native policy
implementation or this note's product-factor conclusion. This note does not
claim a new Lean check of the example.

## 4. Source and review status

The example and its generalization restate Full Pro's
`attacks/AFFINE-POLICY-DOES-NOT-PURIFY-PRODUCT-COINS.md` at local library
commit `1ac9c42ca8c029d2af6b068c0015b794a7a1eee0`: 4,035 bytes/SHA-256
`a91416fd34b972d8c00186cd3bf93fe3b98cb1134219918f5a27802547d294af`.
Its preparation header recorded a pending review at that earlier point.
The later Dot/OpenAI hand review in the same selected library,
`sources/reviews/DOT-CHEBYSHEV-RESPONSE-SINGULAR-0329Z.md`, 15,507
bytes/SHA-256
`852842e05fd373d7dd837971fabe38f65588c83d9646de5582f68b1867770576`,
independently checks this auxiliary example at its stated abstract scope.
That AI review is not external human peer review, a new Lean run or a review
of every claim in the larger programme.

The separate [G7 hand master review](https://github.com/Sodelin/Research-Commons/blob/539c814ac470fde8147b0e1e6d5307972585b6f8/research/2026-10-01-sol61-head-audit-1956z/G7-EXACT-MASTER-REVIEW.md)
describes the exact-law rank argument and its source/resource assumptions.
The dated guide's retained Lean-binding record identifies
`GProgram.G7.OriginalFamilyStrategy.actual_total_original_strategy_has_bounded_plan`
in module `G7OriginalFamilyStrategy` at source SHA-256
`1a95edf6b4a0e361ccc053531fd24de4de45b6253a139b266e68d282c3fbecd5`;
its bound and scope are recorded separately from the hand argument above.
This edition has not independently rerun Lean, verified the full source
closure, established current prior art or received human scientific review.
The cited public link has not been freshly checked for availability. Source
sharing, attribution and publication decisions remain open.

The [exact arithmetic check](check_examples.py) verifies the displayed
three-coin comparison and four finite product witnesses. It does not prove
the general statement or check a Lean theorem.
