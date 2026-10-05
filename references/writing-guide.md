# Narrative and section writing

## Evidence before prose

Read the available manuscript, README, results and experimental settings. For
each material claim, note its evidence location, comparator, budget, metric,
aggregation, uncertainty, and scope. A small working table is enough; reuse an
existing map after checking it. Do not add a separate document unless useful to
the deliverable. Keep measured results, analytic guarantees and proposals distinct.

State the contribution in one sentence: what changes, why that change matters,
and what evidence supports it. For an analysis paper, the contribution may be a
controlled distinction or a counterexample rather than a new algorithm. Do not
force a novelty narrative that the evidence cannot support.

When sources are clear, produce the requested draft and state framing assumptions
with it. When sources conflict, narrow the claim and flag the exact conflict;
ask only for information needed to resolve it. Drafting does not authorize running
new experiments, submitting, or installing external services.

## A short procedure for rewriting

1. Read the requested section, the evidence supporting it, and the corresponding
   section below. For an abstract or conclusion, also inspect the body claims.
2. Extract the facts to keep: contribution, mechanism, comparisons, assumptions,
   units, uncertainty and limitations. Identify missing facts before drafting.
3. Give each paragraph one job; use the chapter pattern to fix missing logical
   links before polishing individual words. Change only the requested scope.
4. Rewrite from those facts. Do not fill empty pattern slots with plausible
   motivation, a theorem, an experiment or a citation. Keep already-clear prose.
5. Compare original and rewrite against the facts. Run the equivalence pass in
   [reviewer-guidelines.md](reviewer-guidelines.md), then the applicable artifact
   checks in [style-conventions.md](style-conventions.md).

The examples below are authored teaching examples, not research results or prose
to insert into a user's paper. Square-bracket fields require verified manuscript
content; they are not citation keys. Unbracketed example facts apply only to that
example. A rewrite is not permission to change the scientific conclusion.
When an original passage overclaims relative to its evidence, report a necessary
narrowing as a substantive correction, not a meaning-preserving rhetorical edit.
Do not introduce new support to rescue it.

## Chapter patterns and examples

Read the requested chapter; a complete draft needs all relevant chapters. These
are defaults, not mandatory sentence counts, page limits or section orders.

### Abstract

**Job:** state the specific contribution, mechanism, evidence and supported
takeaway in a compact passage that can be understood without the paper.

Use five moves when useful: achievement → difficulty/importance → mechanism →
evidence → implication. “We introduce,” “We prove,” or “We find” must match the
actual contribution. Include necessary scope and assumptions adjacent to the
result. Name the baseline and metric when giving a number. A theory abstract
can lead with its result and assumptions; a negative-results paper should lead
with the supported finding rather than invent an improvement.

Avoid a generic field-history opening, acronym lists, contribution inventories,
or a best-case number presented as the overall result. A proposed mechanism is
not a measured achievement. Missing results stay an author-facing gap, not a
fabricated “extensive evaluation.”

**Before:** “Language models have made remarkable progress. We propose X, which
contains A, B and C. Extensive experiments demonstrate its effectiveness.”

**After pattern:** “We introduce X to address [specific failure under stated
conditions]. X [distinctive operation], allowing [supported consequence]. Under
[matched evaluation setting], X [measured result against named comparator].
[Material qualification]. These findings [bounded implication].”

This repairs missing information only when the body supplies it. For an already
sound abstract, reorder existing statements locally instead of filling the
pattern with additional claims.

**Completed teaching example.** Assumed facts: mean-normalized token selection;
matched counts for confidence-ranked and random masks; task differences change
sign; one training run per configuration. These are example premises, not results
for a new manuscript:

> Token selection can change both reward-term membership and normalization. We
> compare confidence-ranked and uniform masks at matched retained counts under
> the same mean normalization. Across the evaluated tasks, their downstream
> differences vary in direction. Each configuration has one training run, so the
> comparisons establish neither superiority nor equivalence. The findings support
> using matched random controls and explicit normalization when interpreting
> confidence-based selection.

