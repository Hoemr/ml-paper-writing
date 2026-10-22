# The polish layer: making a figure look designed

This file exists because mechanical correctness is a floor, and a floor is not
the complaint. The complaint is: "this looks like default TikZ" — the box-arrow
diagram that compiles, passes every check, and still reads as amateur next to a
polished Fig. 1. What follows is the aesthetic system the mechanical gate
cannot check: named style families, exact numbers, and the restraint laws that
keep decoration from decaying into slide-deck kitsch.

Distilled from: `Noi1r/tikz-academic` (saturation-hierarchy doctrine, font
ladder, style-debt list), `chingswy/Skill-Research-Figure` (card grammar,
10-role palette tokens), `gxCaesar/open-research-skills` (style profiles,
3-pass refinement), `0xE1337/thesis-figure-skill` (hierarchy levers, anti-slop
gate, cover test), `TAO-QKV/Icarus-Figures` (real-method-object red line, hero
doctrine), `opentikz` (fill/stroke pairing, one-emphasis law),
`anthropics/skills canvas-design` (craftsmanship language), the pgf-blur and
arrows.meta source documentation, plus "Ten Simple Rules for Better Figures"
(Rougier et al., PLOS Comput Biol 2014) and the MIT Communication Lab figure
guide. Design ideas only; no prose was copied from unlicensed sources.

## 1. Name the style family first

"Polished" is not one look. There are two legitimate families, and mixing them
is the single fastest way to look amateur. **The family is a contract decision
(STEP 1), and every figure in one paper uses the same family.**

| | **flat journal** (default) | **soft card** (modern LLM/RL report) |
| --- | --- | --- |
| Reads as | Nature/CV-journal figure, ViT/Swin era | DeepSeek/Qwen/LLaMA-report Fig. 1, Figma-era |
| Corners | 0–2pt, often square | 4–6pt rounded cards |
| Depth | none — tints only | one subtle blur shadow per card |
| Fills | flat tint `X!8–15` | faint vertical gradient `top X!10 → bottom X!3` |
| Borders | thin, `gray!50` or hue `!70!black` | hue `!60–70!black`, 0.9–1.0pt |
| Type | serif or sans, follows the paper | sans-serif (`\sffamily`), math stays serif |
| Icons | rare, only semantic | semantic only: ❄ frozen / 🔥 trainable / DB cylinder |
| Use for | CV/vision papers, data figures, Nature-adjacent venues | LLM/RL/NLP method pipelines — the "directly generated" look |

The flat-journal family also includes the **reference-led pastel LLM** profile
in [reference-led-llm.md](reference-led-llm.md): semantic token/document/model
graphics, substantial pastel fills, green modules and dashed neutral groups.
Use that profile when the supplied reference calls for it. “Flat journal” does
not mean gray boxes or sparse graphics; LLM subject matter does not require
soft-card UI effects. Reference-specific type and palette override the defaults below.

Neither family licenses decoration. What both families ban outright:
bevels, 3-D perspective boxes, glow, clip art, rainbow fills, decorative
border art, icon per panel.

**Verified user verdict (2026-09-25, ICLR method figure).** A full soft-card
treatment — gradient cards, full-width dark header bands, one blur shadow per
card, fontawesome icons — was rejected as "AI 味太重……完全没法用" by the
paper's own author, who preferred a plain flat NPG-palette version in that task.
That is feedback about that composition, not a permanent preference for NPG
colors or a ban on semantic illustrations. Heavy header bands, shadows and
gradient cards can conflict with a light academic reference. Use the user's
current reference to choose; do not treat “AI-looking” as a measurable property
or preserve a rejected palette because an older example approved it.
TeX-native polish lives elsewhere: stroke-width hierarchy, saturation steps of
one hue, ruthless alignment rhythm, real method objects, and a confident type
scale (11pt-class labels at natural size, not 7pt wall-of-text).

## 2. Colour: hierarchy through saturation, not colour count

> "Saturated colours are reserved for *meaning*, never for ornament."
> "If everything is orange, nothing is."

Budget: **≤ 6 colour families, exactly one accent role.** Hierarchy comes from
saturation *steps within a hue*, not from more hues.

