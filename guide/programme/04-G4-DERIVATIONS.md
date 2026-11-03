# G4's compact derivation library

These are the retained component arguments developed during the 31 October collaboration. Most are hand proofs with separate exact producer controls. They are not a new Lean release, a new source-evaluator audit, or closure of either master. The [original G4 quantifiers](02-G1-TO-G7.md) remain in force. Citations below point to the preserved authored bodies and their correction history.

## 1. The simple three-cycle wrapper

The wrapper has root $\rho$, an ordinary reference lineage $C$ on one root child, and an upper kernel $K_U$ on the other leading to cycle top $v$. The cycle is $v\to w\to H$, $v\to H$. Taxon $A$ enters below $H$, taxon $B$ at $w$. Write
$$
g=P(H\text{ chooses }w),\quad x=x_{vw},\quad
y=x_{wH},\quad r=x_{vH},\quad0<g,x,y,r<1.
$$
Descendant components are actual single-cut kernels $K_A,K_B$, including finite tails. Stop $K_A$ before $H$ routes. All controls here are natural I. The known completion with one $C$ decodes the labelled forest at the top of $K_U$.

Two all-taxa physical rows $(A,B,C,D)=(1,3,1,1),(2,1,1,1)$, followed by fixed-label pruning, supply the six essential laws
$$
(A,B,C),(B^2,C),(A,B^2,C),(B^3,C),(A,B^3,C),(A^2,B,C).
$$
$(A^2,C)$ is optional, already a marginal. No zero-copy physical experiment is introduced. A narrower menu or coarsened topology channel is not covered.

### 1.1 Low-cap geometry is not a global obstruction

For an equal-arm bigon with arm survival q and coin g, put v=g(1−g), δ=1−q, **d_B=2v+(1−2v)q=1−(1−2v)δ** and e_B=t_B−t_ord(d_B). Triple separation is n_B=(1−3v)q³+3vq. Expanding(n_B−d_B³)/6 gives exactly
$$
e_B=v\delta^2\left[\frac{1-4v}{2}
-\frac{\delta(3-12v+8v^2)}6\right].
$$
At fairness v=1/4 this is−δ³/48<0. The deficit δ is not pair separation d_B; the earlier ambiguous d notation is corrected here. With a small bias and short arms it can be positive. At $q=9/10$, the bracket is $R(v)=9/20-9v/5-2v^2/15$, decreasing in $v$, negative at $1/4$, positive at $6/25$. Thus a transverse zero occurs for $g\in(1/2,3/5)$. An ordinary pad multiplies excess by its survival cubed and scales pair separation independently; the two-parameter pad/bigon map has nonzero Jacobian at the crossing. The inverse-function theorem puts the ordinary cap-three point in the interior of actual positive-word coordinates. If logarithmic arm time tends to zero jointly with bias, its expansion must retain the fourth-order remainder as well.

At cap three, the coloured exit law factors through three pair coordinates and two new coordinates on each of $\{A,A,B\}$, $\{A,B,B\}$, hence dimension at most seven. A producer's exact nonzero seven-minor supports the local relaxed fibre and its movement; the evaluator/minor was not independently reimplemented. The positive-word interior supplies local realizations. A separate existing COMMON row detects the upper word already at the central point and continues by continuity. This is actual low-cap ambiguity, not an all-cap G4 negative.

