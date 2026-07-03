---
type: Template
title: Master Factory Prompt
description: Copyable prompt for invoking the factory with an AI agent.
tags: [template, prompt, factory]
timestamp: 2026-06-30T00:00:00-07:00
---
# Master Factory Prompt

```text
请使用“Crash Course Learning OKF Factory”为我生成一门课程的状态化学习 OKF。

输入信息：

课程名：
我的基础：零基础 / 很弱 / 学过但忘了 / 复习
考试日期：
可用天数：默认 7 天
每天可用时间：默认 1 小时
时间策略：默认 soft；如果我明确要求严格控制时间，则 strict
考试形式：未知 / 闭卷 / 开卷 / 选择题 / 名词解释 / 简答 / 论述 / 混合
课程类型：概念密集 / 理论密集 / 社科 / 人文 / 法学概论 / 混合 / 其他
目标：60 分及格优先
教材、课件、老师重点或往年题：没有 / 我会上传 / 如下
其他约束：

请按以下要求生成：

1. 先把输入规范化为 Factory Input。
2. 查询或读取资料，完成课程侦察；优先使用我提供的资料。
3. 生成一个新的 Course Learning OKF，而不是只给我学习计划。
4. 该课程 OKF 必须包含：
   - mission.md
   - course-map.md
   - resources.md
   - priority-map.md
   - plan/seven-day-plan.md
   - plan/day-1.md 到 plan/day-N.md
   - state/current-state.md
   - state/topic-ledger.md
   - state/recall-deck.md
   - state/misconceptions.md
   - state/score-history.md
   - state/next-action.md
   - state/plan-changes.md
   - state/interest-ledger.md
   - sessions/day-1-session.md
   - learning-records/0001-initial-baseline.md
   - quizzes/day-1-quiz.md 到 quizzes/day-N-quiz.md
   - final-review/compressed-notes.md
   - final-review/must-know-list.md
   - final-review/answer-templates.md
   - final-review/mock-exam.md
   - teacher/teacher-notebook.md
   - teacher/visibility-rules.md
   - teacher/teaching-protocol.md
   - teacher/engagement-monitor.md
   - teacher/engagement-intervention-rules.md
   - teacher/time-policy.md
   - teacher/rubrics/day-N-rubric.md
   - teacher/answer-keys/day-N-answer-key.md
5. 每次学习前必须读取 state/ 目录、最近 session、score-history 和 next-action。
6. 每次学习后必须更新 state/ 目录、sessions/ 记录、teacher notebook、interest-ledger 和 score-history。
7. 如果我答得不好，请改写后续计划，不要机械推进。
8. 生成后必须运行质检：先检查文件结构，再检查内容是否课程专属、无占位符、Day 1 可直接执行、测验和 mock exam 可考试，最后检查学生可见 prompt 是否泄露教师内部评分要点。
9. 如果质检失败，请先根据 quality-report 修订失败文件，再重新质检；不要把只存在文件但内容空泛的 OKF 标为通过。
10. 输出 zip 包，并告诉我入口文件、Day 1 入口、状态保存位置、恢复学习方法、structural validation、content quality gate、teaching runtime quality gate 和 repair status。
```

## Round 5 Visual Teaching Protocol

When generating a Course OKF, include visual teaching support. If a course topic uses curves, graph shifts, coordinate axes, equilibrium models, flow/process structures, geometry, or spatial layouts:

1. Require a diagram in the daily plan.
2. Prefer generated Python/matplotlib diagrams when the image is simple and stable.
3. For complex diagrams, search authoritative open sources such as official institutions, open textbooks, university open courseware, Wikipedia/Wikimedia Commons, or credible open-source tutorials.
4. Record source URL, license, and attribution for external diagrams.
5. Avoid complex ASCII diagrams as the primary teaching image.
6. Store diagrams under `assets/diagrams/` and update `assets/diagrams/index.md`.
7. Insert images near their explanation in the lesson.
8. Validate visual teaching through `visual_teaching_quality` before returning `passed=true`.
