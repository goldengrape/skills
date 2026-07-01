---
type: Schema
title: Recall Card
description: Retrieval-practice card schema used by generated course OKFs.
tags: [schema, state, retrieval]
timestamp: 2026-06-30T00:00:00-07:00
---
# Recall Card

```yaml
- id: string
  topic_id: string
  prompt: string
  expected_answer_points: []
  due_on: string
  interval: same_day | next_day | plus_2_days | final_day
  status: new | due | answered | missed | retired
  last_result: correct | partial | missed | not_tested
  attempts: integer
```

# Rules

* Cards should ask for active recall, not recognition.
* Keep prompts short.
* Expected answer points should be scoring cues, not long textbook answers.
* Missed cards become due again next session.
