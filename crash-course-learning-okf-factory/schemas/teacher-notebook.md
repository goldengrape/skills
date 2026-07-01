---
type: Schema
title: Teacher Notebook
description: Schema for private teacher-side runtime notes during a course session.
tags: [schema, teacher, notebook, runtime]
timestamp: 2026-06-30T00:00:00-07:00
---
# Teacher Notebook

```yaml
course: string
visibility: teacher_private_runtime_file
time_policy: soft | strict
status: initialized | active | closed
turns:
  - turn_id: string
    phase: explanation | guided_practice | blind_quiz | feedback | interest_branch | state_update
    teacher_says:
      - string # safe to show to learner
    teacher_thinks:
      task_goal: string
      expected_answer_elements: []
      do_not_reveal_before_answer: []
      scoring_rule: string
    engagement_observation:
      interest_level: high | normal | uncertain
      attention_signal: stable | maybe_dropping | unknown
      evidence: []
    teaching_decision:
      action: continue_core | continue_branch | offer_choice | short_check | pause_and_summarize
      reason: string
    state_updates: []
```

# Rule

Do not paste `teacher_thinks`, expected answer elements, answer keys, or scoring rules into the student-visible conversation before the learner answers.
