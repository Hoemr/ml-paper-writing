# Audit Existing References — Read-Only Verification of a Draft's Citations

> In-skill replacement for the now-consolidated ref-check workflow. The 4-phase pipeline below lives here, not in a sibling skill, so that `ml-paper-writing` is self-contained. Companion to [citation-workflow.md](citation-workflow.md) (which covers adding *new* citations). Same trigger rules apply: **only run this when the user explicitly asks to audit, verify, or challenge existing citations**.

> **Read-only principle.** This audit never modifies the manuscript `.tex`, `.bib`, `.docx`, or any reference list. It only produces an audit report file (default `check-ref-report.md` next to the paper). The only file written outside that report is `scripts/api_keys.local.json` during Phase 0 (search configuration, not paper content). Trust in an audit depends on the auditor not perturbing the audited object.

## When to use this file

| Trigger | Why this file |
|---------|---------------|
| "Audit my references" / "verify my .bib" / "check for hallucinated citations" | Pre-submission or pre-rebuttal risk reduction |
| "Reviewer says my ref X doesn't say what I claim — check it" | Claim-support dimension (Phase 3) |
| "Check if any of my citations are swapped to wrong papers" | Truth dimension (Phase 2) with field comparison |
| "Write a section" or "edit prose" | **Do not** trigger this file — preserve existing `\cite{}` as-is |

## Phase 0 — Inventory (read-only, no edits)

1. **Detect Tavily MCP availability.** Check whether `mcp__tavily__*` tools exist in the current session. In both cases (available or not), print one status line:
   - Available: `Detected Tavily MCP — will prefer it for web verification.`
   - Not available: `No Tavily MCP detected. WebSearch will be used instead. Install Tavily (tavily.com) and register via \`claude mcp add\` to improve retrieval precision.`

   Detection runs every session (MCP availability varies per machine). Do not ask follow-up questions; do not block.

2. **Check / ask for search API keys (once).** Read `scripts/api_keys.local.json`. If the file does not exist or its `prompted` field is `false`, ask the user once via AskUserQuestion whether to provide OpenAlex / Semantic Scholar API keys. Write the answer back to `api_keys.local.json` and set `prompted: true`. If `prompted` is already `true`, skip the question. Missing or empty key fields are fine — the script auto-degrades to anonymous mode (both APIs allow it, with stricter rate limits).

3. **Identify the main file.** LaTeX: root `.tex` (containing `\documentclass`) and its `\bibliography{...}` / `\addbibresource{...}`. Word: the `.docx` itself.

4. **Read the full prose once.** No skipping, no sampling. The audit needs every citation point, not just chapters that "look reference-heavy".

5. **Parse the full `.bib` (or Word reference list).** Extract every entry: `{key/number, title, author, year, journal/booktitle, publisher, volume, issue, pages, doi}`. Handle nested braces (`title = {{Deep} Learning}`), `%` comments, and `"..."` vs `{...}` field wrappers. If `bibtexparser` is installed, use it; otherwise fall back to a brace-balanced regex. Leave `@comment` / `@string` macros for manual review rather than guessing.

6. **Identify in-text citation style.** `\cite / \citep / \citet`, numeric `[12]`, or author-year `(Smith, 2020)`. Determines how Phase 1 locates citation points.

## Phase 1 — Extract two lists (full pass, no batching)

1. **Entry list (input to Dimension 1).** The full set from Phase 0.5, numbered.
2. **Citation point list (input to Dimension 2).** For every in-text reference:
   - LaTeX: match `\cite{key1,key2}`, `\citep{...}`, `\citet{...}`, `\citeauthor{...}`, including optional args (`\cite[see][]{key}`). Multiple keys in one command split into multiple citation points but share context.
   - Word: detect style from a few samples, then full-text regex.
   - Record `{location (chapter/paragraph), key/number, cited sentence excerpt, specific claim/number/method/dataset involved}`.
   - **One sentence serving multiple distinct claims/numbers → split into multiple points.** Do not pack them together, or Phase 3 will miss "partial support" cases.
   - **Do not exclude any citation point**, even those in abstract / analysis / conclusion. This audit is "are the existing citations correct", not "should there be more citations" — the inclusion rule is opposite of search-and-add workflows.

Continue only after both lists are complete.

## Phase 2 — Dimension 1: Per-entry truth audit (full set, serial)

For each entry in Phase 1's entry list, run:

```bash
python scripts/search_paper.py --doi <doi>              # when DOI is available, prefer this
python scripts/search_paper.py "<title>" --limit 5     # otherwise fall back to title search
```

