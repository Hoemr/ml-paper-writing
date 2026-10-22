# Constraint catalogue

Every rule here names **the defect it prevents**. A rule that cannot state that
does not belong in the file. `[auto]` means `qa.sh` enforces or reports it;
`[eye]` means only the render can judge it.

Provenance: **S1** = `0xE1337/thesis-figure-skill` (MIT) · **S2** =
`SipengXie2024/superpower-writing` (MIT) · **S3** = `ai4paper/apaper-plugin`
(MIT) · **S4** = `TAO-QKV/Icarus-Figures` (MIT) · **S5** = `opentikz/opentikz`
(MIT code + CC0 content) · **S6** = `Patrick-Healy/tikz-diagrams-skill`
(**unlicensed — ideas only, no code or prose reproduced**) · **V** = venue style
guides · **A** = accessibility literature.

---

## A. Spacing minimums

Verified baseline values. Violating one produces an overlap or a cramped read.

| Element | Minimum | Prevents |
| --- | --- | --- |
| Same-row sibling boxes, x-gap | **1.5 cm** | < 1.0 cm they visibly touch |
| Cross-row vertical gap | **1.2 cm** | Rows reading as one block |
| Zone padding to outermost content | **0.8–1.0 cm** | < 0.5 cm the dashed border cuts the text |
| Zone title to first content row | **0.8 cm** | Title crowding content |
| Legend to nearest content | **0.5 cm** | Legend/panel collision |
| Text to its own box border | **0.25 cm** per side | Long labels "biting" the frame |
| Multi-column in-box gap | **0.3 cm** | Columns merging |
| Label ↔ label | **0.3 cm** | Grazing text |
| Label ↔ line/arrow | **0.3 cm** | A tag riding the line it annotates |
| Label ↔ shape boundary | **0.4 cm** | Text touching a border |
| Bend distance from a node edge | **≥ 1.0 cm** | Sharp bends hugging the box |
| Bend to target frame | **≥ 1.5 cm** | A `rounded corners` arc eats ~0.5 cm |
| Merge-node (⊕/⊗) side clearance | **0.4 cm** | Shaft invisible |

`qa.sh` reports the label/box and box/box classes as `TIGHT` advisories at
whatever `--min-gap-cm` you pass. The rest need the eye. **[auto/eye]**

**Do not shrink the text to fit.** Widen the box, shorten the label, or move the
element. Shrinking text is the one fix that always makes a figure worse.

---

## B. Arrow geometry

The most frequent defects in a review loop are all arrow defects.

### Tip size must track shaft length

Default `Stealth` = 5pt + 1.5 × line width = **6.5pt**, plus shorten. On a 15pt
(0.5 cm) arrow that leaves **5.5pt of visible stem** — it reads as a floating
head. **Below 1.5 cm you must switch to a short-tip style.** **[auto]**

Line width is the knob, not tip scale:

| Role | Line width |
| --- | --- |
| Primary flow | 1.0pt |
| Emphasis | 1.6pt |
| Secondary / detail | 0.6pt |

Tuning `-{Stealth[scale=0.75]}` treats the symptom; four rounds of iteration
converged on "fix the line width, let the tip follow". Use the
`length=5pt 1.5` syntax so the tip scales automatically.

Note: `shorten` does **not** support the dual-argument syntax — use absolute pt.

### Direction sense

A reader decides arrow direction in about a tenth of a second. If the visual flow
disagrees with the logical flow, the figure feels wrong even when it is correct.

- **Exit anchor faces where the target is.** Target below → leave from `.south`;
  right → `.east`. Corner anchors (`.south west`) are forbidden; they look
  unnatural.
- **The classic silent bug: a midpoint that overshoots the target.**
  In `(A) -- (mid) -- (B)`, if `mid` is past `B` along the axis, the last segment
  reverses and the tip points backwards. Every mid-path point must lie strictly
  between its endpoints, or share x or y with the previous point. **[auto via static lint on obvious cases]**
- **Fan-out is a tree, never a broom.** Scattering N diagonal lines from one
  anchor is the most recognisable amateur tell. Trunk from the source's exact
  centre, a horizontal crossbar, then vertical branches. The trunk carries no
  arrowhead; the branches do. Hand-typing the crossbar's x is the number-one
  cause of a crooked tree — derive it with `|-`.
- **Fan-in mirrors it.** N sources → spine → one tip at the target.
- **Junction dots must not be stabbed by tips.** Around a dot, all adjacent lines
  are plain `\draw` with no arrowhead; the tip goes only on the segment reaching
  a bordered target. **[eye]**

