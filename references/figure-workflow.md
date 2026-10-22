# Method figures: narrative, TikZ construction and QA

Method schematics for machine-learning papers, authored as TikZ and gated
mechanically before delivery.

This is the self-contained method-figure module of ml-paper-writing. It includes
construction rules, templates, visual references and mechanical checks; no
separate figure skill is required. Read this module for method diagrams only.
Measured plots use the plotting route in style-conventions.md.

Resource paths in prose and commands are relative to the ml-paper-writing skill
root unless linked. Run the bundled QA script by its absolute path when working
in a manuscript directory; pass the figure source path explicitly. The shell
runner requires Bash, Python 3, XeLaTeX and a PDF-to-PNG renderer. If Bash is
unavailable, run the same six stages directly using the bundled Python helpers,
XeLaTeX and a renderer; report any stage that could not run.

## Narrative → design contract

Read the live manuscript, method equations/algorithm, existing figures/README,
figure source/design record and git state. State the contribution from that
evidence. For a proposed revision, identify which variant the diagram depicts
and which variant the experiments evaluate.

Decide whether the job is a whole-method overview, a local mechanism, a control
comparison, or measured evidence. One figure has one primary task. Freeze the
claim, reading path, hero, language, shape roles, edge legend, style and print
envelope using the contract below. Preserve canonical method names.

Before writing coordinates, explain the composition: meaningful regions,
alignment groups, repeated structures, what changes between branches, and the
main/secondary routes. Keep this in the existing design record or source comments;
do not require a separate brief/spec/plan document trio. In a comparison, keep
the shared structure stable and make the actual changed field easy to locate.
Design from the mechanism; references guide density and restraint, not content.

Check the final figure against the manuscript's equations and algorithm. A
PNG-only reviewer cannot establish semantic agreement. Inspect the compiler log
for overfull boxes as well as the mechanical findings. Computed foreach elements
may be skipped by instrumentation: their named parent must enclose the full
repeated object. Source naming alone is not proof of coverage.

## External lessons and limits

FigGenie contributes content-derived composition plans, stable repeated layouts
with highlighted differences, and inspecting real print-size output. Its SVG/PPTX
pipeline, separate JSON spec, mandatory brief approval, corpus statistics and
thresholds are not imported. Provenance lives in [sources.md](sources.md).

## Why this exists

Most "make me a figure" workflows produce something that compiles and still
embarrasses you. The failures are not mysterious, and they split cleanly in two:

- **Mechanical defects** — text overlapping, labels crossing lines, type too
  small once the figure is scaled to a column, arrowheads clipped at the border.
  These are *objectively checkable* and this skill checks them.
- **Design defects** — no focal point, a wall of equal boxes, colour carrying no
  meaning, a figure that displays rather than argues. These are *not* checkable,
  and this skill encodes conventions plus a review pass instead of pretending
  otherwise.

The split is the whole design. Every rule below either (a) a script enforces, or
(b) names the concrete defect it prevents. A rule that can do neither does not
belong in this skill.

A documented finding worth internalising: static checkers are a **floor, not a
ceiling**. Measured on a real paper figure, not a hypothetical: a version that
broke visibly under a one-line edit still returned `CLEAN`, because most of its
elements were anonymous nodes and raw `\draw` paths that the geometry pass never
looked at — it checked **10 nodes out of ~30 elements**. Named and rebuilt by
construction, the same figure exposes **37 nodes** and the gate starts finding
real defects. Passing `qa.sh` means "no known mechanical defect", never
"good figure" — and it only means that much if everything has a name.

## Workflow

### 0. Classify the request

| Request | Do this |
| --- | --- |
| New figure from a paper section | Steps 1 → 5 |
| Fix collisions in an existing figure | Start at 3, but read 1 to check the contract still holds |
| Restyle, match a reference, or respond to rejected aesthetics | Reopen the design contract in 1; do not preserve the rejected palette or composition by default |
| Audit a finished figure | Use [method-figure/review-checklist.md](method-figure/review-checklist.md) only; do not redraw unasked |

