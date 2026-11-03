# Matching heights and a restricted juggling series

The existing [Thue–Morse hand edition, Parts II–III](https://github.com/Sodelin/research-working-papers/blob/98e38d4ce6384cb5051b42ef30f758e68dcda688/manuscripts/sequence/Thue-Morse-Hand-Proofs.md) gives two specific applications of a matching-graph theorem. These are attributed to dot (OpenAI), using an earlier matching-height theorem and digit recurrence. They do not solve the enumeration of all juggling patterns or establish a new physical limit on juggling.

At the three-ball ground state, the primitive loops (3) and (4,2) encode bits 0 and 1. This code and first-return parsing are classical. Replacing each bit-labelled edge of the original avoidance graph by its own code path, retaining distinct constraint vertices, transports its exact maximum L(v) to throw count H(v)=W(L(v)), where W(k)=k+sum_(j<k)t(j). The resulting H(v)<=4v for v>=1 has equality exactly at v=3*2^(2r)-1. Individual throws are at most 4. The unconstrained encoded infinite Thue–Morse routine can continue forever; the finite maximum comes from the additional avoidance graph, not the physical juggling state graph.

For two distinct primitive loops at a common b-ball state with positive beat lengths a,c, count one pattern per Thue–Morse block-prefix length, including the empty bookkeeping prefix. With P(x)=product_(r>=0)(1-x^(2^r)), the source derives

```
F_(a,c)(z) = [1+(z^a+z^c)/2]/(1-z^(a+c))
             + (z^a-z^c)P(z^(a+c))/2,   |z|<1.
```

If a=c this is 1/(1-z^a). If a differs from c, the unit circle is a natural boundary; for b>=2, F_(a,c)(b^(-s))-1 has boundary Re(s)=0. This applies the classical Thue–Morse product to a specified subset. The prefix family is not closed under concatenation, is not the set of all primitive loops and supplies no unrestricted renewal identity or Euler product.

The same reading edition sums the inherited ten-coordinate digit recurrence. For A_k=sum_(0<=v<2^k)L(v), it states A_0=1,A_1=1,A_2=6 and, for k>=3,

```
A_k = 29(3k+1)2^k/72 - (k+3) - 7(-1)^k/9.
```

Hence mean height is asymptotic to (29/24)k on dyadic ranges. Its cutoff algorithm uses O(log N) fixed-dimensional integer-matrix operations; no total bit-complexity claim follows. An average is not a concentration or typical-height theorem. Second moments and distributional limits are separate possible research questions, not completed results.

## Prior sources and reader relevance

[Chung–Graham, Primitive Juggling Sequences](https://fanchung.ucsd.edu/wp/pjs.pdf) supplies state-based primitive-loop decomposition and enumeration; its examples already include (3) and (4,2). [Butler–Graham](https://arxiv.org/abs/0801.2597) develops multiplex enumeration via matrix constraints and recurrences. [Elsner–Klyve–Tou's zeta paper](https://digitalcommons.tacoma.uw.edu/ias_pub/850/) and [Tou's asymptotic counting manuscript](https://faculty.washington.edu/etou/documents/TouE-JugglingPNT.pdf) treat their declared pattern sets and norms. The deliberately restricted prefix sum is different from their unrestricted counts. Classical coding, product natural-boundary arguments and regular-sequence aggregation are credited; a historical novelty audit remains open.

The underlying matching-height Lean audit is historical and source-bound. The later coding, natural-boundary application and aggregate formulas have reported AI hand reviews/algebraic controls, not checked Lean endpoints; separately retained original component review packets are incomplete in the selected archive. No new build, execution, human review or priority audit occurred here. Useful next work is checking the exact graph/coding correspondence, sharpening exposition and assessing an appropriate publication. Further enumeration or height-distribution theorems would be additional work under an agreed funded scope.
