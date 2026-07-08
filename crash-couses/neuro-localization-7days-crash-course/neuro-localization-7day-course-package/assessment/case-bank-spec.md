---
type: Assessment Spec
title: Case Bank Specification
description: Case inventory and coverage policy; teacher answer locations are controlled by the runner and are not exposed in student-facing specs.
tags: [assessment, case-bank, v3]
timestamp: 2026-07-07T10:05:00-07:00
---

# Case Bank Specification

```yaml
visibility: runner_controlled
student_visible: false
answer_key_policy: teacher_private_controlled_by_runner
```

## Case ID Convention

- `DAY{N}-CASE-A`：每日典型题。
- `DAY{N}-CASE-B`：每日反例/迷惑题。
- `MOCK-001..009`：Day 7 混合模拟题。
- `SPINAL-001..005`：脊髓专项题。

## Case Inventory

| Case ID | Module | Localization tag | Student prompt surface | Answer visibility |
|---|---|---|---|---|
| DAY1-CASE-A | course map | corticospinal_umn.screening | plan/day-1.md | teacher_private_after_answer |
| DAY1-CASE-B | course map | hemiparesis_boundary | plan/day-1.md | teacher_private_after_answer |
| DAY2-CASE-A | motor | umn_lmn.discrimination | plan/day-2.md | teacher_private_after_answer |
| DAY2-CASE-B | motor | quadriparesis_boundary | plan/day-2.md | teacher_private_after_answer |
| DAY3-CASE-A | spinal | spinal_cord.hemicord | plan/day-3.md | teacher_private_after_answer |
| DAY3-CASE-B | spinal | polyneuropathy_vs_spinal | plan/day-3.md | teacher_private_after_answer |
| DAY4-CASE-A | brainstem | brainstem.crossed | plan/day-4.md | teacher_private_after_answer |
| DAY4-CASE-B | brainstem | facial_palsy_boundary | plan/day-4.md | teacher_private_after_answer |
| DAY5-CASE-A | supratentorial | dominant_frontal_language | plan/day-5.md | teacher_private_after_answer |
| DAY5-CASE-B | cerebellar | coordination_vs_weakness | plan/day-5.md | teacher_private_after_answer |
| DAY6-CASE-A | peripheral | polyneuropathy.length_dependent | plan/day-6.md | teacher_private_after_answer |
| DAY6-CASE-B | motor_unit | muscle_vs_nmj | plan/day-6.md | teacher_private_after_answer |
| MOCK-001 | mixed | corticospinal_umn.screening | final-review/mock-exam.md | teacher_private_after_answer |
| MOCK-002 | mixed | brainstem.pons_crossed | final-review/mock-exam.md | teacher_private_after_answer |
| MOCK-003 | mixed | spinal_cord.level | final-review/mock-exam.md | teacher_private_after_answer |
| MOCK-004 | mixed | peripheral.polyneuropathy | final-review/mock-exam.md | teacher_private_after_answer |
| MOCK-005 | mixed | aphasia_vs_dysarthria | final-review/mock-exam.md | teacher_private_after_answer |
| MOCK-006 | mixed | root_vs_nerve | final-review/mock-exam.md | teacher_private_after_answer |
| MOCK-007 | mixed | brainstem_crossed_reasoning | final-review/mock-exam.md | teacher_private_after_answer |
| MOCK-008 | mixed | dominant_hemisphere_language_motor | final-review/mock-exam.md | teacher_private_after_answer |
| MOCK-009 | mixed | muscle_vs_nmj_vs_neuropathy | final-review/mock-exam.md | teacher_private_after_answer |
| SPINAL-001..005 | spinal | spinal_subsyndromes | assessment/spinal-localization-drill.md | teacher_private_after_answer |

## Coverage Rule

A-priority localization tags must appear in at least one daily question and one mixed review item. Mixed review uses exactly 9 items, aligned across `plan/day-7.md`, `final-review/mock-exam.md`, and Day 7 teacher material.
