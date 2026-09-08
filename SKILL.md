---
name: ml-paper-writing
description: Write publication-ready ML/AI/Systems papers for NeurIPS, ICML, ICLR, ACL, AAAI, COLM, OSDI, NSDI, ASPLOS, SOSP. Use when drafting papers from research repos, structuring arguments, verifying citations, revising LaTeX manuscripts, converting venue formats, or preparing camera-ready submissions.
license: MIT
---

# ML Paper Writing for Top AI and Systems Conferences

Write papers as an evidence-grounded collaborator. Build the scientific story from the repository, results, and author-provided claims; do not invent missing evidence, citations, experiments, or implementation details.

## Provenance

This customized skill is derived from the open-source `ml-paper-writing` skill in [Orchestra Research's AI Research Skills library](https://github.com/Orchestra-Research/AI-Research-SKILLs). It retains the upstream MIT License and extends the original with a slimmer progressive-disclosure structure, stricter evidence and delivery gates, and customized notation and equation-formatting rules.

## Operating Contract

- Treat the author as the owner of the scientific claims and the agent as an active writing and engineering collaborator.
- Inspect the available evidence before drafting. Distinguish demonstrated results, planned experiments, hypotheses, and unknowns.
- Preserve technically meaningful caveats. Improve clarity without silently strengthening claims.
- Never fabricate citations, BibTeX, metrics, ablations, baselines, hyperparameters, or venue requirements.
- **Do not proactively call citation APIs, fetch BibTeX, or run reference audits.** Verification is on-demand: only when the user explicitly asks to verify, search, or audit citations. Writing or revising a section does not trigger a citation check.
- Verify current venue rules from official sources because page limits, disclosure policies, and templates change.
- Keep repository paths, run IDs, internal task names, and code-facing identifiers out of manuscript prose.
- Compile and inspect deliverable LaTeX rather than stopping after source edits.

## Progressive Disclosure

Load only the references needed for the current task:

| Need | Read |
|---|---|
| Narrative, abstract, introduction, sentence clarity, mathematical writing | [references/writing-guide.md](references/writing-guide.md) |
| Per-section paragraph role templates (Abstract, Intro, Related Work, Conclusion) | [references/module-writing-guide.md](references/module-writing-guide.md) |
| Cross-cutting tone rules, banned openings, claim-evidence discipline, pre-delivery gate | [references/writing-style.md](references/writing-style.md) |
| Kaiming He exemplar overlay (observation-first, two core designs, minimal related work) | [references/styles/kaiming-he-style.md](references/styles/kaiming-he-style.md) |
| Citation search, BibTeX retrieval, and read-only audit of existing `.bib` / citation points | [references/citation-workflow.md](references/citation-workflow.md) |
| Rebuttal phase: dispatch to the rebuttal skill with project-level MUST overlays | [references/rebuttal-guideline.md](references/rebuttal-guideline.md) |
| Venue checklists and submission requirements | [references/checklists.md](references/checklists.md) |
| Reviewer criteria, rebuttals, review simulation | [references/reviewer-guidelines.md](references/reviewer-guidelines.md) |
| OSDI, NSDI, ASPLOS, SOSP specifics and conversions | [references/systems-conferences.md](references/systems-conferences.md) |
| Primary writing and venue sources | [references/sources.md](references/sources.md) |
| Bundled LaTeX snapshots | [templates/README.md](templates/README.md) |

Do not load every reference by default. The main skill contains the stable workflow; references contain detailed or venue-specific material.

## Repository Intake

When starting from a research repository:

1. Inspect repository guidance and state.
   - Read `README*`, `AGENTS.md`, `CLAUDE.md`, existing paper drafts, and experiment documentation.
   - Check `git status` before editing; preserve unrelated user changes.
2. Map the research surface.
   - Locate training, evaluation, configuration, result, plotting, and manuscript files.
   - Prefer `rg` and structured parsers over broad manual browsing.
3. Build an evidence inventory.
   - Record the problem, method, baselines, datasets, metrics, seeds, uncertainty, compute, and limitations.
   - Trace headline numbers to raw outputs or authoritative tables.
4. Build a claim-evidence map.
   - For each intended claim, identify its supporting theorem, experiment, citation, or author statement.
   - Mark unsupported claims as hypotheses or TODOs; do not smooth over the gap.
5. Confirm the intended venue and submission stage.
   - Draft, anonymous submission, rebuttal, revision, and camera-ready work have different constraints.

Repository facts are source material, not reader-facing language. Translate implementation details into scientific descriptions.

## Collaboration

Be proactive when evidence is available:

- Draft complete sections and make scoped LaTeX edits.
- Surface contradictions, missing controls, unclear assumptions, and overclaims early.
- Use explicit placeholders only when necessary, with a precise description of the missing evidence.
- Ask focused questions when a decision changes the paper's central claim, experimental interpretation, or venue compliance.
- Do not repeatedly ask for details that can be discovered from the repository.

For a new or structurally weak paper, agree on the central narrative before polishing sentences. For an established draft, preserve its architecture unless restructuring has a clear scientific payoff.

## Narrative Before Prose

Define the paper in five moves:

1. **Problem**: What concrete technical problem matters?
2. **Gap**: Why do existing approaches or explanations remain insufficient?
3. **Controlled question**: What exact hypothesis or comparison does the paper isolate?
4. **Answer**: What principle, method, or empirical finding resolves that question?
5. **Evidence and boundary**: What supports the answer, and what does it not establish?

Use one stable term per concept. State the strongest defensible claim, not the most dramatic one.

### Custom Narrative Defaults

- Start from the actual controlled comparison rather than a broad field-level slogan.
- Separate optimization efficiency, semantic importance, causal importance, and downstream performance unless evidence connects them.
- Treat matched controls and random baselines as part of the claim, not as incidental implementation details.
- Explain the practical consequence of each theorem or empirical result in plain language.
- Keep the introduction light on notation and derivations.

## End-to-End Workflow

### 1. Establish the Contribution

Write a one-paragraph internal brief containing:

- the problem and why it matters;
- the precise gap;
- the proposed idea or diagnostic;
- the strongest evidence;
- the principal limitation.

Reject contribution statements that merely say the method is "novel," "effective," or "simple." Name the mechanism and measurable consequence.

### 2. Build the Paper Skeleton

Create section headings and one-sentence goals before drafting:

- Abstract
- Introduction
- Background or Problem Formulation
- Method or Theory
- Experiments
- Related Work
- Limitations or Discussion
- Conclusion
- Appendix

Adapt the structure to the venue and paper type. Systems papers usually need explicit design, implementation, and operational evaluation sections; theory-heavy papers need assumptions and proof organization.

Use the heading hierarchy to expose the argument:

- Keep section and subsection titles short and use established field terminology.
- Make subsections carry the section's main line. A reader who scans only the subsection titles should recover the section's logical progression.
- Put supporting analyses, implementation details, corollaries, controls, and side discussions in `\subsubsection{...}` or ordinary paragraphs under the relevant main-line subsection.
- Avoid creating a subsection for every local topic. Merge closely coupled theory and intervention material when they answer one research question.
- Avoid a section with only one redundant subsection; write the section opening directly when no additional hierarchy is needed.

### 3. Draft Abstract and Introduction

The abstract should usually contain:

1. problem;
2. limitation of prior understanding;
3. approach or principle;
4. key quantitative or theoretical result;
5. implication and scope.

The introduction should let a reviewer recover the complete story without reading the methods. Front-load the controlled question, contribution, evidence, and limitation. Use contribution bullets only when they improve scanability and make each bullet independently verifiable.

### 4. Write Methods and Theory

- Define the setting, data, policy or model, objective, and assumptions before derivations.
- Keep Problem Formulation focused on objects, notation, assumptions, and objectives. Move newly derived claims and analysis results to a Theory, Analysis, or Method section.
- Separate definitions, propositions, proofs, and empirical hypotheses.
- Use a lemma for a technical result that serves as a step toward a main theorem.
- Omit optional theorem names by default. Add one only when a short, standard name helps navigation; use explanatory prose before or after the result instead of a sentence-length theorem title.
- Give every theorem or proposition a plain-language interpretation.
- State what a local, asymptotic, output-space, or idealized result does not imply about finite training.
- Keep proof details in the appendix when the main text only needs the result and intuition.
- Align symbols with implementation concepts without exposing repository-local names.

### 5. Write Experiments Around Questions

Each experiment should answer one explicit question:

- **Question**: What claim is tested?
- **Design**: What varies, what is held fixed, and why is the comparison fair?
- **Metric**: What observable supports or refutes the claim?
- **Result**: What happened, including uncertainty and negative results?
- **Interpretation**: What conclusion is justified?

Report seeds, dispersion or confidence intervals, dataset splits, model selection, hyperparameters, compute, and evaluation procedures when relevant. Distinguish exploratory pilots from confirmatory evaluations. Never promote a small point estimate into a robust claim without uncertainty evidence.

### 6. Write Related Work as Comparison

Organize by technical relationship, not by paper chronology. For each cluster, explain:

- the shared problem;
- the mechanism used by prior work;
- the closest overlap;
- the exact distinction from this paper.

Keep every citation adjacent to the claim it supports. Do not use citation piles as a substitute for explaining differences.

### 7. Write Limitations and Conclusion

Limitations should identify the boundary of the evidence, missing controls, scale or domain restrictions, and assumptions that may fail. The conclusion should answer the controlled question and restate the supported implication without introducing new claims.

### 8. Run the Delivery Gate

Before delivery:

- compile from a clean or reproducible build path;
- resolve undefined references, citations, labels, and control sequences;
- inspect page count, float placement, table readability, and overfull boxes;
- verify headline numbers against authoritative results;
- scan for unsupported superlatives and claim drift;
- check anonymization and current venue requirements;
- ensure appendix material appears in the intended order.

## Writing Discipline

### Sentence and Paragraph Clarity

- Put familiar context before new information.
- Keep the grammatical subject close to its verb.
- Place the main action in the main verb.
- Use paragraph openings for context and paragraph endings for emphasis.
- Prefer concrete nouns and verbs over vague terms such as "performance," "quality," or "improvement."
- Prefer standard domain terminology over novel paraphrases for established concepts.
- Remove filler and intensifiers unless they change meaning.
- Do not use em dashes as a default device for explanations or parenthetical asides. Rewrite the material as a direct sentence, a concise clause, or an established technical compound.
- Use ordinary paragraphs for narrative flow; reserve `\paragraph{...}` for occasional compact signposts.

Read [references/writing-guide.md](references/writing-guide.md) for examples and detailed editing guidance.

### Notation and LaTeX Format Discipline

- **Define symbols on first use**: Explain every mathematical symbol, operator, set, index, and abbreviation in prose before relying on it.
- **Keep intro notation light**: Use simple generic symbols only when they make the story easier to follow. Move dense notation and derivations to methods or the appendix.
- **Use notation sparingly**: Do not introduce aliases for the same concept. Reuse the smallest stable symbol set that carries the argument.
- **Respect mathematical types**: Distinguish scalars, vectors, matrices, sets, and sequences consistently. Use the project macro for each type, such as a vector macro for prompts or token sequences when the notation contract defines one.
- **Treat project math macros as the notation contract**: When a project provides a shared macro file such as `math_commands.tex`, inspect it before editing and use its symbols and operators consistently. Avoid duplicate local definitions, resolve symbol collisions, and do not introduce alternative spellings for existing macros.
- **Prefer inline math for simple statements**: Write short, non-core definitions and one-step identities inline with `$...$`. Do not use `\[...\]` or `$$...$$` in manuscript source.
- **Number substantive displays**: Use `equation`, `align`, or another numbered AMS environment for core formulas, multi-line derivations, and equations discussed later. Give each substantive display a stable `\label{eq:...}` and refer to it consistently. Use unnumbered displays only when the user or venue explicitly requires them.
- **Budget vertical space deliberately**: Under tight page limits, keep simple or auxiliary formulas inline and reserve display space for objectives, theorems, methods, and equations used later. Do not shrink typography or spacing to compensate for avoidable display math.
- **Limit boxed equations**: Box at most one or two equations that state the paper's central result or prediction. Explain each boxed equation immediately before or after it, and leave supporting formulas unboxed.
- **Honor venue compatibility**: Use commands already supported by the venue template whenever possible. Inspect the official author kit before adding a formatting package or custom emphasis environment, then compile and visually inspect the result.
- **Layer notation explanations**: Explain core symbols in readable prose in Problem Formulation or the methods opening. At the beginning of the appendix, provide a comprehensive notation table covering symbols used in the main text and appendix unless the venue or user requires another placement.
- **Audit notation and displays before delivery**: Search for forbidden display delimiters, duplicated macro definitions, legacy spellings, undefined or overloaded symbols, and inconsistent equation references. Compile and verify that labels resolve and the notation table precedes appendix proofs or derivations.
- **Explain formal results**: After each theorem, proposition, or lemma, state what it answers, why it matters for the ML objective, and what it does not prove.

## Citation Safety

Never generate a citation or BibTeX entry from memory.

For every new citation:

1. Search an authoritative scholarly index or the publisher.
2. Verify that the paper exists and that title, authors, year, and venue agree across reliable sources.
3. Read enough of the paper to confirm the attributed claim.
4. Retrieve BibTeX from a DOI, publisher, arXiv, or another authoritative record.
5. Add the citation next to the narrow claim it supports.

If verification fails, insert `[CITATION NEEDED]` or a clearly named placeholder and tell the author exactly what remains unverified. Never invent a plausible reference.

Use [references/citation-workflow.md](references/citation-workflow.md) for APIs, BibTeX handling, and troubleshooting. When browsing is available, prefer current primary sources.

## Venue and Template Workflow

Venue rules are temporally unstable. Check the official call for papers, author instructions, checklist, and template for the exact submission cycle before changing the manuscript.

When starting from a bundled template:

1. Copy the complete venue directory, including style and bibliography files.
2. Compile the untouched template first.
3. Replace example content section by section.
4. Do not edit venue style files to recover space.
5. Compile frequently and compare the output with the official format.

Bundled templates are convenience snapshots, not authority. Official venue files override them.

For venue conversion:

1. Start a fresh project from the target venue template.
2. Move manuscript content, figures, tables, and bibliography entries.
3. Do not merge source and target preambles or style files.
4. Re-audit required sections, anonymity, page limits, disclosures, and references.
5. Compile and visually inspect the converted paper.

Read [references/checklists.md](references/checklists.md) for venue checklists and [references/systems-conferences.md](references/systems-conferences.md) for systems-specific structure and conversion guidance.

## Reviewer-Oriented Quality Gate

Evaluate the draft on:

- **Soundness**: Are claims supported by correct theory or experiments?
- **Significance**: Does the result matter for a clearly identified problem?
- **Originality**: Is the distinction from the closest work explicit?
- **Clarity**: Can a reviewer recover the argument and evidence quickly?
- **Reproducibility**: Are data, settings, metrics, and compute described?
- **Scope discipline**: Do conclusions stay within the demonstrated setting?

For a pre-submission review or rebuttal, load [references/reviewer-guidelines.md](references/reviewer-guidelines.md).

## Tables and Figures

Tables:

- use `booktabs` and consistent decimal precision;
- state metric direction and units;
- distinguish best values only when comparisons are valid;
- include uncertainty when available;
- make captions self-contained.

Figures:

- use vector output for plots and diagrams when possible;
- use accessible palettes and verify grayscale readability;
- avoid titles inside figures when the caption serves that role;
- ensure labels remain legible at final paper size;
- write captions in standard descriptive prose, stating what the figure shows and the main takeaway;
- keep captions concise when the figure already contains explanatory text or annotations;
- do not repeat the figure's labels, turn the caption into a miniature methods section, or append a broad limitations discussion that belongs in the main text.

## Bundled Resources

The `templates/` directory includes snapshots for major ML/AI and systems venues. See [templates/README.md](templates/README.md) for inventory and compilation notes.

The detailed references preserve the long-form guidance intentionally omitted from this file. Keep the main skill concise; add new venue-specific or tool-specific detail to the relevant reference rather than expanding `SKILL.md`.
