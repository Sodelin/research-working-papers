# Phase recovery from a noisy sequence window

The [grouped-sequence source](GROUPED-PHASE.md) proves sharp
**noiseless** phase and parameter thresholds for a particular family of
substitution fixed points. This note adds a phase-labelled Hamming-distance
interface and two finite exact examples. The new deductions are elementary
and **await independent review**. They do not claim that the supplied fixed
word or its binary substitution-error model describes biological sequence data.

## Retained noiseless statement and its provenance

For `n≥1`, write `q=2n` and let `uₙ` be the infinite fixed point starting
in `0` of

```text
τₙ(0)=0ⁿ1ⁿ,     τₙ(1)=1ⁿ0ⁿ.
```

For a length-`L` factor at an unknown position, the level-`k` phase is its
starting residue modulo `qᵏ`. The retained [reading-edition proof](../manuscripts/sequence/Pattern-Hierarchies-and-Selected-Digit-Proofs.md)
states that the least length at which every factor has exactly one phase is

```text
Dₙ(k)=q^(k−1)(4n²−n)+1,       n,k≥1.
```

The edition proves an explicit first-level ambiguous word, then uses a
uniform-substitution phase-scaling lemma whose columns are permutations. The
same edition reports the separate common-factor supplier and its independent
AI acceptance; that supplier's original hashed review body was not recovered.
Neither grouped result is claimed Lean-verified. The actual phase is relative
to a construction grid and does not identify an absolute occurrence.

The source literature already contains general recognizability and
synchronization work, including [Durand–Leroy](https://cs.uwaterloo.ca/journals/JIS/VOL20/Leroy/leroy4.pdf)
and [Klouda–Medková](https://arxiv.org/abs/1507.05223). Their definitions
and window conventions are not silently equated with `Dₙ(k)`. In particular,
an exact threshold for this one source family is not a new general
recognizability method or an established solution to a named open problem.

## The classical distance idea, applied to phase labels

Fix `n,k,L`, and let `C_p(L)` be the set of length-`L` factors of `uₙ`
occurring at start residue `p mod qᵏ`. The sets can overlap. Let

```text
d_phase(L) = min { d_H(x,y) : x∈C_p(L), y∈C_r(L), p≠r },
```

where Hamming distance counts differing positions. The finite alphabet and
finite number of phases and length-`L` words make this minimum attained;
all residues occur as starting positions in the infinite word. A word in two
phase sets makes the distance zero.

Suppose the received word has the same length as its true factor and at
most `e` substitutions, with the true factor allowed to be any factor at any
position. Then **every** received word compatible with the promise identifies
its phase exactly if and only if `d_phase(L)≥2e+1`. To see sufficiency,
two different phase candidates within distance `e` would be within distance
`2e` of each other by the triangle inequality. Conversely, if two different
phase factors differ at `d≤2e` positions, form a received word by changing
up to `e` of those differing positions from one factor toward the other;
the remaining distance to the other is also at most `e`. The received word
then admits both phases. If a received word has no candidate within the
promised radius, a sound decoder should report that the promise is not met;
the theorem does not provide a true phase for such an input.

This is a labelled-set specialization of classical error-correction geometry,
not a new coding-theory discovery. [Hamming's 1950 paper](https://onlinelibrary.wiley.com/doi/10.1002/j.1538-7305.1950.tb00463.x)
already develops Hamming distance and the single-error distance criterion;
the source-based phase labels and their finite calculations here are a
separate guide comparison. We require separation only **across different
phase labels**, not between two different factors having the same label.

For a fixed infinite word and modulus, `d_phase(L)` is nondecreasing and can
increase by at most one when `L` increases by one. Prefixing an `L+1` pair
gives two legal `L` factors at the same respective start phases, proving the
lower inequality. Conversely, extend a minimizing `L` pair by one true next
symbol in the infinite word; its Hamming distance increases by at most one.
This is a guide argument, not a separate checked Lean endpoint.

## Two complete finite controls for ordinary Thue–Morse

Take `n=1`, so `u₁=t`, the binary digit-parity Thue–Morse word. Its noiseless
thresholds are `D₁(1)=4` and `D₁(2)=7`. For at most **one substitution**,
the finite factor/phase calculation gives:

| Level `k` | Window `L` | Distinct factors | `d_phase(L)` | Received words with multiple possible phases |
| --- | ---: | ---: | ---: | ---: |
| 1 | 11 | 32 | 2 | 4 |
| 1 | 12 | 36 | 3 | 0 |
| 2 | 14 | 42 | 2 | 4 |
| 2 | 15 | 44 | 3 | 0 |

Hence the smallest guaranteed one-error lengths in this exact fixed-word
experiment are **12 at level 1** and **15 at level 2**. The upper claims
use complete finite phase inventories and the distance argument. The lower
claims hold for the preceding lengths and for every shorter length: truncate
the same ambiguous received word and both actual factors to that length.

For example, at level 1 the length-11 factors at positions 10 and 43 are
`01011010010` and `01001011010`, with residues `0` and `1`. The received
word `01001010010` is one bit away from each. At level 2, positions 20 and
30 give `01100110100110` and `01100101100110` with residues `0` and `2`
modulo four; `01100100100110` is one bit away from each.

The historical control reused the existing complete
finite-factor routine: it obtains the legal adjacent-pair closure, expands
the uniform substitution until an image is at least `L` and the level is at
least `k`, then enumerates all windows crossing at most two consecutive
expanded images with their start residues. It computes distances between all
different-phase pairs and enumerates all radius-one received words. Its
reported tests independently generated the
first 4,096 digit-parity symbols and recover the same full phase inventories
for the two positive cases. A long finite prefix alone would not prove an
infinite factor inventory; completeness uses the substitution/pair-closure
argument. No general noisy-phase formula for arbitrary `n,k,e` is asserted.

This is an adapted reading copy of the source guide identified in the collection provenance. The finite calculations and tests above are historical source reports; this edition did not rerun them or independently review the deductions. The underlying result sources keep their own AI authorship and review limits.
