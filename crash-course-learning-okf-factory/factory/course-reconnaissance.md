---
type: Factory Procedure
title: Course Reconnaissance
description: Procedure for building a minimal exam-oriented understanding of the requested course.
tags: [factory, research, course-map]
timestamp: 2026-06-30T00:00:00-07:00
---
# Purpose

Course reconnaissance turns a course name into a usable exam-preparation map. It should gather only enough information to identify likely units, high-value concepts, common question forms, and source gaps.

# Source Priority

1. User-provided syllabus, slides, notes, past exams, or teacher hints.
2. Official university syllabi and course descriptions.
3. Standard textbooks or open courseware.
4. Reputable educational summaries.
5. General web material only when higher-trust sources are unavailable.
6. Generic model knowledge only as a marked fallback.

# Required Reconnaissance Outputs

```yaml
course_scope:
  likely_units: []
  likely_exam_topics: []
  likely_question_types: []
  prerequisite_concepts: []
priority_map:
  A_must_learn: []
  B_should_learn: []
  C_can_skip: []
resources:
  - id: string
    type: string
    title: string
    priority: primary | secondary | background
    confidence: high | medium | low | unknown
    used_for: []
risk_notes: []
source_gaps: []
```

# Rules

* If the user has uploaded course materials, prefer them over generic web results.
* If the exam format is unknown, assume mixed recall, term definition, and short-answer questions.
* Do not overbuild the syllabus. The factory optimizes for a pass-level exam outcome, not full mastery.
* Mark uncertain assumptions explicitly in `resources.md` and `course-map.md`.
* Do not invent citations. If no source was read, write `source: generic_fallback` and set confidence to `low` or `unknown`.
