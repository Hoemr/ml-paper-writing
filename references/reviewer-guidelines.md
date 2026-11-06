# Scientific review, shared writing standard and author voice

This file owns narrative and anti-defensive decisions across all sections.
Apply its shared standard during drafting and revision; section guides supply
local craft, while style-conventions owns punctuation and artifact mechanics.
The standard incorporates the user-supplied anti-defensive-writing-en guidance;
no sibling skill is required.

## Shared writing standard

### Build the story around the strongest supported value

Treat the paper as a press conference: identify its most publishable strength
and build the most favorable, complete and persuasive account the evidence
supports. Do not give every attempted idea, metric or observation equal space.

- Center the genuine advantage: a new capability, problem, mechanism,
  perspective, applicability, cost, efficiency, scalability or meaningful
  trade-off. An empirical distinction or negative finding can itself be the
  contribution. Material with no role in that contribution need not enter the
  main storyline.
- Explain the final standing logic: why the problem matters, where existing
  approaches leave a gap, what this work provides and how the evidence supports
  it. Remove chronological accounts of attempts, failures and editorial audits.
- Choose the task, evaluation dimension, scenario, constraint and comparison
  frame in which the supported value is clearest. Do not make a non-strength
  the paper's headline contest or promise wins on every metric and dataset.
  State under which conditions the advantage holds, what problem it solves and
  why it matters. Explain its cause only when that explanation is supported.
- Let the strongest evidence determine the story. When it cannot support the
  original framing, reconsider the problem, contribution order, headline result
  and experiment structure rather than defending the original plan. Synchronize
  title, abstract, introduction and conclusion within the authorized scope;
  identify broader changes when only a local edit was requested.

### State contributions without self-undermining

Remove authorial self-judgments such as "unfortunately," "merely," "only
achieves," "still lags far behind," "limited improvement" and "severely
insufficient." Avoid verdicts such as "our method is weaker" or "fails to
surpass" that turn a bounded comparison into a judgment on the whole method.
Do not manufacture reviewer objections, volunteer unrelated weaknesses or
complete an opposing argument the paper does not need to answer.

Before discussing unfavorable material, use this decision order:

1. Remove material irrelevant to the core claim.
2. Narrow an overbroad claim to the contribution the evidence supports.
3. Choose an evaluation dimension or scenario that represents that value.
4. Explain differing goals, constraints or a reasonable trade-off when supported.
5. Reorganize experiments so the demonstrated advantage is the narrative and
   visual center.
6. Reframe the paper's story if its current central claim remains unsupported.
7. State an unfavorable result plainly when it materially affects the central
   conclusion and cannot be addressed through accurate framing.

This order governs selection, emphasis and wording. Keep numbers, comparison
conditions and material evidence accurate. A narrower claim must not imply
overall superiority; a selected scenario must be named; a trade-off needs
evidence on both sides. Do not invent an explanation or silently change a
metric, denominator or evaluation protocol. Place necessary qualifications
beside the affected inference and satisfy required limitations/disclosures,
without repeating them as a weakness inventory across the paper. State known
facts directly and attach uncertainty to the specific untested inference.

### Give experiments and sections a persuasive job

Experiments are tools of argument. Each main-text experiment should establish
the claimed outcome, test the key mechanism, demonstrate value in the target
scenario or distinguish a plausible alternative explanation. Move, condense or
remove distracting material; propose redesign only when experiment design is
in scope. Do not run new experiments as part of a writing-only task.

The abstract and introduction should quickly establish the important problem,
the gap, the distinctive approach and the strongest result with its meaning.
Establish the contribution before discussing limitations. Methods explain the
final design, results support the selected claims, and discussion interprets
their value. The conclusion reinforces what was solved, proposed or established
and why it matters; do not end with a fresh self-negation or expanded limitations.

### Check before delivery

Check the requested scope for sentences that expand the paper's obligations,
raise unasked objections, generalize a local observation into a universal flaw,
or use a negative judgment broader than the evidence. Remove work-report
chronology and non-strength headline contests. Confirm that the abstract's
opening establishes both problem and contribution, the advantage is explicit,
and the conclusion closes on the supported takeaway. Use these checks during
drafting as well as final review, not as a new paragraph of disclaimers.

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

Apply the core standard's selection and reframing order before deciding that
an unfavorable observation belongs in the narrative. The examples below help
preserve the meaning of material that is actually needed; they do not require
volunteering weaknesses or assigning every result equal prominence.

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
A short revision needs only the material reasons. This table is not a priority
order; the core standard supplies that order. Do not resurrect rhetoric
the author explicitly removed, even in another section.

### Distinguish selecting claims from suppressing evidence

A method abstract can explain a supported construction and measured memory
comparison without listing every unfinished evaluation. Keep the comparison's
budget and measurement boundary. If it also claims accuracy superiority, mixed
accuracy findings constrain that claim there. If quality/cost is the central
trade-off, describing cost alone can mislead even without the word "accuracy."

Establish the contribution before introducing limitations. Put a necessary
boundary where the reader needs it. A precise definition at the comparison
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
| Self-dismissal | "Unfortunately, we only evaluated X on these tasks." | First ask whether an untested-scope discussion serves the claim. Where scope is needed, REFRAME: "The evaluation covers [named task scope]." Do not add an inventory of untested settings. |
| Genuine uncertainty | "The preliminary results suggest that X may help." | KEEP uncertainty unless evidence justifies a change. "X demonstrably works" is not a style edit. |
| Scalar versus gradient property | "The correction has zero trajectory mean, but we do not claim policy-gradient preservation." | REFRAME around the proved trajectory-mean identity and its scope. Discuss the gradient distinction where a claim actually depends on it; do not append the negation to every summary. |
| Different efficiency metrics | "We did not measure long-run training speed; this profile measures peak memory." | REFRAME as "The profile measures peak memory." Retain the speed gap where speed or overall efficiency is assessed; never rewrite as "X accelerates training." |
| Unresolved comparison | "X has a higher point estimate, but available uncertainty does not establish superiority." | KEEP the unresolved comparison. Neither "X outperforms" nor "the methods are equivalent" is supported. |
| Mixed findings | "X is effective, although two tasks decline." | Narrow the claim to the supported benefit or trade-off and organize around that contribution. Report task results where needed to assess it; do not turn a local comparison into a verdict on the entire method. |
| Internal editing diary | "We fixed the denominator after several audits." | State the current denominator in a normal final manuscript. Preserve the history in a correction notice or revision letter when required or scientifically material. |
| Repeated figure disclaimer | Every caption says "This is not independent validation." | Define the actual repeated-run, shared-input or same-checkpoint design at appropriate entry points; retain that identity in captions needed for standalone interpretation. |

Unsupported "first," "significant," "optimal" and "state of the art" need an
accurate statement or evidence, not a different flattering adjective.
When a negative finding, failure analysis or correction is itself the central
contribution, foreground the insight it establishes. This does not require
rewriting an unrelated method paper as a critique of its own shortcomings.

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
