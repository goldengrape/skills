---
type: Schema
title: Course OKF Output
description: Schema for the factory's generation result after creating a course-specific OKF.
tags: [schema, output, validation]
timestamp: 2026-06-30T00:00:00-07:00
---
# Course OKF Output

```yaml
course_okf_name: string
course_slug: string
created_files:
  - path: string # relative to the generated course OKF root
    required: boolean
    source_template: string
initial_state:
  current_day: integer
  days_remaining: integer
  completed_sessions: integer
  pass_readiness: very_low | low | unstable | plausible | stable
  risk_level: low | medium | high
  time_policy: soft | strict
  next_action: run_day_1 | continue | repair | review | simulate | final_review
seven_day_plan: plan/seven-day-plan.md
day_1_entrypoint: plan/day-1.md
state_update_rules:
  - read state before teaching
  - create session record after session
  - update score history after assessment with score_type and prompt_visibility
  - update teacher/teacher-notebook.md
  - update state/interest-ledger.md when learner-led branches occur
  - update recall deck for missed or high-value items
  - update misconceptions for wrong distinctions
  - write next action before ending
resume_rules:
  - read state/current-state.md
  - read state/next-action.md
  - read state/recall-deck.md
  - read state/misconceptions.md
  - read state/score-history.md
  - read latest sessions/*.md
  - read relevant plan/day-N.md
  - read teacher/teacher-notebook.md without displaying teacher_thinks
  - read state/interest-ledger.md
validation_result:
  passed: boolean # true only if structural, content quality, and teaching runtime checks pass
  structural:
    passed: boolean
    missing_files:
      - string
    warnings:
      - string
    source_gaps:
      - string
  quality_gate:
    passed: boolean
    attempts:
      - attempt: integer
        action: initial_quality_check | course_seed_repair | post_repair_quality_check
        passed: boolean
        score: integer
        applied: boolean
        seed_id: string | null
    repair_result:
      applied: boolean
      seed_id: string | null
      written_files:
        - string
      reason: string
    final_report:
      passed: boolean
      score: integer
      teaching_runtime_quality:
        passed: boolean
        failures: []
        warnings: []
```

# Rule

The output object is not a replacement for the generated OKF. It is a compact handoff summary that tells a human or AI where to start, how to resume, and whether the generated instance is actually usable.

`validation_result.passed` must not be set to true from file existence alone. It requires:

```text
validation_result.structural.passed == true
validation_result.quality_gate.passed == true
quality_gate.final_report.teaching_runtime_quality.passed == true
```

If the quality gate fails, the factory must keep `validation_result.passed=false` and return the exact failures and repair actions.

## Round 5 Validation Result Extension

`generation-output.json` may include visual teaching quality through the quality report:

```yaml
validation_result:
  passed: structural.passed && quality_gate.passed
  structural: ...
  quality_gate:
    final_report:
      visual_teaching_quality:
        passed: true
        curve_lessons_detected: true
        diagram_assets_found:
          - assets/diagrams/day3-ad-curve.png
        indexed_png_count: 1
```
