# Observation transport: Jacobian import repair

This records a source-dependency defect and an uncompiled repair. It does not
report a Lean failure or success, prove the Jacobian or interval statements,
or authorize a compiler job.

## Finding

At source epoch `3f44da83d4636339beeff2d3493c43c19ed5a9d9`,
`PhysicalObservationTransportDraft` called the project theorem
`physical_feature_derivative_injective`. Its sole definition found in the
local manuscript Lean tree was in `PhysicalJacobianDraft`, but the recorded
local import projection for the observation target did not include that
module. The projection's 18 directly named external imports were Mathlib
modules; their transitive declarations were not exhaustively inspected.

The earlier `PhysicalDomainDraft` had imported `PhysicalJacobianDraft`.
Its `bd29f7a` successor instead imported the lighter physical-feature source,
while the observation theorem still called the Jacobian declaration. The
historical r36 source snapshot has the same observed source dependency gap.
This is a local source-graph finding, not an observed compiler error; no Lean
elaboration was run to exclude an unexpected transitive external declaration
or to determine any other errors.

## Successor source layout

Source commit `3323b857ae715e9c464d2e4b304051e3161530bc` separates the
independent transport from the derivative-injectivity theorem:

| Source | Role in the successor |
| --- | --- |
| PhysicalObservationCoreDraft (internal supporting file not included: `PhysicalObservationCoreDraft.lean`) | Retains the generic feature agreement, derivative equality, injectivity and conditional interval transport declarations, without asserting derivative injectivity. |
| PhysicalObservationTransportDraft (internal supporting file not included: `PhysicalObservationTransportDraft.lean`) | Imports the core and `PhysicalJacobianDraft`, then retains the original generic derivative-injectivity theorem. |
| JCSourcePhysicalCoreDraft (internal supporting file not included: `JCSourcePhysicalCoreDraft.lean`) | Retains the constructed-source feature and interval specializations without the separate derivative-injectivity declaration. |
| JCSourcePhysicalTransportDraft (internal supporting file not included: `JCSourcePhysicalTransportDraft.lean`) | Imports the source core and generic Jacobian facade, then retains the original constructed-source derivative-injectivity theorem. |
| JCSourceFiniteContractorDraft (internal supporting file not included: `JCSourceFiniteContractorDraft.lean`) | Imports the source core, preserving an interval path that does not require the unrelated determinant chain. |

Both moved theorem blocks and the remaining declaration suffixes were compared
byte-for-byte with their predecessor Git bodies. A declaration-name comparison
found the original nine generic declarations partitioned as eight core and one
facade, and the original seven constructed-source declarations as six core and
one facade. The finite contractor changed only its import. The old module names
are retained as facades intended to expose the same declarations through their
imports; actual Lean name resolution and proof elaboration remain untested.

At the successor manifest epoch, the core/facade projections have 35/54 local
and 18/19 directly named external imports for the generic transport, and
206/226 local and 52/53 external names for the constructed-source transport.
Both facades' local projections contain `PhysicalJacobianDraft`; neither core
nor the 210-local/52-external finite contractor projection does. These are
textual graphs, not selected object closures. The historical 35/206 counts
described earlier facade files that still contained the derivative theorem;
they are not evidence that those files could compile with the omitted local
provider.

For the restored analytic chain, the owner's pinned Mathlib source defines
[`Matrix.BlockTriangular`](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/LinearAlgebra/Matrix/Block.lean#L53-L64)
using `b j < b i` for a zero at row `i`, column `j`. The local candidate
uses `OrderDual` so that a later original column is required to vanish; that
is the intended orientation for the lower-block Jacobian. The same source
revision displays the [block determinant product](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/LinearAlgebra/Matrix/Block.lean#L301-L305)
and the [coordinate-update derivative interface](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Analysis/Calculus/FDeriv/Pi.lean#L16-L20)
used by the draft. These source-level interfaces do not prove Lean's instance
resolution, elaboration or the local proof terms.

The refreshed source identities, limited marker screen and retained historical
snapshot boundaries are in the verification record (internal supporting file not included: `VERIFICATION.md`).
The complete source/observation correspondence, the Jacobian proof, interval
enclosures, current compiler-owner selection and independent review remain open.
