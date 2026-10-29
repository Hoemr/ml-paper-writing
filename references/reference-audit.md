# Reference audit: identity and claim support

This is the built-in successor to check-ref. It supports LaTeX with BibTeX or
biblatex, Word manuscripts and supplied plain-text manuscripts/reference lists.
It shares identity/support rules with [citation-workflow.md](citation-workflow.md).
No separately installed skill is required.

## Activation, scope and write boundary

- Full drafting, whole-manuscript revision and a full ml-paper-writing run audit
  every entry in the manuscript's bibliography sources and every actual citation
  occurrence in the final manuscript. Include retained and newly added references.
  Label uncited entries separately; an unused library entry has no support occurrence.
- A stand-alone audit is read-only: do not alter manuscript, bibliography, citation
  fields, comments or tracked changes. Deliver findings and proposed corrections.
- During authorized writing/revision, the audit identifies issues; the writing
  workflow may implement verified corrections within its existing edit scope.
  Preserve author decisions and recheck the changed entry and affected occurrences.
  Do not silently substitute another work or change the intended claim to fit it.
- Partial edits check new, changed and directly affected references/occurrences.
  An explicit audit subset or exclusion overrides defaults; name it in the report.
- Do not repeat completed checks with unchanged sources. Reuse metadata/abstracts
  per work, but judge each occurrence's claim separately. Changed claims need a
  fresh support check even when the key is unchanged.

## 1. Build complete inventories

Read the whole in-scope manuscript, including captions, tables, footnotes and
appendix. For LaTeX follow included files and bibliography declarations from the
root document. Account for multiple .bib files, custom citation macros, optional
arguments, multi-key commands, nocite and undefined keys. Do not count commented
or inactive source as a published claim; disclose unresolved conditional content.

Parse BibTeX with a suitable installed parser or a brace-aware reader, handling
multiline and quoted values, nested braces, string macros and concatenation.
Do not silently truncate a title with a flat regular expression. Ignore comments;
inspect unsupported constructs directly and report parsing gaps.

For Word, inspect paragraphs, tables, footnotes/endnotes and citation-manager
fields as available. Determine numeric, superscript or author-year style, join
wrapped reference entries and expand numeric ranges. Preserve field codes and
document contents. If the reader omits a component, disclose it rather than
claiming full coverage. Plain text uses explicit source locations/paragraph IDs.

Create two inventories before verification:

1. Entries: key/number, title, complete author list when present, year,
   journal/conference, publisher, volume, issue, pages, DOI/arXiv ID, source file,
   cited/uncited status and declared version.
2. Occurrences: stable ID, file/section/paragraph or page, key/number, exact claim
   excerpt and the proposition/number/method/dataset being attributed. Split
   compound claims and multi-key citations; retain their shared context.

Do not exclude citations because they appear in abstracts, experiments or
conclusions. Reconcile totals, duplicate keys, missing references and ambiguous
author-year mappings. Missing files or mappings are incomplete coverage.

## 2. Verify each entry's identity

Use an index record plus independent primary-source corroboration for every
entry, not a sample. Prefer DOI/arXiv-ID lookup; otherwise search cleaned title
plus first author/year. Remove formatting commands but preserve semantic words
and mathematical identifiers. For translated titles, verify the original-language
record rather than treating a guessed translation as an exact title.

The bundled helper is optional, from the skill root:

```text
python3 scripts/check-ref/search_paper.py --doi 10.1109/CVPR.2016.90 --json
python3 scripts/check-ref/search_paper.py "paper title" --limit 5 --json
```

Use its absolute path when working elsewhere. It queries OpenAlex/Semantic
Scholar and returns candidate metadata and abstracts; it does not decide identity
or support. Use full JSON abstracts, not the shortened human-readable preview.
Inspect output/errors; an empty list is not proof the paper does not exist.

Use available search/API tools; no Tavily installation is required. The helper
reads optional credentials from scripts/check-ref/api_keys.local.json. Preserve
existing credentials without displaying, logging or placing them in reports.
Do not solicit keys or write configuration just to begin an audit. Authentication
and quotas must be checked against current provider documentation when relevant;
do not assume anonymous access works. If a provider is unavailable, use accessible
authoritative sources and explicitly record the unavailable verification channel.
Never claim a two-source check when only one source was accessible.

