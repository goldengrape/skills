---
type: Playbook
title: Handle Interest-Led Branch
description: Decide how to respond when the learner asks a deeper question or shows strong interest.
tags: [playbook, interest, time-policy]
timestamp: 2026-06-30T00:00:00-07:00
---
# Handle Interest-Led Branch

## Default

Treat learner-led questions as useful learning evidence, not as a problem.

## Procedure

1. Classify the branch:
   - `core_blocker`: needed to understand the current A-topic.
   - `useful_extension`: not strictly required, but deepens understanding.
   - `interest_extension`: interesting but low exam value.
2. Check `time_policy`:
   - `soft`: continue when it supports understanding or motivation.
   - `strict`: answer briefly, record it, and return to the planned task.
3. Connect the branch back to the exam spine when possible.
4. Record it in `state/interest-ledger.md`.
5. If it changes the next session, update `state/next-action.md` or `state/plan-changes.md`.

## Guard

Do not force a hard stop merely because the session exceeds `daily_minutes`. Only enforce a hard limit when the learner requested strict time control or `time_policy: strict` is set.
