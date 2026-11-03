# Quantum testing, noisy dynamics, scattering and structural certificates

The shared mathematical ideas are finite nets, positive moments, risk comparison, contraction and compatibility fibres. Their source contracts differ. A scattering matrix construction is not a fixed-contact Hamiltonian realization; a good numerical fit is not a presence certificate; an auxiliary completely positive evolution cannot supply positivity of Redfield dynamics.

## P1: copy complexity and a measurement-level information bound

**CB-PHYS-P1-001.** Two unknown N-qubit Gibbs states share one known fixed β>0. Each Hamiltonian is at most k-local with each nonidentity Pauli coefficient bounded by 1. There is **no** degree or total per-site strength bound. Test equality against FULL trace norm≥ε, allowing collective/adaptive measurements and charging the worst-case total copies from both sources. Put M=Σ_{j=1}^k3^j binom(N,j).

**Upper proof.** Round each of the M coefficients on a certified rational grid of spacing O(ε/(βM)); coefficient error bounds Hamiltonian operator error by its sum. The Gibbs Lipschitz supplier transfers that error to trace distance. The resulting finite admitted net has log size O(M log(2+βM/ε)). Fix Helstrom witness projectors for net pairs before seeing either unknown source. Their paired positive-contraction effects commute across the two systems: every mean is1/2 under equality, whereas a separated pair has a net witness with a constant times ε excess. The collective threshold-DECISION supplier tests this finite family using O((log net size+log(1/δ))/ε²) paired samples. Charge two unknown copies per paired sample. Certified Hermitian approximations preserve the witness gap; mesh singleton and zero-distance cases are separate trivial branches. Therefore

$$
O\!\left(\frac{M\log(2+\beta M/\varepsilon)+\log(1/\delta)}{\varepsilon^2}\right)
$$

