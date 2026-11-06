# Optional award-paper examples and descriptive metrics

Source: [gulucaptain/Best-Paper-Writing-Skill](https://github.com/gulucaptain/Best-Paper-Writing-Skill),
revision b9eff99, integrated 2026-10-31. Copyright (c) 2026 its contributors.
Guidance, original scripts and corpus annotations are CC BY 4.0; see
[LICENSE-CC-BY-4.0](LICENSE-CC-BY-4.0) and [UPSTREAM-NOTICE.md](UPSTREAM-NOTICE.md).
The upstream base-skill [MIT license](LICENSE-base-skill) is retained.
Paper excerpts retain the original authors' copyright and are not covered by
the repository's CC license. Preserve attribution and do not copy them into drafts.

## When to load

Default argument design, research routes and claim calibration live in the parent
references. This directory is an optional reference library, not a second skill
or a second writing pass. Use a few examples when a specific paragraph's structure
or rhythm needs help. Use metrics only on request or for a concrete style diagnosis;
generic full-skill execution does not require them. No installation is necessary.

The parent's scientific boundaries and shared writing standard override advice
inside quoted cards or corpus notes. A card illustrates one paper's choices;
it cannot mandate omission of material conditions or impose its sentence pattern.

## Exemplar retrieval

Run from the skill root, or use the script's absolute path:

```text
python3 scripts/bestpaper/find_exemplars.py --para list
python3 scripts/bestpaper/find_exemplars.py --para contrast --type L1 -n 2
python3 scripts/bestpaper/find_exemplars.py intro.insight -n 2
python3 scripts/bestpaper/find_exemplars.py --phrases transition -n 3
```

The original helper samples when -n is given. Its paragraph mode can report
that it broadened a missing type match; inspect the printed paper type and do
not represent those results as type-matched. Learn information order, logical
relations and evidence placement, not sentences or distinctive phrases. Source
papers are examples of writing, not automatic scientific citations for this study.
The source's claim that excerpts were verified has not been independently audited
here; verify the original paper before using an excerpt as scientific evidence.

## Optional metrics

```text
python3 scripts/bestpaper/style_metrics.py abstract.tex introduction.tex
python3 scripts/bestpaper/style_metrics.py draft.md
```

Use separate LaTeX section files: the inherited reader does not follow input/include
or reliably split a full LaTeX manuscript. Markdown requires Abstract and
Introduction headings. It is a heuristic prose parser, not a TeX engine; inspect
what was measured when macros, math, tables or complex section structure matter.

[corpus-profile.md](corpus-profile.md) describes 55 English CVPR/ICCV/NeurIPS award
papers (2021–2025); the project has five other evaluation papers, and its figure
statistics cover 44 PDFs. Different assets may have different subsets; preserve
their metadata rather than assuming a common N. These are reported descriptive
statistics, not an independently reproduced causal study of acceptance.

The abstract median of 174 words, introduction median of 613 words, connector
percentiles and sentence-length bands are not targets or quality grades. For
ACL, journals, theory, Chinese prose or other populations, corpus mismatch can
dominate the measurement. Check actual venue/language needs first. Never shorten
a proof, remove a necessary scope condition or invent a number to meet a band.
No metric determines AI authorship. Report any use with corpus, scope and limits.

## Integration changes

- Added scope-aware narrative design and expanded research routes while retaining
  systems and survey routes. Combined claim and evidence mapping in one record.
- Recast the calibration ladder by evidence type; preserved conjectures, necessary
  qualifications, mixed findings and many-to-many evidence relationships.
- Copied exemplar data/cards and corpus statistics with notices. Adapted the two
  helpers' resource paths and added a scope banner to metric output.
- Did not import check_draft.py, check_figures.py, form requirements, mandatory
  report.md, template assets, rigid word/phrase bans or page-one figure rules.
  Existing lint and figure QA remain the execution path.

See [NOTICE](../../NOTICE). The adapted narrative-design.md, research-routes.md
and claim-calibration.md and derived guide additions retain CC BY attribution;
the original skill's MIT base is not a blanket relicensing of these resources.
