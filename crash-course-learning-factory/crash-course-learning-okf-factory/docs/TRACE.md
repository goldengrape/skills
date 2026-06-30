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


## ADD Matrix Status

The ADD matrix is maintained as a decoupled / lower-triangular matrix. Structural validation is traced to ADD-FR-011, content quality evaluation to ADD-FR-012, and repair/recheck to ADD-FR-013. These are final acceptance and repair stages, not direct dependencies of ADD-FR-001 through ADD-FR-010.
