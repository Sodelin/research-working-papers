# Jacobian candidate: domain and coordinate audit

1 November 2026. This is a bounded reading of the **uncompiled** analytic
Jacobian candidate, not a Lean receipt or an independent scientific review.
It checks the visible target, coordinate conventions and selected factor
signatures against the manuscript; it does not establish the proof terms or
the process-to-observation correspondence.

The source epoch is `ef452b2d954a92ba4ef7a0b788ed1e37e25571b8`. The
source manifest (internal supporting file not included: `SOURCE-MANIFEST.json`), SHA-256
`add7ceabe7e004dd9fa24e2032a4332d6c22f2ee3beabf4276237a39c7b51ae4`,
binds the 13 bodies selected for this comparison. Their current bytes, lengths
and hashes matched that manifest and the epoch's Git tree/blob bytes. The
displayed definitions and signatures were inspected; not every proof body was
read. The target's recorded local textual import projection has 41 modules and
ten external names; this audit does not inspect or qualify that complete
closure.

The selected bodies are `ForwardDraft`, `CoordinatesDraft`,
`RecoveryFeatureMapDraft`, `PhysicalFeatureDifferentiabilityDraft`,
`RootJacobianDraft`, `RateJacobianDraft`, `PulseJacobianDraft`,
`ABJacobianCompletionDraft`, `BBJacobianDraft`, `DiagonalProductDraft`,
`RecoveryJacobianCompletionDraft`, `PhysicalJacobianDraft` and
`PhysicalJacobianMatrixDraft`. Their exact paths and individual identities are
in the pinned manifest; the earlier compiler receipt applies to `ForwardDraft`
at its selected hash, not to the uncompiled Jacobian target.

## Exact target and domain

The final candidate
`physical_feature_jacobian_det_ne_zero` (internal supporting file not included: `PhysicalJacobianMatrixDraft.lean`)
states nonzero determinant for `physicalFeature` at `x`, assuming
`PhysicalAdmissible x`. It has no explicit distinct-rate premise. The matrix
definition uses output-feature indices as rows and physical-coordinate
indices as columns. The stated target concerns the transcribed analytic
feature map, not yet the distribution of the six sampled sequences.

The physical coordinate order is
`x = (h,u,v,rA,rB,rC,rAB,R,g)`, with `u=t1-h` and `v=t0-t1`.
`physicalParameters` (internal supporting file not included: `PhysicalFeatureDifferentiabilityDraft.lean`)
sets `t1=h+u` and `t0=h+u+v`. Its displayed domain requires `h,u,v>0`, all
five rates positive and `0<g<1`. In real coordinates these are equivalent to
the manuscript's `0<h<t1<t0`, positive rates and strict pulse probability.
The candidate also states this equivalence and the equality of its physical
feature map with `nineRawFeatures` at those parameters. The feature order is
`(AC1,AC2,CC1,BC1,BC2,AB1,AB2,AA1,BB1)` and the fixed exponent is `8/3`.
Those stated equalities and their Lean proof terms remain unchecked.

## Coordinate orientation

The recovery coordinate order in the source (internal supporting file not included: `CoordinatesDraft.lean`)
is `y=(T,R,rC,h,g,a,rAB,rA,rB)`, where `T=h+u+v` and `a=h+u`.
Its linear map from `x` has rows

```text
(h+u+v, R, rC, h, g, h+u, rAB, rA, rB).
```

Let `C` be its matrix in these displayed orders. Subtracting row 5 from
row 0 and then row 3 from row 5, using zero-based row numbers, leaves the
permutation of physical-coordinate columns `(2,7,5,0,8,1,6,3,4)`. That
permutation has 18 inversions, so these determinant-preserving row operations
give `det(C)=+1`. An in-memory integer check confirmed the row reduction and
inversion count. This checks the displayed coordinate calculation, not the
Lean definitions, differentiation or determinant proof.

Consequently, **if** the candidate derivative chain and its positive
recovery-order determinant are established, the chain rule gives the same
positive determinant in this particular physical coordinate order. The
manuscript needs only nonsingularity; this conditional orientation observation
does not establish the manuscript theorem.

## Explicit factor premises

The selected positive-product candidate (internal supporting file not included: `DiagonalProductDraft.lean`)
uses the following six named source statements. Their visible hypotheses are
entailed by the strict domain and the positive exponent when the parameters
are substituted as in that file:

| Factor | Visible hypotheses in the named statement |
| --- | --- |
| Root two-by-two block | `R>0` and `c>0`. |
| C rate | `Admissible p` and `c>0`. |
| Pulse two-by-two block | `R>0`, `rC>0`, `c>0`, `h<T` and `g>0`. |
| AB two-by-two block | `R>0`, `rAB>0`, `c>0`, `a<T` and `g<1`. |
| A rate | `Admissible p` and `c>0`. |
| B rate | `Admissible p`, `c>0` and the separately supplied positive rate, instantiated as `rB`. |

The source's `jcPairExponent` is `8/3`. None of these displayed signatures
introduces a pairwise rate-inequality premise. A narrow line-based screen found
no `variable`, `variables`, `axiom`, `constant` or `opaque` declaration in
the 13 selected files; it is not a Lean parser or an axiom audit. Imported
declarations, implicit elaboration, the six factor proofs, the matrix
factorization, differentiability and the chain rule all still require the
existing owner's exact source/dependency selection and kernel/axiom checks.
The other 28 local modules and ten direct external names in the textual target
were not audited here.

A later [source-overlap comparison](PHYSICAL-JACOBIAN-ANALYTIC-OVERLAP.md)
checked the current 41 target bodies against their recorded Git epoch and
found that 17 match the repaired sources associated with the owner's earlier
analytic formula-injectivity receipt. It records the ten direct external names
and three not directly named in that earlier 18-source selection. Neither
source overlap nor those names qualify this Jacobian target or its objects.
