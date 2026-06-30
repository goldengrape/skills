---
type: Test Report
title: Darwin Round 3 Local Test Report
summary: Local tests for post-generation quality gate and repair loop.
tags: [darwin, tests, quality-gate, macroeconomics]
timestamp: 2026-06-30T00:00:00-07:00
---
# Darwin Round 3 Local Test Report

## Test Command

```bash
python -m pytest -q
```

Result:

```text
5 passed in 0.13s
```

## Macroeconomics Generation Retest

Input:

```yaml
course_name: 宏观经济学
baseline: zero
days_available: 7
daily_minutes: 60
target_score: 60
```

Command:

```bash
python tools/materialize_course_okf.py \
  --course-name '宏观经济学' \
  --baseline zero \
  --days-available 7 \
  --daily-minutes 60 \
  --target-score 60 \
  --output-dir /mnt/data/round3_macro_test
```

Generated folder:

```text
course-okf-course-1b9e0c9c-pass/
```

The non-ASCII slug fallback is expected because the local slugifier keeps ASCII paths stable.

## Quality Gate Result

```yaml
validation_result:
  passed: true
  structural:
    passed: true
    missing_files: []
  quality_gate:
    passed: true
    attempts:
      - action: initial_quality_check
        passed: false
        score: 22
      - action: course_seed_repair
        applied: true
        seed_id: macroeconomics-v1
      - action: post_repair_quality_check
        passed: true
        score: 100
```

## Course-Specific Terms Found

```text
GDP
inflation
CPI
unemployment
aggregate demand
aggregate supply
fiscal policy
monetary policy
central bank
interest rate
```

## Repair Behavior Confirmed

The first quality check failed because the initial skeleton still contained placeholders. The materializer then applied `macroeconomics-v1`, rewrote critical files, and reran the quality check. The final check passed.

Critical files repaired:

```text
course-map.md
priority-map.md
glossary.md
plan/seven-day-plan.md
plan/day-1.md ... plan/day-7.md
quizzes/day-1-quiz.md ... quizzes/day-7-quiz.md
final-review/compressed-notes.md
final-review/must-know-list.md
final-review/answer-templates.md
final-review/mock-exam.md
```

## Unknown Course Behavior

An unknown course still gets a structural file tree, but does not get `validation_result.passed=true`. The quality gate returns repair actions and requires course-specific content from materials or AI/human review.
