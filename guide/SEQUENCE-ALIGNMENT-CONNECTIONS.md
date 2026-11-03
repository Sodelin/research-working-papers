# Sequence recovery, subsequences and alignment: distinct receivers

This Codex/OpenAI synthesis preserves the original source attribution and review limits. It connects retained sequence material to concrete mathematical and implementation tasks without counting external literature as an original result. No new proof, compiler, solver, benchmark, clinical/biological analysis or human review occurred here.

| Object | What is available | Useful question or receiver | Exact remaining gap |
| --- | --- | --- | --- |
| Grouped substitution phase | An explicit noiseless grid-phase threshold for the stated binary substitution family | Synchronization and labelled-window decoding in this exact construction | General noisy/error formula, implementation and source-specific review; phase does not identify absolute position |
| Finite noisy Thue–Morse examples | Complete factor/phase controls giving two one-substitution threshold examples, with a classical cross-label distance criterion | An exact phase-labelled error-correction test fixture | Review/completeness correspondence and wider parameters; no biological barcode or indel model follows |
| Thue–Morse/complement LCS | Established external asymptotic bounds and bounded exact guide controls | Best–Peres's growth-exponent question and an exact algorithm oracle for proposed constructions | The retained later deletion-walk proof/checker/review packet is not recovered; no new growth theorem is claimed |
| Multiple random-string LCS | External expected-LCS bounds under independent uniform inputs | A probabilistic baseline and a separate deletion-code interface | Different inputs/quantifiers, not a theorem for the deterministic pair or correlated genomic sequences |
| Native exact alignment | A standard exact recurrence and a known upstream ranged-indexing repair in a Rust diff library | A version-pinned, independently checked implementation of the declared edit objective | Current caller/version, exact-versus-deadline behavior, authorized build and semantic refinement; no product impact or installed fix is established |

## Phase labels give a concrete error-correction interface

For τ_n(0)=0^n1^n, τ_n(1)=1^n0^n and q=2n, the retained hand edition's sharp noiseless level-k threshold is q^(k−1)(4n²−n)+1. Its object is a residue of the unknown starting position modulo q^k. Known n,k, the fixed construction and the permitted window model matter. This is not a general theorem identifying positions in arbitrary sequences.

The noisy guide instead takes C_p(L), the true length-L factors at phase p, and minimizes Hamming distance **across different phase labels**. At most e substitutions can be corrected for every admitted received window precisely when that minimum is at least 2e+1. Two different factors with the same phase need not be separated. An input outside every admitted radius must not be assigned a guaranteed true phase.

The [finite phase-control note](NOISY-SEQUENCE-PHASE.md) gives one-error thresholds 12 for ordinary Thue–Morse level one and 15 for level two. Their completeness relies on the substitution/adjacent-pair argument, not just a long sampled prefix. The examples and new guide deductions await independent review and are not a new general error-correcting-code theory or Lean endpoint. No general formula for arbitrary n,k,e is supplied. Real barcodes, UMIs, uncertain alphabets, indels and a biological read process require separate scientific admission; a shared Hamming-distance vocabulary is insufficient.

## An external open direction must not be replaced by a missing packet

Let S(n) be the LCS of a length-n Thue–Morse prefix and its complement. In Best–Peres's convention, D(n)=n−S(n) is half the total number of insertion/deletion operations. Their Proposition 3 gives D(n)≥sqrt(n/6)−1; Section 5.1 asks for the logarithmic growth liminf/limsup and whether they coincide. The current arXiv record read here identifies v3, revised 17 September 2025. These are the authors' statements and research question, not a new result from this archive or a complete present-day literature determination. [Primary v3](https://arxiv.org/html/2501.00440v3), [version record](https://arxiv.org/abs/2501.00440).

The retained guide also records Blikstad's published constructive bounds, separating the [later journal article](https://doi.org/10.1016/j.ipl.2020.106020) from the [older arXiv version](https://arxiv.org/abs/1904.00248v2). Its version-specific warning about a missing n in one displayed Best–Peres upper bound is preserved rather than silently using that expression. No author-confirmed correction or full independent proof audit is claimed.

The retained reading-edition status mentions a later deletion-walk lower-bound/relaxation packet but does not supply its proof, checker or review. Bounded searches through the installed selected evidence/path discovery did not recover that packet in this assessment. Those snapshots are not all research history. The gap is source recovery and exact comparison with prior work; neither a status sentence nor numerical controls can substitute for the missing argument. No old worker was awakened and no new proof task was started.

Li–Ren–Wen's separate multiple-string theorem concerns γ(k,d), the limiting expected common-subsequence fraction of d independent uniform k-symbol strings, with n tending to infinity first for fixed k,d. Its binary estimate is 1/2+Θ(d^(−1/2)); its larger-alphabet upper/lower corrections differ by sqrt(log k) in the stated regime. The selected primary preprint statements were read, not independently proved. This does not solve the deterministic Thue–Morse exponent or supply an exact finite-input multiple-alignment algorithm. [Primary preprint](https://arxiv.org/html/2504.10425v1), [journal record](https://doi.org/10.1017/S000497272610104X).

## Preserve the algorithm and its actual caller

The exact two-string LCS recurrence is a useful independent reference, with quadratic time and linear length-only storage in the rolling-row form. It corresponds to a global insertion/deletion objective, or substitution cost two under matching conventions. Unit-cost substitutions, affine gap penalties, local alignment and evolutionary likelihoods are different tasks.

The selected local `similar` 2.7.0 LCS source has a recorded source-level offset counterexample: `0001` versus `0100` should preserve three symbols, while the traced old path retains two. The Rust implementation was not run in that guide. The [upstream repair](https://github.com/mitsuhiko/similar/commit/5ab26a8a1d92083793aef24eb56f75d038fcfe28) was read here and does correct ranged indexing and add regressions. Its existence is not a completed local upgrade. The visible preview caller was reported to default to Myers; no current production LCS use or impact has been established. A deadline fallback may intentionally be approximate and must retain that status.

Useful integration work is therefore specific: pin the actual caller and objective, select an applicable implementation/version, test exact outputs against a genuinely independent oracle, preserve approximation/timeout states and verify compatibility within the existing owner's authorized execution window. This note neither modifies that owner's project nor reopens any device/build/model hold.

Source identities and the limited primary readings are recorded in the collection provenance. The current result is a correspondence and recovery map, not an assertion that every selected alignment entry is novel, proved, deployed or externally reviewed.
