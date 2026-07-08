---
type: Teacher Runtime
title: Teaching Protocol
description: 学生可见教学与教师侧记录的运行规则；已按 round5 加入视觉教学要求。
tags: [teacher, protocol, round5]
timestamp: 2026-07-03T00:00:00-07:00
---

# Teaching Protocol

## Core Split

每个教学回合分成两层：

```yaml
teacher_says:
  - shown to learner
teacher_thinks:
  - private planning, expected answer elements, scoring rule, next intervention
```

学习者作答前，只展示 `teacher_says`。`teacher_thinks` 保存在 `teacher/teacher-notebook.md` 或当天教师 notebook 中。

## Assessment Flow

1. 在教师侧记录任务目标、预期答题元素和评分规则。
2. 只展示学生可见题目。题干要中性，不提前暗示曲线名称、移动方向、缺口类型或答案结果。
3. 等学习者作答。
4. 作答后再评分、反馈和修正。
5. 在 `state/score-history.md` 记录 score type 和 prompt visibility。

## Score Types

| score_type | Meaning |
|---|---|
| blind_score | No answer elements or scoring hints were shown before the learner answered. |
| semi_assisted_score | The format was scaffolded, but specific answer elements were hidden. |
| assisted_score | Specific answer elements or substantial hints were shown before the learner answered. |

## Visual Teaching Flow

遇到曲线、坐标轴、图形移动、均衡模型、产出缺口、政策移动或流程图时：

1. 先读 `teacher/visual-teaching-policy.md` 和 `assets/diagrams/index.md`。
2. 优先使用 `assets/diagrams/` 中已有图像。
3. 新图形要优先用 Python/matplotlib 生成，保存到 `assets/diagrams/`，并更新索引。
4. 图像必须靠近对应解释，不只给孤立链接。
5. 不用复杂 ASCII 图作为主要讲解图。
6. 图形讲解顺序固定为：坐标轴 → 曲线含义 → 斜率/形状原因 → 沿曲线移动 vs 曲线移动 → 均衡变化。

## Interest-Led Branches

学习者提出更深问题时，默认按 `time_policy: soft` 处理。只要问题有助于理解核心概念，就可以继续，并在 `state/interest-ledger.md` 记录。若分支会挤占当天 A 类主题，应简短连接后放入后续计划。
