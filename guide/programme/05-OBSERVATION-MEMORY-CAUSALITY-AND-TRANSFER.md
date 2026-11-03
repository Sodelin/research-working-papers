# Observation, memory, causality and transfer

These programmes share a small set of mathematical questions: when does an observation lose a needed distinction, when does a quotient preserve dynamics, and when can one experiment simulate another? Their scientific source assumptions remain separate.

## Exact deterministic memory

**CB-MEMORY-001.** Let $T_a:X\to X$ be total dynamics and $c:X\twoheadrightarrow R$ an encoding. A unique reduced update exists iff
$$
c(x)=c(y)\Longrightarrow c(T_ax)=c(T_ay)\quad\text{for all }a.
$$
Necessity substitutes a reduced update. For sufficiency set $\bar T_a(c(x))=c(T_ax)$; fibre compatibility makes this well-defined, and onto makes it unique. Induction gives preservation under every finite action word.

For a fixed output $o$, define $x\sim y$ iff every finite action word, including the empty word, gives the same output from them. This is an equivalence relation stable under every action. Its quotient is an exact output-preserving system. Any onto exact output-preserving representation identifies only $\sim$-equivalent states, so it factors uniquely and surjectively onto this predictive quotient. If depth-$k$ agreement is globally stable at depth $k+1$, induction on words proves it already equals full-future agreement. Sampled agreement on some pairs is insufficient.

In the wait/prime/probe/reset instance, a visible bit and one retained parity bit commute with all four actions on arbitrary finite initial records. A probe distinguishes the two parities at the same visible value; the empty observation distinguishes visible values. Thus exactly four predictive classes exist and are reachable. No fixed suffix window determines parity on all records: prepend one toggling record outside the window. The argument depends on the available probe. Feedback preservation also requires the actual controller to factor through the retained state/history.

**CB-MEMORY-002.** Present membership does not determine predecessor-restoring split. Merge $0,1$ then with 2, or merge $1,2$ then with 0; keep site 3 separate. Both legal histories yield $\{\{0,1,2\},\{3\}\}$. Splitting the same composite into its immediate predecessors yields respectively $\{\{0,1\},\{2\},\{3\}\}$ and $\{\{0\},\{1,2\},\{3\}\}$. Therefore the partition map fails fibre compatibility even on states where the split is admissible. This is not a totalization artefact. The checked tree/list-adjacency theorem and the separately scoped 2×2 implementation check are different evidence.

## Stochastic memory and complete histories

**CB-MEMORY-003.** For countably supported kernels $K_a(x)$ and onto $q$, an exact reduced kernel exists uniquely iff $q_*K_a(x)$ is constant on every $q$-fibre. Define it by a representative; the condition removes that choice. Necessity follows by evaluating the commuting equation. Testing all point-mass initial laws shows equivalence with one-step preservation for **all** initial laws; one favourable initial mixture is weaker.

Push the actual initial law through $q$, decode outputs, and require the action policy to depend on the full retained history. Induction using conditional action selection and the kernel equation preserves the complete finite state/action and observation/action transcript, including initial and terminal observations. For a noisy sensor, apply the condition to the **joint** next-state/measurement kernel. A copied fair bit and a fair bit with its complement have identical marginals but opposite equality events, showing why separate marginal conditions fail.

Full output predictions need not themselves be a commuting state quotient. The six-state counterexample is
$$
s\to\tfrac12u+\tfrac12b,\quad t\to c,\quad
u\to u,\quad b\to v,\quad c\to\tfrac12u+\tfrac12v,\quad v\to v,
$$
with output 1 only at $v$. From $s,t$, every finite output trace is the same half-mixture of $000\cdots$ and $00111\cdots$. Their next predictive-profile laws differ: $t$ goes certainly to the profile of $c$, whereas $s$ goes to the distinct profiles of $u,b$. No kernel on those profiles commutes with the actual transitions. This does not exclude another Markov realization of the same outputs. [Source and exact declaration map](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/e2502c82ab9a77c00543932f775a71e5374221f7/research/open-problems/time-self-reference/predictive-memory/STOCHASTIC.md).

