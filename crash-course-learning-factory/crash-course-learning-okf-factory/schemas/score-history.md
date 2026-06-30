---
type: Schema
title: Score History
description: Schema for recording estimated performance over time.
tags: [schema, state, score-history]
timestamp: 2026-06-30T00:00:00-07:00
---
# Score History

```yaml
assessments:
  - date: date
    session_id: string
    task_type: recall | feynman | term_definition | short_answer | essay_outline | mixed_quiz | mock_exam
    topic_ids: []
    estimated_points: number
    possible_points: number
    pass_level_interpretation: below_pass | borderline | pass_like | strong
    gained_points: []
    lost_points: []
    missing_points: []
    next_action: continue | repair | review | simulate | final_review
```

# Rules

* Estimated points are learning signals, not guaranteed exam predictions.
* Every quiz, mock exam, Feynman task, or exam-style answer review should create one assessment entry.
* If two consecutive entries for an A-topic are below pass-like, set `next_action: repair` or `review`.
