---
type: Teacher Runtime
title: Visual Teaching Policy
description: Rules for when and how to use diagrams in course teaching.
tags: [teacher, visual, diagram]
timestamp: 2026-07-03T05:24:06+00:00
---

# Visual Teaching Policy

## Trigger

If a lesson explains curves, coordinate axes, graph shifts, equilibrium models, geometric relations, flow/process structures, system diagrams, or spatial layouts, use a visual explanation.

## Source Priority

1. **Generate with Python/matplotlib when available.** Use this for stable teaching diagrams such as AD/SRAS/LRAS, supply-demand curves, simple functions, before/after shifts, and simple flow diagrams.
2. **Use authoritative open images when the diagram is complex.** Prefer official institutions, open textbooks, university open courseware, Wikipedia/Wikimedia Commons, or credible open-source tutorials. Record source URL, license, and attribution.
3. **Use ASCII only as a temporary tiny sketch.** Do not rely on ASCII for complex curves, multi-curve models, equilibrium shifts, or mobile-sensitive layouts.

## Teaching Rule

For a new curve or graph, explain:

- horizontal axis and vertical axis;
- why the axes are chosen;
- what each curve means;
- why the slope has that direction;
- movement along the curve vs whole-curve shift;
- old and new equilibrium points when relevant.

## Display Rule

Insert the image near the matching explanation, not only as a detached link. Record every generated or sourced image in `assets/diagrams/index.md`.
