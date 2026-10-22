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
