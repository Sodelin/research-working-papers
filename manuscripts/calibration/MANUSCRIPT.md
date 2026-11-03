# Distinguishing an impossible event from a rare event

**Working expository manuscript · 2 November 2026**

This note assembles an existing AI-assisted project argument for discussion.
It is not a new scientific discovery, a submitted preprint, or an independently
peer-reviewed paper. Sodelin is organizing the research and seeking
collaboration; the human contribution record, scientific authorship, rights
and any eventual author list remain to be determined. The proof and selected
formal evidence are attributed to their source records below.

## Abstract

An event that has not appeared in a finite sample may be impossible or merely
rare. We give the exact optimal errors for a restricted binary testing problem:
one model always produces zero, while the other produces independent ones
with a known, fixed probability. The optimal sum of the two error probabilities
is the chance of an all-zero sample under the alternative; the optimal worst
error is that chance divided by one plus itself. Both bounds are attained,
including for an empty sample. The result quantifies finite-sample uncertainty
under explicit assumptions and does not decide the corresponding question
for arbitrary biological histories or imperfect observation.

## 1. Model and result

Let `n ≥ 0`. We observe the complete sequence of `n` binary trials. Under
model `M₀`, every trial is zero. Under model `Mₑ`, the trials are independent
and each is one with the same known probability `e`, where `0 < e < 1`.
The same decision rule is used under both models; it may randomize on the
entire observed sequence.

Write `α` for the probability of choosing `Mₑ` under `M₀`, and `β` for the
probability of choosing `M₀` under `Mₑ`. Define

\[
q=(1-e)^n.
\]

**Proposition.** Over all such randomized decisions,

\[
\min(\alpha+\beta)=q,\qquad
\min\max(\alpha,\beta)=\frac{q}{1+q},\qquad
\min\frac{\alpha+\beta}{2}=\frac q2.
\]

These are different optimization criteria. The first and third use the
same attaining rule; the second generally uses a different randomized rule.

## 2. Proof

Let `a` be the probability that the decision chooses `Mₑ` after observing
the all-zero sequence. This sequence is certain under `M₀` and has
probability `q` under `Mₑ`. Consequently

\[
\alpha=a,\qquad \beta\ge q(1-a).
\]

Since `0 ≤ q ≤ 1`, every decision satisfies

\[
\alpha+\beta\ge q+(1-q)a\ge q.
\]

Equality is attained by choosing `Mₑ` whenever a one appears and choosing
`M₀` on the all-zero sequence. Dividing the sharp sum by two gives the
equal-prior average-error result.

For worst error, if `a ≥ q/(1+q)`, then `α` is at least that value. If
`a < q/(1+q)`, the lower bound on `β` is strictly greater than that value.
Thus every rule has worst error at least `q/(1+q)`. Choose `Mₑ` whenever a
one appears, and choose `Mₑ` with probability `q/(1+q)` on all zeros. Then
both errors equal `q/(1+q)`, proving sharpness. The argument includes
`n = 0`, where `q = 1` and the optimal worst error is `1/2`. ∎

## 3. Consequences and limits

For fixed positive `e`, the errors can approach zero as `n` grows, but
`q > 0` at every finite `n`. The two full observation laws are distinct;
the limitation is finite-sample uncertainty, not equality of those laws.
If arbitrarily small positive rates are allowed, `q` can be arbitrarily
close to one, so no fixed finite-sample procedure has a uniform worst-error
guarantee below `1/2` across that class.

If a separate assumption supplies a lower bound `e_min > 0` for the rate
whenever the event is possible, then the probability of seeing no event
under the alternative is at most `(1 − e_min)^n`. This gives a chosen error
bound, not certainty that an unseen event is physically impossible. Dependent
trials, unknown rates, missed observations, path-dependent models and
experimental interventions require their own analysis.

## 4. Source and verification status

The [original written argument](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/e2502c82ab9a77c00543932f775a71e5374221f7/research/open-problems/time-self-reference/CALIBRATION-BOUND.md)
states this restricted result and its limits. The
[selected Lean source](https://github.com/Sodelin/Research-Commons/blob/3c6f7a27db9e6a6869d3e3142b82b8a43f8f0ed7/packages/research/lean/ResearchCommons/Calibration/RareEvent.lean)
defines the complete IID sample law and randomized decision, and contains
the corresponding sharp-error declarations. The later
[component verification record](https://github.com/Sodelin/Research-Commons/blob/8940f035a0bbf2f7855a8247517fc3033ab59c7c/packages/research/integration/calibration-component-verification.json)
reports acceptance for this exact known-rate IID claim. Its selected
[printed types and axiom records](https://github.com/Sodelin/Research-Commons/blob/8940f035a0bbf2f7855a8247517fc3033ab59c7c/packages/research/integration/calibration-complete-printed-types.json)
list the standard axioms used by the recorded endpoints.

The portfolio's source-identity audit matched the retained written proof,
Lean source, receipt and 20 printed declaration names at the specified
versions. It did not rerun Lean, independently verify the full raw audit,
or prove universal correctness of a Rust implementation. The older source
headers preserve their then-pending formal status; the later receipt is a
separate evidence epoch. A separate independent-review body and external
human peer review have not been established in the bounded material examined.

The calculation is an elementary binary hypothesis-testing argument. No
claim of historical novelty is made here. A future submission would require
current prior-work comparison, author and rights decisions, and independent
scientific review. Source links in this draft have not been freshly checked
for current public availability.
