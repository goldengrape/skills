---
type: Template
title: Daily Work Package
description: Template for one daily learning package.
tags: [template, daily-session]
timestamp: 2026-06-30T00:00:00-07:00
---
# Daily Work Package Template

````markdown
---
type: Daily Work Package
title: Day {N}: {Focus}
description: One-hour learning package for {Course Name}.
tags: [daily-work-package, day-{N}]
timestamp: {timestamp}
---

# Today’s Goal

By the end, the learner should be able to...

# Why This Matters for the Exam

...

# Time Budget

```yaml
total_minutes: {daily_minutes}
new_A_topics_limit: 3
```

# 0-5 min — Retrieval

Ask without notes:

1.
2.
3.

# 5-10 min — Map

Explain today's position in the course.

# 10-25 min — Core Explanation

Keep to the minimum needed for exam answers. Include examples, counterexamples, and common confusions.

# 25-35 min — Feynman Task

Prompt:

```text
用自己的话向完全没学过的人解释……
```

# 35-45 min — Exam Practice

Question:

Expected scoring points:

# 45-55 min — Feedback

Use [Answer Feedback](../templates/answer-feedback.md).

# 55-60 min — State Update

Update state and write next action.
````
