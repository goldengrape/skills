---
type: Playbook
title: Finalize Session Record
description: Convert teacher notebook and session evidence into public learning records and state updates.
tags: [playbook, session, state]
timestamp: 2026-06-30T00:00:00-07:00
---
# Finalize Session Record

## Procedure

1. Read `teacher/teacher-notebook.md`.
2. Read the session transcript or `sessions/day-N-session.md`.
3. Summarize only learner-safe content into `learning-records/day-N-learning-record.md`.
4. Preserve hidden scoring logic in `teacher/` files.
5. Update:
   - `state/current-state.md`
   - `state/topic-ledger.md`
   - `state/recall-deck.md`
   - `state/misconceptions.md`
   - `state/score-history.md`
   - `state/interest-ledger.md`
   - `state/next-action.md`

## Rule

Learning records are public recovery artifacts. They may include what the learner missed after feedback, but they should not expose future hidden answer keys.
