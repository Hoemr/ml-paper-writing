# Review checklist

The judgment layer. `qa.sh` proves the figure is not mechanically broken; this
proves it is not *empty*.

Rules for using it:

- Answer every item with **evidence from the actual render**, not from the source.
  "The label is 8pt" without having looked is fabrication, and it destroys the
  value of the whole pass.
- Any **N** is a blocker: patch, recompile, re-render, return to the top.
- All-Y means "no obvious defects", **not** "good figure". Do not report it as
  more than that.
- Re-render after every structural change. A fix routinely introduces a new,
  different defect.

## 1. Claim (the figure's job)

- [ ] **One sentence** states what the reader must understand. Not a module list.
- [ ] **Cover the caption** — is the claim still readable from the figure alone?
      If you need the caption to know what is claimed, the figure is displaying,
      not arguing.
- [ ] The **novel contribution** is findable at a glance and is the visual focus.
- [ ] A reader unfamiliar with the paper could describe the figure in 30 seconds.
- [ ] For an overview, the reader can name the input, distinctive operation, and
      output without decoding paper-specific symbols or reading a notation legend.
- [ ] Labels name concrete data or actions; equations and indexed variables appear
      only when necessary for this figure's purpose, not as copied method text.
- [ ] No element is redundant with another (the necessity test: delete it — does
      the claim weaken?).
- [ ] The figure does **not** look interchangeable with the baselines' figures.

## 2. Reading path

- [ ] There is an obvious **entry point** (top-left, or the hero) and an exit.
- [ ] The dominant organizing logic is identifiable without the title.
- [ ] Nothing orbits the whole canvas; secondary branches leave and rejoin locally.
- [ ] Reading order in the figure matches the order things are explained in the text.

## 3. Composition and hierarchy

- [ ] There is a **focal zone**, and it is the novel mechanism or decisive
      comparison — not merely the largest enclosing box.
- [ ] The hero occupies ~45–60% of the height, or ≥1.5× the area of supports.
- [ ] Not an equal-weight card grid. If panels are equal, they carry genuinely
      equal, distinct evidence.
- [ ] No large empty region (> 3 cm × 2 cm). Thin lines do not count as filling it.
- [ ] Content hull fills the canvas without crowding; the figure could not be
      substantially enlarged while keeping all routes.
- [ ] Frames group actual stages or comparisons; whitespace and alignment handle
      local grouping. No redundant frame around every label or object.

## 3b. Polish (references/method-figure/polish-style.md)

- [ ] **5-second answer exists**: you can name the one element a reviewer will
      remember, and it is the hero, not an accident of layout.
- [ ] **Real method objects, not only labels**: at least one embedded object
      (strip, distribution glyph, paired cards, profile) carries the method.
- [ ] **Hierarchy stacks ≥ 2 levers** on the hero (size, weight, colour,
      whitespace, stroke) — no lever acting alone.
- [ ] **Style family is consistent**: one named family (flat journal / soft
      card) across the whole figure — no mixed corner radii, no second shadow
      weight, one accent role, ≤ 6 colour families, text never raw-saturated.
- [ ] **Icons are semantic only** (frozen/trainable/replay/verify), each
      defined in the caption or legend, and the encoding survives grayscale.
- [ ] Same-row elements share top and height; same-column share left and
      width; sibling gaps come from one discrete set — no ad-hoc distances.

## 4. Shapes carry meaning

- [ ] Operators, state, evidence and metadata are **visually distinguishable**
      before reading labels — not every noun rendered as the same rounded rectangle.
- [ ] A state/sequence is drawn as a strip or sequence; an operator as a bounded verb.
- [ ] Embedded plots sit **inside** their stage, not floating at its edge.
- [ ] Abstraction levels are not mixed (neuron + layer + block in one figure).

## 5. Edges

- [ ] Every connection's **source and target are visually unambiguous**.
- [ ] Parallel input/output rows enter within the connected module's bounds;
      no branch appears to bypass a scorer or transform because its port is outside.
- [ ] Every arrowhead points the way the data flows; no tip points backwards.
- [ ] Arrow tips stop **outside** the target box or exactly on its boundary —
      never floating in space, never stabbed into the interior.
- [ ] All labels are beside their line, not on it.
- [ ] No line crosses a **label**.
- [ ] No line crosses an unrelated **node**.
- [ ] Edge labels sit at the midpoint of the longest straight segment, or in clear
      whitespace — not hugging a bend.
- [ ] Fan-out/fan-in is a tree with a crossbar, not a broom of diagonals.
- [ ] Junction dots are not stabbed by arrowheads.
- [ ] Every non-solid style is defined in the legend or caption.

## 6. Legibility at final size

- [ ] Inspect the render **at the declared print width**, not zoomed in.
- [ ] Smallest labels are legible: ≥ 7 pt effective after scaling the complete PDF,
      including its border. Inspect any smaller math subscripts separately.
- [ ] No label is truncated, clipped, or touching its box border.
- [ ] Every label that matters survives **grayscale**.
- [ ] No two labels graze (within 1–2 px).

## 7. Honesty

- [ ] No invented numbers, modules, metrics, or logos.
- [ ] Compressed/repeated structure is annotated, not silently collapsed.
- [ ] A mechanism shown as "per-stage detail" is genuinely the same for all stages;
      otherwise retitle it so it does not bind to one instance.
- [ ] Any uncertainty drawn (dashed, faded, "optional") is explained.
- [ ] The figure does not imply a stronger claim than the data supports.

## 8. Consistency with the paper

- [ ] Labels use the **same terminology** as the body text.
- [ ] Canonical stage/method names and decision literals match the source;
      advisory checks and decisive acceptance gates are not conflated.
- [ ] It agrees with any pseudocode or algorithm float (same stage names, same order).
- [ ] Colours, fonts and line styles match the paper's other figures.
- [ ] The caption does not duplicate the Methods section.

When a user supplies a reference, also compare palette lightness/hues, grouping,
graphic-object vocabulary, typography, line weight and density against that
reference. Record mismatches separately from mechanical defects; a clean QA
report does not establish stylistic correspondence.

## After the checklist

1. **Spawn an independent reviewer** with a blank context and only the PNG. Brief
   it adversarially: "there are defects, find them." Ask for concrete visual
   evidence proving it looked, not a score.
2. **Do not accept a same-context self-pass as the review.** A generator that
   audits itself four times still cannot see the gap between intent and output —
   this is measured, not theoretical: three from-scratch figures broke, each on a
   different axis, and one uniform law held — **the newest structural element,
   the one with no precedent in the figure, is where it breaks.**
3. **Triage** the checker's known false positives rather than treating either the
   machine's verdict or the reviewer's as final.
4. **Re-run the gate after any fix**, since fixes introduce defects.
5. **Show the user.** After the checks and the reviewer both report clean, the
   user is still the gate — vision has structural blind spots, and human
   reviewers have caught large blank regions and misplaced connectors that every
   automated pass missed.

## Escalation

- **≥ 5 blockers on the third round:** local patching will not save it. Return to
  the design contract and reconsider the composition.
- **The same blocker unfixed twice:** your fix is attacking the wrong thing.
  Change approach rather than pushing harder on the same patch.
- **Redrawing the same connector a third time:** the figure is being asked to do
  two jobs. Split it.
