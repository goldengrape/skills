---
type: Schema
title: Misconception
description: Schema for tracking errors that need repair before moving on.
tags: [schema, state, error-repair]
timestamp: 2026-06-30T00:00:00-07:00
---
# Misconception Entry

```yaml
- id: string
  topic_id: string
  error_statement: string
  observed_in: string
  severity: low | medium | high
  repair_status: open | explained | retested | resolved
  repair_prompt: string
  correct_distinction: string
```

# Rules

* A high-severity misconception about an A-topic should trigger `next_action: repair`.
* Do not mark a misconception resolved merely because the correct answer was shown.
* Mark resolved only after the learner uses the idea correctly in a new answer.
