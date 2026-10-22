---
name: ml-paper-writing
description: Draft and revise ML/AI or systems research papers from manuscripts, code and experimental evidence. Use for complete manuscripts, abstracts, introductions, related work, methods, experiments/results, discussion, conclusions, citations, evidence consistency, venue conversion, and creating, restyling, repairing or auditing method overviews, architecture diagrams, pipelines and Fig. 1 concepts with standalone TikZ and mechanical/visual QA.
license: MIT
metadata:
  version: 3.1.0
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

## Core principles

- Organize around one central question and a ranked contribution. Methods,
  analyses, resources, theory and empirical findings need not claim equal
  novelty. Choose a narrative matching the actual research type.
- Preserve objects, assumptions, budgets, units, denominators, uncertainty,
  adverse findings and substantive limitations. Separate proposed designs,
  implemented variants, measured behavior, analytical guarantees and candidate
  explanations.
- Explain the contribution directly. Remove repeated self-defense and editorial
  logs while retaining conditions that change interpretation. Use precise
  definitions rather than a stream of disclaimers.
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
3. **Draft or revise.** Complete independent sections despite local gaps
   elsewhere. Resolve conflicts through designated sources; ask concrete
   scientific questions when needed. Keep queries outside paper prose, except
   clear markers in an explicitly unfinished working draft.
4. **Review meaning and expression.** Read
   [reviewer-guidelines.md](references/reviewer-guidelines.md) for prose rewrites.
   Compare with evidence and author intent, then synchronize affected artifacts.
5. **Verify and deliver.** Use the delivery audit below. Return the actual draft
   or files and a concise account of material changes, checks and gaps.

## Routes and ownership

| Task | Owner of detail |
| --- | --- |
| Complete drafting, argument, research types, section writing, discussion | [writing-guide.md](references/writing-guide.md) |
| Title/abstract selection, drafting and compression | [abstract-and-title.md](references/abstract-and-title.md) |
| Introduction logic, closest work, gap and contribution promises | [introduction.md](references/introduction.md) |
| Related work organization, comparison and closest-predecessor attribution | [related-work.md](references/related-work.md) |
| Method explanation, equations, state/information boundaries and theory | [method-writing.md](references/method-writing.md) |
| Experimental setup, main comparisons, ablations and result narration | [experiments-results.md](references/experiments-results.md) |
| Conclusion, supported implications and final promise check | [conclusion.md](references/conclusion.md) |
| Evidence, implementation trace, source updates and bilingual synchronization | [evidence-workflow.md](references/evidence-workflow.md) |
| Scientific review, defensive wording, author voice and equivalence | [reviewer-guidelines.md](references/reviewer-guidelines.md) |
| Notation, tables, experimental captions, algorithms and punctuation | [style-conventions.md](references/style-conventions.md) |
| Pseudocode package recipes and examples | [algorithms.md](references/algorithms.md) |
| Citation identity, support and attachment | [citation-workflow.md](references/citation-workflow.md) |
| Method overview, architecture/pipeline, restyle or figure audit | [figure-workflow.md](references/figure-workflow.md), including construction and independent visual QA |
| Exact venue/year and submission requirements | [checklists.md](references/checklists.md) |
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
| Section quality and voice | Abstract selects evidence; introduction earns the gap; related work locates the advance; method explains it; experiments answer claims; discussion interprets; conclusion closes the promise. Retain necessary boundaries without repetitive defenses. |
| Cross-component consistency | Changed claims agree with methods, equations, algorithms, figures, captions, tables, appendix and requested languages. |
| Citations | Verify added references and their support; preserve claim attachment during editing. |
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
