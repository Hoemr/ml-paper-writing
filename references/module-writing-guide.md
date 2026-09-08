# Module Writing Guide — Per-Section Role Templates

> Action layer. Universal paragraph-role templates plus Kaiming He variants for the four high-leverage sections (Abstract, Introduction, Related Work, Conclusion). Method and Experiments already have working templates in [SKILL.md](../../SKILL.md) § End-to-End Workflow and are not duplicated here.
>
> Sentence-level mechanics (subject-verb proximity, stress position, hedging) live in [writing-guide.md](writing-guide.md). Cross-cutting tone rules (active voice, banned openings, vocabulary) live in [writing-style.md](writing-style.md). He-specific overlays live in [styles/kaiming-he-style.md](styles/kaiming-he-style.md). This file links out rather than restating those rules.

## How to use this file

For each section:

1. Choose the **pattern** that matches the paper type (Challenge-Contribution, Multiple Contributions, …).
2. Assign each paragraph a **role** from the table.
3. Decide **register**: universal or He. He applies when the paper type matches the table in [styles/kaiming-he-style.md](styles/kaiming-he-style.md) § When to use this style. Otherwise stay universal.
4. Run the **deliverable check** before moving on.
5. Cross-check with the **claim-evidence map** to ensure every paragraph forwards a claim that later evidence anchors.

If a paragraph has no assigned role, rewrite it. If a role appears twice, merge or split.

---

## 1. Abstract

### 1.1 Three universal patterns

| Pattern | Use when | Paragraph roles |
|---------|----------|-----------------|
| Challenge → Contribution | One technical contribution solves one bottleneck | task, challenge, contribution, benefit, evidence |
| Challenge → Insight → Contribution | The novelty is an insight before an implementation | task, challenge, insight, implementation, evidence |
| Multiple Contributions | Two or three separable technical contributions | task, contribution+advantage, contribution+advantage, result |

### 1.2 He variant — observation-first, 6 sentences

When the paper is empirical and observation-driven, replace the pattern with a He-style 6-sentence template:

1. **Counterintuitive observation** — the empirical result that motivates the work.
2. **Problem restatement** — why the observation is a problem, not just a curiosity.
3. **Two core designs** — the atomic contributions, named explicitly.
4. **Headline number** — one concrete quantitative result.
5. **Implication** — what the result enables or changes.
6. **Scope boundary** — what the result does not establish.

Skip the insight step (He papers rarely introduce a separate insight before the implementation; the observation itself is the insight).

For full He register (sentence-level, vocabulary), apply [styles/kaiming-he-style.md](styles/kaiming-he-style.md) on top.

### 1.3 Universal deliverable check

- [ ] Length: 5-8 sentences, or 150-250 words (venue-dependent — verify against the call).
- [ ] Sentence count matches the chosen pattern.
- [ ] One number appears in the abstract (headline result or evaluation setting).
- [ ] No citation pile-up (>2 citations in one sentence).
- [ ] No banned opening (`Recently, X has achieved…`). See [writing-style.md](writing-style.md) § Banned openings.
- [ ] No acronym appears without first-mention expansion.
- [ ] Scope boundary is explicit (no universal claims).

### 1.4 Cross-references

