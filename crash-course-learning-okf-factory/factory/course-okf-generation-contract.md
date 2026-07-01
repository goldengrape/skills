---
type: Factory Contract
title: Course OKF Generation Contract
description: Defines the input, output, and invariants of generating a course-specific OKF.
tags: [factory, contract, course-instance]
timestamp: 2026-06-30T00:00:00-07:00
---
# Contract

The factory accepts a learner's course request and emits a complete Course Learning OKF bundle.

# Required Input Fields

```yaml
course_name: string
baseline: zero | weak | partial | review
exam_date: optional ISO-8601 date
days_available: integer
daily_minutes: integer
target_score: integer | pass | stable_pass | high_score
exam_format: unknown | closed_book | open_book | multiple_choice | term_definition | short_answer | essay | mixed
course_type: concept_heavy | theory_heavy | law_intro | social_science | humanities | mixed | other
materials_available: none | uploaded | urls | mixed
materials:
  - type: syllabus | slides | notes | textbook | past_exam | teacher_hint | open_course | encyclopedia | article | other
    path_or_url: string
    priority: primary | secondary | background
    confidence: high | medium | low | unknown
constraints: []
```

# Optional Input Fields

```yaml
school_or_department: string
teacher_style: string
language: string
must_include_topics: [string]
must_avoid_topics: [string]
no_browse: boolean
user_preferences:
  answer_language: string
  explanation_style: concise | detailed | example_first
  quiz_intensity: light | normal | hard
  exam_answer_focus: term_definition | short_answer | essay | mixed
```

# Required Output Object

The generation run must return a compact output object:

```yaml
course_okf_name: string
course_slug: string
created_files: [string]
initial_state:
  current_day: integer
  pass_readiness: string
  next_action: string
seven_day_plan: string
day_1_entrypoint: string
state_update_rules: [string]
resume_rules: [string]
validation_result:
  passed: boolean
  structural:
    passed: boolean
    missing_files: [string]
    warnings: [string]
  quality_gate:
    passed: boolean
    attempts: [object]
    repair_result: object | null
    final_report: object
```

See [Course OKF Output](../schemas/course-okf-output.md).

# Required Generated Files

The generated course OKF must contain at least the files listed in [Course Instance Layout](../schemas/course-instance-layout.md).

# Executable Local MVP

The repository includes `tools/materialize_course_okf.py` as a minimal standard-library implementation of the layout, initial state, structural validation, content quality gate, and one repair attempt when a matching local course seed exists.

It is not a full universal content generator. Unknown courses still require a human or AI to fill course-specific content from materials or reconnaissance, and they must remain quality-failed until that content passes the quality gate.

# Invariants

1. The generated OKF represents exactly one course.
2. `state/current-state.md` is the canonical learner-position source.
3. `state/next-action.md` is the canonical next-step source.
4. Every learning session must create or update a session record.
5. Every quiz or answer review must update score history.
6. Every missed or confused concept must update recall deck or misconception tracker.
7. The remaining plan may change when evidence shows the original plan is too hard, too easy, or misaligned with exam risk.
8. The agent must read state before generating the next session.
9. User-provided materials outrank generic source knowledge.
10. Missing source evidence must be recorded as a source gap, not hidden.
11. Structural validation alone cannot set `validation_result.passed=true`.
12. Content quality failure must trigger repair and recheck, or remain visibly failed with exact repair actions.
