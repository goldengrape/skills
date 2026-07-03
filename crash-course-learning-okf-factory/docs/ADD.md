---
type: Axiomatic Design Document
title: Crash Course Learning OKF Factory ADD
description: Functional decomposition, design parameters, execution order, and coupling notes for the factory.
tags: [vibe, add, axiomatic-design, factory]
timestamp: 2026-06-30T00:00:00-07:00
---

# ADD — Design Split

## Design Goal

Split the factory into small, readable parts so an AI or local helper can generate, resume, update, evaluate, repair, and return a Course Learning OKF without mixing course content, learner state, factory rules, and quality gates.

## Design Conclusion

| Item | Result |
|---|---|
| Matrix type | Decoupled / lower triangular |
| Main revision in this round | Split post-generation quality from structural validation, then add a repair-and-recheck step. |
| Reason | The macroeconomics test showed that file-existence validation can pass while the generated course OKF is still a generic skeleton. |
| Guard | A generated course OKF is not return-ready unless structural validation and course-content quality both pass, or the failure report lists exact repair actions. |

## Functional Requirements and Design Parameters

| FR ID | Functional Requirement | DP ID | Design Parameter |
|---|---|---|---|
| ADD-FR-001 | Normalize learner request and defaults. | ADD-DP-001 | `schemas/factory-input.md` and `playbooks/normalize-factory-input.md`. |
| ADD-FR-002 | Emit one complete course-instance file tree. | ADD-DP-002 | `schemas/course-instance-layout.md`, course-instance templates, and `tools/materialize_course_okf.py`. |
| ADD-FR-003 | Gather course sources and mark confidence. | ADD-DP-003 | `factory/course-reconnaissance.md` and `templates/resources.md`. |
| ADD-FR-004 | Classify topics by exam value. | ADD-DP-004 | `templates/priority-map.md` and topic-priority rules. |
| ADD-FR-005 | Build a time-planned daily work package. | ADD-DP-005 | `templates/seven-day-plan.md`, `templates/daily-work-package.md`, and quiz templates. |
| ADD-FR-006 | Persist learner state across sessions. | ADD-DP-006 | State schemas and templates plus materializer initialization for state files. |
| ADD-FR-007 | Resume from the correct next step. | ADD-DP-007 | `playbooks/resume-course-session.md` and `state/next-action.md`. |
| ADD-FR-008 | Update state after learning evidence. | ADD-DP-008 | `playbooks/update-state-after-session.md`, session records, assessment events. |
| ADD-FR-009 | Adapt the remaining plan when evidence requires it. | ADD-DP-009 | `playbooks/adapt-remaining-plan.md` and `schemas/plan-change.md`. |
| ADD-FR-010 | Generate final review materials. | ADD-DP-010 | `playbooks/generate-final-review.md` and `templates/final-review-pack.md`. |
| ADD-FR-011 | Validate generated OKF structure and output contract. | ADD-DP-011 | `factory/validation-checklist.md`, `playbooks/validate-generated-course-okf.md`, `schemas/course-okf-output.md`, and structural validation output. |
| ADD-FR-012 | Evaluate generated course OKF content quality. | ADD-DP-012 | `schemas/course-okf-quality-report.md`, `playbooks/evaluate-generated-course-okf.md`, and `tools/quality_check_course_okf.py`. |
| ADD-FR-013 | Repair failed course OKF content and rerun quality checks. | ADD-DP-013 | `playbooks/repair-generated-course-okf.md`, `tools/course_seed_registry.py`, and the materializer quality-repair loop. |
| ADD-FR-014 | Separate teacher-private planning from student-visible teaching. | ADD-DP-014 | `teacher/` runtime directory, `schemas/teacher-notebook.md`, `schemas/visibility-policy.md`, and generated visibility rules. |
| ADD-FR-015 | Prevent pre-answer prompt leakage. | ADD-DP-015 | `playbooks/render-student-prompt.md` and `tools/lint_prompt_visibility.py`. |
| ADD-FR-016 | Record score type and prompt visibility. | ADD-DP-016 | Expanded `schemas/score-history.md` and score-history template. |
| ADD-FR-017 | Support interest-led branches under soft time policy. | ADD-DP-017 | `state/interest-ledger.md`, `teacher/time-policy.md`, and `playbooks/handle-interest-led-branch.md`. |
| ADD-FR-018 | Maintain interest and recover attention using observable signals. | ADD-DP-018 | `teacher/engagement-monitor.md` and `teacher/engagement-intervention-rules.md`. |
| ADD-FR-019 | Evaluate teaching runtime quality. | ADD-DP-019 | Teaching runtime section of `tools/quality_check_course_okf.py` and `tools/lint_prompt_visibility.py`. |

