---
type: Template
title: Course Instance Root Index
description: Template for the root index of a generated Course Learning OKF.
tags: [template, course-instance]
timestamp: 2026-06-30T00:00:00-07:00
---
# Template

```markdown
---
okf_version: "0.1"
bundle: course-okf-{course-slug}
title: {Course Name} Crash Course OKF
description: Stateful one-hour-per-day learning OKF for pass-level exam preparation.
timestamp: {timestamp}
---

# {Course Name} Crash Course OKF

This bundle stores the learning plan, course materials, learner state, session records, and final review materials for {Course Name}.

# Start

* [Mission](mission.md)
* [Course Map](course-map.md)
* [Priority Map](priority-map.md)
* [Seven-Day Plan](plan/seven-day-plan.md)
* [Current State](state/current-state.md)
* [Next Action](state/next-action.md)

# Resume Rule

Before continuing, read `state/current-state.md`, `state/next-action.md`, due recall cards, unresolved misconceptions, and the latest session record.
```
