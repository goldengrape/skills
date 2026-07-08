---
type: Schema
title: Case Answer Schema
description: Case, teacher material and state event schema.
tags: [schema, case]
timestamp: 2026-07-07T07:38:01+00:00
---

# Case and Answer Schema

## Student-Facing Case

```yaml
case_id: CASE-DAY4-001
visibility: student_prompt
stem: 教学模拟病例。只呈现病史和查体线索。
question: 请定位病灶并说明依据。
allowed_time_minutes: 6
```

## Teacher-Private Material

```yaml
teacher_private:
  localization_conclusion: string
  supporting_evidence: list[string]
  exclusion_reasoning: list[string]
  common_mistakes: list[string]
  score_points: list[object]
  remediation: list[string]
```

## State Event Output

```yaml
state_event:
  case_id: string
  localization_tag: string
  score_type: blind_score | semi_assisted_score | assisted_score
  prompt_visibility: hidden_until_answer | hinted_before_answer | shown_after_answer
  error_type: side_confusion | level_confusion | evidence_missing | disease_before_location | correct
  next_retest: string
```