### Routing

- **Straight if you can.** Same x → vertical. Same y → horizontal. Only bend when
  both differ, and every bend needs a reason (avoiding an obstacle).
- **Orthogonal L-shapes only; no diagonals.** Bends get `rounded corners=5pt` —
  one canonical value.
- **Never let a connector cross a node box.** PGF does no obstacle-aware routing:
  `(A.south) |- (B.west)` runs its horizontal segment straight through `B` when
  A's x falls inside B's x-range. **[eye, or arithmetic if anchors are instrumented]**
- **`rounded corners` on a straight `--` path emits ghost arcs at both ends.**
  Apply it only to paths with a real corner. **[auto]**
- **Dashed/auxiliary lines must not cross a zone border.** Exit the node, transit
  outside the border, arrive. A rail must sit ≥ 1.0 cm outside the border.
- **Direct beats detour.** If source and target share a column, do not take the
  right-hand rail. "All feedback lines take the right rail" is a recognisable
  machine habit.
- **Route around, don't mask.** Never hide a line that crosses a label with an
  opaque white box; re-route or move the label. **[V]**
- **`|-` between points sharing an axis** yields a redundant segment; use plain
  `--`. **[eye]**

### When arrows are the wrong tool

- Sub-blocks that are flush (gap < 1pt) need **no arrows**: adjacency plus reading
  order already implies flow. Arrow only at stage granularity.
- 1-to-N broadcast is a fork with N one-way arrows, never a double-headed curve.
  `{Stealth}-{Stealth}` is reserved for genuine bidirectional interaction.
- Compressed multi-step processes must be **annotated** (`{4,5}`, "(2 substeps)")
  plus a caption note. Silent compression is visual lying.

---

## C. Typography and print size

### Effective size is a ratio, not a number

```
effective_pt = design_pt × (print_width / canvas_width)
```

Every 10% the canvas exceeds the print width costs 10% of the type size. A figure
authored on a 190 mm canvas and printed at 140 mm loses 26% — a 9pt label becomes
6.6pt. **[auto: `check_fontsize.py`]**

| Floor | Value |
| --- | --- |
| Working floor, ML figures | **7 pt** |
| Primary labels | **8 pt** |
| Absolute limit, venue production | **5 pt** |

Type scales that work: body/axis 10–11pt, secondary 8–9pt, annotations 7–8pt.

### Size rules are two-sided

A rule that only gives a lower bound is a **one-way ratchet**. "Not smaller than"
invites enlarging, and enlarging is pure gain under the rule system — until the
figure is cramped. This was learned the hard way: bumping a document base from
10pt to 11pt raised body text 23% and titles 38%; every box was individually
clearer and the whole figure became tight.

For any "at least X" rule, state the ceiling too. Related ceilings that matter:
a label should occupy ≤ 80% of its box's inner width and ≤ 60% of its inner
height; a panel title bar ≤ 20% of panel height. **[eye]**

### Other typography rules

- **Relative sizes, not absolute.** `\small` / `\footnotesize` survive a
  paper-wide size change; `\fontsize{8.5}{10}` does not. **[auto]**
- **Match the host paper's base size.** `standalone`'s underlying class supports
  only 10/11/12pt — **any other option is silently ignored**, leaving an
  `Unused global option(s)` line and a figure whose text is the wrong size. For a
  9pt paper, pass `class=IEEEtran`. Better still: `\input` the `tikzpicture`
  into the paper so it inherits everything. **[auto detects the docclass option]**
- **Never scale a finished figure to fit.** `\resizebox`, `every node/.style={scale=}`,
  `transform shape`, and `\includegraphics[width=...]` on a text-bearing figure
  all change the effective font size silently.
- **Sentence case for labels.** Display-style caps only for canonical names
  (`XGBoost`, `GPT-5.2`) — never blind-apply title-casing. **[eye]**
- **Rotated labels** are harder to read and their bounding boxes defeat geometric
  checking. Prefer horizontal; if you must, keep them short. **[auto warns]**
- **No sentences in boxes.** In-figure text is ~30% shorter than authors want;
  the rest belongs in the caption. **[eye]**

---

## D. Colour

- **One palette block at the top, referenced by name.** No inline hex outside it.
  `[auto]`
- **Default to Okabe–Ito** (`#E69F00 #56B4E9 #009E73 #F0E442 #0072B2 #D55E00 #CC79A7`),
  the standard colourblind-safe scheme (Wong, *Nat. Methods* 2011). **[A]**
