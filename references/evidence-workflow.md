# Evidence, source changes and manuscript consistency

Use for complete manuscripts, several source files, changing experiment
versions, figure renumbering or requested bilingual synchronization. A local
sentence edit needs only the sentence, context and its source. Reuse existing
records; do not impose a project database on ordinary writing.

## Establish the current source

Identify the author-designated manuscript and result versions. Preserve a
baseline for substantial changes. Current author decisions supersede earlier
editorial preferences within their scope. An author decision does not turn an
unsupported numerical or scientific claim into verified evidence; flag the
specific conflict without silently substituting another version.

Distinguish author-provided, actually checked, unresolved, conflicting and
superseded information. A file inventory is not a content review. State what
was read and which claims were checked, without re-opening unrelated settled work.

## Smallest useful claim map

Use existing labels or short stable IDs when several artifacts need linking.
Printed figure numbers and paragraph positions can change; scientific identity
should remain traceable. Most IDs belong in working records, not paper prose.

| Field | Record when relevant |
| --- | --- |
| Claim and role | Central advance, supporting finding, diagnostic, theoretical result or future proposal. |
| Evidence identity | Implemented variant, model/checkpoint, dataset version, split, task, source table/cell or saved output. |
| Comparison | Baseline, input information, training/tuning budget, hardware and measurement boundary. |
| Quantity | Metric, units, denominator, aggregation, uncertainty method and sampling unit. |
| Method | Formula, pseudocode, executed implementation/configuration and relevant assumptions. |
| Presentation | Abstract/body, equation, table, figure/panel, caption, appendix and requested translation. |
| External support | Exact literature claim and read passage, separately from this paper's measured result. |
| Status/query | What is checked, what is author-provided, what conflicts, and the smallest missing fact. |

Add **strongest supported wording**, **necessary scope**, and **evidence role**
(headline / supporting / table-only) to this same map when drafting or revising
substantial claims; use [claim-calibration.md](claim-calibration.md). Link each
claim to the relevant method subsection, proof or construction and the available
experiment/table/figure/control. Relationships can be many-to-many; a theorem
needs no invented experiment and a component needs no ceremonial ablation.
Keep one record, not separate claim-map and evidence-map files.

A theoretical claim maps to statement, assumptions and proof rather than
invented empirical fields. A resource maps to construction, coverage, access
state and demonstrated uses. Omit irrelevant columns.

## Trace methods to execution when needed

If a method description disagrees with a result summary, inspect the relevant
executed call, configuration and saved output. Do not read the entire repository
for a local ambiguity. Check input qualification, selection, thresholds, ties,
normalization, missing cases and repeated-run aggregation as the gap requires.
An installed package, function definition or unused branch is not evidence that
it generated the result.

Preserve distinctions between independent runs, evaluation examples, tasks,
tokens and repeated computations on one model. Zero, missing, failed, not
executed and below-threshold are different states. Keep separate denominators
when they describe different populations. Do not force numerical uniformity
across legitimate subsets.

Arithmetic consistency checks on already reported values can support writing.
New inference, refitting, reselecting thresholds or training needs separate scope.

## Update only actual dependencies

Classify the change:
- Expression: check meaning, quotation/citation attachment and affected layout.
- Organization: update figure/equation labels, paragraph maps and appendix entry
  points; preserve scientific identities and unique moved definitions.
- Fact/source: trace every claim using the changed method, value, model variant,
  population, comparison or availability state.

For a source change, inspect the affected title/abstract, introduction promises,
results, discussion, conclusion, tables/figures, captions, algorithms, appendix
and any requested submission text. Reopen dependent checks, not the whole
manuscript indiscriminately. Do not inherit a previous pass for changed content.

Record a short source → affected locations → changes → remaining query list.
Keep the old source and replacement relationship. Do not choose the more
positive or convenient result as the authority.

For example, if a method version starts normalizing over retained tokens instead
of all sampled tokens, unchanged numeric tables do not establish the same
method. Check equations, algorithm steps, loss description, experiment identity,
captions and summary claims before associating the results with the new variant.

## Figures, appendix and languages

Maintain old → new display labels when figures move, with panel membership and
affected references. A complete figure is its full panel set, not a file name.
Captions, source data and methods must describe the quantity actually drawn.
Main-text/appendix moves preserve unique definitions and needed controls.

Only synchronize languages when requested. Neither language is automatically
authoritative if both have new author edits. Pair by scientific function rather
than sentence count. Preserve objects, quantifiers, negation, conditions, time,
endpoint, effect scale, proposed/measured identity and citation role.
Allow natural differences in syntax. Identical digits do not prove agreement.

## Resume and completion

For work spanning sessions, save a brief state only if useful: current source,
author decisions, completed components, pending queries, affected dependencies
and actual verification coverage. Reuse existing project records. Do not create
parallel state files merely to follow a template.

Content completion, file generation, compilation, rendered-page review,
independent review and submission readiness are separate facts. Report them
separately. Leave precise unresolved queries with affected locations and continue
independent writing. Never fabricate an approval number, public URL or missing
result to make the package look complete.

## Quality gates and delivery audit

Audit the requested scope plus directly affected interfaces. Maintain a compact
list of checked sections, tables, algorithms, symbols and citation points.
Full scope covers the whole requested manuscript.

| Gate | Check when applicable |
| --- | --- |
| Argument and scientific meaning | Explain the contribution; each material claim has evidence or an explicit query. Do not upgrade novelty, certainty, causality, efficiency or generality. |
| Shared writing standard | The strongest supported value organizes the requested scope; no experiment diary, volunteered irrelevant weaknesses, inflated obligations or new concluding self-negation. Necessary evidence and claim conditions remain accurate. |
| Section quality and voice | Abstract selects evidence; introduction earns the gap; related work locates the advance; method explains it; experiments answer claims; discussion interprets; conclusion closes the promise. Retain necessary boundaries without repetitive defenses. |
| Cross-component consistency | Changed claims agree with methods, equations, algorithms, figures, captions, tables, appendix and requested languages. |
| Citations | Verify new/affected references and claim attachment for partial scope. Full scope audits every bibliography entry and citation occurrence with separate identity and support results; disclose incomplete coverage. |
| Source and layout | Compile affected LaTeX without new unresolved citations/references or overflow; inspect final-size renders including affected appendix pages. |
| Method figures | Editable standalone source, PDF/PNG, design contract, no unresolved HARD findings, warning triage and independent visual evidence, per the figure route. |
| Mechanical style findings | For edited LaTeX run `python3 scripts/lint_style.py <files> [--bib refs.bib] [--log main.log]`; triage lexical flags in context. |

For a full manuscript or a prose rewrite, obtain fresh-context review when
delegation is available and permitted: supply relevant rules, text and necessary
evidence, not prior editorial conclusions. The reviewer reports violations rather
than rewriting. Otherwise perform a separate self-review and name it accurately.
A spot correction needs local checks; method figures retain their dedicated
independent visual-review requirement.

Keep a gate record with coverage, findings and resolutions. Deliver a compact
audit table for full-paper work; a short verification note suffices for a small
edit. Mark irrelevant checks not applicable and unavailable checks not performed.
Plain-text writing does not require a manufactured LaTeX build. Do not call an
unfinished draft submission-ready or claim unperformed verification.

Stop when the requested components and necessary corrections are complete.
Writing does not authorize new experiments, retraining, new statistical analyses,
submission, public upload or correspondence; these need their own task scope.