For a saturated-base palette, this fill/stroke/text pairing is a useful default
(the explicit-pastel reference profile uses its listed fills directly):

```latex
fill = X!8–15          % surfaces: barely-there tint
draw = X!60–75!black   % borders: medium shade of the SAME hue
text = X!50–60!black   % accent text, never raw X — raw red/blue "vibrates"
neutral text = ink     % a near-black slate, not pure black
```

Backgrounds lightest → borders medium → text/arrows darkest. A container and
the sublayers inside it need two distinguishable greys (`gray!15` container,
`gray!6` sublayer).

Two verified palettes; define once, use tokens, never inline hex:

```latex
% --- soft-card / LLM-report set (Tailwind-tint derived, blue-orange contrast)
\definecolor{ink}{HTML}{334155}      % slate-700: structure text, arrows
\definecolor{inklight}{HTML}{94A3B8} % slate-400: de-emphasised labels
\definecolor{cblue}{HTML}{2563EB}    % primary flow / frozen modules
\definecolor{corange}{HTML}{D97706}  % THE accent: the novel component
\definecolor{cgreen}{HTML}{059669}   % verified / positive outcome (small areas)
\definecolor{cviolet}{HTML}{7C3AED}  % loss / optimisation nodes (small areas)
% --- colourblind-safe set (Okabe-Ito, Wong Nat. Methods 2011)
% blue #0072B2 · orange #E69F00 · green #009E73 · vermillion #D55E00
% purple #CC79A7 · sky #56B4E9   (blue/orange and blue/vermillion are the
%                                 safest contrast pairs)
```

A third palette Wei approved on 2026-10-15 is the pastel-card set he picked out of a reference overview (`#FDF3D0` model card, `#E7EBF7` group container, `#F8FCF7` / `#FAF5F6` sibling cards, `#F2F2F2` neutral container, `#BFBFBF` hairline, and `#4B7254` as the single accent). It is recorded with its reference image in `references/method-figure/reference-led-llm.md`; use it when the request is "like that overview", and keep the flat-journal palettes above otherwise.

Role semantics for ML method figures (use consistently across the paper):
blue = standard/frozen/base; **orange or green = your contribution**; green
additionally = verified/pass (small chips only); purple = loss/objective; red
only for warning/negative/baseline-failure; grey = neutral structure and
replay/storage. Red vs green as opposites must survive grayscale — never let
hue alone carry the distinction.

## 3. The soft-card kit (verified, but use sparingly)

The kit below is verified to compile and render. Treat it as a reference for
the rare explicit soft-card request — not as the default polish pass. The
flat-journal sections of this skill (cv-transformer-styles.md, the NPG-style
palette in ml-conventions.md) remain the working default.

```latex
\usetikzlibrary{arrows.meta,bending,calc,fit,positioning,backgrounds,shadows.blur}
\usepackage{fontawesome5}   % \faSnowflake[regular], \faFire, \faDatabase ...

\tikzset{
  % --- card: rounded, gradient body, one quiet shadow -------------------
  card/.style 2 args={rounded corners=5pt, draw=#1!65!black, line width=1.0pt,
      top color=#1!10, bottom color=#1!3, inner sep=8pt, align=center,
      blur shadow={shadow xshift=.5ex, shadow yshift=-.5ex,
        shadow blur radius=.4ex, shadow blur steps=8,
        shadow blur extra rounding, shadow opacity=30}},
  % --- header pill: sits ON the card's top edge, centred or left ---------
  hdrpill/.style 2 args={fill=#1!75!black, text=white, rounded corners=6pt,
      font=\sffamily\bfseries\footnotesize, inner xsep=8pt, inner ysep=3.5pt},
  % --- chip: status pill ("frozen", "x N", "ours") -----------------------
  chip/.style 2 args={rounded corners=7pt, draw=#1!65!black, line width=0.7pt,
      fill=#1!10, text=#1!55!black, font=\sffamily\scriptsize,
      inner xsep=6pt, inner ysep=2.5pt},
  % --- arrows: three weights, geometric tips, round caps -----------------
  flow/.style={-{Stealth[length=2.2mm,width=1.7mm,round]}, line width=1.1pt,
      draw=ink, line cap=round, shorten >=1.5pt, shorten <=1pt},
  thinflow/.style={flow, line width=0.6pt, draw=inklight,
      -{Stealth[length=1.6mm,width=1.2mm,round]}},
  emphflow/.style={flow, line width=1.7pt},     % the contribution path only
  % --- type ladder: exactly four sizes, sans; bold ONLY on titles --------
  tag/.style={font=\sffamily\bfseries\footnotesize, text=ink, inner sep=1.5pt},
  note/.style={font=\sffamily\scriptsize, text=inklight, align=center},
}
```

