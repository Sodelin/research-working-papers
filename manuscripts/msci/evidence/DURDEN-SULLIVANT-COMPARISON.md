# Prior-work comparison: Durden and Sullivant

## Source and scope of this check

Chris Durden and Seth Sullivant, [*Identifiability of phylogenetic parameters from k-mer data under the coalescent*, arXiv:1705.06993v1](https://arxiv.org/pdf/1705.06993v1), were identified by the retained two-site proof as a predecessor to its root-pair step. On 31 October 2026 UTC, this pass read the arXiv PDF's extracted text for §2, equation (2), §5/Theorem 5.1 and the §6 discussion. The [arXiv record](https://arxiv.org/abs/1705.06993) identifies v1 as submitted 19 May 2017. A later pass also read [arXiv's HTML equation (2) and Theorem 5.1](https://arxiv.org/html/1705.06993v1) and inspected the relevant lines of the [v1 TeX source archive](https://arxiv.org/src/1705.06993v1) in memory. These are representations of the same arXiv source, not independent investigations. PDF page-render requests returned no inspectable image payload through this interface; no visual PDF comparison was performed, and no original PDF bytes were saved or hashed.

The [publisher's record](https://link.springer.com/article/10.1007/s11538-018-0399-1) also identifies the journal article in *Bulletin of Mathematical Biology* 81, 431–451 (2019), DOI `10.1007/s11538-018-0399-1`, with a 1 February 2018 online version-of-record date. Only that record and abstract were read; the published article body was not compared with the preprint. The extracted preprint title page separately displays `September 24, 2018` even though its arXiv watermark and submission history identify v1 with 19 May 2017.

In a later bounded check on 31 October 2026, the publisher's article page again provided a subscription preview, and the publisher PDF address redirected to that preview. Neither exposed the journal's theorem or equations through this interface. No subscription, paywall bypass, article-body comparison or new normalization conclusion followed; the discrepancy discussed below remains specific to arXiv v1.

The retrieved v1 TeX source uses the standard `article` class and `\maketitle`, with no explicit `\date` or `\today` command in its main TeX file. The [LaTeX class documentation](https://raw.githubusercontent.com/latex3/latex2e/main/base/classes.dtx) describes the default date as the processing date, and [arXiv's date FAQ](https://github.com/arXiv/arxiv-docs/blob/develop/source/help/faq/today.md) explains that generated PDFs can be rebuilt later. This is a plausible explanation of the title-page discrepancy, not evidence of the actual build date or environment for this particular PDF; loaded package behavior and original PDF bytes were not authenticated. The arXiv submission history remains the source for the submission date.

The received source archive was 21,131 bytes, SHA-256 `bd25f887baf7f24831eb2a0a54f17bd9f986276b9ddb69868b35878b1447b399`; its main TeX member was 66,580 bytes. The archive and source were read in memory and not retained. This hash identifies the received response, not a signed publisher edition or a previously retained original.

Theorem 5.1 states injectivity for the two-parameter map formed from expected k-mer distances at distinct positive k-mer lengths. Its paper uses a tree/coalescent setting with a shared population-size parameter in its tree construction. This is a prior identification result, not by itself a proof of the manuscript's nine-parameter pulse-family result. The paper's observations are expected k-mer-count distances; the manuscript uses literal phased-site character products. Neither observable is relabelled as the other.

## Root-pair connection for lengths one and two

The following is an algebraic comparison of the paper's equation (2) with the retained proof's root-only pair formulas; it is not an independent proof audit of either theorem. For a fixed known sequence length `m >= 2`, let the paper's transformed divergence parameter be `x`, its positive coalescent parameter be `theta`, and set `c=8/3`. Write

$$
u_h=\frac{x^h}{1+c h\theta},\qquad
z_k=1-\frac{f_k}{2(m-k+1)}.
$$

Expanding equation (2) for `k=1,2` gives

$$
z_1=\frac{1+3u_1}{4},\qquad
z_2=\frac{1+6u_1+9u_2}{16}.
$$

The transformations can therefore be reversed: `u1=(4 z1-1)/3` and `u2=(16 z2-1-6 u1)/9`. Under the identification `x=beta` and `theta=1/R`, they become

$$
u_1=\frac{\beta R}{R+c},\qquad
u_2=\frac{\beta^2 R}{R+2c},
$$

the root-pair moment expressions in the retained identification proof, with `beta=exp(-c T)`. Thus, on these stated conventions, the pair of expected distances and the pair of root moments contain the same two algebraic coordinates. The paper's boundary `x=1` is broader than the manuscript's strict positive-time source domain.

For `k=1,2`, an explicit algebraic reconstruction on the image makes the scope of this comparison concrete. Set `a=c theta` and `q=u2/u1^2`; then `u1>0` and

$$
q=\frac{(1+a)^2}{1+2a}=1+\frac{a^2}{1+2a}>1,
\qquad
a=q-1+\sqrt{q(q-1)},\quad
\theta=\frac{a}{c},\quad x=u_1(1+a).
$$

The other quadratic root for `a` is negative, so the displayed root is unique on `a>0`. In the manuscript's root notation this gives `R=c/a` and `T=-log(x)/c`. This is a hand algebraic reconstruction for exact points in the stated image; it does not establish an implemented inverse, an informative finite-sample bound, or a uniform conditioning guarantee. It matches the structure of the compiler owner's previously reported `rootRatio`/root-time component, but the displayed square-root formula itself has no separate Lean receipt. At `x=1/2`, `theta=3/4`, exact rational arithmetic gives `u1=1/6`, `u2=1/20`, `q=9/5` and recovers `a=2`, `x=1/2`.

## Time and rate conventions for this pair

The extracted preprint's §2 defines its species divergence `t` as the **sum** of the two species-tree paths, and its sequence divergence as `t+2s`, where `s` is an ancestral coalescence wait with rate `1/N`. Its JC generator has diagonal `-mu` and off-diagonal `mu/3`. It then measures time in substitutions and sets `theta=N*mu`, so the ancestral coalescence rate in those units is `1/theta`. These statements are from PDF pages 5 and 7–8, counting from the first PDF page.

For the manuscript's contemporaneous AC pair, let `T=t0` be the root age in its mutation-scaled time and `R=rR` the root pair-merger rate in those units. Under the retained AC pair marginal, the two species paths each have duration `T` and the post-root wait has rate `R`. The preprint's substitution-scaled species-path sum is therefore `t_paper=2T`, and its ancestral parameter is `theta=1/R`. Consequently `x=exp(-4 t_paper/3)=exp(-8T/3)=beta`, while `t_paper+2s=2(T+s)` in the same units. This explains both factors of two in the root-pair formula; `N` is the paper's own inverse-coalescence-rate convention, not an assumed conversion to a diploid census size.

This is a comparison of the stated two-lineage marginal and JC normalization. It relies on the manuscript's retained AC pair marginal rather than independently deriving it from the full six-sample pulse process. It does not identify the different observables or prove that all the models, sampled data or joint laws coincide.

## A normalization discrepancy in arXiv v1

The v1 source's equation (2) has `f_k = 2(m-k+1) g_k` after its own substitutions `y=3x` and `xi=8 theta/3`. Its Theorem 5.1 proof instead writes `g_k = f_k`; its displayed partial derivatives of `g_k` also omit the common factor `4^(-k)`. These are discrepancies between the displayed formulas in that arXiv source, confirmed against its HTML and TeX representations; the journal body was not read, so this observation is not attributed to that edition.

For example, at `m=2`, `k=1`, `x=1/2`, and `theta=3/4`, the formulas give `g_1=5/8` and `f_1=5/2`; the correct `y` and `xi` derivatives of `g_1` are `-1/12` and `1/24`, respectively, while the displayed unscaled sums give `-1/3` and `1/6`. These values were checked with exact rational arithmetic. For the manuscript's `k=1,2`, `m>=2` comparison, each missing coordinate multiplier is positive and invertible, and each missing derivative factor is positive. Thus the correction preserves equality of the two-coordinate fibers and the signs and zero/nonzero status of the corresponding derivatives and determinant. This limited observation does not constitute an independent proof of Theorem 5.1 or of the manuscript's nine-parameter theorem.

## The cited univalence theorem

Durden and Sullivant cite Theorem 7 of Gale and Nikaidô. In the [university-hosted reproduction of the 1965 paper](https://fig.if.usp.br/~marchett/fluidos/jacobian-matrix-global-univalence-mapping_gale-nikaido.pdf#page=11), the extracted text places that theorem explicitly in the **two-dimensional** section: for a continuously differentiable map on a rectangular region, nonvanishing of *all principal minors* gives injectivity. Its statement is stronger than merely requiring a nonzero determinant, and it should not be presented as an automatic nine-dimensional conclusion. The [publisher record](https://doi.org/10.1007/BF01360282) identifies the 1965 journal article; the reproduced PDF was not byte-authenticated against the publisher edition or visually inspected.

The arXiv v1 proof invokes this two-dimensional result for its two-coordinate map and asserts the needed nonvanishing. The positive normalization corrections above do not change that nonvanishing test. I did not independently audit its general `k<l` determinant argument; the explicit `k=1,2` reconstruction above is narrower and separate from the full nine-feature Jacobian and global-identification arguments.

## Remaining work

The paper supports the retained proof's attribution of a two-length root-pair predecessor. Its theorem does not settle the subsequent B/C pulse or AB-onset assembly, establish applicability to the manuscript's biological data, or resolve overall historical priority. A visual PDF equation check, confirmation of the particular PDF's build history, comparison with the journal body, wider prior-work search and independent scientific review remain open. Three exact rational arithmetic spot checks of the displayed substitution passed in the earlier pass, including one boundary value `x=1` outside the manuscript's strict domain; these checks are not a proof of either theorem. No Lean, solver, biological model or source-provider execution was performed.
