---
type: Playbook
title: Repair Generated Course OKF
description: Repair loop for a generated course OKF that failed post-generation quality evaluation.
tags: [playbook, repair, quality]
timestamp: 2026-06-30T00:00:00-07:00
---
# Trigger

Run when `Evaluate Generated Course OKF` returns `passed: false`.

# Rule

Never mark the course OKF as return-ready immediately after a failed quality report. Repair the failed files, then rerun the quality gate.

# Procedure

1. Read `quality-report.json` or the quality gate result inside `generation-output.json`.
2. Group failures by file path.
3. Repair only the failed files unless a dependency requires a related file to change.
4. Use this repair order:
   1. `course-map.md`
   2. `priority-map.md`
   3. `glossary.md`
   4. `plan/seven-day-plan.md`
   5. `plan/day-1.md`
   6. `quizzes/day-1-quiz.md`
   7. final-review files
   8. state files
5. For each repaired content file, include:
   - course-specific topics;
   - A/B/C exam-value reasoning when relevant;
   - examples, counterexamples, or easy confusions;
   - exam-style prompts or scoring where relevant.
6. Rerun `Evaluate Generated Course OKF`.
7. If the result passes, update `generation-output.json` so `validation_result.passed` is true.
8. If the result still fails, keep `validation_result.passed=false` and return exact remaining failures and repair actions.

# Local MVP Behavior

`tools/materialize_course_okf.py` runs one deterministic repair attempt when a local course seed exists in `tools/course_seed_registry.py`.

For example, the macroeconomics seed repairs generic files by writing:

```text
course-map.md
priority-map.md
glossary.md
plan/seven-day-plan.md
plan/day-N.md
quizzes/day-N-quiz.md
final-review/compressed-notes.md
final-review/must-know-list.md
final-review/answer-templates.md
final-review/mock-exam.md
```

Unknown courses do not get a fake pass. They remain quality-failed until a human or AI fills course-specific content using course materials or reconnaissance.

# Failure Handling

| Failure | Repair action |
|---|---|
| `placeholder_content` | Replace the placeholder with course-specific content. |
| `insufficient_course_specific_terms` | Add a course term bank and propagate terms into maps, plans, quizzes, and final review. |
| `day1_not_runnable` | Rewrite Day 1 as a concrete 60-minute work package. |
| `quiz_missing_exam_items` | Add term explanation, short answer, comparison, and scoring bands. |
| `mock_exam_not_exam_like` | Create a scored mock exam near the target-score level. |
| Unknown course has no seed | Use course materials or reconnaissance; do not pass automatically. |
