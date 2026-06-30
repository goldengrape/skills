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
| ADD-FR-005 | Build a time-boxed plan and daily work packages. | ADD-DP-005 | `templates/seven-day-plan.md`, `templates/daily-work-package.md`, and quiz templates. |
| ADD-FR-006 | Persist learner state across sessions. | ADD-DP-006 | State schemas and templates plus materializer initialization for current state, topic ledger, recall deck, misconceptions, score history, next action, and plan changes. |
| ADD-FR-007 | Resume from the correct next step. | ADD-DP-007 | `playbooks/resume-course-session.md` and `state/next-action.md`. |
| ADD-FR-008 | Update state after learning evidence. | ADD-DP-008 | `playbooks/update-state-after-session.md`, session records, assessment events. |
| ADD-FR-009 | Adapt the remaining plan when evidence requires it. | ADD-DP-009 | `playbooks/adapt-remaining-plan.md` and `schemas/plan-change.md`. |
| ADD-FR-010 | Generate final review materials. | ADD-DP-010 | `playbooks/generate-final-review.md` and `templates/final-review-pack.md`. |
| ADD-FR-011 | Validate generated OKF structure and output contract. | ADD-DP-011 | `factory/validation-checklist.md`, `playbooks/validate-generated-course-okf.md`, `schemas/course-okf-output.md`, and structural validation output. |
| ADD-FR-012 | Evaluate generated course OKF content quality. | ADD-DP-012 | `schemas/course-okf-quality-report.md`, `playbooks/evaluate-generated-course-okf.md`, and `tools/quality_check_course_okf.py`. |
| ADD-FR-013 | Repair failed course OKF content and rerun quality checks. | ADD-DP-013 | `playbooks/repair-generated-course-okf.md`, `tools/course_seed_registry.py`, and the materializer quality-repair loop. |

## Design Matrix

Rows are FRs. Columns are DPs. `X` means the DP directly satisfies the FR. `x` means a permitted prior dependency.

The matrix is ordered so dependencies flow only from earlier DPs to later FRs. This keeps the design **decoupled / lower triangular**. No earlier FR depends on a later DP.

| FR \ DP | DP1 Input | DP2 Layout | DP3 Sources | DP4 Priority | DP5 Plan | DP6 State | DP7 Resume | DP8 Update | DP9 Adapt | DP10 Final | DP11 Structure Validate | DP12 Quality Evaluate | DP13 Repair Loop |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FR1 Normalize input | X |  |  |  |  |  |  |  |  |  |  |  |  |
| FR2 Emit layout | x | X |  |  |  |  |  |  |  |  |  |  |  |
| FR3 Source reconnaissance | x |  | X |  |  |  |  |  |  |  |  |  |  |
| FR4 Priority classification |  |  | x | X |  |  |  |  |  |  |  |  |  |
| FR5 Time-boxed plan | x |  |  | x | X |  |  |  |  |  |  |  |  |
| FR6 Persist state |  | x |  | x |  | X |  |  |  |  |  |  |  |
| FR7 Resume |  |  |  |  | x | x | X |  |  |  |  |  |  |
| FR8 Update state |  |  |  |  |  | x |  | X |  |  |  |  |  |
| FR9 Adapt plan |  |  |  | x | x | x |  | x | X |  |  |  |  |
| FR10 Final review |  |  |  | x |  | x |  |  |  | X |  |  |  |
| FR11 Structure validation | x | x | x | x | x | x | x | x | x | x | X |  |  |
| FR12 Quality evaluation | x | x | x | x | x | x |  |  |  | x | x | X |  |
| FR13 Repair and recheck | x | x | x | x | x | x |  |  |  | x | x | x | X |

## Matrix Interpretation

The design is **decoupled / lower triangular**, not fully uncoupled.

This means:

1. Each FR has one primary DP.
2. Later FRs may depend on earlier DPs.
3. Earlier FRs do not depend on later DPs.
4. Structural validation is not enough; content quality is a separate later FR.
5. Repair is later than quality evaluation, because repair must be driven by explicit failures.

Execution order:

1. Normalize input.
2. Create or materialize the instance layout.
3. Run reconnaissance.
4. Build A/B/C priority map.
5. Generate plan, daily packages, quizzes, and initial final-review materials.
6. Initialize state.
7. Fill course-specific content from resources, priority decisions, or course seeds.
8. Run structural validation.
9. Run content quality evaluation.
10. If quality fails, repair the failed files and rerun quality evaluation.
11. Return the bundle only with a passed validation result, or return a failed report with exact repair actions.

For local MVP execution, `tools/materialize_course_okf.py` performs layout creation, initial state creation, structural validation, quality evaluation, and one deterministic repair attempt using `tools/course_seed_registry.py`. Unknown courses are not silently accepted; they receive a failed quality report until course-specific content is supplied.

## Quality Gate Split

| Layer | What it checks | Example failure from macroeconomics test | Repair response |
|---|---|---|---|
| Structural validation | Required files and state files exist. | No structural failure. | None. |
| Content quality evaluation | Critical files are course-specific, exam-ready, and not placeholders. | `course-map.md`, `priority-map.md`, quizzes, and final-review files were generic placeholders. | Rewrite those files with macroeconomics topics, terms, questions, and mock exam items. |
| Repair loop | Failed files are revised, then checked again. | Previous versions stopped after generation. | Materializer applies known course seed when available; playbook requires AI/human repair otherwise. |

## Matrix Revision Notes

The previous version treated `validation_result.passed` as enough when required files existed. The macroeconomics test showed that this creates a false pass: a generated instance can be structurally complete but educationally unusable.

This revision keeps the matrix lower triangular by adding two later FRs:

| New FR | Reason |
|---|---|
| ADD-FR-012 Quality evaluation | Checks content readiness after structure exists. |
| ADD-FR-013 Repair and recheck | Uses the quality report to revise failed files, then reruns the quality gate. |

No earlier FR depends on ADD-DP-012 or ADD-DP-013. The quality gate reads generated files; it does not change the input contract, layout contract, state schema, or daily-session rules.

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
| One-hour plan becomes too large. | Daily package template requires minute budget and topic limits. |
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
