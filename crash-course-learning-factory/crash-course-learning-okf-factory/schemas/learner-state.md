---
type: Schema
title: Learner State
description: Canonical learner-state schema for generated course OKFs.
tags: [schema, state, learner]
timestamp: 2026-06-30T00:00:00-07:00
---
# Canonical State

`state/current-state.md` stores the learner's current position.

```yaml
course_name: string
course_slug: string
baseline: zero | weak | partial | review
target_score: integer | pass | stable_pass | high_score
exam_format: string
course_type: string
daily_minutes: integer
days_available_initial: integer
current_day: integer
days_remaining: integer
completed_sessions: integer
pass_readiness: very_low | low | unstable | plausible | stable
risk_level: low | medium | high
last_session_date: date
next_action: run_day_1 | continue | repair | review | simulate | final_review
active_constraints: []
source_gaps: []
latest_summary: string
```

# Interpretation

* `pass_readiness` is not a real exam prediction. It is a coarse learning-status label.
* `next_action` tells the agent what to do next.
* `risk_level` determines whether future plan days should be rewritten.
* `source_gaps` lists missing syllabus, past-exam, teacher-hint, or textbook information that limits confidence.

# Update Rule

This file must be read before and updated after every learning session.
