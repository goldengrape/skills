---
type: Learner State
title: Current State
description: Fresh learner state for a new 7-day run.
tags: [state, learner]
---

# Current State

```yaml
course_name: "7 天速通神经内科定位诊断"
course_slug: "neuro-localization-7day-course-package"
baseline: unknown_or_low
use_case: medical_student_exam_review
exam_format: mixed
course_type: case_reasoning
daily_minutes: 60
days_available_initial: 7
current_day: 1
days_remaining: 7
completed_sessions: 0
state_data_status: fresh_template_no_real_learner_data
pass_readiness: unknown
risk_level: unknown
next_action: read_mission_then_start_day_1
active_constraints:
  - open-authoritative-online-sources-only
  - no-school-specific-materials
```

# Update Rule

After each session, update:

1. `state/score-history.md`
2. `state/misconceptions.md`
3. `state/next-action.md`
4. `state/recall-deck.md`

Do not treat this template as evidence of learning. It becomes useful only after real learner answers are recorded.