**Strictly serial.** One entry's script query + field comparison completes before the next begins. Do not fan out to subagents; do not concatenate queries. Rationale: OpenAlex / Semantic Scholar rate-limit per IP / API key, and concurrency raises 429 probability; serial is fast enough for paper-scale entry counts. WebSearch is a separate channel — see Phase 2.3 for its parallel batching.

1. Query the script for authoritative record (title / authors / year / journal or conference / publisher / volume / issue / pages). Strip LaTeX math or special chars from titles before searching (e.g. `$...$`, `\textit{}`).
2. Compare fields using the [Field comparison rules](#field-comparison-rules) below. Critical fields must agree; minor fields can differ with a note.
3. **WebSearch independent confirmation (batched 5/parallel).** Use a simplified query (`"<title>" <first-author-surname> <year>`). Don't pack the query with every field — longer queries degrade search quality. For DOI-bearing entries, a lightweight WebFetch of `https://doi.org/<doi>` is a faster alternative. For non-DOI entries, escalate to additional queries with more qualifying terms. Both script field-comparison AND WebSearch must pass; record which one failed if either does.
4. Handle rate limits with the [backoff strategy](#rate-limit-handling) below.

### Field comparison rules

| Severity | Field | Compare how | Action on mismatch |
|----------|-------|-------------|---------------------|
| Critical | Title | Allow case / hyphen / post-colon subtitle differences; substantive word change fails | Mark **fail** |
| Critical | Authors | At least first and last (corresponding) surnames must match; missing middle authors tolerated if data source differs | Mark **fail** if entirely different list |
| Critical | Year | Must match exactly; if `.bib` notes preprint-vs-published ambiguity, compare against the declared version | Mark **fail**; record "year ambiguity" for downstream review |
| Minor | Journal / conference | Allow full-name ↔ abbreviation equivalence (`CVPR = IEEE Conference on Computer Vision and Pattern Recognition`); model judges equivalence | Mark **pass**, note difference |
| Minor | Publisher | Same as journal | Mark **pass**, note difference |
| Minor | Volume / issue / pages / DOI | Exact match preferred; if DOI mismatches but title/authors/year agree, trust the script's DOI | Mark **pass**, note difference |

**Decision rule.** One critical-field mismatch OR both sources unable to find the paper → entry fails Dimension 1. Minor-field mismatches alone → entry passes, with differences recorded in the report's "field-difference notes" column.

### WebSearch query simplification

Default query: only `"<title>" <first-author-surname> <year>`. Longer queries degrade results. Only escalate to longer queries (DOI, full venue, full author list) when the simplified query returns ambiguous results.

### Layered confirmation strategy

| Entry condition | WebSearch / WebFetch effort |
|-----------------|----------------------------|
| Has DOI | Lightweight: one simplified query, OR WebFetch `https://doi.org/<doi>` |
| No DOI | Heavier: simplified query + at least one more precise query with author / venue terms |
| Script already found field differences | Escalate: 1-2 additional queries from different angles; WebFetch the candidate page if needed |

### WebSearch batched parallel

Fixed 5 entries per batch. Fire all 5 WebSearch / WebFetch calls in one turn; wait for the batch to return before analysing. Then start the next batch. Do not apply the script's serial rule to WebSearch — they are independent channels.

## Phase 3 — Dimension 2: Per-citation-point claim audit (serial, no WebSearch)

For each citation point in Phase 1's citation point list, **strictly serial** (same rate-limit rationale as Phase 2):

1. If the key was already fetched with an abstract in Phase 2, reuse it. Otherwise call `scripts/search_paper.py` again by title or DOI to get the abstract.
2. Apply the [Claim-match criteria](#claim-match-criteria) below. Substantive support from the abstract is required, not just topic overlap.
3. Categorise any "questionable" point into one of: **unsupported by abstract / topic-level false positive / abstract unavailable / number-or-method mis-attribution**, and write the specific concern.

WebSearch is NOT used in this phase — Dimension 1 already exhausted web confirmation; Phase 3 judges purely against the abstract.

### Claim-match criteria

| Situation | Verdict |
|-----------|---------|
| Abstract's subject has substantive overlap with the citation's claim | Pass |
| Abstract's subject is only topically related but not the same sub-field | **Questionable: topic-level false positive** |
| Citation attributes a specific number; abstract's task / dataset / metric roughly matches | Pass (with note) |
| Citation attributes a specific number; abstract's task / dataset / metric does not match | **Questionable: number attribution uncertain** |
| Citation names a method / dataset; cited paper is the original proposer or has substantive discussion | Pass |
| Citation names a method / dataset; cited paper only mentions it in passing | **Questionable** |
| Abstract unavailable after two attempts (DOI + title) | **Questionable: cannot judge** (do not default to pass) |

## Phase 4 — Report

Produce the only output artefact: `check-ref-report.md` next to the paper. If the file exists, ask the user (overwrite vs. timestamped filename like `check-ref-report-20260706.md`); never silently overwrite history. If the user says "tell me in chat only", skip the file.

The report template is in [§ Report template](#report-template) below.

## Phase summary table

| Phase | Input | Tool | Output | Concurrency |
|-------|-------|------|--------|-------------|
| 0 | Main file path | Read / AskUserQuestion | Inventory state | — |
| 1 | Phase 0 inventory | Regex / parser | Entry list + citation point list | — |
| 2 | Entry list | `scripts/search_paper.py` (serial) + WebSearch (5/batch) | Per-entry pass/fail with notes | Script serial; WebSearch 5/batch parallel |
| 3 | Citation point list | `scripts/search_paper.py` (serial, abstract only) | Per-point pass/questionable with category | Strict serial |
| 4 | Phase 2 + 3 results | Markdown formatter | `check-ref-report.md` | — |

## Rate-limit handling

Both APIs back off with cascading waits:

| API | On 429 |
|-----|--------|
| OpenAlex | Script retries once with the configured API key; if still 429, waits 5 s and retries once more |
| Semantic Scholar | Wait 5 s, then 10 s; if still failing, do not force — OpenAlex usually has enough coverage |

If both APIs miss after retries, record the entry as "no authoritative record found — truth audit incomplete" rather than marking it as failed. Never judge fail from a transient 429 alone.

## scripts/search_paper.py usage

```bash
python scripts/search_paper.py "ResNet deep residual learning" --limit 5
python scripts/search_paper.py --doi 10.1109/CVPR.2016.90
python scripts/search_paper.py "contrastive learning" --author "Chen" --year 2020 --json
```

Returns candidates from OpenAlex and Semantic Scholar with: title, authors, year, DOI, venue, publisher, volume, issue, pages, citation count, abstract. `--author` and `--year` are advisory only — printed as a reminder for human verification, never used to auto-filter. Prefer `--doi` when available; it is more robust against same-titled paper confusion.

## Report template

```markdown
# Reference audit report — <paper title or filename>

Generated: <date>
Scope: <.bib path> with <N> reference entries; <M> citation points in the prose

## Summary

| Dimension | Total | Pass | Fail / questionable |
|-----------|-------|------|---------------------|
| Dimension 1: Entry truthfulness | N | ... | ... |
| Dimension 2: Citation claim support | M | ... | ... |

## Dimension 1: Entry truthfulness

### Passed

| # | Key/number | Title | .bib field summary | Field-difference notes |
|---|------------|-------|--------------------|------------------------|
| 1 | he2016deep | Deep Residual Learning for Image Recognition | He et al., 2016, CVPR | none |

### Failed

| # | Key/number | Title (.bib record) | Mismatched field | .bib value | Verified correct value | Verification method | Note |
|---|------------|---------------------|------------------|------------|------------------------|---------------------|------|
| 1 | smith2019x | ... | year | 2019 | 2018 | script (OpenAlex) + WebSearch | .bib year wrong; actually 2018 |
| 2 | wang2020y | ... | whole entry | — | not found | script + WebSearch both missed | possibly fabricated or title severely wrong |

## Dimension 2: Citation claim support

### Passed

| # | Location (chapter/paragraph) | Key | Cited excerpt | Support basis (abstract point) |
|---|------------------------------|-----|---------------|--------------------------------|
| 1 | Introduction §2 | he2016deep | "...residual networks significantly alleviate the degradation problem..." | abstract explicitly proposes residual learning to address deep-network degradation |

### Questionable

| # | Location | Key | Cited excerpt | Concern type | Note |
|---|----------|-----|---------------|--------------|------|
| 1 | Related Work §1 | zhang2021z | "...contrastive learning is widely used in reinforcement learning..." | topic-level false positive | that paper's abstract discusses contrastive learning in image domain, not RL |
| 2 | Introduction §3 | li2018w | "...reaches 95% accuracy on ImageNet..." | abstract unavailable | script did not return an abstract; cannot confirm the number originates from this paper |

## Conclusion and recommendation

- The <k> Dimension 1 failures should be checked entry by entry, with .bib fields corrected or the cited paper replaced as appropriate.
- The <j> Dimension 2 questionable points should be re-read in context; either swap the citation or rewrite the sentence to better match what the cited paper actually says.
- This report is a read-only audit result. No modifications were made to the manuscript text or .bib file.

## What this file deliberately does not cover

- Forward citation search (adding new citations) → [citation-workflow.md](citation-workflow.md) § Verified Citation Workflow
- Per-module manuscript writing templates → [module-writing-guide.md](module-writing-guide.md)
- Universal writing philosophy → [writing-guide.md](writing-guide.md)
- Cross-cutting tone rules → [writing-style.md](writing-style.md)
