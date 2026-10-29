# Submission requirements: verify the exact venue and year

This file owns submission policy checks. Do not infer page limits, unlimited
appendices, mandatory checklists, anonymity, AI disclosure, or resubmission rules
from another venue or an old bundled template. Read the current official author
instructions for the selected venue, year, track and submission stage.

## Official starting points

| Venue | Primary policy source |
| --- | --- |
| NeurIPS | [Conference site](https://neurips.cc/); [checklist guide](https://neurips.cc/public/guides/PaperChecklist) |
| ICML | [Conference site](https://icml.cc/) → selected year's author instructions |
| ICLR | [Conference site](https://iclr.cc/) → selected year's author guide |
| STOC | [Selected conference](https://acm-stoc.org/); for 2027 use the [official CFP](https://acm-stoc.org/stoc2027/stoc2027-cfp.html) and [stage-specific guide](venues/stoc2027.md) |
| ACL / ARR | [ACL Rolling Review](https://aclrollingreview.org/); [style files](https://github.com/acl-org/acl-style-files) |
| AAAI | [AAAI](https://aaai.org/) → selected year's author kit and CFP |
| COLM | [COLM](https://colmweb.org/); [template](https://github.com/COLM-org/Template) |
| OSDI / NSDI | [USENIX conferences](https://www.usenix.org/conferences) → selected CFP |
| ASPLOS | [ASPLOS](https://www.asplos-conference.org/) → selected CFP and cycle |
| SOSP | [SIGOPS](https://www.sigops.org/) → selected conference CFP |

Record the source URL and access date in the task's submission audit, with the
resolved values for: main/appendix/reference limits, paper/column width, required
sections and checklist forms, anonymity, disclosure, track/cycle, resubmission,
deadlines/time zone, and supplementary/artifact rules. Report unavailable or
ambiguous policies explicitly. Do not install or replace templates automatically.

## Venue-specific requirements

For STOC 2027 writing, citation formatting or conversion, read
[the STOC 2027 guide](venues/stoc2027.md). It separates initial submission
(single-column, at least 11pt, Letter, 1-inch margins, no total page cap) from
accepted ACM proceedings (sigconf, 12-page cap), and covers the first-12-page
exposition, reference recommendations, AI disclosure and accompanying materials.
Recheck its official source for the current task; do not extend 2027 policies
to another year or treat recommended choices as mandates.

## General preparation checklist (not universal venue mandates)

- Claims match measured results or stated theorem assumptions; proposals and
  tested variants are clearly distinguished.
- Comparators, tuning budgets, splits, seeds and uncertainty units are explicit.
- Material limitations and negative results remain visible.
- Named models/data/benchmarks and added citations have appropriate verified support.
- Required sections, disclosures and forms follow the exact official policy.
- Source compiles; new undefined references/citations and layout overflow are fixed.
- Figures have captions and final-size visual review; method-figure rules remain
  in the built-in [figure-workflow.md](figure-workflow.md) module.
- Anonymous artifacts follow venue policy without deleting scientifically needed
  self-citations. Supplementary material and reproducibility instructions are coherent.

Use [templates/README.md](../templates/README.md) for setup/conversion mechanics;
[systems-conferences.md](systems-conferences.md) owns systems argument/evaluation.
Submission or publication requires a separate user instruction.
