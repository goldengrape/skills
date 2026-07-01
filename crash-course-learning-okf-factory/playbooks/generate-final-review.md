---
type: Playbook
title: Generate Final Review
description: Procedure for producing final-day compressed notes and mock exam materials.
tags: [playbook, final-review]
timestamp: 2026-06-30T00:00:00-07:00
---
# Trigger

Use on the final day or when `next_action: final_review`.

# Inputs

Read:

* `priority-map.md`
* `state/topic-ledger.md`
* `state/misconceptions.md`
* `state/score-history.md`
* all session summaries

# Outputs

Create or update:

```text
final-review/compressed-notes.md
final-review/must-know-list.md
final-review/answer-templates.md
final-review/mock-exam.md
```

# Rules

* Prioritize A-topics with low or unstable mastery.
* Include exact answer structures for likely exam formats.
* Include a final recall list.
* Do not add low-value new material unless it is required to repair a core misconception.
