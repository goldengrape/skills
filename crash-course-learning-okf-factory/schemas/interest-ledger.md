---
type: Schema
title: Interest Ledger
description: State schema for learner-led questions and interest-driven branches.
tags: [schema, state, interest]
timestamp: 2026-06-30T00:00:00-07:00
---
# Interest Ledger

```yaml
branches:
  - date: date
    branch_id: string
    trigger: student_question | student_example | student_requested_exercise | teacher_choice
    topic: string
    relation_to_exam: core_blocker | useful_extension | interest_extension
    interest_evidence: []
    teacher_decision: continue_branch | brief_answer_then_return | defer_to_later | offer_choice
    time_policy: soft | strict
    impact_on_plan:
      main_goal_completed: boolean
      extra_completed: []
      next_session_recall: []
```

# Rule

Learner-led questions are not a failure by default. In `soft` mode, they may continue when they deepen understanding or maintain interest. In `strict` mode, they are answered briefly and recorded for later.
