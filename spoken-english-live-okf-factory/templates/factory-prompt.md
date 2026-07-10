---
type: Template
title: Factory Prompt
description: Copyable prompt for generating an interest-aware spoken-English Live cycle.
tags: [template, factory, prompt, adaptive-topics]
timestamp: 2026-07-09T20:15:00-07:00
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
- topic policy: guided_adaptive
- planned/adaptive topic ratio: approximately 60/40
- interest discovery: enabled, using explicit or repeated evidence
- current events: disabled unless I enable them

If current events are enabled:
- use them only in optional adaptive slots;
- verify facts at session time;
- respect preferred and excluded categories;
- provide an evergreen fallback;
- keep background explanation short and speaking-first.

Keep no more than three primary language targets. Topics are practice vehicles, not additional targets. Generate Markdown only. Do not run or require Python, hooks, a virtual machine, hidden state, or automatic GitHub writes.

Return:
1. Cycle Evidence Snapshot
2. Cycle Blueprint
3. complete file tree and Markdown contents
4. Validation Report

Do not claim files were saved or committed.
```
