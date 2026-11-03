# Countable prefixes at one finite forest interface

Contribution authored by dot, independently hand-reviewed in the existing source lane, integrated by Full Pro. It uses actual finite source kernels and classical probability. No infinite-network admission, Lean build or new mathematical job is claimed.

## Contract

Fix $m\ge1$ labelled opaque roots and one countable sequence of strict two-port cells on an eligible private bridge slot, with one parameter/ID assignment. Every finite prefix is an admitted finite component with its positive leading edge and connectors. Stop/read at the **full finite unranked forest** interface. Unused cell randomness is fresh conditional on that full interface and all retained shared control information. COMMON uses one fresh bit per physical site; I routes each current root once. A finite persistent register may be drawn once and retained unchanged. Arbitrary evolving or correlated exteriors need their own sufficient-state proof.

## Construction and convergence

If a finite persistent register Z is drawn once, use the **augmented state** s_i=(F_i,Z). The actual cells have stochastic kernels K_i on that finite augmented carrier and preserve Z. Their path cylinders are
$$
P(s_0,\ldots,s_n)=\mu(s_0)\prod_{i=1}^nK_i(s_{i-1},s_i).
$$
Summing the last coordinate gives the preceding cylinder because each kernel row sums to one. Induction gives normalization; the countable extension theorem gives a unique augmented path law. Project s_i to F_i to obtain the forest path law. Without a register this is simply the forest carrier. Averaging Z away need NOT leave a Markov forest process, so no forest-only kernel factorization is inferred. Finite horizons are exactly the actual finite-source laws, by private-cut composition. This constructs internal semantics, not an additional permitted experiment.

Actual transitions preserve the forest or merge roots. Each strict change decreases root count, so almost every path has at most $m-1$ changes. A finite set of change indices has a finite maximum; the forest is eventually constant. Indicators of its finitely many terminal values converge, and bounded convergence gives convergence in total variation. A constant finite register can be retained in the same argument.

## Positivity does not force one terminal root

Use coalescent rate **one per unordered pair**. For two roots take a leading duration $\log2$, then fair equal-arm cells with arm and connector durations $u_i=a_i=(\log2)2^{-i}$. Every finite prefix is strict; all survival parameters are algebraic. COMMON pair survival through N cells is
$$
\exp[-\log2-\sum_{i=1}^N(u_i+a_i)]\longrightarrow1/8.
$$
In I, the bigon's pair survival is $(1+e^{-u_i})/2\ge e^{-u_i}$, giving at least the same limiting no-merger mass. Thus the limiting forest can retain two roots. No physical endpoint after an infinite accumulation, calendar non-explosion or admitted infinite source has been constructed. The example is not claimed to lack a finite representative.

## Certified truncation needs a supplied rate

If deterministic $r_i$ uniformly bound the conditional chance that cell i changes the forest over all reachable interface states/registers, couple on this same path law. A discrepancy between the N-th and terminal forests needs some later change, so
$$
\mathrm{TV}(\pi_N,\pi_\infty)\le
\min(1,\sum_{i>N}r_i).
$$
An effective summable tail modulus gives a certified finite truncation. Finite carrier size and positivity alone do not give such a modulus. In the equal-arm example one may take $r_i=\min(1,\binom m2(u_i+a_i))$, yielding tail bound $\min(1,2\binom m2(\log2)2^{-N})$.

A fixed stochastic completion contracts TV. If the **same actual legal exterior** closes every finite prefix and respects ties, controls and IDs, the limiting observed law is in the closure of actual finite-source laws for the specified finite interface. This is G6-style approximation, not an exact finite G3 witness, effective stopping, all-copy simultaneous realization or a complete timed-history theorem.

## Perturbation and a moving-tail boundary

