---
type: Playbook
title: Diagram Failure Recovery
description: Fallback behavior when diagram generation or retrieval fails.
tags: [playbook, visual, diagram, failure]
timestamp: 2026-07-03T00:00:00-07:00
---
# Diagram Failure Recovery

If a diagram generation request fails, do not return an empty response.

## Required Fallback

1. State that the diagram could not be generated or retrieved in the current step.
2. Provide a short text explanation of axes and variables.
3. Attempt a simpler generated diagram, or search for an authoritative open image if the diagram is complex.
4. Use temporary ASCII only for tiny sketches and mark it as `temporary_ascii`.
5. Record the failure in `teacher/teacher-notebook.md`.
6. Mark the missing diagram in `assets/diagrams/index.md` as `repair_needed` if the course should keep it.

## Notebook Record

```yaml
diagram_event:
  status: failed
  requested_diagram:
  failure_mode:
  fallback_used:
  repair_needed: true
```
