---
type: State Protocol
title: Reset Protocol for Real Learner Use
description: How to reset package dry-run state before using the course with a real student.
tags: [state, protocol, v3]
timestamp: 2026-07-07T10:05:00-07:00
---

# Reset Protocol for Real Learner Use

The course package includes one marked dry-run state transition to prove that the state mechanism can route an error to a retest. It is not real learner evidence.

Before starting with a real student:

1. Archive current `state/*.md` files if quality evidence must be preserved.
2. Reset `state/score-history.md` to `assessments: []`.
3. Reset `completed_sessions: 0`, `last_session_date: null`, and `next_action: run_day_1` in `state/current-state.md`.
4. Keep `assessment/retest-bank.md`; it is reusable.
5. During actual teaching, update state only after student answers.
