---
type: Schema
title: Course OKF Quality Report
description: Schema for post-generation content quality evaluation of a Course Learning OKF.
tags: [schema, quality, validation, repair]
timestamp: 2026-06-30T00:00:00-07:00
---
# Course OKF Quality Report

This report is separate from structural validation. Structural validation answers: **do the files exist?** Quality validation answers: **can the learner actually start using this course OKF for the target exam?**

```yaml
passed: boolean
score: integer # 0-100
threshold: 75
course_name: string
known_course_seed_terms: boolean
found_course_terms:
  - string
term_count: integer
placeholder_files:
  relative/path.md:
    - matched_placeholder_pattern
failures:
  - code: missing_required_quality_file | placeholder_content | insufficient_course_specific_terms | abc_priority_missing | priority_too_thin | day1_not_runnable | quiz_missing_exam_items | mock_exam_not_exam_like | next_action_unparseable | score_history_unusable
    path: string
    message: string
warnings:
  - code: string
    path: string
    message: string
repair_actions:
  - string
quality_dimensions:
  structure_presence: checked
  placeholder_absence: checked
  course_specificity: checked_with_seed_terms | needs_manual_or_ai_review
  exam_readiness: checked
  recoverability: checked
  teaching_runtime_quality:
    prompt_visibility: checked
    teacher_notebook: checked
    score_type: checked
    time_policy: checked
    interest_and_engagement: checked
teaching_runtime_quality:
  passed: boolean
  failures: []
  warnings: []
```

# Hard Gates

The generated course OKF cannot be marked return-ready when any of these gates fails:

| Gate | Failure code |
|---|---|
| Required quality-critical file missing | `missing_required_quality_file` |
| Placeholder remains in critical learning file | `placeholder_content` |
| Known course lacks enough visible course terms | `insufficient_course_specific_terms` |
| Day 1 is not directly runnable | `day1_not_runnable` |
| Day 1 quiz lacks exam-style items | `quiz_missing_exam_items` |
| Mock exam is not scored or exam-like | `mock_exam_not_exam_like` |
| Teaching runtime file missing | `missing_teaching_runtime_file` |
| Student prompt leaks answer elements | `prompt_visibility_leak` |
| Teacher notebook schema missing | `teacher_notebook_schema_missing` |
| Score type or prompt visibility missing | `score_type_missing`, `prompt_visibility_field_missing` |
| Soft/strict time policy missing | `time_policy_missing_soft_strict` |

# Critical Files

The content gate must inspect at least:

```text
course-map.md
priority-map.md
glossary.md
plan/seven-day-plan.md
plan/day-1.md
quizzes/day-1-quiz.md
final-review/must-know-list.md
final-review/mock-exam.md
state/current-state.md
state/next-action.md
state/score-history.md
state/interest-ledger.md
teacher/teacher-notebook.md
teacher/visibility-rules.md
teacher/time-policy.md
```

# Rule

`validation_result.passed` is true only when structural validation, content quality, and teaching runtime quality pass.

## Round 7 Compact Learning Control Quality

```yaml
learning_control_quality:
  passed: boolean
  learning_contract_present: boolean
  default_core_target: L6 | other | unknown
  assistance_modes_checked: boolean
  productive_friction_policy_present: boolean
  barehand_checkpoints_present: boolean
  failures: []
  warnings: []
```

Hard failures include missing compact learning contract, missing L1-L9 stages, missing assistance modes, missing L6 misuse checks, missing feedback/source anchor, missing model-vs-reality distinction, missing negative-feature list, or unsupported mastery claims.
