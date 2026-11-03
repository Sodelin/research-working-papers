# How a fixed model's observable law changes with its parameters

**Working expository manuscript · 3 November 2026.** This note explains one
selected AI-assisted research component and a standard polynomial argument.
It is not a submitted preprint, a claim of priority, an empirical validation
or a proof of the entire G6 programme. Sodelin is organizing the research
and seeking collaborators; human contributions, authorship and rights for
any eventual publication remain open.

## Abstract

For a finite observed alphabet, suppose the probability of each outcome is
given by one fixed polynomial in coordinates lying in the unit cube. A
coefficient-and-degree sum bounds how much the observable probability law can
change when the coordinates change. We explain the elementary argument and
identify an existing formal component that applies it to a specified
ancestral model on one fixed graph and date/cut cell. The source-model
construction needed for that application is a separate part of the result.

## 1. A bound for a polynomial family of laws

Let `O` be a finite set of possible observed outcomes and let
`x=(x₁,…,xₘ)` and `y=(y₁,…,yₘ)` lie in `[0,1]ᵐ`. For each outcome `o`, let

$$
 Q_o(z)=\sum_{\alpha} a_{o,\alpha}z^\alpha,
 \qquad z^\alpha=\prod_{i=1}^m z_i^{\alpha_i},
 \qquad |\alpha|=\sum_i\alpha_i,
$$

where each sum has finitely many nonzero coefficients and each exponent is
a nonnegative integer. Assume that `(Q_o(x))` and `(Q_o(y))` are probability
distributions. We do **not** need to assume that `Q` defines a distribution at
every other point in the cube.

Let `ε ≥ 0` satisfy `|xᵢ−yᵢ| ≤ ε` for every coordinate, and define

$$
 K=\frac12\sum_{o\in O}\sum_{\alpha}
       |a_{o,\alpha}|\,|\alpha|.
$$

Then, using the half-L1 convention for total variation,

$$
 \operatorname{TV}(Q(x),Q(y))
 =\frac12\sum_{o\in O}|Q_o(x)-Q_o(y)|\le K\varepsilon. \tag{1}
$$

For a finite alphabet, the left side is also the largest absolute difference
the two laws assign to an event. The bound may exceed one; in that case one
may additionally use the general bound `TV ≤ 1`. A zero-degree term
contributes zero to `K`.

### Argument

Write a monomial as a product of `|α|` individual factors, repeating `zᵢ`
exactly `αᵢ` times. Replace the factors at `x` by those at `y` one at a
time. Every remaining factor has absolute value at most one, so the
telescoping sum gives

$$
 |x^\alpha-y^\alpha|
 \le\sum_i\alpha_i|x_i-y_i|
 \le |\alpha|\varepsilon.
$$

Multiply by each coefficient's absolute value, sum over monomials and
outcomes, and divide by two. This proves (1). The argument is a familiar
finite-product inequality; no novelty or optimality of `K` is claimed. For an
empty coordinate set, both evaluations agree and the bound is zero.

## 2. A small example

Suppose a binary observation has `Pₓ(1)=x²` and `Pₓ(0)=1−x²`, with
`x∈[0,1]`. The degree-weighted coefficient sum gives `K=2`, and

$$
 \operatorname{TV}(P_x,P_y)=|x^2-y^2|\le 2|x-y|.
$$

This example illustrates the algebra. It is not an example of the original
ancestral source or an analysis of biological observations.

## 3. The selected source-model application

The existing source fixes a finite rooted-binary source graph, its original
parent registry and inheritance-mode flags, a nonempty finite sample, a
finite set of cuts, one realized date/cut cell and one finite
source-independent reader. The reader sees the same-record unranked forest
and pairwise merger-bin matrix. It is not granted access to latent source
codes or private register bits.

Under the source's exact hypotheses, its selected cell theorem supplies one
rational polynomial table that applies throughout that realized cell. Its
observed-law theorem applies the bound above to the actual shared physical
bank. That bank includes original inheritance probabilities and survival
coordinates formed from rates and durations; repeated coordinates remain
linked through the same physical parameters. The theorem uses the **sum of
absolute differences of those bank coordinates** as the distance. It does
not claim that these coordinates may be chosen independently, or that the
same constant works over unknown graphs or other cells.

The polynomial inequality alone does not produce that source-to-table
construction. Nor does the result provide a table-extraction algorithm, a
rare-event conditional bound, an inverse estimator, a biological data adapter
or evidence that this model fits a dataset. The full G6 claim has its own
accepted hand status; this is one selected formal consumer, not a complete
formalization of that claim.

## 4. Source and checking status

The two source declarations are
`UnifiedLean.G6.CellCompletedBinPolynomial.actual_cell_completed_bin_polynomial`
and `UnifiedLean.G6.ActualCellObservedTV.actual_cell_completed_observed_tv`.
Their selected bodies are 10,497 and 11,433 bytes, with SHA-256 values
`023420092662177cb45bd933535ca51920e07d56f8e53c1388aeb0af503cbe96` and
`978e3f369e69ccc718e54820f4e53b25d2fde5ea2e65eba8d581e36adced669c`,
respectively, at guide commit `501730afc601aa196ff4c7b84e96105a63199668`.
The source credits dot / OpenAI and retains its original candidate header.
The later [source-package report](https://github.com/Sodelin/Research-Commons/blob/de3011fa352e04f9be64cf9f4da8a5528cad68db/research/2026-10-10-dot-g6-completed-cell-tv-0258z/README.md)
is associated with separate owner-reported checks; its historical status is
not inferred merely from the source header.

A nine-file source selection in the original local portfolio matches selected
guide sources and source-pin records but omits much of the 233/236-module
historical closure. Its original evidence row describes retained projected
terminal receipts and an uninspected raw-audit boundary. The [public source-package report](https://github.com/Sodelin/Research-Commons/blob/de3011fa352e04f9be64cf9f4da8a5528cad68db/research/2026-10-10-dot-g6-completed-cell-tv-0258z/README.md)
provides the earlier public account. This manuscript has not received a new Lean check or independent
human review. Prior literature, contributions, rights and any eventual
external release require their own review.
