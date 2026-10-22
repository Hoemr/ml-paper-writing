# Exemplar corpus

Composition references for ML method figures. **Links and analysis only — no
figure images are stored here.** We study composition; we do not archive artwork,
and any reuse of a specific figure's layout in your own paper is your call to
make with the original authors' terms in mind.

## How to use this file

Read an exemplar for its **compositional decision**, never its science or its
exact layout. For each one, ask:

1. What is the reading path, and what made it obvious?
2. Where is the focal point, and how much area does it get?
3. How is the novel part differentiated from the standard parts?
4. What shape grammar is in play — what is a box, what is a strip, what is a plot?
5. How does it mark training-only / frozen / inference-time?
6. Would it survive grayscale?

Then write your own contract (SKILL.md step 1) and build your own figure. Do not
transplant a topology; the source paper's scientific structure is not transferable
and a figure that copies one looks like a figure that copies one.

**What is verified versus what is my reading.** Every entry carries a `Verified`
line naming exactly what was checked against the paper's own source. The
`Composition` prose is my reading of the figure, not a measurement, and should be
treated as an argument to check against the render, not a fact. Grayscale
survival is **not verified for any entry here** — that requires rendering and
inspection, and I did not download the artwork.

## Measured corpus geometry

Recomputed directly from the `topconf-paper-figure-gallery` dataset
(`qwdwqfwq/topconf-paper-figure-gallery`, `data/figures.json`, n = 2730 Fig. 1 /
teaser crops from ICLR/ICML/NeurIPS/CVPR/ACL/AAAI 2023–2025; 979 NeurIPS, 521
ICLR, 415 ICML, 326 ACL, 264 AAAI, 225 CVPR). These are `w`/`h` fields straight
from the dataset, so they are reproducible.

| Pattern | n | median w:h | p25 | p75 |
| --- | --- | --- | --- | --- |
| teaser | 1237 | 2.38 | 1.88 | 2.92 |
| architecture | 424 | 2.31 | 1.78 | 2.85 |
| conceptual | 364 | 2.37 | 1.92 | 2.86 |
| pipeline | 314 | 2.26 | 1.82 | 2.91 |
| framework | 216 | 2.24 | 1.82 | 2.81 |
| taxonomy | 165 | 2.11 | 1.75 | 2.56 |
| **all** | **2730** | **2.32** | **1.85** | **2.87** |

ICLR alone (n = 521): median 2.34, p10 1.54, p90 3.32; 23.4 % are ≥ 3:1.

Three readings worth acting on:

- **The guidance in `venues.md` ("2:1 to 3:1") is empirically the norm, not a
  stylistic preference.** The p25–p75 band is 1.85–2.87. A figure at 2.3 is
  ordinary; that is the shape a 140 mm single-column slot wants.
- **What is penalised is *square*, not *extreme*.** Median gallery score by
  aspect bucket is flat at ≈ 60 from 1.5:1 upward (60.9 / 60.1 / 59.7 / 58.3),
  but drops to **51.4** below 1.5:1. Square-ish figures (w:h < 1.2) are only
  **3.6 %** of the corpus, and the ones that do it are disproportionately
  `taxonomy` and survey figures — where a grid of categories is genuinely the
  content. Shape follows the communication task; it is not a free variable.
- **Do not read the `score` column as a design verdict.** It is the gallery's own
  heuristic, so ranking by it is circular. The geometry columns are independent
  measurements; the score is not.

I did not reproduce the colour/whitespace/label statistics that circulate for
this dataset (saturation, bitmap fraction, label spans). Those require
downloading and analysing every crop, and no decoder for the JPEG crops is
available in this environment (`numpy` and `PIL` are both absent). Treat any such
figures you see quoted as unverified here.

## Local exemplars

The strongest references available are the figures already in this repository,
because their design rationale is recorded rather than guessed at.

| Figure | Role | Design record |
| --- | --- | --- |
| `figures/method_overview.tex` | Two-branch method figure with a matched-control pair | `figures/method_overview.design.md` |

`method_overview.design.md` is worth reading even if you never reuse the figure:
it records the figure claim, the narrative map, the role-to-shape mapping, the
grayscale plan, and — most usefully — the four defects that the first draft had
and how the review pass found them, including a spurious edge that implied a data
path the method does not have. That is the shape a design record should take.

---

## The corpus, by communication task

Pick the row matching the job your figure has to do. Two or three entries per job
is a deliberate cap; reading twelve figures teaches less than reading three.

