---
type: Playbook
title: Adapt Remaining Plan
description: Procedure for changing future daily work packages based on learner evidence.
tags: [playbook, adaptation, plan]
timestamp: 2026-06-30T00:00:00-07:00
---
# Trigger Conditions

Run when:

* pass readiness drops to `low` or `very_low`
* an A-topic has mastery below 2 after practice
* a misconception remains open after repair
* the learner misses two related recall cards
* daily time changes
* exam format becomes clearer
* mock exam score is below pass-level threshold

# Adaptation Moves

| Problem | Change |
|---|---|
| Too many weak A-topics | Collapse B/C topics and add repair time. |
| Definitions known but answers weak | Add answer-template practice. |
| Good short answers but poor comparison | Add contrast drills. |
| Recall poor | Add more retrieval and fewer new topics. |
| Exam soon | Convert remaining sessions to review and mock questions. |
| Strong Day 1/2 performance | Preserve A-topics and add only high-value B-topic practice. |

# Required Output

Append a plan-change entry to:

```text
state/plan-changes.md
```

Then revise future `plan/day-N.md` and affected `quizzes/day-N-quiz.md` files.

# Rule

Plan changes must cite evidence: session record, quiz result, misconception entry, recall card miss, or changed user constraint.
