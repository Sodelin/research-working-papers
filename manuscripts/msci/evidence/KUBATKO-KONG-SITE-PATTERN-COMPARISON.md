# Related site-pattern identification and network inference

This bounded comparison concerns two published papers found on 1 November
2026. It is not an independent proof review, a comprehensive literature
search, a historical-priority claim or a statement that either method is
implemented in this project.

## Fixed trees and speciation times

Laura Kubatko, Alexander Leonard and Julia Chifman, “[Identifiability of
speciation times under the multispecies coalescent](https://doi.org/10.1016/j.jtbi.2024.111927),”
*Journal of Theoretical Biology* 595, 111927 (2024), report identifiability
of branch lengths on fixed three- and four-taxon species trees and estimators
from site-pattern frequencies. The [PubMed record](https://pubmed.ncbi.nlm.nih.gov/39216590/)
identifies the three authors and publication details. Indexed publisher text
describes a JC69, molecular-clock setting with one sampled lineage per
species, one effective population size across the tree and independent sites.
I inspected the abstract and selected cached introduction and discussion
passages; direct opening of the publisher page returned HTTP 403. I did not
audit the proofs or inspect the publisher PDF or supplements.

This is related sequence-based *tree* identifiability, but it does not by
itself establish the present fixed-pulse model's nine-parameter result. The
present manuscript has a directed pulse, two sampled lineages per species,
multiple population rates subject to stated ties, and two sites sharing a
genealogy. Its selected first- and second-site products are a different
observable from the cited paper's single-site pattern frequencies.

There is a version boundary: an indexed [2020 bioRxiv manuscript](https://doi.org/10.1101/2020.11.24.396424)
with the same title lists Kubatko and Chifman, without Leonard. A searchable
mirror of that earlier manuscript says its analysis assumes the population
size parameter is known. I did not compare its complete bytes or assumptions
with the 2024 article; that earlier wording must not silently be attributed
to the later version. The precise treatment of that parameter in the 2024
proof remains a follow-up source check.

## Sequence-based network estimation

Sungsik Kong, David L. Swofford and Laura S. Kubatko, “[Inference of
Phylogenetic Networks From Sequence Data Using Composite Likelihood](https://doi.org/10.1093/sysbio/syae054),”
*Systematic Biology* 74(1), 53–69 (January 2025 issue; online 10 October
2024), describe PhyNEST. The [publisher's indexed text](https://academic.oup.com/sysbio/article/74/1/53/7817714)
and [PubMed record](https://pubmed.ncbi.nlm.nih.gov/39387633/) describe
quartet site-pattern composite likelihood under JC69 and a constant effective
population size. The method estimates networks from sequence alignments;
the paper evaluates it in simulations and reports performance under a
particular form of substitution-model misspecification. Its described
quartet construction uses one lineage per quartet tip. The indexed method
section assumes coalescent-independent sites while the described inputs
include multilocus alignments; the implications of linkage for a specific
dataset require the paper's full treatment.

This is a practical network-inference method, not a proof that the present
nine features identify the present nine parameters. Quartet *single-site*
pattern counts and a constant population size do not by themselves give the
shared-genealogy two-site joint products or the separate rate ties used here.
The [authors' Julia repository](https://github.com/sungsik-kong/PhyNEST.jl)
is available for future methodological comparison, but its version, code,
performance and suitability for this manuscript were not tested. I read the
publisher's indexed abstract, selected site-pattern and method passages, and
the bibliographic record. Direct opening of the publisher article failed
through the web interface; the full article and code were not independently
inspected.

### Reticulation time and inheritance model

The publisher's indexed introduction describes PhyNEST's **common
inheritance** assumption: lineages reaching a reticulation in one gene follow
the same parent. Its parameterization section reports that the reticulation
age and both parent ages are not all identifiable under that model, and
states that the implemented parameterization sets the reticulation age equal
to the younger parent age. The article points to Supplementary Material S3
for its proof. These are the authors' claims for their specified model, not a
claim about arbitrary coalescent networks.

The authors' [Dryad record](https://doi.org/10.5061/dryad.bg79cnpkm) names a
supplementary PDF on Zenodo. [Zenodo record 13760620](https://doi.org/10.5281/zenodo.13760620)
lists the matching title, authors, date and filename. Its 1,606,866-byte PDF
was retrieved in memory and matched the record's MD5; the received bytes had SHA-256
`fbaa2a6157a88f1ebd73b8643e407f088d26e777ddc05c2163745ce9ffe2a7b5`.
Selected PDF text and in-memory renderings of printed pages 8–9 show S3's
common-inheritance comparison and an argument using two displayed trees whose
expressions do not contain the reticulation-time parameter. The initial
ad-hoc stream extraction did not reliably decode mathematical symbols; a
later reading with the phone's existing PDFium library and visual inspection
of the S3 pages confirmed the relevant text and symbols. In its parenthetical
description of a time-consistent network, S3 prints
`τφ = τ2 = τ3`. On a later, hash-matched in-memory read, S3 was found to
explicitly identify its example with **Figure 1c of the main article** and
to define `τφ` as that example's reticulation age. The main article's indexed
Figure 1 caption identifies `φ` as the reticulation vertex and `τ2`, `τ3` as
the two parent-node ages. For that figure it sets `τφ = τ2`; its
parameterization text describes a “zipped” convention allowing either
`τ2 = τ3` or `τ2 < τ3`. S3 also explicitly considers `τφ` differing from
`τ3` before giving its displayed-tree expressions.

This identifies the shared figure and substantially narrows the notation
question, but it does not explain the authors' use of “time-consistent” in
the S3 parenthesis or establish the exact domain on which the proof and the
implemented convention are intended to agree. The all-equal parenthetical
and the strict-inequality option should therefore both remain visible rather
than being silently treated as the same constraint. I did not visually inspect
the article's Figure 1 or independently audit its displayed-tree proof. Our
comparison has not received independent human review. The metadata checksum
is not a publisher signature.

The present manuscript instead specifies independent routing for each
**current** B block at the pulse, two phased samples per species, potentially
different population rates with stated ties, and a joint two-site observable
sharing one genealogy. When two B blocks are still distinct, a split between
parents has positive conditional probability under this manuscript's interior
`g`, whereas one shared common-inheritance choice sends them to the same
parent. That elementary distinction is recorded in the [inheritance
comparison](PULSE-INHERITANCE-SOURCE-COMPARISON.md); it does not by itself
prove either source's full probability law or settle the relationship between
the two identifiability statements. A precise mapping of model, data and S3's
parameters, and independent mathematical review of both arguments, remain
open. The comparison is not an assertion that this manuscript's theorem is
contradicted or verified.

Both papers broaden context for a prospective collaborator. The exact model
mapping, a comprehensive novelty search, biological validation and independent
mathematical review remain open.
