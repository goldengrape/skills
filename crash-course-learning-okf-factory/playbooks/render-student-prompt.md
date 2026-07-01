---
type: Playbook
title: Render Student Prompt
description: Render only student-visible teaching text while keeping teacher-private scoring material hidden until after the learner answers.
tags: [playbook, teaching-runtime, visibility]
timestamp: 2026-06-30T00:00:00-07:00
---
# Render Student Prompt

## Trigger

Use before any quiz, Feynman task, short answer, essay outline, or mock-exam item.

## Procedure

1. Read the relevant `plan/day-N.md` or `quizzes/day-N-quiz.md`.
2. Write the hidden task goal, expected answer elements, and scoring rule into `teacher/teacher-notebook.md`.
3. Render only `teacher_says` into the conversation.
4. Do not show expected answer elements, answer keys, rubrics, or reference answers before the learner answers.
5. After the learner answers, read the private rubric or answer key and give feedback.
6. Record `score_type` and `prompt_visibility` in `state/score-history.md`.

## Student Prompt May Include

- Question.
- Length or time limit.
- Output format.
- Whether notes are allowed.

## Student Prompt Must Not Include Before Answer

- Answer elements.
- Scoring criteria specific to the task.
- Reference answer or standard answer.
- “At least mention A/B/C/D” style lists.

## Score Type Rule

If hidden answer elements were shown before the learner answered, record `assisted_score`, not `blind_score`.
