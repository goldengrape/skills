---
type: Traceability Map
title: Spoken English Live OKF Factory Trace
description: Trace links from user requirements to design parameters, artifacts, and checks.
tags: [trace, requirements, design, adaptive-topics]
timestamp: 2026-07-09T21:30:00-07:00
---

# TRACE — Spoken English Live OKF Factory

| URD requirement | ADD FR | ADD DP | Authoritative artifact | Validation evidence |
|---|---|---|---|---|
| URD-REQ-001 | ADD-FR-001 | ADD-DP-001 | `contracts/cycle-evidence-contract.md` | Input normalization gate |
| URD-REQ-002 | ADD-FR-002, ADD-FR-003 | ADD-DP-002, ADD-DP-003 | blueprint, schema, materializer | Target, time, progression checks |
| URD-REQ-003 | ADD-FR-002, ADD-FR-003, ADD-FR-004 | ADD-DP-002, ADD-DP-003, ADD-DP-004 | blueprint, daily plans, runtime | Objective/topic separation checks |
| URD-REQ-004 | ADD-FR-003, ADD-FR-004 | ADD-DP-003, ADD-DP-004 | runtime and Live settings | Speaking-first checks |
| URD-REQ-005 | ADD-FR-004 | ADD-DP-004 | runtime protocol | Interruption/correction checks |
| URD-REQ-006 | ADD-FR-001, ADD-FR-004, ADD-FR-005 | ADD-DP-001, ADD-DP-004, ADD-DP-005 | evidence contract, runtime, closeout | Interest-threshold checks |
| URD-REQ-007 | ADD-FR-002, ADD-FR-004, ADD-FR-005 | ADD-DP-002, ADD-DP-004, ADD-DP-005 | blueprint, runtime, session template | Verification/provenance/fallback checks |
| URD-REQ-008 | ADD-FR-005 | ADD-DP-005 | closeout and template | Session-record gate |
| URD-REQ-009 | ADD-FR-001, ADD-FR-005, ADD-FR-006 | ADD-DP-001, ADD-DP-005, ADD-DP-006 | evidence, closeout, rollover | Continuity citation checks |
| URD-REQ-010 | ADD-FR-002, ADD-FR-005, ADD-FR-006 | ADD-DP-002, ADD-DP-005, ADD-DP-006 | blueprint, state patch, rollover | Next-topic and next-cycle checks |
| URD-REQ-011 | ADD-FR-007 | ADD-DP-007 | validation playbook | Pass/fail report |

## Acceptance Trace

| Acceptance criterion | Primary check |
|---|---|
| URD-AC-001 | Evidence snapshot contains defaults, topic policy, conflicts, and gaps. |
| URD-AC-002 | Pack contains exactly `cycle_days` time-bounded day files. |
| URD-AC-003 | Guided-adaptive plan mixes anchored and adaptive-capable days while preserving objectives. |
| URD-AC-004 | Adaptive day has fallback and selection rules. |
| URD-AC-005 | Pack requires Markdown reading only. |
| URD-AC-006 | Runtime defines one-breath correction and immediate continuation. |
| URD-AC-007 | Interest confirmation follows explicit/repeated-evidence thresholds. |
| URD-AC-008 | Non-affinity load does not downgrade interest. |
| URD-AC-009 | Future current-event slot stores a rule and fallback, not a required article. |
| URD-AC-010 | Session template captures current-event provenance. |
| URD-AC-011 | Session record contains patch and one next action. |
| URD-AC-012 | Saved files are sufficient to resume objective, topic policy, and next action. |
| URD-AC-013 | Rollover makes evidence-backed language and topic decisions. |
| URD-AC-014 | Validator rejects generic/no-fallback plans. |
| URD-AC-015 | Validator rejects time, closeout, certainty, and runtime violations. |
| URD-AC-016 | Validator rejects unverified or background-heavy current-event plans. |
| URD-AC-017 | Closeout enforces language and interest evidence thresholds. |
| URD-AC-018 | Rollover stops for materially new directions. |
| URD-AC-019 | Guided-adaptive cycles enforce topic diversity unless the learner requests a thematic cycle. |
