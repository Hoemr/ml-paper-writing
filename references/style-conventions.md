# Style conventions, organised by artifact

These are artifact-specific defaults from revision work. Preserve the paper's
scientific meaning and established notation; follow explicit user and official
venue requirements when they differ. Check evidence and layout rather than
claiming that a stylistic pattern identifies machine-generated writing.

The organising principle behind all of them: **the paper reports what was done
and why it is true.** It is not an audit log, and it does not argue with itself.

---

## Notation

- **One scheme, declared once.** Sets and spaces in script capitals (`\mathcal F`),
  vectors in bold roman (`\vx`, `\vy`), scalars in lowercase italic, operators
  upright (`\mathrm{crit}`, `\mathrm{Var}`). Put the declarations in one file and
  treat it as the authority.
- Avoid ambiguous notation collisions. Case distinctions are acceptable when
  conventional and clearly defined; do not rename established symbols casually.
- **Avoid unnecessary single-use intermediate variables.** Inline a quantity
  used once when doing so improves readability. Keep a named intermediate if it
  clarifies a complex expression or a meaningful mathematical role. Check this
  mechanically: list every symbol in the notation table and count its uses
  outside the table; anything at zero should not be in the table at all.
- **Reuse one family for related objects.** A quantity and its sampled
  realisation should be `M_u` and `M_{u_t}`, not `M_u` and `M_{\tilde c_t}`.
- **Define at first use, then index.** Every symbol is defined where it first
  appears *in the body*; the appendix carries the complete table and the problem
  setup points at it.

## Cross-references

- When compatible with the venue and existing source, use `\cref`/`\Cref` with abbreviated names — `Fig.`/`Figs.`, `Tab.`/`Tabs.`,
  `Sec.`/`Secs.`, `Eq.`/`Eqs.` — so the manual `Table~`/`Section~` prefix
  disappears and the plural adds an "s".
- **cleveref's appendix detection keys off chapter counters.** In an
  article-class document, `\cref` to an appendix `\section` prints "section B.3".
  Supply the appendix wording explicitly — e.g.
  `\newcommand{\appref}[1]{appendix~\labelcref{#1}}` — for every appendix-section
  reference. Verify by compiling a two-page probe, not by assuming.
