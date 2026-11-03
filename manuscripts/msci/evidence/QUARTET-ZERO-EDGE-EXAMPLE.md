# Conditional quartet coincidence with one zero hybrid edge

The following is an exact arithmetic comparison with the six quartet-CF
coefficients in [Allman, Baños, Garrote-Lopez and Rhodes (2024), Proposition 36](https://pmc.ncbi.nlm.nih.gov/articles/PMC11272829/).
It addresses the [open candidate edge-length question](QUARTET-CYCLE-CROSSWALK.md#constraint-implied-by-the-candidate-table).
The arithmetic and proposed label/length correspondence have not received
independent review or a Lean check. The equality concerns the paper's
**gene-tree topology summaries**. A separate conditional comparison of the
manuscript's sequence features appears below.

## Two distinct inputs to the published formulas

Use the paper's symbols and order each tuple as
`(gamma, x, ell1, ell2, ell3, h1, h2)`. Consider

| Point | `gamma` | `x` | `ell1` | `ell2` | `ell3` | `h1` | `h2` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `1/2` | `1/2` | `1/2` | `1/2` | `1/2` | `1` | `9/10` |
| 2 | `20/33` | `32/65` | `41/80` | `15/32` | `13/24` | `1` | `368/533` |

The points are distinct, the hybridization probabilities and all edge
probabilities except `h1` lie strictly between zero and one, and `h1 = 1`
represents a zero-length hybrid edge. The paper allows nonnegative hybrid
lengths and positive tree lengths. Direct substitution into its six displayed
coefficients yields, in the order `(alpha, beta, eta, delta, epsilon, zeta)`,

```text
(23/320, 11/60, 1/8, 1/8, 17/240, 1/24).
```

The [exact-rational check](../scripts/check_quartet_boundary_example.py) evaluates the
six formulas separately for both inputs. There are 15 choices of four of the
six labelled pseudotaxa: one each of types `aabb`, `aacc`, `bbcc` and four
each of `aabc`, `abbc`, `abcc`. On the paper's stated exchangeability and
six vector formulas, equal coefficients therefore give the same 15 quartet
CF vectors. This is a calculation from those formulas, not independent
verification of the formulas or of a stochastic model.

## Candidate connection to the time/rate constraints

The paper's `a` cherry is below its hybrid node. The author preprint's
[figure source](https://arxiv.org/src/2401.06290v1), `Figures/6taxon.tex`,
places `ell1` below that node, `ell2` and `ell3` on the other two cherries,
`x` on the opposite cycle edge, and `h1`/`h2` on the two hybrid edges. The
source text associates `gamma` with the `h1` side by the locations of its
TikZ labels. This is a reading of the preprint source coordinates, not a
rendered-image or publisher-edition check.

For the candidate mapping, identify the paper's `(a,b,c)` cherries with the
manuscript's `(B,C,A)` populations, put the zero `h1` edge on the donor side,
and take `g = gamma`. Set

```text
b = -log(ell1),  c = -log(ell2),  a = -log(ell3),
d = -log(h2),    s = -log(x).
```

The existing candidate image requires all five lengths positive and
`s > c*d/b`. For the first point, `b=c` and `x<h2`, so `s>d=c*d/b`.
For the second point the exact rational inequalities

```text
(15/32)^2 > (41/80)^3       and       (32/65)^2 < (368/533)^3
```

give `c < 3*b/2` and `3*d/2 < s`, respectively. Thus both points meet that
inequality. The script checks these rational comparisons, without evaluating
floating-point logarithms.

The earlier explicit realization can then be applied separately to each point:

```text
h = 1,  t1 = 1 + d/b,  t0 = t1 + (s - c*d/b)/(2*c),
rA = a/t1,  rB = b,  rC = rAB = c,  rR = 1,  g = gamma.
```

It gives `0 < h < t1 < t0`, positive rates, the required B/C rate ties,
and the five lengths in the candidate table. Since the two `gamma` values
differ, these are distinct physical-coordinate assignments. This is an
algebraic realization of the **candidate length assignment**. The complete
identification of that assignment with the paper's NMSC quartet law and with
the manuscript's original process remains an explicit source-to-model gate.

## A conditional sequence-feature distinction for these points

For the particular realization above, the displayed expression for `t0`
simplifies to

```text
t0 = 1 + (d/b + s/c)/2.
```

The first point has `s=c` and `(9/10)^4 > 1/2`, hence `d/b < 1/4` and
`t0 < 13/8`. For the second point,

```text
(368/533)^2 < 41/80       and       (32/65)^4 < (15/32)^3
```

imply `d/b > 1/2` and `s/c > 3/4`, respectively, so `t0 > 13/8`.
The script checks the rational inequalities; the logarithmic implications
use monotonicity and the positive lengths. Thus the two constructed root
times differ without relying on floating-point rounding.

The manuscript's [AC forward expression](../MANUSCRIPT.md#forward-pair-transforms)
gives `m_AC(1) = exp(-(8/3)*t0) * rR/(rR+8/3)`. Under that stated
forward/JC observation law, with `rR=1` in both realizations, the first
point has a strictly larger AC one-site character expectation. In fact,
the common separating value is `(3/11) * exp(-13/3)`: the first expectation
is larger and the second is smaller. As that character is a function of the
first site, the corresponding two-site distributions would also differ.
This is a conditional hand argument using
the stated model's forward law, not an independent verification of that law,
the source-to-model correspondence, or the manuscript's full identification
theorem.

## How the candidate arose and what remains

For the special case `h1=1`, eliminating the other variables from the
displayed formulas gives a quadratic candidate equation for `L=ell3`:

```text
(alpha/3 - beta*eta)*L^2
 + (beta*zeta + epsilon*eta - alpha*delta - 3*delta*beta*eta)*L
 - 2*epsilon*zeta + 3*delta*beta*zeta + 3*delta*epsilon*eta = 0.
```

For the common coefficients above, its two roots are `1/2` and `13/24`.
This was used to find the second tuple; direct substitution, rather than the
quadratic alone, is the recorded equality check. Two earlier hand-selected
seeds were rejected: one yielded the singular recovery value `ell3=3*delta`;
the other produced negative or out-of-range parameters. No search over the
parameter space or general nonidentifiability theorem is claimed.

A reviewer should check the formula transcription, the graph/edge and
hybrid-probability correspondence, the realization and the distinction between
quartet and two-site data. An exact same-CF pair in the candidate image gives
a more specific comparison than unrestricted three-cycle nonidentifiability,
but does not refute the manuscript's sequence-identification claim or supply
its physical-model, Lean, sampling or biological validation.
