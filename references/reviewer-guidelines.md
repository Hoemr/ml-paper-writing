# Scientific review, direct expression and author voice

This file owns defensive-writing decisions and the equivalence review.
Use it after establishing the argument and evidence, not as a replacement for
section development. Abstract/introduction structure lives in their dedicated
guides; punctuation and artifact rules live in style-conventions.

## Scientific assessment first

Read claims against sources and author decisions. Check soundness (assumptions,
proofs, controls), clarity (definitions and reproducibility), significance (what
the finding changes), and originality (the precise distinction from closest
work). Use the current official review form only when a formal review or score
is requested; scores and criteria are not universal.

Evidence resolves mismatched budgets, missing controls or conflicting values.
Wording cannot repair a technical weakness. If the original claim overstates the
evidence, identify the necessary substantive correction separately from stylistic
edits. For systems claims also use [systems-conferences.md](systems-conferences.md).

## Defensive writing examples

### Identify the function before editing

Defensive rhetoric anticipates an imagined objection instead of explaining the
research: repeated "we stress," unsupported reassurance, self-dismissal,
audit-success announcements, and the same disclaimer after every observation.

Scientific boundaries have a different function: assumptions, information
access, measured quantities, negative or conflicting findings, sample scope,
independent units, denominators, missingness and alternative explanations.
These are not removable merely because a sentence contains "not," "only,"
"may," "preliminary" or "simple."

Ask what the reader would infer without the sentence. If its removal changes
the object, mechanism, comparison, certainty or consequence, preserve the
information and improve its expression.

### Choose the smallest justified editorial action

| Action | Use |
| --- | --- |
| KEEP | Necessary fact, uncertainty, reasoning or already effective prose. |
| TIGHTEN | Preserve information while reducing repetition or needless emphasis. |
| REFRAME | Express the actual object, operation or finding directly instead of rebutting a hypothetical criticism. |
| RELOCATE | Put implementation detail or editorial history where it belongs, keeping an adequate definition or condition beside the affected claim. |
| CUT | Delete information-free rhetoric or a true duplicate. Do not quietly delete a scientific proposition. |
| QUERY | The evidence or intended meaning is insufficient; identify the specific author question. |

These are editorial decisions, not mandatory labels to print for every sentence.
A short revision needs only the material reasons. Do not resurrect rhetoric
the author explicitly removed, even in another section.

### Distinguish selecting claims from suppressing evidence

A method abstract can explain a supported construction and measured memory
comparison without listing every unfinished evaluation. Keep the comparison's
budget and measurement boundary. If it also claims accuracy superiority, mixed
accuracy findings constrain that claim there. If quality/cost is the central
trade-off, describing cost alone can mislead even without the word "accuracy."

Put a boundary where the reader needs it. A precise definition at the comparison
entry can replace repeated disclaimers in later paragraphs. Detailed execution
records can move to methods or project notes. A restriction that changes the
central inference cannot disappear into an obscure appendix solely to make the
abstract or conclusion stronger. Required limitations and scientifically
material version history remain visible in their appropriate context.

State established facts directly and attach uncertainty to the untested link.
Do not weaken every observation with "may"; do not turn a candidate explanation
into a demonstrated mechanism to sound confident.

During the final pass, collect repeated scientific propositions across sections,
not just repeated words. Once unsupported speed, optimality or causal claims
are removed, do not automatically append their negations to every summary.
Retain the boundary at necessary claim/definition locations and in required
limitations; use other passages to explain the actual contribution. Summaries
that still imply the stronger claim must retain an adequate qualification.

### Synthetic ML teaching pairs

These hypothetical premises explain editorial decisions, not facts to insert in
a manuscript. Each rewrite requires matching evidence.