Ask at most two or three questions, batched. Everything else: assume, state the
assumption in one line, keep it cheap to reverse.

For a Figure 1, method overview, or a reference-inspired restyle, read
[method-figure/overview-first.md](method-figure/overview-first.md) before choosing
labels. An overview should introduce the mechanism before asking the reader to
learn its notation. Default to short concrete labels and visual objects, with no
paper-specific equations or indexed variables. Familiar operators such as `+`
may stay when they explain a real operation. Technical detail figures and
explicitly requested mathematical diagrams can use necessary, defined notation.

When the user supplies a visual reference, its visual grammar takes precedence
over a default palette or a previous user's style preference. Read
[method-figure/reference-led-llm.md](method-figure/reference-led-llm.md) to extract
that grammar and map manuscript terminology and semantic graphic objects before
drawing. A reference-led restyle must be visibly recognizable as such, not just
pass the collision checker.
That route includes a [bundled user-supplied reference PNG](method-figure/images/role-play-judge-moderator.png);
inspect the actual image when matching that style. For numerical selection,
consider probabilities inside token cells rather than empty masks.

### 1. Freeze the design contract before drawing anything

Write these down *first*. Skipping this step is the single largest source of
redraw, because a layout mistake costs one eraser stroke on paper and an hour of
coordinate surgery on screen.

```
FIGURE CLAIM   one sentence the reader must understand afterwards.
               Not a module list. If you cannot write it, the figure has no job.
READING PATH   left-to-right spine | two-branch comparison | hero + satellites |
               cycle. Pick one; it determines the whole layout.
HERO           which element is the novelty, and how it is visually heaviest.
               Novel parts get area; standard parts get compressed.
LANGUAGE       intended reader; plain-language names for the data and actions.
               For an overview, justify any notation that survives simplification.
               Preserve the manuscript's named methods, stages and decisions;
               simplify their explanations, not their identities.
STYLE FAMILY   flat journal (default) | soft card (only on explicit user
               request — UI-mimicry in TikZ reads as AI-generated; see
               method-figure/polish-style.md §1). Same family paper-wide.
ROLE -> SHAPE  what is a box, what is a strip, what is a glyph, what is a plot.
EDGE LEGEND    what each line style and colour MEANS. Anything non-solid must be
               named in the legend or the caption.
ENVELOPE       print width, aspect ratio, and the resulting font-size budget.
```

Two quality-bar questions the contract must also answer, asked before drawing
and again before delivery:

- **The 5-second question.** What will the reviewer remember in five seconds?
  A figure with no memorable element is not worth delivering. The memorable
  thing should be the HERO above, stated before any pixel is placed.
- **The cover test.** Cover the caption — the claim must still be readable.
  Cover any panel — information must be lost that no other panel carries.
  An element that passes neither cover test is decoration; delete it.
- **The first-read test.** Without reading the paper or a notation legend, can
  someone name the input, the distinctive operation, and the output? Replace
  unfamiliar symbols with concrete labels or objects; do not add a symbol legend
  to rescue an otherwise opaque overview.

Two rules that do most of the work:

- **One figure, one job.** If you find yourself redrawing the same connector a
  third time, the figure is being asked to do two jobs. Split it.
- **The figure must look different from the baselines' figures.** If your method
  diagram is silhouetted the same as prior work, readers conclude there is no
  novelty. Differentiate the novel module or zoom into it.

One law that separates a method figure from a generic flowchart, and which
applies in both style families:

- **Real method object > text label.** If you can draw the distribution, do not
  write the word "distribution". Embed the actual object — the token strip, the
  mini full-vocabulary distribution, the paired replay cards with the one
  differing field, the weight profile, the before/after with the metric on the
  transform arrow. A hero made only of labelled boxes is the most-penalised
  pattern in method-figure review.

### 2. Write the TikZ by construction

Read [method-figure/by-construction.md](method-figure/by-construction.md) before the first `\node`. The short version:
define spacing once, place by relative positioning, connect by node anchors, size
containers with `fit`, wrap text with `text width`.

