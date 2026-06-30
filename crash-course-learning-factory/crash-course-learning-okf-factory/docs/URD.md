---
type: User Requirement Document
title: Crash Course Learning OKF Factory URD
description: User requirements for a reusable, stateful OKF generator for short exam preparation.
tags: [vibe, urd, requirements, factory]
timestamp: 2026-06-30T00:00:00-07:00
---

# URD — Crash Course Learning OKF Factory

## Purpose

This project is a **meta-factory**. It does not store one fixed course. It generates a new, course-specific **Course Learning OKF** for short university exam preparation.

The default use case is: a learner has about one week, about one hour per day, and wants a pass-level result around 60 points in a concept-heavy humanities or social-science course.

## Roles

| ID | Role | Description |
|---|---|---|
| URD-ROLE-001 | Learner | The person preparing for an exam with limited time. |
| URD-ROLE-002 | Factory agent | The AI or tool that reads factory files and generates a course-specific OKF instance. |
| URD-ROLE-003 | Session agent | The AI or tool that resumes a generated OKF, runs daily sessions, updates state, and adapts future work. |
| URD-ROLE-004 | Reviewer | A human or AI checking whether a generated course OKF is complete and usable. |

## Goals

| ID | Goal |
|---|---|
| URD-GOAL-001 | Generate a fresh Course Learning OKF from course name, baseline, exam target, available time, and materials. |
| URD-GOAL-002 | Optimize for short-term pass-level exam readiness, not full subject mastery. |
| URD-GOAL-003 | Save learner state in files so future sessions can resume without relying on model memory. |
| URD-GOAL-004 | Use provided materials and recorded source confidence before relying on generic model knowledge. |
| URD-GOAL-005 | Adapt the remaining plan when quiz, recall, or answer evidence shows the learner is behind, confused, or ready to advance. |

## Functional Requirements

| ID | Requirement | Success condition |
|---|---|---|
| URD-REQ-001 | Normalize input into a stable factory input contract. | Missing non-critical fields receive defaults and assumptions are recorded in `mission.md`. |
| URD-REQ-002 | Treat each course as a separate generated OKF instance. | Output path is `course-okf-{course-slug}/`; no course notes are written into the factory itself. |
| URD-REQ-003 | Generate the required file tree. | The generated instance contains mission, map, resources, priority map, plan, state, sessions, learning records, quizzes, and final review files. |
| URD-REQ-004 | Initialize learner state. | `state/current-state.md`, `topic-ledger.md`, `recall-deck.md`, `misconceptions.md`, `score-history.md`, `next-action.md`, and `plan-changes.md` are created. |
| URD-REQ-005 | Build a daily work package that fits the configured time. | Default package totals 60 minutes and includes retrieval, map, explanation, Feynman task, exam practice, feedback, and state update. |
| URD-REQ-006 | Prioritize topics by exam value. | `priority-map.md` separates A/B/C topics and explains why each item belongs there. |
| URD-REQ-007 | Record source provenance and gaps. | `resources.md` records source type, priority, confidence, and source gaps. |
| URD-REQ-008 | Support recovery from saved state. | Resume flow reads state, recall deck, misconceptions, score history, latest session, and next plan before teaching. |
| URD-REQ-009 | Adapt future work based on evidence. | Weak A-topics, unresolved misconceptions, missed recall cards, low mock score, or changed constraints trigger plan repair. |
| URD-REQ-010 | Persist session evidence. | Every session creates a session record and updates relevant state files. |
| URD-REQ-011 | Generate final review materials. | Final review includes compressed notes, must-know list, answer templates, and 60-point mock exam. |
| URD-REQ-012 | Validate generated instances. | Factory output includes created files, initial state, entrypoint, resume rules, state update rules, and validation result. |
| URD-REQ-013 | Support course and exam variants without bloating the MVP. | Input accepts `course_type`, `exam_format`, `days_available`, and `daily_minutes`; default behavior remains seven days and one hour per day. |
| URD-REQ-014 | Avoid blind model-memory generation when materials exist. | User-provided materials outrank public or generic sources in reconnaissance and priority decisions. |
| URD-REQ-015 | Evaluate generated course OKF content quality after structural generation. | Validation fails if critical files are placeholders, generic, not course-specific, or not exam-ready. |
| URD-REQ-016 | Repair failed generated course OKF output before returning it as usable. | Failed quality reports produce repair actions; after repair the quality gate is rerun and result is recorded. |
| URD-REQ-017 | Distinguish structural pass from course-content pass. | Output contains both structural validation and content quality gate results; `passed=true` requires both. |

## Constraints

| ID | Constraint |
|---|---|
| URD-CON-001 | Default target is pass-level / 60-point exam readiness. |
| URD-CON-002 | Default time budget is seven days, 60 minutes per day. |
| URD-CON-003 | Primary course family is concept-heavy humanities and social-science courses. |
| URD-CON-004 | MVP does not promise high scores, full mastery, or long-term disciplinary training. |
| URD-CON-005 | Generated state must be stored in OKF files, not in the AI model's unstated memory. |
| URD-CON-006 | The factory must remain modular; future variants should be added through schemas, templates, and playbooks rather than one giant prompt. |
| URD-CON-007 | File existence is not sufficient for validation; content quality must be checked separately. |
| URD-CON-008 | Unknown courses without local seed content may be structurally generated, but must remain quality-failed until filled from materials or reviewed by AI/human. |

## Out of Scope for MVP

| ID | Out-of-scope item |
|---|---|
| URD-OOS-001 | Full textbook reading plans. |
| URD-OOS-002 | High-score exam coaching. |
| URD-OOS-003 | Math, physics, chemistry, programming, or other long problem-set based courses as the primary target. |
| URD-OOS-004 | Automatic grading that claims to predict a real exam score precisely. |
| URD-OOS-005 | LMS integration, calendar integration, account login, payment, or multi-user classroom management. |

## Acceptance Criteria

| ID | Acceptance criterion |
|---|---|
| URD-AC-001 | Given `管理学 / zero / 7 days / 60 minutes / target_score 60`, the factory can generate a complete `course-okf-management-pass/` instance. |
| URD-AC-002 | A generated instance can resume from Day 3 after a failed quiz and choose repair/review instead of mechanically entering Day 4. |
| URD-AC-003 | A daily package clearly fits the configured minute budget. |
| URD-AC-004 | Every state-changing session has a session record and score-history entry. |
| URD-AC-005 | A/B/C priorities are visible and affect the plan. |
| URD-AC-006 | The final day can produce compressed notes, must-know list, answer templates, and a 60-point mock exam. |
| URD-AC-007 | Validation reports missing files, missing state files, missing resume rules, and missing source gaps instead of silently passing. |
| URD-AC-008 | MVP local materialization can create the required course OKF skeleton and initial state from a normalized input. |
| URD-AC-009 | Given `宏观经济学 / zero / 7 days / 60 minutes / target_score 60`, the factory detects a generic skeleton as not quality-ready, repairs it with macroeconomics seed content when available, and reruns the quality gate. |
| URD-AC-010 | A generated course OKF with unresolved placeholders in `course-map.md`, `priority-map.md`, daily quizzes, or final-review files cannot return `validation_result.passed=true`. |

## Open Questions

| ID | Question | Default until answered |
|---|---|---|
| URD-Q-001 | Should the generated instance use Chinese, English, or course-language defaults? | Use the user's answer language when known; otherwise record the assumption in `mission.md`. |
| URD-Q-002 | Should the 3-day and 14-day variants be separate playbooks or parameters in one playbook? | MVP keeps one playbook parameterized by `days_available`. |