The later producer rank-13 cap-four calculation is local rigidity at one target, not global uniqueness. The hand theorem below supersedes the numerical global scans and unfinished interval covers for this wrapper. [Exact positivity check and caveats (source availability)](README.md#source-availability); the early demand for an explicitly in-certificate COMMON witness was subsequently retracted, as preserved in the correspondence.

### 1.2 Observable substitutions

Set
$$
D_u=1-g+gx,\quad D_v=g+(1-g)x,\quad
s_1=1-g+gx^2,\quad s_{1m}=g+(1-g)x^2,\quad w=g(1-g).
$$
Let $P_1$ be the $a,b$ pair-separation exit probability, $P_3$ the $b,b$ pair separation, $E_S$ the all-separate $a,b,b$ probability, and $e_*$ the observed three-B composite excess. With $U=d_U$, L5 gives
$$
U=P_1/D_u,\quad d_B=P_3D_u/(xP_1),\quad
n_U=E_SP_1/(P_3D_us_1)>0,
$$
$$
e_U=(n_U-U^3)/6,\quad
e_B=(e_*/x^3-d_B^3e_U)/n_U,
\quad n_*:=P_3^3+6e_*=n_Bx^3n_U>0.
$$
Pairs prove the first two equations. The $a,b,b$ all-separate event proves the third. Serial multiplication of $d,n$ proves the excess and $n_*$ equations. All divisors are positive; there is no hidden slope exception.

### 1.3 Coin and prefix are globally pinned

For one specified $((a,b_1),b_2)$ exit triple, direct root-count bookkeeping gives
$$
6E_{Tab}-E_S=d_B(2D_v-3Ux).
$$
Substituting the previous equations identifies $D_uD_v/x$, hence
$$
I_3:=w(1-x)^2/x
$$
from the target's law.

Next subtract the per-labelled triple-plus-singleton forests
$$
\Delta=P(((b_1,b_2),b_3)|a)
-P(((a,b_1),b_2)|b_3).
$$
The fresh-four upper terms cancel by exchangeability. Two entering roots carry coefficient $U$; three entering roots carry $c_U$. The compatible lower graft cases give
$$
\Delta=U[t_BD_u+c_B(gc_x+(1-g)(1-x))+n_B(1-g)t_x]
+c_U[c_Bxs_1+n_B(1-g)c_x].
$$
Use $c=(d-n)/2$ and the substitutions above; collecting terms gives
$$
\Delta=K_0+K_1s_1s_{1m}/x^2,
\quad K_0=P_1/3-P_3/4-E_S/4+n_*/4,
\quad K_1=-P_3n_*/(12E_S)<0.
$$
Thus the law identifies $I_4=w(1-x^2)^2/x^2$. Dividing $I_4/I_3$ identifies $(1+x)^2/x$, strictly decreasing for $0<x<1$. Therefore $x$ is unique, then $w$ is unique, leaving only $g$ and $1-g$.

To remove that mirror, subtract probabilities of these **one-root comb forests in the finite exit law decoded using C**, rather than eventual completed-topology probabilities:
$$
\Delta_c=P((((b_1,b_2),a),b_3))-P((((a,b_1),b_2),b_3)).
$$
Below the upper kernel, their differences at one, two and three roots are respectively $gc_Bt_x$, $gc_Bc_x$, $c_Bxs_1+n_B(1-g)c_x$; fresh-four terms cancel. Hence
$$
\Delta_c=gc_B[t_x+(1-U)c_x]
+t_U[c_Bxs_1+n_B(1-g)c_x].
$$
Put $\beta=P_3n_*/(P_1E_S)>0$. Subtract its mirror, using $D_u-D_v=(1-2g)(1-x)$, $s_1-s_{1m}=(1-2g)(1-x^2)$, and
$$
D_us_1+D_vs_{1m}-1-x^3=-2w(1-x)^2(1+x).
$$
The $P_1$ terms and the $d_B$ terms cancel, leaving
$$
\Delta_c(g)-\Delta_c(1-g)
=-\frac{(1-2g)\beta w(1-x)^3(1+x)(1+x+x^2)}{6x^3}.
$$
It is nonzero unless $g=1/2$, where the mirror is the target itself. Thus every same-wrapper matching strict rival has the same $g,x$, with no exceptional target. Arbitrary nonordinary actual descendant/upper kernels are included; upper level-four coordinates cancelled.

Here t_U and 1−U belong to the finite exit kernel. Section6's directly observed completed-tree contrast instead has two-root completion coefficient one; these are different readouts.

### 1.4 One two-A law pins both private arms

Let $a=d_A,p=d_Ay,q=d_Ar$. At $v$, the probabilities of all separate, one specified mixed cherry plus singleton, and one specified mixed-first complete triple are
$$
S_v=g^2x^3p+(1-g)^2q+2wxa,
\quad C_{ab}=g^2pc_x+w(1-x)a,
\quad T_{ab}=g^2pt_x.
$$
A pair already merged in $K_A$ routes once; separate roots route independently. These cases give the expressions. For this A²B law denote measured exits E_S^(AAB),E_C^(AAB),E_T^(AAB); they are not the earlier ABB coordinates. Invert the now-known cap-three K_U triangularly:
$$
S_v=E_S^{(AAB)}/n_U,\quad C_{ab}=(E_C^{(AAB)}-S_vc_U)/U,
\quad T_{ab}=E_T^{(AAB)}-S_vt_U-C_{ab}(1-U).
$$
Then
$$
p=T_{ab}/(g^2t_x),\quad
a=(C_{ab}-g^2c_xp)/(w(1-x)),\quad
q=(S_v-g^2x^3p-2wxa)/(1-g)^2.
$$
Every denominator is strictly positive. Recover $y=p/a,r=q/a$. This pins all four intrinsic core parameters, $K_A$ through cap two, and $K_B,K_U$ through cap three. It does not identify their words.

[Consolidated full proof and evidence ledger (source availability)](README.md#source-availability); [mirror graft cases (source availability)](README.md#source-availability). Producer checks are supporting evidence, not the hand proof's logical basis.

## 2. Pruning transfers to one-gall families

This transfer compares the stated fixed ordered ports, known C completion, actual private single-cut kernels and inherited serial upper-word interface. It is not arbitrary exterior decoding. Target and rival have separate tuples, each fixed across all its rows.

In a simple gall, choose one original taxon $A$ below the hybrid and one $B_u$ from each side cut component. Delete all but $A,B_u,C$ **jointly**. Empty side ports inject nothing; ordinary cycle edges compose by L1. A left-arm port with prefix $P_i$, total left survival $L$, and total right survival $R$ becomes
$$
W3(g,P_i,L/P_i,R;K_A,K_{B_u},K_U).
$$
A right port becomes $W3(1-g,Q_j,R/Q_j,L;\ldots)$. This is a marginal analysis, not a substituted experiment.

Triplicate each chosen $B_u$ in one physical all-taxa row; use one additional row doubling $A$. Single-A wrapper recovery gives every prefix, the oriented coin and cap-three kernels. One two-A law gives the chosen suffix and other arm total, hence both totals. Consecutive prefix ratios and the last total/prefix ratio recover every original cycle edge. A portless arm is its single ordinary edge. All products/divisors stay strict. For a $k$-cycle there are $k-2$ side ports, so $k-1$ rows suffice. Actual finite descendant components, even with nested blobs, are admitted via L4; their interiors are not identified.

The two four-cycle placements are instances: same-arm pruning gives $(g,x_1,x_2x_3,y)$ and $(g,x_1x_2,x_3,y)$; opposite-arm pruning gives $(g,x_1,x_2,x_3x_4)$ and $(1-g,x_3,x_4,x_1x_2)$. Prefix ratios finish the transfer. [Family theorem and finite-port use-site checks (source availability)](README.md#source-availability).

## 3. Root and side-port inference with a known C completion

At a two-cut root, two taxa on one side and a third on the other have triple law $(1-2d/3,d/3,d/3)$, $d<1$: a positive top edge forces strict within-side preference. If another nontrivial root partition differs, choose a pair together in the first but separated in the second and a taxon on the other first side. The two partitions demand different strict favourite pairs. Thus the root partition is forced by the all-one-copy law.

For side taxa $b,c$, define $D_{bc}=3P(((b,C),c))$, and decode the common upper pair survival $U$. Write $x_b$ for the cycle prefix to $b$'s port. Then
$$
D_{bc}/U=\begin{cases}
1&\text{opposite arms},\\
\max(x_b,x_c)&\text{same arm, different ports},\\
x_bz_{bc}&\text{same port},\quad0<z_{bc}<1.
\end{cases}
$$
One lineage per component is an identity; different arms never pool below $v$; same-arm pairs share exactly the nearer prefix; same-port roots also cross their actual positive top edge. Wrapper rows identify each $x_b$. Therefore $D=U$ detects opposite arms, and among same-arm pairs equality of prefixes detects the same port. Prefixes strictly decrease down an arm, giving order and cycle length. No coin asymmetry is needed.

For a common hybrid-descendant anchor $A$ and common side anchor $B$, put $d=1-g+gx_B$, $M=1-g+gd$, $p_{ij}=D_{ij}/U$. A taxon $t$ is below the hybrid iff
$$
p_{Bt}=d,\qquad p_{At}<M.
$$
Below the hybrid, $p_{At}=z[g^2L+(1-g)^2R+2w]<M$. For a side taxon, opposite/same/farther ports give $p_{Bt}\ne d$; a nearer port can equal $d$ only with prefix $d$, where $p_{At}=M$. These exhaust the stated class.

The common side-anchor premise can be removed once a common $A$ is given. If the two sources' side sets were disjoint, choose one taxon from each. Equal cross pairs force all three pair separations among them and $A$ equal in each source, making their cherry contributions equal. Exit triple differences then cancel $K_U$. In the source where $A,t$ lie below the hybrid and $b$ is side,
$$
E_{((A,t),b)}-E_{((A,b),t)}
=g(1-x)[(1-z)+zg(1-y)]>0,
\quad E_{((A,b),t)}=E_{((b,t),A)}.
$$
The rival with $t$ side requires the other equality, a contradiction. A shared side anchor therefore exists, and the preceding test classifies every taxon consistently. This is conditional on a common hybrid anchor and no upper taxa; it is not general H1.

## 4. The mixed-copy orientation sign

Let $\alpha$ enter below a simple hybrid and $\beta$ at a side port. Retain two of each. Define
$$
X=\{((\alpha_1,\beta_1),\alpha_2),\beta_2\},
\quad Y=\{((\alpha_1,\beta_1),\beta_2),\alpha_2\}.
$$
Their common refinements are the same mixed-cherry three-root forest and four singletons. Every upper contribution from those refinements cancels; the two-root term has coefficient $U$. Both lower histories share the term with both $\alpha$'s routed to the side arm. Only $Y$ also has the split route: $\alpha_2$ avoids the prefix while $\alpha_1,\beta_1,\beta_2$ form their specified triple. Hence
$$
S_{\alpha\beta}:=E(X)-E(Y)
=-U\kappa_\alpha\kappa_\beta g(1-g)t_x<0.
$$
Earlier same-colour cherries are incompatible with both outputs. Swapping which taxon is below the hybrid reverses the same labelled sign, so a strict dual-wrapper pair cannot match the $(2,2,C)$ law. The two-taxon reduction then excludes disjoint hybrid blocks. Choose an anchor in their intersection, apply the preceding anchor-free argument and side-port/family recovery. This proves the stated no-upper-taxa one-gall class theorem from the universal triplicate and double-pair panel. It does not compare arbitrary different multi-hybrid cores. [Sign proof and source reduction (source availability)](README.md#source-availability).

Preselect the n triplicate rows and every unordered double-pair row: n(n+1)/2 all-taxa allocations, each with≤n+2copies. This conclusion compares two-cut-root sources with one simple main gall, no upper-region taxa and the stated source/upper interfaces; arbitrary nested descendant cut interiors remain allowed.

## 5. Upper spines and designation gauges

With common hybrid/side anchors, prune upper taxa and recover composite $U$ by W3. A taxon entering the tree spine at $u$ first meets either anchor there. Let $h_u$ be pair survival from $u$ to $\rho$, $l_u$ from $v$ to $u$. Then $D_{At}=D_{Bt}=h_u$ and $U=l_uh_u<h_u$. Gall taxa have $D_{At}\le U$. Thus upper taxa are exactly those with $D_{At}>U$. Equal $h$ means the same attachment; decreasing $h$ orders attachments away from the root. Ratios give segment **pair** coordinates, not individual durations or words. A common two-boundary ancestral region works only with one lower input population, one upper port, no other retained inputs and no shared external register.

Two disjoint outer galls hanging from a tree fork can each be designated “main” in the **same** source. Different main designations are a gauge, not a law collision. Observable graph components give a finite designation list; they do not force one arbitrary designation to equal another.

## 6. Complete combs remove the C decoder

Let $T_X=(((a_1,b_1),a_2),b_2)$, $T_Y=(((a_1,b_1),b_2),a_2)$, and $J_{ab}=P(T_X)-P(T_Y)$ in the completed four-leaf law. At any population receiving all retained roots, the compatible forests are respectively the whole comb, its triple-plus-singleton, the **same** mixed-cherry three-root forest and the same four singletons. In any label-blind single-entry ancestor region ending in completion, the last two contributions cancel and a triple-plus-singleton completes with probability one. Therefore
$$
J_{ab}=V(T_X)-V(T_Y)+V(X)-V(Y).
$$
For a simple cycle, complete comb differences below its top are zero: on split/direct routes four roots never pool there, and on the all-side route their four-root process is exchangeable. Thus
$$
J_{ab}=-\kappa_a\kappa_b g(1-g)t_{x_b}<0
$$
for every hybrid-descendant/side pair, at **any depth**, including a root cycle or a nested cycle. The ancestral region may be unknown; no inverse is used. If two colours first pool through disjoint cut components at a tree vertex, earlier same-colour cherries are incompatible and the four-root continuation is exchangeable, so $J=0$.

Consequently a simple gall with a tree/word boundary above it has its below-top block as a connected component of the observable graph $J\ne0$. Its hybrid/side cross pairs connect it, and all outside tree-separated pairs vanish. Under the explicit **whole-source simple-cycle** subclass predicate, the nontrivial components are exactly the outermost cycle blocks. A root cycle gives one component on all taxa. Inner cycle blocks are connected but need not be closed, because an enclosing gall adds cross edges. General original sources can have non-simple blobs, so this is not a universal blob detector. [Decoder-free cover and exact predicates (source availability)](README.md#source-availability).

When all of a cycle's components are tree-like up to serial words, its directed $J<0$ arcs are exactly hybrid block $\to$ side block. The tails therefore identify roles. Under nesting, the same three arcs $a\to a',a\to b,a'\to b$ arise with $a'$ either below the outer hybrid or in its side component. This is a graph-only ambiguity. CE plus the strict same-port triple pattern separates the two particular nested templates: their triple vectors are $(q,p,p)$ and $(m,m,M)$, $m<M$, which cannot agree. This does not prove a general nested-role theorem.

## 7. Known-role triple classifier, at any depth

Retain one hybrid-descendant $a$ and two side taxa $b,c$. Three fresh roots reaching the top have an exchangeable complete continuation, so each rooted triple has probability $1/3$. A cherry plus root completes as that triple. This remains true through an unknown single-entry ancestor region with no other retained input.

* Opposite arms: $T_{bc}$ is the unique minimum, with gaps $g(1-x_b)$ and $(1-g)(1-x_c)$.
* Same arm, distinct ports with $b$ nearer the top: $T_{ab}$ is the unique minimum, with other gaps $(1-g)(1-x_1)$, $g(1-x_2)$, where $x_2$ is the inter-port survival.
* Same port, actual joint separation $z$:
$$
P(T_{ab})=P(T_{ac})=z[g+(1-g)x]/3,
\quad P(T_{bc})-P(T_{ab})=(1-z)+z(1-g)(1-x)>0.
$$

Each follows by conditioning on $a$'s route and the first possible pair merger. The three patterns are exclusive. All-one-copy marginals therefore give the port partition, arm split up to naming, order and cycle length **when roles are common and every port is represented**. They do not recover the coin/edges or roles themselves. [Exact known-role source (source availability)](README.md#source-availability).

## 8. The two-hybrid atom and feature cancellation

The admitted three-port, two-hybrid atom has two upstream ordinary edges $x_1,x_2$, private arms $p_A,r_A,p_B,r_B$, and coins $g,h$. Its shared chord makes it non-simple. Let $k_A,k_B$ be actual private pair separations. Conditioning on current-root routes yields
$$
S_{AB}=Uk_Ak_B[g^2L-g(1-g)R],
\quad L=x_1p_Ah(1-h)t(x_2),
$$
$$
R=h^2p_Bt(x_1x_2)+(1-h)^2r_Bt(x_1)
+h(1-h)[(1-x_2)(1-x_1)+2x_2t(x_1)].
$$
The positive term requires both A roots deep and exactly the first B deep: its completed triple below $v_1$ survives $x_1$. The negative term requires the second A direct, with the other three completing the Y triple below $v_0$. All symmetric four-root histories cancel. Thus $g=R/(L+R)$ makes the orientation feature zero at a strict source. At the original tuple, $L=1/160,R=157/1600,g=157/167$. This is a feature failure, not a full-law collision.

The three-root colour contrast transports as $n_U\Delta_3$, but is already the marginal difference $E_S(abb)-E_S(aab)$. It is not tree-null. Calibrate it instead by
$$
\tau_{ab}=E_S(abb)D_{aa}-E_S(aab)D_{bb}.
$$
For a tree-separated pair with lower separations $k_a,k_b$, the two triple probabilities are $n_Uk_b,n_Uk_a$, and pair separations $Uk_a,Uk_b$; hence $\tau=0$. At the original S-cancellation tuple, $\tau\ne0$. The later exact source/review reports a different strict atom with **both** S and tau zero. Thus their union graph is still not a universal detector. That report does not fit the original target's full panel or establish a G4 negative. The native general-J review has now supplied the distinct complete-comb feature; see the dated successor in section10. Its earlier pending status is retained in Git history.

## 9. JOINT-SIX-EDGE: current exact system, not a result of identification

All eight intrinsic atom parameters now co-vary, as do actual descendant kernels and the upper word. AP is **one joint** cut kernel. The ten original physical rows, in order A,P,B,C, are
$$
3111,1311,1131,1113,2211,2121,2112,1221,1212,1122.
$$
The six C-singleton rows give G-side exit laws; the B-singleton/C-triplicate marginal decodes the C kernel through cap three and projectivity plus forward product rebuild the other C rows. All ten remain the acceptance test. With P retained, the upper cap is five and AP cap four; P-pruned fitting alone is necessary, not sufficient.

For the P-pruned subsystem define
$$
E_0=1-g+g[hx_1x_2+(1-h)x_1],
$$
$$
A_0=g^2p_Ax_1x_2+(1-g)^2r_A+2g(1-g),
\quad B_0=h^2p_Bx_1x_2+(1-h)^2r_Bx_1+2h(1-h)x_1,
$$
$$
C_0=g^2p_A[h(x_1x_2)^3+(1-h)x_2x_1^3]
+2g(1-g)[hx_1x_2+(1-h)x_1]+(1-g)^2r_A,
$$
$$
D_0=g[h^2p_B(x_1x_2)^3+(1-h)^2r_Bx_1^3
+2h(1-h)x_2x_1^3]+(1-g)B_0.
$$
Then $S_{11}=UE_0,S_{20}=Uk_AA_0,S_{02}=Uk_BB_0,S_{21}=n_Uk_AC_0,S_{12}=n_Uk_BD_0$. These actual no-merger path sums eliminate
$$
U=S_{11}/E_0,\quad k_A=S_{20}E_0/(S_{11}A_0),\quad
k_B=S_{02}E_0/(S_{11}B_0),
\quad n_U=S_{21}UA_0/(S_{20}C_0),
$$
and give the nuisance-free hexagon
$$
S_{21}S_{02}/(S_{20}S_{12})=C_0B_0/(A_0D_0).
$$
Two specified exit triple differences add
$$
E_{((aa),b)}-E_{((ab),a)}=(1/U-1)(S_{11}-S_{20})+\Delta_{21},
$$
$$
\Delta_{21}=gQ(1-k_A)+k_Ag^2[(1-p_A)Q+p_A(1-h)(1-x_1)(1-x_2)],
\quad Q=h(1-x_1x_2)+(1-h)(1-x_1),
$$
and
$$
E_{((bb),a)}-E_{((ab),b)}=(1/U-1)(S_{11}-S_{02})+\Delta_{12},
$$
$$
\Delta_{12}=gQ(1-k_B)+k_BgZ_{12},
\quad Z_{12}=h^2(1-p_B)(1-x_1x_2)
+(1-h)^2(1-r_B)(1-x_1)-h(1-h)(1-x_1)(1-x_2).
$$
$Z_{12}$ is **not** the orientation $R$; the original mistaken identification was corrected. At the target they are $3/16$ and $157/1600$.

For the colour-swapped same-colour-cherry forests $F=\{(aa),b,b\}$, $X=\{((aa)b),b\}$, $Y=(((aa)b)b)$, refinement gives
$$
e_F=n_U\Delta_F,\quad e_X=U\Delta_X+c_U\Delta_F,
\quad e_Y=\Delta_Y+(1-U)\Delta_X+t_U\Delta_F.
$$
Since $c_U+t_U=(1-n_U)/3$,
$$
e_X+e_Y+e_F/3=\Delta_X+\Delta_Y+(k_BD_0-k_AC_0)/3.
$$
This E6 cancellation is independently hand-checked and **upper-free**. Its remaining actual lower-history polynomials and legal private-kernel substitutions are still required before calling it core-only; E7/E8 are not accepted. A count of equations, local rank or formal kernel direction will not prove global joint pinning or actual realization. [System (source availability)](README.md#source-availability), [erratum and E6 (source availability)](README.md#source-availability), [independent review, section5](https://github.com/Sodelin/Research-Commons/blob/73e34a9bb3f083abffecf2bec40b64e0e14c33b6/research/2026-10-31-cut-cohort-source-review/REVIEW.md).

For G4, joint intrinsic identifiability is a stronger possible sufficient route. The required conclusion is only constancy of the inherited COMMON-certificate coordinates on the actual finite-I fibre. A sound relaxation can establish this without realizing every relaxed point, but its coverage of every admitted unknown-size rival must be proved. Necessary identities alone do not establish that coverage, positive finite-source membership, or terminating G3 recognition.

## 10. Dated successor: general-J and fixed-target consumers accepted

The existing native reviewer has now HAND ACCEPTED the full 7,991-byte addendum, SHA256 `cf19dfde23ebdefbb10397e9e041b2cb15089d5d1496e54358ce642216a6a7b8`. Full Pro has acquired and read that scoped public review and the separately checked consumers; no duplicate derivation or fresh formal/source-engine execution occurred.

Write $L_J=p_Ah(1-h)t(x_2)$, so $L=x_1L_J$. On the **same** actual tuple, private cuts and single-entry upper source,
$$
J_{AB}=k_Ak_B[g^2L_J-g(1-g)R],\quad
S_{AB}=Uk_Ak_B[g^2x_1L_J-g(1-g)R],
$$
$$
J_{AB}-S_{AB}/U=k_Ak_Bg^2(1-x_1)L_J>0.
$$
The additional complete-tree difference forms the X triple on $x_2$, then merges it with the bypassing B root on $x_1$; its coefficient is $(1-x_1)L_J$. Shared three-/four-root refinements cancel and the two-root completion coefficient is one, proving the formula through an arbitrary actual single-entry upper completion. Observing S still requires the known-C decoder; pruning C from the same physical row observes J. Independent fits with different U or private kernels would not supply the gap. This now makes JOINT-SIX-EDGE's E5 an available accepted supplier at its actual use-site premises; it does not solve the joint equations.

For the one fixed strict four-taxon target and three six-copy rows, the separate consumer audit checked all K4 pair-pruning maps and the doubled-pair cases with original strict paths and private tails. The K4 cases force J nonzero whenever S is zero on every pair, contradicting the target's zero AP pair. Doubled-pair type A reverses the required oriented sign; types B/C already fail the strict simple-gall S sign. This discharges the nonroot (4,3) exclusion. With the accepted (4,2) exclusion/classification, matching **two-cut-root** rivals reduce to the (3,2) atom, and the same signs force the directed AP-below-HA/B-below-HB roles. The result is for this fixed target and panel, not arbitrary targets, root multi-hybrid rivals or joint parameter recovery. The outermost cover retains its explicit simple-or-atom predicate.

[Native supplier review (source availability)](README.md#source-availability) ([immutable public pin](https://github.com/Sodelin/Research-Commons/blob/384fa17668593dde93c793a5e9f504d80e9c35db/research/2026-10-31-g4-general-complete-j-interface/REVIEW.md)); [separate consumer acceptance (source availability)](README.md#source-availability) ([public pin](https://github.com/Sodelin/Research-Commons/blob/21c2a1bd9ecfd2234cbbe7c7a0ecf01db34c0f07/research/2026-10-31-g4-general-complete-j-interface/CONSUMER-ACCEPTANCE.md)). The former pending paragraphs of the intake cards remain dated history with their successor links.

## 11. Current boundary

Known-exterior simple-wrapper intrinsic pinning, one-gall family transfers, conditional structural inference, decoder-free orientation/known-role triples and explicit non-simple feature boundaries are proved at their stated hand interfaces. General finite COMMON determination, general finite natural BOTH forcing and entire natural-I⇒entire COMMON are already accepted suppliers, [with exact sources in chapter 02](02-G1-TO-G7.md). The remaining positive G4 goal is a finite legal I panel forcing the inherited finite COMMON certificate for every fixed admitted target against every unknown-size finite rival. Unique graphs/words/all latent parameters are optional stronger routes. A sound actual-fibre enclosure with constant required coordinates suffices positively; a negative or G3 YES requires an actual strict finite same-tuple lift. Current components do not yet supply that finite bridge. Earlier numerical scans, failed covers, retracted global-curve wording and invalid endpoint-Sturm shortcuts remain failed/superseded evidence, not assumptions.
