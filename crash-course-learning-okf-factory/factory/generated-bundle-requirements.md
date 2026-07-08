---
type: Factory Requirement
title: Generated Bundle Requirements
description: Required properties of every course OKF emitted by this factory.
tags: [factory, requirements]
timestamp: 2026-06-30T00:00:00-07:00
---
# Required Properties

A generated Course Learning OKF must be:

* **single-course**: one course, one exam target
* **stateful**: able to resume from saved learner state
* **evidence-based**: learner progress is recorded through answers, quizzes, and corrections
* **adaptive**: future sessions can change based on state
* **exam-oriented**: all content traces back to likely assessment value
* **time-aware**: optimized for the configured daily minutes, with soft mode as the default and strict mode only when requested
* **source-aware**: user materials and source gaps are explicit
* **validatable**: required files, course content quality, and teaching runtime quality can be checked before handoff
* **visibility-safe**: teacher-private scoring material is not shown before learner answers
* **interest-preserving**: learner-led deeper questions are recorded and used constructively

# Required State Behavior

Before a session:

1. Read `state/current-state.md`.
2. Read `state/next-action.md`.
3. Read due cards from `state/recall-deck.md`.
4. Read unresolved misconceptions from `state/misconceptions.md`.
5. Read recent `state/score-history.md` entries.
6. Read recent `sessions/*.md`.
7. Read the relevant `plan/day-N.md`.
8. Read `teacher/teacher-notebook.md` without displaying private notes.
9. Read `state/interest-ledger.md`.

After a session:

1. Create or update a session record.
2. Update score history with `score_type` and `prompt_visibility`.
3. Update topic ledger.
4. Add or revise recall cards.
5. Add, revise, or resolve misconceptions.
6. Append teacher runtime notes to `teacher/teacher-notebook.md`.
7. Record learner-led branches in `state/interest-ledger.md`.
8. Write the next action.
7. Add a plan-change record if future plans are revised.
8. Adapt future plan when necessary.

# Hard Stop Rules

* Do not proceed to a dependent A-topic while a high-severity prerequisite misconception is still open.
* Do not mark a misconception as resolved unless the learner succeeds on a new transfer or retest question.
* Do not return a generated OKF without a validation result.
* Do not mark a generated OKF as passed when critical learning files still contain placeholders.
* Do not treat a structurally complete OKF as educationally usable until the content quality gate passes.
* If content quality fails, repair the failed files and rerun the quality gate before handoff.
* Do not reveal rubrics, answer keys, or expected answer elements before the learner answers.
* Do not treat `daily_minutes` as a hard limit unless `time_policy: strict` or the learner explicitly asks for strict time control.

## Round 5 Visual Asset Requirements

Generated Course OKF bundles must now include a visual teaching layer:

```text
assets/
└── diagrams/
    ├── index.md
    └── *.png / *.svg when generated or sourced

teacher/
├── visual-teaching-policy.md
├── diagram-quality-rules.md
└── diagram-source-rules.md
```

A course that teaches curves, graph shifts, coordinate models, equilibrium diagrams, geometry, process flows, or spatial structures must either provide generated diagrams or record authoritative open-source diagram references. Complex ASCII diagrams are not acceptable as final teaching assets.

## Learning Contract and AI Diet Requirements

Every generated Course OKF must include a compact learning-control layer: `learning-contract/index.md`, `teacher/learning-control-policy.md`, `state/concept-mastery-state.md`, and `state/assessment-evidence-ledger.md`. A-priority concepts default to L6 unless the user overrides. L6 requires misuse-discrimination evidence; L7 requires transfer evidence. Scores must record assistance mode.