Run this helper serially to respect shared quotas; reuse results across occurrences.
Its existing retries are bounded; do not add an outer retry loop. Independent web
lookups may be batched within the actual tool limits. Use DOI landing pages,
publisher/proceedings records or the original arXiv version as corroboration.
Two endpoints or search snippets from the same index are not independent evidence.
Open the underlying record; similar titles do not establish the same work.

Compare fields and record supplied versus verified values:

| Field | Decision |
| --- | --- |
| Title | Allow case/formatting differences, not changed scientific meaning. |
| Authors | Compare the full list where available, including order. Initials/transliteration may be equivalent; a truncated index list is incomplete evidence. The last author is not necessarily the corresponding author. |
| Year/version | Resolve preprint versus proceedings/journal publication before declaring a mismatch; retain the cited version when it supports the claim. |
| Venue/publisher | Equivalent abbreviations are harmless. A different venue or publisher is a substantive mismatch, not automatically a formatting note. |
| DOI/arXiv ID | Resolve the identifier to the actual work/version. A DOI pointing to another work is an identity conflict; never prefer a script's value blindly. |
| Volume/issue/pages | Record exact verified values and corrections. Missing metadata stays missing. |

Identity statuses are **verified**, **verified with metadata corrections**,
**mismatched work/identity**, or **unresolved**. Harmless abbreviations are verified
with a note; incorrect bibliographic fields are corrections. Conflicting records,
one-source-only evidence, unavailable services and no results are unresolved until
resolved. Do not call an unlocated paper fabricated solely because searches failed.
When sources disagree, compare identifiers and primary records; neither a search
result nor the helper automatically wins. Record each evidence URL and check date.

## 3. Verify every occurrence's support

Reuse the correctly matched work's abstract for initial screening. Ask whether it
supports the actual proposition, not merely the topic or shared vocabulary.
Verify task, population/dataset, method, metric, comparator and conditions.
Separate introducing a method/dataset from later use or incidental mention.
Do not attribute this manuscript's measured effects to an external mechanism paper.

An abstract can support a broad statement when it says it clearly. Specific
numbers, theorem assumptions, causal claims, limitations or disputed attribution
require the relevant primary full-text passage/table/theorem. Fetch that source
when accessible and record its location. Abstract silence alone is not evidence
of contradiction. If needed full text is unavailable, mark **unresolved** and state
what evidence is missing. A verified title does not establish support.

Assign **supported**, **partially supported/overstated**, **contradicted or
misattributed**, or **unresolved**. Classify issues such as topical false match,
wrong numerical attribution, missing conditions, wrong method/dataset origin,
unclear source identity or unavailable text. Do not mark support verified for a
source whose identity remains ambiguous. A source cited repeatedly gets separate
occurrence-level decisions, even when retrieval is shared.

## 4. Report and reconcile coverage

Default to check-ref-report.md in the manuscript/output directory; if it exists,
use a fresh timestamped filename rather than overwriting prior evidence. Honor
chat-only or a user-specified destination. Full-paper work may incorporate this
report into its delivery audit if all entry/occurrence detail remains available.
Do not create an extra duplicate audit. Keep local credentials out of deliverables.

Include the following, in the user's language:

1. Scope, source files/version, date, exclusions and inaccessible components.
2. Separate identity and support totals by status. Counts must reconcile with
   inventories; do not merge number of works with number of citation occurrences.
3. Identity table for every entry: key, title, status, original versus verified
   metadata, harmless differences, index and independent source URLs, notes.
4. Support table for every occurrence: location, key, claim excerpt, status,
   evidence passage/abstract summary and URL/page/table, issue type and reason.
5. Clearly grouped corrections and unresolved issues with the evidence needed
   to resolve them; include passing rows, not only a failure sample.
6. Write boundary: for a stand-alone audit state that manuscript and bibliography
   were unchanged; for writing/revision list actual corrections and recheck results.

Example summary columns:

| Dimension | Total | Verified/supported | Corrections/partial | Mismatch/contradiction | Unresolved |
| --- | --- | --- | --- | --- | --- |
| Reference identity | N entries | ... | ... | ... | ... |
| Citation support | M occurrences | ... | ... | ... | ... |

Full audit is complete only when every in-scope item has a recorded outcome.
Unresolved evidence must remain visible; completed inventory processing does not
mean all references passed. Never report sampled checking as full verification.