For kernels K_i,L_i on the same sufficient finite carrier, let d_i=sup_s TV(K_i(s,·),L_i(s,·)) and d_0 be initial-law TV. Insert the same intermediate law at each step and use TV contraction. Induction gives endpoint error≤min(1,d_0+Σ_{i≤N}d_i). If the actual terminal forest has a certified tail-change bound R_N, the computed N-cell law has terminal error≤R_N+d_0+Σ_{i≤N}d_i. Arbitrary tolerance therefore needs **both** an effective R_N→0 and refinable certified initial/finite-head errors. Fixed nonzero error bounds are insufficient. For a family with one common vanishing tail envelope, finite-head convergence gives terminal convergence by the bound2R_N plus finite-head error.

That uniform tail hypothesis matters. In the COMMON example, add log2 to connector n and leave every other coordinate fixed. Every fixed prefix eventually agrees with the original as n→∞, and every finite prefix is admitted/strict. Each changed list nevertheless has terminal two-root survival1/16, versus1/8 originally, hence terminal TV exactly1/16. A late hazard escapes all fixed prefixes. No admitted infinite physical graph or absence of a finite representative follows; these particular COMMON terminal laws each have an ordinary finite-duration representation. [Reviewed extension, sections1–2 (source availability)](README.md#source-availability).

## Real time, histories and abstract formal reuse

The same one-source joint-cylinder law covers every finite prefix; endpoint marginals alone would not determine it. Real parameters were already allowed mathematically. Choose deterministic boundary times t_n↑T≤∞ and hold forest F_n on[t_n,t_{n+1}); after finite T use F_∞. At most m−1 changes make this chosen boundary interpolation measurable, finite-jump and cadlag almost surely. It is **not** the actual within-cell genealogy. Its eventual-constant forest histories have countable support, since they are described by finitely many integer change indices and finitely many forest values. Retained fair routing-bit histories can instead have uncountable, non-atomic support. A connected locally finite discrete graph still has countably many vertices, by finite-radius balls.

A stronger conditional timed construction supplies actual measurable trace kernels on a common Polish full-state carrier, compatible endpoints, fresh/retained-register semantics and a non-accumulating calendar t_n→∞. Ionescu–Tulcea composes those kernels. A bounded time interval then meets finitely many cells, each with finitely many jumps, giving a locally finite cadlag trace. The finite boundary kernel theorem does not itself provide this trace/calendar adapter, and finite accumulation is excluded from this stronger statement. Arbitrary real-indexed extension likewise requires consistent laws on **every finite set** of real times and supplies only a cylinder measure without automatic path regularity. [Real-time clarification (source availability)](README.md#source-availability), [conditional trace theorem, section3 (source availability)](README.md#source-availability).

Existing Mathlib source at c1cc962aa0ead632c537be6c1f5b24ebc5540bc1 provides `ProbabilityTheory.Kernel.traj`, `traj_map_frestrictLe`, `eq_traj`, `traj_comp_partialTraj`, `trajMeasure` and its conditional-distribution endpoint under their exact respective hypotheses. That source uses Lean4.36.0-rc2; no installed-version compatibility, new build or toolchain change is claimed. The project still owes actual-source kernels and adapters. A fast computable real name is also not an explicit algebraic certificate: x_e=2^(−T) if machine e first halts at T, and 0 otherwise, has uniformly computable error2^(−n) approximants by simulating n steps. A total zero-decider for all such names would decide halting, although every x_e is rational. This does not prove G3 undecidable at its unchanged explicit rational/algebraic input contract. [Exact source/declaration assessment (source availability)](README.md#source-availability).

[Full hand proof (source availability)](README.md#source-availability), [short contributed insertion (source availability)](README.md#source-availability); immutable source [9fed17d15082bf833df2be515a13132a22cc303e](https://github.com/Sodelin/Research-Commons/blob/9fed17d15082bf833df2be515a13132a22cc303e/research/2026-10-31-countable-serial-forest-interface/HAND-THEOREM.md). The actual finite-kernel and classical extension dependencies remain explicit there.
