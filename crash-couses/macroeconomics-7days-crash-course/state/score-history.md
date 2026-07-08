---
type: State
title: Score History
description: 每日测验、分数类型、题目可见性与 readiness 记录。
tags: [state, score-history, round5]
timestamp: 2026-07-03T00:00:00-07:00
---

# Score History

| Date | Day | Quiz / Practice topic | Score | Score type | Prompt visibility | Hints shown before answer | Pass readiness after quiz/practice | Evidence | Next action |
|---|---:|---|---:|---|---|---|---|---|---|
| 2026-06-30 | 0 | initial baseline | null | diagnostic | n/a | n/a | very_low | 0 基础，未开始 | run_day_1 |
| 2026-06-30 | 1 | GDP 与国民收入核算 | 38 / 40 | blind_score | student_prompt_only | no | current_topic_stable; overall_improving | GDP、最终产品、支出法、nominal/real GDP、GDP deflator 稳定 | run_day_2 |
| 2026-07-01 | 2 | CPI、通胀率与失业率 | 45.5 / 50 | blind_score | student_prompt_only | no | continue | CPI、失业率、灰心工人、三类失业稳定；劳动参与率需轻复习 | run_day_3 |
| 2026-07-02 | 3 | AD-AS 综合练习 | 79 / 95 | blind_score | student_prompt_only_no_answer_hints | no | continue_with_light_repair | AD/SRAS/LRAS、产出缺口和长期调整基本稳定；AD 右移价格结果、供给冲击长期调整需修复 | run_day_4 |

## 记录规则

每次 quiz 或综合练习后增加一行。必须记录 `Score type` 和 `Prompt visibility`。如果作答前给了具体内容提示，不能把结果记作 `blind_score`。低于 60% 时必须在 `state/plan-changes.md` 记录补救动作。
