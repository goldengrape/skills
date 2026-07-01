---
type: Schema
title: Topic Ledger
description: Per-topic tracking schema for priority, mastery, evidence, and next practice.
tags: [schema, state, topic]
timestamp: 2026-06-30T00:00:00-07:00
---
# Topic Entry

```yaml
- id: string
  title: string
  priority: A | B | C
  exam_value: high | medium | low
  status: unseen | introduced | practiced | shaky | usable | stable | deferred
  mastery_estimate: 0-4
  common_question_types: []
  evidence:
    - date: date
      source: session | quiz | feynman | short_answer
      result: correct | partial | missed | confused
      note: string
  next_practice: string
```

# Mastery Scale

| Value | Meaning |
|---:|---|
| 0 | unseen |
| 1 | recognized but cannot explain |
| 2 | can define but weak on use or comparison |
| 3 | can answer ordinary exam questions |
| 4 | stable enough for pass-level exam use |

# Rule

A-topic entries cannot remain `unseen` after Day 4 unless the plan explicitly records why.
