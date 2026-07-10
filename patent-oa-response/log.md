# Bundle Update Log

## 2026-07-09

* **Creation**: Created the Patent OA Response Skill Bundle in OKF-style markdown.
* **Design**: Split the system into one user-invoked orchestrator and reusable model-invoked skills.
* **Policy**: Added bounded iteration rules to avoid self-reinforcing win-rate loops.
* **Refactor**: Added URD, ADD, and TRACE documents; separated OA analysis from fact reading; made win-rate evaluation the only probability output; changed revision variants to require second simulation and evaluation before final selection.

## Darwin Optimization

* **Domain rubric**: Added domain research, domain rubric, test prompts, and rubric evaluation metadata.
* **Quality gates**: Added domain quality gates and final-output quality-check template.
* **Workflow**: Inserted hard-gate checks after candidate formation, after evaluation, after A/B selection, and before final response drafting.
* **Probability boundary**: Removed probability ranking from examiner simulation; kept probability intervals only in win-rate evaluation.
* **Jurisdiction boundary**: Added jurisdiction/procedure-stage confirmation to intake and legal safety rules.
* **Traceability**: Updated URD, ADD, TRACE, usage, index, policy index, and template index.

## Generic Release

* Removed all real case-specific reports, regression-case files, identifiers, company names, file names, application numbers, and concrete citation numbers from the distributable bundle.
* Kept only generalized failure patterns and quality gates that are useful across OA matters.
* Added a privacy audit document and generic regression suite.
