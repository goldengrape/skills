---
type: Test Report
title: Round 4 Test Report
description: Local tests for teaching runtime quality revision.
tags: [test, round-4, teaching-runtime]
timestamp: 2026-06-30T00:00:00-07:00
---
# Round 4 Test Report

## Commands

```bash
python -m pytest -q
python tools/materialize_course_okf.py --course-name '宏观经济学' --baseline zero --days-available 7 --daily-minutes 60 --target-score 60 --time-policy soft --output-dir /mnt/data/r4_macro_test
```

## Results

```text
7 passed
```

Macroeconomics generated bundle:

```yaml
validation_result.passed: true
structural.passed: true
quality_gate.passed: true
teaching_runtime_quality.passed: true
teaching_runtime_failures: []
```

## Checked Runtime Files

- `teacher/teacher-notebook.md`
- `teacher/visibility-rules.md`
- `teacher/teaching-protocol.md`
- `teacher/engagement-monitor.md`
- `teacher/engagement-intervention-rules.md`
- `teacher/time-policy.md`
- `state/interest-ledger.md`

## Checked Prompt Leakage

Student-visible files checked by `tools/lint_prompt_visibility.py`:

- `plan/day-*.md`
- `quizzes/day-*-quiz.md`

Forbidden markers include:

- `至少提到`
- `要求至少`
- `答案要点`
- `评分标准`
- `标准答案`
- `参考答案`
- `得分点`
- `expected_points`
- `teacher_thinks`
