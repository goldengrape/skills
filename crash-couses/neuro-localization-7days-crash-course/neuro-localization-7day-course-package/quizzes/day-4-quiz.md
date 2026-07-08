---
type: Quiz
title: Day 4 Quiz
description: Student-facing Day 4 quiz.
tags: [quiz, day-4, student-visible]
timestamp: 2026-07-07T07:38:01+00:00
---

# Day 4 Quiz

```yaml
visibility: student_prompt
assessment_mode: blind_quiz
score_type_if_unprompted: blind_score
prompt_visibility: hidden_until_answer
```

## Retrieval

1. 名词解释：交叉性体征
2. 简答：同侧脑神经体征和对侧肢体体征为什么提示脑干？
3. 说出今天最容易混淆的一组定位，并给出区分线索。

## Exam-Style Question

Question only:

```text
教学病例：患者右侧周围性面瘫，左侧肢体无力，左侧病理反射阳性。请定位层级。
```

## Boundary / Misuse Check

```text
解释为什么同侧脑神经体征加对侧 Babinski 不能定位为对侧大脑半球。
```

## Pass-Level Check

```yaml
possible_points: 14
pass_like_threshold: 9
A_topics_checked: [day-4-core]
prompt_visibility: hidden_until_answer
```

## State Update

作答后记录 score_type、prompt_visibility、错误类型、复测安排和下一步任务。