This is not style advice. Absolute coordinates mean one edit breaks five places;
relative construction means the same edit reflows cleanly. It is the difference
between a figure you can maintain and one you have to redraw.

### 3. Run the mechanical gate

```bash
scripts/method-figure/qa.sh figure.tex --venue iclr
```

Six stages, cheapest first:

1. **static lint** — source hazards, no TeX needed (`lint_static.py`)
2. **instrument + compile** — must build standalone
3. **glyph gate** — xelatex fails *silently* on an unresolved font
4. **geometry** — exact node boxes: overlaps, tight gaps, off-canvas
5. **effective type size** — pt at the real print width, not on your screen
6. **render a PNG** — for the eyes that must still look at it

Fix every `HARD`. Warnings are smells: confirm each in the render before acting,
because a linter that cries wolf gets ignored and then protects nothing.

The geometry pass uses TikZ's own bounding boxes, so it has **no false positives**
from glyph shapes or anti-aliasing — unlike raster-based checkers, which need
lists of known false-positive families to stay usable.

### 4. Review what the machine cannot see

Read [method-figure/review-checklist.md](method-figure/review-checklist.md) and answer every item with evidence from
the actual render. Then:

- **A fresh, independent pass.** Spawn a blank-context agent to read only the
  rendered PNG adversarially ("there are defects, find them"). A generator
  re-reading its own output is not a review — the blindness is structural: you
  cannot see the gap between what you meant to draw and what rendered.
- **Triage the known false-positive families** (below) rather than trusting or
  dismissing the list wholesale.
- **The user is the final gate.** Report what you checked and what remains
  uncertain; do not declare a figure publication-ready on their behalf.

### 5. Deliver

```
figures/<name>.tex     source, standalone-compilable
figures/<name>.pdf     the asset included by the paper
figures/<name>.png     render for review
```

Include with `\includegraphics[width=\linewidth]{...}` — never a hard-coded inch
value. End with a one-line assumptions summary:

> Assumptions: light palette, single-column width, 4 stages — say the word to change any.

## Hard rules

Never violate. Each names the defect it prevents.

| Rule | Prevents |
| --- | --- |
| `\documentclass[tikz]{standalone}` with `border=` ≥ 10pt | A figure that cannot be QA'd alone; clipped labels and arrowheads |
| No bare `scale=` — use `transform shape` or shrink spacing | Gaps shrink while text does not, silently creating overlaps |
| Labels use `text width` + `align`; boxes declare explicit dimensions | Labels that grow past their box and eat the neighbour |
| Never `node {label}` directly on a `--` path | Text sitting on the line; the most reliable silent collision in TikZ |
| Connect named nodes by anchor: `(a.east) -- (b.west)` | Tips landing inside boxes; lines vanishing under fills |
| `\usetikzlibrary{bending}` whenever a path curves | Arrowheads visibly misaligned on every bend |
| Colours by palette name from one block at the top | Ad-hoc hex that cannot be re-themed and drifts between figures |
| One meaning per visual code | Dashed used for two different things, which is the root of "the schematic is confusing" |
| Semantic node names (`(enc)`, `(layer1)`) | Un-editable figures; anonymous nodes cannot be geometry-checked |
| **Name every element**, and make any repeated run (a strip of tiles, a row of cells) a real node even if you then draw into it | A gate that sees 10 of your 30 elements is not coverage. A bare `\fill` run is invisible to the checker, so it can hang half a tile into its neighbour and pass |
| Background layers behind every fill they sit under | Content painted over by a container fill |

## Known false-positive families

Do not chase these; confirm them in the render and move on.

- Rotated and math-heavy labels report larger or misplaced text boxes.
- Dense grids, heatmaps and matrix cells report as mutual overlaps.
- Legitimately nested containers (a zone enclosing its children) are excluded by
  the containment exemption, but a zone that *cuts across* an unrelated node is a
  real defect and is correctly reported.
