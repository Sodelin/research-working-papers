# A sampled locus on the original source record

This is a hand construction for the next source/observation join. It is not a Lean declaration, compiler receipt, physical-model identification or proof that real sequence data follow the model. In particular, the almost-sure source and JC properties used below are currently attempted by uncompiled candidates.

At local source epoch `287dd45ed007b897302a7530e914406cdef19b1e` the complete working bodies of JCLocusCoreDraft.lean (internal supporting file not included: `JCLocusCoreDraft.lean`), JCSourceMeasuredLocusDraft.lean (internal supporting file not included: `JCSourceMeasuredLocusDraft.lean`), JCAveragedLocusDraft.lean (internal supporting file not included: `JCAveragedLocusDraft.lean`) and PulseFullSuffixLocusJointDraft.lean (internal supporting file not included: `PulseFullSuffixLocusJointDraft.lean`) matched Git. Their respective SHA-256 values are `4633b2956d16b83bb54ccf79305fb53489c82dd86ce7b85cc5bb40f26a16749b`, `e09454fb8678f54a10a19c567d01d4183e62040439ffc795bac435f396dfcb2c`, `d5680309477633a79a137cec0ad3db33de9553172757158b29d9e51371e43259` and `0eeed3130e24305c635a36faa62037e12a2e3a8078bd42f1cdf67dcaa5a91ce3`. The epoch is an exact local Git source selection, not an owner-selected compilation context.

## Conditional construction

Let `Ω` be the measurable space of the **original complete source record** and `μ` its selected probability law. Let `L` be the finite set of two-site patterns on six labelled samples, and for each `ℓ ∈ L` let

$$
q_\ell(z)=\operatorname{jcPanelConditionalLocusMass}
  (\operatorname{zeroEdgeActualTree}(z),\ell).
$$

The attempted `zero_edge_actual_conditional_locus_measurable` states that each `q_ℓ` is measurable; `zero_edge_actual_conditional_locus_law` attempts nonnegativity and normalization **almost everywhere**, not necessarily on every syntactically possible record. Assume those statements and the selected source probability law for this construction. Because `L` is finite, the set

$$
V=\{z: (\forall\ell\in L,\ q_\ell(z)\ge0)\quad\text{and}\quad
                     \sum_{\ell\in L}q_\ell(z)=1\}
$$

is measurable and has `μ(V)=1`. Choose one fixed pattern `ℓ₀`, for example the all-zero nucleotide pattern, and define a pointwise valid finite mass by

$$
q^*_\ell(z)=\begin{cases}
q_\ell(z),&z\in V,\\
\mathbf 1_{\{\ell=\ell_0\}},&z\notin V.
\end{cases}
$$

Every `q*` is measurable, lies in `[0,1]`, and the `q*` values sum to one **for every record**. The fallback only changes a `μ`-null set. It does not assert that invalid records are biologically possible or supply an unproved validity theorem.

The later fallback source candidate (internal supporting file not included: `SafeConditionalLocusDraft.lean`), source commit `a5fd7960cf54a19986488a2ea9b54fb47f77f05c`, 7,461 bytes/SHA-256 `8cee02c38ab20bf6299f4ab0b1a9c2b264a9a9dfaef81b5d38c0600d281f3767`, attempts the validity-set measurability, pointwise fallback law, almost-everywhere equality and preservation of the existing average. Its source-specific versions use the same selected complete record and the existing conditional-law candidate. This is not a sampled joint measure: the measure construction below is not yet in that file. The new source and all its dependencies remain unreviewed and uncompiled; the pending r29 packet did not contain it.

For a measurable `A ⊆ Ω × L`, write `A_ℓ={z:(z,ℓ)∈A}` and define

$$
\nu(A)=\sum_{\ell\in L}\int_{A_\ell}q^*_\ell(z)\,\mu(dz).
$$

Each section `A_ℓ` is measurable; each weighted term is a finite measure, and the finite sum is a probability measure. Summing the pointwise conditional masses shows that its record marginal is exactly `μ`. Its locus marginal at `ℓ` is `∫ q_ℓ dμ`, because `q*` and `q` agree almost everywhere. This is the same integral used by the attempted `zeroEdgeAveragedLocusMass`; no independent pair genealogies or independently averaged site masses are introduced.

Dot's r29 review (internal supporting file not included: `subspace-msci-delivery-20261031.md`) independently describes this standard finite-output continuation in general, conditional on the already named almost-everywhere law; it did not receive or review this later note. The subsequent joint-measure source candidate (internal supporting file not included: `RecordLocusJointMeasureDraft.lean`), commit `eaf31cbab1ed6dd67ba42d36feb5d4ef878d6709`, 11,138 bytes/SHA-256 `737ce8f38e235d675ed32bba41af5e066ae120b5acb8ce36a818f445c91e6267`, attempts the weighted-record measure, its original-record marginal, probability normalization and each individual pattern marginal. It explicitly assumes a measurable pattern space with measurable singletons; a finite discrete space is a natural later choice that must be instantiated. The source was not supplied in r29 and has no Lean or peer receipt. Its sum is symbolic, not a claim of an efficient enumeration.

## Preserve the pulse and sampled observation jointly

Let `R(z)` be the pair consisting of the original first-interval segment and the canonical readout of the same record's pulse-time path. For any measurable set `B` of these pairs,

$$
\nu\{(z,\ell'):R(z)\in B,\ \ell'=\ell\}
=\int \mathbf1_B(R(z))q_\ell(z)\,\mu(dz).
$$

The attempted full-suffix theorem records the same three components on the original endpoint-matched mixture. Its Lean product is right-associated as `(first,(canonical,q))`; a formal argument must supply the measurable reassociation to `(R,q)`. If that theorem and its suppliers are checked, the right side is recovered from the reassociated law using the bounded measurable test `(r,t) ↦ 1_B(r) max(0,min(1,t))`; clipping changes nothing on the full-measure valid set. Thus the proposed sampled-locus joint distribution can use the **actual attached suffix and ancestral tail** rather than choosing a fresh genealogy from a canonical output. This is a conditional hand derivation; no equality of a canonical-state future law is assumed.

The pattern type has `4^(2·6)=16,777,216` possible labelled patterns. The sums above are finite mathematical expressions, not a claim that materializing or enumerating this table is a practical computation. A future implementation or formal proof may use the existing conditional node-sampling factorization, provided it proves the same joint law. This construction concerns one locus; independent replication across loci, identification with the intended physical pulse/JC process, the pair transforms, proof elaboration, object/axiom audits and independent scientific review remain separate obligations.
