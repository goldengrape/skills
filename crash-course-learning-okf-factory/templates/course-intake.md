---
type: Template
title: Course Intake
description: User-facing intake template for generating a course OKF.
tags: [template, input]
timestamp: 2026-06-30T00:00:00-07:00
---
# Course Intake

```yaml
course_name:
baseline: zero
exam_date:
days_available: 7
daily_minutes: 60
target_score: pass
exam_format: unknown
materials: []
school_or_department:
teacher_style:
must_include_topics: []
must_avoid_topics: []
preferences:
  explanation_style: concise
  quiz_intensity: normal
  answer_language: zh-CN
```

# Notes

If the learner only gives a course name and says they are zero-base, generate with defaults and record assumptions in `mission.md`.