**CB-MEMORY-004.** In $n$ independent fully observed trials, compare impossible success with a known success rate $0<e<1$. Put $q=(1-e)^n$. If the all-zero sample triggers the rare model with probability $a$, the errors satisfy $\alpha=a$, $\beta\ge q(1-a)$. Therefore
$$
\min(\alpha+\beta)=q,\qquad
\min\max(\alpha,\beta)=q/(1+q),\qquad
\min\text{equal-prior error}=q/2.
$$
Always choose the rare model after a success; choose it with probability 0 or $q/(1+q)$ after all zeros to attain the two respective optima. This includes $n=0$. For fixed $e$, error tends to zero but never gives finite certainty. With arbitrarily small $e$, no fixed $n$ uniformly beats worst error $1/2$. A supplied $e_{\min}>0$ gives the explicit all-zero bound $(1-e_{\min})^n$, not certainty.

## Statistical transfer

**CB-TRANSFER-001.** A single parameter-independent Markov kernel $K:X\rightsquigarrow Y$ simulates source experiment $P_\theta$ as target $Q_\theta$ with error $\sup_\theta\mathrm{TV}(KP_\theta,Q_\theta)$. TV contracts under a kernel, so every bounded target decision incurs at most its loss range times this error.

For arbitrary nonempty measurable spaces, an ordinary kernel is equivalent to a positive unital linear map $T:B_b(Y)\to B_b(X)$ with pointwise continuity from above on indicators. Set $K_x(A)=T1_A(x)$. Positivity gives finite additivity; applying continuity to decreasing tail unions gives countable additivity. The actual bounded-measurable codomain gives measurability of $x\mapsto K_x(A)$. Uniform simple approximation recovers integration of every bounded measurable function. Without countable additivity or pointwise measurable representatives, an abstract operator need not be an ordinary kernel.

