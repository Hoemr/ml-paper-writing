# ml-paper-writing

Customized and extended from the open-source `ml-paper-writing` skill in [Orchestra Research's AI Research Skills library](https://github.com/Orchestra-Research/AI-Research-SKILLs). Retains the upstream MIT license; rebuilds the workflow around **two entry modes**, a **mandatory delivery audit**, and a **mechanical style lint**, so an agent's output still matches the skill's rules at the end of a long session — not just at the start.

Write publication-ready ML / AI / Systems papers for **NeurIPS, ICML, ICLR, ACL, AAAI, COLM, OSDI, NSDI, ASPLOS, SOSP**. Use when drafting papers from research repositories, structuring arguments, verifying citations, revising LaTeX manuscripts, converting venue formats, or preparing camera-ready submissions.

## One-click install (paste this to your agent)

```
请把 https://github.com/Hoemr/ml-paper-writing 下载下来，把其中 SKILL.md、
references/、scripts/、templates/ 完整复制进你自己读取 skills 的目录下的
ml-paper-writing/ 子目录（例如 ~/.claude/skills/、~/.codex/skills/、
~/.zcode/skills/，以你实际使用的平台为准）。完成后读取其中的 SKILL.md
确认可用。不要向我提问，直接做完并汇报安装到了哪个路径。
```

```
Download https://github.com/Hoemr/ml-paper-writing and copy SKILL.md, references/,
scripts/ and templates/ into ml-paper-writing/ under the skills directory your agent
reads (for example ~/.claude/skills/, ~/.codex/skills/ or ~/.zcode/skills/ - whichever
applies to your platform). Then read SKILL.md to confirm. Do not ask questions; finish
and report the install path.
```

## What this skill adds on top of the upstream

| Addition | Where | Purpose |
|----------|-------|---------|
| **Two entry modes** | `SKILL.md` § Modes | Partial mode (default): touch only the requested scope. Full mode: whole-manuscript revision/polish — read the writing guide and style conventions completely, revise chapter by chapter. |
| **Mandatory delivery audit** | `SKILL.md` § Delivery audit | Rules read early in a long session decay. Before reporting completion the agent must enumerate every changed unit, lint mechanically, review judgment calls with a fresh-context reviewer, and deliver a gate table — a gate with no row counts as not checked. |
| **Mechanical style lint** | `scripts/lint_style.py` | 10 checks with flag/triage severities: manual `\ref` prefixes vs `\cref`, lowercase table headers, named artifacts without a citation, over-claim rhetoric (`novel`, "extensive experiments", "state of the art", …), semicolon chains / explanatory-dash density, single-use macros, `--bib` missing cite keys, `--log` overfull & undefined references. |
| **Punctuation & notation gates** | `references/style-conventions.md` | Semicolons and explanatory dashes used sparingly; no single-use intermediate symbols; one declared notation scheme; `\cref` with abbreviated names where the venue allows. |
| **Single-owner progressive disclosure** | `references/` | `SKILL.md` stays a routing table; each topic has exactly one owner file (writing-guide, style-conventions, algorithms, citation-workflow, figure-workflow, reviewer-guidelines, checklists, systems-conferences, sources) — no second drifting copy of any rule. |
| **Venue template snapshots** | `templates/` | LaTeX snapshots for the 10 supported venues, with per-venue setup notes in `templates/README.md`. |

## Repository layout

```
ml-paper-writing/
├── SKILL.md                    ← modes, workflow, gates, delivery audit
├── references/
│   ├── writing-guide.md        ← evidence-first rewriting and chapter patterns
│   ├── style-conventions.md    ← notation, cross-refs, tables, prose, punctuation
│   ├── algorithms.md           ← pseudocode recipes and worked examples
│   ├── citation-workflow.md    ← search / verify / add new citations
│   ├── figure-workflow.md      ← route into the sibling ml-method-figure skill
│   ├── reviewer-guidelines.md  ← defensive writing, equivalence check
│   ├── checklists.md           ← submission rules; verify exact venue and year
│   ├── systems-conferences.md  ← OSDI / NSDI / ASPLOS / SOSP specifics
│   └── sources.md              ← guidance provenance and external limits
├── scripts/
│   ├── lint_style.py           ← mechanical delivery-audit lint (see below)
│   └── audit_pseudocode.py     ← mechanical audit for a pseudocode block
├── templates/                  ← venue template snapshots + setup notes
├── LICENSE                     ← MIT (from upstream)
└── README.md
```

## The delivery audit in one minute

```
1. Enumerate changed units (sections, tables, algorithm blocks, symbols, citations)
2. Lint: python3 scripts/lint_style.py paper.tex --bib refs.bib --log main.log
   → triage every finding (fix it, or state why it stands)
3. Fresh-context reviewer (rules + text only, no conversation history) for judgment gates
4. Deliver the gate table:  | Gate | Items checked | Violations | Resolution |
```

The mechanism borrows from audit-style skills: an explicit list first, per-item verdicts second, a report format that makes omissions visible. Louder MUSTs do not survive a long session; a required table does.

## Operating principles (from SKILL.md)

1. One central contribution with an explicit problem, mechanism, evidence, and consequence.
2. Preserve scientific meaning: assumptions, comparison budgets, denominators, uncertainty, adverse results, limitations. Never invent results or citations.
3. Default to partial mode; go full only on a whole-manuscript request, and say which mode was chosen.
4. Run the delivery audit before reporting completion; report actual coverage and failures.
5. Verify current venue rules from official sources — page limits, disclosure policies, and templates change.

## License

MIT (same as upstream). See [LICENSE](LICENSE).

## See also

- [Orchestra Research's AI Research Skills library](https://github.com/Orchestra-Research/AI-Research-SKILLs) — upstream
- `ml-method-figure` — sibling skill owning method-figure construction and QA
- `check-ref` — sibling skill for read-only audits of existing references
- [Hoemr/my_paper_hub](https://github.com/Hoemr/my_paper_hub) — personal reference paper hub
