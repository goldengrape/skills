---
type: Schema
title: Diagram Asset
description: Metadata schema for generated or externally sourced teaching diagrams.
tags: [schema, diagram, asset, visual]
timestamp: 2026-07-03T00:00:00-07:00
---
# Diagram Asset

Each reusable teaching image must be recorded in `assets/diagrams/index.md`.

```yaml
diagram_id: day3-ad-curve-v1
title: AD 曲线、坐标轴与左右移动
course: macroeconomics
day: 3
topic: AD-AS
concepts:
  - aggregate demand
  - price level
  - real output
  - curve shift
file_path: assets/diagrams/day-3-ad-curve-v1.png
source_type: generated # generated | external | temporary_ascii
source:
  generator: python_matplotlib
  script: tools/render_diagram_asset.py
  external_url: null
  source_name: null
  license: generated_by_course
  attribution_required: false
axis:
  x: real output Y
  y: price level P
curves:
  - AD0
  - AD_left
  - AD_right
used_in:
  - plan/day-3.md
  - teacher/teacher-notebook.md
  - learning-records/day-3-macroeconomics-learning-record.md
quality_checks:
  diagram_exists: true
  axes_labeled: true
  curve_labels_present: true
  direction_correct: true
  readable_on_mobile: true
  linked_from_index: true
```

## Required Fields

- `diagram_id`
- `file_path`
- `topic`
- `source_type`
- `used_in`
- `quality_checks`

External images must also record source URL, source name, license, and attribution.
