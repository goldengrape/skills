---
type: Factory Checklist
title: Validation Checklist
description: Checklist for validating a generated Course Learning OKF.
tags: [factory, validation]
timestamp: 2026-06-30T00:00:00-07:00
---
# Validation Checklist

Use this checklist after generating a course OKF.

## Structure

- [ ] Root `index.md` exists.
- [ ] Root `log.md` exists.
- [ ] `mission.md` names the course, goal, constraints, assumptions, and out-of-scope topics.
- [ ] `course-map.md` lists likely units and dependencies.
- [ ] `resources.md` lists sources, source confidence, and source gaps.
- [ ] `priority-map.md` separates A/B/C topics.
- [ ] `plan/seven-day-plan.md` exists or equivalent configured-day plan exists.
- [ ] `plan/day-N.md` exists for every available day.
- [ ] `quizzes/day-N-quiz.md` exists for every available day.
- [ ] `sessions/day-1-session.md` exists as a pending or template record.
- [ ] `learning-records/0001-initial-baseline.md` exists.
- [ ] Final review files exist: compressed notes, must-know list, answer templates, mock exam.

## State

- [ ] `state/current-state.md` exists and has a parseable learner state.
- [ ] `state/topic-ledger.md` exists.
- [ ] `state/recall-deck.md` exists.
- [ ] `state/misconceptions.md` exists.
- [ ] `state/score-history.md` exists.
- [ ] `state/next-action.md` exists.
- [ ] `state/plan-changes.md` exists.
- [ ] `state/interest-ledger.md` exists.

## Learning Plan

- [ ] Day 1 work package is immediately runnable.
- [ ] Daily plan includes retrieval, map, core explanation, Feynman task, exam answer practice, feedback, and state update.
- [ ] Daily workload fits `daily_minutes`.
- [ ] A/B/C priorities affect the daily plan.

## Content Quality

- [ ] Critical files do not contain unresolved placeholders such as `TBD`, `Fill this`, or `今日 A 类概念`.
- [ ] `course-map.md` contains course-specific units, dependencies, and easy-confusion notes.
- [ ] `priority-map.md` contains A/B/C topics with exam-value reasons.
- [ ] `plan/day-1.md` is directly runnable and course-specific.
- [ ] `quizzes/day-1-quiz.md` contains exam-style term explanation, short-answer, or comparison tasks.
- [ ] `final-review/must-know-list.md` contains course-specific high-value concepts.
- [ ] `final-review/mock-exam.md` is scored or clearly exam-like.
- [ ] If content quality fails, `quality-report.json` lists repair actions and the factory reruns the quality gate after repair.

## Teaching Runtime Quality

- [ ] `teacher/teacher-notebook.md` exists and defines `teacher_says` and `teacher_thinks`.
- [ ] `teacher/visibility-rules.md` separates before-answer and after-answer behavior.
- [ ] Student-visible prompts do not reveal answer elements before the learner answers.
- [ ] `state/score-history.md` records `score_type` and `prompt_visibility`.
- [ ] `teacher/time-policy.md` distinguishes soft and strict modes.
- [ ] `teacher/engagement-monitor.md` uses observable signals only.
- [ ] `teacher/engagement-intervention-rules.md` preserves interest and offers attention-repair moves.

## Adaptation

- [ ] There is a defined rule for when to slow down.
- [ ] There is a defined rule for when to advance.
- [ ] There is a defined rule for when to rewrite future days.
- [ ] Plan rewrites append to `state/plan-changes.md`.

## Output Contract

- [ ] Generation result includes `course_okf_name` and `course_slug`.
- [ ] Generation result lists `created_files`.
- [ ] Generation result includes `initial_state`.
- [ ] Generation result includes `day_1_entrypoint`.
- [ ] Generation result includes `state_update_rules`.
- [ ] Generation result includes `resume_rules`.
- [ ] Generation result includes `validation_result`.


# Local Materializer Check

When `tools/materialize_course_okf.py` is used, verify that the generated course folder contains `generation-output.json` and `quality-report.json`. `validation_result.passed` is true only when structural validation, content quality, and teaching runtime quality all pass.

## Round 5 Visual Teaching Validation

A generated Course OKF must pass the visual teaching gate when visual triggers are present.

Required checks:

- `teacher/visual-teaching-policy.md` exists and prefers Python/matplotlib for simple generated diagrams.
- `teacher/diagram-source-rules.md` exists and requires source/license/attribution for external images.
- `teacher/diagram-quality-rules.md` exists and requires axes, labels, source/generator, and diagram index records.
- `assets/diagrams/index.md` exists.
- Curve/model lessons have generated or sourced diagram assets.
- Complex ASCII diagrams are not used as the main explanation for curve/model lessons.
- Diagram assets are listed in `assets/diagrams/index.md`.

Failure keeps `validation_result.passed=false`.

## Learning Control Quality Checklist

- [ ] Learning contract explains L1-L9 and default L6.
- [ ] Concept target levels are present.
- [ ] AI assistance modes are defined and linked to score types.
- [ ] Compact learning-control policy preserves recall, own explanation, misuse checks, and transfer.
- [ ] L6 concepts have misuse-discrimination checks recorded in concept state/evidence ledger.
- [ ] L7 targets have transfer or barehand checks recorded in the evidence ledger.
- [ ] Feedback policy is evidence-anchored.
- [ ] No unsupported mastery claims or pseudo-precise gamification.
