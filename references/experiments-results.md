# Experiments and results: use comparisons to answer the paper's questions

Use for experimental-section planning, writing, reorganization or revision.
Writing from completed experiments and designing new experiments are distinct
tasks. In a writing request, identify important missing evidence without
pretending to have produced it or requiring a new experiment before editing
independent supported results.

## Recover the evaluation and each comparison's purpose

Read the main claims, current experimental text, source tables/plots and the
method variant that generated them. Use [evidence-workflow.md](evidence-workflow.md)
for provenance and [citation-workflow.md](citation-workflow.md) for source
attribution. A manuscript table can be the working source for a local rewrite;
do not demand run logs unless needed to settle a concrete conflict.

Privately associate each central question with available evidence:

| Question | Evidence and reading task |
| --- | --- |
| Does the method improve the stated outcome? | Matched main comparison, actual metric and uncertainty. |
| Which design choice matters? | A controlled replacement, ablation or other diagnostic with its precise changed factors. |
| Under which conditions does the finding hold? | Actual coverage, subgroup/regime results, sensitivity or distribution-shift evaluation. |
| What resources are required? | Measured accounting boundary and quality/workload conditions. |
| What behavior explains or illustrates the result? | Diagnostic or qualitative evidence with selection and inference scope. |

Use only rows the paper needs and has evidence for. A method paper does not
automatically require every common ablation, benchmark, robustness experiment
or visualization. An empirical analysis may put a diagnostic comparison first;
a systems paper may center an end-to-end workload and its bottleneck.

## Write setup so the results are interpretable

Establish the actual protocol before or beside the first result that needs it:
- Tasks, datasets/versions, splits and independent evaluation units.
- Model, baseline implementation/version, input access and relevant resources.
- Training, tuning, model/checkpoint selection and inference conditions.
- Primary metrics, direction, scale, aggregation and reference comparison.
- Runs, seeds, resampling and the meaning of reported uncertainty.
- Hardware, precision, batch/workload and cost boundary when resource claims
  depend on them.

Separate reported facts from missing metadata. Do not call an unclear
comparison fair because both rows use the same benchmark name. Data, model
size, pretrained access, tuning effort, generation/sample budget and retrieval
or tool access can change the comparison. Describe meaningful mismatches
rather than inventing protocol equality.

Identify which baseline numbers were rerun and which were taken from a source.
Literature values may be informative context while using different protocols.
Use distinct groups or clear labels instead of implying a controlled rank.
Choose baselines because they test the claim or represent a relevant
alternative, not because they are easy to beat.

Test data must not be described as validation data or vice versa. When
checkpoint, threshold or hyperparameter selection affects interpretation,
explain the actual selection data and rule. Unrecorded selection rules remain
queries; do not add leakage-free behavior as boilerplate.

## Organize around findings and questions

Decide what each subsection adds to the main argument. A useful order might be
overall comparison, a targeted design diagnostic, then the conditions of
success or failure. A failure-analysis paper may start with the failure pattern.
The logic, not experiment chronology or dataset names alone, chooses the order.

Use headings that reveal the question or supported observation. "Ablations"
can be sufficient for a compact section; a more informative heading may help
a complicated diagnostic. Do not turn unresolved comparisons into strong
finding titles.

A result paragraph needs enough design context to interpret the observation,
the actual readout and a conclusion licensed by it. These are functions,
not a fixed question-method-number-caveat-template for every paragraph.

### Describe the artifact's informative feature

Point to the row, column, metric or curve region carrying the finding. Explain
the pattern instead of reading every table cell. A global pattern plus a
justified exception often teaches more than a sequence of selected wins.

Keep necessary effect sizes and uncertainty near the claim. Complete numeric
coverage belongs in a readable table or source data. Preserve important adverse
results, missing comparisons and incomparable conditions. Do not cite one
variant's table as evidence for another variant's mechanism.

If giving a computed difference, preserve metric units. Accuracy changing
from 70% to 72% is +2 percentage points, not automatically a 2% relative
increase. A micro-average, macro-average and average of dataset scores answer
different questions. Do not invent a new average or statistical summary to
make the narrative cleaner.

### Separate observation from interpretation

Give the actual observation before a proposed explanation. A more favorable
diagnostic can motivate an explanation without establishing the downstream
mechanism. Matching budgets reduces specified confounding; it does not make
all explanations identifiable.

Do not equate non-significance with no effect or equivalence. A significant
result in one condition and a non-significant result in another do not by
themselves demonstrate a difference between conditions. Different point-estimate
directions are not an established task interaction.

