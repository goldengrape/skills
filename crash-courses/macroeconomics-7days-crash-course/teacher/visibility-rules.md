---
type: Teacher Runtime
title: Visibility Rules
description: 区分作答前和作答后的可见内容。
tags: [teacher, visibility]
timestamp: 2026-06-30T00:00:00-07:00
---

# Visibility Rules

## Before Learner Answers: Allowed

- 题目本身。
- 时间或字数范围。
- 输出格式。
- 是否允许看笔记。
- 中性提醒：先按自己的理解作答。

## Before Learner Answers: Not Allowed

- 具体答题元素。
- 隐藏评分细则。
- 标准或参考表达。
- “你需要写出这些点”一类提示。
- 教师内部判断。

## After Learner Answers: Allowed

- 遗漏内容。
- 修正表达。
- 简洁的参考写法。
- 评分解释。
- 新的回忆卡和错因修复。

## Exception

引导练习可以给支架，但该结果必须记录为 `assisted_score` 或 `semi_assisted_score`，不能记录为 `blind_score`。