total copies suffice. This is a copy bound without efficient-computation or single-copy-measurement claims. Threshold search has a different imported complexity and must not replace threshold decision. [Complete upper](https://github.com/Sodelin/Research-Commons/blob/809dcb6dcef78da700fddd888e9177bcff098b0f/research/2026-10-16-g6-gibbs-certification/COLLECTIVE-CERTIFICATION-UPPER-13.md), [exact independent review](https://github.com/Sodelin/Research-Commons/blob/bf1d9a0e98b99eaf0a7d229de640a345210b78d4/research/2026-10-16-g6-gibbs-certification/COLLECTIVE-UPPER-13-INDEPENDENT-REVIEW.md).

**Lower proof chain.** A classical closeness-testing hard family is encoded into diagonal Gibbs states using actual signal/clone/reservoir spins. Coefficientwise bounded terms lock clone blocks; conditional minority-count and reservoir-energy estimates bound leakage without assuming their independence. Smoothing preserves exact equality and sufficient trace separation. Diagonal quantum measurements, including collective/adaptive processing, are classical postprocessing of samples, so a faster quantum test would violate the classical lower bound. All auxiliary spins enter physical N. Padding zero-Hamiltonian spins covers every sufficiently large N. The different accepted encodings yield:

| Supplier | Domain, with fixed k,β,ε | Lower copies |
|---|---|---|
|24|k≥3,0<ε≤1/4|Ω(N^{2k/3}/(log N)^{2/3})|
|26|k=3,0<ε≤1/256|Ω(N^{9/4}/(log N)^{9/8})|
|27|k=4,0<ε≤1/256|Ω(N³/log N)|
|27|k=5,same ε domain|Ω(N^{7/2}/(log N)^{7/8})|
|29|k≥5,0<ε≤1/1024|Ω(N^{(2k+1)/3}/(log N)^{(2k+1)/(3(k−1))})|
|32|k≥5,0<ε≤1/4096|Ω(N^a/(log N)^{a/(k−1)}), a=min{(2k+2)/3,(4k−1)/5}|

The clone/reservoir combinatorics are nontrivial named suppliers, not proved by that paragraph. The [24 review](https://github.com/Sodelin/Research-Commons/blob/0e3e40d07edb9292a2c5a4c64c8f6fe0ae56e98d/research/2026-10-16-g6-gibbs-certification/reservoir-amplified-lock-24/P1-RESERVOIR-AMPLIFIED-LOCK-REVIEW-24.md) checks physical support collisions, both parity cases and N_s=O(s(log s)^{1/k}); [32 source](https://github.com/Sodelin/Research-Commons/blob/9b7bb4034a136542a4d2c06afce84c64d1a50ce3/research/2026-10-16-g6-gibbs-certification/latent-light-fraction-32/README.md) links the strongest listed encoding. The canonical catalogue binds26/27 reviews and the earlier shell21, which remains valid including its k=2 domain. Take the strongest applicable rate only on complete domain intersections. The optimal general upper/lower and accuracy/temperature dependence remain separate.

**CB-PHYS-P1-002 — actual PGM.** For a finite prior(p_i,ρ_i), set R_i=ρ_i^{⊗n}, S=Σp_iR_i, and use the n-copy POVM Λ_j=p_jS^{−1/2}R_jS^{−1/2} on its support. Its actual joint weights are w_ij=p_iTr(R_iΛ_j), with Σw_ij=1. Define affinity A_ij=Tr(√ρ_i√ρ_j), square-root loss Q_n=2Σw_ij(1−A_ij), and δ_n=χ(n+1)−χ(n). Then

$$
R_{\rm Bures^2}(\mathrm{PGM})\le Q_n
\le2(1-e^{-\delta_n})\le2\delta_n,
\qquad R_{\|\cdot\|_1^2}(\mathrm{PGM})\le4Q_n\le8\delta_n.
$$

**Short full matrix argument.** For a CPTP Φ, σ=Φ(I), density r and F(z)=σ^{(z−1)/2}Φ(r^z)σ^{(z−1)/2}, the function f(q)=log||F(q)||_{1/q} is convex on(0,1]. Indeed the positive2×2 matrix with diagonal r^q and off-diagonal r^{q+it} stays positive under Φ; its off-diagonal block factors as Y^{1/2}KY^{1/2}, ||K||≤1. Schatten Hölder bounds its p-norm by||Y||_p. Imaginary σ powers are outside and unitary. Three-lines interpolation gives convexity. Now f(1)=0 and
f'(1)=D(r||I)−D(Φ(r)||σ)=Δ. The tangent at 1 gives
Δ≥−log||σ^{−1/4}Φ(√r)σ^{−1/4}||²_2.

Take the block Gram matrix G_ij=√(p_ip_j)√R_i√R_j and the channel Φ(X)_ij=X_ij⊗√ρ_i√ρ_j. Kraus vectors |i,u⟩↦|i,u⟩⊗√ρ_i e_a prove CPTP. G and S have the same nonzero spectrum; Φ(G) has the(n+1)-copy average's spectrum. Thus Δ=δ_n. Functional calculus gives ||(√G)_ij||²_2=w_ij, and the squared Hilbert–Schmidt norm in the bound is Σw_ijA_ij=1−Q_n/2. This proves the displayed Q bound. Regularize singular G on the fixed output support and pass to the finite-dimensional continuous limit; no eigenvalue floor is assumed. Affinity≤root fidelity and the fidelity/trace inequality give the two operational risks. The extra register in this proof is algebraic, not another unknown copy. [Full proof, including support and interpolation details (source availability)](README.md#source-availability), [immutable original](https://github.com/Sodelin/Research-Commons/blob/43cebb410eed5fbf6764b000f0b2e40d77090e25/research/2026-10-20-p1-pgm-information-increment/P1-PGM-AFFINITY-INCREMENT-20261020-v2.md).

**Related accepted comparison.** Embed ρ↦√ρ in the real Hilbert space of Hermitian matrices, including the identity coordinate. The actual PGM's scalar quadratic risk is≤2 times optimal scalar Bayes risk: in an eigenbasis of S this reduces to2/(s_u+s_v)≤1/√(s_us_v). Sum the scalar inequalities using **one common state-valued estimator** and Parseval; do not assume separately optimal scalar measurements are jointly implementable. Since Bures²≤||√ρ−√σ||²_2≤2Bures² and full trace²≤4Bures², one obtains R_PGM,Bures²≤4R*_Bayes,Bures² and R_PGM,trace²≤16R*_Bayes,Bures², without a dimension-squared factor. [Complete comparison](https://github.com/Sodelin/Research-Commons/blob/2a2ee35f0660daaa6c41c78ad8c1f6e636ce935f/research/2026-10-19-p1-distance-weighted-pgm-route/actual-distortion/square-root-comparison/P1-SQUARE-ROOT-PGM-COMPARISON-20261019.md).

Neither argument proves a uniform Gibbs δ_n=O(M/n) or corresponding dyadic Holevo bound. A cumulative O(M log n) bound does not give a constant dyadic increment by subtraction. Prior-independent two-source construction and full copy accounting remain required. The theorem is not measured Umegaki-risk equality or generic unrotated Petz recovery.

## P5: actual generator comparison and its boundary

**CB-PHYS-P5-001.** Accepted components include finite-window support decomposition, signed-energy identities, auxiliary interacting-noise influence estimates and incidence velocity3kh. The full infinite-filter commutator estimates are part of the operator-incidence supplier. Its integrated auxiliary reference needs g>3kh, guaranteed for general k=2 in the original box, not all k. These suppliers cannot be relabelled as a complete actual Redfield/original-GKSL comparison. [Operator-incidence source](https://github.com/Sodelin/Research-Commons/blob/04c9808f1fc4ec3c1c57cdbca200e91e82d32d5d/research/2026-10-20-p5-operator-incidence/README.md).

**CB-PHYS-P5-002.** The initial reviewed packet also contains a two-qubit actual Redfield nonpositivity example: a positive initial state evolves to a nonpositive operator under that specified generator. It defeats the shortcut “Redfield evolution is always positive,” not every comparison estimate. The example's exact generator/state calculation is a linked supplier, not reconstructed from an acceptance summary. [Initial scoped review](https://github.com/Sodelin/Research-Commons/blob/d855ab1267d2e29719ff7e865aac7df85ef7c6a0/research/2026-10-16-p5-strong-noise-coarse-graining/P5-STRONG-NOISE-INDEPENDENT-REVIEW-01.md).

**CB-PHYS-P5-003 — commuting actual theorem.** Let H=Σ_ZJ_ZP_Z consist of commuting Pauli terms with sup_iΣ_{Z∋i}|J_Z|≤h. Set S_i={i}∪⋃_{Z∋i}Z; require|S_i|≤m and at mostν such sets through each site, uniformly in volume. All sites have independent X/Y/Z channels with positive-type thermal covariance, Φ(−s)=conjΦ(s), |Φ(s)|≤(γ/τ_B)e^{−|s|/τ_B}, Re∫_0∞Φ≥b_0γ>0. For

$$
g=8b_0\gamma-2h-24\nu2^m\gamma h\tau_B>0,
\quad \delta=3\nu(32\gamma hT+4\gamma\tau_B/T+8\gamma h\tau_B),
$$

the actual full-infinite-filter Redfield R and original square-window GKSL L_T with triangular Lamb shift satisfy, for every s-site O, finite volume and t≥0,

$$
\|e^{tL_T^*}O-e^{tR^*}O\|\le 2^s\|O\|\delta/g.
$$

**Proof.** Commutativity localizes A_i(−u)=e^{−iHu}A_ie^{iHu} to S_i, with variation≤2h|u|. Freeze at A_i. The Redfield correction per channel is≤8γhτ_B. The finite-window dissipator/ordered Lamb-shift error is≤32γhT+4γτ_B/T. Only 3νw(P) channels meet a Pauli string P, hence ||(L_T*−R*)P||≤δw(P). Frozen X/Y/Z noise damps each occupied Pauli site by at least8b_0γ. Hamiltonian column norm costs≤2hw(P); correcting Redfield costs≤24ν2^mγhτ_Bw(P), using local Pauli ℓ1≤2^m operator norm. For nonidentity Pauli coefficients put V=Σ|c_P| and W=Σw(P)|c_P|. Thus D⁺V≤−gW, so ∫_0∞W(e^{uR*}O)du≤V(O)/g. Identity output cannot feed back since R*(I)=0. Duhamel with the **CP unital L_T evolution on the outer side** contracts operator norm and gives δV(O)/g≤2^s||O||δ/g. Redfield positivity is never used. This also bounds expectations for every initial density, entangled or not. [Full proof and exact original generator conventions](https://github.com/Sodelin/Research-Commons/blob/d855ab1267d2e29719ff7e865aac7df85ef7c6a0/research/2026-10-16-p5-strong-noise-coarse-graining/P5-STRONG-NOISE-COMMUTING-PAULI-CANDIDATE.md), [separate PASS](https://github.com/Sodelin/Research-Commons/blob/d855ab1267d2e29719ff7e865aac7df85ef7c6a0/research/2026-10-16-p5-strong-noise-coarse-graining/P5-STRONG-NOISE-INDEPENDENT-REVIEW-01.md). This is not microscopic system–bath accuracy or a global/multitime estimate.

**CB-PHYS-P5-004 — unrestricted comparison counterexample.** The later owner hand proof retains the actual same static H in full infinite Redfield filters and the original square-window GKSL with **ordered** Lamb shift. For each integer ℓ≥40 fix γ=1, τ=2^{−ℓ}, b_G=e^{−1/8}√(π/8)e^{−1/128}, originalΓ=9/4, b_0=2b_G/9,h=b_G/4,j=b_0/2,k≤12,m≤30,ν≤30,β=τ/8 and T=√(τ/Γ). Positive normalized initial densities and fixed O=X_1Y_2X_3 give an infinite supremum of the difference's operator norm over volume/time. On sufficiently large balanced binary trees N=2^{q+1}−1, a finite real-grid maximum of actual predictions is≥exp(y²√N/55296), y=b_Gτ/32>0, at times≤N^{−1/2}.

**Proof chain, not a replacement of its 111288-byte argument.** A negative projected Redfield rate gives a positive first derivative for one logical functional. Static clock spins, binomial-tail control and ordered gates embed that functional in the same physical H with bounded supports. Touched-support Dyson/cb estimates control higher terms, weak links and full infinite-filter tails. Finite analytic interpolation converts the derivative and complex bounds into real source-grid/time/probe values with positive initial states. Actual thermal Gaussian/KMS channels and original normalization are checked. The Redfield prediction grows while the original CP-GKSL prediction stays bounded by||O||=1, forcing unbounded difference. The tail exponent N^{2/3} dominates √N log³N, and interpolation/weak-link losses are o(√N). Each named supplier is essential. [Complete owner proof](https://github.com/Sodelin/Research-Commons/blob/c98b221d605f7dda739f249e1a9e049136fed51c/research/2026-10-23-p5-original-comparison-hand-proof/P5-ORIGINAL-COMPARISON-HAND-PROOF-v1.md), SHA964fe1e3070913ea64b0ffca5de65c271ada7f966c808dd2f29ca0e35152c264; [owner verdict and supplier graph](https://github.com/Sodelin/Research-Commons/blob/c98b221d605f7dda739f249e1a9e049136fed51c/research/2026-10-23-p5-original-comparison-hand-proof/P5-HAND-PROOF-VERDICT-v1.md).

Every future finite-witness search must start at q≥4ℓ+80, by the [admission correction](https://github.com/Sodelin/Research-Commons/blob/c98b221d605f7dda739f249e1a9e049136fed51c/research/2026-10-23-p5-original-comparison-hand-proof/P5-FINITE-WITNESS-ADMISSION-CORRECTION-v1.md). No such search or full independent/formal review is claimed here. This unrestricted-tree boundary does not contradict narrower commuting or path/ring positive results.

## Reflection visibility: what each observation can identify

**CB-NANO-001.** In the fixed60-site known-normal-lead Rashba model, zero internal loss and **unrestricted finite scalar potentials**, two opposite visibility classes Q≤−0.1 and Q≥0.1 have zero separation in their full lowest-energy curves over B∈[0,2]. The potential of each device is fixed throughout its sweep.

**Proof chain.** Raise finite endpoint barriers while keeping the microscopic contacts fixed. A central chiral minor's exact rational inverse certificate proves a transverse crossing and nonzero endpoint weights. A Schur-complement limit narrows the effective coupling: two nearby fixed potentials on opposite sides retain opposite strict visibility limits, while their closed-wire lowest branches approach uniformly. Continuity selects finite admitted barriers for each desired curve tolerance. The rational finite fixture separately encloses opposite determinant margins and whole-field energy difference≤0.09999μeV. Conductance separates **that pair**; exact identical energy curves are not claimed. [Full construction/review/certificate](https://github.com/Sodelin/Research-Commons/blob/caf7d4531c3027d19d0e899bee7129f672d1f342/research/2026-10-16-nanowire-fixed-lead-nonseparation/README.md), [finite fixture](https://github.com/Sodelin/Research-Commons/blob/b6b1f91d84e58506b9028dec1ff0c59e05317224/research/2026-10-16-nanowire-fixed-lead-nonseparation/finite-example/README.md). The large-barrier limit does not authenticate a bounded-potential source, positive loss, original dataset generator or the different≥1μm unsupervised contract.

**CB-NANO-002.** For any finite N electron channels, a contractive canonical-PHS reflection matrix has conductance g and real determinant Q in the exact region

$$
0\le g\le2N,\quad |Q|\le1,\quad Q\ge1-g,
\quad(-1)^NQ\ge g-(2N-1).
$$

**Proof chain.** The Majorana contraction supplies an auxiliary fermionic state whose parity expectation is Q and mean occupation is g/2. The integer occupation inequalities (−1)^n≥1−2n and (−1)^N(−1)^n≥2n−(2N−1), averaged in that state, give the two bounds. The covariance/Pfaffian realization of this auxiliary state is the nontrivial algebraic supplier. Explicit endpoint contractions and a continuous path fill each permitted interval. Thus g<1 forces Q>0 without knowing N. This is sharp **algebraic** attainability, not realization by every fixed-contact wire. [Complete all-channel proof/review](https://github.com/Sodelin/Research-Commons/blob/f79a9a7626de25a58ee33d4a3dbff00f9f3f3db1/research/2026-10-16-nanowire-fixed-lead-nonseparation/all-channel/README.md).

**CB-NANO-003.** The saved known-device1mK forward enclosure, zero Hamiltonian drift and conductance error0.001 yields Q lower≈0.05925. Its 64-cell thermal quadrature includes the rigorous full upper bound4 for every failed enclosure cell;60 inverse witnesses and an independent Fermi-mass checker support the exact rational bound. It is a source-bound forward/error control, not a universal warm-to-cold inverse theorem, experiment or unknown-device certificate. [Execution/review scope](https://github.com/Sodelin/Research-Commons/blob/5055e470b32c17bdf93c55e09a891969be9ea23f/research/2026-10-16-nanowire-fixed-lead-nonseparation/thermal-model-budgets/refined-thermal-execution/PUBLICATION-README.md).

**CB-NANO-004 — exact transmission/sign fibre.** Take loss-free zero-energy, zero-temperature/bias canonical-PHS two-terminal scattering, two electron modes per lead. Observe g and the complete quasiparticle transmission spectrum0≤T_1≤⋯≤T_4≤1 from the **same** parent's t†t. Write a≥b≥c≥d=the ordered√(1−T_i), p=abcd, w_±=ab±cd. For p>0 the exact feasible determinant set is

$$
\{+p:|g-2|\le w_+\}\ \cup\ \{-p:|g-2|\le w_-\}.
$$

If p=0 it is{0} iff|g−2|≤ab, otherwise empty. In particular a negative-only set never occurs.

**Proof.** Oriented SVD and the four-dimensional Hodge supplier bound |2−g| by the largest complementary singular-product sum. For positive determinant it is ab+cd, since subtracting the other pairings gives(b−c)(a−d) and(b−d)(a−c). For negative determinant ab−cd dominates ac−bd and|ad−bc| by the analogous nonnegative products. With d=0 the radius is ab. Attain every point by D_σ=diag(a,c,b,σd), M=R_θD_σ, rotating the 3–4plane: the Hodge contraction is(ab+σcd)cosθ and detM=σp. Put C=√(I−D_σ²). The matrix

$$
S=\operatorname{diag}(R_\theta,I)
\begin{pmatrix}D_\sigma&C\\C&-D_\sigma\end{pmatrix}
\operatorname{diag}(I,R_\theta^T)
$$

is a common SO(8) parent: its left reflection is M and its left-to-right transmission is C, hence it has exactly the given spectrum. Undo the Majorana basis to obtain canonical PHS. If|y−g|≤η and T is exact, the best possible |g−2| is max(0,|y−2|−η); substitute that in the criterion. With uncertain T take a union over the authenticated **joint** error/source relation, not independent endpoint substitution. [Complete proof and Hodge supplier](https://github.com/Sodelin/Research-Commons/blob/bcb7c4e3d58b0eaab3c24d89f5971fedf92e14cd/research/2026-10-23-dot-nanowire-transmission-sign-fibre/TRANSMISSION-SPECTRUM-SIGN-FIBRE-20261023.md). This common algebraic parent still need not be a prescribed local microscopic Hamiltonian.

**CB-NANO-005 — closed symmetry route.** For the 60-site path adjacency A, skew path K (upper+1/lower−1), S_a=diag(a)−tA and t=501643/20000, real orthogonal O with OKOᵀ=±K and OS_aOᵀ=S_b implies b=a or reverse(a), with no genericity assumption. The accepted real spin-sector reduction extends this to the declared field-independent diag(O_+,O_−) spatial ansatz, trivial on Nambu coordinates, satisfying both S identities and O_+KO_−ᵀ=K.

**Proof chain.** Gauge by powers of i so K becomes iA and A becomes iK. The simple sine spectrum of A makes the commuting conjugacy diagonal in phase. Reality removes cross terms in squared moduli, giving all labelled distances among the 31 odd sine/Fourier coefficients. One-dimensional distance rigidity yields one common sign and translation, even with repeated coefficients; the 61-term geometric sum kills the translation. Trace/diagonal data determine even coefficients. Interpolation at 60 distinct cos(jπ/61) nodes recovers the profile, leaving only its original or reversal. For the spin ansatz the relative real rotation lies in the scalar symmetric commutant, reducing it to that classification. The actual fixed-contact scattering proof gives equal left/right reflection determinants through complementary principal minors, even for singular blocks; reversal with spin correction preserves the contacts. Thus b=a or reverse(a) has equal actual Q at B=2 for λ=5/2,Δ=1/5,B∈[0,2], endpoint self-energies−iI and zero internal loss. Opposite strict margins are impossible **within this ansatz and the same prescribed class**. [Complete classification](https://github.com/Sodelin/Research-Commons/blob/c22ac1651c6605e96b488695c02d0750104c204e/research/2026-10-16-nanowire-fixed-lead-nonseparation/spin-sector-classification/SPIN-SECTOR-PROFILE-CLASSIFICATION-CANDIDATE-18.md), [supplier-by-supplier independent review](https://github.com/Sodelin/Research-Commons/blob/c22ac1651c6605e96b488695c02d0750104c204e/research/2026-10-16-nanowire-fixed-lead-nonseparation/spin-sector-classification/SPIN-SECTOR-PROFILE-CLASSIFICATION-INDEPENDENT-REVIEW-18.md). Other transformations and the full bounded-potential master remain separate.

## Materials: equal descriptors need not close the dynamics

**CB-MATERIALS-001.** On the actual 12³ balanced lattice, and more generally L=12m with even L_z≥6, let A={0,1,4,6},B={0,1,3,7} modulo12 and σ_X(u,v,K)=a_X(u)(−1)^K, a_X=+1 on X and−1 elsewhere. Both are balanced. Their six unordered cyclic pair distances are1,…,6 once each, hence their periodic autocorrelations and all implemented pair sums agree. Fourier **amplitudes** also agree. Thus the eight/nine-pair descriptors and full retained amplitude augmentation D9F coincide; labelled arrays need not.

For an unlike swap i,j in a reciprocal four-neighbour class c,
ΔS_c=−2r_c(i)−2r_c(j)−4m_c(i,j), with r_c(i)=σ_iΣ_{neighbours}σ_j. For these striped configurations, r_ip1(u)=2+a(u)[a(u−1)+a(u+1)] and r_ip3(u)=2+a(u)[a(u−2)+a(u+2)], so both fields belong to{0,2,4}; the mutual multiplicity m_c is also nonnegative. In A there is no site with r_ip1=r_ip3=0. Therefore no accepted unlike swap can preserve both sums. In B the pair(7,0,0),(7,0,1) has both fields zero and reaches a destination descriptor y_B with ΔS_ip1=ΔS_ip3=0 but ΔS_c2=−8. Self loops/rejections cannot reach y_B from A. For the **actual half-local/half-arbitrary mixture**, its transition fibre mass is0 at A and at least α_T(d_B)/N²>0 at B for every finite T>0 and finite couplings. At the exact binary64-lifted fitted parameters d_B=41128429432628793/281474976710656meV; displayed decimals are not substituted for source coefficients. Thus no universal memoryless quotient on D9F satisfies the G2 intertwining K P=P B.

This exact one-attempt obstruction does not prove non-Markovianity of the later fixed-initializer/coarser-cadence observed history: its history-determinant conditioning probabilities are positive, but the needed determinant nonzero remains unproved. Energy still factors through pair descriptors. [Full source-bound homometric witness, field table and mixture proof](https://github.com/Sodelin/Research-Commons/blob/ab80109bcaf0edec8bc3eb58aea2fd369d824fa6/research/2026-10-15-codex-materials-exact-obstruction-2052z/MATERIALS-EXACT-MIXTURE-OBSTRUCTION-01.md).

## Diffraction: a presence certificate is a fibre statement

**CB-DIFFRACTION-001.** On declared observed bins let F(a,ν)=Sa+Nν, N=[1,h], and let Θ include every admitted source/provenance branch. With justified error ε define C_ε(y)={θ∈Θ:||y−F(θ)||≤ε}. If truth lies there and H(C_ε(y)) is a nonempty singleton, that singleton is its target. Proof: truth is one element of the set. A best fit alone supplies neither premise.

For a desired label ℓ let r_ℓ=inf_{H(θ)≠ℓ}||y−F(θ)||. If C_ε is nonempty and ε<r_ℓ, only ℓ fits. If ε>r_ℓ, an admitted wrong-label witness fits by the definition of infimum. At equality one needs attainment, not just distance to a closure. With unrestricted Euclidean ν, orthogonal projection P off col(N) gives min_ν||y−Sa−Nν||=||P(y−Sa)|| by Pythagoras. Project **both** observations and templates. Constrained nuisance projection is only a relaxation. Forward column errors add at mostΣ|a_i|η_i+|β|η_h by the triangle inequality, so a coefficient-independent radius needs justified coefficient bounds. Statistical coverage transfers only from a supplied honest residual event, simultaneous if inspected sequentially.

The audited molecular case has 32labels but lacks numerical profiles/templates, a complete fit registry and calibrated errors. The table's4merE/prose-and-supplement4merI ambiguity must remain two provenance branches until resolved. No empirical fit, presence certificate or physical validation was produced. [Complete conditional proof, nuisance/error and exact-boundary analysis](https://github.com/Sodelin/Research-Commons/blob/6a7d50f699245c87727961f59808c1ec0c9adfe5/research/2026-10-16-ge-diffraction-certification/CONDITIONAL-CERTIFICATE-01.md).
