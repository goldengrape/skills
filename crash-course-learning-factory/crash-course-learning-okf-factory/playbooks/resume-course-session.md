---
type: Playbook
title: Resume Course Session
description: Procedure for resuming a course OKF from saved state.
tags: [playbook, resume, state]
timestamp: 2026-06-30T00:00:00-07:00
---
# Trigger

Use when a learner returns to an existing course OKF.

# Required Reads

Read in this order:

1. `state/current-state.md`
2. `state/next-action.md`
3. `state/topic-ledger.md`
4. `state/recall-deck.md`
5. `state/misconceptions.md`
6. `state/score-history.md`
7. latest file in `sessions/`
8. current or next file in `plan/`

# Decision

Use `next_action` and evidence:

| next_action | Do this |
|---|---|
| `run_day_1` | Start Day 1. |
| `continue` | Start the next planned day only if no blocking A-topic misconception is open. |
| `repair` | Repair misconceptions before new content. |
| `review` | Run retrieval and short-answer consolidation. |
| `simulate` | Run a mock exam or partial mock exam. |
| `final_review` | Generate final-day compressed review. |

# Evidence Override

Even if `next_action` says `continue`, switch to repair or review when:

* a high-severity A-topic misconception is open
* the latest A-topic quiz is below pass-like
* the learner missed two related recall cards
* the last session says a prerequisite was not usable

# Output

Start with a short state recap:

```text
你现在在 Day N；A 类主题中 X 个稳定，Y 个不稳；今天先处理 Z。
```

Then run the session using [Run Daily Session](run-daily-session.md).
