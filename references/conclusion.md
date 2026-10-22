# Conclusion: answer the original question and explain the supported consequence

Use for drafting, rewriting or compressing a conclusion. Read the current
introduction promises, central method/result statements and any updated
discussion or limitations first. The conclusion is the paper's last scientific
claim, so it must use the current evidence rather than an older stronger story.

## Decide what the reader should retain

Identify the answer to the original question, the idea or evidence that makes
it credible and the consequence for the intended reader. Select those few
relationships instead of replaying every section, component and benchmark.

A method paper can explain what its construction now enables under the
evaluated conditions. A theory paper can state the main result with the
assumptions needed to understand it. An analysis can state the revised
understanding, including a negative or heterogeneous finding. A resource paper
can state which research task the delivered resource makes possible.

These are alternative emphases, not a requirement to claim all four kinds
of contribution. A useful negative finding does not need a positive algorithm
result to justify its conclusion.

## Build a short, complete ending

Reconnect to the question at the level of the answer, not by copying the
introduction's motivation. Explain the main advance in a sentence a reader
can remember. Name the decisive evidence at a higher level where useful,
then state the supported consequence.

The sequence can vary. Some conclusions need one paragraph; others need
separate scientific and practical implications. Do not force a three-sentence
formula, a fixed word count or a standalone Conclusion section where the
article already ends appropriately in Discussion.

Keep scope integral to the claimed result. Do not weaken all facts with
"may" or append a list of all unmeasured properties. A central unresolved
claim must remain unresolved, however: mixed observed results cannot become
consistent improvement just because the conclusion is short.

## Choose an appropriate implication

A consequence should follow from what was built, proved, observed or actually
made available. For example, a controlled comparison may change how a claim
should be evaluated; a decomposition may reveal reusable computation; a
benchmark may expose a specific failure regime.

Do not add a new theorem, causal explanation, priority claim, generalization,
deployment benefit, public-release state or performance metric. "Efficient,"
"robust" and "general" still need defined support in the ending.

Future work is optional. If useful, identify one concrete question arising
from the established finding or important remaining boundary. State it as
prospective, not completed. "Many exciting applications" and "more work is
needed" rarely give the reader a useful final thought.

## Synthetic examples

Premises only: a token-ranking comparison has observed accuracy mean changes
of +0.8, -0.6 and +0.1 percentage points against matched random retention on
three tasks, with uncertainty insufficient to establish overall superiority.
No optimal-credit result is proved.

Weak:
> We proposed a novel token-credit framework. Extensive experiments demonstrate
> robust improvements and open a new paradigm for efficient learning.

Possible conclusion:
> The matched-retention comparison yields accuracy mean changes in different
> directions across the three evaluated tasks. It does not establish an overall
> advantage for score-ranked selection. These results make the retention rule,
> alongside the retained count, an explicit comparison factor when assessing
> token-selection methods.

The negative qualification matters because it is the result being concluded.
Do not reuse this ending for a method with a well-supported positive finding.

For a different synthetic paper that implements two fixed linear projections
and checks numerical agreement, an ending can instead explain how those
projections support repeated directional queries while the underlying vectors
stay fixed. It need not repeat the absence of runtime measurements unless it
makes a performance claim.

## Revision and completion checks

Compare conclusion → introduction → actual evidence:
- Does the ending answer the same question and honor the promised contribution?
- Is the main idea or finding intelligible without a component inventory?
- Does it retain the current direction, assumptions and material uncertainty?
- Is every consequence already supported in the body?
- Are future possibilities distinguishable from achieved outcomes?
- Does it end at the contribution or a specific next question rather than
  generic praise, repeated self-defense or a new claim?

A valid rewrite may preserve most of an existing conclusion. If no concrete
problem remains, stop rather than generating endless alternate endings.
