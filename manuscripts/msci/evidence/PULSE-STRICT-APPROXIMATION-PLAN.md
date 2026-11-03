# A conditional strict-calendar approximation for the pulse

1 November 2026. This was originally an unreviewed hand-level plan for one possible bridge
between the [zero-duration pulse program](PULSE-ZERO-EDGE-CONSTRUCTION.md)
and the existing strict-calendar source. It supplies neither a Lean theorem
nor a physical-process identification. In particular, a limit of endpoint
laws must not be confused with equality of raw timed paths.

## Candidate calendars and the short window

Keep the same seven-edge graph, six original copy labels, pulse parameter and
positive edge/root rates as in the zero-edge candidate. In particular, the
two C edges both use `rC`, and donor edge 5 keeps its placeholder rate `1`.
For `0 < epsilon < t1 - h`, move only donor vertex `D` from age `h` to
`h + epsilon`; keep `H` at `h`, `AB` at `t1`, `R` at `t0`, and the tips at
zero. All seven edge durations are then positive. This arithmetic check is
not an inhabitant of the source `Calendar` type or a checked compilation of
its scheduled operations.

During a positive-length donor interval, edge 5's selected rate `1` is an
actual auxiliary-model rate: routed lineages can spend time there. It is not
automatically the target C-population rate `rC`. Its zero-duration placeholder
interpretation and any comparison to another positive edge-5 rate require the
separate unused-edge and common-continuation arguments.

Immediately before `h`, suppose the two programs have the **same original
code** and the actual support places A, B and C roots on edges 2, 6 and 4,
respectively, with no additional live roots. At `h`, both exit edge 6 and
route each B root at `H` using the same independent pulse coins. The
zero-duration program also exits edge 4, routes migrants across edge 5 and
enters the older C edge 1 at `D`. The positive-duration candidate leaves C
roots on edge 4 and routed B roots on edge 5 until `h + epsilon`, when both
exit to `D` and enter edge 1.

The key deterministic obligation is that, **if neither program has a real
merger in this window**, their original `Code` values agree immediately after
the delayed boundary at `h + epsilon`. That requires an actual source proof
that moving the C roots and applying the B-root pulse commute in this
placement, that the pulse coin indexing and law are unchanged, and that the
two exit/entry sequences preserve the same encoded forest and locations.
Graph inspection and a matching count of roots do not prove this identity.

### Candidate C-exit/pulse commutation on snapshots