The qualifier constrains the result; it is not an apology. This is an analysis
abstract, so it does not manufacture a new algorithm or a remarkable number.

### Introduction

**Job:** make the research question feel necessary and explain why the proposed
answer or analysis is informative.

A useful sequence is: concrete problem and consequence → closest approaches →
specific unresolved boundary → insight → approach overview → qualified evidence
preview → short contribution list. The gap must follow from the preceding work,
not appear as an unsupported “no existing method.” Keep broad field history
short. Explain the mechanism once in plain language before introducing notation.
Put essential motivation and contributions early; page budgets come from the
actual venue rather than a universal 1.5-page rule.

Usually a few contribution bullets suffice. Each names a supported result,
construction, resource or analytical distinction, with assumptions where needed.
“We study” is fine when followed by what the study establishes; “extensive
experiments” alone does not state a contribution. Do not promise benefits the
experiments do not measure.

**Before:** “Previous methods have several limitations. We ask three questions
and propose a novel framework. We conduct comprehensive experiments.”

**After pattern:** “Existing [approach] addresses [problem] through [mechanism],
but the available comparisons also change [confounding factor]. They therefore
leave [specific attribution] unresolved. We hold [control] fixed and vary
[intervention] to test it. The results establish [supported finding], within
[evaluated scope].”

**Contribution example:** replace “We provide extensive experiments” with
“We compare [interventions] under a matched [budget], finding [observed result].”
Replace “We provide theory” with “We prove [statement] under [assumptions].”
Neither pattern licenses inventing the result or theorem.

### Related work

**Job:** place the contribution among approaches addressing the same question
and make the closest methodological distinction inspectable.

Organize paragraphs by signal source, assumption, objective or problem boundary.
For each family: explain the common mechanism, cite verified representatives,
state its relevant boundary, and compare with this paper on the same axis.
Discuss the closest work directly; do not bury it among distant citations.
Distinguish “different from our setting” from “inferior.” Avoid a chronological
author-by-author list unless history itself is the question.

**Before:** “Work A introduced A. Work B proposed B. Work C developed C. Our
method is different from all of them.”

**After pattern:** “[Verified family A] obtains [signal] from [source], while
[verified family B] estimates it using [other source]. X instead uses [its
source]. The closest [verified work] shares [common construction] but differs
in [specific assumption or operation].”

Keep references on the clauses they support. Verify both existence and claim
support using [citation-workflow.md](citation-workflow.md). Group citations only
when they support the same statement. Do not claim priority from an incomplete
search or cite generously merely to flatter potential reviewers.

### Method or system design

**Job:** explain the final mechanism so an expert can reconstruct it.

Start with inputs → distinctive computation → outputs → objective/update. Then
define notation at first use, state assumptions, and present the operations in
dependency order. Before each major equation, say what quantity it defines and
why it is needed; afterwards explain its consequence or role. Explain design
choices through the problem they address, not a diary of discarded versions.

Make scoring targets, normalization denominators, frozen/trainable components,
gradient boundaries and consequential edge cases explicit when applicable.
Give necessary architecture, hyperparameters and reproduction details in the
body or a referenced appendix. A named helper is not a substitute for its
definition. Algorithm formatting belongs to style-conventions/algorithms; method
figure construction belongs to [figure-workflow.md](figure-workflow.md).

**Teaching example facts:** X scores the same sampled tokens under two contexts,
using a frozen model; it subtracts their scores, centers the differences within
the trajectory, and adds the correction to a verified outcome anchor.

**Before:** “We calculate a score and normalize it. Our advantage is given by
Eq. [number]. We then train the model.”

**After:** “A frozen model scores the same sampled tokens under two contexts.
Their score difference defines the token correction. We center the differences
within each trajectory and add them to its verified outcome anchor to obtain
the learning signal.”

