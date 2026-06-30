---
type: Template
title: Daily Quiz
description: Template for day-N quiz files in generated Course Learning OKFs.
tags: [template, quiz, assessment]
timestamp: 2026-06-30T00:00:00-07:00
---
# Daily Quiz Template

````markdown
---
type: Quiz
title: Day {N} Quiz
description: Short exam-oriented check for Day {N}.
tags: [quiz, day-{N}]
timestamp: {timestamp}
---

# Day {N} Quiz

## Retrieval

1.
2.
3.

## Exam-Style Question

Question:

Expected scoring points:

## Pass-Level Check

```yaml
possible_points:
pass_like_threshold:
A_topics_checked: []
```

## State Update

After scoring, update `state/score-history.md`, `state/topic-ledger.md`, `state/recall-deck.md`, `state/misconceptions.md`, and `state/next-action.md`.
````
