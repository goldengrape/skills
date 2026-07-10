---
type: Template
title: Factory Prompt
description: Copyable prompt for generating the next spoken-English Live cycle.
tags: [template, factory, prompt]
timestamp: 2026-07-09T18:10:00-07:00
---

# Factory Prompt

```text
Read this Spoken English Live OKF Factory in its documented order.

Generate the next learner-specific course cycle by executing:
1. DP-001 Cycle Evidence Contract.
2. DP-002 Derive Cycle Blueprint.
3. DP-003 Materialize Cycle Pack.
4. DP-007 Validate Cycle Pack.

Use previous session records and cycle reviews when supplied. Do not rely on unstated memory.

Defaults unless I override them:
- cycle_days: 7
- daily_minutes: 15
- session_mode: ChatGPT Live
- target English: clear global English
- correction style: brief live micro-corrections plus repair at natural pauses

Keep no more than three primary cycle targets. Generate Markdown only. Do not run or require Python, hooks, a virtual machine, or hidden state.

Return the complete course-pack files followed by a validation report. Do not claim files were saved or committed.
```
