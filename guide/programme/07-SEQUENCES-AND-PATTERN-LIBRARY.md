# Sequences: short proofs and exact boundaries

Put $t(n)=s_2(n)\bmod2$. The two identities used repeatedly are $t(2n)=t(n)$, $t(2n+1)=1-t(n)$. Arithmetic-progression lengths, avoidance-graph heights, raw factor counts and coded beat counts are different quantities.

## First maximum progressions

**CB-SEQ-001.** For an integer d>0, A(d) is the maximum length of a constant-letter arithmetic progression t(i),t(i+d),…, and i(d) its earliest start. For q=2^m,m≥2, “plus” means step d=q+1 and “minus” means d=q−1. The plus family has length q+2, earliest start3q²−q−1; even-m minus has length q+4, earliest start3q²−q+1; odd-m minus has length q, earliest start q−1. The m=1 exceptions are A(3)=8,i(3)=45 and A(1)=2,i(1)=1.

**Proof mechanism.** A block $c\mathbin\oplus t(0),\ldots,c\mathbin\oplus t(q-1)$ can start only at a multiple of $q/2$: its first four symbols force even phase, then desubstitute repeatedly. At phase $lq$ its orientation is $t(l)$; at $lq+q/2$ it requires $t(l)=t(l+1)=1-c$. For a plus progression, write its start $aq+b$ and split at the low-digit wrap. Equal adjacent low parities force contradictory high-index parities unless $b=0,q-2,q-1$; the first two fail the block test. All surviving starts are
$$
s=lq^2-q-1,\qquad t(l-1)=t(l+1)=1-t(l).
$$
For even-m minus, the two repeated high letters around a reverse wrap likewise force $b=1$, giving $s=lq^2-q+1$ with the same condition. Its first solution is l=3. One extra progression term would make two consecutive starts obey the same residue condition although their difference is $\pm1\pmod q$; hence the stated constructed lengths are maximal. For odd-m minus, reflection $t(q-1-r)=1-t(r)$ gives the length-q witness at q−1. Any q+1 terms include low residues0,q−1 with the same high index and opposite parity, so longer is impossible; the same pair excludes earlier starts. This is self-contained in digit identities. Checked names: `ThueMorseMAP.conjecture_3_8_plus`, `conjecture_3_8_even_minus`, `conjecture_3_8_odd_minus`. [Full block/carry proof](../../manuscripts/sequence/Thue-Morse-Hand-Proofs.md).

## Period-doubling is not regular in this statistic

**CB-SEQ-002.** For $u=\operatorname{fix}(0\mapsto01,1\mapsto00)$, let P be minimum prefix palindrome count and $d(n)=P(n+1)-P(n)$. Then d is not 2-automatic and P is not 2-regular. This is an accepted **computer-assisted hand proof**, not a Lean theorem.

The palindrome endpoint/lift suppliers define $C(n)$: some optimum uses singleton1, and prove $C(n)\iff d(2n)=0$. In Gray code $g(n)=n\oplus\lfloor n/2\rfloor$, let I be the minimum number of adjacent-11 dominoes and single-1 monomers covering the 1-runs. Every palindrome edge has nonnegative cost slack, giving $P\ge I$. For binary $N(a,b)=(10)^a(010)^b0$, the accepted off-diagonal constructions give C true when a−b is odd and at least3, and $C(N(a,a-1))\iff P(N(a,a))=2a$.

It remains to exclude that equality. Equal parity of endpoint and optimum permits an all-odd optimal factorization by the exact lift. Its reversed path would consist of zero-slack odd edges. Minimum Gray tilings emit c for a domino at parity c and two copies of 1−c for a monomer. A zero-slack edge lifts target tilings to source tilings whose expressions reduce by $cc\to\varnothing$, $ccc\to1-c$, at most twice. One edge type is direct; the other is the sole universal finite-state inclusion certificate, whose complete reachable closure and separate checker are retained. It has no word-length cutoff.

