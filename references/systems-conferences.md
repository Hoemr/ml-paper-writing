# Systems contribution and evaluation

Read for systems papers or an ML-to-systems revision. Current submission policy
is owned by [checklists.md](checklists.md), including official venue/year lookup;
this file does not maintain a second deadline, scoring or page-limit table.

## A systems argument must come from the artifacts

Identify the workload, bottleneck, mechanism, implemented boundary, and measured
benefit. Explain why an existing system cannot achieve the same outcome under
the same constraints. An ML benchmark result alone does not establish a systems
contribution; changing venue does not create implementation or deployment evidence.

A useful structure is introduction → workload/background → design choices →
implementation → evaluation → discussion/related work. Adapt it to the actual
contribution rather than filling mandatory-looking slots.

## Evaluation decisions

Connect end-to-end behavior to the mechanism with a targeted diagnostic or
microbenchmark. Match hardware, workload, data, tuning budget and measurement
boundaries. Distinguish throughput, latency, memory, energy and cost; improvement
in one does not imply improvement in another. Document warm-up, repetitions,
variability, and which components the accounting includes where data exist.

Use scaling, failure behavior, deployment lessons, or artifact evaluation only
when relevant to the claim and supported by actual artifacts. Do not invent
production experience or prescribe distributed robustness for a private program.

## Format conversion

Read [templates/README.md](../templates/README.md) for the conversion procedure.
Reframe only supported findings for the target community. Move explanatory
detail as the verified page budget permits; retain limitations, controls, and
evidence necessary to assess the result. Additional experiments remain open
work unless separately authorized and completed.
