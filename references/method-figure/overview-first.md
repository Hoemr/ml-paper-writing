# Overview-first method figures

Use this guide for Figure 1, method overviews, and reference-inspired schematics.
Its purpose is to make the mechanism understandable before the reader learns the
paper's notation. It is not a ban on mathematics in technical detail figures.

For a supplied visual reference or an explicit request for LLM-style graphic
objects, also use [reference-led-llm.md](reference-led-llm.md). Preserve canonical
method/stage names from the paper; short labels are not permission to rename them.

## 1. Translate the method before drawing

Write one sentence containing the input, the distinctive operation, and the
output in ordinary language. Then assign a short noun to each data object and a
short verb phrase to each operation. Keep terminology consistent with the paper,
but do not import its subscripts, abbreviations, and equations into every label.

For an overview, start with **zero paper-specific equations and variables**.
Retain notation only if it saves the intended reader effort and is needed to
understand the mechanism. A familiar plus sign for actual addition is useful;
an indexed advantage formula usually belongs in the method text. A user asking
for fewer symbols is asking for less decoding, not just fewer displayed equations.

Examples of semantic translation, not universal replacement rules:

| Mathematical label | Overview label or object |
| --- | --- |
| Policy symbol with parameter subscript | Policy |
| Indexed realized and matched future variables | Own future / Matched future, with parallel strips |
| Indexed log probabilities | Scores, next to aligned score strips |
| Difference between two token scores | Compare token scores |
| Outcome multiplication and normalization formula | Use outcome sign; Center and scale |
| Indexed centered correction | Token credit, with a signed profile around zero |
| Final advantage equation | A plus junction between the two actual inputs, followed by Learning signal |

Keep the construction faithful: do not rename an uncalibrated score as a
probability, an alignment operation as a verifier, or a signed correction as an
always-positive weight. Simplify the language, not the method.

Aim for labels of roughly 1–4 words. Use two short lines when necessary. Avoid
replacing one equation with a sentence inside a box. Definitions, exact
normalization, exceptions, and loss details belong in the caption or Methods.
The caption explains the picture; it should not become a displaced derivation.

## 2. Let shapes do the explanatory work

- Draw sequences as tiled strips, scores as aligned cells or small profiles, and
  computation as bounded modules. Label what the object means; a bare strip is
  not automatically self-explanatory.
- In a comparison, keep the two branches aligned and visually identical except
  for the field that actually changes. Show shared computation once. State the
  shared context in one short label instead of repeating a field list twice.
  Keep compared outputs distinct until the comparison module, using separate
  input ports when a shared incoming edge would obscure the two operands.
- Give the distinctive operation more space than routine sampling or updating.
  A paired comparison should remain recognizable when all text is blurred.
- Keep the entry and exit obvious. A secondary reward or control path may bypass
  the main comparison if the method requires it; label the path and rejoin it at
  an explicit operator. Do not add arrows for every dependency already stated
  clearly by a shared-context label.
- Use a signed profile only when the quantity can be signed. Schematic tiles and
  bars must not look like measured results; say they are schematic in the caption.

## 3. Reference-inspired flat pastel style

When the user likes a reference, extract its visual grammar: reading direction,
grouping, shapes, color roles, density, line weights, and emphasis. Transfer those
choices to the actual method. Do not transplant irrelevant agents, layers,
emojis, or repeated stages. Do not fade an essential operation just because a
reference fades its continuation.

For the light academic schematic used in this workflow, a useful starting set is:

| Role | Appearance |
| --- | --- |
| Page / text and arrows | White / near-black `#222222` |
| Stage grouping | Very pale gray `#F8F8F8`; thin gray dashed outline `#959595` |
| Two compared views | Pale blue `#D8E5FA` / pale pink `#F4D9D6` |
| Shared target tokens | Cream `#FFF3CE` |
| Computation | Pale green `#DEECD7`; slightly stronger green border `#86AC70` |
| Final update | Pale lavender `#E5DCEA` |

This is a starting palette, not a required mapping for every paper. Use color
for roles and correspondence, not one arbitrary hue per stage. Keep text dark;
branch labels and position must carry the distinction in grayscale as well.

Use modest corner rounding, thin black arrows, and plain titles outside stage
frames. Avoid gradients, shadows, heavy title bands, and decorative icons in this
style. Semantic vector glyphs and labeled document/model objects are encouraged
when they replace prose or expose an input/output. Dashed frames are appropriate when they genuinely group stages; do not
frame every label. Define dashed grouping in the caption and do not reuse the
same dash code for uncertainty or optional computation.

Preserve the reference's openness at the venue's actual width. Do not force its
aspect ratio when it would make your method unreadable. The venue font budget
takes priority over matching an image's pixel dimensions.

## 4. Construction lessons that prevent regressions

- Base paired rows on a shared rhythm. Match stage tops and bottoms using the
  bounds of **all** stage contents, including the lowest labels. A common bottom
  derived only from the last panel breaks when another panel's text grows.
- Derive scorer height from both input/output rows, or verify explicitly that
  every port lies within the box. A line above or below the scorer can appear to
  bypass the very operation it is meant to enter.
- Shorten labels or enlarge their allotted space before reducing font size.
  Replacing symbols with words changes text extents: recompile and inspect the
  whole drawing after the replacement, even if no coordinates were edited.
- Keep label clearance on bypass routes. A raised accent or tall glyph can
  touch a dashed frame even when the baseline looks clear.
- Use coordinates for invisible positioning helpers. Named strip or plot nodes
  should enclose actual visuals; phantom rectangular helpers create misleading
  geometry overlap reports.
- Check font size after scaling the complete PDF, including standalone borders,
  into the manuscript. The geometry script's content-only estimate can be
  optimistic. If math remains, inspect its smaller subscripts separately.

## 5. Acceptance checks

Mechanical QA is necessary but cannot measure comprehension. On the rendered
image, ask an independent reviewer who has not read the paper to:

1. Explain the input, distinctive operation, and output in one sentence.
2. List any labels that require looking up a variable or acronym.
3. Identify what changes between branches and what is shared.
4. Trace both inputs into any combination operator, checking port locations.

If the reviewer can only read the module names aloud, the mechanism is still
opaque. Revise the labels or real objects instead of adding prose everywhere.
Then inspect color, grayscale, and the final manuscript insertion for wrapping,
clipping, border contacts, and readable type.

After the checks pass, show the user the result. Record their accepted visual
choices and subsequent corrections separately: approval of style does not imply
approval of notation density or scientific interpretation.
