---
type: Trace Document
title: Crash Course Learning OKF Factory Trace
description: Links user requirements to design parameters and implementation files.
tags: [vibe, trace, requirements]
timestamp: 2026-06-30T00:00:00-07:00
---
# TRACE — Requirement to File Links

| Requirement | Design FR | Main files |
|---|---|---|
| URD-REQ-001 Normalize input | ADD-FR-001 | `schemas/factory-input.md`, `playbooks/normalize-factory-input.md`, `factory/course-okf-generation-contract.md` |
| URD-REQ-002 Separate course instance | ADD-FR-002 | `factory/factory-overview.md`, `schemas/course-instance-layout.md`, `tools/materialize_course_okf.py`, `playbooks/generate-new-course-okf.md` |
| URD-REQ-003 Generate required tree | ADD-FR-002 | `schemas/course-instance-layout.md`, `tools/materialize_course_okf.py`, `factory/validation-checklist.md`, `playbooks/validate-generated-course-okf.md` |
| URD-REQ-004 Initialize state | ADD-FR-006 | `schemas/learner-state.md`, `schemas/score-history.md`, `schemas/next-action.md`, `schemas/plan-change.md`, `templates/state-*.md`, `tools/materialize_course_okf.py` |
| URD-REQ-005 Daily 1-hour package | ADD-FR-005 | `templates/daily-work-package.md`, `playbooks/run-daily-session.md` |
| URD-REQ-006 A/B/C priority | ADD-FR-004 | `templates/priority-map.md`, `schemas/topic-ledger.md` |
| URD-REQ-007 Source provenance | ADD-FR-003 | `factory/course-reconnaissance.md`, `schemas/resource-registry.md`, `templates/resources.md` |
| URD-REQ-008 Resume saved state | ADD-FR-007 | `playbooks/resume-course-session.md`, `schemas/next-action.md` |
| URD-REQ-009 Adapt future work | ADD-FR-009 | `playbooks/adapt-remaining-plan.md`, `schemas/plan-change.md`, `templates/state-plan-changes.md` |
| URD-REQ-010 Persist session evidence | ADD-FR-008 | `playbooks/update-state-after-session.md`, `schemas/session-record.md`, `schemas/assessment-event.md` |
| URD-REQ-011 Final review | ADD-FR-010 | `playbooks/generate-final-review.md`, `templates/final-review-pack.md` |
| URD-REQ-012 Validate output | ADD-FR-011 | `schemas/course-okf-output.md`, `factory/validation-checklist.md`, `playbooks/validate-generated-course-okf.md`, `tools/materialize_course_okf.py` |
| URD-REQ-013 Support variants | ADD-FR-001 / ADD-FR-005 | `schemas/factory-input.md`, `templates/seven-day-plan.md` |
| URD-REQ-014 Avoid blind model memory | ADD-FR-003 | `factory/course-reconnaissance.md`, `templates/resources.md` |
| URD-REQ-015 Evaluate content quality | ADD-FR-012 | `schemas/course-okf-quality-report.md`, `playbooks/evaluate-generated-course-okf.md`, `tools/quality_check_course_okf.py` |
| URD-REQ-016 Repair failed output | ADD-FR-013 | `playbooks/repair-generated-course-okf.md`, `tools/course_seed_registry.py`, `tools/materialize_course_okf.py` |
| URD-REQ-017 Split structural/content pass | ADD-FR-011 / ADD-FR-012 / ADD-FR-013 | `schemas/course-okf-output.md`, `validation-report.json`, `tests/test_materialize_course_okf.py` |
| URD-REQ-018 Teacher/student split | ADD-FR-014 | `teacher/teacher-notebook.md`, `teacher/visibility-rules.md`, `tools/materialize_course_okf.py` |
| URD-REQ-019 Prompt leakage prevention | ADD-FR-015 | `tools/lint_prompt_visibility.py`, `playbooks/render-student-prompt.md`, `tools/quality_check_course_okf.py` |
| URD-REQ-020 Teacher notebook | ADD-FR-014 / ADD-FR-015 | `schemas/teacher-notebook.md`, `teacher/teacher-notebook.md` |
| URD-REQ-021 Score type | ADD-FR-016 | `schemas/score-history.md`, `state/score-history.md` |
| URD-REQ-022 Interest-led branches | ADD-FR-017 | `state/interest-ledger.md`, `playbooks/handle-interest-led-branch.md` |
| URD-REQ-023 Soft/strict time policy | ADD-FR-017 | `schemas/factory-input.md`, `teacher/time-policy.md` |
| URD-REQ-024 Engagement maintenance | ADD-FR-018 | `teacher/engagement-monitor.md`, `teacher/engagement-intervention-rules.md` |
| URD-REQ-025 Teaching runtime quality | ADD-FR-019 | `tools/lint_prompt_visibility.py`, `tools/quality_check_course_okf.py` |
| URD-REQ-026 Teaching runtime repair | ADD-FR-019 | `quality-report.json`, `playbooks/repair-generated-course-okf.md` |


