# Tooling, export, and what does not work here

## The gate

```bash
scripts/method-figure/qa.sh figure.tex --venue iclr [--min-gap-cm 0.4] [--keep]
```

| Stage | Script | Needs |
| --- | --- | --- |
| static lint | `lint_static.py` | python3 only |
| instrument + compile | `instrument.py` | python3 + a LaTeX engine |
| glyph gate | — (grep on the log) | — |
| geometry | `check_geometry.py` | python3 only |
| type size | `check_fontsize.py` | python3 only |
| render | `qlmanage`, `sips`, or `pdftoppm` | macOS ships the first two |

**No third-party Python packages are required.** This is deliberate: the usual
approach (extract text boxes from the PDF with PyMuPDF) needs an install that may
not be available, and a QA gate that silently skips is worse than no gate.

## Rendering PNGs: transparency is the trap

A standalone TikZ PDF has **no painted page background**. How a rasteriser
treats that decides whether your QA preview is reviewable:

- **`qlmanage -t -s 2400 -o <dir> fig.pdf`** (preferred) — writes
  `fig.pdf.png`, flattened onto white. Shadows and gradients render intact.
- **`sips -s format png ...`** — keeps the page as an **alpha channel**.
  Viewers that composite transparency onto black show a black figure; JPEG
  output matts to white instead. `\pagecolor{white}` does land in the PDF but
  sips still rasterises the page as transparent (verified on macOS 25).
- If sips is the only option and you need an honest PNG, paint the page as
  *content* at the end of the `tikzpicture`:

```latex
\begin{scope}[on background layer,overlay]
  \fill[white] ($(current bounding box.south west)+(-12pt,-12pt)$)
    rectangle ($(current bounding box.north east)+(12pt,12pt)$);
\end{scope}
```

`overlay` keeps the fill out of the bounding box, so the page size is
unchanged; the +12pt covers the standalone `border`. This recipe lives in
`references/method-figure/polish-style.md` §7.

## How the geometry check works

Most tools rasterise the PDF and guess at text positions from pixels. That
approach carries a permanent list of false-positive filters — glyph shapes,
anti-aliasing, drop shadows, heatmap cells — because pixels are lossy evidence.

This skill asks **TikZ itself** instead:

```latex
\path let \p1=(#1.south west), \p2=(#1.north east) in
  \pgfextra{\immediate\write\qafile{__QA NODE #1 \x1 \y1 \x2 \y2}};
```

`instrument.py` injects that before every `\end{tikzpicture}`, so the dump is
exact. Consequences:

- **No false positives** on the overlap test — the boxes are the real boxes.
- Reports in TikZ coordinates, so distances are directly comparable to the
  spacing minimums in `constraints.md`.
- Requires nodes to have **literal names**. Anonymous nodes and nodes generated
  inside a `\foreach` cannot be checked, which is one more reason to name nodes
  semantically.

Known limitation, stated in `references/figure-workflow.md` too: **paths are not instrumented**, so a
line crossing a label is not detected. To measure a specific connector, wrap it:

```latex
\begin{scope}\pgfresetboundingbox
  \draw[flow] (a) -- (b);
  \qapicture            % dumps THIS path's bounding box
\end{scope}
```

## Building the figure

```bash
xelatex -interaction=nonstopmode -halt-on-error figure.tex
```

Use `xelatex` if the figure contains any non-ASCII text; otherwise `pdflatex` is
fine and faster. Keep the engine consistent with the paper's.

## Including in the paper

```latex
\includegraphics[width=\linewidth]{figures/figure.pdf}
```

Never a hard-coded inch value, and never a text-bearing `\resizebox` — both
change the effective type size silently. Better still, `\input` the
`tikzpicture` directly so the figure inherits the paper's fonts and base size.

## SVG export: does not work in this environment

Requested and investigated; reporting the result honestly rather than shipping a
broken flag.

`dvisvgm` 3.6 is installed, so the route looks available. It is not:

| Route | Result |
| --- | --- |
| `latex` → DVI → `dvisvgm` | **"105 PostScript specials ignored"**; output has **zero `transform` attributes**, so every glyph and shape is drawn at the origin, piled on top of itself |
| `xelatex -no-pdf` → XDV → `dvisvgm` | **"1206 PDF specials ignored"**; same pile-up |
| `dvisvgm` on the PDF | needs Ghostscript; `gs` is not installed |

Reproduced on a **three-box minimal figure**, so this is not a property of any
particular diagram — this `dvisvgm` build does not position TikZ output at all.

What would fix it, in order of least effort:

1. **`brew install poppler`** → `pdftocairo -svg figure.pdf figure.svg`. Converts
   from the PDF, which is already correct, so it sidesteps the DVI/XDV problem
   entirely. This is the recommended fix.
2. **`brew install librsvg`** → `rsvg-convert -f svg figure.pdf -o figure.svg`.
3. **Inkscape** → `inkscape figure.pdf --export-type=svg`.

Also note a tradeoff that applies even once SVG works: exporting text as
**outlines** (dvisvgm's `--no-fonts`) renders identically everywhere but is no
longer editable in Inkscape or Illustrator; keeping text live makes it editable
but lets a viewer substitute fonts, which can split multi-word labels. For a
paper, the PDF is the artefact that matters and SVG is a slide/web convenience —
so choose per use, and keep the PDF canonical.

**The PDF is the deliverable.** It is what `\includegraphics` consumes, it is
vector, and it is verified.
