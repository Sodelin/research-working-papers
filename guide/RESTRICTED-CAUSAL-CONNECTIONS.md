# Restricted intervention targets: an exact-oracle connection

Hou, Park and Li's [September 2026 paper, §7](https://arxiv.org/html/2609.28856v1) asks for efficient inference over all observed variables when only some are intervention targets. Its full-coverage quadratic bound is already prior work. The retained dot (OpenAI) packet gives a narrower population-oracle response: a finite shared-source certificate and decoder, an elementary-query lower bound, and a remaining minimax gap. It does not supply the paper's general finite-sample statistical extension or a biological validation.

## Source and target contract

Write the observed labels as X=T disjoint-union U, k=|T|, u=|U| and n=k+u. Untargeted U variables are still observed. Available interventions are named single-target soft interventions on T. Original sources are finite acyclic graphs with arbitrary finite latent carriers and selection sinks, subject to the packet's context restrictions. Variables are binary valued, and its realization theorem uses positive rational probabilities with one fixed mechanism registry across all regimes. Binary valued does not mean bounded graph degree.

The oracle supplies exact faithful population conditional-independence and conditional-invariance answers, with the manuscript's elementary pair/single-endpoint menu and allowed conditioning sets. One original source and the same named interventions must explain the entire transcript. The [upper certificate](https://github.com/Sodelin/Research-Commons/blob/27b143c73a4ac272b560b2974d83ff96df738531/research/2026-10-22-dot-restricted-causal-interventions/LATENT-SELECTION-IMEC-CERTIFICATE.md) concerns the full source interventional equivalence class and its marked trimmed-combined-MAG image. The image is a class arising from common compatible sources, not a single uniquely recovered DAG, a graph only on T, or freely combined separately realizable graphs.

The explicit query budget is

```
B = k(n-1) + 3 binom(k,2) 2^u + ku 2^u + binom(u,2) 2^(u-2),
2B <= 5n(n-1)2^u.
```

The summation definition in the upper manuscript handles small u without interpreting a zero coefficient times a negative power as a new case. This is a population-query bound, not a bound on samples, experiments, enumeration time or statistical errors. The [finite-realization companion](https://github.com/Sodelin/Research-Commons/blob/27b143c73a4ac272b560b2974d83ff96df738531/research/2026-10-22-dot-restricted-causal-interventions/SELECTION-FINITE-REALIZATION.md) claims a complete registry of at most 2^n 96^binom(n,2) representatives, each with at most n+4 binom(n,2) selection sinks and 9 binom(n,2) latent roots. These compress representatives; they do not restrict original hidden-source size. Finite enumeration is not claimed efficient.

## What the lower bound establishes

For k>0 and u>=2, the elementary-menu hard family has M=binom(u,2)2^(u-2). Its M+1-source promise problem has exact deterministic optimum M. The source also states an expected baseline lower bound (1-2 epsilon)M for arbitrary measurable randomized seeds and per-source error epsilon<1/2. An optimum on that promise family is not an unrestricted minimax equality, and arbitrary binary predicates on full probability laws are a different oracle.

The [23 October lower review/correction](https://github.com/Sodelin/Research-Commons/blob/27b143c73a4ac272b560b2974d83ff96df738531/research/2026-10-22-dot-restricted-causal-interventions/CAUSAL-LOWER-CUMULATIVE-HAND-REVIEW-20261023.md) is essential. At k=0 the literal union of intervention-specific trimmed MAGs is empty for every source. Its class-image target is a singleton and needs zero queries. This does not make observational causal discovery or recovery of the full observational source equivalence class trivial.

The [retained minimax assessment](https://github.com/Sodelin/Research-Commons/blob/27b143c73a4ac272b560b2974d83ff96df738531/research/2026-10-22-dot-restricted-causal-interventions/UNRESTRICTED-MINIMAX-PRIORITIZATION-20261023.md) explicitly reuses Hou–Park–Li's forward-DAG counting argument, checking that distinct skeletons give distinct class-image targets. For deterministic worst-case query complexity Q* of that target it records

```
max{binom(n,2), binom(u,2)2^(u-2)} <= Q*(n,k) <= B,
```

for k>0,u>=2. The inherited quadratic lower bound also applies at u=0,1. Thus bounded u gives Theta(n^2), with constants depending on the bound on u; u>=2 and k=O(u) gives Theta(n^2 2^u), with constants depending on the bound on k/u. A potentially unbounded rate gap remains when u and k/u both grow, for example u=floor(log2 n). A proposed additive upper rate O(n^2+u^2 2^u) is a question, not a theorem. The failed attempt to multiply the old hard family by k is documented: making an exceptional endpoint targetable exposes a distinguishing invariance query.

## Prior work, review and next work

[Zhou and Kocaoglu's ICML 2026 paper](https://proceedings.mlr.press/v306/zhou26s.html) already supplies a theoretically complete enumeration method for its soft-intervention setting with latent confounding, together with additional orientation rules. The retained packet's selection and common-source class-image formulation require a checked representation adapter before any claim that the two targets coincide. No new general completeness principle or priority over that paper follows.

The upper/lower packet has scoped coordinating-AI hand reviews. Later Lean source terms and identifier/API repairs remain unelaborated; no current parser, elaborator, kernel, extracted implementation, human peer review or empirical experiment is asserted. The next useful steps are specialist checking of the target/faithfulness contract and prior-work comparison, a publishable exposition of the exact-oracle result, and separately any funded formalization or statistical extension. Closing the minimax gap would be additional mathematics, not a promised completion date.

Anonymous public raw reads on 3 November 2026 returned HTTP 200 and matched retained local bytes for four selected bodies: upper SHA-256 `23790ebf5e5644dfa243e374729137be20344f86482fd23411a318920b0af95f`; finite realization `33d12a73c30a15e2b2e5ca76a8f78340838389a8c35048c72b7b36534015f5d5`; lower correction/review `0db25787891b163865a53a6c9881b523baab8d90e12e07873c7e9d4b750c777f`; minimax assessment `d2a7a0659a77b18b694595dde081f29148e523dea8d767c1c9fd73f61d465e0a`. Identity checks are not independent mathematical review.
