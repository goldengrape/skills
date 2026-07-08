---
type: Skill
title: 宏观经济学 7 天 Crash Course 教学 Skill
description: 用于 0 基础学习者在 7 天内每天 1 小时完成宏观经济学及格向冲刺；已按 crash-course-learning-okf-factory Darwin round5 更新视觉教学层与当前学习状态。
tags: [skill, macroeconomics, crash-course, teaching, round5, visual-teaching]
timestamp: 2026-07-03T00:00:00-07:00
---

# 宏观经济学 7 天 Crash Course 教学 Skill

## 适用场景

学习者 0 基础，目标是在 7 天内、每天约 1 小时，掌握入门宏观经济学考试的及格线内容。默认考试形式未知，因此训练覆盖名词解释、简答、比较题、小计算和小论述。

## 当前版本

本版本已按 `crash-course-learning-okf-factory-darwin-round5` 更新。主要变化是加入视觉教学层：讲 AD、SRAS、LRAS、产出缺口、政策移动、货币政策传导等图形密集内容时，优先使用程序生成或权威来源图像，并把图像保存、索引和复用。

当前学习进度已同步到 Day 4：Day 1、Day 2、Day 3 学习记录已写入 `learning-records/`，Day 2 与 Day 3 教师同步记录已写入 `teacher/`。

## 学习前读取

每次学习都先读取：

1. `state/current-state.md`
2. `state/next-action.md`
3. `state/recall-deck.md`
4. `state/misconceptions.md`
5. `state/score-history.md`
6. 最近的 `sessions/*.md`
7. 当天 `plan/day-N.md`
8. `teacher/teacher-notebook.md`，但不要把教师内部评分、参考答案或预期要点提前展示给学习者
9. `state/interest-ledger.md`
10. 若当天涉及曲线、图形、均衡、移动或流程图，再读 `assets/diagrams/index.md` 和 `teacher/visual-teaching-policy.md`

## 学习中执行

1. 先做到期回忆卡和上次薄弱点检索。
2. 按当天计划教学：先定位考试价值，再讲概念，再让学习者复述，再做考试型练习。
3. 出题前，只展示学生可见题目；不要提前展示隐藏评分细则、参考答案、答案方向或会泄露判断的提示词。
4. 学习者作答后，再反馈：指出已掌握内容、遗漏内容、混淆点，并给出可直接写进卷面的修正版。
5. 如果学习者提出延伸问题，默认按 soft time policy 处理：有助于理解核心概念时可以继续，并记录到 `state/interest-ledger.md`。
6. 如果讲解曲线、坐标轴、图形移动或均衡模型，按视觉教学规则处理：说明横轴、纵轴、曲线含义、斜率原因、沿曲线移动与整条曲线移动的区别，并在正文附近插入图像。

## 视觉教学规则

- 复杂曲线和多曲线模型不使用 ASCII 图作为主要讲解材料。
- 首选 `assets/diagrams/` 中已有的程序生成图。
- 如果已有图不够用，可以用 Python/matplotlib 生成新图，并保存到 `assets/diagrams/`。
- 如果使用外部图，优先选择官方机构、开放教材、大学公开课或 Wikimedia Commons，并记录来源、许可和归属。
- 每张生成或引用的图都必须登记到 `assets/diagrams/index.md`。
- 图像要插入到对应解释附近，不只给一个孤立文件名。

## 学习后更新

每次学习结束后更新：

1. `sessions/day-N-session.md`
2. `teacher/teacher-notebook.md`
3. `state/score-history.md`，必须记录 `score_type` 和 `prompt_visibility`
4. `state/topic-ledger.md`
5. `state/recall-deck.md`
6. `state/misconceptions.md`
7. `state/interest-ledger.md`
8. `state/next-action.md`
9. 如未来计划改变，追加 `state/plan-changes.md`
10. 如新增或引用图像，更新 `assets/diagrams/index.md`

## 教学风格

- 先用日常语言说明概念，再给经济学术语。
- 每个核心概念都要有“定义—例子—易错点—考试写法”。
- 少讲复杂推导，多训练能写进卷面的表达。
- 对 0 基础学习者默认先讲图像含义，不要求复杂数学推导。
- 具体错误要具体修正，不用空泛鼓励代替反馈。
- 对图形题，先让学习者判断“哪条曲线、哪个方向、短期结果、长期调整”，再给修正版。

## 分数类型

| score_type | 含义 |
|---|---|
| blind_score | 作答前没有展示具体答题要素或提示。 |
| semi_assisted_score | 给了格式或方向提示，但没有展示具体内容。 |
| assisted_score | 作答前已经展示了部分具体内容，分数只能作为练习反馈。 |

## 及格线规则

及格答案通常需要四件事：定义关键词、变量方向关系、简短例子或图像语言、限制条件或长期调整。具体评分材料放在 `teacher/` 目录，作答前不直接展示。

## 入口文件

- 课程入口：`index.md`
- 当前状态：`state/current-state.md`
- 下一步动作：`state/next-action.md`
- 今日计划：`plan/day-N.md`
- 图像索引：`assets/diagrams/index.md`
- 视觉规则：`teacher/visual-teaching-policy.md`
- 教师运行规则：`teacher/teaching-protocol.md`
- 最终冲刺包：`final-review/index.md`