| Job | Entry |
| --- | --- |
| Two encoders / dual-branch, become the field's reference | CLIP Fig. 1 |
| Two-branch with a matched control, minimal styling | SimCLR Fig. 2 |
| Patchify / tokenise an input into a sequence | ViT Fig. 1 |
| Asymmetry in *capacity* (big encoder, small decoder) | MAE Fig. 1 |
| Frozen beside trainable | LoRA Fig. 1 |
| A glyph carries the novelty | ControlNet Fig. 1 |
| Existing pipeline vs ours, as a two-panel contrast | DPO Fig. 1 |
| One figure spanning task → model → data scope | SAM Fig. 1 |
| Three sequential training stages, with edge semantics | InstructGPT Fig. 2 |
| Dense architecture, made legible by in-figure annotation | U-Net Fig. 1 |
| Problem / failure motivation | Pitfalls of Next-Token Prediction Fig. 1 |
| Model outputs embedded as evidence | Chain-of-Thought Fig. 1 |
| Annotating an existing diagram to critique it | Neural Circuit Diagrams Fig. 1 |

---

## 1. CLIP — Fig. 1

- **Paper.** Radford et al., *Learning Transferable Visual Models From Natural
  Language Supervision*, ICML 2021. <https://arxiv.org/abs/2103.00020>
- **Figure.** Fig. 1. Asset `main-diagrams.png`, **476 × 169 = 2.82:1**.
  Inserted in a `figure*` spanning the full text width.
- **Job.** Make "two encoders, trained by pairing" land in one glance, and get the
  reader to the contrastive objective without a legend.
- **Composition.** A single wide strip read strictly left to right. Two parallel
  lanes — image encoder above, text encoder below — converge on a shared middle
  column where the pairing is scored. The convergence *is* the argument: the
  reader sees two independent paths meet, which is what contrastive training is.
  The right-hand third is reserved for the payoff (the zero-shot classifier
  synthesised from the text encoder), so the figure ends on the consequence rather
  than on the loss. Novelty is carried by position — the middle is the only place
  the lanes touch — not by colour or a callout.
- **Transfer.** Encode a *relation between two streams* by where the streams meet,
  not by labelling the relation. If two branches converge, the meeting point is
  the figure's thesis and deserves the centre.
- **Do not transfer.** The specific strip is a scientific claim about CLIP's
  training; the lane topology is not a template. Also, the figure's legibility
  depends on full text width — it was drawn for 140 mm and will not compress.
- **Verified.** Caption verbatim from the arXiv HTML rendering; asset geometry
  (476 × 169) from the same render; title via the arXiv API. Source is a
  multi-panel vector PDF in a `figure*` (source structure reported by an earlier
  pass, not re-derived here).

## 2. SimCLR — Fig. 2

- **Paper.** Chen et al., *A Simple Framework for Contrastive Learning of Visual
  Representations*, ICML 2020. <https://arxiv.org/abs/2002.05709>
- **Figure.** Fig. 2 (**not Fig. 1** — Fig. 1 is an accuracy bar chart).
- **Job.** Show that two views of one image are pushed together, and that the
  projection head used for that push is *discarded* afterwards.
- **Composition.** Two lanes from one source, symmetrical about a vertical axis,
  joined by a loss. The asymmetry that matters is temporal, not spatial: the
  training-time apparatus (projection head) is visibly downstream and then
  visibly absent at inference. The figure is honest about a module that exists in
  training and not at test time, which is the thing `ml-conventions.md` says
  people most often quietly fudge.
- **Transfer — and this is the most useful entry in the file.** This is the
  clearest evidence available that **a top-venue method figure can be plain
  TikZ with almost no styling**: the source is inline TikZ in `main.tex` with
  no colour definitions, plain `draw, circle` nodes, and `>=latex` arrows.
  The composition, not the production value, is what carries it. Do not let the
  absence of a palette or custom glyphs make you think a figure is unfinished.
- **Do not transfer.** The symmetry is justified by the method being literally
  symmetric; do not impose mirrored lanes on an asymmetric method.
- **Verified.** Figure number, caption, and the TikZ source facts (inline TikZ,
  no colour definitions, plain `draw, circle`, `>=latex`) from the arXiv LaTeX
  source, by an earlier pass in this project. Title via the arXiv API. I did not
  independently re-extract the source tarball here.

## 3. ViT — Fig. 1

- **Paper.** Dosovitskiy et al., *An Image is Worth 16x16 Words*, ICLR 2021.
  <https://arxiv.org/abs/2010.11929>
