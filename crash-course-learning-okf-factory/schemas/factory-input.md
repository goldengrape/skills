---
type: Schema
title: Factory Input
description: Schema for the user request accepted by the factory.
tags: [schema, input]
timestamp: 2026-06-30T00:00:00-07:00
---
# Schema

```yaml
course_name: string
baseline: zero | weak | partial | review
exam_date: optional date
days_available: integer
daily_minutes: integer
time_policy: soft | strict
target_score: integer | pass | stable_pass | high_score
exam_format: unknown | closed_book | open_book | multiple_choice | term_definition | short_answer | essay | mixed
course_type: concept_heavy | theory_heavy | law_intro | social_science | humanities | mixed | other
materials_available: none | uploaded | urls | mixed
materials:
  - type: syllabus | slides | notes | textbook | past_exam | teacher_hint | open_course | encyclopedia | article | other
    path_or_url: string
    priority: primary | secondary | background
    confidence: high | medium | low | unknown
constraints:
  language: string
  no_browse: boolean
  daily_schedule: optional string
  maximum_new_A_topics_per_day: optional integer
  must_include_topics: [string]
  must_avoid_topics: [string]
preferences:
  answer_language: string
  explanation_style: concise | detailed | example_first
  time_policy_note: daily_minutes is soft unless time_policy is strict
  quiz_intensity: light | normal | hard
  exam_answer_focus: term_definition | short_answer | essay | mixed
```

# Defaults

```yaml
baseline: zero
daily_minutes: 60
time_policy: soft
days_available: 7
target_score: 60
exam_format: unknown
course_type: concept_heavy
materials_available: none
materials: []
constraints:
  no_browse: false
  maximum_new_A_topics_per_day: 3
preferences:
  answer_language: zh-CN
  explanation_style: concise
  quiz_intensity: normal
  exam_answer_focus: mixed
```

# Normalization Rules

| User wording | Normalized value |
|---|---|
| 零基础 | `baseline: zero` |
| 很弱 / 基础弱 | `baseline: weak` |
| 学过一点 / 听过课 | `baseline: partial` |
| 复习 / 学过但忘了 | `baseline: review` |
| 及格 / 60 分 | `target_score: 60` |
| 名词解释 | `exam_format: term_definition` |
| 简答 / 论述混合 | `exam_format: mixed` |

# Notes

When a field is missing, use a safe default and record it in the generated `mission.md` under `Assumptions`. Do not ask for clarification unless the missing field blocks generation.
