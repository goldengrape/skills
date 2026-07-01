---
type: Schema
title: Next Action
description: Schema for the next step instruction in a generated course OKF.
tags: [schema, state, next-action]
timestamp: 2026-06-30T00:00:00-07:00
---
# Next Action

```yaml
next_action: run_day_1 | continue | repair | review | simulate | final_review
reason: string
priority_focus:
  - topic_id: string
    reason: string
read_before_running:
  - state/current-state.md
  - state/topic-ledger.md
  - state/recall-deck.md
  - state/misconceptions.md
  - state/score-history.md
  - latest sessions/*.md
  - relevant plan/day-N.md
write_after_running:
  - sessions/day-N-session.md
  - state/current-state.md
  - state/topic-ledger.md
  - state/recall-deck.md
  - state/misconceptions.md
  - state/score-history.md
  - state/next-action.md
```

# Decision Rule

The next action must be chosen from evidence. Do not choose `continue` when a high-severity A-topic misconception remains open or the latest assessment is below pass-like.
