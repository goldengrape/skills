---
type: Template
title: State Next Action
description: Template for generated `state/next-action.md`.
tags: [template, state, next-action]
timestamp: 2026-06-30T00:00:00-07:00
---
# Next Action Template

````markdown
---
type: Next Action
title: Next Action
description: The next step the session agent should run.
tags: [state, next-action]
timestamp: {timestamp}
---

# Next Action

```yaml
next_action: run_day_1
reason: "Course OKF has been initialized and no session has been completed."
priority_focus: []
read_before_running:
  - state/current-state.md
  - state/topic-ledger.md
  - state/recall-deck.md
  - state/misconceptions.md
  - state/score-history.md
  - plan/day-1.md
write_after_running:
  - sessions/day-1-session.md
  - state/current-state.md
  - state/topic-ledger.md
  - state/recall-deck.md
  - state/misconceptions.md
  - state/score-history.md
  - state/next-action.md
```
````