## Design Matrix

Rows are FRs. Columns are DPs. `X` means the DP directly satisfies the FR. `x` means a permitted prior dependency.

The matrix remains **decoupled / lower triangular**: later FRs may read earlier DPs, but no earlier FR depends on a later DP.

| FR \ DP | DP1 | DP2 | DP3 | DP4 | DP5 | DP6 | DP7 | DP8 | DP9 | DP10 | DP11 | DP12 | DP13 | DP14 | DP15 | DP16 | DP17 | DP18 | DP19 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FR1 Normalize input | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR2 Emit layout | x | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR3 Source reconnaissance | x |  | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR4 Priority classification |  |  | x | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR5 Daily package | x |  |  | x | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR6 Persist state |  | x |  | x |  | X |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR7 Resume |  |  |  |  | x | x | X |  |  |  |  |  |  |  |  |  |  |  |  |
| FR8 Update state |  |  |  |  |  | x |  | X |  |  |  |  |  |  |  |  |  |  |  |
| FR9 Adapt plan |  |  |  | x | x | x |  | x | X |  |  |  |  |  |  |  |  |  |  |
| FR10 Final review |  |  |  | x |  | x |  |  |  | X |  |  |  |  |  |  |  |  |  |
| FR11 Structure validation | x | x | x | x | x | x | x | x | x | x | X |  |  |  |  |  |  |  |  |
| FR12 Content quality | x | x | x | x | x | x |  |  |  | x | x | X |  |  |  |  |  |  |  |
| FR13 Repair and recheck | x | x | x | x | x | x |  |  |  | x | x | x | X |  |  |  |  |  |  |
| FR14 Teacher/student split | x | x |  |  |  | x |  | x |  |  |  |  |  | X |  |  |  |  |  |
| FR15 Prompt leakage prevention | x | x |  |  | x |  |  |  |  |  |  |  |  | x | X |  |  |  |  |
| FR16 Score type recording |  |  |  |  |  | x |  | x |  |  |  |  |  | x | x | X |  |  |  |
| FR17 Interest-led branches | x |  |  | x | x | x |  | x |  |  |  |  |  | x |  |  | X |  |  |
| FR18 Engagement handling |  |  |  |  | x | x |  | x |  |  |  |  |  | x |  |  | x | X |  |
| FR19 Teaching runtime quality | x | x |  |  | x | x |  | x |  |  | x | x |  | x | x | x | x | x | X |

## Matrix Interpretation

The design is **decoupled / lower triangular**, not fully uncoupled.

This revision adds a teaching-runtime layer after content quality. The layer checks whether the generated course OKF can be run as a fair teaching interaction: teacher-private notes are separated from student-visible prompts, answer elements are not leaked before assessment, score types are recorded, interest-led branches are supported, and engagement handling uses observable signals.

Execution order:

1. Normalize input.
2. Create or materialize the instance layout.
3. Run reconnaissance.
4. Build A/B/C priority map.
5. Generate plan, daily packages, quizzes, and initial final-review materials.
6. Initialize state.
7. Fill course-specific content from resources, priority decisions, or course seeds.
8. Generate teacher runtime files.
9. Run structural validation.
10. Run content quality evaluation.
11. If content quality fails, repair the failed files and rerun quality evaluation.
12. Run teaching runtime quality checks.
13. Return the bundle only with all required gates passed, or return a failed report with exact repair actions.

