# Related work: explain the intellectual neighborhood and the exact distinction

Use for drafting, restructuring or revising Related Work. The aim is to let a
reader locate this contribution among the approaches that matter to its claim.
A bibliography inventory, a list of abstracts or a performance leaderboard
does not by itself establish that relationship.

## Start from the paper's question and the closest work

Read the current contribution, mechanism, evaluation scope, existing
bibliography and relevant source passages. For a local rewrite, use the
supplied supported sources; do not turn it into an unsolicited field survey.
When discovery is requested or a crucial gap requires it, search from the
actual task, shared construction, assumptions and citation trails. Use
[citation-workflow.md](citation-workflow.md) for identity and support.

A compact internal comparison can help:

| Dimension | What to establish |
| --- | --- |
| Shared question | Which problem or capability connects this work to the paper? |
| Technical relation | Shared information, objective, architecture, estimator, data construction or analytical assumption. |
| Difference | The specific operation, setting, assumption or result that differs. |
| Consequence | Why the distinction matters to the paper's question; distinguish expected from measured consequences. |
| Evidence | Relevant source passage, theorem or result and actual read scope. |
| Paper interface | What is inherited, what is added, and whether a direct experimental comparison is appropriate or present. |

Not every source needs a table row. Keep the closest methodological predecessor
explicit even when it belongs to a broad family. A very similar construction
with different terminology may be more important than a famous same-task paper.

## Choose a meaningful organization

Choose groups that explain the contribution: information source, learning
objective, representation, assumptions, measurement, application conditions
or a genuine research debate. Combine small groups when they share the same
mechanism and their separation teaches nothing. Keep distinct groups when they
answer different questions, even if one has few references.

Each group should answer a reader question, such as how methods obtain a
training signal or preserve a fixed representation. Headings such as
"Deep learning" or a string of model names are usually too broad or arbitrary
for a specific technical paper. Chronology is appropriate when development
over time is itself informative.

Group membership must follow the actual sources. Do not invent a taxonomy
that makes the proposed method the only entry with all desirable properties.
A family can contain exceptions; avoid attributing one paper's limitation to
every method in the group.

## Write comparative paragraphs, not annotated bibliographies

A useful paragraph establishes the common goal or mechanism, attributes
representative contributions and develops the relevant distinction. It may
then connect that distinction to this paper. These are paragraph functions,
not a compulsory four-sentence sequence.

Name individual works where their construction or evidence matters. Elsewhere,
group citations only when they support the same claim. Explain a comparison
axis before asking the reader to remember many acronyms.

End where the comparison is complete. Repeated "unlike all these works, ours..."
closings can turn the section into promotional rebuttal. Some paragraphs only
need to establish an inherited idea or complementary line of evidence.

### Inherited components and actual novelty

Differentiate:
- A borrowed method, implementation or dataset, with its proper attribution.
- A changed operation or assumption.
- A new empirical comparison or analytical result.
- A different application of an existing construction.

These can all be useful contributions, but they are not interchangeable.
An unchanged objective is not novel because it is paired with a new sampler.
A new setting alone does not establish that older methods cannot be applied.

Avoid negative claims based on absence from the current reading. "The supplied
study evaluates joint updates" is supportable from that study's methods;
"existing methods require joint updates" needs much broader evidence.
Do not infer priority from a few selected sources.

## Divide work with Introduction, Method and Experiments

Introduction carries the short contrast needed to understand the gap and idea.
Related Work develops the conceptual relationships without repeating the whole
motivation. Method cites borrowed constructions where they are defined.
Experiments explains which baselines were actually compared and under what
protocol. Citation in Related Work does not substitute for experimental setup,
and a benchmark win does not replace conceptual attribution.

Placement follows dependencies and venue conventions. A technical contrast can
appear after Method if it needs the new definitions; the essential predecessor
should still be visible early enough to judge the contribution.

A comparison table is useful when several verified dimensions would be hard to
follow in prose. Define cells and exceptions; distinguish "not evaluated,"
"not reported" and "not supported." Do not turn missing documentation into a
cross or turn assumed capabilities into check marks. Do not make a table merely
because a fixed number of methods was reached.

## Synthetic example

Teaching premises only: P1 updates both retrieval encoders. P2 freezes the
document index and trains a query adapter with uniformly sampled negatives.
P3 uses score-based negatives in joint-encoder training. The current method
keeps P2's adapter and objective but samples negatives according to their scores
in a fixed-index query-adaptation setting. Only supplied experiments establish
whether that change helps.

Weak:
> P1 proposed retrieval adaptation. P2 proposed an adapter. P3 proposed hard
> negatives. Unlike these methods, ours is the first efficient query adapter.

More informative:
> Query-only adaptation preserves a document index by changing the query
> representation. P2 implements this approach with a query adapter and uniformly
> sampled negatives. The present construction retains that adaptation structure
> and changes the negative-selection rule. Score-based selection also appears
> in P3's joint-encoder setting; its relation to the fixed-index setting is a
> question for a matched comparison.

The source labels are not real citations. Do not add "first," an efficiency
claim or a claim of incompatibility without the relevant evidence.

## Drafting and revision procedure

1. Identify the relationships a reader needs to assess the central contribution.
2. Read and map the closest sources before choosing group headings.
3. Draft the section as those relationships, keeping exact source attachments.
4. Check family-level statements against individual sources and exceptions.
5. Compare with Introduction, Method and baseline descriptions for attribution,
   duplication and consistency.
6. Remove citation padding, unsupported disparagement and repeated self-defense.

When asked for prose, deliver the prose and only necessary source queries.
Unverified citation identities stay in author notes or clear working markers;
do not generate plausible bibliography entries to fill the section.

## Completion checks

- Groups explain relevant technical relationships rather than author order.
- The closest predecessor is explicit and represented fairly.
- Inherited pieces and actual additions are distinguishable.
- Comparisons preserve assumptions, settings and source support.
- A different setting or incomplete search has not become a universal
  limitation, priority claim or evidence of superiority.
- The section complements the introduction and experimental comparisons.
