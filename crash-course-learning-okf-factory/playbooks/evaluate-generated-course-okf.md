---
type: Playbook
title: Evaluate Generated Course OKF
description: Post-generation content quality gate for a generated course-specific OKF.
tags: [playbook, quality, validation]
timestamp: 2026-06-30T00:00:00-07:00
---
# Trigger

Run after the required Course Learning OKF files have been generated and structural validation has passed.

# Purpose

Do not treat file existence as success. A generated course OKF must also be course-specific, exam-ready, and immediately runnable.

# Procedure

1. Read the generated `generation-output.json` if present.
2. Read critical files:
   - `course-map.md`
   - `priority-map.md`
   - `glossary.md`
   - `plan/seven-day-plan.md`
   - `plan/day-1.md`
   - `quizzes/day-1-quiz.md`
   - `final-review/must-know-list.md`
   - `final-review/mock-exam.md`
   - `state/current-state.md`
   - `state/next-action.md`
   - `state/score-history.md`
3. Fail the quality gate if unresolved placeholders remain, including `TBD`, `Fill this`, `placeholder`, or generic prompts such as `今日 A 类概念`.
4. Check course specificity:
   - For known local course seeds, require visible course terms in the critical files.
   - For unknown courses, require AI/human review using `resources.md` and `course-reconnaissance.md` before passing quality.
5. Check exam readiness:
   - `priority-map.md` has A/B/C topics with exam-value reasons.
   - `plan/day-1.md` includes retrieval, course map, core explanation, Feynman task, exam practice, feedback, and state update.
   - `quizzes/day-1-quiz.md` includes term explanation and short-answer or comparison tasks.
   - `final-review/mock-exam.md` is scored or clearly exam-like.
6. Check recoverability:
   - `state/next-action.md` has a parseable `next_action`.
   - `state/score-history.md` can record assessment events.
7. Write a report using `schemas/course-okf-quality-report.md`.

# Local MVP Command

```bash
python tools/quality_check_course_okf.py ./out/course-okf-macroeconomics-pass --output-json ./out/course-okf-macroeconomics-pass/quality-report.json
```

# Output

```yaml
quality_gate:
  passed: false
  score: 52
  failures:
    - code: placeholder_content
      path: priority-map.md
      message: Unresolved placeholder markers remain.
  repair_actions:
    - Rewrite priority-map.md with course-specific A/B/C topics and exam-value reasons.
```
