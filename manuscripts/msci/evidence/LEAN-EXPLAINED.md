# What a Lean proof would mean for this research

Lean is software for writing mathematical statements and proofs in a precise
language. Its proof checker can verify that a particular conclusion follows
from the definitions and assumptions in the checked files. A successful check
is useful evidence about that exact formal statement and its dependencies.

It does not by itself establish that the formal definitions match the
researcher's intended biological model, that the assumptions hold for a
dataset, or that the result is new or useful. Those questions require separate
scientific and literature review.

## What has been checked so far

The existing compiler owner reports a successful Lean check of a restricted
algebraic result: on the stated strict parameter domain, equality of the
nine selected **formula values** implies equality of the model parameters.
The [qualification record](LEAN-ANALYTIC-QUALIFICATION-20261031.md) identifies
the selected sources, assumptions, toolchain and audit limits. An earlier
[two-file check](msci-two-file-qualification.md) covered
an algebraic root-recovery component. These are reports from that owner; they
are not claims that this phone independently reran the checks.

Think of the formula check as verifying a link in an argument: **if these
particular nine mathematical formulas describe the quantities being
compared**, then those values distinguish the admitted parameter vectors. It
does not on its own prove that six sampled lineages and their observed
sequences produce those formulas.

Dot, an AI reviewer, has also read some additional written arguments. For
example, Dot reviewed an argument that swapping the two branches at a point
in a genealogy leaves the stated sequence likelihood unchanged when each
branch keeps its own properties. That is feedback on one part of the
reasoning; it is not a Lean check or an independent human review. The
review record (internal supporting file not included: `subspace-msci-delivery-20261031.md`)
states exactly what Dot received and what remains open.

In later reviews, Dot examined a conditional argument about keeping two
sample lineages separate until the root population and a Lean source draft
that describes the order of recorded mergers. Dot found no mathematical
mismatch within the stated assumptions, but the draft has not been compiled.
Dot also reviewed the next local step for following each recorded merger
through one interval; that feedback is likewise conditional and is not a
computer-checked proof of the full history.
Later drafts try to carry that interval into the same longer record. Dot has
now conditionally reviewed those three drafts without finding a mathematical
mismatch in the stated scope; they have not been checked by Lean. They cover
the first interval, not the entire recorded history.
Since that review, a further source draft has attempted to connect the first
interval to the full record. That new draft has not yet been reviewed or
checked by Lean, and the later parts of the history still need proof.
A separate set of newer drafts tries to follow the recorded mergers through
every interval of the same finite history. Those drafts are also unchecked;
they do not yet establish what happens at the boundaries or connect the
history to the biological observation model.
These are steps toward connecting the formula check to the model, not a
completed proof of that connection. The [timed-genealogy note](TIMED-GENEALOGY-ORIENTATION.md)
explains the assumptions and open steps in more detail.

## What still needs checking

The local source drafts attempt to connect the specified lineage process,
one shared genealogy for both sites, and the sequence observations to the
nine formulas. They also contain candidates for the separate Jacobian and
conditional interval-inclusion arguments. None of those complete chains has
a Lean proof receipt. The feature status (internal supporting file not included: `FEATURE-CHAIN-STATUS.md`) and
readiness record (internal supporting file not included: `LEAN-READINESS.md`) describe the selected drafts and gaps.

The physical interpretation of the instantaneous pulse, the correspondence
between the stated model and its formal representation, and independent
mathematical and biological review remain important even if the code later
checks. Exact identification also does not give a useful sample-size bound for
parameter precision, an implemented estimator, or evidence that the model fits
real organisms. A feature-error bound under stated sampling assumptions does
not automatically give a narrow parameter estimate.

For a complete formal result, the existing compiler owner would need to
select the exact files and dependencies and report which statements were
checked, their assumptions and any axioms or admitted steps. Merely having
source files, a list of dependencies or an AI source review is not that
receipt. No new compiler job or publication follows from this note.
