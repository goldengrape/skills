---
type: Quiz
title: Day 3 Quiz
description: Student-facing Day 3 quiz.
tags: [quiz, day-3, student-visible]
timestamp: 2026-07-07T07:38:01+00:00
---

# Day 3 Quiz

```yaml
visibility: student_prompt
assessment_mode: blind_quiz
score_type_if_unprompted: blind_score
prompt_visibility: hidden_until_answer
```

## Retrieval

1. 名词解释：感觉平面
2. 简答：感觉分离为什么有助于脊髓定位？
3. 说出今天最容易混淆的一组定位，并给出区分线索。

## Exam-Style Question

Question only:

```text
教学病例：患者胸部以下痛温觉下降，双下肢痉挛性无力，膀胱功能异常。请定位层级。
```

## Boundary / Misuse Check

```text
解释“手套袜套样感觉异常”和“感觉平面”的差别，并各给一个定位方向。
```

## Pass-Level Check

```yaml
possible_points: 14
pass_like_threshold: 9
A_topics_checked: [day-3-core]
prompt_visibility: hidden_until_answer
```

## State Update

作答后记录 score_type、prompt_visibility、错误类型、复测安排和下一步任务。
