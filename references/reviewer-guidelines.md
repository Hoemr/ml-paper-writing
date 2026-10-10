# Evidence review and a final wording pass

## Scientific assessment first

Read the claim–evidence map against the manuscript. Check soundness (assumptions,
proofs, controls), clarity (definitions and reproducibility), significance (why
the supported finding matters), and originality (the precise distinction from
closest work). Use the target year's official review form when a score or formal
review is requested; scoring scales and review procedures are not universal.

Resolve mismatched budgets, denominators, missing controls, or conflicting values
through evidence or explicit qualifications. A stylistic edit cannot repair a
technical weakness. In systems work, also read [systems-conferences.md](systems-conferences.md).

## Small meaning-preserving edits

After ordinary drafting, consider a local change only when it helps present an
existing contribution or result. This adaptation draws on the canonical
Game-the-LLM-Reviewer repository; exact provenance is in [sources.md](sources.md).

- Make the supported contribution the grammatical focus.
- Express a measured comparison as an effect only with the same baseline, units,
  denominator and aggregation. Verify any arithmetic; retain original values.
- Move an existing abstract contribution earlier when its context and material
  qualifications remain clear.
- Replace empty self-dismissal with factual wording; retain scientific uncertainty.
- State evaluated scope directly with its untested boundary equally explicit.

For each change, compare original, rewrite and evidence. A knowledgeable reader
must recover the same claim, assumptions, quantifiers, causal status, certainty,
adverse findings, and limitations. Revert any change that strengthens inference.
No score gains or model preferences are guaranteed. No target-reviewer queries,
hidden directives, invented authority or repeated optimization loop are part of
this pass. Leave a satisfactory passage unchanged when no safe change helps.

## Defensive writing examples

Remove rhetoric that argues with an imagined criticism instead of reporting the
work: repeated “we stress,” anticipatory rebuttals, empty self-dismissal, and
unsupported reassurance. Preserve factual negations when they define a method,
theory, control or limitation. Do not mechanically delete “not,” “only,” “may,”
“preliminary,” or “simple”; assess what scientific information each word carries.

Use three decisions: **remove** empty rhetoric; **reframe** a supported fact as a
direct statement; **retain** a qualification whose removal changes inference.
Keep an essential caveat adjacent to its claim. Do not relocate it solely to make
the abstract or conclusion sound stronger. The original skill's blanket ban on
describing unmeasured work is not reinstated.

Distinguish claim selection from suppressing evidence. A method abstract may
report a verified mechanism and a measured cost comparison without summarizing
every task's accuracy curve or missing evaluation. In that case, keep the cost
comparison's budget condition in the abstract and report the accuracy evidence
in the results. If the abstract also claims accuracy superiority, the relevant
mixed results and uncertainty constrain that claim there. Avoid project-status
phrases such as “comparisons remain incomplete” when the abstract makes no claim
that depends on those comparisons.

These are authored teaching pairs. Their facts are hypothetical and must not
be transferred to a manuscript without evidence. A blocked rewrite illustrates
what an agent must refuse, not wording to imitate.

| Situation | Before | After / decision |
| --- | --- | --- |
| Empty reassurance | “We stress that our method is not merely a heuristic, and we believe it is useful.” | Remove the unsupported reassurance; state the actual mechanism or demonstrated property. Do not invent a theorem to replace “heuristic.” |
| Overexplaining a design choice | “It should be emphasized that we do not feed future context to the deployed policy.” | “The policy uses past context at deployment; future context is used in the training scorer.” Keep the two information boundaries. |
| Dismissive tone around a real observation | “Our method is unfortunately only evaluated on the supplied tasks.” | “The evaluation covers the supplied tasks; other task settings remain untested.” Preserve the boundary without apologetic wording. |
| A materially uncertain proposal | “The preliminary results suggest that X may help.” | Retain “preliminary” and “may” unless the evidence changes. **Blocked:** “The results demonstrate that X works.” |
| A scalar identity mistaken for a gradient guarantee | “The correction has zero trajectory mean; we do not claim that it preserves the policy gradient.” | Retain this qualification if readers could infer gradient preservation. A concise option is “The correction has zero trajectory mean; policy-gradient preservation is not established.” |
| A missing measurement | “We did not measure long-run training speed; the profile measures peak memory.” | “The profile measures peak memory. Long-run training speed remains unmeasured.” **Blocked:** “X improves training efficiency.” |
| An unresolved baseline comparison | “X has a higher point estimate, but available uncertainty does not establish superiority.” | Retain the unresolved comparison. **Blocked:** “X outperforms the baseline,” or deleting the second clause. |
| Internal revision diary | “We previously used the wrong denominator, then fixed it after an audit.” | In an ordinary final draft, state and justify the current denominator. For a correction notice, revision letter, or scientifically material version difference, preserve the history in the required form. |

Replace unsupported “first,” “significant,” “optimal,” and “state of the art” with
the actual supported statement rather than a different flattering adjective.
Delete redundant defenses once, not at the cost of a definition. An analysis of
failure or an audit can legitimately foreground negative findings.

### Final equivalence check

For every rhetorical edit, compare original → rewrite → evidence. Check:

- Same mechanism, conditions, comparator, units and denominator?
- Same proposed-versus-measured status and uncertainty?
- Same adverse results, untested scope and severity of unresolved defects?
- Same interpretation available to a knowledgeable reader?

If any answer is no, restore the qualification or reject the edit. Keep only a
short edit note outside the paper; do not turn the manuscript into an audit log.

## Deliver and handle feedback

Return the requested revised artifact plus a compact note about meaningful edits
and remaining evidence gaps. Keep editorial commentary out of manuscript prose.
Compile modified LaTeX and inspect effects on linked claims and page budget.

For actual rebuttal or revision letters, route to `$reviewer-response-rebuttal`
when available. Respond to each concern using evidence and completed changes;
distinguish remaining work from work already done. Preparation does not authorize
posting a response or submitting a manuscript.
