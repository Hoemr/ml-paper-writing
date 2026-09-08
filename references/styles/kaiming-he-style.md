# Kaiming He Style — A Vertical Case Study

> Single-author exemplar for "empirical, observation-first, minimalist" ML papers.
> Use this as a vertical slice through the universal philosophy in [writing-guide.md](../writing-guide.md) and the cross-cutting rules in [writing-style.md](../writing-style.md), not as a replacement.

Source corpus: ResNet (CVPR 2016), Focal Loss (ICCV 2017), Mask R-CNN (ICCV 2017), MoCo (CVPR 2019), MAE (CVPR 2022). Distilled structure patterns are cross-checked with [K-Dense-AI/mimeographs/kaiming-he](https://github.com/K-Dense-AI/mimeographs/tree/main/mimeographs/kaiming-he) principles (residual learning, activation-aware init, generative as universal solver, simplicity in complexity, AI as common language).

## When to use this style

| Match well | Do not force this style |
|------------|------------------------|
| Empirical CV / ML method paper with 1-2 design choices | Pure theory paper (He style mostly avoids proofs in main text) |
| A surprising empirical observation motivates the method | Survey / benchmarking paper (too many contributions to compress) |
| The contribution can be stated as "two core designs" | Engineering-heavy systems paper (needs different structure) |
| Ablation tables isolate each design choice cleanly | Resource / dataset paper (no method to ablate) |

If two of the "match well" column are true, lean He. If two of the "do not force" column are true, use the universal philosophy in [writing-guide.md](../writing-guide.md) without He-specific overlay.

## The one-line philosophy

**Observation first, simple fix second, ablation as proof, conclusion as opening.**

Everything below is operationalisation of these five words.

## The 10-item checklist

Run this against a full draft. If more than three items fail, the paper is not yet in He register.

| # | Item | Pass criterion |
|---|------|----------------|
| 1 | Opening observation | First section (or first paragraph of intro) presents a counterintuitive empirical result, often as Figure 1 |
| 2 | Two core designs | Contribution can be compressed into ≤ 2 atomic ideas; introduction names them explicitly |
| 3 | Numbered perspective list | Introduction uses `(i)(ii)(iii)…` numbered points to dissect the problem before proposing the answer |
| 4 | Lean method section | Method body is ≤ 2 pages (excluding appendix); one key equation, one figure |
| 5 | Ablation first | Experiment section opens with a dedicated ablation subsection that isolates each design choice |
| 6 | One table per claim | Each table or figure answers one question; no "miscellaneous results" tables |
| 7 | Minimal related work | Related work is ≤ 1 page, often merged into the tail of the introduction |
| 8 | Non-restating conclusion | Conclusion is ≤ 1 paragraph, states limitation and future direction, does not restate the contribution |
| 9 | Declarative voice | Sentences start with `We observe / find / develop / show`; no `very / remarkably / significantly` |
| 10 | Figure 1 is an observation, not an architecture | The first figure shows the empirical phenomenon or input/output example, not the method diagram |

## He signature sentence patterns

Use these as templates. Replace bracketed slots with the actual content; do not copy the templates verbatim into the paper.

- **Observation framing**: `[Surprising empirical result]. This is not caused by [common misconception].`
  - ResNet: `When deeper networks are able to start converging, a degradation problem has been exposed: with the network depth increasing, accuracy gets saturated and then degrades rapidly.`

- **Reframe**: `Rather than [standard formulation], we [new formulation].`
  - MoCo: `We maintain a dictionary to look up keys... Momentum updating makes this dictionary evolve smoothly.`

- **Simplicity claim**: `Our approach is simple: [one sentence method].`
  - MAE: `Our MAE approach is simple: we mask random patches of the input image and reconstruct the missing pixels.`

- **Numbered perspective**: `(i) [aspect A]. (ii) [aspect B]. (iii) [aspect C]. These differences lead us to [design choice].`
  - MAE introduction uses three numbered perspectives on vision vs. language masked autoencoding.

- **Ablation spine**: `We ablate each design choice in Table N. Removing [X] drops accuracy by Y%, suggesting [interpretation].`

- **Honest boundary**: `[Method] works in [setting]. It remains unclear whether [open question].`

For sentence-level mechanics that underlie these patterns (stress position, subject-verb proximity, old-before-new), see [writing-guide.md § Sentence-Level Clarity](../writing-guide.md#sentence-level-clarity). For the cross-cutting tone rules, see [writing-style.md](../writing-style.md).

## Vocabulary mapping (He register)

This is a subset of the general rules in [writing-style.md](../writing-style.md) § He register, kept here as a quick lookup. When in doubt, prefer the general rule.

| Avoid | Prefer |
|-------|--------|
| `very / extremely / remarkably / significantly / dramatically` | delete, or replace with the actual number |
| `state-of-the-art` | `outperforms the prior best by X% on Y benchmark` |
| `novel` (after first mention) | delete |
| `It can be seen that / It is obvious that` | `We observe that` |
| `We propose a novel framework that combines X and Y` | `We develop X. We combine it with Y.` (two sentences) |
| `In recent years, [field] has achieved great success` | delete (see [writing-style.md](../writing-style.md) § banned openings) |
| `Our method is effective` | `Our method improves accuracy by X% on Y` |

## Structural template (He-flavoured)

Apply on top of the per-module templates in [module-writing-guide.md](../module-writing-guide.md). Each module row says "if He, do X; otherwise use the universal template."

```
Title                  : Noun phrase + optional acronym (ResNet / MAE / MoCo). No "We propose".
Abstract               : 6 sentences — observation, problem, two designs, headline number, implication, scope
Introduction           : 4 sections — observation, problem reframe, two designs numbered (i)(ii), contributions
Related Work           : ≤ 1 page, often a single section after the introduction, grouped by mechanism
Method                 : ≤ 2 pages, one core equation, one architecture / data-flow figure
Experiments § Main     : ablation table first, then main comparison, then transfer / scaling
Conclusion             : ≤ 1 paragraph, limitation + future direction, no restatement
```

For full per-module role templates (universal + He variant), see [module-writing-guide.md](../module-writing-guide.md).

## What this file deliberately does not cover

- Sentence-level mechanics (Gopen & Swan 7 principles) → [writing-guide.md](../writing-guide.md)
- Word choice beyond He-specific items → [writing-guide.md](../writing-guide.md) § Word Choice
- Mathematical writing and notation → [writing-guide.md](../writing-guide.md) § Mathematical Writing
- Figure design → [writing-guide.md](../writing-guide.md) § Figure Design
- Per-module paragraph role templates → [module-writing-guide.md](../module-writing-guide.md)
- Operating cheat sheet (one page) → [writing-style.md](../writing-style.md)

If you find yourself duplicating content from those files here, move the content back to the source file and link instead.
