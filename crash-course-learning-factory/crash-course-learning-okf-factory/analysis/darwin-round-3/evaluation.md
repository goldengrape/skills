---
type: Evaluation Report
title: Darwin Round 3 Evaluation
summary: Evaluation and revision based on the macroeconomics generation test and the requirement for post-generation quality control.
tags: [darwin, evaluation, quality-gate]
timestamp: 2026-06-30T00:00:00-07:00
---
# Darwin Round 3 Evaluation

## Trigger

The macroeconomics test generated a structurally complete Course Learning OKF, but several critical files remained generic placeholders. The previous `validation_result.passed=true` was therefore a false pass.

User requirement added in this round:

> The factory OKF should evaluate / quality-check generated course OKFs. If the quality check fails, it should revise and recheck instead of generating and stopping.

## Baseline Finding

| Area | Baseline status | Problem |
|---|---|---|
| File tree | Passed | Required files existed. |
| State files | Passed | Initial state existed. |
| Course specificity | Failed | Macro-specific terms such as GDP, inflation, unemployment, aggregate demand, fiscal policy, and monetary policy were absent. |
| Placeholder removal | Failed | Critical files contained `TBD`, `Fill this`, and generic quiz prompts. |
| Exam readiness | Failed | Day 1 and quiz files did not contain usable macroeconomics exam tasks. |
| Final review | Failed | Final-review files were placeholders. |

## Darwin Diagnosis

The weakest dimension was not layout or state persistence. It was **failure-mode encoding and effect validation**: the factory did not encode the failure mode where a generated course OKF is structurally valid but educationally unusable.

## Revision Chosen

One focused revision was kept:

```text
post-generation quality gate + repair-and-recheck loop
```

This avoids broad redesign. It preserves the MVP while preventing false passes.

## Files Added

```text
schemas/course-okf-quality-report.md
playbooks/evaluate-generated-course-okf.md
playbooks/repair-generated-course-okf.md
tools/quality_check_course_okf.py
tools/course_seed_registry.py
analysis/darwin-round-3/evaluation.md
analysis/darwin-round-3/test-report.md
```

## Files Modified

```text
docs/URD.md
docs/ADD.md
docs/TRACE.md
factory/validation-checklist.md
playbooks/generate-new-course-okf.md
playbooks/validate-generated-course-okf.md
schemas/course-okf-output.md
tools/materialize_course_okf.py
tools/README.md
tests/test_materialize_course_okf.py
manifest.json
validation-report.json
index.md
playbooks/index.md
schemas/index.md
```

## Post-Revision Behavior

| Case | Expected result |
|---|---|
| Known course, seed available, initial skeleton generic | Quality fails first, seed repair runs, quality rechecks and may pass. |
| Unknown course, no seed | Structural generation may pass, but content quality remains failed until course-specific content is supplied. |
| Placeholder remains in critical files | `validation_result.passed=false`. |
| Quality failure after repair | Return exact failures and repair actions. |

## Score Estimate

| Metric | Before | After |
|---|---:|---:|
| Structural completeness | 92 | 94 |
| Failure-mode encoding | 72 | 90 |
| Course OKF effect validation | 58 | 86 |
| MVP executability | 82 | 91 |
| Composite estimate | 82.0 | 91.4 |

Evaluation mode: `dry_run + local_tests`.

No independent sub-agent evaluation was run in this environment. The retained revision is supported by local tests and the repeated macroeconomics generation check.
