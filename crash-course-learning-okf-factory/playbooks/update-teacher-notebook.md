---
type: Playbook
title: Update Teacher Notebook
description: Append private teacher-side runtime notes during a daily session.
tags: [playbook, teacher, notebook]
timestamp: 2026-06-30T00:00:00-07:00
---
# Update Teacher Notebook

## Procedure

For each significant teaching turn, append:

```yaml
turn_id: dayN-tXX
phase: explanation | guided_practice | blind_quiz | feedback | interest_branch | state_update
teacher_says:
  - student-visible text
teacher_thinks:
  task_goal: hidden goal
  expected_answer_elements: []
  do_not_reveal_before_answer: []
  scoring_rule: hidden rule
engagement_observation:
  interest_level: high | normal | uncertain
  attention_signal: stable | maybe_dropping | unknown
  evidence: []
teaching_decision:
  action: continue_core | continue_branch | offer_choice | short_check | pause_and_summarize
  reason: string
state_updates: []
```

## Rule

The notebook is a runtime file. The assistant may tell the learner that it was updated, but should not paste `teacher_thinks` content into the conversation before the learner answers.
