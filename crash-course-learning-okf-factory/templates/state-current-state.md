---
type: Template
title: State Current State
description: Template for generated `state/current-state.md`.
tags: [template, state]
timestamp: 2026-06-30T00:00:00-07:00
---
# Current State Template

````markdown
---
type: Learner State
title: Current State
description: Canonical current state for this course-learning OKF.
tags: [state, learner]
timestamp: {timestamp}
---

# Current State

```yaml
course_name: "{Course Name}"
course_slug: "{course-slug}"
baseline: "zero"
target_score: 60
exam_format: "unknown"
course_type: "concept_heavy"
daily_minutes: 60
days_available_initial: 7
current_day: 1
days_remaining: 7
completed_sessions: 0
pass_readiness: "very_low"
risk_level: "medium"
last_session_date:
next_action: "run_day_1"
active_constraints: []
source_gaps: []
latest_summary: "Course OKF initialized. No learning evidence yet."
```

# Read Rule

This file must be read before every session and updated after every session.
````