- **Merge multi-key references** into one call (`\cref{a,b,c}` → "tabs. 1, 2 and
  3") and keep the keys in ascending printed order, or the reader sees
  "tables 2, 4 and 3".
- Keep cross-reference formatting consistent; explicit references may be needed
  for special objects or venue restrictions.

## Tables

- **Capitalise prose header cells.** "Stage", "Consumed", "Avg. 7-bench" — not
  "stage", "consumed". Apply to appendix tables too, while retaining mathematical
  symbols and case-sensitive dataset or split identifiers.
- **Use one spelling for configuration names inside tables and figures.** If the baseline
  is "Ordinary DPO" in a table, it is "Ordinary DPO" everywhere in tables and
  figures; lowercase is fine only in running prose.
- Report uncertainty with its sampling unit and method. Evaluation standard
  errors and training-seed variability answer different questions. Prefer paired
  differences when paired observations exist; do not invent tests from summaries.
- **Exact numbers live in tables; a figure may replace a table, not duplicate
  it.** When a figure already carries every number a table carries, move the
  table to the appendix.
- **Never leave an overfull table.** Wrap long text columns in
  `>{\raggedright\arraybackslash}p{...}`, shorten headers, or reduce
  `\tabcolsep`. An unbreakable multi-centimetre cell (a macro, a long
  `\mbox`) silently pushes tables past the margin.
- Select columns relevant to the stated claim, retaining adverse evidence and
  controls necessary to judge it. Move supporting detail without hiding it.

## Mathematical statements

- Name a theorem, lemma, or proposition with a short mathematical noun phrase,
  such as “Baseline invariance,” “Bounded credit,” or “Score identity.” State
  conditions, scope, and conclusions in the statement, not a sentence-length
  title. Earlier-variant provenance belongs in surrounding prose.
- Distinguish an established identity from the paper's new construction. A
  bounded coefficient does not by itself prove optimizer stability or causal
  credit assignment.

## Figures

- Method schematics and their captions: [figure-workflow.md](figure-workflow.md)
  routes to `$ml-method-figure`, the single owner of construction and QA rules.
- Measured plots: use the relevant plotting skill (such as `$nature-figure`)
  when available. Preserve data and uncertainty, label units and comparisons,
  and follow the venue's caption style. A mechanism diagram need not invent
  numerical results to earn its place.

## Algorithms

- Aim for about 20 numbered lines in a main-text overview. `algorithmic` spends a line number on `\FOR`,
  `\ENDIF` and `\ENDFOR` as well as on `\STATE`, unless it is loaded with the
  `noend` option. Past 20, review whether material belongs in prose or an appendix
  listing rather than treating the target as a hard limit.
- **Every line is one operation, in the imperative.** No subordinate clauses, no
  `\emph`, no definition smuggled into a step. "Set $\bar\kappa_t\gets0$ and skip
  the row" is a conditional written as a clause; give it `\IF`/`\ELSE`.
- **A step is an operation; a definition is not a step.** Moving a symbol's
  definition into a numbered line makes the reader spend two steps learning
  vocabulary before reaching an operation. Definitions go in the block's header
  run, in `\REQUIRE`, or in the notation table, and once only.
- **The listing states the order; the method defines the computations.** Link
  scientific scores, credit rules, and objectives to their numbered equations or
  explicit helper definitions rather than re-deriving them. Ordinary operations
  such as sampling, verifying, and freezing a snapshot need no separate equation.
  Every consequential operation must agree with the method description; an
  unnumbered operation is not itself evidence of fabrication.
- **Name the sub-computations; do not expand them.** A helper needing more than
  two lines, or used twice, gets a name. SimSiam's loss is a named `D(p,z)` under
  the loop rather than ten inlined lines. Fuse a guard into the condition it
  guards, and collapse a loop whose body is one formula into a step over the
  loop index: nesting can read as an implementation transcript. A block over the
  suggested budget because of several `\ENDIF`s deserves a compaction review,
  while necessary branches take precedence over the suggested line count.
- **Setup outside the loop, work inside it, the update as one line.**
- Concision is about conceptual operations, not squeezing implementation detail
  onto fewer lines. Move chunk precision, storage layout, replay assertions, and
  explanatory prose to a referenced implementation paragraph. Retain scientific
  invariants such as frozen scoring, gradient boundaries, masking, and baseline
  update order in the listing or its immediately adjacent setup.
- **Caption titles the listing, it does not summarise it.** "Pseudocode of MoCo
  in a PyTorch-like style" names the artifact and stops. A caption that restates
  the steps is a second abstract.
- If a readable listing needs more space, use a named helper, an appendix
  listing, or prose as appropriate. Do not omit necessary branches to meet a
  line budget. Examples in algorithms.md are examples, not venue mandates.
- **Audit mechanically, then trace by hand.** Check consequential operations
  against the method section in order. An unsupported scientific computation
  requires correction; explanatory method prose need not become a numbered step.
  See [algorithms.md](algorithms.md) for the two reference blocks, the LaTeX
  recipes for `algorithmic`/`algpseudocode`/`algorithm2e`, and
  `scripts/audit_pseudocode.py`.

## Prose and structure

- **Prefer ordinary sentence boundaries.** Semicolons are occasional tools for
  closely related independent clauses or an ambiguous complex list. Do not use
  them as the default link between sentences, explanations, experimental settings,
  or multiple facts in a caption. Avoid several semicolons within a paragraph.
  Split clauses into complete sentences or use a precise conjunction when that
  reads more naturally. Do not replace semicolons mechanically with commas and
  create comma splices or sentence fragments.
- **Use explanatory dashes sparingly.** Do not repeatedly insert explanations
  with em dashes, TeX triple hyphens, or spaced en dashes. Prefer a complete
  sentence, a colon introducing a needed explanation, or short parentheses.
  Preserve genuine ranges, compound-name punctuation, mathematical minus signs,
  and table placeholders. Equations and code syntax are not prose punctuation.
- Apply these defaults to abstract, introduction, related work, methods,
  results, captions, and appendix prose. Inspect each retained semicolon or
  explanatory dash in context and keep it only when it improves clarity.
  Preserve conditions, adverse evidence, and citation attachment.

- For chapter patterns and rewriting, use [writing-guide.md](writing-guide.md).
  Defensive-writing decisions and examples live only in
  [reviewer-guidelines.md](reviewer-guidelines.md#defensive-writing-examples).
- Keep author workflow commentary out of paper prose. Retain provenance,
  preregistration, caveats and version distinctions when scientifically material;
  explain them where the affected claim is assessed.
- **Background must earn the questions.** Never open a paragraph with "This
  paper asks three questions" after unrelated motivating prose. Show that the
  surveyed lines each stop at the same boundary, then let the questions fall out
  of that boundary.
- Contributions are a short overview, not an inventory. Tie each to a supported
  empirical finding, theoretical result, construction or resource; distinguish
  proposed from evaluated work. No over-claiming, and no bold run-in unless the
  venue's style uses one.
- Attach citations to supported clauses. Group citations when all support the
  same statement; split them when their claims differ. Support requires reading
  the relevant source, not merely matching its title.
- Keep exact experimental counts when they define scope and update them when
  the scope changes. Avoid unsupported broadening to vague generality.
- **Name and cite every artifact.** Every model, dataset, and benchmark named in
  the experiments carries a citation at first use.

## The verification loop

1. After any bulk edit, rebuild and compare the **Overfull count** against the
   previous build. A regression there is a defect, not a warning.
2. After adding references, rebuild with `bibtex` and confirm every new key
   resolves in the `.bbl` and that the log reports no undefined citations.
3. For citation identity, metadata, support and failure handling, follow only
   [citation-workflow.md](citation-workflow.md). Check consistency of the changed
   claims across abstract, body, figures and conclusion.
4. Render representative main-text pages and every appendix page affected by
   display or float edits. Inspect at readable size for column overlap, line
   numbers crossing text, clipped equations, and replacement glyphs. Inspect
   source encoding separately: layout collisions can look like corrupted text.
   Full-width displays inserted into line-numbered two-column proofs deserve
   particular care; prefer column-width aligned derivations when they fit.
