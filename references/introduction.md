# Introduction: lead the reader from a concrete problem to a supported advance

The introduction establishes why this question matters, what is already
possible, which precise step remains and how this paper advances it. It does
not need a grand field history, a manufactured failure of prior work or a fixed
number of paragraphs.

## Establish the argument before polishing sentences

Read the research question, actual mechanism/findings, closest work and author's
current draft. Use verified literature passages when making claims about prior
work. For a local revision do not demand the entire research database.

Make a compact connection:
- What does the intended reader need to understand, compute, predict or decide?
- What can the closest approaches already do, under which conditions?
- Which specific unresolved step matters to that task?
- What does this work change, and which evidence supports that change?

If the gap is broader than the evaluated advance, narrow the gap. If the
contribution is a controlled distinction, a counterexample or a resource, let
that be the contribution. Do not relabel it as a new algorithm or pretend prior
work universally fails.

## Organize by reader needs

### Establish the problem and its consequence

Start at a concrete scientific or technical task. Explain why its constraint
affects an outcome the reader cares about. General importance is useful only
when it leads to this question.

An opening about "rapid progress in large language models" gives little
direction. Depending on the actual evidence, an opening about learning token
credit from sequence-level feedback can establish a real problem. Do not invent
that problem for a manuscript whose contribution addresses something else.

A question, observation, practical constraint or clearly contextualized
contribution can all open an introduction. No compulsory hook or question mark
is required. Define a task before burying it in notation and internal names.

### Explain existing capabilities fairly

Group work by mechanism, information source, assumption or capability. Say what
each route achieves and why it is relevant. Give the closest direct predecessor
its actual role; distinguish inherited components from this paper's additions.
A general survey can move to Related Work, while the decisive comparison stays.

A different setting does not mean a prior method is inferior. Do not describe
all preceding work as computationally expensive, biased or ineffective unless
the relevant evidence supports those claims under comparable conditions.

### Derive a gap this paper actually addresses

The gap should follow from the capabilities just described. It might be a
missing comparison, an undefined object, an untested condition, an unresolved
mechanism or a construction that enables a needed operation. Explain why the
step matters before announcing the solution.

Check the closest work: is the claimed gap already addressed? Is it untested
only in this setting? Is it merely absent from the supplied reading? Incomplete
search is not evidence for "no previous work." If support is missing, use a
narrow documented distinction and keep the unresolved literature query outside
the finished prose.

### Explain the idea and fulfill the promise

Give the central insight in ordinary language before names and equations.
Connect its distinctive operation to the stated difficulty: why does this
operation address that difficulty? Do not make readers infer the relationship
from a component inventory.

Preview decisive findings at the contribution level. Point to relevant internal
evidence in a manuscript that uses cross-references. Use verified external
citations for claims about other work; they cannot substantiate this paper's
own results.

Contribution bullets are optional. If used, each should name an actual advance:
a construction, theorem with assumptions, empirical distinction, or useful
resource. A method paper may emphasize its methodological advance and summarize
supporting experiments together. Do not split routine implementation choices
into artificial novelties or dismiss a genuine empirical contribution as "only
evaluation." "We conduct extensive experiments" is not itself a finding.

## Make paragraphs connect through content

For each paragraph that needs work, identify:
- The understanding it adds.
- The evidence or reasoning supporting its main statement.
- The object or question carried over from the preceding paragraph.
- What the next paragraph must now explain.

These notes can remain internal. One paragraph may introduce a constraint,
another explain two existing routes and a third develop the key idea. Their
lengths and internal structures can differ. A long paragraph with two distinct
jobs may split; a useful short transition need not be inflated.

At a boundary ask, "Why does this next paragraph appear here?" If the answer is
only "another literature group" or "the template calls for contributions,"
repair the dependency rather than adding "however" or "therefore." Repeat a
stable technical noun when it clarifies continuity; synonym variation can break
the argument.

## Synthetic worked route

Premises for teaching only: sequence-level rewards supervise token generation.
Existing method A broadcasts the outcome score to all tokens. Existing method B
uses an additional trained token critic. ContextDelta instead compares the same
sampled tokens under two scorer contexts using a frozen scorer. Its experiments
test matched-count masks and downstream task outcomes. No optimal-credit theorem
is supplied.

A possible route:
1. Explain the token-credit problem created by a sequence-level outcome.
2. Attribute the broadcast and trained-critic capabilities to A and B. Explain
   the specific construction question ContextDelta studies, without calling
   either family generally ineffective.
3. Introduce the two-context comparison and why comparing the same tokens makes
   the signal interpretable. Define the scorer's role and information boundary.
4. Preview the actual matched comparisons and findings supplied by the study.
   A zero-mean correction, if present, is an identity rather than proof of
   unbiased policy gradients.

This is a route, not ready-made prose. Without actual findings and verified
citations, do not invent the final result preview or bibliography.

## Learn from reference papers when requested

Read the relevant supplied introduction and identify paragraph functions,
transitions, closest-work treatment and the role of citations. Map each useful
move to evidence in the current study. Learn the relationship between problem
and answer, not an impressive vocabulary, fixed paragraph count, hypothesis
history or borrowed experimental strength. Record whether the full section or
only an excerpt was available.

## Reverse-check the introduction

Read from promises back to results:
- Does the opening problem lead to the actual contribution?
- Are the closest work's capabilities and limitations fairly represented?
- Is every gap supported and no broader than the paper's answer?
- Is the main idea understandable without the acronym or module names?
- Does each claimed advance resolve to a method, proof, result or resource?
- Are result previews representative, including mixed findings where relevant?
- Do paragraph transitions continue a real object or unresolved question?

For a mature introduction, make only changes that repair these issues. Return
finished prose when asked; do not substitute a paragraph plan for a requested
introduction.
