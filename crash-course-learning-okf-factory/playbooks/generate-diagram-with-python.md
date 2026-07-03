---
type: Playbook
title: Generate Diagram With Python
description: Create simple, stable teaching diagrams with Python/matplotlib when the environment supports it.
tags: [playbook, visual, diagram, python, matplotlib]
timestamp: 2026-07-03T00:00:00-07:00
---
# Generate Diagram With Python

Use this playbook when a curve, coordinate model, simple process chart, or before/after comparison can be generated reliably.

## Procedure

1. Identify the concept and the intended learning purpose.
2. Define axes and labels before drawing.
3. Generate a stable PNG or SVG under `assets/diagrams/`.
4. Add a row to `assets/diagrams/index.md`.
5. Insert the image inline near the corresponding explanation.
6. Record the diagram event in `teacher/teacher-notebook.md`.

## Quality Rules

- Label axes.
- Label curves.
- Label important shift directions or equilibrium points.
- Keep the image readable on mobile.
- Do not use ASCII as the main diagram for multi-curve graphs.

## Example

```bash
python tools/render_diagram_asset.py --diagram ad_sras_four_shocks --output-dir assets/diagrams
```