- **Several Okabe–Ito colours do not reach 3:1 contrast on white** — notably
  yellow and sky blue. For thin lines or small glyphs on white, use a 5-colour
  subset and add marker/line-style redundancy. Then audit the actual render.
- **Fills get tints, strokes get shades.** `fill=accent!12`, `draw=accent!75!black`.
  Adjacent blocks then read as distinct without shouting.
- **≤ 6 colours: 1 accent + 2–3 primary + 1–2 secondary + grey.** 5+ saturated
  hues is the amateur tell.
- **Never rely on colour alone.** Pair every distinction with shape, line style,
  pattern, or a direct label. Red–green defects affect up to 8% of men; across
  three male reviewers the chance at least one is colourblind is ~22%. **[A]**
- **Banned:** rainbow/jet/hsv (perceptually non-uniform), neon, light yellow on
  white, a sequential ramp repurposed as categorical colours. **[V]**
- **Grayscale survival is the test.** Desaturate and confirm every distinction
  survives. Some venues state it outright. **[eye]**
- **One mapping, paper-wide.** Never let the same colour mean different things in
  two figures, and don't let a neutral baseline out-shout the hero.

---

## E. Layers and z-order

Draw order is code order. The canonical stack, bottom to top:

1. zone background fills
2. connectors
3. boxes, text, labels
4. titles, legends, annotations

- **Containers must be on the background layer**, declared *after* the nodes they
  `fit`, so they sit behind. **[eye]**
- **The trap two independent projects hit:** the background layer sits behind node
  fills, so content *inside* a filled box — a mini-network, heatmap cells — must
  be drawn on the **main** layer, edges first, marks second, or the fill paints
  over it.
- **`\pgfonlayer` is the environment name** — not `pgfonbackgroundlayer`, which
  errors but still emits a broken PDF.
- Zone styles carrying `inner sep` can silently fail inside `pgfonlayer`; inline
  the style instead.

---

## F. Standalone and compilation traps

| Trap | Symptom | Rule |
| --- | --- | --- |
| Sub-preamble not read | "works standalone, dies in the paper" for `\usetikzlibrary` | Load libraries in the **main** preamble, or `\usepackage[subpreambles]{standalone}` |
| Missing font | **Silent** — blank/tofu glyphs, no error | `grep -c "Missing character" *.log` must be 0 **[auto]** |
| `\texttt{}` with non-ASCII | Missing glyphs | Mono fonts cover ASCII only **[auto warns]** |
| `bending` not loaded | Arrowheads misaligned on every curve | Always load it **[auto]** |
| Node name with a dot | `No shape named 'pipe16'` | Alphabetic names only **[auto]** |
| Colour *name* looped through `\foreach` | `Undefined color 'barGreen '` (trailing space) | Unroll, or loop a numeric tint instead **[auto]** |
| `scale=` without `transform shape` | Coordinates shrink, text does not → overlaps | **[auto]** |
| Stale externalized figures | Looks right, is out of date — the nastiest class | Don't rely on `externalize` for figures under edit |
| `\pgfplotset{compat=}` missing | Breaks after a TeX distribution upgrade | Declare it explicitly when using pgfplots |
| `\newlength{\z1drop}` | `Missing \begin{document}` — a control-sequence *name* may not contain digits, so `\z1drop` is parsed as `\z` followed by the text `1drop`, which TeX then tries to typeset in the preamble | Length-register names: **letters only** (`\onedrop`). Node names may contain digits; register names may not |
| `\setlength{\x}{.5\dimexpr\a+\b\relax}` | `Illegal unit of measure` — a numeric factor may not precede `\dimexpr` | Put the factor on a register: `\dimexpr.5\a+.5\b\relax` |
| `\global\pgfmathsetlengthmacro{...}` | `You can't use a prefix with \begingroup` | `\global` attaches to an *assignment*, not to a macro that opens a group. Declare a register and use `\global\reg=\dimexpr...\relax` |
| `\pgfmathsetlengthmacro` inside `\pgfextra` | The macro is group-local and is gone by the next statement — the failure surfaces later and elsewhere as `Undefined control sequence` | Same fix: write into a declared register |
| `([yshift=1cm]a |- b)` | **Silently wrong position.** An option list and a line-crossing operator cannot be combined in one coordinate; TikZ drops the operator instead of erroring, so the point quietly takes `a`'s x and y | Split into two coordinates: `\coordinate (p) at (a -| b);` then `[yshift=1cm]p` |
| `(a |- b)` read as "x from a" | Half of all routing bugs | `(a |- b)` is **a's x with b's y**; `(a -\| b)` is **b's x with a's y**. Say it out loud before typing it |

