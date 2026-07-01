---
type: Schema
title: Visibility Policy
description: Student-visible and teacher-private content contract for generated course OKFs.
tags: [schema, visibility, teacher]
timestamp: 2026-06-30T00:00:00-07:00
---
# Visibility Policy

```yaml
student_visible_before_answer:
  allowed:
    - question
    - length_limit
    - time_limit
    - output_format
    - note_policy
  forbidden:
    - expected_answer_elements
    - rubric
    - answer_key
    - standard_answer
    - reference_answer
    - teacher_internal_judgment
student_visible_after_answer:
  allowed:
    - missing_points
    - scoring_explanation
    - corrected_wording
    - compact_reference_answer
    - recall_card
    - misconception_repair
teacher_private:
  files:
    - teacher/teacher-notebook.md
    - teacher/rubrics/*.md
    - teacher/answer-keys/*.md
```

# Rule

Guided practice may reveal scaffolds, but the score must be recorded as `assisted_score` or `semi_assisted_score`.
