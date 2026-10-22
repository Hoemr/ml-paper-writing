# Method: make the idea understandable and the procedure reconstructable

Use for Method, Approach, Model, System Design, problem formulation and the
exposition surrounding mathematical results. This guide owns scientific
organization; notation and algorithm formatting remain in
[style-conventions.md](style-conventions.md), recipes in
[algorithms.md](algorithms.md), and diagrams in [figure-workflow.md](figure-workflow.md).

## Recover the actual method before describing it

Read the research question, current method, necessary equations, diagram or
pseudocode, result identity and relevant implementation/configuration. Follow
[evidence-workflow.md](evidence-workflow.md) for execution-source conflicts.
Do not require all raw data for an ordinary language revision.

Identify the smallest sufficient method description:
- Task, inputs, outputs and information available at each stage.
- The central construction and what difficulty it addresses.
- Operations in dependency order and any maintained state.
- Trainable/frozen components and update or inference behavior.
- Conditions, parameters and consequential exceptional cases.
- What is inherited, what changes and what later evidence evaluates.

These are questions to answer, not mandatory subsections or an author form.
Some methods are one equation; some need an iterative algorithm and a system
diagram. Let the scientific dependencies choose the presentation.

## Give a conceptual overview before local machinery

Explain what flows through the method and the distinctive transformation.
A running example can help readers follow objects and dimensions if it
materially reduces abstraction. Mark it as illustrative; it proves no benefit.

An overview should make the key idea recoverable without knowing internal
module names. A component list gives inventory but usually misses the reason
for the construction. Connect the operation to the specific requirement,
then formalize it.

Separate problem setup from the proposed solution. Define the task and
available information independently of the architecture so that the problem
does not silently assume the proposed answer. Background should include only
definitions or results needed later.

## Develop the method in dependency order

Introduce an operation after the objects it consumes are known. For each
substantial stage, make clear what it computes, why it belongs here, and what
the next stage receives. Explain the design rationale where it helps a reader
understand a choice, without forcing every stage through identical prose.

Use functional subsection titles when they reveal the idea, such as
"Selecting negatives from a fixed index." Generic "Module A" or "Our framework"
headings can obscure the scientific work. Retain established names when they
already carry a clear definition.

Present the final design. Explain documented alternatives when they illuminate
a real trade-off. Do not invent failed attempts, historical motivations,
discarded baselines or an ablation to justify each component.

### Equations need a role, definitions and interpretation

Before an equation, explain the quantity or relationship it introduces.
Define symbols, domains, reductions and conditions where first used. After it,
explain what the expression does in this method or which property follows.
Do not merely translate every symbol back into words or announce "Eq. 3."

Keep sign conventions, normalization sets and units explicit. Loss averaged
over all sampled tokens differs from loss averaged over retained tokens.
A softmax over candidates differs from filtering a normalized distribution
afterward. A coefficient's bound does not establish stable training.

When rewriting mathematics:
- Preserve equality versus approximation, expectation versus sample estimate,
  optimization variables, conditioning and stop-gradient boundaries.
- Distinguish a mathematical identity from a new result.
- Keep denominators and reduction order aligned with the evaluated variant.
- Treat a changed formula or assumption as a scientific change, not polish.

### State and information boundaries

For learning or iterative methods, clarify initialization, data generation,
scoring, selection, objective and updates in their actual order. Explain which
model produces a signal, when parameters change and which computations permit
gradients. Do not leave these properties implied by a generic training loop.

Separate training, validation selection and inference. Privileged training
information is not automatically available at deployment. A frozen scorer is
not a trainable policy. An offline index, cached representation or stale
checkpoint needs its actual validity conditions.

Consequential edge cases belong in the method: empty selections, no valid
pairs, tied candidates, masked tokens or degenerate normalization when they
change the produced quantity. Routine storage details can remain in the
implementation description.

### Prose, equations, diagram and pseudocode divide the work

Prose explains rationale and scientific meaning. Equations define quantities
and relationships. A diagram shows objects and interfaces. Pseudocode exposes
state, branching and update order when these matter.

Keep all representations consistent without narrating the entire algorithm
twice. A short equation-based method may need no algorithm. A nontrivial update
order should not be hidden in an unnamed helper. Formatting and line-budget
defaults in the algorithm guide never justify dropping a necessary branch.

## Reproducibility and main/appendix placement

Keep defining operations, central assumptions and result-changing choices in
the main explanation. Put exhaustive configuration tables, detailed
architectures, long derivations and routine implementation recipes in a
referenced appendix when appropriate. "Implementation details in Appendix"
cannot replace the definition of the central estimator.

For the current paper, supply the parameters and protocol information needed
to understand and reproduce its results. Do not fill missing optimizer,
threshold, seed or sampling rules from common practice. Resolve a gap from
the corresponding executed version or list the specific missing fact.

Differentiate a fixed design parameter from one selected on validation data,
including the selection criterion and actual search when relevant. Methods
explains the procedure; Experiments defines the actual evaluation protocol
and measured outcomes. Avoid conflicting parameter copies in both sections.

## Theory and complexity within the method

State what formal question a proposition answers, its assumptions and
conclusion. Explain the main proof idea and the significance of difficult
steps; complete details can live in a pointed-to appendix. Do not compress
a proof by removing a condition needed for the result or fabricate a lemma
to bridge a gap.

Distinguish:
- A standard identity used to define the method.
- A guarantee derived under stated assumptions.
- A conjecture or intuition motivating an empirical prediction.
- Observed behavior of the implemented optimizer.

A theorem in a simplified setting may explain a possible relationship without
proving the real training mechanism. Empirical agreement does not prove the
theorem, and the theorem does not replace evaluation of its operational use.

Define the variables and accounting boundary of a complexity claim. Separate
setup from per-query cost, training from inference, and theoretical operation
counts from measured latency or memory. Do not silently omit a material
precomputation or recurring update.

## Synthetic worked method passage

Premises only: a fixed document index contains embeddings \(d_i\); a trainable
query adapter produces \(q_\theta(x)\). Candidate retrieval returns 20 IDs,
then the known relevant IDs are removed to form \(N_x\). For \(N_x\ne\varnothing\),
one negative is sampled with

\[
p(i\mid x)=
\frac{\exp(q_\theta(x)^\top d_i/\tau)}
{\sum_{j\in N_x}\exp(q_\theta(x)^\top d_j/\tau)},\qquad i\in N_x .
\]

The sampler uses detached scores, \(\tau=0.5\), and empty candidate sets skip
the query. Only the adapter updates under a supplied contrastive loss.

Possible explanation:
> The document representations remain fixed during adaptation. For each query,
> the current adapter retrieves 20 candidates; removing known relevant IDs
> defines the set from which a negative is drawn. The normalized similarity
> scores assign greater probability to candidates closer to the query
> representation. Selection uses detached scores, and queries with an empty
> candidate set are skipped. The sampled negative and the labeled relevant
> document then enter the contrastive objective, which updates the query adapter.

This illustrates data flow and boundaries. The actual objective must still be
specified from the study. Do not invent it from "contrastive," differentiate
through the sampler, normalize over the unfiltered 20 IDs or claim optimal
negatives on the basis of this example.

## Completion checks

- A reader can explain the central idea before tracing the local equations.
- Inputs, outputs, available information and stage interfaces are explicit.
- Definitions, formulas, diagram and algorithm describe the evaluated method.
- Frozen/trainable state, gradients, selection and consequential cases agree.
- Rationale explains real design choices without fabricated research history.
- Reproduction detail has a findable home; unknown values remain queries.
- Formal claims and computational claims retain assumptions and boundaries.
