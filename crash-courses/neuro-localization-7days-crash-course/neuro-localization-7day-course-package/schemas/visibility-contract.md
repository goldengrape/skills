---
type: Schema
title: Visibility Contract
description: Rules for student and teacher material separation.
tags: [schema, visibility]
timestamp: 2026-07-07T07:38:01+00:00
---

# Visibility Contract

## Student-Visible Before Answer

Can show: learning goal, short concept map, case stem, question, allowed time, and answer format.

Cannot show: teacher private material, expected reasoning, point allocation, model response, common mistakes list, or remediation target.

## After Learner Answer

Can show: correctness judgment, evidence-based feedback, missed distinctions, corrected reasoning, and next practice.

## File Separation

- Student files: `plan/day-N.md`, `quizzes/day-N-quiz.md`, selected `final-review/` files.
- Teacher private files: `teacher/rubrics/`, `teacher/answer-keys/`, `teacher/teacher-notebook.md`.

## Rule

If a file is used to ask the learner a question, it must not include hidden teacher material for that question.
