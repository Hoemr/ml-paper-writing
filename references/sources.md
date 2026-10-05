# Guidance provenance

Links identify guidance sources, not citations to insert automatically into a
paper. Verify the exact claim and metadata before citing research. Opinionated
writing advice and repository observations are not universal venue policy or
proof of reviewer behavior.

## Writing guidance retained from the original skill

- [Neel Nanda](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers): a central narrative connecting contribution, evidence and relevance.
- [Sebastian Farquhar](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/): an abstract pattern, used as an optional drafting aid.
- [Gopen and Swan](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf): reader expectations, context and sentence emphasis.
- [Zachary Lipton](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/): concrete wording and removal of empty intensifiers.
- [Ethan Perez](https://ethanperez.net/easy-paper-writing-tips/): local clarity and ambiguous-pronoun repair.
- [Jacob Steinhardt](https://jsteinhardt.stat.berkeley.edu/blog/advice-for-authors): precise terms and explicit assumptions.
- [Andrej Karpathy](https://karpathy.github.io/2016/09/07/phd/): research/paper framing. Previously unsourced direct quotations are not retained.

These inherited links were not re-audited as research claims in this revision.
Unverified citation-error percentages and reviewer reading-rate statistics were
removed rather than restated. The original upstream library attribution remains
MIT / Orchestra Research; no automatic software acknowledgment is required.

## Sources inspected on 2026-10-03 (UTC+8)

### FigGenie

Canonical repository: [Sleepy-Avacado/FigGenie-paper-diagram-skill](https://github.com/Sleepy-Avacado/FigGenie-paper-diagram-skill).
Inspected revision: `82be26d6f2954c8bfc4089d70d8dcf82fe395864`.

Read its [skill](https://github.com/Sleepy-Avacado/FigGenie-paper-diagram-skill/blob/82be26d6f2954c8bfc4089d70d8dcf82fe395864/skills/figgenie-paper-diagram/SKILL.md),
[drawing plan](https://github.com/Sleepy-Avacado/FigGenie-paper-diagram-skill/blob/82be26d6f2954c8bfc4089d70d8dcf82fe395864/skills/figgenie-paper-diagram/references/drawing-plan.md),
and [anti-patterns](https://github.com/Sleepy-Avacado/FigGenie-paper-diagram-skill/blob/82be26d6f2954c8bfc4089d70d8dcf82fe395864/skills/figgenie-paper-diagram/references/anti-patterns.md).
Adapted principles: explain composition before coordinates, let the mechanism
choose the arrangement, align repeated structures while exposing their actual
difference, and inspect print-size renders after linting. Their local adaptation
is in [figure-workflow.md](figure-workflow.md); mechanical implementation remains
in ml-method-figure. No SVG/PPTX code, corpus counts, acceptance statistics or
large prose blocks were copied.

### Game the LLM Reviewer

Canonical repository: [Michael-Jiahao-Zhang/game-the-llm-reviewer](https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer).
Confirmed against GitHub's repository identity and primary README, rather than
a similarly named catalog entry. Inspected revision:
`08ba6ff57487967f7090863efe21bbd95186637f`.

Read its [skill](https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer/blob/08ba6ff57487967f7090863efe21bbd95186637f/skills/game-the-llm-reviewer/SKILL.md)
and [strategy cards](https://github.com/Michael-Jiahao-Zhang/game-the-llm-reviewer/blob/08ba6ff57487967f7090863efe21bbd95186637f/skills/game-the-llm-reviewer/references/strategies.md).
Adapted principles: evidence-anchored local wording, contribution/effect framing,
selective abstract reordering, explicit scope, and an equivalence check against
the original scientific interpretation. The adaptation lives only in
[reviewer-guidelines.md](reviewer-guidelines.md). Its linked research papers have
not been independently verified here and are not imported as paper citations;
no performance number or claim of universal reviewer preferences is retained.

The same-day follow-up restored selected chapter patterns from the pre-refactor
personal skill and added original teaching examples. Defensive-writing examples
adapt the inspected repository's lexical/scope/equivalence principles; they do
not copy its examples or restore the old blanket prohibition on limitations.
No new studies or claims of measured improvement for weaker agents were added.

### Local figure authority

[ml-method-figure](../../ml-method-figure/SKILL.md) owns design/construction and
mechanical/visual checks. Its own attribution governs its rules. This skill
routes to it rather than copying a second rulebook.

## Citation lookup documentation

[Semantic Scholar](https://api.semanticscholar.org/api-docs/),
[Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/),
[arXiv](https://info.arxiv.org/help/api/basics.html), and
[OpenAlex](https://docs.openalex.org/) are lookup tools; metadata hits do not
establish claim support. Current venue policies are routed through
[checklists.md](checklists.md).
