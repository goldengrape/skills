---
type: Quiz
title: Day 2 Quiz
description: Student-facing Day 2 quiz.
tags: [quiz, day-2, student-visible]
timestamp: 2026-07-07T07:38:01+00:00
---

# Day 2 Quiz

```yaml
visibility: student_prompt
assessment_mode: blind_quiz
score_type_if_unprompted: blind_score
prompt_visibility: hidden_until_answer
```

## Retrieval

1. 名词解释：上运动神经元体征
2. 简答：UMN 和 LMN 的三个关键区别是什么？
3. 说出今天最容易混淆的一组定位，并给出区分线索。

## Exam-Style Question

Question only:

```text
教学病例：患者右上肢和右下肢无力，肌张力增高，右侧 Babinski 阳性，同时无失语。请列出两个可能层级，并说明还需要什么线索区分。
```

## Boundary / Misuse Check

```text
同样是四肢无力，分别写出高颈髓、多发周围神经病、NMJ、肌病各自最关键的一条区分线索。
```

## Pass-Level Check

```yaml
possible_points: 14
pass_like_threshold: 9
A_topics_checked: [day-2-core]
prompt_visibility: hidden_until_answer
```

## State Update

作答后记录 score_type、prompt_visibility、错误类型、复测安排和下一步任务。