- **Figure.** Fig. 1. Source asset `images/model_scheme.pdf`, ratio ≈ 1.98:1.
- **Job.** Explain a reframing: an image is not an image, it is a sequence of
  patch tokens.
- **Composition.** Left third performs the transformation the paper is named for
  — image cut into patches, patches into a row. The remaining two thirds are a
  deliberately generic transformer block, drawn as a repeated grey slab. The
  proportion is the message: the paper's contribution is the front door, and the
  transformer is explicitly borrowed (the caption credits the box's illustration
  to Vaswani et al.). A reader skimming only the picture still learns where the
  novelty is.
- **Transfer.** When your contribution is a *front-end* to a well-known
  backbone, give the front-end the area and draw the backbone as a single
  undifferentiated compressed block, attributed in the caption.
- **Do not transfer.** The small patch grid is a literal depiction of a specific
  patch size; it is not decoration you can lift.
- **Verified.** Caption verbatim from the arXiv HTML rendering; asset geometry
  (ar5iv raster `model_scheme.png`, 455 × 230 = 1.98) from the same render. The
  source ships a **PDF**, which ar5iv rasterised, so the published figure is
  vector. Title via the arXiv API.

## 4. MAE — Fig. 1

- **Paper.** He et al., *Masked Autoencoders Are Scalable Vision Learners*, CVPR
  2022. <https://arxiv.org/abs/2111.06377>
- **Figure.** Fig. 1. Asset `arch.png`, **672 × 372 = 1.81:1** — a raster, not
  vector. One of the few figures here that would fail the "vector, text still
  editable" row of `constraints.md` §G.
- **Job.** The asymmetry: a heavy encoder sees only the visible patches, and a
  light decoder does the reconstruction.
- **Composition.** The size of the drawn encoder and decoder blocks *is* the
  argument — the decoder is drawn small because it is cheap, and the masking is
  drawn as an explicit visible/masked split at the input rather than described.
  The 75 % masking figure that the whole paper rests on is shown as a picture of
  removed patches, not as a number. This is a figure that could have been three
  grey boxes and a label, and is instead a diagram whose geometry carries the
  claim.
- **Transfer.** When the contribution is a *proportional* claim — this part is
  big, that part is small — draw the proportion. A caption saying "lightweight
  decoder" is weaker than a decoder drawn at one third the height.
- **Do not transfer.** The literal patch mosaic is tied to the method. And do not
  copy the raster delivery: a PNG method figure cannot be re-typeset.
- **Verified.** Caption verbatim and asset geometry from the arXiv HTML render;
  title via the arXiv API.

## 5. LoRA — Fig. 1

- **Paper.** Hu et al., *LoRA: Low-Rank Adaptation of Large Language Models*,
  ICLR 2022. <https://arxiv.org/abs/2106.09685>
- **Figure.** Fig. 1. Caption, verbatim: *"Our reparametrization. We only train A
  and B."*
- **Job.** Frozen `W₀` beside a trainable low-rank pair `BA`, with the frozen
  path still carrying the output.
- **Composition.** This is the canonical frozen-vs-trainable figure: the frozen
  matrix is drawn as the wide, established path and the trainable pair as a
  narrow parallel branch that rejoins it. Note the caption's discipline — it
  states in eight words the one thing a reader must not get wrong about the
  figure. The figure does not contain a legend; the caption is the legend.
- **Transfer.** Two things. (a) Mark frozen by *path width and parallel
  structure*, and say it in the caption in one clause. (b) The
  "eight-word caption that names the one thing that must not be misread" is a
  reusable caption pattern, and better than a longer caption that covers
  everything.
- **Do not transfer.** The specific rank-factorisation topology. Also note this
  figure has no in-figure frozen glyph at all — the ❄/🔒 habit
  `ml-conventions.md` describes is not present here, which is a reminder that
  the glyph is a habit, not a standard.
- **Verified.** Caption verbatim from the arXiv HTML render; title via the arXiv
  API. Asset type: the render exposes no `ltx_graphics` image for Fig. 1, so the
  figure's asset type is undetermined from this probe — do not assume it is a
  raster.

## 6. ControlNet — Fig. 1

- **Paper.** Zhang, Rao & Agrawala, *Adding Conditional Control to Text-to-Image
  Diffusion Models*, ICCV 2023. <https://arxiv.org/abs/2302.05543>
