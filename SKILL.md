---
name: ml-paper-writing
description: Draft and revise ML/AI, theoretical computer science, or systems research papers from manuscripts, code and experimental evidence. Use for complete manuscripts, abstracts, introductions, related work, methods, experiments/results, discussion, conclusions, citations and complete reference audits (check-ref), evidence consistency, venue conversion, and creating, restyling, repairing or auditing method overviews, architecture diagrams, pipelines and Fig. 1 concepts with standalone TikZ and mechanical/visual QA. Also supports explicitly requested paper-title-optimizer, GEO/AI-search discoverability, recent citation-growth keyword recommendations and method-name collision checks; these optional workflows never activate from ordinary title polishing or a generic full-skill run.
license: MIT
metadata:
  version: 3.4.0
  author: Orchestra Research; personal workflow revision
---

# ML paper writing

Develop a paper around what the research enables or establishes. Explain the
problem, central idea, evidence and its meaning in the requested language,
preserving the author's decisions and the study's actual scope.

## Select the task and its scope

Determine these from the request and materials, without asking the author to
repeat known information. Task and scope are separate:

| Task | Work to complete |
| --- | --- |
| Draft from research materials | Develop the argument and finish all requested, supported sections. An outline is intermediate unless only planning was requested. |
| Revise an existing manuscript | Diagnose concrete problems, preserve effective passages and author decisions, and revise within scope. |
| Read-only assessment or draft comparison | Locate issues and explain choices without overwriting sources. |
| Figure, format conversion or submission preparation | Follow that artifact's route without expanding to unrelated prose or research. |

**Partial** is the default scope for an unspecified edit: the requested section
and directly affected interfaces. **Full** means a complete draft or
whole-manuscript revision was requested. Read the writing guide and style
conventions completely for full scope, plus relevant section/artifact routes.
For partial scope read only relevant guidance. An abstract revision does not
automatically authorize rewriting the entire paper.

## Workflow activation

Treat this skill as a collection of writing workflows. Full scope means complete
coverage of the requested manuscript, not activation of every optional workflow.
Honor an explicit user exclusion and record the excluded checks.

| Request | Citation coverage | Title/abstract route |
| --- | --- | --- |
| Local edit, section rewrite, ordinary title/abstract polish | New, changed and directly affected references/claim attachments | Normal abstract-and-title guidance only |
| Full draft, whole-manuscript revision, or full skill run | Audit all bibliography entries and every citation occurrence in the final manuscript, without sampling | Normal writing; retrieval optimization stays off |
| Read-only reference audit, including “check-ref” | All entries and occurrences unless the user explicitly limits scope; report only | No title rewrite |
| Explicit “paper-title-optimizer”, GEO/AI-search visibility, query coverage, trend terminology, recent citation-growth keyword recommendations or acronym-collision request | Verify evidence needed for the requested optimization; not automatically a full reference audit | Load the optional title-optimization route, limited to requested capabilities |

Do not load the title-optimization module, its supporting references or probes
for ordinary writing or a generic “full/all” request. It requires specific opt-in.
Full-paper audits use the built-in reference-audit module; no external check-ref
skill is required. Missing manuscript/bibliography material makes coverage
incomplete, not passed. Continue independent work and identify the missing input.

## Core principles

- Organize around one central question and a ranked contribution. Methods,
  analyses, resources, theory and empirical findings need not claim equal
  novelty. Choose a narrative matching the actual research type.
- Preserve objects, assumptions, budgets, units, denominators, uncertainty,
  adverse findings and substantive limitations. Separate proposed designs,
  implemented variants, measured behavior, analytical guarantees and candidate
  explanations.
- Apply the shared writing standard below throughout drafting and revision.
  Build the narrative around the strongest supported contribution; do not turn
  the paper into a work report, experiment diary or self-audit.
- Preserve current author decisions and successful passages. Do not restore
  explicitly deleted rhetoric elsewhere, invent failed attempts or impose
  sentence counts, paragraph recipes or rewrite quotas.
- Keep terminology consistent across prose, equations, algorithms, figures and
  appendix. Numerical agreement alone is not semantic agreement.
