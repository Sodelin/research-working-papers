# Physical Jacobian draft: source overlap with the analytic receipt

1 November 2026. This local comparison identifies reusable **source bytes**
for a possible later decision by the existing compiler owner. It is not an
offer, a new compiler job, object selection, proof review or Lean receipt.

The physical Jacobian target (internal supporting file not included: `PHYSICAL-JACOBIAN-TARGET.json`), 4,074
bytes/SHA-256 `8692cda18623848b70f02f8c666e50dd13c04dd2ef82df9a2dbd43d583ebe2bd`,
is a textual projection of the source manifest (internal supporting file not included: `SOURCE-MANIFEST.json`) at
source epoch `3f44da83d4636339beeff2d3493c43c19ed5a9d9`, manifest SHA-256
`7cfdf6923758fa07fe708967eb7ca8d0d766b0e7f2af7b56d0895312dfe4b2b5`,
retained at metadata commit `7c7cb04ce5cf932173b811119f1b76bcfb4c36ab`.
It names 41 local modules and ten directly imported external module names.
All 41 working bodies were checked against their recorded length, SHA-256,
Git blob and source-epoch Git bytes. This is not a transitive external closure.

The terminal PhysicalJacobianMatrixDraft (internal supporting file not included: `PhysicalJacobianMatrixDraft.lean`)
is 1,706 bytes/SHA-256
`f4e66b7d957697ffc699b4aa8e68450760a3072dd51efe1682a02ded12c1a989`,
Git blob `41faf499ede03e6e7bfced64ccdfcd40a25b8447`. It attempts a
nonzero determinant for the analytic feature map on `PhysicalAdmissible`;
the [domain and coordinate audit](JACOBIAN-SIGNATURE-AND-COORDINATES.md)
describes that statement and its unverified chain. It is not the timed
genealogy or the observed-sequence Jacobian.

## Exact comparison with the earlier reported qualification

The [analytic qualification record](LEAN-ANALYTIC-QUALIFICATION-20261031.md)
attributes a successful formula-injectivity check to the existing compiler
owner, for 18 selected local sources. It records that all 18 local source
hashes at repair commit `80834791ba37185954d0647ac3408166b907ff98` matched the
owner's selected identities. The older
offer manifest (internal supporting file not included: `SOURCE-MANIFEST.json`)
has SHA-256 `6fc729432ddea54687a473ae768957fd69f7df3c0c0bb8c88325f7bf2a869236`
and was used here to select those 18 **module names only**; it predates repairs
and is not the selected byte record.

Seventeen of the 41 Jacobian target names occur among those 18. Each current
body was compared byte-for-byte with both the `3f44da8` Git source epoch and
the `8083479` repaired-source commit; all 17 matched. Their individual source
hashes and blob IDs are in the manifest cited above:

```text
ABContinuationDraft     ABCrossingDraft          ABIntegralDraft
ABOrderingDraft         ABRecoveryDraft          ABSurvivalDraft
ARecoveryDraft          BBContinuationDraft      BCExcessDraft
BCRecoveryDraft         CRecoveryDraft           FixedContinuationDraft
ForwardDraft            PulseIntegralDraft       PulseKernelDraft
PulseScoreDraft         RootDraft
```

All names have the prefix `MSCi.TwoSite.`. The sole earlier analytic name
outside this target is `BBRecoveryDraft`. The other 24 target modules are not
covered by this 17-source receipt comparison; this does not assert that they
lack other evidence. The owner reported 16 fresh analytic compilations and
two previously qualified Forward/Root providers. Those providers retain the
previously reported brief execution overlap. This pass did not reread or
rescan the owner's raw audit and did not check the Jacobian target's proof.

## Direct imports and the remaining decision

The 18 source bodies at `8083479` directly name seven external imports:

```text
Mathlib.Analysis.Calculus.Deriv.Inv
Mathlib.Analysis.Calculus.Deriv.MeanValue
Mathlib.Analysis.SpecialFunctions.Exp
Mathlib.Analysis.SpecialFunctions.ExpDeriv
Mathlib.Analysis.SpecialFunctions.Integrals.Basic
Mathlib.Data.Fin.VecNotation
Mathlib.Tactic
```

The ten direct external names in the Jacobian projection include these seven
and additionally name:

```text
Mathlib.Analysis.Calculus.FDeriv.Pi
Mathlib.LinearAlgebra.Matrix.Block
Mathlib.Topology.Algebra.Module.FiniteDimension
```

The latter three were not directly imported by the earlier 18 selected local
source bodies. This observation does **not** show whether the earlier build
used them transitively or whether compatible objects are available now. The
earlier selected-trace overlap (internal supporting file not included: `SELECTED-FIRST-TRACE-ANALYTIC-OVERLAP.md`)
records owner-reported historical object identities for `Exp`, `VecNotation`
and `Tactic`; it does not establish a sufficient object closure here.

The exact remaining work is owner selection of a coherent source/object and
toolchain context, checking the unqualified Jacobian declarations and their
dependencies, and an appropriate named theorem/axiom audit. The separate
same-genealogy source/observation correspondence remains essential to the
manuscript's biological-model interpretation. No compiler action follows from
this comparison, and the existing graph-only offer retains its scope.
