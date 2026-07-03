---
type: Darwin Evaluation
title: Round 5 Visual Teaching Protocol Evaluation
description: Evaluation and revision summary for adding diagram generation, sourcing, indexing, and quality gates.
tags: [darwin, round-5, visual-teaching, diagram]
timestamp: 2026-07-03T00:00:00-07:00
---
# Round 5 Visual Teaching Protocol Evaluation

## Trigger Evidence

Day 3 macroeconomics learning exposed that curve-heavy lessons require stable images. Without a factory-level rule, the teaching skill initially attempted ASCII diagrams, which are fragile across phone and desktop layouts. The learner then requested program-generated diagrams, inline image placement, and authoritative/open-source references for complex diagrams.

## Revision Goal

Add visual teaching as a first-class Course OKF capability:

1. Detect curve/model/diagram-heavy concepts.
2. Prefer Python/matplotlib generated images when feasible.
3. Source complex diagrams from authoritative open materials and record attribution.
4. Avoid complex ASCII diagrams.
5. Persist images under `assets/diagrams/` with an index.
6. Validate visual teaching quality before marking a generated Course OKF as ready.

## Files Added

- `schemas/visual-teaching-trigger.md`
- `schemas/diagram-asset.md`
- `schemas/external-image-source.md`
- `playbooks/generate-diagram-with-python.md`
- `playbooks/find-authoritative-diagram.md`
- `playbooks/insert-diagram-in-lesson.md`
- `playbooks/update-diagram-index.md`
- `playbooks/diagram-failure-recovery.md`
- `tools/render_diagram_asset.py`
- `tools/check_diagram_quality.py`

## Main Implementation Changes

- `tools/materialize_course_okf.py` now creates:
  - `assets/diagrams/index.md`
  - `teacher/visual-teaching-policy.md`
  - `teacher/diagram-quality-rules.md`
  - `teacher/diagram-source-rules.md`
- `tools/course_seed_registry.py` now renders reusable macroeconomics diagrams during `macroeconomics-v1` seed repair.
- `tools/quality_check_course_okf.py` now includes `visual_teaching_quality`.
- `tests/test_materialize_course_okf.py` now checks diagram layer creation, macro diagram rendering, ASCII misuse detection, and rendering utility output.

## Smoke Test

Input:

```yaml
course_name: 宏观经济学
baseline: zero
days_available: 7
daily_minutes: 60
time_policy: soft
```

Result:

```yaml
validation_result.passed: true
quality_gate.passed: true
quality_score: 100
visual_teaching_quality.passed: true
diagram_assets_found: 7
```

Generated macro diagrams:

- `assets/diagrams/day3-ad-curve.png`
- `assets/diagrams/day3-sras-curve.png`
- `assets/diagrams/day3-lras-curve.png`
- `assets/diagrams/day3-ad-sras-equilibrium.png`
- `assets/diagrams/day3-ad-sras-four-shocks.png`
- `assets/diagrams/day3-output-gaps.png`
- `assets/diagrams/day3-policy-closing-output-gaps.png`

## Local Tests

```text
python -m pytest -q
11 passed in 6.36s
```

## Decision

Keep revision. It adds a necessary visual teaching protocol without turning the MVP into a heavy graphics system. The diagram renderer is intentionally narrow and reusable; complex images are delegated to authoritative external sources with attribution records.