- Verify citation identity and specific support. Never fabricate results,
  references, experiments, proof steps, disclosures or resource access.
- Inspect source-control status when a repository exists, protect unrelated
  changes, and preserve a recoverable baseline for substantial edits. Follow
  the manuscript, user and current official venue rules over local defaults.

## Shared writing standard

This standard incorporates **anti-defensive-writing-en** and applies while
writing, revising, cutting and organizing every section, including captions and
appendix prose. It is part of the default writing workflow, not an optional
polishing pass. Its narrative and language rules take precedence over older
guidance or examples elsewhere in this skill. Section guides supply local
craft; [reviewer-guidelines.md](references/reviewer-guidelines.md) supplies
supporting examples and meaning checks. No standalone sibling skill is required.

### Build the story around the strongest supported value

Treat the paper as a press conference: identify its most publishable strength
and build the most favorable, complete and persuasive account the evidence
supports. Do not give every attempted idea, metric or observation equal space.

- Center the genuine advantage: a new capability, problem, mechanism,
  perspective, applicability, cost, efficiency, scalability or meaningful
  trade-off. An empirical distinction or negative finding can itself be the
  contribution. Material with no role in that contribution need not enter the
  main storyline.
- Explain the final standing logic: why the problem matters, where existing
  approaches leave a gap, what this work provides and how the evidence supports
  it. Remove chronological accounts of attempts, failures and editorial audits.
- Choose the task, evaluation dimension, scenario, constraint and comparison
  frame in which the supported value is clearest. Do not make a non-strength
  the paper's headline contest or promise wins on every metric and dataset.
  State under which conditions the advantage holds, what problem it solves and
  why it matters. Explain its cause only when that explanation is supported.
- Let the strongest evidence determine the story. When it cannot support the
  original framing, reconsider the problem, contribution order, headline result
  and experiment structure rather than defending the original plan. Synchronize
  title, abstract, introduction and conclusion within the authorized scope;
  identify broader changes when only a local edit was requested.

### State contributions without self-undermining

Remove authorial self-judgments such as "unfortunately," "merely," "only
achieves," "still lags far behind," "limited improvement" and "severely
insufficient." Avoid verdicts such as "our method is weaker" or "fails to
surpass" that turn a bounded comparison into a judgment on the whole method.
Do not manufacture reviewer objections, volunteer unrelated weaknesses or
complete an opposing argument the paper does not need to answer.

Before discussing unfavorable material, use this decision order:

1. Remove material irrelevant to the core claim.
2. Narrow an overbroad claim to the contribution the evidence supports.
3. Choose an evaluation dimension or scenario that represents that value.
4. Explain differing goals, constraints or a reasonable trade-off when supported.
5. Reorganize experiments so the demonstrated advantage is the narrative and
   visual center.
6. Reframe the paper's story if its current central claim remains unsupported.
7. State an unfavorable result plainly when it materially affects the central
   conclusion and cannot be addressed through accurate framing.

This order governs selection, emphasis and wording. Keep numbers, comparison
conditions and material evidence accurate. A narrower claim must not imply
overall superiority; a selected scenario must be named; a trade-off needs
evidence on both sides. Do not invent an explanation or silently change a
metric, denominator or evaluation protocol. Place necessary qualifications
beside the affected inference and satisfy required limitations/disclosures,
without repeating them as a weakness inventory across the paper. State known
facts directly and attach uncertainty to the specific untested inference.

### Give experiments and sections a persuasive job

Experiments are tools of argument. Each main-text experiment should establish
the claimed outcome, test the key mechanism, demonstrate value in the target
scenario or distinguish a plausible alternative explanation. Move, condense or
remove distracting material; propose redesign only when experiment design is
in scope. Do not run new experiments as part of a writing-only task.

The abstract and introduction should quickly establish the important problem,
the gap, the distinctive approach and the strongest result with its meaning.
Establish the contribution before discussing limitations. Methods explain the
final design, results support the selected claims, and discussion interprets
their value. The conclusion reinforces what was solved, proposed or established
and why it matters; do not end with a fresh self-negation or expanded limitations.

### Check before delivery

