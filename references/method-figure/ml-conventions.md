# ML method-figure conventions

What ML/CV papers conventionally encode, and where the conventions are genuinely
unsettled. Contested items are marked as such — do not turn them into rules.

## Edge semantics

**Solid arrow = forward data flow.** This is the one near-universal convention.

Everything else is fragmented. The literature attests dashed meaning *all* of:
frozen module, optional path, error path, interface boundary, reference line,
predicted vs ground-truth curve, gradient quantity. There is no national
convention, and a reader cannot guess which you meant.

**Therefore the rule is not "dashed means X" — it is: any non-solid style must be
defined, once per paper, in a legend or the caption.** A figure whose dashed edge
is unexplained is ambiguous by construction.

A defensible taxonomy to draw from (pick a subset, define it, keep it stable):

| Relation | Encoding |
| --- | --- |
| Data flow | solid, coloured by source |
| Control / orchestration | solid, grey |
| Loss / supervision | enters the loss node; **label it** |
| Gradient / backward | reverse direction, or a distinct style — never implicit |
| Optional / conditional | dotted |
| Failure / negative path | dashed |
| Bidirectional | double-headed |

Two specifics worth getting right:

- **Draw the loss as an explicit node**, not floating text. This is the modern
  computation-graph convention and it makes where-gradient-flows unambiguous.
- **Supervision enters the loss from a label drawn as an input**, not as another
  data-flow arrow.
- If you use a stop-gradient / detach gate, **draw it** and legend it. `sg` is
  documented at the equation level; representing it in a figure is common but
  unwritten, so it must be explained.

## Frozen, trainable, train-only, inference-only

**The de facto glyph standard, verified in current PEFT-era papers: snowflake ❄
= frozen parameters, fire 🔥 = trainable** — e.g. the LoRA+ paper's caption
(arXiv:2402.14714): "The fire and snowflake emojis indicate the trainable and
frozen parameters respectively." Padlock and lightning bolts appear as variants.
Rules for using the convention:

1. Always define the glyph in the caption or an in-figure legend — never make a
   reader decode it.
2. In TikZ, use `fontawesome5` (`\faSnowflake[regular]`, `\faFire`) rather than
   emoji fonts: the glyphs are monochrome, inherit `text=` colour, and print.
   Render slightly large — size them deliberately (see `polish-style.md` §3).
3. Pair the glyph with a **second channel** (desaturated fill, dashed border,
   grey tint) so frozen/trainable survives grayscale.

There is no citable standard beyond that practice; the substantive rule is
unchanged: colour-coding plus a caption statement remains the safest pairing.

Two encodings *are* documented:

1. **Colour-coded and stated in the caption** — e.g. "grey = frozen, blue =
   trainable". This is the most common current practice and the safest.
2. **Solid = unfrozen, dashed = frozen.** Documented, but dashed is overloaded
   (above), so it needs a legend.

**The substantive correctness point, which is the one people actually get wrong:**
if training and inference have *different topology* — adapters merged into the
base, a branch dropped at test time — then one diagram cannot honestly serve both.
Either draw two panels, or draw the training topology and state the inference
difference in the caption. A single diagram that quietly conflates the two is a
correctness defect, not a style choice.

Also: a module that is present but *deactivated* is conventionally shown
**disconnected**, not merely greyed.

## Where the novelty goes

The most ML-specific rule in this reference, and the one with no analogue in
journal-style guides:

> **The method figure must look different from prior work's method figures.
> If it looks the same, readers assume there is no novelty.**

Consequences:

- The figure's job is to **highlight novelty and give a legible skeleton** — not
  to make the reader understand the method. The prose does that.
- Compress standard parts (encoders, decoders, off-the-shelf layers) to small
  grey boxes. Spend the area on what is new.
- If the overall pipeline is conventional, **zoom into the novel module** rather
  than drawing the whole stack again.
- Label modules with the **real names from the paper**, and annotate tensor
  shapes where they clarify — described by practitioners as the single most
  useful addition.
- **Draw from the model definition, not from memory.** Architecture figures that
  disagree with released code are a recurring reproducibility complaint.
- Leave optimiser, learning rate and batch size out of the figure.

## Figure 1 paradigms

Three established patterns; pick by what the contribution is.

| Paradigm | Use when | Avoid when |
| --- | --- | --- |
| **A. Running example + failure** (default) | The problem is concrete and a failure is visible side by side | No single input exposes the problem |
| **B. Existing vs ours**, two columns | The contribution is a structural change to a mechanism | The two look nearly identical at schematic level — "spot the difference" |
| **C. Performance teaser** | The gain is the headline, large, and the paper is short | **Gains are marginal** — a teaser advertises weakness before the first claim is read |

Within a multi-panel figure: panel (a) is the hook and assumes zero context,
panel (b) is the one that read alone makes your sentence true, and the rest are
evidence ordered by how much they strengthen (b). **Do not force equal panel
sizes when importance differs.**

## Captions

- **No title inside the figure** — an explicit ICML rule; the caption serves that
  function. (NeurIPS specifies caption case but does not state the ban.)
- First sentence: what the figure shows. Then the takeaway.
- **Never open with "Figure N shows…"** — the number is already printed.
- Self-contained: define every abbreviation, colour and line style used, so the
  figure is readable without the body text.
- Do not re-narrate results or duplicate the Methods section.
- Sentence case (NeurIPS house style).
- Report statistics on the figure, not only in prose: `n`, and which interval
  (SD, SE and 95% CI differ by √N and tell different stories).

## Contested — decide per paper, then stay consistent

| Item | Positions | Guidance |
| --- | --- | --- |
| Typeface | serif matching the body vs sans-serif (Arial/Helvetica) | Per-paper choice, stated once. ML schematics increasingly sans |
| Min type size | 7 pt (ML practice) vs 5 pt (Nature production floor) | 7 pt working floor, 5 pt hard limit |
| Panel label form | `a` (Nature) vs `(a)` (most ML venues) | `(a)` is the ML default; consistency beats the choice |
| Legend | always vs direct labels preferred | Direct labelling wins when regions are spatially stable |
| Grayscale requirement | stated at OSDI/SOSP; not formally at ML venues | Keep it anyway — it is a strong norm |