## Quality Gate Split

| Layer | What it checks | Example failure | Repair response |
|---|---|---|---|
| Structural validation | Required files and state files exist. | Missing `teacher/teacher-notebook.md`. | Create missing runtime file. |
| Content quality evaluation | Critical files are course-specific, exam-ready, and not placeholders. | Generic `course-map.md`. | Rewrite with course-specific topics. |
| Repair loop | Failed content files are revised, then checked again. | Skeleton macroeconomics files. | Apply course seed or AI/human repair. |
| Teaching runtime quality | Prompt visibility, teacher notebook, score type, time policy, interest handling, engagement rules. | Student prompt reveals “at least mention these points”. | Move hidden elements to `teacher/rubrics/` or `teacher/teacher-notebook.md`. |

## Matrix Revision Notes

The Day 1 macroeconomics session showed a new class of failure: the course content can be educationally useful while the teaching prompt still leaks scoring criteria before the learner answers. This revision treats that as a teaching-runtime quality failure, not merely a style issue.

## Accepted Coupling


| ID | Coupling | Why accepted | Guard |
|---|---|---|---|
| ADD-COUP-001 | Priority map depends on reconnaissance. | Topic priority cannot be assigned without course/source evidence. | `resources.md` records source confidence and source gaps. |
| ADD-COUP-002 | Daily plan depends on priority map. | A/B/C classification controls what fits into one hour. | Quality evaluation checks daily work references course-specific topics. |
| ADD-COUP-003 | Resume depends on state and latest session records. | Recovery requires both canonical state and recent evidence. | Resume playbook has a fixed read order. |
| ADD-COUP-004 | Adaptation changes future plan and state. | Plan repair is the core behavior when the learner struggles. | Plan changes are recorded in `state/plan-changes.md`. |
| ADD-COUP-005 | Repair depends on quality evaluation. | Repair should be driven by exact failures, not guesswork. | `quality-report.json` must list failures and repair actions. |

## Failure Modes and Design Responses

| Failure mode | Design response |
|---|---|
| Factory emits only a learning plan, not an OKF instance. | Structural validation requires the full file tree and output contract. |
| Factory emits complete files that are still generic placeholders. | Quality evaluation fails `placeholder_content` and blocks return-ready status. |
| Generated course OKF lacks course-specific terms. | Quality evaluation checks known course term banks or requires AI/human review from materials. |
| Day 1 exists but is not runnable. | Quality evaluation checks retrieval, Feynman task, exam practice, and state update markers. |
| Mock exam exists but is not exam-like. | Quality evaluation checks for scored mock-exam structure. |
| Quality fails but factory returns anyway. | Repair playbook requires revise-and-recheck; output remains `passed: false` if still failing. |
| Agent skips state and continues mechanically. | Resume and daily-session playbooks require state read order before teaching. |
| User materials exist but generic knowledge dominates. | Reconnaissance source priority and `resources.md` confidence fields. |
| Learner-led interest extends beyond planned minutes. | Under `time_policy: soft`, continue when useful and record the branch; under `strict`, answer briefly and return to plan. |
| Misconception is shown once but not repaired. | Misconception schema requires retest before `resolved`. |
| Adaptation is invisible. | `state/plan-changes.md` records reason, evidence, and changed files. |

## Trace Summary

