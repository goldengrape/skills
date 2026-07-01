---
type: Playbook
title: Generate New Course OKF
description: Main procedure for creating a stateful course OKF from user input.
tags: [playbook, factory, generation]
timestamp: 2026-06-30T00:00:00-07:00
---
# Trigger

Use this playbook when the user gives a course name and wants a crash-course learning OKF.

# Procedure

## 1. Normalize Input

Follow [Normalize Factory Input](normalize-factory-input.md). Use defaults when safe and record assumptions.

## 2. Run Reconnaissance

Follow [Course Reconnaissance](../factory/course-reconnaissance.md). Prefer user materials. Record source confidence and source gaps in `resources.md`.

## 3. Create Course Slug

Use a short slug:

```text
course-okf-{course-name}-pass
```

Example:

```text
course-okf-management-pass
```

## 4. Emit Course OKF Layout

Create all required files from [Course Instance Layout](../schemas/course-instance-layout.md). If `days_available` is not 7, create matching `plan/day-N.md` and `quizzes/day-N-quiz.md` files for each day.

For local MVP execution, use `tools/materialize_course_okf.py` to create the skeleton first, then fill or revise course-specific content using the reconnaissance result.

## 5. Initialize State

Create:

* `state/current-state.md`
* `state/topic-ledger.md`
* `state/recall-deck.md`
* `state/misconceptions.md`
* `state/score-history.md`
* `state/next-action.md`
* `state/plan-changes.md`
* `state/interest-ledger.md`

The initial `next_action` should usually be `run_day_1`.

## 6. Generate Plan and Work Packages

Create:

* `plan/seven-day-plan.md` or configured-day plan
* `plan/day-1.md` through `plan/day-N.md`
* `quizzes/day-1-quiz.md` through `quizzes/day-N-quiz.md`
* `sessions/day-1-session.md` as a pending session record
* `learning-records/0001-initial-baseline.md`
* final review placeholders
* `teacher/` runtime files: notebook, visibility rules, time policy, engagement monitor, rubrics, and answer keys

Day 1 must be immediately runnable and include:

1. 5-minute baseline retrieval or diagnostic
2. 10-minute course map
3. 15-minute core explanation
4. 10-minute Feynman task
5. 10-minute exam answer practice
6. 5-minute feedback
7. 5-minute state update

## 7. Validate, Quality-Check, and Repair

Run [Validate Generated Course OKF](validate-generated-course-okf.md). This now has three layers:

1. Structural validation: required files and output contract exist.
2. Content quality gate: critical files are course-specific, not placeholders, and exam-ready.
3. Teaching runtime quality gate: prompts do not leak hidden answer elements, teacher notebook exists, score type is recorded, soft/strict time policy is present, and interest/engagement rules exist.

If the quality gate fails, run [Repair Generated Course OKF](repair-generated-course-okf.md), then rerun [Evaluate Generated Course OKF](evaluate-generated-course-okf.md). Do not return `validation_result.passed=true` until structural validation, content quality, and teaching runtime quality pass.

## 8. Optional Local Materialization Command

```bash
python tools/materialize_course_okf.py --input-json examples/management-factory-input.json --output-dir ./out
```

The helper creates the required file tree, runs structural validation, runs a content quality gate, and makes one repair attempt when a matching local course seed exists. Unknown courses remain quality-failed until course-specific content is filled from materials or reviewed by AI/human.

# Output Message

Tell the user:

* generated bundle name
* entrypoint file
* Day 1 file
* where state is saved
* how to resume next time
* structural validation result
* content quality result
* repair status, if any
* teaching runtime quality result
