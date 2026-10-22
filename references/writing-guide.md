# Narrative, complete drafting and section writing

Contents: evidence and research types; whole-paper workflow; rewriting;
abstract/introduction routes; related work; method and theory; experiments;
discussion and limitations; conclusion.

## Evidence before prose

Read the current manuscript or available method, results, figures and author
decisions. Identify what changes, why it matters and what establishes it.
Use [evidence-workflow.md](evidence-workflow.md) for sources, claim mappings and
updates. Do not require a separate ledger for a local edit.

Choose a central contribution and rank the supporting work. Each experiment,
theorem and figure needs an inferential role. A paper can combine several
evidence types without claiming that each is an independent validation of the
same thing.

| Research type | Narrative center and evidence boundary |
| --- | --- |
| Method | Explain the specific difficulty, insight and operation; test the claimed benefit under interpretable comparisons. A module list is not an insight. |
| Theory | State the question, assumptions, result and consequence; keep theorem guarantees separate from empirical optimizer behavior. |
| Empirical analysis or negative result | Establish the distinction, phenomenon, failure condition or counterexample; no new algorithm is needed to make it a contribution. |
| Benchmark, dataset or resource | Explain the research capability, construction and demonstrated uses; dataset size or a working interface alone is not utility evidence. |
| Systems | Connect workload and bottleneck to implementation and measured benefit; use [systems-conferences.md](systems-conferences.md). |
| Survey | Organize verified literature around a synthesis or question. Do not describe a selective review as systematic without a documented search and selection process. |

Mixed papers can use several branches. Match section responsibilities to the
study rather than imposing every section, an independent Discussion or a fixed
figure count.

## From materials to a complete manuscript

When a full draft is requested, infer language, format, current source and
author decisions from context. Without a specified venue, use a sensible
research-paper structure and leave exact venue limits undecided. Do not require
a venue, bilingual version, cover letter or tracked changes unless needed.

### Assess support locally

| State | Action |
| --- | --- |
| Sufficient | Complete the requested sections and linked components. |
| Local gap | Write supported material and identify only the dependent sentence, parameter, citation or component as unresolved. |
| Conflicting sources | Compare object, version and conditions before declaring conflict. Keep the affected claim provisional and continue independent work. |
| Planned results only | Write supported background, implemented methods and a research plan as appropriate. Do not fabricate Results or call it a completed research paper. |

Distinguish extracting a reported number from producing new statistical results.
Retraining, fitting a new model, choosing a new threshold or running a new
experiment is not ordinary writing preparation. Missing hyperparameters cannot
be filled with package defaults.

### Develop and complete the argument

Establish the main question and advance, then connect decisive evidence and
necessary controls. A short outline can support drafting internally. If drafting
was authorized, continue to finished sections rather than requesting permission
to move beyond the outline.

A useful dependency order is results/methods and figure roles, then introduction
and discussion, then title/abstract finalization. This is not a mandatory
chronology: authors may already have a strong introduction. Revisit early
summaries once the core conclusions are stable.

Complete the requested body, captions, appendix material and bibliography
interfaces. The paper explains findings; captions explain how to read panels;
methods explain how results were obtained; appendix preserves needed detail.
Move unique definitions before deleting duplicated supplementary prose.
Mark unfinished draft passages clearly or place queries in an author note.
Unknown disclosures, permissions and access states stay unknown.

Check title, abstract, introduction promises, results, discussion and conclusion
against the same main claim. Do not promote an exploratory variant into the
final method because its result is more favorable. Deliver the supported draft
and exact gaps, distinguishing content completion from file generation, rendering
and submission preparation.

## Revising existing prose

1. Read the requested passage, supporting evidence and relevant section route.
2. Identify what the paragraph contributes and which facts/conditions must stay.
3. Diagnose the actual problem: missing interpretation, broken transition,
   unsupported claim, repeated defense or awkward language.
4. Repair the smallest coherent scope. Preserve successful wording and author
   choices. A structural problem may require more than synonym replacement.
5. Use [reviewer-guidelines.md](reviewer-guidelines.md) for editorial decisions
   and the meaning-equivalence check, then check affected artifacts.