| URD requirement | ADD FR | Main files |
|---|---|---|
| URD-REQ-001 | ADD-FR-001 | `schemas/factory-input.md`, `playbooks/normalize-factory-input.md` |
| URD-REQ-003 | ADD-FR-002 | `schemas/course-instance-layout.md`, `tools/materialize_course_okf.py` |
| URD-REQ-007 | ADD-FR-003 | `factory/course-reconnaissance.md`, `templates/resources.md` |
| URD-REQ-006 | ADD-FR-004 | `templates/priority-map.md` |
| URD-REQ-005 | ADD-FR-005 | `templates/daily-work-package.md` |
| URD-REQ-004 | ADD-FR-006 | state schemas and templates |
| URD-REQ-008 | ADD-FR-007 | `playbooks/resume-course-session.md` |
| URD-REQ-010 | ADD-FR-008 | `playbooks/update-state-after-session.md` |
| URD-REQ-009 | ADD-FR-009 | `playbooks/adapt-remaining-plan.md` |
| URD-REQ-011 | ADD-FR-010 | `playbooks/generate-final-review.md` |
| URD-REQ-012 | ADD-FR-011 | `factory/validation-checklist.md`, `schemas/course-okf-output.md` |
| URD-REQ-015 | ADD-FR-012 | `schemas/course-okf-quality-report.md`, `playbooks/evaluate-generated-course-okf.md`, `tools/quality_check_course_okf.py` |
| URD-REQ-016 | ADD-FR-013 | `playbooks/repair-generated-course-okf.md`, `tools/course_seed_registry.py` |
| URD-REQ-018 | ADD-FR-014 | `schemas/teacher-notebook.md`, `schemas/visibility-policy.md`, `tools/materialize_course_okf.py` |
| URD-REQ-019 | ADD-FR-015 | `playbooks/render-student-prompt.md`, `tools/lint_prompt_visibility.py` |
| URD-REQ-021 | ADD-FR-016 | `schemas/score-history.md` |
| URD-REQ-022 / 023 | ADD-FR-017 | `schemas/interest-ledger.md`, `playbooks/handle-interest-led-branch.md` |
| URD-REQ-024 | ADD-FR-018 | `teacher/engagement-monitor.md`, `teacher/engagement-intervention-rules.md` |
| URD-REQ-025 / 026 | ADD-FR-019 | `tools/quality_check_course_okf.py`, `tools/lint_prompt_visibility.py` |

## Round 5 Visual Teaching Extension

| FR | Functional Requirement | DP | Design Parameter |
|---|---|---|---|
| ADD-FR-020 | Detect concepts that require visual teaching. | ADD-DP-020 | `schemas/visual-teaching-trigger.md` and visual trigger rules in course plans. |
| ADD-FR-021 | Define image generation/source priority. | ADD-DP-021 | `teacher/visual-teaching-policy.md` and `teacher/diagram-source-rules.md`. |
| ADD-FR-022 | Generate simple reusable diagrams when supported. | ADD-DP-022 | `tools/render_diagram_asset.py` and `playbooks/generate-diagram-with-python.md`. |
| ADD-FR-023 | Source complex diagrams from authoritative open materials. | ADD-DP-023 | `playbooks/find-authoritative-diagram.md` and `schemas/external-image-source.md`. |
| ADD-FR-024 | Persist diagrams as reusable course assets. | ADD-DP-024 | `assets/diagrams/`, `assets/diagrams/index.md`, and `schemas/diagram-asset.md`. |
| ADD-FR-025 | Insert diagrams into lessons near the explanation. | ADD-DP-025 | `playbooks/insert-diagram-in-lesson.md` and `playbooks/update-diagram-index.md`. |
| ADD-FR-026 | Recover from diagram-generation failure without empty responses. | ADD-DP-026 | `playbooks/diagram-failure-recovery.md`. |
| ADD-FR-027 | Evaluate visual teaching quality. | ADD-DP-027 | `tools/check_diagram_quality.py` and the visual section of `tools/quality_check_course_okf.py`. |

### Visual Matrix Fragment

The visual extension remains lower triangular:

```text
FR20 -> DP20
FR21 -> DP20, DP21
FR22 -> DP20, DP21, DP22
FR23 -> DP20, DP21, DP23
FR24 -> DP22, DP23, DP24
FR25 -> DP24, DP25
FR26 -> DP21, DP22, DP23, DP26
FR27 -> DP20, DP21, DP22, DP23, DP24, DP25, DP26, DP27
```

Earlier factory functions do not depend on the visual quality gate. Visual quality is checked after generation and any deterministic seed repair.
