# Theory-paper titles: COLT and STOC reference

Use this reference when naming a learning-theory or theoretical-computer-science
paper. It supplements the ordinary title route; it is not a template, acceptance
criterion, trend forecast or permission to strengthen a claim.

## Evidence snapshot and scope

The snapshot was measured on 2026-11-03 (Asia/Shanghai):

- COLT 2011--2024: 1,416 titles from
  [PaperCopilot paperlists](https://github.com/papercopilot/paperlists/tree/main/colt),
  repository commit `f4fa42d0eb48ca73c479ab08979eab43ec616ed9`.
- Recent historical slice: 770 COLT titles from 2020--2024.
- COLT 2025--2026: 377 research titles after excluding two prefaces, from the
  official [PMLR 291](https://proceedings.mlr.press/v291/) and
  [PMLR 336](https://proceedings.mlr.press/v336/) tables of contents.
- STOC 2025--2026: 363 research-paper titles from the official
  [STOC 2025](https://acm-stoc.org/stoc2025/toc.html) and
  [STOC 2026](https://acm-stoc.org/stoc2026/toc.html) tables of contents.

Counts are descriptive title occurrences, not causal evidence about acceptance,
retrieval or citations. The corpora span many subfields; a frequent word is not
automatically appropriate for a particular paper.

| Corpus | Compact structure | Selected title vocabulary |
| --- | --- | --- |
| COLT 2020--2024 | Median 8 words; interquartile range 7--11; colon in 21.2% | `learning` 203/770, `estimation` 34, `sampling` 27, `statistical` 17, `lower bounds` 17, `sample complexity` 11 |
| COLT 2025--2026 | 377 research titles | `learning` 84, `estimation` 16, `sampling` 16, `sample complexity` 12, `score matching` 5 |
| STOC 2025--2026 | Median 7 words; colon in 11.3% | `learning` 25/363, `lower bounds` 17, `estimation` 7, `sampling` 5 |

In the recent COLT/STOC samples, exact phrases such as `density ratio`,
`likelihood ratio` and `weak overlap` were absent. This does not disqualify them:
specialized object and condition terms can be more informative than a frequent
generic word. It does mean that an unfamiliar task needs an exact bridge to a
broader community term in the title or abstract.

## Choose the title's intellectual center

A theory title should let a broad reader recover at least two of these three:

1. **Object or task:** what is learned, estimated, sampled, optimized or bounded.
2. **Regime or obstruction:** the condition making the result nontrivial.
3. **Formal advance:** the specific bound, separation, characterization,
   complexity result or constructive mechanism.

Prefer one grammatical center. Useful compact forms include:

- `<Object or task> under <regime> via <mechanism>`
- `<Concrete result> for <object> under <assumptions>`
- `<Object>: <short, subordinate theorem consequence>`

A colon is optional. Use it when the left side is clearly the primary title and
the right side is a shorter qualifier. If both halves have similar length and
importance, merge them with `under`, `for`, `via` or `with` instead of making two
titles compete.

Venue-matched concision overrides the generic title optimizer's 12--20-word
heuristic. For COLT/STOC-style work, 7--11 words is a useful observed reference,
not a quota. Keep a longer title when a necessary object, condition or theorem
scope would otherwise disappear.

## Map specialized terminology without changing the object

When a subfield term is narrow, map it to an exact broader term only if the
mathematical objects coincide. Bind the two terms at first use in the abstract.
For example, a density ratio between two specified distributions is also a
likelihood ratio; the broader term can expose hypothesis-testing and theoretical
inference connections without changing the estimator. A merely related
application, baseline or downstream use is not an eligible replacement.

Method names should state the actual operation. If auxiliary variables are
minimized in closed form and substituted back, `analytic elimination` or
`partial minimization` is usually clearer than an unexplained `profiling` brand.
Use `marginalization` only for integration and `variable projection` only when
that established construction is genuinely the intended relation. Avoid an
acronym when its expansion is less clear than the operation or when it collides
with a standard term in an adjacent field.

## Gate theorem words by the proved object

COLT/STOC titles often use words such as `lower bounds`, `sample complexity`,
`optimal`, `minimax`, `rates`, `hardness` and `separation`. These are theorem
claims, not decorative theory signals.

- Use `sample complexity` only when the theorem controls the required sample
  size for a stated accuracy/confidence target; an error bound alone may not.
- Use `lower bound` only for the task or estimator class actually lower-bounded.
- Use `optimal` or `minimax` only with the matching comparison class and rate.
- Qualify `separation` by the separated quantity and regime when the bare word
  is not self-explanatory, such as `risk separation` or
  `polynomial--exponential risk separation`.
- Use `finite-sample guarantees` only when the operational estimator is covered
  under the title's stated setting.

Do not promote an application term such as `distribution shift` into the title
when the paper only demonstrates it downstream. Likewise, `learning`,
`statistical` and `information-theoretic` are useful only when they identify the
actual task or proof, not because they are frequent in the corpus.

## Final checks

- Read the title without the abstract: is the primary object unambiguous?
- Can every theorem-strength noun be pointed to a statement with matching scope?
- Does a broader synonym remain mathematically equivalent to the paper's object?
- Is one side of a colon clearly subordinate, if a colon is used?
- Would deleting a method acronym improve retrieval for readers who do not yet
  know the method?
- Report corpus year and source whenever its statistics influence a recommendation.
