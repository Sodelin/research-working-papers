# Two coordinates for exchangeable three-lineage forests

**Working expository manuscript · 3 November 2026.** This note explains an
existing AI-assisted project argument and adds an abstract four-label
illustration. It is not a submitted preprint, a claim of mathematical
priority or a biological validation. Sodelin is organizing the research and
seeking collaboration; human contributions, authorship and rights for any
eventual publication remain open.

## Abstract

For a label-exchangeable, projective law on rooted binary forests of at most
three fresh lineages, two separation probabilities determine the entire
unranked forest law. Under an explicit serial-kernel assumption, the two
coordinates multiply, so reversing two stages gives the same law through three
lineages. We give a four-label matching example showing that the two
coordinates do not determine a larger forest law. These are statements about
specified abstract forest laws; physical realization and timed or observed
data require additional arguments.

## 1. The seven possible forests

Begin with three distinct labelled roots. Assume the output is an unranked
rooted **binary** forest on those labels, with no extra observable marks.
There is one forest with all three roots separate; there are three forests
with one specified two-label cherry and one singleton; and there are three
complete rooted triples, one for each possible first cherry. No simultaneous
three-way merger is included in this state space.

Suppose the law is invariant under relabelling. Write `n` for the probability
that all three roots remain separate, `c` for the probability of any *one
specified* cherry-and-singleton forest, and `t` for the probability of any
*one specified* complete rooted triple. Thus

\[
 n+3c+3t=1. \tag{1}
\]

Assume that deleting a label and suppressing any resulting unary vertex gives
the same two-root law as applying the kernel directly to those two roots.
Let `d` be the probability that the two retained roots are separate. They are
separate in the all-singleton forest and in the two cherry-and-singleton
forests whose cherry contains the deleted label. Hence

\[
 d=n+2c,\qquad
 c=\frac{d-n}{2},\qquad
 t=\frac{n-3d+2}{6}. \tag{2}
\]

These equations determine all seven output probabilities from `(d,n)`.
In particular, nonnegativity requires `0 ≤ n ≤ d ≤ 1` and `n ≥ 3d−2`.
The equations do not assert that every admissible pair is realized by a
particular physical population model.

## 2. Two serial stages

Consider two fixed forest-growth kernels `K₁,K₂` with coordinates
`(d₁,n₁)` and `(d₂,n₂)`. Each stage must act on the *current* roots, treat
their already-built subtrees as opaque labelled objects, and use the same
exchangeable/projective two- and three-root laws just described. Conditional
on its input forest, the second stage uses its specified kernel; in
particular, there is no unaccounted shared random choice coupling the stages.

A chosen pair remains separate after both stages exactly when it remains
separate in each stage. All three remain separate exactly when no merger
occurs in either stage. Therefore the serial law has

\[
 d_{12}=d_1d_2,\qquad n_{12}=n_1n_2. \tag{3}
\]

For example, a specified cherry followed by a singleton has probability

\[
 c_{12}=c_1d_2+n_1c_2
       =\frac{d_1d_2-n_1n_2}{2}. \tag{4}
\]

Equation (2) then determines the complete-triple probabilities. Both
coordinates in (3) are unchanged by exchanging the stage order, so the two
orders have the same **unranked forest distribution through three roots**.
This conclusion does not preserve stage labels, merger times, ranks, routes
or other marks. If the stages share a once-drawn register, the multiplication
must be justified conditional on the complete relevant register; products of
unconditional averages do not generally follow.

For an ordinary edge with a constant positive rate `λ` per unordered pair
and duration `s ≥ 0`, put `x=e^(−λs)`. Pair separation is `d=x`; with three
live roots the total initial merger rate is `3λ`, so `n=x³`. Equations (2)
give

\[
 c=\frac{x-x^3}{2},\qquad
 t=\frac{(1-x)^2(2+x)}{6}. \tag{5}
\]

The coordinate `e=(n-d³)/6` measures the difference from the ordinary-edge
triple coordinate at the same `d`. Substituting (3) yields

\[
 e_{12}=d_2^3e_1+d_1^3e_2+6e_1e_2. \tag{6}
\]

## 3. The coordinates do not determine four-root laws

This abstract example uses four labelled roots and random matchings. Choose
`M ∈ {0,1,2}` and then choose uniformly among matchings of size `M` in the
complete graph on the four labels. Each chosen pair becomes a cherry; all
other roots stay singletons. The law is exchangeable. Its two- and three-root
laws are obtained by restricting this same four-root forest.

There are six possible edges. A fixed pair is matched with probability
`E[M]/6`, so `d=1−E[M]/6`. A fixed triple contains an expected `M/2`
matching edges; it cannot contain two disjoint matching edges. Therefore
`n=1−E[M]/2`. Consider these two distributions:

| Law | `P(M=0)` | `P(M=1)` | `P(M=2)` |
| --- | --- | --- | --- |
| A | `1/4` | `1/2` | `1/4` |
| B | `1/3` | `1/3` | `1/3` |

Both have `E[M]=1`, hence `(d,n)=(5/6,1/2)` and `t=0`. Their complete
two- and three-root laws agree by (2). But the probability that **all four**
roots remain separate is `1/4` under A and `1/3` under B. Thus `(d,n)` does
not determine the four-root forest law. The example is an abstract
exchangeable matching construction; no claim is made that either distribution
is admitted by the project's positive-rate biological source model.

## 4. Sources and verification status

Equations (1)–(6) and the stated cap-three interface are presented in
Full Pro's `01-CONTRACTS-AND-REUSABLE-LEMMAS.md`, section L5, at library
commit `1ac9c42ca8c029d2af6b068c0015b794a7a1eee0`: 13,022 bytes, SHA-256
`4c8b605464c12ecd8f5d7ed767d444011383baf830101b4afe1c7fd1d4045119`.
The corresponding `cap-three-coordinates` unit describes L5 as elementary
algebra in a reviewed reading chapter and names `whole-source-projectivity`
as a dependency. It does not claim a new Lean check. The precise history and
scope of that chapter's reviews remain with the source records; an AI review
is not human peer review.

The existing guide also indexes an earlier related argument as
`XR-G4-COMMUTE3`, linked there to `CB-G4-001`. Its 1 October source,
authored by GPT-6 Astra Pro, gives the equivalent three-root count-matrix
composition under its exchangeability, sampling-consistency and grafting
assumptions. The selected source is 11,126 bytes, SHA-256
`9ace2081cfd430b028e62c2ad79ca66a77d4f91414c5203e3db8715d32d9c271`,
in guide commit `501730afc601aa196ff4c7b84e96105a63199668`. The guide
attributes a later scoped coordinating-AI acceptance and an exact polynomial
check; neither is an independent human review. The guide records no complete
Lean formalization of that theorem. This is a related source and component,
not a derivation of the complete G4 claim.

That earlier source also reports a positive four-root example in its declared
two-port model where reversing an ordinary edge and an independent bigon
changes an observable probability. It reports exact rational computations;
we have not rerun them or checked the underlying model implementation in
this edition. This reported model-specific example and our abstract matching
example above have different assumptions and verification histories.

The four-root matching example above is an expository construction in this
edition, not a claimed novel result or an example attributed to L5. Its
[exact arithmetic check](check_examples.py) enumerates the finite matching
cases and checks selected rational serial-coordinate identities. It does
not prove the general theorem or establish a physical-source coupling.
No new Lean run, full prior-art search, human subject-matter review,
implemented inference procedure or publication is claimed.
