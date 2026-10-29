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
in the built-in figure module and `scripts/method-figure/`. No SVG/PPTX code, corpus counts, acceptance statistics or
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
the original scientific interpretation. The adaptation originally lived in
[reviewer-guidelines.md](reviewer-guidelines.md); current narrative authority is
the [shared writing standard](../SKILL.md#shared-writing-standard). Its linked
research papers have not been independently verified here and are not imported as paper citations;
no performance number or claim of universal reviewer preferences is retained.

The same-day follow-up restored selected chapter patterns from the pre-refactor
personal skill and added original teaching examples. Defensive-writing examples
adapt the inspected repository's lexical/scope/equivalence principles; they do
not copy its examples or restore the old blanket prohibition on limitations.
No new studies or claims of measured improvement for weaker agents were added.
The later anti-defensive integration below supersedes the earlier narrative
priority where they differ.

### Local figure authority

The built-in [figure workflow](figure-workflow.md) owns design/construction and
mechanical/visual checks. Its attribution and per-rule provenance in
[constraints.md](method-figure/constraints.md) are retained from the former
standalone figure skill. Templates, the reference PNG and QA helpers are bundled
inside ml-paper-writing; no sibling skill is needed.

## NC Manuscript Craft adaptation — 2026-10-22 (UTC+8)

Source: [i386345669/nc-manuscript-craft](https://github.com/i386345669/nc-manuscript-craft),
v1.1.0, inspected revision `90c4348a396f2fdb15c3148996fcd0ea6684ed9a`.
Read its entrypoint and relevant guidance on argument, title/abstract,
introduction, discussion, expression, citations, full drafting, evidence/state,
and study types. Also inspected selected guidance on figures, bilingual work,
literature learning and submission preparation. This is not a claim to have
executed or behaviorally evaluated NC itself.

Adapted ideas: distinguish task from scope; complete supported manuscript
components despite local gaps; select an abstract's decisive evidence; derive
an introduction's gap from actual existing capabilities; interpret findings in
Discussion; preserve author choices; replace repeated defenses with precise
definitions; track actual dependencies when source evidence changes.

The local adaptation is in [writing-guide.md](writing-guide.md),
[abstract-and-title.md](abstract-and-title.md), [introduction.md](introduction.md),
[reviewer-guidelines.md](reviewer-guidelines.md) and
[evidence-workflow.md](evidence-workflow.md), with citation/caption interfaces
in their existing owner files. Examples were written for ML contexts. NC's
biomedical examples, prompt collection and project-state templates are not
imported as manuscript evidence or runtime dependencies. Existing ML theorem,
algorithm, comparison-budget and method-figure capabilities remain local.

The defensive-writing guide also retains the evidence/equivalence principles
from the Game the LLM Reviewer adaptation above; it does not use reviewer-score
optimization. NC is MIT licensed, copyright (c) 2026 i386345669; its license
notice is retained in [NOTICE](../NOTICE). No acceptance, detector-score or
empirical writing-quality improvement is asserted by this adaptation.

## Section-guide expansion — 2026-10-22 (UTC+8)

NC v1.1.0 at the revision recorded above was reread for Results (04), Methods
and statistics (06), Discussion/conclusion (05) and supplementary material (08).
Adapted principles: organize findings by their scientific job; describe actual
execution rules; distinguish main explanation, reproducibility detail and
editorial history; preserve unique definitions when moving appendix content;
end with the supported research increment. Biomedical examples were not imported.

Also inspected these primary skill repositories:

- [Orchestra Research, AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/773a52944ba4747a18bd4ae9ade53fff041adcbc/20-ml-paper-writing),
  revision `773a52944ba4747a18bd4ae9ade53fff041adcbc`: its ML writing guide and
  selected systems section blueprints. Relevant ideas are reproducible method
  exposition, claim-linked evaluation and explicit prior-work comparison.
  The inherited Orchestra attribution remains in NOTICE/LICENSE. Fixed page or
  paragraph counts, universal venue claims, mandatory active voice, vocabulary
  marketing rules and fabricated design histories are not adopted.
- [slark-prime/ml-paper-writing, section renderers](https://github.com/slark-prime/ml-paper-writing/blob/9146d4023e0e632396725e796fcc3a40637e80ef/references/section-renderers.md),
  revision `9146d4023e0e632396725e796fcc3a40637e80ef`: read the relevant related
  work, method, experiments and conclusion guidance, plus selected entrypoint
  material. Considered comparison dimensions, explanation of component
  interfaces and division of labor among prose and artifacts. No license was
  identified in the inspected repository metadata; no code, templates, examples
  or substantial text blocks were imported. Local instructions and examples are
  newly written. Acceptance optimization, compulsory planning objects and
  automatic research-completion work are not adopted.

The expanded local guides are [related-work.md](related-work.md),
[method-writing.md](method-writing.md),
[experiments-results.md](experiments-results.md) and [conclusion.md](conclusion.md).
They own section writing; citations, artifact mechanics and evidence tracking
remain in their existing owner files. Narrative and defensive-wording authority
now resides in the [shared writing standard](../SKILL.md#shared-writing-standard).
This source review does not independently verify the repositories' linked research, quoted advice,
conference policies or claims of writing success.

## Anti-defensive writing integration — 2026-10-29 (UTC+8)

Source: the user-supplied local `anti-defensive-writing-en/SKILL.md`, read in
full. The inspected standalone source is identified by its content hash:
SHA-256: `49705a92677d06b1be9f78be5be4f966b1d30c4ed72a3b97c86a973d06683b9b`.

Its press-conference principle, strength-centered narrative, language against
self-undermining, experiment responsibilities, section responsibilities,
ordered treatment of unfavorable material and final checks are incorporated
into [SKILL.md](../SKILL.md#shared-writing-standard). At the author's explicit
request, that core standard takes precedence over the previous anti-defensive
guidance and section-level examples throughout the writing lifecycle.

The standalone source is retained unchanged; using ml-paper-writing does not
require loading or installing it. Reviewer guidance now supplies subordinate
examples and equivalence checks. Section-guide pointers and examples follow the
core standard. Factual comparison conditions and evidence remain accurate;
selection and reframing do not turn a scoped benefit into universal superiority.
This is a local writing preference, not a verified claim about acceptance or
reviewer behavior.

## Citation lookup documentation

[Semantic Scholar](https://api.semanticscholar.org/api-docs/),
[Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/),
[arXiv](https://info.arxiv.org/help/api/basics.html), and
[OpenAlex](https://docs.openalex.org/) are lookup tools; metadata hits do not
establish claim support. Current venue policies are routed through
[checklists.md](checklists.md).


## Integrated local workflows (3.2.0)

The local check-ref workflow supplied complete bibliography/occurrence inventories,
independent identity verification, field comparisons, support assessment, report
structure and scripts/check-ref/search_paper.py. These are consolidated in
reference-audit.md and citation-workflow.md. Abstract-only uncertainty can now be
resolved with primary full text; missing search evidence is not proof of fabrication.
Provider setup prompts and tool-brand requirements are not scientific gates.

The local paper-title-optimizer supplied the explicit-only title-optimization.md
workflow, its supporting references/data and three JavaScript helpers. Its MIT
license is retained at title-optimization/LICENSE. Historical trend/title statistics
and effect-size statements are not freshly verified evidence or guaranteed outcomes.
The parent writing rules take precedence over heuristic sentence templates.
Neither integrated workflow requires its former standalone skill installation.
