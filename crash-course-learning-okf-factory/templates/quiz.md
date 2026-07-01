---
type: Template
title: Daily Quiz
description: Template for day-N quiz files in generated Course Learning OKFs.
tags: [template, quiz, assessment, visibility]
timestamp: 2026-06-30T00:00:00-07:00
---
# Daily Quiz Template

````markdown
---
type: Quiz
title: Day {N} Quiz
description: Short exam-oriented check for Day {N}; student prompt only.
tags: [quiz, day-{N}, student-visible]
timestamp: {timestamp}
---

# Day {N} Quiz

```yaml
visibility: student_prompt
assessment_mode: blind_quiz
score_type_if_unprompted: blind_score
private_teacher_files:
  - teacher/rubrics/day-{N}-rubric.md
  - teacher/answer-keys/day-{N}-answer-key.md
```

## Retrieval

1.
2.
3.

## Exam-Style Question

Question only:

```text
{student-facing question}
```

Do not include hidden answer elements in this file. Put them in the private teacher files.

## Pass-Level Check

```yaml
possible_points:
pass_like_threshold:
A_topics_checked: []
prompt_visibility: hidden_until_answer
```

## State Update

After scoring, update `state/score-history.md`, `state/topic-ledger.md`, `state/recall-deck.md`, `state/misconceptions.md`, `state/interest-ledger.md`, `teacher/teacher-notebook.md`, and `state/next-action.md`.
````
