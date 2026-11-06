# Calibrate claims to their evidence

Adapted from Best-Paper-Writing-Skill b9eff99 (CC BY 4.0), with evidence-specific
boundaries; see [provenance](bestpaper/README.md). This is default writing guidance.
Use the strongest accurate statement the evidence supports, avoiding both inflated
claims and unnecessary hesitation. These are different evidence types, not a
universal ranking of proof above all empirical research.

| Evidence and claim type | Appropriate expression | Boundary to preserve |
| --- | --- | --- |
| Established theorem/proof | “We prove … under …”; state the actual result directly | Assumptions, quantifiers, object and proof scope; a simplified model does not prove real training behavior |
| Repeated consistent comparisons | “X improves Y across A, B and C”; “We demonstrate …” | Actual tasks, metrics, budgets, uncertainty and exceptions; several benchmarks do not imply universal superiority |
| Controlled comparison/intervention | “Replacing X changes Y by … under …” | Changed and held-fixed factors; an ablation does not uniquely establish a mechanism or eliminate every confound |
| Single-setting observation/correlation | “We observe …”; state the measured association | Sample, setting and uncertainty; avoid causal or broad generalization claims |
| Untested explanation/design rationale | “This motivates …”; “We hypothesize/conjecture …” where accurate | A reason for a design is not measured validation; confident phrasing cannot promote an explanation into a finding |
| Resource or measurement contribution | State what was constructed, covered or measured | Actual availability, collection/validation procedure, precision and demonstrated uses |

Assert supported observations plainly. “Our key insight is …” is not needed to
make an observation important. Conversely, a formal conjecture must not be
renamed a theorem or an observation to avoid a supposed weak phrase. A negative
result may establish a counterexample without overturning an entire research area.

## Extend the existing evidence map

The [evidence workflow](evidence-workflow.md) owns the single record. When needed,
add the intended claim wording, strongest supported alternative, necessary scope,
method/proof location, result/control locations and presentation role. Several
pieces of evidence can support one claim; one result can inform several claims.
Do not require an experiment for a formal result, or an ablation for every module.

Classify numerical details by job:

- **Headline:** establishes the central advance or defines a resource/scale.
- **Supporting:** explains an important contrast, operating condition or mechanism.
- **Table-only:** useful detail that does not need repetition in narrative prose.

Choose counts from the argument and venue, not a target of one or two numbers.
An abstract can have no numerical claim when the contribution is theoretical or
qualitative. Preserve units, denominators, baselines and precision where needed.

## Mixed findings and scoped confidence

Lead with the strongest supported value and integrate a necessary condition at
the point it changes the meaning. Do not turn a loss on one task into a global
judgment of the method, or selected wins into a claim of overall superiority.
A quality/cost trade-off central to the contribution must stay intelligible.
Do not hide decisive contradictory evidence in author notes or limitations.
Required limitations/disclosures still follow current venue rules.

Synthetic example: a method uses less peak memory at the same training schedule,
with higher accuracy on one task and lower accuracy on another. State the memory
benefit and relevant quality trade-off. Do not infer speed, equal-quality cost,
or uniform accuracy gains. If a theorem establishes unbiasedness for independent
samples, say so; do not silently extend it to dependent samples in the real system.

## Delivery check

The title, abstract, introduction, result narration and conclusion must preserve
the same claim identity and strength, while serving different reader functions.
Verify any new “first”, “optimal”, “causes”, “robust” or “general” assertion against
the evidence it requires; do not ban the word when that evidence exists. Missing
support is an exact author query or a scoped scientific correction, not filler.
