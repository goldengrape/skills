---
type: Schema
title: Course Instance Layout
description: Required directory tree for generated course-specific OKF bundles.
tags: [schema, course-instance, layout]
timestamp: 2026-06-30T00:00:00-07:00
---
# Required Layout

```text
course-okf-{course-slug}/
├── index.md
├── log.md
├── mission.md
├── course-map.md
├── resources.md
├── priority-map.md
├── glossary.md
├── plan/
│   ├── index.md
│   ├── seven-day-plan.md
│   ├── day-1.md
│   ├── day-2.md
│   ├── day-3.md
│   ├── day-4.md
│   ├── day-5.md
│   ├── day-6.md
│   └── day-7.md
├── state/
│   ├── index.md
│   ├── current-state.md
│   ├── topic-ledger.md
│   ├── recall-deck.md
│   ├── misconceptions.md
│   ├── score-history.md
│   ├── next-action.md
│   ├── plan-changes.md
│   └── interest-ledger.md
├── sessions/
│   ├── index.md
│   └── day-1-session.md
├── learning-records/
│   ├── index.md
│   └── 0001-initial-baseline.md
├── quizzes/
│   ├── index.md
│   ├── day-1-quiz.md
│   ├── day-2-quiz.md
│   ├── day-3-quiz.md
│   ├── day-4-quiz.md
│   ├── day-5-quiz.md
│   ├── day-6-quiz.md
│   └── day-7-quiz.md
├── final-review/
│   ├── index.md
│   ├── compressed-notes.md
│   ├── must-know-list.md
│   ├── answer-templates.md
│   └── mock-exam.md
└── teacher/
    ├── index.md
    ├── teaching-protocol.md
    ├── visibility-rules.md
    ├── teacher-notebook.md
    ├── engagement-monitor.md
    ├── engagement-intervention-rules.md
    ├── time-policy.md
    ├── rubrics/
    │   ├── day-1-rubric.md
    │   └── ...
    └── answer-keys/
        ├── day-1-answer-key.md
        └── ...
```

# Variable-Day Rule

If `days_available` is not 7, create `plan/day-N.md` and `quizzes/day-N-quiz.md` for each available day. Keep the same state files and final-review files.

# Required Frontmatter

Every non-reserved markdown file must include:

```yaml
---
type: <descriptive type>
title: <display title>
description: <one-line description>
tags: [...]
timestamp: <ISO 8601 datetime>
---
```

`index.md` and `log.md` follow OKF reserved-file conventions.

# Generated Bundle Rule

The generated bundle is not a static syllabus. It is a stateful learning workspace. The `state/` directory is the canonical learner memory. The `teacher/` directory stores teacher-private runtime notes, rubrics, answer keys, visibility rules, and engagement rules; it must not be pasted into the student-visible conversation before assessment.

## Round 5 Visual Teaching Layout

Generated course instances must include:

```text
assets/diagrams/index.md
teacher/visual-teaching-policy.md
teacher/diagram-quality-rules.md
teacher/diagram-source-rules.md
```

If visual triggers are present, `assets/diagrams/` should also contain reusable generated PNG/SVG files or records of authoritative external diagrams.