- **Figure.** Fig. 1 — and the correction that makes this entry useful:
  **ControlNet's Fig. 1 is a results teaser, not the architecture.** Asset
  `tea.png`, **685 × 341 = 2.01:1**. Caption, verbatim: *"Controlling Stable
  Diffusion with learned conditions."* The locked-copy / trainable-copy diagram
  is a **later** figure. Several secondary sources cite "ControlNet Fig. 1" as
  the frozen/trainable diagram; it is not, and the point of the paper's Fig. 1 is
  qualitative results.
- **Job.** (Fig. 1) Show control inputs actually controlling outputs. (Later
  figures) Show the locked copy and zero-convolution structure.
- **Composition.** As a teaser it is a stacked evidence grid: condition above,
  generated result below, repeated across condition types. The pay-off is that
  the *input modality* changes while the composition stays constant, so the
  reader attributes the difference to the method rather than to the layout. This
  is the cheapest honest teaser structure there is, and it needs no schematic at
  all.
- **Transfer.** For a visual-results teaser, hold the layout constant and vary
  only the condition; the constant frame is what makes the varying column
  readable as a comparison. And when a method's novelty is a *constraint on a
  frozen model*, the padlock/lock glyph family is the recognisable idiom — but it
  is a convention, not a standard, so legend it.
- **Do not transfer.** A results teaser advertises a visual gap; if your output
  is not visually self-evident, the format has nothing to sell.
- **Verified.** Figure number, caption, and asset geometry (685 × 341) from the
  arXiv HTML render; title via the arXiv API. That Fig. 1 is the teaser is
  confirmed by the render exposing exactly one figure element (`S0.F1`) mapped to
  `tea.png`.

## 7. DPO — Fig. 1

- **Paper.** Rafailov et al., *Direct Preference Optimization*, NeurIPS 2023.
  <https://arxiv.org/abs/2305.18290>
- **Figure.** Fig. 1. Asset `teaser.png`, **476 × 96 = 4.96:1**. The most
  extreme aspect ratio in this corpus, and worth studying for exactly that.
- **Job.** "Existing methods do this long thing; we do one step."
- **Composition.** Two stacked panels sharing one horizontal rhythm. The upper
  panel is the RLHF pipeline — fit a reward model, then run RL — drawn as
  several stages. The lower panel is DPO, drawn as one arrow. The figure's whole
  rhetorical move is **length as evidence**: the reader measures the two panels
  with their eye and the argument is won by the difference in *extent* before a
  single word is read. Note that a 4.96:1 canvas is only achievable because the
  content is thin — two shallow lanes. A dense diagram cannot use this.
- **Transfer.** For an "existing vs ours" Fig. 1, encode the difference as
  *visible length or step count*, not as labels saying "simpler". And check the
  honest version: this only works if the claim is real — a teaser advertising a
  marginal simplification advertises weakness (`ml-conventions.md`, paradigm C).
- **Do not transfer.** The extreme aspect. 4.96:1 is a deliberate consequence of
  thin content; copying the ratio with dense content produces the unreadable
  wide-shallow figure that `venues.md` warns about.
- **Verified.** Caption verbatim and asset geometry (476 × 96) from the arXiv
  HTML render; title via the arXiv API.

## 8. SAM — Fig. 1

- **Paper.** Kirillov et al., *Segment Anything*, ICCV 2023.
  <https://arxiv.org/abs/2304.02643>
- **Figure.** Fig. 1. Asset `teaser.png`, **679 × 164 = 4.14:1**.
- **Job.** Present three interconnected things of *different kinds* — a task, a
  model, and a dataset — as one story.
- **Composition.** Three panels left to right that widen in scope: (a) the task
  (promptable segmentation, one image), (b) the model and its zero-shot transfer
  (many tasks), (c) the data engine (the dataset, over a billion masks). Each
  panel has a different *kind* of content — a task illustration, a model
  schematic, a data-flow diagram — and they are held together by consistent
  framing and by the left-to-right scope ramp rather than by a shared shape
  grammar. This is the entry to study when your figure must present
  heterogeneous content without a unifying visual metaphor.
- **Transfer.** When panels are heterogeneous, bind them by **increasing scope
  along the reading axis** and by identical framing, and give each panel one
  honest job. Do not force a shared glyph system onto content that does not fit
  one.
- **Do not transfer.** Three panels works because there are exactly three things.
  Do not generalise it to N.
- **Verified.** Caption verbatim and asset geometry (679 × 164) from the arXiv
  HTML render; title via the arXiv API. This geometry independently reproduced a
  value obtained in an earlier, incomplete pass, which is a mild cross-check.

