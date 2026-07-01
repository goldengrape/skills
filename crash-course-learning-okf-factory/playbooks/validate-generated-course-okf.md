---
type: Playbook
title: Validate Generated Course OKF
description: Procedure for validating a generated course-specific OKF before returning it.
tags: [playbook, validation, output]
timestamp: 2026-06-30T00:00:00-07:00
---
# Trigger

Run after generating a Course Learning OKF and before returning it to the user.

# Procedure

1. Read [Validation Checklist](../factory/validation-checklist.md).
2. Check every required file in [Course Instance Layout](../schemas/course-instance-layout.md).
3. Check that `resources.md` records source confidence and source gaps.
4. Check that `state/current-state.md` and `state/next-action.md` are parseable.
5. Check that `plan/day-1.md` is immediately runnable.
6. Check that daily time blocks sum to `daily_minutes` or record a warning.
7. Check that A/B/C priorities appear in the plan.
8. Check that resume and state update rules are present in the output object.
9. Run [Evaluate Generated Course OKF](evaluate-generated-course-okf.md) to inspect content quality.
10. If the quality gate fails, run [Repair Generated Course OKF](repair-generated-course-okf.md), then rerun the quality gate.
11. Return a validation result using [Course OKF Output](../schemas/course-okf-output.md).

# Output

```yaml
validation_result:
  passed: true
  structural:
    passed: true
    missing_files: []
    warnings: []
    source_gaps: []
  quality_gate:
    passed: true
    attempts:
      - action: initial_quality_check
        passed: true
    final_report:
      score: 92
      failures: []
      repair_actions: []
```

# Failure Handling

| Failure | Action |
|---|---|
| Missing required file | Create the file before returning. |
| Missing state file | Create it and rerun validation. |
| Missing source confidence | Add confidence and source-gap notes. |
| Day 1 not runnable | Rewrite `plan/day-1.md`. |
| Daily package too large | Move lower-priority items to later days or C-topic recognition. |
| Content quality fails | Repair failed files using `quality-report.json`, then rerun the quality gate. |
| Quality still fails after repair | Return the bundle with `passed: false` and list exact failures and repair actions. |


## Teaching Runtime Quality Gate

Run `tools/lint_prompt_visibility.py` or equivalent checks. The generated Course OKF fails if:

- student-visible quiz or plan prompts reveal hidden answer elements before the learner answers;
- `teacher/teacher-notebook.md` is missing or lacks `teacher_says` / `teacher_thinks`;
- `state/score-history.md` lacks `score_type` or `prompt_visibility`;
- `teacher/time-policy.md` does not distinguish soft and strict modes;
- interest-led branch or engagement rules are missing.

The gate passes only when the teaching interaction can be run without prompt leakage and without treating learner interest as a default error.