| Situation | Original | Decision / possible revision |
| --- | --- | --- |
| Unsupported reassurance | "We stress that X is not merely a heuristic and is highly reliable." | CUT the reassurance. Describe the actual construction or measured property; do not invent a theorem. |
| Information boundary | "It should be emphasized that we do not feed future context to the deployed policy." | REFRAME: "The deployed policy uses past context. The training scorer also uses future context." Retain both roles if verified. |
| Self-dismissal | "Unfortunately, we only evaluated X on these tasks." | REFRAME: "The evaluation covers [named task scope]." Keep untested scope explicit where extrapolation is discussed. |
| Genuine uncertainty | "The preliminary results suggest that X may help." | KEEP uncertainty unless evidence justifies a change. "X demonstrably works" is not a style edit. |
| Scalar versus gradient property | "The correction has zero trajectory mean, but we do not claim policy-gradient preservation." | KEEP the distinction when readers could infer preservation. State the proved identity and the unresolved gradient property directly. |
| Different efficiency metrics | "We did not measure long-run training speed; this profile measures peak memory." | REFRAME as "The profile measures peak memory." Retain the speed gap where speed or overall efficiency is assessed; never rewrite as "X accelerates training." |
| Unresolved comparison | "X has a higher point estimate, but available uncertainty does not establish superiority." | KEEP the unresolved comparison. Neither "X outperforms" nor "the methods are equivalent" is supported. |
| Mixed findings | "X is effective, although two tasks decline." | Scientific correction may be needed: report the observed directions and scope, then explain the supported contribution. Do not hide declines by calling them defensive. |
| Internal editing diary | "We fixed the denominator after several audits." | State the current denominator in a normal final manuscript. Preserve the history in a correction notice or revision letter when required or scientifically material. |
| Repeated figure disclaimer | Every caption says "This is not independent validation." | Define the actual repeated-run, shared-input or same-checkpoint design at appropriate entry points; retain that identity in captions needed for standalone interpretation. |

Unsupported "first," "significant," "optimal" and "state of the art" need an
accurate statement or evidence, not a different flattering adjective.
Negative results, failure analyses and correction reports can legitimately
foreground limitations; contribution-oriented writing does not require a
positive outcome.

## Natural expression without mechanical style recipes

Judge in order: correct facts and conditions → paragraph function → readable
information relationships → rhythm and word choice.

- Remove repeated closings that merely restate the preceding finding. Keep a
  closing that explains why the next comparison or design choice follows.
- Replace generic importance with the actual capability or understanding
  gained. Do not artificially shrink a genuinely broad supported contribution.
- Use contrast when there is an actual contrast. "Not merely X but Y" adds
  little when X and Y are rhetorical synonyms.
- Three real objects can be listed; three synonymous promotional adjectives
  can usually be reduced. Do not ban lists by item count.
- Keep "we" for real design choices when useful. Object-first or passive
  sentences can coexist naturally. Do not impose subject rotation.
- Split long sentences at distinct information tasks, checking conditions,
  quantifiers, negation and citation roles. No automatic word-count cutoff.
- Keep technical terms stable. Simplify internal labels for readers only when
  definitions, thresholds and source mappings remain recoverable.
- Let sections differ: concise summaries, developed motivation, precise methods,
  interpretable results and substantive discussion need different densities.

An authentic research rationale can explain a documented design choice.
"Initially failed," "unexpectedly," "we had hypothesized" and claims about prior
author work require actual records. Do not invent a discovery story to make
prose sound human. Do not optimize for AI-detector scores or promise reviewer
preferences, acceptance gains or policy certification.

## Final equivalence check

Compare original → rewrite → evidence at the level of scientific propositions:
- Same objects, mechanism, conditions and information access?
- Same comparator, budget, units, denominator and aggregation?
- Same quantifiers, negation, uncertainty and causal/theoretical status?
- Same adverse findings, alternative explanations and material untested scope?
- Same citation roles and interpretation available to a knowledgeable reader?

Moving a condition can preserve meaning when its attachment is still clear;
deleting it may not. Restore information lost by style edits. If new source
evidence or a scientific correction changes the claim, identify that change
explicitly rather than claiming equivalence.

## Deliver and handle feedback

Return the requested artifact and brief reasons for material decisions, keeping
editorial commentary outside paper prose. Use source and rendered checks only
for applicable artifacts; report actual coverage.

For rebuttals or revision letters use $reviewer-response-rebuttal when available.
Respond with evidence and completed changes, distinguishing remaining work.
Preparation does not authorize posting, correspondence or submission.
