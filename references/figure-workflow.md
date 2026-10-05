# From paper narrative to a method figure

This is the bridge from writing to drawing. `$ml-method-figure` owns TikZ
construction, venue-width/type checks, mechanical QA and visual-review rules.
Read its SKILL.md before a drawing task. In this personal installation it is at
`/Users/wei/.codex/skills/ml-method-figure/SKILL.md`; the `.cc-switch` path resolves
to the same skill. If unavailable, report that dependency rather than pretending
its QA ran. Do not copy its thresholds or rule tables into this skill.

## Narrative → design contract

Read the live manuscript, method equations/algorithm, existing figures/README,
figure source/design record and git state. State the contribution from that
evidence. For a proposed revision, identify which variant the diagram depicts
and which variant the experiments evaluate.

Decide whether the job is a whole-method overview, a local mechanism, a control
comparison, or measured evidence. One figure has one primary task. Freeze the
claim, reading path, hero, language, shape roles, edge legend, style and print
envelope using ml-method-figure's contract. Preserve canonical method names.

Before writing coordinates, explain the composition: meaningful regions,
alignment groups, repeated structures, what changes between branches, and the
main/secondary routes. Keep this in the existing design record or source comments;
do not require a separate brief/spec/plan document trio. In a comparison, keep
the shared structure stable and make the actual changed field easy to locate.
Design from the mechanism; references guide density and restraint, not content.

## Contract → TikZ → QA → independent vision

Follow ml-method-figure's overview-first and by-construction routes, author the
standalone TikZ, and run its `scripts/qa.sh` for the actual insertion width.
Repair every HARD and assess each warning from the render. Also inspect the
compiler log against the paper-writing quality gates; a CLEAN QA verdict can
coexist with overfull text boxes. Verify coverage: computed foreach elements
may be skipped by instrumentation, so their named
parent must enclose the full repeated object. Source naming is not proof of coverage.

Then apply its review checklist to color, grayscale, final-width render and
manuscript insertion. Inspect connector crossings separately because node
geometry does not instrument paths. Obtain an independent blank-context visual
pass as required by that skill. Semantic checking still requires comparing the
figure with the method; a PNG-only reviewer cannot establish that agreement.

Deliver source, PDF and review PNG with paths, QA outcomes, unresolved assumptions
and caption. A clean gate is a mechanical floor, not evidence for a claim or
permission to declare publication readiness.

## External lessons and limits

FigGenie contributes content-derived composition plans, stable repeated layout
with highlighted differences, and inspecting real print-size output. We adapt
these to the local TikZ workflow. Its SVG/PPTX pipeline, separate JSON spec,
mandatory brief approval, corpus statistics and thresholds are not imported.
Canonical links and inspected revisions live in [sources.md](sources.md).
