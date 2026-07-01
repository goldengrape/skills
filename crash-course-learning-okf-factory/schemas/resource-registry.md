---
type: Schema
title: Resource Registry
description: Schema for resources.md in a generated course OKF.
tags: [schema, resources, provenance]
timestamp: 2026-06-30T00:00:00-07:00
---
# Resource Registry

```yaml
resources:
  - id: resource-001
    type: syllabus | slides | notes | textbook | past_exam | teacher_hint | open_course | encyclopedia | article | other
    title: string
    path_or_url: string
    priority: primary | secondary | background
    confidence: high | medium | low | unknown
    used_for:
      - course_map
      - priority_map
      - daily_plan
      - quiz
    notes: string
source_gaps:
  - missing_item: syllabus | slides | past_exam | teacher_hint | textbook | other
    effect: string
    fallback: string
```

# Rules

* User-provided course materials are primary by default.
* Public sources must not override uploaded materials unless the generated OKF records why.
* Generic model knowledge is allowed only as a fallback and must be marked as lower confidence.