The later source candidate (internal supporting file not included: `PulseExitCommutationDraft.lean`)
attempts one deterministic part of that obligation. It uses the original
[forest operations](https://github.com/Sodelin/Research-Commons/blob/14be42189b8a72fcaced51ceda4e86445dc09e90/packages/research/vendor/accepted/predecessor-check493/source-store/d6e5b2b57cf03091f8b5b5a2c80cf49de39bab938c50a467b46b30e08f12871d.lean)
and [finite snapshot definition](https://github.com/Sodelin/Research-Commons/blob/14be42189b8a72fcaced51ceda4e86445dc09e90/packages/research/vendor/accepted/predecessor-check493/source-store/4628112bbbc69528748bbc93f8a3f8200bc802a6e72417fb90c39e7acd49f744.lean).
These source bodies were read through their public text views in this pass;
their previously recorded source identities were not freshly hash-checked here.

Take one original forest state and a fixed bit table keyed by possible source
owner identifiers. Only owners actually at the hybrid use bits. An exit of an
edge `e` and that pulse should commute in their **encoded snapshot** when the
edge's source vertex differs from the hybrid and neither of the hybrid's
parent edges is `e`. For a live hybrid owner, the exit neither moves the owner
before the pulse nor moves either possible pulse destination afterward. For a
live owner on `e`, the pulse leaves it alone both before and after its exit,
because the exit leads to a different vertex. Every other live owner is
unchanged. Both orders retain the live set, the entire ancestor map, every
live genealogy, every live location and the register. The source's snapshot
encoding omits dead-owner fields and raw event history, giving the proposed
snapshot equality for a valid forest state.

In the selected graph, the C-tip edge is 4, its source is donor vertex 2, the
hybrid is vertex 3, and the pulse parent edges are 3 and 5; these distinctness
conditions are therefore the intended concrete specialization. The bit table
is a coupling device for current-owner IDs, not evidence of independent coins
per original copy. The raw event lists record the two operations in different
orders; this argument does **not** equate those lists or the timed paths.

The later encoded-operation candidate (internal supporting file not included: `PulseExitCodeCommutationDraft.lean`)
attempts to bridge those raw-state orders to the actual `exitCode` and
`pulseCode` operations. It treats states as equivalent only when their live
owners, full ancestor map, live genealogies and locations, and register
agree. It attempts to show that decode-after-encode and either operation
preserve this relation, then apply the snapshot equality to the two separately
re-encoded chains. The separate program specialization (internal supporting file not included: `PulseExitProgramCommutationDraft.lean`)
attempts equality of the immediate and delayed C-exit boundary sequences with
the same supplied owner bits and no operation inserted between their listed
boundaries. This separation keeps the generic encoded comparison independent
of the larger selected-pulse adapter without dropping the concrete statement.
Neither source assumes an arbitrary incoming `Code` has no dead-owner
snapshot fields. The raw-state specialization spells its six-owner carrier
as `Fin 6`; the existing `SampleLabel` is an abbreviation for that exact type.
This avoids importing the separate local ancestral-state development merely
to name the same carrier.

The candidates and their imports are unreviewed, unparsed and uncompiled.
None transports the Bernoulli product measure, instantiates the strict
scheduler or handles either short-window merger event. Those steps and the
full physical and observation correspondence remain open.

### Candidate common-owner coin law

The later coin-law candidate (internal supporting file not included: `PulseExitCoinLawDraft.lean`) attempts the next endpoint step. For a fixed original code `s`, put the provider's product Bernoulli measure on a table indexed by every possible original owner identifier. Restrict that same table to the **current** owners at the hybrid. The existing [product-restriction source](https://raw.githubusercontent.com/Sodelin/Research-Commons/14be42189b8a72fcaced51ceda4e86445dc09e90/packages/research/vendor/accepted/predecessor-check493/source-store/04a3a1c1f027903e62b77f966639c80da77aaa776871a0d9bd0657eac35b9e4f.lean) states that this restriction has the actual current-owner product law, including when the current-owner index is empty. Unused table entries are auxiliary; they do not give merged copies separate pulse choices.

Apply that restriction once for `s` and once for the actual code after the unrelated exit. Each marginal is the source's own independent pulse kernel. If the earlier deterministic code-commutation candidate holds for every full table, its two endpoint functions are pointwise equal; pushing the **same** table law through them gives the same immediate endpoint PMF. The draft attempts this generic result and the selected C-edge case after the common B-tip exit. The pinned [PMF map-composition interface](https://raw.githubusercontent.com/leanprover-community/mathlib4/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Probability/ProbabilityMassFunction/Constructions.lean) supplies the relevant formal operation, but source availability is not a qualified object or a proof receipt.

This is an unreviewed and uncompiled attempt conditional on its deterministic supplier and the provider's actual definitions. It does not identify a full scheduled program, insert a no-merger interval, construct a strict calendar, couple merger clocks, equate event histories or timed paths, or establish the genealogy/JC observation model. Equal endpoints alone do not imply any of those stronger results.

The pinned [Mathlib PMF/measure interface](https://raw.githubusercontent.com/leanprover-community/mathlib4/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Probability/ProbabilityMassFunction/Basic.lean) makes the typeclass boundary explicit: `PMF.toMeasure_injective` requires measurable singletons, and `Measure.toPMF` requires countability, measurable singletons and a probability measure. The draft uses measurability from the proposed restriction theorem and the provider supplies product-probability instances. The relevant finite-function-space instances and all elaboration remain to be checked; these visible interfaces do not establish that the candidate compiles.

### Candidate finite-source-program composition

The source-program candidate (internal supporting file not included: `PulseExitSourceProgramDraft.lean`) attempts to bind the preceding endpoint comparison through the same arbitrary finite suffix using the original [source program](https://raw.githubusercontent.com/Sodelin/Research-Commons/14be42189b8a72fcaced51ceda4e86445dc09e90/packages/research/vendor/accepted/predecessor-check493/source-store/d009fdfc510bfcaffaeea3bc241401eaf2996178ff4b82376eb22f1e49387831.lean). Its selected comparison starts from the same code and rates: the `h` operations `[exit 6, exit 4, pulse, exit 5, ordinary 1]` are compared with `[exit 6, pulse, exit 4, exit 5, ordinary 1]`, followed in each case by the same finite suffix. There is no interval between the swapped operations.

This attempt depends on the earlier coin-law and deterministic candidates and has not been independently reviewed or compiled. The suffix receives the encoded code at the join; the statement does not establish equality of the earlier raw histories. It does not supply the strict-calendar short-window comparison, a no-merger event, timed genealogy or JC observation correspondence.

## A conditional endpoint bound

Set `m = max(1, rA, rB, rC, rAB, rR)` and `L = 15 m`. The pinned
uniformized source interface (internal supporting file not included: `UNIFORMIZATION-EVENT-CORRESPONDENCE.md`)
uses ordered distinct-root choices with rate one half of their population's
pair rate. At most six roots are live; consequently, if each root belongs to
at most one eligible population, the sum of all real choice rates is at most
`L`. This is a proposed combinatorial bound for the **actual** `Code` and
`Choice` types, not a replacement for the provider's separate uniformization
bound. Dummy uniformization ticks are not real mergers.

For this plan I reread the selected `Choice`, `choiceRate` and `totalRate`
declarations in the pinned source and the `actual_source_kernel_no_merger`
declaration in the pinned holding-clock source through their public text
representations. Their byte identities were recorded in the existing
uniformization note; this later reading did not freshly hash the bodies or
qualify their Lean objects. The proposed sharper bound and its disjointness
premise remain to be proved for the selected source state.

Assume the stated placement, the deterministic identity above, and a
source-law construction that shares the pre-pulse state and the B pulse
coins. Assume also that each interval's actual no-merger probability obeys
the retained fixed-state survival formula. Conditional on the common
pre-pulse state and coins, each program has a real merger in the window with
probability at most `1 - exp(-L * epsilon)`. Coupling the two interval laws
and using the union bound would therefore give, for their endpoint-code laws
immediately after `h + epsilon`,

$$
\sup_A |\mu_\epsilon(A)-\mu_0(A)|
\leq \min\{1,\,2(1-e^{-L\epsilon})\}
\leq 2L\epsilon.
$$

The first expression uses the supremum-over-events convention for total
variation. To turn this conditional hand argument into a source result, one
must prove the actual rate bound and placement, construct the coupled pulse
and no-merger branches on the same original code type, and show the actual
strict-calendar scheduler produces the described operations. The weak
program's interval from `h` to `t1` must also be split at `h + epsilon` using
the **actual** source-kernel semigroup or an equivalent path result. Those
facts have not been checked here. If both endpoint laws then use one identical
later Markov kernel, the same total-variation bound passes to that later
endpoint; that premise and the ancestral continuation remain to be proved.

An unreviewed [finite-kernel alternative](PULSE-ENDPOINT-KERNEL-BOUND.md)
would bound the two endpoint differences from the source kernels' diagonal
probabilities, using the original provider's global rate bound. Conditional
on the instantaneous boundary-law equality and a common later kernel, this
would avoid constructing a joint clock coupling for the endpoint estimate.
It does not establish those premises, the strict scheduler, the Lean result or
any timed-path or biological observation correspondence.

The existing time-semigroup candidate (internal supporting file not included: `PulseTimeSemigroupDraft.lean`)
already attempts the relevant generic endpoint split in
`msci_source_program_split_before_tail`. Its premises include the same
original network, rates and starting code, a fixed finite prefix and tail, and
nonnegative durations `t ≤ b`. The selected zero-edge program places an
interval `b = Real.toNNReal (t1 - h)` immediately after `concretePulseAtH`;
the intended application uses `t = Real.toNNReal epsilon`, with the tip
operations and pulse group in the prefix and the later A/B and root operations
in the tail. That is a proposed instantiation, not a checked equality for the
selected program. The generic source and its imports remain unreviewed and
uncompiled; they neither construct the positive-duration scheduler nor prove
the no-merger coupling or a timed-path correspondence.

## Why this is not raw-path total-variation convergence

Under the described physical occupancy semantics, the positive-duration
program has an edge-5 root at time `h + epsilon/2` whenever at least one
current B root takes the donor route. Mergers on that edge do not move its
last root out of the edge. With at least one B root and independent donor
probability `g`, this event has probability at least `g > 0`. In the
zero-duration program edge 5 is empty throughout the open interval after
`h` and before `t1`, so the corresponding event has probability zero.

Thus, **if** both full physical paths and this occupation event are constructed
as described, their raw edge-labelled path laws have total-variation distance
at least `g` for every such epsilon. The event may depend on epsilon; the
supremum defining total variation allows that. This is a conditional hand
observation, not an established source theorem. It shows why an endpoint
bound cannot be promoted to total-variation convergence of full physical
records. A timed-genealogy or sequence comparison would need an explicit
observation map that forgets the transient edge label, a coupled marked-path
argument, and the shared-genealogy JC construction. Those joins, the
Jacobian and interval claims, and the full manuscript proof remain open.

## Subsequent source/hand review

Dot's r34 return (internal supporting file not included: `subspace-msci-delivery-20261031.md`) conditionally accepts the rate-bound and endpoint-coupling arguments and the contrasting raw-path obstruction in the original plan at commit `755c2d07c72c1e5a32549bf484571891dbff9d81`. It does not instantiate the source scheduler or prove the full-Code boundary/pulse commutation, actual coin transport or kernel split. An endpoint result still does not identify the accumulated genealogy or JC observations. The review is an AI source/hand assessment, not Lean qualification or independent human review.

## Original focused review question

After the existing r33 trace-law review, a useful expert comparison would
check the exact source scheduler, actual pulse-index set and `Code`
transport identities above. A counterexample to the no-merger endpoint
identity would invalidate this particular route. A successful conditional
hand review would still leave Lean elaboration, the source-kernel split,
raw-path projection, external object closure and compiler-owner selection
unresolved. The subsequent r34 review is recorded above; no compiler job follows from it.
