---
type: Answer Material
title: Retest Bank Answer Material
description: Private scoring notes for high-risk misconception retests.
tags: [teacher, answer, retest, teacher-private, v3]
timestamp: 2026-07-07T10:05:00-07:00
---

# Retest Bank Answer Material

```yaml
visibility: teacher_private
source: assessment/retest-bank.md
release_rule: show_after_student_answer
```

## Scoring Protocol

每道复测题只在相关误判处于 `active` 或 `watch` 状态时调用。若学生在新题中能正确使用定位链条，才允许把对应 misconception 从 `active` 改为 `resolved_candidate`；还需下一次混合题不复发，才能改为 `resolved`。

## Feedback Template

```yaml
teacher_private:
  retest_id: RETEST-MC-XXX
  linked_misconception: MC-RISK-XXX
  localization_conclusion: "..."
  supporting_evidence:
    - "..."
  exclusion_reasoning:
    - "..."
  score_points:
    - item: "定位层级"
      points: 2
    - item: "证据"
      points: 2
    - item: "反证/区分"
      points: 2
  state_update:
    pass: "mark misconception as resolved_candidate and schedule mixed-case confirmation"
    fail: "keep active and assign adjacent easier case within 24h"
```
