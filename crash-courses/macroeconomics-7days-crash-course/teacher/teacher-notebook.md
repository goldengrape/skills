---
type: Teacher Notebook
title: Teacher Notebook
description: 教师侧追加式运行记录，用于隐藏目标、评分规则和教学判断；已同步 Day 1-3 进度并按 round5 加入视觉教学层。
tags: [teacher, notebook, private-runtime, round5]
timestamp: 2026-07-03T00:00:00-07:00
---

# Teacher Notebook

```yaml
course: 宏观经济学
visibility: teacher_private_runtime_file
time_policy: soft
status: updated_to_factory_round5
current_day: 4
completed_sessions: 3
```

## Runtime Rule

作答前不展示评分细则、参考答案、预期要点或教师侧判断。作答后再用这些材料评分、修正和更新状态。

## Imported Detailed Notebooks

- Day 2 detailed notebook: `teacher/day-2-teacher-notebook.md`
- Day 3 detailed notebook: `teacher/day-3-teacher-notebook.md`

## Append-Only Turn Log

Use this structure for each teaching turn:

```yaml
turn_id: dayN-tXX
phase: explanation | guided_practice | blind_quiz | feedback | interest_branch | state_update | visual_teaching
teacher_says:
  - "student-visible message"
teacher_thinks:
  task_goal: "hidden teaching goal"
  expected_answer_elements: []
  do_not_reveal_before_answer: []
  scoring_rule: "hidden until after answer"
engagement_observation:
  interest_level: high | normal | uncertain
  attention_signal: stable | maybe_dropping | unknown
  evidence: []
teaching_decision:
  action: continue_core | continue_branch | offer_choice | short_check | pause_and_summarize
  reason: ""
state_updates: []
diagram_assets_used: []
```

## Progress Import Summary

```yaml
turn_id: round5-progress-import
phase: state_update
teacher_says:
  - "Day 1-3 已完成，下一步进入 Day 4。"
teacher_thinks:
  task_goal: "preserve learner evidence while upgrading the course OKF to factory round5"
  expected_answer_elements:
    - "Day 1: GDP, final goods, nominal vs real GDP, GDP deflator, inventory investment"
    - "Day 2: CPI, inflation, unemployment, labor force, discouraged workers, unemployment types"
    - "Day 3: AD, SRAS, LRAS, output gaps, short-run equilibrium, long-run SRAS adjustment"
  do_not_reveal_before_answer:
    - "rubrics"
    - "answer keys"
    - "expected answer elements"
  scoring_rule: "Use blind_score only when the learner answered before seeing answer elements."
engagement_observation:
  interest_level: high
  attention_signal: stable
  evidence:
    - "learner asked extended questions about chained CPI and macro data effects on tech stocks"
    - "learner requested stable generated diagrams instead of complex ASCII diagrams"
teaching_decision:
  action: continue_core
  reason: "Day 3 integrated practice reached 79/95; continue to Day 4 after light repair."
state_updates:
  - "current_day set to 4"
  - "completed_sessions set to 3"
  - "visual teaching policy and diagram index added"
```

## Day 4 Start Watch Points

1. AD 右移时，短期 `Y` 和 `P` 都上升。
2. 负向供给冲击后若 `Y < Y*`，长期自我调整通常来自工资/成本压力下降，使 SRAS 右移；不是 AD 自动右移。
3. 劳动参与率 = 劳动力 / 成年人口；就业人数 / 成年人口 是就业人口比率。
