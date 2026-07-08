---
type: Quiz
title: Day 5 Quiz
description: Student-facing Day 5 quiz.
tags: [quiz, day-5, student-visible]
timestamp: 2026-07-07T07:38:01+00:00
---

# Day 5 Quiz

```yaml
visibility: student_prompt
assessment_mode: blind_quiz
score_type_if_unprompted: blind_score
prompt_visibility: hidden_until_answer
```

## Retrieval

1. 名词解释：失语
2. 简答：失语和构音障碍如何区分？
3. 说出今天最容易混淆的一组定位，并给出区分线索。

## Exam-Style Question

Question only:

```text
教学病例：右利手患者能听懂简单命令，但表达困难，右侧上肢无力。请定位层级。
```

## Boundary / Misuse Check

```text
给出失语与构音障碍各 2 条区分线索，并说明各自最常见的定位意义。
```

## Pass-Level Check

```yaml
possible_points: 14
pass_like_threshold: 9
A_topics_checked: [day-5-core]
prompt_visibility: hidden_until_answer
```

## State Update

作答后记录 score_type、prompt_visibility、错误类型、复测安排和下一步任务。
