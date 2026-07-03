---
type: Test Report
title: Round 5 Visual Teaching Protocol Test Report
description: Local test and smoke-test results for diagram generation and visual quality gates.
tags: [test, visual-teaching, diagram, round-5]
timestamp: 2026-07-03T00:00:00-07:00
---
# Round 5 Test Report

## Commands

```bash
python -m pytest -q
python tools/materialize_course_okf.py \
  --course-name '宏观经济学' \
  --baseline zero \
  --days-available 7 \
  --daily-minutes 60 \
  --time-policy soft \
  --output-dir /mnt/data/cc_okf_round5/smoke_out
```

## Unit Tests

```text
11 passed in 6.36s
```

## Smoke Test Result

```yaml
validation_result.passed: true
quality_gate.passed: true
quality_score: 100
visual_teaching_quality.passed: true
diagram_assets_found: 7
```

## Tested Behaviors

- Generated courses include visual runtime files and diagram index.
- Macroeconomics seed generates reusable diagram PNGs.
- Visual quality gate detects complex ASCII graph misuse.
- Diagram renderer writes valid PNG files.
- `quality_check_course_okf.py` includes `visual_teaching_quality` in final reports.
