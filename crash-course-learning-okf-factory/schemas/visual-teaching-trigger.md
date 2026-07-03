---
type: Schema
title: Visual Teaching Trigger
description: Rules for deciding when a generated course must use diagrams or other visual assets.
tags: [schema, visual, teaching, diagram]
timestamp: 2026-07-03T00:00:00-07:00
---
# Visual Teaching Trigger

A Course OKF must treat visual explanation as required when the concept cannot be safely taught with prose alone.

```yaml
visual_trigger:
  required_when:
    - concept_type: curve
    - concept_type: coordinate_axes
    - concept_type: graph_shift
    - concept_type: equilibrium_model
    - concept_type: geometric_relation
    - concept_type: flow_or_process
    - concept_type: system_architecture
    - concept_type: spatial_layout
  recommended_when:
    - learner_confusion_mentions_axis
    - learner_confusion_mentions_left_right_shift
    - learner_requests_visual
    - concept_has_multiple_states
    - concept_has_before_after_comparison
  not_required_when:
    - pure_definition
    - simple_formula_without_graph
    - short_recall_question
```

## Rule

When `required_when` is triggered, the teacher must use a generated or sourced image. ASCII is allowed only as a temporary fallback for extremely simple sketches and must not become the primary explanation for complex curve or model diagrams.
