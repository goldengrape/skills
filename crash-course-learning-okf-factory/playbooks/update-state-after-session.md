---
type: Playbook
title: Update State After Session
description: Protocol for persisting learner progress after each session.
tags: [playbook, state, memory]
timestamp: 2026-06-30T00:00:00-07:00
---
# Trigger

Run after every learning session, quiz, mock exam, or substantial answer review.

# Required Updates

## 1. Create Session Record

Create or update:

```text
sessions/day-N-session.md
```

Use [Session Record](../schemas/session-record.md).

## 2. Update Current State

Update:

```text
state/current-state.md
```

Fields commonly changed:

* `current_day`
* `days_remaining`
* `completed_sessions`
* `pass_readiness`
* `risk_level`
* `last_session_date`
* `next_action`
* `source_gaps`
* `latest_summary`

## 3. Update Topic Ledger

For each topic practiced, update status, mastery estimate, and evidence.

## 4. Update Recall Deck

Add cards for:

* newly introduced A-topics
* missed quiz items
* weak definitions
* important comparisons
* expected short-answer structures

## 5. Update Misconceptions

Open, revise, retest, or resolve misconceptions based on evidence.

## 6. Update Score History

Add an assessment event for every meaningful task. Use [Score History](../schemas/score-history.md) and [Assessment Event](../schemas/assessment-event.md).

## 7. Write Next Action

Update:

```text
state/next-action.md
```

Choose `repair`, `review`, `simulate`, or `final_review` when evidence requires it. Do not default to `continue` mechanically.

## 8. Adapt Remaining Plan

If risk triggers appear, run [Adapt Remaining Plan](adapt-remaining-plan.md) and append a record to `state/plan-changes.md`.

# Completion Checklist

- [ ] Session record created or updated.
- [ ] Current state updated.
- [ ] Topic ledger updated for practiced topics.
- [ ] Recall deck updated for missed/high-value items.
- [ ] Misconceptions updated.
- [ ] Score history updated.
- [ ] Next action written.
- [ ] Plan changes recorded when future days were revised.

# Rule

A session is not complete until the next action is written.
