# Candidate graph and time-scale comparison

This is a hand-derived comparison of the selected [two-site model](../MANUSCRIPT.md#2-model-observations-and-notation) with the definitions in §§2–3 of [Allman, Baños, Garrote-Lopez and Rhodes (2024)](https://link.springer.com/article/10.1007/s11538-024-01339-4). It extends the [quartet-CF source note](ALLMAN-ET-AL-2024-QUARTET-COMPARISON.md). It has not been independently reviewed or checked in Lean. It is not an assertion that every hypothesis of the paper's Corollary 31 has been verified for this model.

## Graph and candidate edge lengths

Write `R` for the backbone join at age `t0`, `S` for the A/B join at `t1`, `U` for the point on the C branch at `h`, and `V` for the point on the B branch at `h`. In forward time the graph has edges

```
R -> S, R -> U, S -> A, S -> V, U -> C, U -> V, V -> B.
```

The zero-duration donor edge is `U -> V`; the backward choice from `V` to `U` has probability `g`. The other parent choice from `V` to `S` has probability `1-g`. For these three species, `R` is the least stable ancestor in the graph: every root-to-A and root-to-C path meets it, while neither `S` nor `U` lies on every path to all three. Suppressing `R` as in the paper's semidirected construction replaces `S-R-U` by an undirected `S-U` edge. The resulting cycle is `S-U-V-S`, with the two hybrid edges directed into `V`; the pendant branches lead respectively from `S` to A, `V` to B and `U` to C. Attaching the paper's two pseudotips to each sampled species gives a central three-cycle with three cherries, and the B cherry below the hybrid node, matching the **description** in its Figure 6 caption after relabelling. The figure itself was not visually inspected.

On 1 November 2026 UTC the publisher's [Figure 6 page](https://link.springer.com/article/10.1007/s11538-024-01339-4/figures/6) returned its caption, but a request for the linked image timed out. The caption is not an inspection of the diagram or an independent copy of the paper.

The paper's Figure 6 caption and Propositions 35–36 give opposite left/right panel references in the inspected HTML text. For a separate inverse-formula term, an earlier recorded PDF text reading differed from the HTML, while a later web extraction agreed with it. The [source comparison](ALLMAN-ET-AL-2024-QUARTET-COMPARISON.md#figure-and-formula-reading-limits) records these readings and an arithmetic control; the figure and PDF equation remain visually unverified. Do not use a panel reference or an unverified extracted formula alone to assign the candidate edge labels.

Integrating the manuscript's per-pair rates along the corresponding population segments suggests this semidirected coalescent-unit assignment:

| Edge after suppressing `R` | Candidate coalescent length |
| --- | --- |
| `S-A` | `rA * t1` |
| `V-B` | `rB * h` |
| `U-C` | `rC * h` |
| `S-V` | `rB * (t1-h)` |
| `U-V` | `0` |
| `S-U` | `rAB * (t0-t1) + rC * (t0-h)` |

The `S-U` expression concatenates the `S-R` AB segment and the `R-U` C segment for the paper's semidirected quartet representation. The ancestral root rate `rR` is not among these finite edge lengths. This table is a proposed translation of the model's population segments, not an independently established equality of the two complete stochastic laws. In particular, the effect of the zero-length hybrid edge, the two-sample pseudotips and the rate/time constraints on the exact scope of the paper's numerical nonidentifiability statement still needs a checked parameter-level mapping. The paper permits nonnegative hybrid-edge lengths, but that alone does not transfer its unrestricted nonidentifiability alternatives into this constrained family.

## Constraint implied by the candidate table

The rate ties and event ordering impose a concrete constraint even before the
stochastic-law comparison. Write the five nonzero candidate edge lengths in
the table as

$$
(a,b,c,d,s)=(r_A t_1,\ r_B h,\ r_C h,\ r_B(t_1-h),\
 r_{AB}(t_0-t_1)+r_C(t_0-h)).
$$

They are all positive and necessarily satisfy `s > c d / b`: indeed
`c d / b = rC (t1-h)`, while `t0 > t1` and `rAB > 0` add positive
terms. Conversely, this inequality and positivity characterize the image of
the **displayed candidate length assignment**, with the hybrid-edge length
fixed at zero. To see this, for any positive `a,b,c,d,s` satisfying the
inequality, choose

$$
h=1,\quad t_1=1+d/b,\quad
t_0=t_1+\frac{s-cd/b}{2c},\quad
r_A=a/t_1,\quad r_B=b,\quad r_C=r_{AB}=c.
$$

These choices have `0 < h < t1 < t0` and reproduce all five lengths. The
root rate may be any positive value and the pulse probability any value in
`(0,1)`; neither occurs in these five equations. The construction uses an
allowed equality of two rates, not an assumption that the model requires it.
This elementary algebra does not identify the proposed lengths with the
paper's full stochastic model or determine whether the paper's alternative
parameter values stay in this constrained, zero-hybrid-edge image. It is a
hand-derived, unreviewed boundary for the comparison, not a proof of either
identifiability claim.

Three exact rational substitutions in memory agreed with the displayed
construction and the identity `s - c d / b = (rAB + rC)(t0 - t1)`. These
examples check arithmetic only; they do not prove the universal statement or
validate the source-model crosswalk.

The subsequent [zero-hybrid-edge example](QUARTET-ZERO-EDGE-EXAMPLE.md)
gives two exact distinct inputs to the paper's six quartet-CF formulas and
an algebraic realization of their candidate lengths satisfying this
inequality. The formula arithmetic is checked with rational numbers; the
same example has different AC one-site character expectations under the
manuscript's stated forward/JC law. The figure-label reading, stochastic-law
crosswalk and that conditional feature comparison remain to be reviewed
separately. This is not a counterexample to the two-site claim.

## A separate time-scale illustration

The model itself suggests a direct way to see why a gene-tree topology summary and a known-clock sequence law can behave differently. Fix any admissible parameter point and `lambda > 1`. Divide `h`, `t1` and `t0` by `lambda`; multiply all five rates `rA`, `rB`, `rC`, `rAB` and `rR` by `lambda`; leave `g` and the JC clock fixed. Strict ordering, positive rates and the rate ties are preserved. Each candidate edge length in the table is unchanged.

For the specified piecewise-constant coalescent, use the same unit-rate exponential draws and pulse-routing choices in the two histories. Every waiting time and scheduled boundary is divided by `lambda`, so the merger/routing order and hence each unrooted gene-tree topology are the same in this coupling, while every pair's coalescence time changes from `T` to `T/lambda`. The root phase is included in this time change. This is a hand argument from the model description, not a formalized construction of its probability space.

For an A/C pair, `T >= t0 > 0`: the two lineages are in separate populations until the root. Under the manuscript's JC character identity with `c=8/3`, the corresponding one-site character expectation changes from `E[exp(-c T)]` to `E[exp(-c T/lambda)]`, which is strictly larger for `lambda > 1`. Thus this coupled pair of parameter points has the same gene-tree topologies but different known-clock sequence expectations, assuming the stated source and observation laws. It is a concrete reason a CF nonidentifiability result need not conflict with identification from the manuscript's sequence law. It does not establish the manuscript's full identification theorem or a general information ordering between CFs and two-site data.

Independent mathematical review, a complete stochastic-law correspondence, and kernel-checked derivations of the process and observation claims remain open.
