# ml-paper-writing

Customized and extended from the open-source `ml-paper-writing` skill in [Orchestra Research's AI Research Skills library](https://github.com/Orchestra-Research/AI-Research-SKILLs). Retains the upstream MIT license; adds a Kaiming He exemplar overlay, per-module paragraph-role templates, and a consolidated 4-phase citation audit.

Write publication-ready ML / AI / Systems papers for **NeurIPS, ICML, ICLR, ACL, AAAI, COLM, OSDI, NSDI, ASPLOS, SOSP**. Use when drafting papers from research repositories, structuring arguments, verifying citations, revising LaTeX manuscripts, converting venue formats, or preparing camera-ready submissions.

## What this skill adds on top of the upstream

| Addition | Where | Purpose |
|----------|-------|---------|
| **Kaiming He style overlay** | `references/styles/kaiming-he-style.md` | Vertical case study distilled from ResNet / Mask R-CNN / MAE / MoCo / Focal Loss: 10-item checklist, signature sentence patterns, vocabulary mapping, structural template. Observation-first, two core designs, ablation-before-main, non-restating conclusion. |
| **Method-figure design guide** | `references/method-figure-guide.md` | Mechanism-first layouts, explicit arrow semantics, optional dark semantic palette, vector sources, and final-size visual checks. |
| **Per-module paragraph-role templates** | `references/module-writing-guide.md` | Abstract / Introduction / Related Work / Conclusion each get: universal pattern(s), He variant, deliverable check, cross-references. Replaces ad-hoc structure decisions. |
| **Cross-cutting operating cheat sheet** | `references/writing-style.md` | One-page dispatch table, four one-liners, claim-evidence discipline, banned openings, de-AI traces, pre-delivery gate. Read before drafting a section. |
| **Rebuttal dispatcher** | `references/rebuttal-guideline.md` | Bridges to the sibling `reviewer-response-rebuttal-skill` with 6 project-level MUST overlays (no `\cref` in rebuttal, future-work 2-4 sentences, compile gate, red/blue markers preserved, jmlr2e shared theorem counter, main text does not restate appendix notation). |
| **Consolidated 4-phase citation audit** | `references/audit-existing-references.md` + `scripts/search_paper.py` | Read-only audit pipeline (entry truthfulness + claim support). Two-dimension verification with field-comparison rules, WebSearch batched 5/parallel, rate-limit backoff. The audit script and its workflow now live here instead of in a separate sibling skill. |

## Repository layout

```
ml-paper-writing/
├── SKILL.md                              ← main entry; operating contract + progressive disclosure
├── LICENSE                               ← MIT (from upstream)
├── README.md                             ← this file
├── references/
│   ├── writing-guide.md                  ← universal philosophy (Gopen & Swan, Farquhar, Lipton, Steinhardt, Perez)
│   ├── writing-style.md                  ← cross-cutting operating cheat sheet
│   ├── module-writing-guide.md           ← per-section role templates (Abstract / Intro / Related Work / Conclusion)
│   ├── styles/
│   │   └── kaiming-he-style.md           ← Kaiming He exemplar overlay (10-item checklist)
│   ├── citation-workflow.md              ← forward direction: search / verify / add new citations
│   ├── audit-existing-references.md      ← backward direction: read-only 4-phase audit of existing citations
│   ├── rebuttal-guideline.md             ← dispatcher + project MUST overlays for rebuttal phase
│   ├── checklists.md                     ← venue checklists
│   ├── reviewer-guidelines.md            ← reviewer criteria
│   ├── sources.md                        ← primary writing and venue sources
│   └── systems-conferences.md            ← OSDI / NSDI / ASPLOS / SOSP specifics
├── scripts/
│   ├── search_paper.py                   ← OpenAlex + Semantic Scholar search (used by audit)
│   └── api_keys.local.json               ← local-only secrets (NEVER commit)
└── templates/                            ← LaTeX snapshots for the 10 supported venues
```

## Kaiming He style — when to use it

The He overlay applies when the paper is:

- Empirical CV / ML method paper with 1-2 design choices
- Motivated by a surprising empirical observation (often Figure 1)
- Stated as "two core designs" or similar
- Accompanied by ablation tables that isolate each choice

It does **not** force-fit onto pure theory, survey, or systems-engineering papers. See `references/styles/kaiming-he-style.md` § "When to use this style" for the matching criteria, and the 10-item checklist (opening observation → declarative voice → Figure 1 is an observation, not an architecture) for self-audit.

## Operating principles (from SKILL.md)

1. Treat the author as the owner of scientific claims; the agent is an active collaborator.
2. Never fabricate citations, BibTeX, metrics, ablations, baselines, hyperparameters, or venue requirements.
3. **Do not proactively call citation APIs, fetch BibTeX, or run reference audits.** Verification is on-demand: only when the user explicitly asks.
4. Verify current venue rules from official sources because page limits, disclosure policies, and templates change.
5. Compile and inspect deliverable LaTeX rather than stopping after source edits.

## Provenance

Derived from the open-source `ml-paper-writing` skill in [Orchestra Research's AI Research Skills library](https://github.com/Orchestra-Research/AI-Research-SKILLs). Retains the upstream MIT license. Extensions: slimmer progressive-disclosure structure, stricter evidence and delivery gates, Kaiming He exemplar overlay, per-module templates, consolidated 4-phase citation audit, and rebuttal dispatcher with project-level MUST overlays.

## License

MIT (same as upstream). See [LICENSE](LICENSE).

## See also

- [Orchestra Research's AI Research Skills library](https://github.com/Orchestra-Research/AI-Research-SKILLs) — upstream
- `reviewer-response-rebuttal-skill` — sibling skill for rebuttal phase (depth content)
- [Hoemr/my_paper_hub](https://github.com/Hoemr/my_paper_hub) — personal reference paper hub