- Small tight gaps between an element and its own arrow are reported as `TIGHT`
  advisories at 0.19–0.20cm.
- A node that is the outermost element of the picture differs from
  `current bounding box` by exactly its `outer sep` (0.2pt = 0.007cm), which used
  to report as `OFFCANVAS`. `check_geometry.py` now carries a 1pt tolerance for
  this. If you see `OFFCANVAS` at a gap larger than that, it is real.
- A zone title that is simply painted over its zone reads as an overlap. This is
  not a checker flaw to suppress — it is a construction choice to change: place
  the title first and pass it to the zone's `fit`, and the containment exemption
  applies as intended.

## What this skill cannot see

Stated plainly so it is not mistaken for coverage.

- **A line crossing a label.** Only nodes are instrumented; paths are not. Check
  this by eye in every render. (To measure a suspicious connector, wrap it in
  `\begin{scope}\pgfresetboundingbox ... \qapicture\end{scope}` and read its box.)
- **Whether the figure argues the right thing** — that is step 1, not a script.
- **Whether a composition has a focal point**, or reads as a card wall.
- **Cross-figure consistency** with the rest of the paper.
- **Semantic contradictions** between a panel's numbers and the text.

## Reference map

| File | Read when |
| --- | --- |
| [method-figure/by-construction.md](method-figure/by-construction.md) | Before writing any TikZ. The idioms that make a figure editable |
| [method-figure/constraints.md](method-figure/constraints.md) | When a rule needs justification, or you hit a defect not listed here |
| [method-figure/ml-conventions.md](method-figure/ml-conventions.md) | Choosing budgets, palettes, arrow semantics, and what marks frozen vs trainable |
| [method-figure/polish-style.md](method-figure/polish-style.md) | Every figure. The style families (flat journal vs soft card), the palette/typography/shadow kit with exact numbers, the composition laws, and the failure modes that make a figure look like default TikZ |
| [method-figure/overview-first.md](method-figure/overview-first.md) | Figure 1, accessible method overviews, reference-inspired pastel schematics, or feedback that a figure has too many symbols or too much text |
| [method-figure/reference-led-llm.md](method-figure/reference-led-llm.md) | A supplied reference, rejected palette, more LLM-style graphic elements, or terminology alignment with the manuscript |
| [method-figure/cv-transformer-styles.md](method-figure/cv-transformer-styles.md) | When the user asks for ViT/Swin/Transformer/CV architecture styling, patch/token/window-attention diagrams, or a more polished CV-paper look |
| [method-figure/venues.md](method-figure/venues.md) | Setting the canvas width and aspect for a specific venue |
| [method-figure/review-checklist.md](method-figure/review-checklist.md) | Step 4, every time |
| [method-figure/tikz-template.tex](method-figure/tikz-template.tex) | Starting a new flat-journal figure; copy the preamble and styles |
| [method-figure/tikz-template-soft.tex](method-figure/tikz-template-soft.tex) | Starting a new soft-card figure (modern LLM/RL-report look) |
| [method-figure/exemplars.md](method-figure/exemplars.md) | Choosing a composition; analysing what good figures do |
| [method-figure/tooling.md](method-figure/tooling.md) | Export formats, QA-render flattening, and the SVG situation in this environment |

## Attribution

Synthesised from MIT-licensed sources — `0xE1337/thesis-figure-skill`,
`SipengXie2024/superpower-writing`, `ai4paper/apaper-plugin`,
`TAO-QKV/Icarus-Figures`, `opentikz/opentikz`, `Noi1r/tikz-academic`,
`chingswy/Skill-Research-Figure`, `gxCaesar/open-research-skills` — plus
published venue style guides, the pgf-blur and arrows.meta documentation, and
the accessibility literature. `Patrick-Healy/tikz-diagrams-skill` is
**unlicensed** and `anthropics/skills` (canvas-design) informed prompt language
only; neither contributed code or prose. See [method-figure/constraints.md](method-figure/constraints.md) for
per-rule provenance.
