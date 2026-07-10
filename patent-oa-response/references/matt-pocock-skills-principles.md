---
type: Reference
title: mattpocock skill 设计原则
description: "说明本专利答通 skill 组合如何借鉴小型、可组合、用户调用与模型调用分离等设计原则。"
resource: https://github.com/mattpocock/skills
tags:
  - skills
  - design
  - reference
timestamp: "2026-07-09T00:00:00-07:00"
---


# 借鉴原则

本 bundle 借鉴了 mattpocock/skills 中几个核心设计思想：

## 小而可组合

专利答通流程很长，但不应写成一个巨大的单体 prompt。这里拆成：

- 一个用户调用总控 skill；
- 多个模型调用子 skill；
- 多个模板和策略规则。

## 用户调用与模型调用分离

`patent-oa-response` 是用户调用的总控 skill。其余 skill 可以由总控流程按需调用。

## 完成标准可检查

每个步骤都设置可检查输出，例如 claim chart、胜率区间、A/B 方案表，而不是写“充分分析”。

## 渐进披露

常用流程放在 skill 文件中，模板和政策放在单独目录，避免总控 skill 过长。

## 防止流程膨胀

专利答通有天然的循环冲动。本 bundle 用迭代停止规则限制循环，避免只靠模型自我评估不断上调胜率。

# Citations

- Skills repository: https://github.com/mattpocock/skills
- Writing great skills: https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md
