---
type: Schema
title: Assessment Event
description: Schema for recording quiz, short-answer, and Feynman-task performance.
tags: [schema, assessment, feedback]
timestamp: 2026-06-30T00:00:00-07:00
---
# Assessment Event

```yaml
- date: date
  session_id: string
  task_type: recall | feynman | short_answer | essay_outline | mixed_quiz | mock_exam
  topic_ids: []
  raw_answer_summary: string
  estimated_points: number
  possible_points: number
  scoring_notes:
    gained: []
    lost: []
    missing: []
  action:
    continue | repair | add_recall_card | revise_plan
```

# Scoring Rule

Feedback must separate:

* valid scoring points
* inaccurate statements
* missing required points
* fluent but non-scoring filler
* one concrete revision that would improve the answer