- Narrative principle (What / Why / So What) — [writing-guide.md § The Narrative Principle](writing-guide.md#the-narrative-principle).
- Farquhar 5-sentence formula (alternative universal template) — [writing-guide.md § Abstract Writing Formula](writing-guide.md#abstract-writing-formula).
- Generic opening blacklist — [writing-style.md](writing-style.md) § Banned openings.

---

## 2. Introduction

### 2.1 Six paragraph roles

Assign each paragraph exactly one role. Merge if two roles fit one paragraph; split if two paragraphs share a role.

| Role | Content | Failure signal |
|------|---------|----------------|
| Task / application opening | Define the task or use case and the target requirement | Opens with field-level slogan, no task boundary |
| Prior-work limitation | Summarise representative methods by mechanism and shared limitation | Paper-by-paper list with no technical reason |
| Technical bottleneck | State the unresolved challenge and its root cause | Gap is a marketing claim, not a mechanism |
| Proposed solution | Introduce the pipeline or key insight, anchor to a figure if present | Method appears before the challenge is clear |
| Why it works | Explain the technical advantage in bounded terms | Claims novelty without mechanism |
| Evidence / contributions | Preview experiments and enumerate contributions | Contributions do not map to later evidence |

### 2.2 Four intro patterns (universal)

| Pattern | Use when |
|---------|----------|
| Task first | Niche task; reader needs the input/output contract before applications |
| Application first | Familiar task; open with the use case and the target requirement |
| General-to-specific | New setting inside a familiar area |
| Open with challenge | The unresolved failure case is immediately understandable |

### 2.3 He variant — 4 paragraphs, numbered perspective list

When in He register, replace the six-role structure with:

1. **Observation** — counterintuitive result as Figure 1 (often the only figure referenced in this paragraph).
2. **Problem reframe** — restate the observation as a problem with a precise boundary.
3. **Two core designs** — name them explicitly, possibly via `(i) … (ii) …` numbered perspectives that dissect the problem before the solution.
4. **Contributions and evidence** — 2-4 bullets, each falsifiable, each pointing to a specific table or figure later.

Method should start by the second column-inch or the second page — same constraint as the universal intro, just with a more compressed narrative.

### 2.4 Anti-pattern (universal + He)

Do not write the story as "a naive baseline exists, then we patch it." That makes the contribution look obvious. Instead, identify the real technical bottleneck that prior families of methods still cannot resolve.

### 2.5 Deliverable check

- [ ] Every paragraph has exactly one role from § 2.1 (universal) or § 2.3 (He).
- [ ] Length ≤ 1.5 pages in two-column format; method starts by page 2-3.
- [ ] Contributions map forward: each contribution bullet names the table, figure, or section that supports it.
- [ ] Closing paragraph or sentence previews the evidence (headline number).
- [ ] Subject-verb proximity and stress-position rules respected — see [writing-guide.md § Sentence-Level Clarity](writing-guide.md#sentence-level-clarity).

### 2.6 Cross-references

- Contribution bullets good vs. bad — [writing-guide.md § Contribution Bullets](writing-guide.md#contribution-bullets-good-vs-bad).
- Narrative principle — [writing-guide.md § The Narrative Principle](writing-guide.md#the-narrative-principle).
- Time allocation (intro gets equal weight as abstract + figures) — [writing-guide.md § Time Allocation](writing-guide.md#time-allocation).
- He signature sentence patterns — [styles/kaiming-he-style.md](styles/kaiming-he-style.md) § He signature sentence patterns.

---

## 3. Related Work

### 3.1 Five-role paragraph template (universal)

| Order | Role | Content |
|-------|------|---------|
| 1 | Topic scope | What line of work is being discussed |
| 2 | Representative methods | Compact summary of shared paradigm |
| 3 | Comparison | Mechanism, assumption, strength, trade-off versus this paper |
| 4 | Limitation | What remains unresolved for the target challenge |
| 5 | Bridge | How the current paper differs, without overclaiming |

### 3.2 Topic-cluster design (universal)

Use 2-4 focused clusters. A common 4-cluster split:

1. Mainstream methods for the task
2. Methods closest to the core idea
3. Auxiliary techniques or theory the method builds on
4. Evaluation settings or datasets that define the gap

Merge adjacent clusters if a cluster has fewer than ~5 citations.

### 3.3 Rewrite chain (universal)

When revising a list-shaped related-work section, walk this chain:

```
Consensus → Disagreement → Limitations → Gap → This paper
```

Preserve existing citation anchors. Do not add new citations unless the user has authorised a literature pass.

### 3.4 He variant — ≤ 1 page, often merged into the introduction

When in He register, write Related Work as a single subsection at the tail of the introduction (≤ 1 page). Compress the five-role template into one paragraph per cluster, dropping the explicit "limitation" row in favour of the cluster's contribution bullet earlier in the intro.

Use He register when the cluster count is ≤ 3 and the distinctions are mechanistic rather than empirical.

### 3.5 Universal safety rules

- A citation key only proves the source is cited; it does not prove it supports the gap claim. Cross-check the strongest baseline.
- Do not hide the strongest baseline. If missing from the draft, flag the missing comparison instead of writing around it.
- Do not turn "few papers discuss X" into "no work has studied X" unless verified.
- Use bounded distinction language: `differs from`, `targets`, `focuses on`, `complements`, `addresses the setting of`.

### 3.6 Deliverable check

- [ ] Every cited paper is attached to a claim it supports (no citation piles).
- [ ] Each cluster follows the five-role template (universal) or the single-paragraph compression (He).
- [ ] The strongest baseline is present and compared.
- [ ] Distinction from this paper uses bounded verbs (`differs / targets / focuses on / complements / addresses`).
- [ ] Length ≤ 1 page (universal target) or ≤ 1 page merged into intro (He).

### 3.7 Cross-references

- Methodological vs paper-by-paper rationale (one-paragraph summary, kept here as the legacy phrasing) — see also [SKILL.md § Write Related Work as Comparison](../../SKILL.md).

---

## 4. Conclusion

### 4.1 Five required roles (universal)

| Order | Role | Content |
|-------|------|---------|
| 1 | Solved problem | Restate the target problem and core technical idea |
| 2 | Evidence recap | Summarise the strongest supported finding with setting boundary |
| 3 | Implication | State what the result enables or suggests |
| 4 | Limitation | Name a real scope boundary without undermining the contribution |
| 5 | Future work | Connect the limitation to a specific next direction |

### 4.2 Closure check

Cross-check every Introduction promise against the Conclusion answer:

```
Intro claim: ...
Conclusion answer: ...
Evidence anchor: ...
Status: closed / weakly closed / missing
```

If a promise is not answered, add a bounded answer only when evidence exists. Otherwise flag the missing evidence rather than smoothing over the gap.

### 4.3 He variant — ≤ 1 paragraph, do not restate

When in He register, collapse roles 1-3 into a single sentence ("We have shown that X achieves Y in setting Z") or skip them entirely. Spend the paragraph on:

- One honest limitation (not a self-criticism disguised as modesty)
- One specific future direction (concrete enough to be falsifiable)

Title convention: `Discussion and Conclusion` rather than `Conclusion` — leaves room for the forward-looking paragraph without claiming completeness.

### 4.4 Safe wording vs avoid wording

| Safe | Avoid |
|------|-------|
| `The presented results indicate … in the evaluated setting.` | `This solves …` (when only a benchmark subset is tested) |
| `A current limitation is …` | `The method is universally applicable …` (without cross-domain evidence) |
| `Extending the method to … remains an important direction.` | `Future work will improve performance.` (vague) |
| `[Result] holds under [assumptions].` | `[Result] holds.` (no boundary) |

### 4.5 Deliverable check

- [ ] Length ≤ 1 page (universal) or ≤ 1 paragraph (He).
- [ ] Five roles appear in order (universal) or limitation + future work only (He).
- [ ] Every Introduction promise has a closure row in the § 4.2 table.
- [ ] No new claim introduced that was not in the body.
- [ ] Future work is specific and falsifiable (not "improve performance" or "explore more applications").
- [ ] Future-work paragraph is 2-4 sentences (per project memory).

### 4.6 Cross-references

- Limitations honesty principle — [SKILL.md § Write Limitations and Conclusion](../../SKILL.md).
- Future-work paragraph length (project memory: 2-4 sentences) — apply in § 4.3 and § 4.5.

---

## Quick role lookup (one-page summary)

If you only have time to scan one page before drafting, this is the contract for each section.

| Section | Universal roles | He variant | Length budget |
|---------|-----------------|-----------|---------------|
| Abstract | 3 patterns × sentence budget | 6-sentence observation-first | 5-8 sentences / 150-250 words |
| Introduction | 6 roles + 4 patterns | 4 paragraphs + numbered perspectives | ≤ 1.5 pages |
| Related Work | 5 roles × 2-4 clusters | ≤ 1 page, often merged | ≤ 1 page |
| Conclusion | 5 roles + closure check | 1 paragraph, no restatement | ≤ 1 page / ≤ 1 paragraph |

For the discipline that applies across all four sections (claim-evidence alignment, terminology consistency, no overclaim), run [writing-style.md](writing-style.md) § Claim-evidence discipline.

For the deliverable gate that runs after all four sections are drafted, see [SKILL.md § 8. Run the Delivery Gate](../../SKILL.md).
