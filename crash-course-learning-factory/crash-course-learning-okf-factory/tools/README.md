---
type: Tool Guide
title: Local Tools
description: Minimal local helpers for creating and quality-checking Course Learning OKF instances.
tags: [tool, materializer, quality, mvp]
timestamp: 2026-06-30T00:00:00-07:00
---
# Local Tools

## `tools/materialize_course_okf.py`

Creates a Course Learning OKF directory from normalized input. It now does four things:

1. materializes the required file tree;
2. initializes learner state;
3. runs structural validation;
4. runs a post-generation content quality gate and makes one deterministic repair attempt when a matching local course seed exists.

Example:

```bash
python tools/materialize_course_okf.py \
  --course-name "Macroeconomics" \
  --baseline zero \
  --days-available 7 \
  --daily-minutes 60 \
  --target-score 60 \
  --output-dir ./out
```

## `tools/quality_check_course_okf.py`

Checks whether a generated Course Learning OKF is actually usable, not merely structurally present.

```bash
python tools/quality_check_course_okf.py ./out/course-okf-macroeconomics-pass \
  --output-json ./out/course-okf-macroeconomics-pass/quality-report.json
```

The quality gate checks:

- unresolved placeholders;
- course-specific terms;
- A/B/C priority map quality;
- Day 1 runnability;
- Day 1 quiz exam style;
- final mock exam shape;
- basic recoverability state files.

## `tools/course_seed_registry.py`

Contains small tested seed packs for common courses. Current MVP seeds:

```text
macroeconomics-v1
management-v1
```

Unknown courses do not get a fake pass. The local helper still creates the file tree, but `validation_result.passed` remains false until the generated course OKF is filled from materials or reviewed by AI/human and passes the quality gate.

## Output Files

A generated course folder includes:

```text
generation-output.json
quality-report.json
```

`generation-output.json` contains:

```yaml
validation_result:
  passed: structural.passed && quality_gate.passed
  structural: ...
  quality_gate: ...
```
