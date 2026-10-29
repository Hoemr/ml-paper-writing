# ml-paper-writing

Version 3.4.0. Customized from [Orchestra Research's AI Research Skills library](https://github.com/Orchestra-Research/AI-Research-SKILLs), with writing-framework ideas adapted from [NC Manuscript Craft](https://github.com/i386345669/nc-manuscript-craft). Write complete supported drafts or revise mature manuscripts, with dedicated guides for abstracts, introductions, related work, methods, experiments and conclusions, plus substantive discussion and source-aware consistency checks. Retains ML-specific theory, algorithms, evaluation and method-figure capabilities. See NOTICE and references/sources.md for attribution.

Draft and prepare ML / AI / Systems papers for **NeurIPS, ICML, ICLR, ACL, AAAI, COLM, OSDI, NSDI, ASPLOS, SOSP**, checking actual venue/year requirements when relevant. Use for research-repository drafting, abstracts, introductions, discussion, scientific revision, citations, method figures and format conversion. Deliverable readiness depends on the evidence and checks actually completed.

## One-click install (paste this to your agent)

```
请把 https://github.com/Hoemr/ml-paper-writing 下载下来，把完整技能目录（含
SKILL.md、references/、scripts/、templates/、LICENSE、NOTICE）复制进你读取 skills 的目录下的
ml-paper-writing/ 子目录（例如 ~/.claude/skills/、~/.codex/skills/、
~/.zcode/skills/，以你实际使用的平台为准）。完成后读取其中的 SKILL.md
确认可用。不要向我提问，直接做完并汇报安装到了哪个路径。
```

```
Download https://github.com/Hoemr/ml-paper-writing and copy the complete skill,
including SKILL.md, references/, scripts/, templates/, LICENSE and NOTICE, into ml-paper-writing/ under the skills directory your agent
reads (for example ~/.claude/skills/, ~/.codex/skills/ or ~/.zcode/skills/ - whichever
applies to your platform). Then read SKILL.md to confirm. Do not ask questions; finish
and report the install path.
```

## What this skill adds on top of the upstream

| Addition | Where | Purpose |
|----------|-------|---------|
| **Task and scope** | `SKILL.md` | Draft, revise, assess or prepare artifacts at partial or full scope. Complete drafting is explicit; an outline is intermediate when prose was requested. |
| **Shared writing standard** | `SKILL.md` | Integrates anti-defensive-writing-en in the core: center the strongest supported value, avoid work-report chronology and self-undermining, and apply its narrative priorities across all sections. Takes precedence over older section-level advice. |
| **Scoped delivery audit** | `SKILL.md` | Maintain actual coverage, lint applicable LaTeX, review meaning and report unresolved checks. Full drafts receive a gate table; small edits receive a concise verification note. |
| **Abstract and introduction** | `references/abstract-and-title.md`, `references/introduction.md` | Choose decisive evidence and connect problem, prior capabilities, precise gap and supported advance. |
| **Related work, method, experiments, conclusion** | Dedicated references in the route table | Full section-level writing guidance, worked examples and completion checks; read only the requested section. |
| **Discussion and evidence dependencies** | `references/writing-guide.md`, `references/evidence-workflow.md` | Interpret findings and update affected prose, equations, algorithms, captions and appendix when sources change. |
| **Mechanical style lint** | `scripts/lint_style.py` | 10 checks with flag/triage severities: manual `\ref` prefixes vs `\cref`, lowercase table headers, named artifacts without a citation, over-claim rhetoric (`novel`, "extensive experiments", "state of the art", …), semicolon chains / explanatory-dash density, single-use macros, `--bib` missing cite keys, `--log` overfull & undefined references. |
| **Punctuation & notation gates** | `references/style-conventions.md` | Semicolons and explanatory dashes used sparingly; no single-use intermediate symbols; one declared notation scheme; `\cref` with abbreviated names where the venue allows. |
| **Progressive disclosure** | `references/` | Each topic has a designated owner. Abstract, introduction and evidence guidance load only when relevant; artifact-specific mechanics stay in existing modules. |
| **Built-in method figures** | `references/figure-workflow.md`, `references/method-figure/`, `scripts/method-figure/` | Architecture diagrams, method overviews, pipeline schematics, reference-led restyling, collision repair and figure audits, with standalone TikZ, PDF/PNG and six-stage QA. |
| **Venue template snapshots** | `templates/` | LaTeX snapshots for the 10 supported venues, with per-venue setup notes in `templates/README.md`. |

## Workflow activation

- Local edits: verify new/affected references and their support.
- Full drafts/revisions/full-skill runs: audit all bibliography entries and every
  citation occurrence, including existing references. Report incomplete checks.
- Reference-only audits: report findings without editing the manuscript or bibliography.
- Title/abstract retrieval optimization: explicit request only. Normal title polish
  and full-skill requests do not run GEO, query coverage, trend or visibility probes.

Examples: “用 ml-paper-writing 全量修订” includes reference auditing;
“只核查引用，不修改论文” runs a read-only audit;
“启用标题检索优化 workflow” enables the optional title optimizer.

The optional title optimizer now prioritizes semantically appropriate terms with
verified recent citation growth: rolling 365-day comparison, fixed paper cohorts,
base counts, absolute/relative growth and single-paper concentration. It offers
a concise title and an evidence-backed keyword variant, without promising search
gains. See references/title-optimization/citation-momentum.md. Publication trends
remain separately labeled auxiliary evidence. No live keyword ranking is bundled.

## Repository layout

```
ml-paper-writing/
├── SKILL.md                    ← shared writing standard, modes, workflow, gates
├── references/
│   ├── writing-guide.md        ← complete drafting, research types and sections
│   ├── abstract-and-title.md   ← selection, argument, compression and titles
│   ├── introduction.md         ← capabilities, gap, idea and fulfilled promises
│   ├── related-work.md         ← source relationships and exact comparison
│   ├── method-writing.md       ← idea, equations, procedure and reproduction
│   ├── experiments-results.md  ← evaluation questions and result narration
│   ├── conclusion.md           ← supported answer and consequence
│   ├── evidence-workflow.md    ← sources, dependencies and synchronization
│   ├── style-conventions.md    ← notation, cross-refs, tables, prose, punctuation
│   ├── algorithms.md           ← pseudocode recipes and worked examples
│   ├── citation-workflow.md    ← unified citation verification and audit routing
│   ├── reference-audit.md      ← complete identity and occurrence-level support audit
│   ├── title-optimization.md   ← opt-in retrieval optimization workflow
│   ├── title-optimization/     ← supporting guidance, snapshots and license
│   ├── figure-workflow.md      ← built-in narrative, TikZ construction and QA
│   ├── method-figure/          ← drawing guides, TikZ templates and reference PNG
│   ├── reviewer-guidelines.md  ← supporting wording examples, equivalence check
│   ├── checklists.md           ← submission rules; verify exact venue and year
│   ├── systems-conferences.md  ← OSDI / NSDI / ASPLOS / SOSP specifics
│   └── sources.md              ← guidance provenance and external limits
├── scripts/
│   ├── lint_style.py           ← mechanical delivery-audit lint (see below)
│   ├── check-ref/              ← literature lookup helper and private local configuration
│   ├── paper-title-optimizer/  ← optional trend, title-statistics and visibility helpers
│   ├── audit_pseudocode.py     ← mechanical audit for a pseudocode block
│   └── method-figure/          ← QA runner, lint, instrumentation, geometry/type checks
├── templates/                  ← venue template snapshots + setup notes
├── LICENSE                     ← MIT (from upstream)
├── NOTICE                      ← upstream and adapted-guidance notices
└── README.md
```

## The delivery audit in one minute

```
1. Record the requested scope and directly affected components
2. For edited LaTeX: python3 scripts/lint_style.py paper.tex --bib refs.bib --log main.log
   → triage every finding (fix it, or state why it stands)
3. Fresh-context reviewer (rules + text + needed evidence) when available and permitted;
   otherwise a separately identified self-review. Method figures retain independent visual QA.
4. Full-paper work: gate table. Small edits: concise verification note. Report actual gaps.
```

Checks follow the actual artifact. Plain-text prose needs no artificial compile; a compiled PDF still needs visual review. Never equate lint success with scientific correctness.

## Operating principles (from SKILL.md)

1. One central contribution with an explicit problem, mechanism, evidence, and consequence.
2. Preserve scientific meaning: assumptions, comparison budgets, denominators, uncertainty, adverse results, limitations. Never invent results or citations.
3. Default to partial scope for local edits; complete-draft and whole-manuscript requests use full scope.
4. Run the delivery audit before reporting completion; report actual coverage and failures.
5. Verify current venue rules from official sources — page limits, disclosure policies, and templates change.

## License

MIT (same as upstream). See [LICENSE](LICENSE).

## See also

- [Orchestra Research's AI Research Skills library](https://github.com/Orchestra-Research/AI-Research-SKILLs) — upstream
- [Built-in method-figure module](references/figure-workflow.md) — standalone TikZ source, PDF/PNG, design rules and mechanical/visual QA; no separate figure skill required
- [Built-in reference audit](references/reference-audit.md) — full coverage during full-paper work; read-only when requested as an audit
- [Optional title retrieval optimization](references/title-optimization.md) — explicit opt-in only, excluded even from generic full-skill runs
- [Hoemr/my_paper_hub](https://github.com/Hoemr/my_paper_hub) — personal reference paper hub