## 9. InstructGPT — Fig. 2

- **Paper.** Ouyang et al., *Training language models to follow instructions with
  human feedback*, NeurIPS 2022. <https://arxiv.org/abs/2203.02155>
- **Figure.** **Fig. 2** (Fig. 1 is a human-evaluation bar chart). Asset
  `InstructGPT_Diagram3.1.png`, **476 × 288 = 1.65:1** — notably squarer than the
  corpus median, because three stacked stages need height.
- **Job.** Three training stages in sequence, where **which data trains which
  model** is the part readers get wrong.
- **Composition.** A vertical stack of three stages, each a row: SFT, then reward
  modelling, then PPO. The load-bearing decision is that the figure encodes *two
  different relations* — data flow and "this data is used to train this model" —
  and distinguishes them by colour, then **defines the encoding in the caption**,
  verbatim: *"Blue arrows indicate that this data is used to train one of our
  models."* That is precisely the discipline `ml-conventions.md` demands: the
  non-obvious edge style is named, once, where the reader can see it.
- **Transfer.** The pattern to steal is *two edge classes, one of them
  counter-intuitive, defined in the caption in a single clause*. If a reader
  could plausibly misread an arrow's role, the caption must say what it means.
- **Do not transfer.** The three-stage stack is a factual description of RLHF.
  Also: this figure is a raster PNG, so it is not a production model to imitate
  even though its composition is worth imitating.
- **Verified.** Figure numbers for both Fig. 1 and Fig. 2, both captions
  verbatim, and asset geometry (476 × 288) from the arXiv HTML render; title via
  the arXiv API.

## 10. U-Net — Fig. 1

- **Paper.** Ronneberger, Fischer & Brox, *U-Net: Convolutional Networks for
  Biomedical Image Segmentation*, MICCAI 2015.
  <https://arxiv.org/abs/1505.04597>
- **Figure.** Fig. 1 — the canonical dense architecture diagram, and the most
  reproduced method figure in this corpus.
- **Job.** Convey a many-layer architecture with channel counts and spatial sizes
  without overwhelming the reader.
- **Composition.** A U-shaped spine with skip connections. The decisive move is
  that the figure carries **no colour legend and no in-figure key**; instead the
  caption states the encoding exhaustively, verbatim: *"Each blue box corresponds
  to a multi-channel feature map. The number of channels is denoted on top of the
  box. The x-y-size is provided at the lower left edge of the box. White boxes
  represent copied feature maps. The arrows denote the different operations."*
  Every visual variable is defined in one sentence each, in a fixed order. The
  figure is dense but not ambiguous, and the reason is that its legend lives in
  the caption.
- **Transfer.** Two reusable decisions. (a) **Annotate each block with its tensor
  shape** — channel count on top, spatial size at the lower left — which
  `ml-conventions.md` calls the single most useful addition practitioners report.
  (b) When a figure has several visual variables, define them all in the caption
  in a fixed order; that is cheaper than an in-figure legend and does not consume
  canvas.
- **Do not transfer.** The layer count. This figure has far more modules than the
  5–12 budget in `venues.md`, and it survives only because the modules are
  geometrically regular and the annotations are tiny but systematic. Copying the
  density without the regularity produces exactly the rejected-in-review figure.
- **Verified.** Caption verbatim from the arXiv HTML render; title and authors
  from the arXiv listing. Fig. 1 is rendered natively rather than as a
  `ltx_graphics` image in this render, so its pixel geometry could not be read —
  no aspect ratio is claimed.

## 11. Pitfalls of Next-Token Prediction — Fig. 1

- **Paper.** Bachmann & Nagarajan, *The pitfalls of next-token prediction*,
  NeurIPS 2024 (best paper). <https://arxiv.org/abs/2403.06963>
- **Figure.** Fig. 1. Asset `graph_encodings_dir.png`, **229 × 73 = 3.14:1** —
  tiny in absolute terms, which is the point.
- **Job.** Define the problem instance the paper will show a failure on. Not a
  method figure at all.
- **Composition.** A minimal path-star graph: a centre node, spokes, a goal. The
  figure is doing almost nothing visually and that is correct — its job is to
  fix a *definition* in the reader's head so that the failure in §5 is legible.
  The caption then does the real work, naming each element (`p`, `r`) and
  stating the variants explored.
