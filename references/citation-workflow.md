# Citation identity and claim support

## Add a reference

1. Search a suitable index (Semantic Scholar, OpenAlex, Crossref, arXiv) or an
   official proceedings/publisher page. Match the exact work, not the first
   title-like result. Inspect existing bibliography entries for duplicates.
2. Verify title, complete authors, year, venue/version and DOI or arXiv ID against
   the primary record; corroborate through an independent authoritative record
   when available. Two endpoints of the same provider are not independent sources.
3. Fetch BibTeX from the publisher, proceedings, DOI content negotiation or arXiv
   export. If export is unavailable, transcribe only verified metadata and record
   that fact; missing fields stay missing. Never generate identity from memory.
4. Read the relevant abstract, theorem, method or result before attributing a
   claim. A keyword match establishes neither entailment nor the conditions of
   a result. Metadata verification and claim support are separate checks.
5. Add the entry using existing key/backend conventions, compile the bibliography,
   and check key resolution. Preserve unrelated entries and do not switch a
   venue's natbib/BibTeX stack to biblatex for convenience.

Use available web/API tools; no particular connector or Python dependency is
required. Provider quotas and authentication change: consult current official
API documentation if relevant instead of trusting stored rate-limit numbers.

## Incomplete support

If identity is uncertain, omit the invented citation and leave an explicit
`[CITATION NEEDED]` drafting marker or author note. If identity is verified but
support is unclear, narrow the claim or flag the exact passage requiring review.
Report which checks succeeded, which failed and what source would resolve them.
Do not put fabricated placeholder keys into a bibliography to make it compile.

Do not silently replace a preprint with a later paper: check that the cited
result and author/version metadata still match. Preserve needed self-citations
and apply the venue's anonymization rules rather than deleting relevant work.

## Existing-reference audits

For a requested read-only audit, use `$check-ref` if available and follow its
coverage/report requirements. Do not expand ordinary prose editing into a full
bibliography audit. Flag discovered identity or support issues proportionally.

Official API links and source provenance live in [sources.md](sources.md).
