---
type: Quiz
title: Day 1 Quiz
description: Student-facing Day 1 quiz.
tags: [quiz, day-1, student-visible]
timestamp: 2026-07-07T07:38:01+00:00
---

# Day 1 Quiz

```yaml
visibility: student_prompt
assessment_mode: blind_quiz
score_type_if_unprompted: blind_score
prompt_visibility: hidden_until_answer
```

## Retrieval

1. 名词解释：定位诊断
2. 简答：为什么不能一看到偏瘫就直接写大脑半球？
3. 说出今天最容易混淆的一组定位，并给出区分线索。

## Exam-Style Question

Question only:

```text
教学病例：患者左侧肢体无力，左侧腱反射活跃，左侧 Babinski 阳性，无明显肌萎缩。请写定位层级和依据。
```

## Boundary / Misuse Check

```text
一看到偏瘫时，列出至少两个能把半球、脑干、脊髓区分开的线索。
```

## Pass-Level Check

```yaml
possible_points: 14
pass_like_threshold: 9
A_topics_checked: [day-1-core]
prompt_visibility: hidden_until_answer
```

## State Update

作答后记录 score_type、prompt_visibility、错误类型、复测安排和下一步任务。
