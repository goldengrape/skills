---
type: Example
title: Management Factory Input
description: Example input for generating a management course OKF.
tags: [example, management]
timestamp: 2026-06-30T00:00:00-07:00
---
# Example Input

```yaml
course_name: "管理学"
baseline: "zero"
exam_date: "2026-07-07"
days_available: 7
daily_minutes: 60
target_score: 60
exam_format: "mixed"
course_type: "social_science"
materials_available: "none"
materials: []
preferences:
  explanation_style: "concise"
  quiz_intensity: "normal"
  answer_language: "zh-CN"
```

# Expected Factory Behavior

Generate `course-okf-management-pass/` with a management course map, source registry, A/B/C priority map, seven-day plan, initialized state, Day 1 work package, Day 1 quiz, pending Day 1 session record, and validation result.