If the whole source family has one common dominating probability and $Y$ is standard Borel, the minimum deficiency is attained. Its decision dual is the supremum, over **finitely supported priors, finite action sets and losses in[0,1]**, of optimal SOURCE Bayes risk minus optimal TARGET Bayes risk. This direction matches simulation from source to target; the normalization matches TV in[0,1]. Compactify $Y$ into a compact metric space. Positive unital operators have weak-star compact coordinates; their linear/order constraints are closed. A countable dense function family permits one null-set repair and Riesz representation gives a measurable kernel. TV is a supremum of continuous tests, hence lower semicontinuous, so the uniform error attains its minimum; finite parameter constraints have the finite-intersection property. Minimax and finite action approximations give that risk dual. A measurable repair from the compactification back to $Y$ cannot increase TV. Common domination makes the repaired null set harmless to every parameter. This is not an effective algorithm for arbitrary spaces. [Full representation review](https://github.com/Sodelin/Research-Commons/blob/f87a6c50029c1ae13f0340818b3bf358b1bf3de3/research/2026-09-30-general-transfer-closure/REVIEW-dominated.md).

For a hidden answer $a(\theta)$, use target $\delta_{a(\theta)}$. Since $\mathrm{TV}(R,\delta_a)=1-R\{a\}$, simulation is exactly randomized answer recovery. Exact randomized recovery has one deterministic measurable decoder: the Dirac embedding of a standard-Borel answer space has a Borel inverse on its image. Different answers therefore require disjoint measurable recovery regions; pairwise singularity alone does not construct such regions for arbitrary uncountable families. The binary lower bound is $(1-\mathrm{TV}(P_1,P_2))/2$. A source sequence approaching a different-answer source in TV defeats uniform finite-sample error below $1/2$, by product coupling. None of these theorems validates an unspecified scientific observation map.

**CB-TRANSFER-002.** A fixed simulator valid outside one prior-null set extends to every parameter if the prior has full support, the source family is setwise continuous and the target family is weakly continuous on a Polish target. A violating continuous bounded test would define a nonempty open parameter set; full support gives it positive mass, a contradiction. Weak source continuity alone does not control an arbitrary measurable $Kf$.

For sequential standard-Borel laws, exact whole-history equality is equivalent to equal initial laws and equal next-observation kernels almost everywhere under the common prefix law at each step. Necessity uses a countable generating class; sufficiency inducts over cylinders. For possibly different initial laws put d_0=TV(P_0,Q_0), and let e_i∈[0,1] uniformly bound the conditional next-step TV over matching histories. Prefix TV obeys
$$
d_{i+1}\le d_i+(1-d_i)e_{i+1},
\quad d_m\le1-(1-d_0)\prod_{i=1}^m(1-e_i).
$$
Split prefix measures into their common submeasure and residuals to prove the recurrence. Equal initial laws give d_0=0 and the familiar product bound. Finite cylinders approximate all events under $(P+Q)/2$, so full-path TV is the supremum of prefix TVs and the product bound passes to infinity. A deterministic zero path versus independent Bernoulli coordinates attains it. Constant positive step error can give infinite-path TV one.

**CB-TRANSFER-003.** On finite alphabets and an effectively covered parameter class, one exact rational primal/dual pair certifies uniform transfer. For a grid, let $U$ be a feasible kernel's maximum empirical-law TV error and $L$ a feasible dual value. Let joint law errors sum to $\rho$, covering radius be $r$, and source/target TV moduli be $\omega_P,\omega_Q$. Then
$$
\max(0,L-\rho)\le\delta\le
\min(1,U+\rho+\omega_P(r)+\omega_Q(r)).
$$
TV contraction bounds law perturbation by $\rho$; restrict to the grid for the lower bound and use its covering point and the **same** kernel for the upper bound. A dual witness $\lambda_i\ge0,\sum\lambda_i=1,0\le v_{iy}\le\lambda_i$ has value
$$
\sum_{iy}v_{iy}\widehat Q_i(y)-
\sum_x\max_y\sum_i\widehat P_i(x)v_{iy},
$$
obtained by minimizing each stochastic row. Hoeffding plus a finite union bound supplies simultaneous coordinate errors; repeated inspection uses summable failure budgets. If cover, law errors and primal-dual gap shrink, the interval converges; strictly separated thresholds eventually resolve, equality need not. Compactness alone supplies none of the effective access or scientific premises.

## Restricted causal interventions

**CB-CAUSAL-001.** For the specified finite DAG model with binary-valued variables, arbitrary finite latent/selection carriers, selection sinks, available target set $T$, $U=X\setminus T$, put n=|X|, k=|T|, u=|U|. Require a positive rational baseline/soft-intervention registry jointly satisfying **full-vertex selected elementary-pair faithfulness on the original and every separate augmented carrier**, not merely faithfulness of the observed margin. The full marked TCM class is recoverable with
$$
B=k(n-1)+\sum_{\{x,y\}}2^{|U\setminus\{x,y\}|}
 +\sum_{t\in T,x\ne t}2^{|U\setminus\{x\}|},
\qquad 2B\le5n(n-1)2^{|U|}.
$$
These are elementary exact-population CI/invariance queries, not laboratory intervention counts or samples.

**Proof chain.** Exhaust the named baseline separation and target-invariance coordinates in this finite family. The accepted closest/discriminating-path and refined-family lemmas show that their equality determines the entire graphical signature and full marked target class. A canonical-source representation simultaneously preserves that signature across **all** separate targets; finite enumeration therefore outputs exactly its class, not independently realizable slices. The physical-source supplier proves nonvacuity on each original DAG: an active-path/activation-branch circuit gives a nonzero CI minor; finitely many such minors exclude proper polynomial zero sets, and density supplies one positive rational CPT registry faithful to all required augmented graphs at once. Untargeted mechanisms are shared. Count the literal finite subsets to obtain $B$. The deeper path-splicing/canonicalization cases remain named proved suppliers in the [complete cumulative hand review](https://github.com/Sodelin/Research-Commons/blob/174168effef1efc5be13d941814c51520de9a8cb/research/2026-10-22-dot-restricted-causal-interventions/CAUSAL-FULL-UPPER-CUMULATIVE-HAND-REVIEW-20261023.md). Its Lean source is explicitly **unelaborated**; mathematical hand acceptance is not parser/kernel acceptance. Binary-valued does not mean binary-degree.

**CB-CAUSAL-002.** For $k>0,u\ge2$, put $M=\binom u2 2^{u-2}$. The admitted hard family has a baseline and $M$ different-target rivals, each changing exactly its own elementary query class and agreeing on every other legal query. After fewer than $M$ paid queries along the fixed baseline transcript, some rival is untested and realizes that **whole** transcript. Thus $M$ is necessary, and querying all indices attains it on the explicit $M+1$-source promise.

For a random seed and each rival index $q$, never testing $q$ forces an error on the baseline or that rival under the same-seed coupling. Uniform per-source error $\le\varepsilon<1/2$ therefore gives $P(\text{test }q)\ge1-2\varepsilon$. Summing the finite index indicators and bounding them by actual paid queries yields extended expectation $\ge M(1-2\varepsilon)$ on one fixed baseline. Infinite querying has infinite cost; silent divergence is failure. No independent seeds per source, finite-mean or almost-sure-termination premise is needed. The crucial source/signature/target witness is supplied by the reviewed physical hard family, not an abstract answer table.

**CB-CAUSAL-003.** If $T=\varnothing$, its literal TCM-union target is the empty graph. Every source has that one target, so zero queries suffice. The positive-target lower proof genuinely uses $k>0$.

## The compact soft-science library: all 85 selected declarations

The five canonical groups below comprise all 85 declarations of the retained theorem map, including support lemmas, examples, reused endpoints and integrity checks, not85 discoveries. They are small formal models, not empirical psychology/sociology conclusions. The exact map is [THEOREM-BY-THEOREM.md](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/8e665d2a9f6168e6448b2ca49fccbec87d57d3ad/research/publication-audit-2026-09-29/THEOREM-BY-THEOREM.md),27311bytes/SHA3a1aa6850eee94cfb27a1017b2bfb000476cd714c8c3990f11e0537e46be750e, with [machine-readable signatures/source hashes](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/8e665d2a9f6168e6448b2ca49fccbec87d57d3ad/research/publication-audit-2026-09-29/theorem-audit.json). It binds the 85 declarations at source 7835157627548823f03f29dd3987e55601807b55. The grouped elementary arguments, including the support cases below, avoid repeating the same algebra under each name.

**CB-SOFTSCI-001 (27 declarations).** On $\mathbb Z^2$, a sum loses the component: $(a,b)$ and $(a+1,b-1)$ agree. Sum plus first coordinate recovers the second by subtraction. Extra probes can only shrink an equivalence fibre; postprocessing can only enlarge it. In response $r=a+b$, subtract the two responses and rearrange a supplied bias interval to obtain the latent interval; a bias bound smaller than the observed gap fixes the sign. Adding a correct exact label retains a fitting truth and deletes a disagreeing rival; a wrong label deletes truth; conflicting labels make the fit empty; duplicated identical equations change nothing. These prove the nine identifiability, nine measurement and nine learning declarations.

Equality at every probe is reflexive, symmetric and transitive and restricts to smaller designs. An empty design equates every pair; it identifies parameters only if their type is subsingleton. A common intercept preserves order and cancels from differences. Compensated latent/intercept shifts preserve every response, including population functions by extensionality. A known intercept identifies the latent value; a known latent anchor identifies the intercept. Latent0/bias2 versus latent1/bias0 exhibits reversal. The order theorem needs only an **upper** differential-bias bound strictly smaller than the observed gap, not a symmetric absolute bound. Empty evidence fits every hypothesis; cons adds one equation and append conjoins fits, so list inclusion gives evidence monotonicity. A nondiscriminating new label need not shrink the fibre strictly.

**CB-SOFTSCI-002 (six declarations).** Models $Y=T$ and $Y=U$ agree observationally under $T=U$. At intervention $T=1,U=0$ they differ, with effect numerators 2 and 0. Any estimator of that numerator from the common observational function would return both numbers, impossible. Full response-function equality identifies that function. Calling the numerator twice an average effect additionally needs uniform Boolean background.

**CB-SOFTSCI-003 (26 declarations).** Successor/predecessor steps connect any two naturals by walking up/down, and successors give unbounded reach; each neighbour lies in the stated two-element set. Overlapping membership and empty trust are direct constructions. Subtract contributing and withdrawing payoffs: mutual contribution is weakly stable exactly when sanction covers cost. With integer transfers, acceptable shares are exactly $[\mathrm{cost}_A,\mathrm{budget}-\mathrm{cost}_B]$, nonempty iff total cost does not exceed budget. Positive total surplus need not make an arbitrary offered share acceptable. Fixed capabilities and outside options are premises, not consequences of graph connectedness.

Membership nesting is transitivity of the supplied inclusions. Positive cost with zero sanction fails stability. Different/equal labels and constant markers merely attach functions absent from the payoff. Mutual contribution improves on mutual defection iff cost<benefit+sanction, a separate subtraction from unilateral weak stability. For fixed capabilities, a witness remains after adding members. Restricting participants preserves retained participation inequalities, not necessarily task coverage; acceptance of a union is acceptance of both groups. Removing the only capable agent for a specified task removes every witness. Two Boolean specialists jointly cover both roles while neither alone does. Costs(1,1),rewards(0,3) have total surplus but refusal; rewards(1,2) restore participation while preserving coverage. Transfers are unrestricted **signed integers**, outside options zero. At vertex0 the actual neighbour is1; truncated Nat subtraction makes the stated containing set{1,0}, not two actual neighbours. Empty task sets are feasible vacuously; the indispensable-member argument explicitly supplies a task.

**CB-SOFTSCI-004 (eight declarations).** Cross multiplication verifies $9/10>80/100$, $20/100>1/10$, but pooled $29/110<81/110$. This is a concrete Simpson reversal with positive denominators. Adding two supplied weak integer inequalities preserves their order. Component nonidentification and recoding reuse the preceding fibre arguments; they are not independent discoveries or arbitrary weighted-rate/causal-adjustment theorems.

**CB-SOFTSCI-005 (18 declarations).** In the fixed four-time Boolean danger fragment, avoid behaviour produces identical complete records in both states, so no classifier can be correct on both; approach records differ and are injective. For the scaled implicit observation columns, sum the entries to obtain mass $10u$; the explicit bounds $0<u,0\le c\le10u$ give nonnegativity. Subtract the two approach columns: equality is exactly $c=u$, or normalized CABi $=0.1$. The four source-table equalities are direct substitutions into the fixed sensory/affective/transition/implicit tables. They do not verify the upstream MATLAB/SPM execution, clinical validity or adaptive learning outside this fragment.

The transitions reduce to start–stimulus–approach–interact and start–stimulus–avoid–safetyCost. At c=u the implicit safe/danger maps coincide at **every phase** for arbitrary integer parameters; avoidance columns ignore c. Probability normalization additionally needs u>0 and the bounds above; u=c=0 gives equality but zero mass, not CABi. Separately the explicit-prior pair(scale−safe,safe) is nonnegative with total scale if0<scale and 0≤safe≤scale. This is not the 10u implicit identity. “Complete records” here means those fixed modalities and four times with spider present and fixed action, not every experiment or the upstream model. The historical67-foundation receipt alone does not cover the separate18 clinical declarations.

## Reuse rule

An exact quotient, a simulator and an identified answer are different interfaces. A small counterexample can prove impossibility only for the stated source and observations. A general transfer theorem gives a useful proof tool, but the application still owes its observation laws, causal/biological admission, target map and any promised finite-data or cost guarantee.