For $N(a,a)$, the unique expression is $0^a$ followed by an alternating tail of length a starting1. If $\ell$ is longest alternating suffix, $H=2\ell-|w|=2>0$. Either reduction preserves H or increases it and cannot produce empty. Thus no zero-slack path to0 exists, proving $P(N(a,a))>2a$. For integers r≥1, the binary prefixes $(10)^{2r}$ are pairwise distinguished by appending $(010)^{2r-1}0$: C is false for the matching prefix and true for every later one. Infinitely many distinct automaton states are needed, so C and hence d are not automatic; the bounded-difference equivalence gives nonregularity of P. [Complete proof and exact certificate semantics](https://github.com/Sodelin/Research-Commons/blob/64e1fa9f532439e5f63b660d295dc6b33dfe7ec0/research/2026-10-04-dot-period-doubling-nonregularity-1150z/NONREGULARITY-THEOREM.md).

## Uniform morphism lengths and a real endpoint change

**CB-SEQ-003.** For each avoidance threshold in $[(8/3)^+,3)$, the permitted positive uniform binary morphism lengths are exactly all except3,6. At strict8/3, length5 fails.

The source odd-length construction supplies Thue–Morse factors with specified endpoint markers. Their complementary images are cubefree. Each block boundary carries one of four five-letter markers, absent inside a block. A periodic output factor of exponent greater than8/3 and least period $p\ge5$ contains a marker and its p-shift; equal markers force p to be a multiple of block length. Injective image columns then desubstitute the whole touched parent factor, including partial end blocks, with at least the same exponent. Periods1–3 already give cubes; the remaining period4, length11 case would contain a forbidden image suffix or a period4 overlap within one Thue–Morse block. Thus $\mathrm{ce}(h(w))\le\max(8/3,\mathrm{ce}(w))$ for every cubefree input.

Odd lengths at least5 follow; composition with powers of the length2 morphism covers all lengths except the doubling family of 3. A length12 complementary seed `010011001001`/its complement meets the retained universal sufficient criterion: marked ends, no long crossing overlap, and the complete22 short-input certificate with exponent at most8/3. Doubling it covers12,24,…. The source impossibility excludes3,6. At strict8/3, marked five-letter images reduce to four pairs; two force cubes, the remaining two force an exponent8/3 factor on admissible inputs011 or001. Hence length5 really changes at the plus endpoint. [Full marker/seed proof and source attributions](https://github.com/Sodelin/Research-Commons/blob/ccf88c3e5f14c33ee927d74ccc1df568d52fec88/research/2026-10-04-dot-complementary-avoidance-stability-0954z/STABILITY-THEOREM.md). No all-input result is inferred from testing one fixed point.

## Matching heights, shifted targets and finite edits

The actual avoidance graph has $w-1\to w$ labelled t(w), $w-2\to w$ labelled1−t(w), for $w\ge2$, and no0→1. A path's kth edge must read t(k).

The actual general own-target graph for a binary word s has rows r_s(2j)=s(j), r_s(2j+1)=1−s(j). For w≥2, edge w−1→w has label r_s(w), and w−2→w its complement; there is no 0→1 edge. A matching path reads s(k) at step k. Only for Thue–Morse is r_t(w)=t(w). Replacing the destination label by an arbitrary s(w) defines a different graph. This is the graph used in 004–006; the exact source alias is [BinaryAvoidance.lean](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/e2502c82ab9a77c00543932f775a71e5374221f7/lean/SamuelAlexanderResearch/BinaryAvoidance.lean).

**CB-SEQ-004.** Write $\lfloor v/2\rfloor+1=(2h+1)q$, $q=2^r$, $T=t(h),U=t(h+1)$, and $A(h)=[h\equiv1\pmod4,t(\lfloor h/4\rfloor)=0,t(\lfloor h/4\rfloor+1)=1]$. The attained maximum L, including L(0)=1, is

| Start/condition | L(v) |
|---|---:|
| even, T=1 | $1-(r\bmod2)$ |
| even, T=0, q=2 | $7-2U$ |
| even, T=0, q≠2 | $(4-2U)q-1$ |
| odd, T=0 | 0 |
| odd, T=1,U=0 | $4q-1$ |
| odd, T=U=1,A=0 | $10q-1$ |
| odd, A=1 | $16q-3$ |

**Why this is a maximum.** Define boundaries X_a with advance1 when the next graph bit matches the current target bit and 2 otherwise. The actual vertices reachable at time k from v form exactly $[X_v(k),X_{v+1}(k))$. Thus first coalescence at K gives attained maximum K−1. Dyadic block identities give the short cases, the odd-10 trajectories meet at 4q, the odd-11 nonspecial pair at 10q, and the special pair is a translated sharp pair meeting at 16q−2. For the even ascent, the pattern $2^s1^{4s}$ doubles the boundary scale; the final meeting is2q or4q according to U. The exceptional q=2,U=1 pair is a translated base pair and meets at 6, explaining the otherwise easy-to-miss table exception. The [full finite-window/run calculations](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/e2502c82ab9a77c00543932f775a71e5374221f7/notes/FULL-HEIGHT-PROOF.md) give the actual-path bridge and every case.

Consequently $3L(v)\le8v-1$ for v>0, with equality exactly $v=3\cdot2^n-1$. For an integer phase a≥0 and positive start v≥1 in the own-target graph of $s_a(k)=t(k+a)$, the proved phase transport gives
$$
3L_a(v)\le8v+5a-1,
$$
with equality iff $a\le2^n,v=3\cdot2^n-a-1$, then $L_a=8\cdot2^n-a-3$. Both graph and target shift; merely moving the target in the old graph is a different question. Checked names include `FullHeight.height_isMaximum`, `height_closed_form`, `DigitRecurrence.evaluate_isMaximum`, `PhaseExtremal.shifted_extremal_iff`.

**CB-SEQ-005.** For integers m≥0 and starts v≥1, if s differs from t only before m, finite matches transport between their actual own-target graphs with starts differing by at most m and identical suffix from time min(m,length). The source row law gives2k≤path(k): at equality an attempted one-step2k→2k+1 has label1−s(k), so every matched extension preserves the invariant. At splice time r=min(m,length), rebuild backwards from an endpoint≥2r using actual required parents, never the missing0→1 edge. Remaining destinations≥2m have the same row because the two words agree at⌊w/2⌋≥m. This yields3L_s(v)≤8v+8m−1 and genuine maxima. The separate exact tail/dyadic refinement bounds the optimal additive constant by a finite search:
$$
N(m)=3\cdot2^{m+3}+m,\quad
B_s=\max_{1\le v\le N(m)}(3L_s(v)-8v).
$$
Every positive start obeys $3L_s(v)\le8v+B_s$, some start in that finite range attains it, and $-1\le B_s\le8m-1$. The exact bounded-tail supplier is essential; the coarse splice inequality alone would not prove optimality. The chapter's canonical entry retains its complete refinement proof and endpoints `individual_optimum_attained`, `individual_additive_constant_iff`.

**CB-SEQ-006.** A mismatch modulus M(v,b)>b means that for every integer 0≤d≤v there is b≤i<M(v,b) with s(i)≠1−r_s(2i+d+2). For d=2e this breaks antiperiod e+1, and for d=2e+1 it breaks period e+1. Iterating $B_0=0,B_{j+1}=M(v,B_j)$, the finite displacement/offset argument forces every match from v to have length less than $B_{v+1}$; if each window is at most R, the bound is $(v+1)R$. Aperiodicity supplies a modulus by choice, not necessarily an effective one.

There is no universal rate across aperiodic targets. Given any f, recursively set $W_0=1,p_j=|W_j|,v_j=2p_j-1,r_j=f(v_j)+2$,
$$
W_{j+1}=W_j^{r_j}0^{r_jp_j}1.
$$
Prefixes are coherent and lengths increase. The repeated block supplies a constant-offset two-step path of length $(r_j-1)p_j>f(v_j)$. Increasing zero blocks followed by 1 defeat every alleged eventual period; the same target is therefore aperiodic and its graph has no infinite match. This is target-dependent slow avoidance, not one target exceeding every function.

## Averages and a faithful code into juggling

**CB-SEQ-007.** The proved ten-coordinate digit recurrence is $S(2n)=M_0S(n),S(2n+1)=M_1S(n)$. With $A=M_0+M_1$, dyadic totals are $A_k=e_LA^kS(0)$. The exact finite identity
$$
e_LA^3(A-2I)^2(A-I)^2(A+I)=0
$$
gives an order-five recurrence for all k≥3. Its values27,76,199,480,1125 at k=3,…,7 determine
$$
A_k=29(3k+1)2^k/72-(k+3)-(7/9)(-1)^k.
$$
A_0=1,A_1=1,A_2=6 are separate bases. This is a matrix certificate and induction, not a fitted recurrence. Maintain $U(N)=\sum_{v<N}S(v)$ while reading N's bits: bit0 sends $(U,S)\mapsto(AU,M_0S)$; bit1 sends it to $(AU+M_0S,M_1S)$. This computes the exact aggregate in O(log N) fixed-size integer-matrix operations. It is not a claimed bit-complexity or height-distribution theorem. All matrix entries are retained in [the reading proof](../../manuscripts/sequence/Thue-Morse-Hand-Proofs.md).

**CB-SEQ-008.** At three-ball ground state, both primitive loops(3) and(4,2) return to that same state. Encode each original graph edge by its **own** corresponding path, keeping distinct original/internal vertices. A match from an original vertex parses uniquely by first throw, and any partial two-beat block can be finished. Therefore H(v)=W(L(v)), with $W(2m)=3m,W(2m+1)=3m+1+t(m)$. For v≥1 the sharp height inequality gives H(v)≤4v, equality exactly $v=3\cdot2^{2r}-1$. The original constraint graph is essential; the unconstrained juggling routine continues indefinitely. The exceptional start is L(0)=H(0)=1.

More generally, two distinct primitive return loops at the same state, with positive integer lengths a,c and a real weighting base b>1, give, for exactly one pattern per Thue–Morse block prefix,
$$
F_{a,c}(z)=\frac{1+(z^a+z^c)/2}{1-z^{a+c}}
+\frac{z^a-z^c}{2}P(z^{a+c}),\quad P(x)=\prod_{r\ge0}(1-x^{2^r}).
$$
Split prefixes into even/odd length and use digit-pair balance to derive it. If a=c the product disappears and the series is rational. Otherwise P tends to0 radially at the dense dyadic roots of unity; continuation through any arc would have dense zeros, contradicting P(0)=1. Away from the finitely many prefactor zeros/poles, local inversion transfers this natural boundary to F, and z=b^(−s) gives Re(s)=0. This is not unrestricted juggling enumeration.

## Grouped motifs

**CB-SEQ-009.** Take integers n,k≥1. For $\tau_n:0\mapsto0^n1^n,1\mapsto1^n0^n$, the exact worst window determining level-k phase is
$$
D_n(k)=(2n)^{k-1}(4n^2-n)+1.
$$
At level1, any visible change fixes residue modulo n. An ambiguity modulo2n must therefore differ by n; compress the touched n-blocks. Ambiguous opposite parities in a 01/10 image force that compressed word to alternate, with maximum length4n−1 because ancestor runs have length at most2n. Both maximal runs supply a matching witness, giving longest ambiguity4n²−n. Injective columns, including partial end images, multiply the maximum ambiguity by 2n per level. The accepted grouped common-factor formula gives $P_1=9,P_n=4n+1$ for n≥2 as exact parameter-recovery lengths; joint parameter/phase threshold is $\max(P_n,D_n(k))$. Raw unknown-position windows, supplied hierarchy cuts and an arbitrarily chosen grouping are distinct observations.

**CB-SEQ-010.** For an integer n≥1, write $u_n=h_n(v_n)$, with h stretching each bit n times and $v_n$ the established base-2n digit-sum parity word. Short windows have at most two changes, giving p_n(L)=2L for L≤n+1 and $4L-2n-2$ for n+2≤L≤2n. For longer windows, a change fixes the start residue modulo n; those inventories are disjoint. If $k=\lceil L/n\rceil,\delta=(L-1)\bmod n$, exactly n−δ residues touch k parent letters and δ touch k+1, hence
$$
p_n(L)=(n-\delta)P_{2n}(k)+\delta P_{2n}(k+1).
$$
Use the credited generalized Thue–Morse formula for P. For fixed L, all n≥L have exactly the one-change factors, so n=1,…,L exhaust the comparison. At L=33, n=3 gives98 while ordinary Thue–Morse gives96. This does not contradict the next theorem's different selected-digit family.

## Selected digits: complexity, exponent and bispecial factors

**CB-SEQ-011.** For infinite $S=\{0=s_0<s_1<\cdots\}$, let $x_S(r)$ XOR r's bits at positions in S and $A_i=2^{s_i}$. The exact factor counts are p(0)=1 and
$$
\begin{array}{ll}
p(L)=2L,&1\le L\le A_1+1,\\
p(L)=4L-2(A_i-A_{i-1}+2),&A_i+2\le L\le2A_i-A_{i-1}+1,\\
p(L)=2L+2(A_i-1),&2A_i-A_{i-1}+2\le L\le A_{i+1}+1.
\end{array}
$$

**Count proof.** Tail words satisfy $x_j=\phi_{[j\in S]}(x_{j+1})$, with $\phi_0:0\mapsto00,1\mapsto11$, $\phi_1:0\mapsto01,1\mapsto10$. Their languages are complement-closed by adding a high selected bit without a carry. Their exact maximum run is $R_j=2^{z_j+1}$, z_j the distance to the next selected position. At each start parity, image columns recover every parent letter, including partial endpoints. The two inventories intersect only in two constant words for φ0 or two alternating words for φ1, exactly when L<2R. Thus
$$
p_j(L)=p_{j+1}(\lceil L/2\rceil)+p_{j+1}(\lfloor L/2\rfloor+1)-2[L<2R_{j+1}].
$$
Subtract successive lengths. The first difference is2 plus one possible extra2; its growth intervals are exactly $[A_i+2,2A_i-A_{i-1}+1]$. Summing these telescoping intervals proves the formula.

The critical exponent is $\sup_i2^{s_i-s_{i-1}}$. Long constant tail runs give the lower bound after applying their preceding morphisms. A nonconstant factor of exponent>2 must have even period: a repeated change in φ0, or repeated equal adjacent pair in φ1, fixes parity. Desubstitute, including partial endpoints, to halve the period without lowering the exponent. Above the maximum tail run, repetition of this step eventually forces an odd positive period to be even, impossible. For a finite nonnegative bit mask m, the selected-position set S_m={p≥0 : (p bitwise-and m)=0} is INFINITE. Its consecutive selected positions have maximum gap m+1, giving exponent $2^{m+1}$.

Nonempty bispecial factors uniquely desubstitute until an alternating factor at selected position s_i: they are $\Phi_{s_i}(\operatorname{alt}_c(\ell))$, with $1\le\ell<2R$ for i=0 and $2\le\ell<2R$ later, $R=2^{s_{i+1}-s_i}$. Visible parity forces complete parent-image endpoints; the exceptional constant/alternating extension table gives strong at ℓ=R, weak at ℓ=2R−1, ordinary otherwise. The empty word has its separate four-extension strong case. This yields the stated nonempty strong lengths $2^{s_{i+1}}$, weak lengths $2^{s_{i+1}+1}-2^{s_i}$, and the same complexity breakpoints. The complete left/right extension tables are retained in the [full hand reading edition](../../manuscripts/sequence/Pattern-Hierarchies-and-Selected-Digit-Proofs.md).

The formula gives $2L\le p_S(L)\le p_{TM}(L)$ by comparing each preceding selected power with the largest allowed power. If S,T first differ at position r≥1, their first count difference is2 at L=2^r+2; hence the full count function determines S. For masks first differing at bit r, the scale is $2^{2^r}+2$. Cloitre **v2 already gives an effective all-level recurrence**; the retained edition explicitly corrects the obsolete v1-only open-problem description. Classical special cases and desubstitution methods retain credit.

## Finite prefixes versus one positive infinite realization

**CB-SEQ-012.** Use the fully accelerated odd Collatz map $U(n)=(3n+1)/2^{v_2(3n+1)}$. A fixed binary Thue–Morse concatenation of any two nonempty valuation words, if realized by one positive seed N, must start on a cycle.

**Proof.** If two positive odd starts share an exact valuation prefix of length L and sum S, the affine formula and odd endpoint give congruence modulo $2^{S+1}$. A repeated prefix at time J, with different states, therefore has
$$
2^{S+1}\le|U^J(N)-N|<(3/2)^J(N+1).
$$
For L=2d,J=3d, S≥L forces $2\cdot32^d<27^d(N+1)$, hence $10d+27<27N$. Thue–Morse has prefix return $t[0:2h]=t[3h:5h]$, h=2^m. Binary balance makes the encoded lengths exactly L=2d,J=3d even for unequal codeword lengths, with d unbounded. The inequality eventually fails, so some positive return has $U^{3d}(N)=N$.

For code(1)/(2), the balanced return's positive affine correction makes it strictly grow, excluding that cycle; for fixed blocks $1^p3,1^q3$, p,q≥3, every complete block strictly grows by its exact affine formula. Both therefore admit no positive seed. The cycle exception is essential: code(2)/(2), N=1 works. Every finite prefix remains positively realizable; no universal Collatz claim follows. [Complete analytic proof and narrower formal boundary](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/026aa4ad4be6453a005ab950b160a9f2204c5271/proof-search/disproof/TM_Prefix_Return_Exclusion_2026-09-05.md).

## Status and reusable lesson

Exact digit/phase proofs, all-length finite-state certificates and analytic prefix bounds are distinct evidence. Existing Lean endpoints cover the named first-occurrence, height, phase, finite-edit and slow-avoidance components; the later hand applications and the complete Collatz bridge are not thereby formalized. The [retained reading-edition correction ledger](../../manuscripts/sequence/README.md) preserves unavailable older packets and later accepted successors. Finite local feasibility, finite factor inventories and large observed matches must not be mistaken for one infinite realization—the same quantifier warning used in G3.
