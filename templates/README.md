# Bundled LaTeX templates

These are starting assets, not a guarantee of current venue compliance. Verify
the selected venue/year and required class/options using
[checklists.md](../references/checklists.md) before a submission task.

## Setup

Copy the complete selected template into the requested new project directory,
including required style, bibliography and auxiliary files. Compile its example
unchanged before replacing content. If dependencies or a suitable compiler are
missing, report the exact failure; do not install a large toolchain by default.
Keep the original template available as reference rather than embedding long
commented examples in the final manuscript. Preserve official style files.

Use the template's engine, macros and bibliography backend. For a multi-file
paper, run its normal build command (often `latexmk -pdf main.tex`); standalone
method figures use the compilation/QA route in `$ml-method-figure`. Inspect the
final PDF, not merely exit status. Remove unused examples before delivery.

## Available assets

| Directory | Example entrypoint |
| --- | --- |
| `icml2026/` | `example_paper.tex` |
| `iclr2026/` | `iclr2026_conference.tex` |
| `neurips2025/` | `main.tex` |
| `acl/` | `acl_latex.tex` or `acl_lualatex.tex` |
| `aaai2026/` | `aaai2026-unified-template.tex` |
| `colm2025/` | `colm2025_conference.tex` |
| `osdi2026/`, `nsdi2027/`, `asplos2027/`, `sosp2026/` | `main.tex` |

Check what the directory actually contains; some assets may depend on class or
style files installed elsewhere. Do not label a community asset an official
current template without checking its provenance.

## Conversion

Start from the complete target template in a new output directory unless an
in-place migration was requested. Migrate content, figures and verified
bibliography, adapting macros as needed; do not merge old and new preambles.
Preserve relevant self-citations and follow the target's anonymity rules.

Adjust content to the verified page budget by tightening prose or moving
supporting detail. Do not hide adverse evidence or shrink essential labels to
meet a limit. Required sections, disclosure and resubmission statements come
from the official policy, not a hard-coded conversion table. Rebuild figures
when their inclusion width changes and inspect the resulting page layout.