For seeds/runs, intervals and paired designs, report the actual independent
unit and procedure. Standard deviation across training seeds is not a
confidence interval or evaluation-example standard error. If only summaries
are available, write the supported descriptive comparison; do not fabricate
tests, paired outcomes or a variance for their difference.

## Write the important experimental types accurately

### Main comparison

State the outcome and relevant comparison setting. A higher point estimate
can be described as a higher observed mean without asserting reliable
superiority. A result under one budget does not cover all model scales or
operating regimes. Avoid repeating full setup in every paragraph once its
attachment is clear.

### Ablations and replacement controls

Explain what changed, what was held fixed and which question it tests.
Removing a component can also change parameter count, training signal,
information access or computation. Keep those changes explicit. A drop after
removal does not uniquely prove the proposed mechanism or make component
contributions additive.

Replacement controls can isolate a factor better than deletion, but use only
the controls actually performed. Do not invent random controls or claim they
were planned. When designing experiments was requested, propose a control and
its expected diagnostic role as future work, separately from completed results.

### Sensitivity, robustness and transfer

Name the varied parameter or distribution, range, selection rule and actual
coverage. Stable behavior across a tested range supports that range, not all
hyperparameters. Generalization to a held-out split, new dataset, domain,
model family or time period are different tests. A collection of related
benchmarks is not automatically evidence for every type of transfer.

Show meaningful exceptions rather than only a pooled average. Do not guess
that data size or label noise caused a subgroup difference without tests.

### Efficiency and scaling

Distinguish elapsed time, throughput, latency, allocated/peak memory, energy,
tokens, sample count and monetary cost. Account for preprocessing, extra models,
retrieval, selection and amortization when material to the claim.

A fixed-step cost comparison differs from cost at a fixed quality target.
A larger batch can change throughput and latency in different directions.
Report measured quantities with hardware, precision and workload conditions
needed to interpret them. Theoretical operation counts do not become measured
speedups. Report a quality/cost trade-off when it is central to the claim.

### Qualitative cases and diagnostics

State how cases were selected and what the reader should inspect. An example
can illustrate a behavior or explain a failure, but a selected success does not
establish prevalence. A heatmap, embedding plot or attribution score describes
its own computed quantity; it does not independently prove a causal mechanism.

Do not retrofit anecdotes as originally hypothesized findings. Qualitative
evidence can be central when the actual question concerns process or context;
do not dismiss it for lacking a leaderboard.

## Main text, captions and appendix

Main text explains decisive findings and necessary controls. Captions define
panels, groups, n and uncertainty. Methods/setup specifies how quantities were
obtained. Appendix holds detailed configurations, full task breakdowns,
extended diagnostics and supporting derivations.

Move detail without hiding a result that changes the central claim. Preserve
unique definitions and point to the destination. Use
[style-conventions.md](style-conventions.md#figures) for caption semantics and
[reviewer-guidelines.md](reviewer-guidelines.md) for repeated defensive prose.
Do not append every unmeasured property to every result paragraph.

## Synthetic result rewrite

Premises only: three training seeds at the same 10,000-update schedule.
Accuracy means for the full method versus a replacement control are 72.0%
versus 71.1% on A and 65.2% versus 65.7% on B. The source supplies across-seed
standard deviations but no paired outcomes or comparison test. Peak allocated
memory is 20 GB versus 24 GB on the recorded hardware. Runtime is unmeasured.

Weak:
> Extensive experiments prove that the module consistently improves learning
> and accelerates training.

More informative:
> At the matched training schedule, the full method has higher mean accuracy
> on A and lower mean accuracy on B than the replacement control. The comparison
> therefore gives mixed observed accuracy changes under this protocol. Peak
> allocated GPU memory decreases from 24 GB to 20 GB.

Describe uncertainty with its definition in the actual table/caption or nearby
text. The memory observation needs no invented speed claim and the accuracy
pattern needs no invented causal explanation.

## Completion checks

- Each important experiment serves a real paper claim or question.
- Protocol, selection, baseline source and comparison mismatches are explicit.
- Numbers, units, aggregation and uncertainty agree with sources.
- Text explains the informative pattern rather than reciting the table.
- Ablations and diagnostics are interpreted only to their identifying scope.
- Adverse results and material quality/resource trade-offs remain visible.
- Appendix and caption pointers preserve full definitions and evidence.
- Missing analyses remain author queries or proposals, not fabricated findings.
