# Venue widths, aspect, and capacity

Widths measured from the actual `.sty` files shipped with the venue templates,
not from blog summaries.

| Venue | `\textwidth` | Columns | Figure insertion width |
| --- | --- | --- | --- |
| **ICLR** | 5.5 in (140 mm) | 1 | 140 mm (no `figure*` distinction) |
| **NeurIPS** | 5.5 in (140 mm) | 1 | 140 mm (no `figure*` distinction) |
| **COLM** | 5.5 in (140 mm) | 1 | 140 mm |
| **ICML** | 6.75 in (171 mm) | 2 | 82.6 mm column / 171 mm `figure*` |
| **AAAI** | 7.0 in (178 mm) | 2 | 84 mm column / 178 mm `figure*` |
| **ACL / EMNLP** | ≈ 6.30 in (160 mm) | 2 | 77 mm column / 160 mm `figure*` |

**The single most commonly botched number:** single-column venues like ICLR,
NeurIPS and COLM have no wide-figure option. "Full width" *is* 5.5 in. If a
layout needs 170 mm it does not fit, and no `figure*` will save it.

Insert with `\includegraphics[width=\linewidth]{...}`, never a hard-coded inch
value — the latter produces sub-pixel rounding and spurious overfull-hbox warnings.

## Aspect ratio

A full-width method figure should be **wide and shallow, not square**.

- Single-row pipeline at full width: **2:1 to 3:1** (w:h).

**Measured check.** Across 2730 Fig. 1 crops from ICLR/ICML/NeurIPS/CVPR/ACL/AAAI
2023–2025 the median is **2.32:1** (p25–p75 1.85–2.87), so the range above is the
empirical norm rather than a preference. What that corpus penalises is *square*,
not *extreme*. Full table, provenance and the caveats: `exemplars.md`.
- A four-stage L→R pipeline at 6.75 in wide should be roughly **1.7–2.5 in tall**.
- Multi-panel method figures: give the hero schematic **45–60% of the height**,
  support panels a shorter row below (height ratio ≈ `[2.2, 1.0]`).

At 140 mm, a 2:1 figure is 70 mm tall. That is the budget your type size is
competing for: a taller figure at the same content density means smaller type
after scaling, so aspect and font size are the same decision.

## Capacity budget

The only explicit module budget found in the literature, and it matches what
reviewers complain about:

| Slot | Primary modules | Arrows |
| --- | --- | --- |
| Single column | 5–7 | 6–10 |
| Full page | 8–12 | 12–18 |

Figures with 15+ modules, 30+ arrows, and paragraph-length labels get rejected in
review as unclear. **Group before you grow:** if you have more than ~8 top-level
entities, merge them into sections and show the sections.

A module that carries no distinct inference is not a module — it is decoration.

## Practical consequences

- **Half-width at ICML/AAAI is ~84 mm.** An L→R pipeline with more than four
  modules will not fit legibly. Go full width, or stack vertically.
- **NeurIPS/ICLR figures are read on screen at 140 mm.** The 7 pt effective floor
  is the right working target; the 5 pt floor is a print-production limit, not a
  design goal.
- **Decide the width before you draw.** It sets the canvas, which sets the
  achievable type size, which constrains how much you can say. Choosing the width
  afterwards is how figures end up unreadably dense.
