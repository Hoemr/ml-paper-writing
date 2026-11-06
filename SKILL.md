---
name: ml-paper-writing
description: Draft, revise and audit ML/AI, theoretical computer science and systems papers from manuscripts, code and evidence. Supports section writing, complete reference audits (check-ref), venue conversion and TikZ method figures with mechanical and independent visual QA. Title retrieval optimization and citation-growth recommendations require explicit requests.
license: MIT base; CC BY 4.0 adapted Best-Paper material (see NOTICE)
metadata:
  version: 3.6.0
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

Full manuscript scope includes every bibliography entry and citation occurrence;
partial edits check new, changed and directly affected references. The optional
title-optimization route requires specific opt-in, including in a generic full
skill run. See [workflow activation](references/writing-guide.md#workflow-activation)
for coverage, exclusions and missing-input handling.

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

Read [reviewer-guidelines.md](references/reviewer-guidelines.md#shared-writing-standard)
for every prose drafting or revision task. It owns the strength-centered narrative,
treatment of unfavorable evidence and meaning-equivalence checks, and takes
precedence over section examples. Preserve its standards when moving guidance.

## Working sequence

1. **Establish source and argument.** Read current materials, author decisions
   and result sources. Identify the question, central advance and decisive
   evidence. Use [evidence-workflow.md](references/evidence-workflow.md) for
   multi-source or full-paper work; a sentence edit needs local context only.
2. **Choose the reader's route.** Follow [writing-guide.md](references/writing-guide.md).
   Read the requested section's owner in the route table, including its writing
   procedure and examples; a routing summary alone is not the section guidance.
   Use the integrated argument-design route for substantial drafting; connect
   paragraph purposes and evidence before polishing. Planning can remain internal;
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
| Shared narrative and anti-defensive writing, all sections | [reviewer-guidelines.md](references/reviewer-guidelines.md#shared-writing-standard); takes precedence over section-level advice |
| Argument design, contribution routes and calibrated claims | [narrative-design.md](references/narrative-design.md), [research-routes.md](references/research-routes.md), [claim-calibration.md](references/claim-calibration.md) |
| Optional award-paper exemplars and corpus-relative metrics | [bestpaper/README.md](references/bestpaper/README.md); descriptive aids, not universal gates |
| Complete drafting, argument, research types, section writing, discussion | [writing-guide.md](references/writing-guide.md) |
| Title/abstract selection, drafting and compression | [abstract-and-title.md](references/abstract-and-title.md); for theory-paper title wording, also use [theory-title guidance](references/theory-title-guidance.md) |
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

## Quality gates and delivery

Check scientific meaning, the shared writing standard, section quality,
cross-component agreement, citation identity/support and affected layout. For
full-paper work use the [delivery audit](references/evidence-workflow.md#quality-gates-and-delivery-audit);
small edits need a short verification note. Missing material means incomplete
coverage. Report unperformed checks and precise unresolved assumptions.

Method figures require standalone source, PDF/PNG, a design contract, no unresolved
HARD findings, warning triage and independent visual evidence under the figure route.
Use fresh-context prose review when available and permitted; otherwise name the
separate self-review accurately. Complete requested corrections, then stop. Writing
does not authorize new experiments, retraining, submission, upload or correspondence.
