---
type: Playbook
title: Run Daily Session
description: Procedure for conducting one one-hour course-learning session.
tags: [playbook, session]
timestamp: 2026-06-30T00:00:00-07:00
---
# Trigger

Use when the learner starts a daily course session.

# Before Teaching

Read:

1. `state/current-state.md`
2. `state/next-action.md`
3. `state/topic-ledger.md`
4. `state/recall-deck.md`
5. `state/misconceptions.md`
6. `state/score-history.md`
7. latest session record
8. relevant day plan

# One-Hour Structure

| Minutes | Activity |
|---:|---|
| 0-5 | Due recall cards and previous-day retrieval |
| 5-10 | Explain today's goal and exam value |
| 10-25 | Core explanation with examples, counterexamples, and contrasts |
| 25-35 | Feynman task by the learner |
| 35-45 | Exam-style question practice |
| 45-55 | Feedback and repair |
| 55-60 | Write state-update summary |

# Time-Box Rules

* Default: introduce no more than 3 new A-topics in one day.
* If recall fails badly, shorten new teaching and repair first.
* If the learner gives a strong answer, increase challenge slightly rather than adding many new topics.
* If the session exceeds the time budget, move lower-priority material to B/C or a future day.
* Do not end without identifying the next action.


## Teacher Runtime Protocol

Before each assessment prompt:

1. Append hidden goal and expected answer elements to `teacher/teacher-notebook.md`.
2. Render only the student-visible prompt.
3. After the learner answers, show feedback and record `score_type` plus `prompt_visibility`.

## Interest and Time Policy

`daily_minutes` is a planning target under `time_policy: soft`. If the learner asks a useful deeper question, continue when it supports understanding or interest and record it in `state/interest-ledger.md`. Enforce a hard time limit only under `time_policy: strict` or when the learner explicitly asks for strict time control.

## Engagement Handling

Use observable signals only. If interest is high, connect the branch back to the exam spine. If attention may be dropping, shorten the explanation, offer a small question, give a choice, or summarize and pause.
