---
type: Schema
title: Plan Change
description: Schema for recording changes to the remaining plan.
tags: [schema, plan, adaptation]
timestamp: 2026-06-30T00:00:00-07:00
---
# Plan Change

```yaml
- date: date
  reason: string
  evidence: string
  changed_files: []
  old_plan_summary: string
  new_plan_summary: string
  risk_level_after_change: low | medium | high
```

# Trigger Conditions

Create a plan change when:

* an A-topic remains below mastery 2 after practice
* the learner misses two consecutive recall cards for the same concept
* a misconception blocks later topics
* mock exam score is below pass threshold
* user changes constraints or target
