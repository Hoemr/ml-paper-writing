# Writing Style — Operating Cheat Sheet

> One-page cross-cutting rules. Read this before drafting a section; read [writing-guide.md](writing-guide.md) for depth and rationale; read [module-writing-guide.md](module-writing-guide.md) for per-section role templates; read [styles/kaiming-he-style.md](styles/kaiming-he-style.md) when applying the Kaiming He exemplar overlay.
>
> This file deliberately does not repeat Gopen & Swan principles, the Lipton word list, or the He vocabulary mapping in full. It links to them.

## Dispatch table

| You need to … | Read |
|---------------|------|
| Understand the narrative principle (What / Why / So What) | [writing-guide.md § The Narrative Principle](writing-guide.md#the-narrative-principle) |
| Decide sentence structure (stress position, topic position, …) | [writing-guide.md § Sentence-Level Clarity](writing-guide.md#sentence-level-clarity) |
| Pick precise words, drop hedging | [writing-guide.md § Word Choice and Precision](writing-guide.md#word-choice-and-precision) |
| Format equations, symbols, math display | [writing-guide.md § Mathematical Writing](writing-guide.md#mathematical-writing) |
| Build Figure 1 or any figure | [writing-guide.md § Figure Design](writing-guide.md#figure-design) |
| Draft Abstract / Intro / Related Work / Conclusion | [module-writing-guide.md](module-writing-guide.md) |
| Write in Kaiming He register (observation-first, two core designs, …) | [styles/kaiming-he-style.md](styles/kaiming-he-style.md) |

## Four one-liners (apply to every sentence)

1. **One verb, one action.** Nominalisations (`perform an analysis`) → verbs (`analyze`).
2. **One paragraph, one point.** If two ideas share a paragraph, split.
3. **One claim, one number.** "Improves performance" → "improves accuracy by 4.2% on CIFAR-10".
4. **One citation, one claim.** A citation pile at the end of a sentence hides the actual support.

These are the operative form of the Gopen & Swan 7 principles and the Lipton / Steinhardt word rules. For the deep mechanics, go to [writing-guide.md](writing-guide.md).

## Claim-evidence discipline (cross-cutting)

Every claim that survives into the paper must answer three questions:

| Question | Where to find the answer |
|----------|--------------------------|
| Which paragraph in the abstract or intro asserts it? | The contribution bullets |
| Which section, table, or figure anchors it? | The cross-reference (e.g., "see § 4.2, Table 2") |
| Which paragraph in the conclusion restates the bounded answer? | The closure map in [module-writing-guide.md § 4.2](module-writing-guide.md) |

If any row is blank, the claim is unanchored. Either add the anchor, weaken the claim, or drop it.

## Banned openings (do not use as the first sentence of any section)

These appear in [writing-guide.md § Abstract Writing Formula](writing-guide.md#abstract-writing-formula) and are repeated here because they are the most common failure mode at the start of a draft:

- `Large language models have achieved remarkable success …`
- `Deep learning has revolutionized …`
- `In recent years, neural networks have …`
- `Recently, X has attracted increasing attention …`
- `Inspired by …`

Replace each with the paper's specific first move (problem statement, observation, or contribution). If the first sentence could be prepended to any ML paper, delete it.

## He register (quick rules; full list in styles/kaiming-he-style.md)

When the paper matches the He-style criteria in [styles/kaiming-he-style.md § When to use this style](styles/kaiming-he-style.md), apply these three rules in addition to the universal ones:

1. Use `We observe / find / develop / show` instead of `It can be seen / We propose a novel framework`.
2. Number contributions as `(i) … (ii) …` in the introduction.
3. Ablation table comes before the main comparison table.

For the full He vocabulary mapping and signature sentence patterns, see [styles/kaiming-he-style.md](styles/kaiming-he-style.md).

## De-AI traces (tone polish)

AI-assisted drafts tend to over-produce three patterns:

| Pattern | Symptom | Fix |
|---------|---------|-----|
| Stacked intensifiers | `significantly, remarkably, substantially, dramatically` in one paragraph | Keep one if it changes meaning; delete the rest |
| Parallel tricolons | `X is fast, accurate, and scalable` with no number | Replace the last item with the actual number |
| Smoothed transitions | `Moreover, / Furthermore, / Additionally,` as paragraph openers | Replace with the actual link (`This matters because …`) |

These are operating rules, not exhaustive de-AI guidance. Apply the de-AI pass as a separate stage after the structural draft is stable.

## Pre-delivery gate (in addition to [SKILL.md § 8](../../SKILL.md))

| Check | Pass criterion |
|-------|----------------|
| Terminology consistency | One term per concept throughout (no `model / network / architecture` swapping) |
| Citation grounding | Every citation is adjacent to the claim it supports |
| Headline number audit | Every headline number in the abstract appears in the body tables/figures |
| Limitation honesty | At least one real limitation named in the conclusion |
| Anonymisation | No self-citations that reveal identity, for blind submission |

If any check fails, fix the source rather than softening the gate.

## Related files

- [writing-guide.md](writing-guide.md) — universal philosophy, sentence-level depth, math, figures
- [module-writing-guide.md](module-writing-guide.md) — per-section role templates, abstract through conclusion
- [styles/kaiming-he-style.md](styles/kaiming-he-style.md) — single-author exemplar overlay
- [SKILL.md § End-to-End Workflow](../../SKILL.md) — stage gates, claim-evidence map, delivery check