Exact numbers that carry the look:

| Element | Value | Why |
| --- | --- | --- |
| Corner radius | cards 4–6pt; chips 6–8pt (pill); elbows `rounded corners=5–6pt` on the *path* | > 6pt on cards reads toy-like; sharp 90° elbows read dated — round every orthogonal bend |
| Card padding | `inner sep=8pt` ≈ the 8–10px UI-card padding | text needs breathing room or the card reads cramped |
| Shadow | blur, xshift `.5ex`, yshift `−.5ex`, radius `.4ex`, **steps 8 + extra rounding**, opacity 25–35 | default `drop shadow` (hard, 50% black) is the clip-art look; never shadow arrows, labels, or chips |
| Gradient | `top color=X!10, bottom color=X!3` — ≤ 10% mixing distance | beyond that it becomes a slide-deck gradient |
| Stroke hierarchy | 1.7pt contribution > 1.1pt main flow > 1.0pt borders > 0.6pt aux | at least two visual weights, never more than four |
| Arrow tips | `Stealth[length=2.2mm,width=1.7mm,round]`, `shorten >=1.5pt` | default CM tips are the #1 "dated" tell; sub-1.5cm arrows need a shorter tip or the tip eats the stem |
| Type scale | `\small` body → `\footnotesize` labels → `\scriptsize` captions → `\tiny` chips | exactly four roles; bold only container/panel titles — bold body text is a poster |
| Spacing rhythm | one `node distance=10mm and 12mm`; gaps from a discrete set (0.12/0.2/0.3/0.5cm) | inventing a new distance per pair is visible as sloppiness |

Construction notes:

- **Header pill on a card edge**: place the card first, then
  `\node[hdrpill=X, anchor=north] at (card.north) {...}` (or
  `anchor=west` + xshift for left-aligned). The pill overlaps the border —
  draw the pill AFTER the card, in the main layer.
- **Icons are font glyphs**: they inherit `text=` colour, render slightly
  large — wrap in the size you want and keep them monochrome. Semantic
  declarations only: `\faSnowflake[regular]` frozen, `\faFire` trainable,
  `\faDatabase` replay/storage, `\faSearch`/`\faCheck` verify. Define the
  glyph convention in the caption ("❄ = frozen parameters"). Never decorate
  every panel with an icon; that is the first symptom of AI-generated slop.
- **Shadow caveat**: blur shadows misbehave on custom pgf layers — keep
  shadowed nodes on the default layer; zones/fits go on `backgrounds` unlit.

## 4. The composition laws the gate cannot see

**The 5-second question (ask before drawing AND before delivering).**
> 审稿人 5 秒看完，记住的是什么？What will the reviewer remember in five
> seconds? If you cannot name one memorable element, do not deliver.

**Real method object > text label** (the highest-leverage single rule).
> If you can draw the distribution, do not write the word "distribution".

A hero made of bare labelled boxes is the most-penalised figure pattern.
Embed the actual object: the token strip, the mini distribution over the
vocabulary, the paired replay cards with the one differing field, the weight
profile, the before/after with the metric on the transform arrow. One real
object per branch is enough; do not force three.

**Hierarchy needs ≥ 2 stacked levers.** Size / font-weight / colour /
whitespace / stroke-weight — the hero stacks at least two (e.g. 1.5–2× area +
the only 1.7pt stroke + the only saturated header). One lever alone reads as
accident.

**Cover tests.** (1) Cover the caption — the claim must still be readable.
(2) Cover any panel — the figure must lose information no other panel
carries; if nothing is lost, merge or delete the panel. (3) Delete test —
any element whose removal does not weaken the claim was decoration.