The example states data flow; the actual paper must still define the contexts,
score, reduction, degenerate cases and loss. A centered scalar mean does not
by itself establish an unchanged policy gradient or correct causal credit.

### Experiments and results

**Job:** test a stated claim with an interpretable comparison.

For each experiment, give question → control/setup → observed result → bounded
interpretation. Separate the diagnostic quantity from the downstream outcome.
Document matching budgets and uncertainty units; refer to detailed settings
rather than repeat the full recipe in every paragraph. Report mixed results on
the same terms as favorable results.

**Before:** “X performs better, demonstrating the effectiveness of our design.”

**After pattern:** “At fixed [budget], X changes [metric] from [baseline value]
to [X value] on [evaluation scope]. [Other relevant result/uncertainty]. This
supports [tested claim] within [boundary].”

If evidence is only a short memory profile, say “peak memory in this profile,”
not “training efficiency” or “faster training.” If a difference is not resolved
by available uncertainty, it establishes neither equivalence nor superiority.

### Limitations and discussion

**Job:** state which inferences the evidence cannot support and why that matters.

Connect a boundary to its consequence: limited seeds → unresolved training
variability; independent-distribution assumptions → no direct prediction of a
shared-parameter optimizer. Place essential qualifications near the affected
claim and follow the venue's required limitations format. Further experiments
are future work until completed. A caveat is not resolved because it is admitted.

Detailed defensive-writing decisions and contrastive examples have a single
owner: [reviewer-guidelines.md](reviewer-guidelines.md#defensive-writing-examples).

### Conclusion

**Job:** leave the reader with the supported finding and its consequence.

Close the introduction's question: what the work established, what mechanism or
comparison explains it, and what follows within scope. Do not add a new result,
stronger theorem, priority claim or generalization. Avoid replaying a module list
or every benchmark value. Keep a future direction separate from the established
conclusion and tied to a specific unresolved boundary.

**Before:** “We presented X with A, B and C. Experiments prove X is broadly
effective. We will investigate many exciting applications.”

**After pattern:** “Our [analysis/comparison] establishes [supported finding]
under [conditions]. This identifies [bounded consequence for the original
problem]. [Specific unresolved question] is the next evaluation target.”

If the body has mixed results, the conclusion must retain that interpretation.
For instance, “effects vary across the evaluated settings” cannot become “the
method consistently improves performance.”

## Reader expectations

Use Gopen–Swan's useful defaults: keep subject and verb close, supply familiar
context before new information, express action in verbs, and give each paragraph
one function. Put the key inference where the sentence gives it emphasis.

Prefer concrete metrics to “performance,” stable terminology to synonyms, and
short labels to unexplained acronyms. Replace vague pronouns with nouns when
their referent is ambiguous. Delete filler, generic openings and decorative
intensifiers. Active voice often clarifies the actor; passive voice is appropriate
when the operation or object is the subject of interest.

Keep epistemic qualifiers when meaningful. “May,” “preliminary,” and “under these
assumptions” can be essential evidence boundaries. Use “combine” or “extend” when
that accurately describes the contribution; stronger verbs do not create novelty.

## Evidence and reproduction

Report observed baselines and tuning conditions, splits, seeds, hyperparameters,
hardware and compute accounting where available. Label an error bar's meaning
and sampling unit. Distinguish evaluation uncertainty from training-seed variance.
Use paired comparisons when paired observations exist; do not invent confidence
intervals or tests from insufficient summary statistics. Small differences prove
neither superiority nor equivalence by themselves.

For method figures, read [figure-workflow.md](figure-workflow.md). For artifact
checks, use [style-conventions.md](style-conventions.md). For a final small wording
pass, use [reviewer-guidelines.md](reviewer-guidelines.md). Provenance is in
[sources.md](sources.md); this guide makes no claims about reviewer reading rates.