---

## G. What "publication-grade" looks like

The observable differences. The left column is what reviewers read as amateur
before parsing a single word.

| Amateur | Publication-grade |
| --- | --- |
| Software-default font, sizes inconsistent between panels | One deliberate type scale, consistent across the paper |
| Boxes off by a few px; text touching or overflowing borders | Everything on a grid; labels centred with real padding |
| Angled arrows where an orthogonal route exists | Orthogonal routing, one arrowhead style |
| Sentences inside boxes | Short labels; detail in the caption |
| Default colormap, many saturated hues, colour-only encoding | ≤ 3 families + neutrals, redundant shape/line encoding |
| 3D bevels, drop shadows, gradients, glow, clip art | Flat vector; quality signalled through order and restraint. **Style-family caveat:** a *named* family with a disciplined decoration budget is legitimate — `soft card` (modern LLM/RL-report look: 4–6pt radii, one blur shadow per card at ~30% opacity, ≤10% gradients) is sanctioned and specified in `polish-style.md`; what is banned in every family is *undisciplined* decoration — default hard `drop shadow`, rainbow gradients, icon per panel, mixed corner radii |
| 15+ modules, 30+ arrows | 5–12 modules, 6–18 arrows |
| Screenshot pasted at low DPI | Vector, text still editable |
| Every figure its own style | One template across the paper |
| Pipeline looks identical to the baseline's | Novel module visually differentiated, standard parts compressed to grey |

The last row is the most ML-specific and has no analogue in journal-style guides:
**if it looks the same as prior work, readers assume there is no novelty.**

**Negative rules.** No equal-weight card grids by default (give the hero ≥ 1.5–2×
the area). No panel without a unique inferential role — apply "what inference
disappears if I delete this?". No decorative frames to signal grouping; use
whitespace and alignment. No title inside the figure (an explicit ICML rule — the
caption does that job). No legend when direct labelling works. No mixed
abstraction levels in one figure (neuron + layer + block).

---

## H. Sourcing and licensing

| Source | License | Used for |
| --- | --- | --- |
| `0xE1337/thesis-figure-skill` | MIT | by-construction idioms, hard constraints, arrow canon, lint pipeline design, review checklist; hierarchy levers, cover test, anti-slop gate (polish layer) |
| `SipengXie2024/superpower-writing` | MIT | arrow patterns, review-gate design, figure rhetoric, print-width gate |
| `ai4paper/apaper-plugin` | MIT | font-size derivation, grayscale-first stroke hierarchy, tap-junction rules |
| `TAO-QKV/Icarus-Figures` | MIT | mechanical-floor vs judgment-pass split, "bare boxes and arrows" gate, real-method-object red line, hero-area doctrine |
| `opentikz/opentikz` | MIT (code) + CC0 (content) | palette discipline, icon/label separation, padding budget, semantic node naming, compile-before-return, ambiguity protocol |
| `Noi1r/tikz-academic` | MIT | saturation-hierarchy doctrine, font ladder, fill/stroke/text pairing, style-debt list (polish layer) |
| `chingswy/Skill-Research-Figure` | MIT | card grammar, 10-role palette tokens, copy-paste style library (polish layer) |
| `gxCaesar/open-research-skills` | MIT | style profiles, three-pass refinement protocol (polish layer) |
| `anthropics/skills` (canvas-design) | MIT | craftsmanship prompt language only (polish layer) |
| `Patrick-Healy/tikz-diagrams-skill` | **none — all rights reserved** | defect *categories* and the render-and-inspect principle only |
| Wong, *Nat. Methods* 8:441 (2011); Okabe–Ito | published | colourblind-safe palette and contrast caveat |
| Rougier, Droettboom & Bourne, *PLOS Comput Biol* 10(9) (2014) | published | one-message rule, "do not trust the defaults", colour-means-meaning |
| pgf-blur (CTAN) / arrows.meta docs | published | verified shadow recipe and geometric-tip options |
| ICML / NeurIPS / venue style guides | published | no in-figure title, caption form, measured widths |

MIT status of the polish-layer sources reflects the repositories' LICENSE files
as read during synthesis; the prose in `polish-style.md` is original.

Earlier MIT releases of `opentikz` and third-party notices are documented in that
project's `NOTICE`; upstream MIT components retain their original terms.
