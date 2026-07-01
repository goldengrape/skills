---
type: Template
title: Daily Work Package
description: Template for one daily learning package with teacher/student visibility split.
tags: [template, daily-session, visibility]
timestamp: 2026-06-30T00:00:00-07:00
---
# Daily Work Package Template

````markdown
---
type: Daily Work Package
title: Day {N}: {Focus}
description: Learning package for {Course Name}.
tags: [daily-work-package, day-{N}]
timestamp: {timestamp}
---

# Today’s Goal

By the end, the learner should be able to...

# Why This Matters for the Exam

...

# Time Policy

```yaml
total_minutes: {daily_minutes}
time_policy: {soft_or_strict}
new_A_topics_limit: 3
```

`daily_minutes` is a planning target under `time_policy: soft`. Learner-led deeper questions may continue when they support understanding or interest. Enforce a hard limit only under `time_policy: strict` or when the learner asks for strict time control.

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

Student-visible prompt:

```text
用自己的话向完全没学过的人解释……
```

Teacher-private note:

```text
Write expected answer elements to teacher/teacher-notebook.md before asking. Do not show them before the learner answers.
```

# 35-45 min — Exam Practice

Student-visible question:

```text
{question only}
```

Private scoring material:

```text
teacher/rubrics/day-{N}-rubric.md
teacher/answer-keys/day-{N}-answer-key.md
```

# 45-55 min — Feedback

Use [Answer Feedback](../templates/answer-feedback.md) after the learner answers.

# 55-60 min — State Update

Update state, teacher notebook, interest ledger, score history, and next action.
````