- **Transfer.** A motivation figure should be **as small as the concept allows**.
  It is a shared reference point, not a showcase; every unit of visual complexity
  you add is a unit the reader must hold in working memory while following the
  argument. Reserve the visual budget for the figure that carries the
  contribution.
- **Do not transfer.** Nothing here is layout; the graph is the mathematics.
- **Verified.** Caption verbatim, asset geometry (229 × 73), and venue/title/authors
  via the arXiv API. **Note a trap I hit:** this paper's ID is **2403.06963**.
  arXiv 2404.05405 is a different paper (*Physics of Language Models: Part 3.3*),
  and an earlier search in this project had associated the title with the wrong
  record. Verify IDs, not titles.

## 12. Chain-of-Thought — Fig. 1

- **Paper.** Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large
  Language Models*, NeurIPS 2022. <https://arxiv.org/abs/2201.11903>
- **Figure.** Fig. 1. Asset `new-pull-figure-landscape.png`, **457 × 223 =
  2.05:1**.
- **Job.** Show that a model's *reasoning trace* is what changes the answer.
- **Composition.** Model outputs are placed inside the schematic as real
  evidence — an actual worked maths problem with an actual trace — rather than
  summarised. The figure's argument is "look at the difference between these two
  transcripts", so the transcripts must be present and legible in the figure
  itself. Panels are referenced as "Fig. 1 (left)" / "Fig. 1 (right)" in the
  body, i.e. the two halves are addressed as units. The trace that matters is
  set apart by highlight, not by a callout.
- **Transfer.** When the evidence *is* the text, quote it in the figure. But size
  it honestly: this figure is nearly all text, so it needs a full-width landscape
  slot and short samples. Long samples are the reason figures like this become
  unreadable.
- **Do not transfer.** Highlighting is the only visual encoding used, so the
  figure would lose its argument in grayscale if the highlight is a pure hue
  shift. Not verified either way — check the render.
- **Verified.** Caption verbatim and asset geometry (457 × 223) from the arXiv
  HTML render; title via the arXiv API. A companion figure (the bar chart in
  Fig. 2) is `pgfplots` TikZ in the source — a second instance of a top-venue
  figure built from plain, unstyled TeX.

## 13. Neural Circuit Diagrams — Fig. 1

- **Paper.** *Neural Circuit Diagrams: Robust Diagrams for the Communication,
  Implementation, and Analysis of Deep Learning Architectures*.
  <https://arxiv.org/abs/2402.05424>
- **Figure.** Fig. 1. Asset `LabelledOriginal.png`, **430 × 489 = 0.88:1** — the
  only portrait figure in this corpus, and deliberately so.
- **Job.** Not to present a method. To **critique an existing diagram** by
  annotating it.
- **Composition.** Reproduces a published transformer diagram and overlays
  annotations in three colours, with the caption naming each colour's role,
  verbatim: *"Critical information is missing regarding the origin of Q, K, and V
  values (red and blue), and the axes over which operations act (green)."* The
  annotated original is the figure. The portrait ratio follows from the source
  diagram's own shape — the figure inherits its subject's geometry rather than
  imposing one.
- **Transfer.** Two things. (a) **To critique a diagram, annotate the diagram** —
  do not redraw it and hope the reader remembers the original. (b) Colour-code
  annotation *roles* (missing-origin, missing-axis) and name them in the caption;
  this is a case where colour genuinely carries a categorical meaning and should
  be enumerated.
- **Do not transfer.** Colour-only encoding in a figure whose entire content is
  the annotation. This one is a real grayscale risk and I did not verify it. If
  you annotate this way, add a shape or label redundancy.
- **Verified.** Caption verbatim and asset geometry (430 × 489) from the arXiv
  HTML render. Title from the arXiv listing. I did not verify the author list.

---

## What this corpus does not cover

Named so it is not mistaken for coverage:

- **No journal-format exemplars** (Nature/Science multi-panel). Their constraints
  are different enough that mixing them is a category error.
- **No data figures.** Plots, curves, scatter and ablations belong to a data
  plotting skill, not this one. Several entries here contain an embedded plot;
  none is a plot figure.
- **Grayscale survival: unverified for every entry.** I did not download or
  render the artwork. Do not treat any of these as pre-cleared on that
  criterion — the entries that flag a grayscale risk are flagged from their
  colour encoding, not from a measurement.
- **No claim that these are the *best* figures.** They were selected for covering
  distinct communication tasks with verifiable geometry and captions. Quality is
  argued per entry, not asserted by reputation.