**"能不能更少?" — can it be fewer?** Every element must earn its place.
This includes **defensive prose**: footer rows and panel notes that reassure
the reader ("training-only", "no extra rollouts", "signed — direction from the
reward only", "weights stay positive") are caption material, not figure
material. A user verdict on an ICLR method figure (2026-09-25): the bottom
claims row was "完全没必要有的" and was cut together with the per-panel
guarantee notes. If a sentence argues the figure's *validity* rather than its
*content*, it belongs in the caption.
Density must match the method's complexity. Do not add insets or formulas just
to occupy space. First tighten the layout or enlarge the meaningful comparison;
add an object or short label only if it explains missing information. For an
overview, follow `overview-first.md`: equations are not a substitute for a
readable visual mechanism.

**Alignment is the 质感 people unconsciously register.** Same row ⇒ same top
and height; same column ⇒ same left and width; equal gaps between siblings;
visible misalignment cheapens a figure more than any missing shadow hurts it.

**Reading path = visual flow.** For every connector ask whether the reader's
0.1-second intuition matches the logic. Straight when aligned ("能直就直");
rounded elbows when orthogonal; fan-out as a fork with a trunk, never a broom
of diagonals; labels ride the longest straight segment or sit in whitespace.

## 5. The three-pass refinement (after the first clean render)

Mechanical QA returns CLEAN; polish starts there.

1. **Composition pass** — reading order, grouping, relative area. Does the
   core transformation have the most room? Is there exactly one focal zone?
   Are the two branch identities legible before any label is read?
2. **Unit pass** — zoom each schematic element. Would a mini distribution
   beat the word "teacher"? Does each object carry one fact a reader could
   quote? Icons semantic, labels in-place (never make readers match "(a)"
   against the caption).
3. **Harmonisation pass, at final insertion size** — reconcile stroke
   weights, corner radii, palette tokens, type ladder, equation alignment,
   gap rhythm. Fix one thing everywhere, not one thing once.

Aesthetic conservation law: a fix may not break existing symmetry,
parallelism, or spacing. After every fix, re-walk the whole figure — fixes
introduce new defects more often than they remove them.

## 6. Failure modes (the ones polish reviews actually catch)

| Symptom | Defect | Fix |
| --- | --- | --- |
| "Looks like default TikZ" | CM arrowheads, sharp elbows, inconsistent radii, one flat grey | style kit from §3, applied globally |
| Slide-deck feel | saturated fills, heavy shadows, gradients > 10%, icon per panel | §2 budget + §3 recipes; one accent, one shadow weight |
| Word-heavy hero | text labels where objects belong | real method objects (§4) |
| Everything pops | accent used on ≥ 2 elements, or raw saturated text | one accent role; text `X!55!black`; neutrals elsewhere |
| Uneven whitespace | ad-hoc gaps; one cramped card among airy ones | discrete gap set; same-row same height |
| Rainbow branches | a hue per stage with no meaning | hue = role (blue standard / accent novelty); stages differentiate by saturation of one hue |
| Dated conference look | default `->` tips, mixed serif/sans, bold body text | `Stealth[...,round]` tips, one family + math, bold titles only |
| Transparent-background previews render black | standalone PDF page is unpainted; sips keeps alpha | §7 render recipe |

## 7. Flattened QA renders (this environment, verified)

A standalone TikZ PDF has no painted page background. `sips` rasterises that
as **transparent** PNG; viewers that composite onto black (including some
image tools) show a black figure and can mislead a review pass.

- Preferred renderer: **`qlmanage -t -s 2400 -o <dir> fig.pdf`** — produces
  `fig.pdf.png`, flattened onto white, shadows and gradients intact.
- If `sips` must be used, paint the page as *content* so no viewer can
  composite it away. At the very end of the `tikzpicture`:
>
```latex
\begin{scope}[on background layer,overlay]
  \fill[white] ($(current bounding box.south west)+(-12pt,-12pt)$)
    rectangle ($(current bounding box.north east)+(12pt,12pt)$);
\end{scope}
```
>
  `overlay` keeps the fill out of the bounding box, so the page size is
  unchanged; the +12pt covers the standalone `border`. `\pagecolor{white}`
  alone is NOT sufficient under sips (verified: it lands in the PDF but sips
  still rasterises the page as transparent).