## ADD Matrix Status

The ADD matrix is maintained as a decoupled / lower-triangular matrix. Structural validation is traced to ADD-FR-011, content quality evaluation to ADD-FR-012, and repair/recheck to ADD-FR-013. These are final acceptance and repair stages, not direct dependencies of ADD-FR-001 through ADD-FR-010. Round 4 adds ADD-FR-014 through ADD-FR-019 for teaching runtime quality while preserving lower-triangular ordering.

## Round 5 Visual Teaching Trace

| Requirement | Design FR | Main files |
|---|---|---|
| URD-REQ-027 Visual trigger for graph/model lessons | ADD-FR-020 | `schemas/visual-teaching-trigger.md`, `teacher/visual-teaching-policy.md`, `tools/check_diagram_quality.py` |
| URD-REQ-028 Prefer generated diagrams | ADD-FR-022 | `tools/render_diagram_asset.py`, `playbooks/generate-diagram-with-python.md`, `teacher/visual-teaching-policy.md` |
| URD-REQ-029 Authoritative external diagrams | ADD-FR-023 | `playbooks/find-authoritative-diagram.md`, `schemas/external-image-source.md`, `teacher/diagram-source-rules.md` |
| URD-REQ-030 Avoid complex ASCII | ADD-FR-027 | `tools/check_diagram_quality.py`, `teacher/diagram-quality-rules.md` |
| URD-REQ-031 Diagram assets | ADD-FR-024 | `assets/diagrams/index.md`, `schemas/diagram-asset.md`, `tools/materialize_course_okf.py` |
| URD-REQ-032 Axes and visual explanation | ADD-FR-021 / ADD-FR-025 | `teacher/diagram-quality-rules.md`, `playbooks/insert-diagram-in-lesson.md` |
| URD-REQ-033 Inline diagram placement | ADD-FR-025 | `playbooks/insert-diagram-in-lesson.md`, `teacher/visual-teaching-policy.md` |
| URD-REQ-034 Visual quality gate | ADD-FR-027 | `tools/check_diagram_quality.py`, `tools/quality_check_course_okf.py`, `validation-report.json` |

Round 5 adds ADD-FR-020 through ADD-FR-027 for visual teaching while preserving the lower-triangular design principle.

## Darwin Round 6 Trace Additions

- URD-REQ-035..050 -> compact learning-control layer: `learning-contract/index.md`, `teacher/learning-control-policy.md`, `state/concept-mastery-state.md`, `state/assessment-evidence-ledger.md`, `schemas/learning-control.md`, `playbooks/manage-learning-control.md`, `tools/check_learning_stage_evidence.py`.
- Round7 rationale: preserve the learning-stage, AI-diet, verifiability, productive-friction, feedback-anchor, model-vs-reality, negative-feature, barehand, transfer, and assistance-mode requirements while removing duplicate runtime files.


## Round 7 Occam Trace

Round 7 does not remove user-facing learning-control capability. It changes the implementation mapping from many atomic files to four compact runtime files plus one schema and one playbook. Quality gates now test the compact contract instead of individual policy fragments.
