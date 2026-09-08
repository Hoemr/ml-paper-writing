# Rebuttal Guideline — Bridge from Paper Writing to Response Letter

> This file is the dispatcher from ml-paper-writing into the dedicated [reviewer-response-rebuttal-skill](file:///C:/Users/14417/.claude/skills/reviewer-response-rebuttal-skill/SKILL.md). It does not duplicate the 12 reference files or 4 templates in that skill; it adds the project-level overlays that apply only inside this Overleaf repo (jmlr2e style, shared theorem counter, red/blue markers) and gives a state-based routing rule for "what to read next."

If you have already received a decision letter and need to write a response, jump to [§ 4 Decision-tree dispatch](#4-decision-tree-dispatch) and pick the row that matches your situation.

## 1. When this guideline applies

| Trigger | You are in |
|---------|-----------|
| "I just got the reviewer comments" | **Rebuttal phase** — go to § 4 |
| "I need to revise the manuscript" | **Manuscript revision phase** — see [module-writing-guide.md](module-writing-guide.md) § 2.5 deliverable check, then come back here for overlay rules |
| "I want to add new citations / verify a reviewer challenge to a citation" | **Citation audit phase** — see [citation-workflow.md § Auditing References That Already Exist](citation-workflow.md#auditing-references-that-already-exist-in-a-draft) |
| "I want to pre-empt reviewer concerns before submission" | **Pre-submission polish** — see [writing-style.md § Pre-delivery gate](writing-style.md#pre-delivery-gate) and the de-AI pass |

If multiple phases overlap (typical: manuscript revision + rebuttal at the same time), work in this order: manuscript first, then rebuttal cross-refs, then compile, then rebuttal prose.

## 2. Skill boundary

| Lives here (ml-paper-writing) | Lives in reviewer-response-rebuttal-skill |
|------------------------------|------------------------------------------|
| Project-level MUST overlays (this file, § 3) | 12 numbered references: mindset, anatomy, structure, point-by-point, tone, agreeing, disagreeing, conflicts, request types, cover letter, checklist, phrase bank |
| ml-paper-writing → rebuttal handoff (§ 5) | 4 templates: response-letter, point-by-point table, cover letter, phrase bank |
| Cross-phase state check (§ 6) | Diagrams: rebuttal-flow |

Read [reviewer-response-rebuttal-skill/SKILL.md](file:///C:/Users/14417/.claude/skills/reviewer-response-rebuttal-skill/SKILL.md) once at the start of every rebuttal cycle; it lists which of the 12 references to load for which scenario. Do not load all 12 at once.

## 3. Project-level MUST overlays

These rules apply to this Overleaf repo specifically. They are NOT covered by the rebuttal skill's general guidance — they come from accumulated project memory and must be enforced every time.

### 3.1 Manuscript ↔ rebuttal cross-reference rules

| File | Allowed reference style | Why |
|------|------------------------|-----|
| `sample.tex` (manuscript body) | **Must use** `\cref / \ref / \eqref / \autoref` against manuscript `\label` | LaTeX auto-numbers; keeps cross-refs consistent |
| `rebuttal/reviewer*.tex`, `rebuttal/main.tex` | **Must NOT use** `\cref / \ref / \eqref / \autoref / \pageref` against manuscript `\label` | Rebuttal compiles independently; manuscript `\label`s are undefined → renders as `??` |

**Worked example** for the same sentence:

```latex
% manuscript/sample.tex — correct
As shown in Lemma~\ref{lemma:rbf-density}, ...
The reported OS-DRE model fixes the temporal centers
(Section~\ref{subsec:reproducibility}).

% rebuttal/reviewer2.tex — correct
As shown in Lemma~7, ...
The reported OS-DRE model fixes the temporal centers (Section~5.1).
```

**Self-check after every edit**:

```bash
# Should print 0 matches unless the \label is defined inside reviewer*.tex itself
grep -E '\\(cref|ref|eqref|autoref|pageref)\{' rebuttal/reviewer*.tex
```

**Permitted exception**: `\cref / \ref` is allowed against `\label`s **defined inside the same reviewer*.tex file** (e.g. `\label{eq:osdre-fixed-sample-integral}`), because they share the compilation unit.

### 3.2 Future-work paragraph length

| Location | Length | Content placement |
|----------|--------|------------------|
| `sample.tex` future-work paragraph (manuscript main text) | **2-4 sentences** | Brief pointer: "Extending X to Y is an important direction." |
| Rebuttal response explaining the future work | **As long as needed** | Full technical analysis (fill distance, mesh ratio, optimization geometry, non-convex optimization layers) belongs here, not in the main text |

Rationale: reviewer's-eye detail (e.g. mesh-ratio tradeoffs) belongs in the rebuttal because that is the only place reviewers see it; the main text only needs a bounded pointer.

### 3.3 Compile gate

After **every** edit to `sample.tex` or any `rebuttal/reviewer*.tex`, run:

```bash
latexmk -pdf sample.tex        # manuscript
latexmk -pdf rebuttal/main.tex # rebuttal (each reviewer*.tex is included)
```

Verify:

- No `??` (undefined cross-reference) anywhere in the output PDF
- No overfull `\hbox` warnings on title pages or captions
- Page count within venue limit
- `rebuttal/reviewer*.tex` has zero `\\cref\{|\\ref\{|\\eqref\{|\\autoref\{|\\pageref\{` matches against manuscript labels (run the grep above)

If compile breaks, do not start the next edit; fix the build first.

### 3.4 Red / blue markers in the manuscript

`{\color{red}}` and `{\color{blue}}` in `sample.tex` mark revision deltas and **must not be removed** until camera-ready. Their meaning:

| Marker | Meaning |
|--------|---------|
| `{\color{red}…}` | Removed or replaced text |
| `{\color{blue}…}` | Added or modified text |

When updating `sample.tex` for a reviewer comment, preserve or update these markers — they are what reviewers see in the tracked-diff view. Removing them silently looks like a stealth edit.

### 3.5 Shared theorem counter (jmlr2e.sty)

`jmlr2e.sty` shares one counter across `theorem`, `lemma`, `proposition`, `corollary`. Therefore `\cref` against any of these renders as **"Theorem N"**, never "Lemma N" or "Corollary N".

In manuscript main text, when the actual environment is a corollary but `\cref` would say "Theorem", you have two options:

| Option | When to use |
|--------|-------------|
| Write `Corollary~\ref{cor:foo}` (literal word, numbered reference) | When the corollary is the centre of the sentence and "Corollary" must be visible |
| Write `the result of Theorem~N` (use the rendered number, drop the type) | When you want to avoid contradicting the counter — common when citing across environments |

In rebuttal, use literal text (`Theorem~7`) — see § 3.1.

### 3.6 Main-text reference to appendix corollary

When the main text needs to refer to a corollary that lives in the appendix:

| ❌ Don't restate notation | ✅ Generic pointer |
|---------------------------|-------------------|
| "By Corollary~\ref{cor:kfbias}, which bounds $K^{-2\beta}\\|\mu\\otimes\mathrm dt\\|_\\infty$ on compact supports, …" | "By the corollary in Appendix~A (and [cref] for the precise statement), …" |

The first form duplicates appendix notation into the main text and creates two sources of truth. The second uses a generic pointer plus a `\cref` link; readers who need the notation click through.

## 4. Decision-tree dispatch

Match your current state to a row, then read the listed rebuttal-skill files **in order** (left to right).

| Your situation | Read first | Read next | Templates |
|----------------|-----------|-----------|-----------|
| Decision letter just arrived, you haven't parsed it yet | `00-mindset-and-triage.md` | `01-decision-letter-anatomy.md` | `templates/point-by-point-table.md` |
| Major / minor / R&R decided, you have a comment list | `02-response-letter-structure.md` | — | `templates/response-letter-template.md` |
| Writing each per-comment response now | `03-point-by-point.md` | `04-tone-and-diplomacy.md` | `templates/point-by-point-table.md` |
| You agree with a comment and need to write the change-confirmation | `05-agreeing-revising.md` | — | — |
| You disagree with a comment and want to push back | `06-disagreeing-respectfully.md` | `04-tone-and-diplomacy.md` | `templates/phrase-bank.md` (push-back phrases) |
| Two reviewers contradict each other | `07-conflicting-reviewers.md` | — | — |
| Reviewer asks for one of: extra analysis, more citations, deeper theory, method clarification, sample / causality concern, English polish | `08-request-types.md` (locate the matching sub-section) | `03-point-by-point.md` for the response format | — |
| You need to write the cover letter to the editor | `09-cover-letter.md` | — | `templates/cover-letter-template.md` |
| Draft is complete, about to resubmit | `10-resubmission-checklist.md` | `11-phrase-bank-cases.md` for final wording | `templates/response-letter-template.md` |
| You need a polite English / Chinese phrase | `11-phrase-bank-cases.md` | `templates/phrase-bank.md` | — |

The full flow is also drawn in `diagrams/rebuttal-flow.md`.

## 5. Handoff from manuscript revision to rebuttal

After you have edited `sample.tex` to address the reviewers, before you write the rebuttal prose:

1. **Compile the manuscript** (`latexmk -pdf sample.tex`). Resolve every `??`, every undefined citation, every overfull box. The rebuttal will quote exact text and page / line numbers from this compiled PDF.
2. **Update the red / blue markers** to reflect the final state (see § 3.4).
3. **Snapshot the page / line numbers** you will reference. Re-compile after any further edit; page numbers drift.
4. **For each cited lemma / theorem / corollary / equation in the rebuttal draft**, follow § 3.1 (literal text, not `\cref`).
5. **For each future-work pointer in the manuscript**, verify it is 2-4 sentences and that the technical depth lives only in the rebuttal (see § 3.2).

## 6. State-based cross-phase checks

Run these checks at every phase boundary.

| Boundary | Check |
|----------|-------|
| After manuscript revision, before rebuttal writing | § 5.1, 5.2, 5.3, 5.5 |
| After rebuttal drafting, before cover letter | § 3.1 (grep), § 3.3 (re-compile rebuttal), § 5.4 (cross-refs use literal text) |
| Before resubmission | All of: § 3.1, 3.2, 3.3, 3.4, 3.5, 3.6 + the rebuttal skill's `10-resubmission-checklist.md` |

If any check fails, fix the source rather than working around the failure (e.g. if a `\cref` slipped into `rebuttal/*.tex`, rewrite it as literal text; do not suppress the warning).

## 7. What this file deliberately does not cover

- Phrase bank, conflict scenarios, push-back tactics, cover-letter wording → [reviewer-response-rebuttal-skill](file:///C:/Users/14417/.claude/skills/reviewer-response-rebuttal-skill/SKILL.md)
- The 4-phase citation audit → [citation-workflow.md § Auditing References That Already Exist](citation-workflow.md#auditing-references-that-already-exist-in-a-draft) → [audit-existing-references.md](audit-existing-references.md)
- Per-module manuscript templates → [module-writing-guide.md](module-writing-guide.md)
- Universal writing philosophy → [writing-guide.md](writing-guide.md)
- Cross-cutting tone rules → [writing-style.md](writing-style.md)

If you find yourself copying content from those files here, move it back and link instead.
