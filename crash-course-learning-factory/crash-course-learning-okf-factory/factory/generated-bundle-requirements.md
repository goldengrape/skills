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
* **small enough**: optimized for one hour per day unless configured otherwise
* **source-aware**: user materials and source gaps are explicit
* **validatable**: required files, rules, and content quality can be checked before handoff

# Required State Behavior

Before a session:

1. Read `state/current-state.md`.
2. Read `state/next-action.md`.
3. Read due cards from `state/recall-deck.md`.
4. Read unresolved misconceptions from `state/misconceptions.md`.
5. Read recent `state/score-history.md` entries.
6. Read recent `sessions/*.md`.
7. Read the relevant `plan/day-N.md`.

After a session:

1. Create or update a session record.
2. Update score history.
3. Update topic ledger.
4. Add or revise recall cards.
5. Add, revise, or resolve misconceptions.
6. Write the next action.
7. Add a plan-change record if future plans are revised.
8. Adapt future plan when necessary.

# Hard Stop Rules

* Do not proceed to a dependent A-topic while a high-severity prerequisite misconception is still open.
* Do not mark a misconception as resolved unless the learner succeeds on a new transfer or retest question.
* Do not return a generated OKF without a validation result.
* Do not mark a generated OKF as passed when critical learning files still contain placeholders.
* Do not treat a structurally complete OKF as educationally usable until the content quality gate passes.
* If content quality fails, repair the failed files and rerun the quality gate before handoff.
