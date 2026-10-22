# Title and abstract: select a contribution and its evidence

Use for drafting, rewriting or compressing an abstract and for title revision.
Read the current body claims, decisive result sources and author choices before
writing. The abstract is a self-contained argument, not a compressed contents page.

## Decide what the abstract must establish

Identify the actual research type, task, central advance and strongest evidence.
Collect only what is needed: final results, comparison conditions, necessary
limitations, requested language and length. If a venue limit matters, verify the
current venue/year/track rule. Without one, use an explicitly provisional length;
do not delay ordinary drafting to choose a venue.

Privately sort candidate content by function:

| Content | Selection decision |
| --- | --- |
| Problem | The concrete task, decision or unresolved relationship that makes the contribution intelligible. |
| Main advance | What was constructed, established, measured or made possible; rank supporting modules below it. |
| Mechanism | The distinctive operation connecting the idea to the problem, at a level a reader can understand without equations. |
| Decisive evidence | The result or combination of results that actually supports the selected contribution. |
| Necessary boundary | A condition whose removal changes what that result means. Keep it attached to the affected claim. |
| Consequence | The capability, understanding or use demonstrated by this work. Separate prospective uses. |

A short task need not expose this table. Do not require a separate planning
approval when the author already asked for an abstract.

## Build a coherent argument

The reader should understand why the work was needed, what the authors did,
what evidence matters and what follows. These are responsibilities, not a fixed
sentence order. A method paper may open with a concrete constraint; a theory
paper with its result and assumptions; a resource with the missing research
capability; an analysis with the distinction it establishes.

**Opening.** Enter at the level of the actual task. Explain the difficulty that
the method or finding addresses. Avoid several sentences of field history,
unexplained acronyms, and invented bottlenecks. A contribution-first opening is
fine when it supplies the needed context. Do not make every opening a complaint
about prior work.

**Advance and mechanism.** State the main idea through what operates on what.
Explain the informative difference from the closest approach. Module names,
a list of losses and "a novel unified framework" do not explain an idea. Preserve
a meaningful method name after readers have enough context to interpret it.
Implementation detail belongs here only if it is the contribution.

**Evidence.** Choose evidence by inferential role, not the largest number.
Identify the task or evaluation scope, metric, comparator and material budget
condition sufficiently to interpret a numerical claim. One number may suffice;
several may be needed for a trade-off. Usually leave per-task means, standard
deviations and procedural settings to the result table; summarize the observed
pattern and include only numbers needed to assess the abstract's claim.
Do not force a number into a theoretical
or qualitative contribution, or list every benchmark to sound comprehensive.

**Ending.** Explain what understanding or capability the result adds to the
original problem. Do not repeat the method name with "effective and robust."
A measured reduction in peak memory supports a memory claim. Equal-accuracy
cost, wall-clock speed, sample efficiency and deployment utility need their own
evidence.

Put concepts into the sentence where their operation becomes clear. Avoid
requiring the reader to memorize internal labels before learning what they do.
Keep terminology stable rather than replacing it with attractive near-synonyms.

## Select boundaries without turning the abstract into a rebuttal

Use [reviewer-guidelines.md](reviewer-guidelines.md#defensive-writing-examples)
for editorial decisions. Distinguish a necessary result condition from a project
status report. A matched-schedule memory claim needs that schedule condition.
It need not inventory every unfinished deployment study. If the abstract claims
overall superiority, however, adverse accuracy results directly constrain it.

Do not cherry-pick a favorable subset as overall performance. When accuracy
changes sign across tasks, report the heterogeneity for an accuracy claim.
When a cost benefit and accuracy trade-off jointly define the contribution,
present both. A smaller cost number cannot silently stand for equal quality.
Neither overlap of intervals nor a non-significant test establishes equivalence.

Point estimates changing direction across tasks support a description of those
observed estimates. They do not alone establish a task-by-method interaction,
reliable task-dependent usefulness or an explanation for the difference.

State established operations and observations directly; qualify the specific
unproven inference. Avoid blanket "may possibly" language that weakens even
known facts. Do not use caution words as substitutes for explaining evidence.

Do not end every abstract with a list of unmeasured benefits. If an unsupported
speed claim has been removed, an abstract clearly limited to measured peak
memory need not append a separate speed disclaimer. Keep that boundary when
the selected wording still implies a speed or general efficiency claim. Prefer
a supported contribution or finding as the ending when the argument permits.

## Draft, compress, then read backwards

1. Draft from selected facts, not by shrinking every body section.
2. Read without the paper: can a reader identify the task, idea, evidence and
   supported takeaway? Does each technical term earn its space?
3. Trace every empirical or theoretical claim to its source. Compare title,
   abstract, introduction promises and conclusion.
4. Compress redundant background, procedural lists, repeated findings and empty
   evaluation adjectives. Preserve the comparator, condition, unit and inference.
5. Recheck complete sentences, quantifiers, negation, numerical scales and any
   citation attachment after compression. Give the final word count when a word
   target was requested, naming an approximate count if venue counting differs.

Do not add unsupported material to fill a pattern. If the supplied abstract
already works, repair only the diagnosed issue.

## ML teaching example

Synthetic premises, not facts to reuse in a manuscript: PatchStore caches
intermediate patch features during training of one frozen vision encoder.
At the same 20,000-update schedule, its measured peak allocated GPU memory is
18 GB versus 24 GB for the uncached implementation on the recorded hardware.
Accuracy is 81.2 versus 81.4 on task A and 76.9 versus 76.5 on task B, with one
training run per setting. No runtime or equal-accuracy cost was measured.

Weak:
> Vision models have achieved remarkable progress. We introduce PatchStore, a
> novel and efficient framework with a cache module and a reuse module.
> Extensive experiments demonstrate superior performance.

Possible abstract from these premises:
> Training with a frozen vision encoder can repeatedly retain intermediate patch
> features in GPU memory. PatchStore caches these features for reuse during
> training. At a matched 20,000-update schedule on the evaluated encoder and
> hardware, peak allocated GPU memory decreases from 24 GB to 18 GB. Accuracy
> changes in opposite directions on the two evaluated tasks, with one training
> run per setting.

This example emphasizes a measured trade-off because those are its premises.
It is not a template requiring a limitation sentence in every method abstract.
A fully supported new mechanism deserves a clear mechanism explanation; missing
mechanism facts must be queried rather than inferred from "cache."

## Titles

Choose the object and actual advance first. A method title can state the task
and distinctive operation; a theory title its result and setting; an analysis
title the finding; a benchmark title what capability it measures. The method
brand can support identification without replacing that information.

Ask: what work would a reader assume was completed from this title alone?
Remove implied causal proof, comprehensive coverage, universal superiority or
deployment benefit that the body does not establish. Keep identity words such
as simulated, empirical or conditional when they prevent a different reading.
Offer a few genuinely different emphases when alternatives were requested, not
cosmetic adjective swaps. Recommend on accuracy and informativeness.

## Completion checks

- The abstract has one intelligible argument rather than a module or result list.
- The difficulty motivates the actual idea and is supported by source material.
- Main evidence is representative of the stated claim and its scope.
- The title and ending promise no additional theorem, metric or application.
- Necessary conditions remain, with no repeated defensive or audit narrative.
- Language, length and venue constraints are checked to the stated extent.
