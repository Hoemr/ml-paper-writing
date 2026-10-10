---
name: ml-paper-writing
description: Draft, revise, and prepare ML/AI or systems research papers from manuscripts, code, and experimental evidence. Use for contribution framing, scientific prose, citations, method-figure planning, or venue conversion; route TikZ construction and figure QA to ml-method-figure.
license: MIT
metadata:
  version: 2.2.1
  author: Orchestra Research; personal workflow revision
---

# ML paper writing

Turn a supported contribution into a paper a reader can understand and assess.
Work within the requested manuscript and deliverable; proceed from clear source
material and state reversible assumptions. Ask only when missing or conflicting
evidence would materially change the scientific claim.

## Modes

Two entry modes; **partial is the default**. Switch to full mode only when the
user asks for whole-manuscript revision or polishing — "full pass", "润色整篇
论文", "全面修改" or equivalent. When the phrasing is ambiguous, default to
partial and state which mode was chosen.

- **Partial.** The shortest workflow below. Touch only the requested scope and
  read only the routes that task needs. The delivery audit covers exactly the
  changed units.
- **Full.** Whole-manuscript revision and polish. Before editing, read
  [writing-guide.md](references/writing-guide.md) and
  [style-conventions.md](references/style-conventions.md) completely, plus
  every route the manuscript's artifacts need. Revise chapter by chapter
  against the chapter patterns. The delivery audit covers every section,
  table, algorithm block, symbol, and citation point in the manuscript, not
  only changed units.

## Core principles

- One central contribution, with an explicit problem, mechanism, evidence, and
  consequence. Each experiment and figure has a distinct inferential job.
- Frame a method paper around its supported methodological contribution. Give
  readers the specific problem and difficulty before unexplained method names;
  keep experiment-status commentary out of the abstract. Scope each reported
  result accurately without turning contribution prose into a caveat inventory.
- Preserve scientific meaning: assumptions, comparison budgets, denominators,
  uncertainty, adverse results, and substantive limitations. Distinguish proposed
  designs, evaluated variants, analytical models, and measured behavior.
- Never invent results or citations. Verify identity and claim support through
  the citation workflow; flag unresolved support without fabricating a cite key.
- Keep terminology consistent across prose, equations, algorithms, and artwork.
  Local conventions are defaults; the manuscript, user, and official venue rules
  determine the required format.
- Use semicolons and explanatory dashes sparingly. Apply the punctuation
  guidance in style-conventions to prose, captions, and appendix text.
- Inspect git status before editing; protect unrelated changes and read-only
  reference material. Edit the smallest coherent set of files.

## Shortest workflow (partial mode)

1. Read the README, method, results, existing figure sources and design notes.
   Record the supported contribution and a compact claim–evidence map.
2. Choose the route below. Draft or revise from that evidence, marking assumptions
   and missing support. Do not require approval for routine wording choices.
   For prose rewriting, read writing-guide's rewrite procedure and the requested
   section before editing; use reviewer-guidelines for defensive wording. Read
   the references themselves, not only their descriptions in the route table.
3. For method figures: paper narrative → design contract → TikZ by construction
   → mechanical QA → independent visual review. See the figure route; do not
   maintain a second copy of its mechanical rules here.
4. Run the delivery audit below, compile affected LaTeX, inspect final-size
   renders, and deliver changed paths, the audit table, verification results,
   unresolved assumptions, and any failure causes.

## Routes (read only what this task needs)

| Task | Single owner of detail |
| --- | --- |
| Framing, chapter patterns, full draft, or rewrite examples | [writing-guide.md](references/writing-guide.md) |
| Notation, references, tables, algorithms, prose checks | [style-conventions.md](references/style-conventions.md) |
| Pseudocode package recipes and worked examples | [algorithms.md](references/algorithms.md); rules remain in style-conventions |
| New citations or claim support | [citation-workflow.md](references/citation-workflow.md) |
| Method overview or diagram revision | [figure-workflow.md](references/figure-workflow.md), then `$ml-method-figure` |
| Defensive wording examples or final equivalence review | [reviewer-guidelines.md](references/reviewer-guidelines.md) |
| Submission requirements, exact venue/year | [checklists.md](references/checklists.md) |
| Systems narrative and evaluation | [systems-conferences.md](references/systems-conferences.md) |
| Template setup or format conversion | [templates/README.md](templates/README.md) |
| Guidance provenance or external-source limits | [sources.md](references/sources.md) |

## Quality gates

- Every material claim resolves to evidence or a clearly identified open question.
  No rewrite upgrades certainty, novelty, efficiency, or causal interpretation.
- Added references have verified metadata and support the attributed claim.
- Relevant compilation succeeds; no new unresolved citations/references or
  overfull content. Document pre-existing warnings separately.
- Inspect rendered appendix pages as well as the main text. A clean compile does
  not rule out overlapping columns, line numbers, displays, or unreadable glyphs.
- Review punctuation in context. Avoid repeated semicolon chains and dash
  parentheticals without changing claims, qualifiers, or citation scope.
- Method-figure delivery includes editable standalone source, PDF, PNG, a design
  contract, no unresolved HARD findings, warning triage, and independent visual
  evidence. QA alone does not establish semantic correctness or publication readiness.
- Report actual coverage and failures. Publication and submission remain separate
  actions from preparing a reviewable draft.

These gates are the rows of the delivery audit table. A gate left unchecked is
reported as unchecked, never as passed.

## Delivery audit

Mandatory before reporting completion, in both modes; the audited scope follows
the mode. Rules read early in a long session decay, so every gate is re-checked
at delivery time against an explicit list — this is what turns silent omissions
into visible ones.

1. **Enumerate** the audited units in a numbered list: changed
   sections/paragraphs, tables, algorithm blocks, symbols defined or renamed,
   and new citation points. In full mode enumerate the entire manuscript.
2. **Lint mechanically.** Run
   `python3 scripts/lint_style.py <changed .tex files> [--bib refs.bib] [--log main.log]`
   and triage every finding: fix it, or state why it stands. An untriaged
   finding is an unfinished defect. Coverage is exactly the analyzed files.
3. **Review judgments with fresh eyes.** Gates that need reading comprehension
   — over-claiming, defensive writing, background structure, chapter patterns
   — go to a fresh-context reviewer: a subagent given only the relevant rule
   files plus the audited text, never this conversation, reporting violations
   rather than rewrites. Required in full mode and after any prose rewrite in
   partial mode; a spot edit needs only steps 1, 2 and 4.
4. **Deliver the audit table** with changed paths, verification results,
   unresolved assumptions, and failure causes:

   | Gate | Items checked | Violations | Resolution |
   | --- | --- | --- | --- |

   One row per quality gate above plus one row for lint findings. A gate with
   no row counts as not checked; report actual coverage, never "all clean"
   without the rows behind it.
