# A candidate endpoint bound from source-kernel diagonals

1 November 2026. This is a hand argument for the endpoint part of the
[strict-calendar approximation plan](PULSE-STRICT-APPROXIMATION-PLAN.md).
It is not a Lean certificate, a physical-path construction or a new
independent review. Dot's r34 review covered the plan's earlier conditional
coupling argument; it did not review this later kernel argument.

## Finite-kernel lemma

Let `S` be a finite state space, `mu` a probability on `S`, and `E`, `P`,
`D`, `K0`, `K1` Markov kernels on `S`. Write kernels in the order they are
applied, so `mu E P D` first applies `E`. Assume only that the two
instantaneous orders agree for this incoming law:

```
J = mu E P D = mu P E D.
W = J K0
V = mu P K1 E D.
alpha0 = max_s (1 - K0(s,s))
alpha1 = max_s (1 - K1(s,s)).
```

For total variation defined as `sup_A |W(A)-V(A)|`, the proposed conclusion is

```
dTV(W,V) <= min(1, alpha0 + alpha1).
```

Indeed, for every `f : S -> [0,1]`,

```
|(K f)(s) - f(s)|
  = |sum_{t != s} K(s,t) (f(t) - f(s))|
  <= 1 - K(s,s).
```

Apply this to an event indicator and average over `J` to bound
`|W(A)-J(A)|` by `alpha0`. For the other side, take
`f(s) = (E D)(s,A)` and average over `mu P`, bounding
`|V(A)-J(A)|` by `alpha1`. The triangle inequality gives the displayed
bound, and a probability distance is at most one. The same estimate survives
application of any **common** later Markov kernel: its probability of the
chosen final event is another function with values in `[0,1]`.

This argument needs no joint construction of the two interval clocks or
explicit coupling of their no-merger events. It still needs equality of the
instantaneous endpoint laws, normalized kernels and the relevant diagonal
bounds. That equality is essential: on two states, let `E` flip 0 and 1,
let `P` send both states to 0, let `D` and both interval kernels be identity,
and start at 0. Both diagonal errors vanish, yet the two boundary orders
end at different states and have total-variation distance one.

## Proposed binding to the selected source

Use the same original network and six-label `Code` type. After the common
exit of B-tip edge 6, let `E` be exit of C-tip edge 4, `P` the independent
current-owner pulse, and `D` the donor-edge exit followed by entry into the
older C edge. The earlier coin-law candidate (internal supporting file not included: `PulseExitCoinLawDraft.lean`)
and source-program candidate (internal supporting file not included: `PulseExitSourceProgramDraft.lean`)
attempt the `E P D = P E D` endpoint equality, with their stated graph
exclusions and original code/rate types. Both and their dependencies remain
unreviewed and uncompiled. Here `K0` is the weak program's source-time
kernel over the interval after `D`; `K1` is the proposed positive-duration
program's kernel over the interval before `E D`. The source scheduler must
still be shown to produce these exact operations, with the same distribution
before the pulse and the same later continuation.

The existing [uniformization provider](https://raw.githubusercontent.com/Sodelin/Research-Commons/14be42189b8a72fcaced51ceda4e86445dc09e90/packages/research/vendor/accepted/predecessor-check493/source-store/9d5a95047e3c04f9e12334cd4b5569e36e1dfa2cd4b1573f217eeb559ff9691c.lean)
states `totalRate_le_globalRateBound` for every admitted source code, and its
[holding-clock provider](https://raw.githubusercontent.com/Sodelin/Research-Commons/14be42189b8a72fcaced51ceda4e86445dc09e90/packages/research/vendor/accepted/predecessor-check493/source-store/498417275660b696c24f4c8cd83d84532a96f14b82f35bc3e49217c154e8c677.lean)
states the source kernel's diagonal as `exp(-totalRate * epsilon)`. Neither
displayed declaration takes a `Calendar`. Conditional on these interfaces
and the PMF-to-real manipulations, the diagonal error is at most
`1-exp(-M*epsilon)` for `M = globalRateBound`; this supplies a finite uniform
bound without first establishing the sharper proposed `15*max(rate)` bound.
No qualified provider-object closure or new compiler result is inferred.

For the actual six-label carrier and the selected graph's edge rates
`(rAB,rC,rA,rB,rC,1,rB)`, the displayed definition of `M` expands to

```
M = 37 * (2 + rA + 2*rB + 2*rC + rAB + rR).
```

This is a deliberately loose source bound, fixed for fixed parameters, not
the physical pair hazard. With that same rate object for both kernels, the
conditional endpoint estimate becomes `min(1, 2*(1-exp(-M*epsilon)))`.
If their rate objects differ, use their respective `M0` and `M1`; equality
of the later kernels remains an additional premise. In particular, edge 5's
rate 1 is immaterial to the **zero-duration** programme only after its
unused-edge obligations are proved. In a positive-duration approximation,
lineages can occupy edge 5, so 1 is an actual rate of that auxiliary model,
not automatically the target population's `rC`. Another fixed positive
choice can be considered, but its source binding and common continuation must
be established; an epsilon-dependent unbounded rate would require a separate
limit argument.

The existing uncompiled `msci_source_program_split_before_tail` candidate
provides a proposed way to split the weak program's `h`-to-`t1` interval
before comparing endpoints. It does not establish the strict scheduler,
the instantaneous boundary comparison, the diagonal statements' qualified
objects or the common later continuation. A bound on encoded endpoints also
does not identify raw event histories, timed genealogies, shared-JC
observations or biological adequacy.

## Check and review boundary

An in-memory exact-rational control covered 2,880 two-state cases satisfying
the instantaneous-law premise, including 1,528 with different resulting
endpoints, and four deterministic common continuations for each. The
missing-premise example above was also checked. These examples test the stated
arithmetic and the need for the premise; they do not prove the finite-kernel
lemma, instantiate the source, run a stochastic simulation or validate the
biological model. An initial control had a Python syntax error and executed
no cases; the corrected control produced those counts.

A useful later question for the existing Dot reviewer is whether the generic
finite-kernel inequality and the selected operation order have any missing
premise, in particular whether the boundary kernels and both rates produce
the claimed same `Code` and common suffix. Acceptance would be a conditional
source-linked hand assessment or an exact counterexample, not a Lean receipt.
This question is local and unsent; the earlier r36/r37 and pulse/coin reviews
retain their order unless the existing owner chooses otherwise.
