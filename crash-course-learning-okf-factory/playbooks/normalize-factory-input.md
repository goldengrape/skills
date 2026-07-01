---
type: Playbook
title: Normalize Factory Input
description: Procedure for converting a learner request into the factory input schema.
tags: [playbook, input, normalization]
timestamp: 2026-06-30T00:00:00-07:00
---
# Trigger

Use before generating a new Course Learning OKF.

# Procedure

1. Extract course name, baseline, exam date, days available, daily minutes, target score, exam format, course type, materials, and constraints.
2. Apply defaults from [Factory Input](../schemas/factory-input.md) when fields are missing and do not block generation.
3. Normalize common wording:
   - `零基础` → `baseline: zero`
   - `听过一点` → `baseline: partial`
   - `复习` → `baseline: review`
   - `及格` or `60 分` → `target_score: 60`
4. Record assumptions for missing non-critical information.
5. If course materials are available, list them under `materials` and set `materials_available`.
6. If no materials are available, set `materials_available: none` and add a source gap.

# Output

```yaml
factory_input: {}
assumptions: []
source_gaps: []
blocking_questions: []
```

# Rule

Do not ask for clarification unless a missing answer prevents generating a minimally useful OKF. For ordinary missing fields, use defaults and record assumptions.