If the original overclaims, report a necessary narrowing as a scientific
correction, not a meaning-preserving style edit. Do not invent support to rescue
it. If there is no material problem, leave the passage unchanged.

## Title, abstract and introduction

Read [abstract-and-title.md](abstract-and-title.md) for selecting information,
explaining the idea, representative evidence and compression. Read
[introduction.md](introduction.md) for the problem-capability-gap-advance
relationship, paragraph continuity and promise checks. These files own the
detailed guidance; their moves are not sentence or paragraph quotas.

## Related work

Read [related-work.md](related-work.md) for source comparison, meaningful
literature groups, closest-predecessor attribution and comparative paragraphs.
The citation workflow owns source verification, while this route owns how
those sources form an intellectual comparison.

## Method, system design and theory

Read [method-writing.md](method-writing.md) for conceptual overview, problem
setup, dependency order, equations, information/gradient boundaries,
reproducibility and formal-result exposition. Use the existing style,
algorithm and figure routes for artifact mechanics. Systems papers also use
[systems-conferences.md](systems-conferences.md).

## Experiments and results

Read [experiments-results.md](experiments-results.md) for evaluation setup,
question-led organization, artifact readouts, main comparisons, ablations,
transfer, efficiency and qualitative analysis. Do not replace this writing
work with a checklist of every experiment a paper might run.

## Discussion: explain what the findings change

Discussion interprets the research rather than repeating Results or enumerating
defects. Start with the main increment in understanding or capability. A method
paper may explain which constraint the construction changes; an analysis what
attribution is now possible; a resource which research tasks become feasible.

For a finding worth discussing, consider:
- The actual observation and evidence type.
- What it adds to the central question.
- An explanation supported by this study or verified literature.
- Alternative explanations that would change interpretation.
- The comparison or measurement that could distinguish those explanations.

Use only the elements the argument needs. Not every significant value needs a
mechanism paragraph, and not every paragraph needs a future experiment.

### Interpret without upgrading evidence

Separate observation, supported interpretation and hypothesis. State established
observations directly, placing uncertainty on the untested link. A feature
attribution explains the fitted model's output, not necessarily the data
generating process. An ablation with retraining is different from a frozen-model
intervention. A theorem about independent variables may illuminate an effect
without proving shared-parameter optimizer behavior.

For mixed results, explain the pattern actually observed. If the effect changes
direction across settings, identify supported commonalities or differences
before proposing a cause. Candidate explanations such as data size or label
noise remain hypotheses unless discriminating evidence was gathered.
Do not replace heterogeneous outcomes with a generic "robust benefit."

Distinguish different observed point estimates from established effect
heterogeneity. Changing signs alone does not establish a task interaction or
reliable task-specific usefulness; describe the observed pattern and separate
the explanation that remains to be tested.

### Compare specific studies

Compare tasks, input information, budgets, model families, measurement levels,
metrics and conclusions as relevant. Explain whether a study supports a
mechanism candidate, provides a contrast or tests the same claim. "Consistent
with previous work" is insufficient without stating what is comparable.
Experiments in another setting cannot substitute for this paper's missing
measurement. Learn structure from supplied reference papers, not their
experimental strength or hypothesis history.

### Make limitations precise and proportionate

Explain what information or design coverage is missing and which inference it
limits. When useful, identify a targeted test that distinguishes plausible
explanations. Do not guess the direction of bias, guarantee that more data will
improve performance, or append a shopping list of experiments to every paragraph.

Few training runs limit the precision of estimated run-to-run variability; one
run cannot estimate that variability. Missing equal-quality curves leave that
efficiency claim unresolved. These are different limitations.
Retain boundaries near affected claims and follow any required venue limitations
section. A caveat is not resolved merely because it has been admitted.
Defensive-writing decisions have one owner:
[reviewer-guidelines.md](reviewer-guidelines.md#defensive-writing-examples).

## Conclusion

Read [conclusion.md](conclusion.md) to select the answer, decisive support and
consequence, preserve current findings and scope, and close the introduction's
promise without a component inventory or a new claim.