Check the requested scope for sentences that expand the paper's obligations,
raise unasked objections, generalize a local observation into a universal flaw,
or use a negative judgment broader than the evidence. Remove work-report
chronology and non-strength headline contests. Confirm that the abstract's
opening establishes both problem and contribution, the advantage is explicit,
and the conclusion closes on the supported takeaway. Use these checks during
drafting as well as final review, not as a new paragraph of disclaimers.

## Working sequence

1. **Establish source and argument.** Read current materials, author decisions
   and result sources. Identify the question, central advance and decisive
   evidence. Use [evidence-workflow.md](references/evidence-workflow.md) for
   multi-source or full-paper work; a sentence edit needs local context only.
2. **Choose the reader's route.** Follow [writing-guide.md](references/writing-guide.md).
   Read the requested section's owner in the route table, including its writing
   procedure and examples; a routing summary alone is not the section guidance.
   Establish paragraph purposes before polishing. Planning can remain internal;
   deliver finished prose when requested and supported.
3. **Draft or revise.** Apply the shared writing standard in every section.
   Complete independent sections despite local gaps elsewhere. Resolve
   conflicts through designated sources; ask concrete
   scientific questions when needed. Keep queries outside paper prose, except
   clear markers in an explicitly unfinished working draft.
4. **Review meaning and expression.** Check the shared writing standard; use
   [reviewer-guidelines.md](references/reviewer-guidelines.md) for supporting
   examples and meaning checks in prose rewrites. Compare with evidence and
   author intent, then synchronize affected artifacts.
5. **Verify and deliver.** Use the delivery audit below. Return the actual draft
   or files and a concise account of material changes, checks and gaps.

## Routes and ownership

| Task | Owner of detail |
| --- | --- |
| Shared narrative and anti-defensive writing, all sections | [Shared writing standard](#shared-writing-standard) above; takes precedence over section-level advice |
| Complete drafting, argument, research types, section writing, discussion | [writing-guide.md](references/writing-guide.md) |
| Title/abstract selection, drafting and compression | [abstract-and-title.md](references/abstract-and-title.md) |
| Introduction logic, closest work, gap and contribution promises | [introduction.md](references/introduction.md) |
| Related work organization, comparison and closest-predecessor attribution | [related-work.md](references/related-work.md) |
| Method explanation, equations, state/information boundaries and theory | [method-writing.md](references/method-writing.md) |
| Experimental setup, main comparisons, ablations and result narration | [experiments-results.md](references/experiments-results.md) |
| Conclusion, supported implications and final promise check | [conclusion.md](references/conclusion.md) |
| Evidence, implementation trace, source updates and bilingual synchronization | [evidence-workflow.md](references/evidence-workflow.md) |
| Scientific review, supporting wording examples, author voice and equivalence | [reviewer-guidelines.md](references/reviewer-guidelines.md), under the shared writing standard |
| Notation, tables, experimental captions, algorithms and punctuation | [style-conventions.md](references/style-conventions.md) |
| Pseudocode package recipes and examples | [algorithms.md](references/algorithms.md) |
| Citation identity, support, attachment and audit routing | [citation-workflow.md](references/citation-workflow.md) |
| Full-paper or explicitly requested existing-reference audit | [reference-audit.md](references/reference-audit.md) |
| Explicitly requested title/abstract retrieval optimization only | [title-optimization.md](references/title-optimization.md); never implicit in full scope |
| Method overview, architecture/pipeline, restyle or figure audit | [figure-workflow.md](references/figure-workflow.md), including construction and independent visual QA |
| Exact venue/year and submission requirements | [checklists.md](references/checklists.md); for STOC 2027, also read [STOC 2027 requirements](references/venues/stoc2027.md) |
| Systems narrative and evaluation | [systems-conferences.md](references/systems-conferences.md) |
| Template setup or conversion | [templates/README.md](templates/README.md) |
| Provenance and source boundaries | [sources.md](references/sources.md) |

Load relevant modules, not the whole library for every task. Method-figure
construction remains self-contained in its existing route. Do not pass a paper
through successive whole-text rewrites by several tools.

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
