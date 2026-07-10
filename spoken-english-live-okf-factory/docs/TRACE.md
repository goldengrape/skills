---
type: Traceability Map
title: Spoken English Live OKF Factory Trace
description: Trace links from user requirements to design parameters, artifacts, and checks.
tags: [trace, requirements, design]
timestamp: 2026-07-09T20:45:00-07:00
---

# TRACE — Spoken English Live OKF Factory

| URD requirement | ADD FR | ADD DP | Authoritative artifact | Validation evidence |
|---|---|---|---|---|
| URD-REQ-001 | ADD-FR-001 | ADD-DP-001 | `contracts/cycle-evidence-contract.md` | Input normalization checks in `playbooks/validate-cycle-pack.md` |
| URD-REQ-002 | ADD-FR-002, ADD-FR-003 | ADD-DP-002, ADD-DP-003 | `playbooks/derive-cycle-blueprint.md`, `schemas/course-pack-layout.md`, `playbooks/materialize-cycle-pack.md` | Cycle and daily-plan checks |
| URD-REQ-003 | ADD-FR-003, ADD-FR-004 | ADD-DP-003, ADD-DP-004 | `runtime/live-session-protocol.md` and generated `teacher/live-session-settings.md` | Live suitability checks |
| URD-REQ-004 | ADD-FR-004 | ADD-DP-004 | `runtime/live-session-protocol.md` | Interruption and correction checks |
| URD-REQ-005 | ADD-FR-005 | ADD-DP-005 | `playbooks/close-live-session.md`, `templates/session-record-template.md` | Session closeout checks |
| URD-REQ-006 | ADD-FR-001, ADD-FR-005, ADD-FR-006 | ADD-DP-001, ADD-DP-005, ADD-DP-006 | evidence contract, closeout, rollover | Continuity citation checks |
| URD-REQ-007 | ADD-FR-002, ADD-FR-006 | ADD-DP-002, ADD-DP-006 | blueprint and rollover playbooks | Carry-over and next-cycle checks |
| URD-REQ-008 | ADD-FR-007 | ADD-DP-007 | `playbooks/validate-cycle-pack.md` | Pass/fail report with defects |

## Acceptance Trace

| Acceptance criterion | Primary check |
|---|---|
| URD-AC-001 | Normalized evidence snapshot contains defaults and evidence gaps. |
| URD-AC-002 | Cycle plan contains exactly `cycle_days` day files; default duration is 15 minutes. |
| URD-AC-003 | Blueprint cites prior evidence and selects no more than three targets. |
| URD-AC-004 | Generated pack requires Markdown reading only. |
| URD-AC-005 | Runtime protocol defines short micro-correction and immediate continuation. |
| URD-AC-006 | Session record contains state patch and next action. |
| URD-AC-007 | `learner-state.md`, recent session record, and cycle plan are sufficient to resume. |
| URD-AC-008 | Rollover states continue/change/retire/test-next decisions. |
| URD-AC-009 | Validator rejects unnamed or generic scenarios. |
| URD-AC-010 | Validator rejects duration, closeout, certainty, and runtime violations. |
| URD-AC-011 | Runtime simulation demonstrates one-breath correction and immediate return to learner speech. |
| URD-AC-012 | Closeout validation enforces evidence classes and promotion thresholds. |
| URD-AC-013 | Rollover playbook stops at a visible checkpoint for materially new directions. |
