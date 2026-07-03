---
type: Playbook
title: Update Diagram Index
description: Record each generated or referenced image as a reusable course asset.
tags: [playbook, visual, diagram, index]
timestamp: 2026-07-03T00:00:00-07:00
---
# Update Diagram Index

Each course instance must maintain `assets/diagrams/index.md`.

## Required Columns

| Diagram ID | File | Topic | Source | Used in | Notes |
|---|---|---|---|---|---|

## Event Record

Also add a notebook entry when a diagram is used:

```yaml
diagram_used:
  diagram_id:
  file_path:
  source_type:
  inserted_inline:
  purpose:
  student_confusion_addressed: []
  quality_status:
```
