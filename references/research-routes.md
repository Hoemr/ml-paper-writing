# Research type and argument route

Adapted from Best-Paper-Writing-Skill b9eff99 (CC BY 4.0), expanded for this
collection; see [provenance](bestpaper/README.md). Use in substantial drafting
or restructuring, not as a mandatory questionnaire for a sentence edit.

Choose the main intellectual deliverable rather than its buzzwords or venue.
Mixed papers can use a primary and secondary route. L1–L8 labels are retrieval
keys for the optional exemplar bank, not a quality hierarchy or exhaustive
classification. Systems and survey routes remain available independently.

| Type | Reader's route | Evidence that must carry the promise |
| --- | --- | --- |
| L1 Method improvement | Existing capability → concrete remaining difficulty → observation/design principle → operation → demonstrated benefit | Interpretable comparisons and diagnostics relevant to the claimed difference; no invented ablation requirement |
| L2 New capability | Wanted operation and setting → what existing approaches enable → missing capability → construction → demonstration and scope | Evidence that the named capability is achieved; qualify “previously impossible” by verified prior work |
| L3 Scaling/empirical regularity | Practical decision or open question → variables, response and budget → systematic observations → fitted relation/recipe → validation | Observed ranges, fitting/selection procedure and held-out tests if performed; no extrapolation beyond measured scope without support |
| L4 Re-examination | Established belief and its evidence → precise question → discriminating test → findings → revised understanding | Faithful comparison with the original claim's setting; distinguish counterexample, reproduction failure and general refutation |
| L5 Mechanism/analysis | Phenomenon → plausible explanations → proposed mechanism → evidence distinguishing explanations → implication | Controls, interventions, analysis or model appropriate to the inference; correlations alone do not identify mechanism |
| L6 Theory | Formal question → closest known results → main result in words → assumptions and comparison → proof idea → consequence | Theorem statement and proof under actual assumptions; conjectures remain conjectures and experiments are optional |
| L7 Dataset/benchmark/resource | Research need → missing resource capability → construction/coverage → quality and use → demonstrated findings/access | Collection and qualification procedure, access status and supported utility; scale alone is not utility |
| L8 Measurement/instrumentation | Phenomenon to observe → sensing/measurement constraint → principle/instrument → calibration → what becomes measurable | Measurement validity, uncertainty, operating range and appropriate comparisons; not simply another model leaderboard |
| Systems | Workload and bottleneck → design objective → implementation decisions → end-to-end effect → cost and deployment scope | Measured workload, resource boundary, baseline and implementation; see systems-conferences.md |
| Survey/synthesis | Question and scope → source-selection basis → organizing distinctions → synthesis → supported implications | Verified literature and documented search if claiming systematic coverage; no invented empirical contribution |

## Motivation diagnostics for method and capability papers

- **Failure condition:** what exactly fails, when, and what evidence identifies
  the cause? If only the symptom is observed, do not assert its cause.
- **Cost/trade-off:** which resource or competing goal makes a capable solution
  unsuitable? Quantify an obvious alternative only when actually measured or derived.
- **Capability gap:** what input→output operation is missing, and do partial
  baselines still provide useful comparisons?
- **Insight:** which observation or analytical relationship motivates the simpler
  construction? State it before opaque module names.
- **Trend/open question:** what concrete development motivates the next question?
  Use verified history, not an invented three-stage progression.

Choose the explanation that makes this work necessary, with a secondary motive
only when useful. Tension can be uncertainty or an open question; prior methods
need not be portrayed as defective. Theory may lead with a result, resources with
what they enable, and negative findings with the distinction they establish.

For each route, preserve the principle that the contribution answers the opening
question. No fixed paragraph count, contributions list, stance sentence, example
scene, short-sentence quota or Figure 1 placement is required.
