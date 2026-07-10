---
type: Axiomatic Design Document
title: Spoken English Live OKF Factory ADD
description: Functional decomposition, coupling retries, and final lower-triangular architecture.
tags: [add, axiomatic-design, coupling, english-speaking]
timestamp: 2026-07-09T20:45:00-07:00
---

# ADD — Spoken English Live OKF Factory

## Design Objective

Convert the confirmed user requirements into a small set of ordered design responsibilities. A responsibility may depend on earlier outputs, but must not reach backward and change an earlier responsibility’s meaning or implementation contract.

The target is a **decoupled lower-triangular design**. It is not a claim of zero coupling. The system has a real execution order, and later stages necessarily consume earlier evidence.

## Functional Requirements Derived From the URD

| ID | Functional requirement | Source requirements |
|---|---|---|
| ADD-FR-001 | Produce one normalized cycle evidence snapshot from learner input and prior records. | URD-REQ-001, URD-REQ-006 |
| ADD-FR-002 | Derive a bounded cycle blueprint from that snapshot. | URD-REQ-002, URD-REQ-007 |
| ADD-FR-003 | Materialize the blueprint as a compact Markdown course pack. | URD-REQ-002, URD-REQ-003 |
| ADD-FR-004 | Run one time-bounded ChatGPT Live speaking session from the pack. | URD-REQ-003, URD-REQ-004 |
| ADD-FR-005 | Close the session with a persistent evidence record and state patch. | URD-REQ-005, URD-REQ-006 |
| ADD-FR-006 | Convert completed-cycle evidence into the next-cycle proposal and carry-over input. | URD-REQ-006, URD-REQ-007 |
| ADD-FR-007 | Detect and reject invalid inputs, packs, runtime plans, records, or rollover decisions. | URD-REQ-008 |

## Coupling Diagnosis of v0.3

The previous design grouped unrelated responsibilities together:

- `live-speaking-generation-contract.md` specified inputs, generated files, session duration, correction behavior, and quality rules.
- `generate-weekly-speaking-okf.md` selected learning targets and also prescribed runtime behavior.
- `run-live-speaking-session.md`, `correction-policy.md`, and `live-teaching-protocol.md` repeated the interruption and correction rules.
- `current-state.md`, `recurring-errors.md`, `interest-ledger.md`, and `next-action.md` required several files to update one learner state transition.
- validation rules were spread across the generation contract, playbooks, and examples.

This produced an irregular dependency pattern: changing correction behavior could require edits in input contracts, generation, runtime, examples, and validation; changing state shape could require edits across six generated files.

## Structural Retry Log

### Retry 1 — Separate evidence intake from output generation

Changed:

- Split learner input and prior evidence into one evidence contract.
- Moved target selection into a separate blueprint derivation step.
- Moved generated file structure into a separate schema.

Result:

- Input changes no longer require editing Live runtime policy.
- Coupling remained between course generation, correction policy, and state persistence.

### Retry 2 — Consolidate runtime policy and learner state

Changed:

- Merged live teaching and correction policy into one runtime protocol.
- Consolidated current status, recurring errors, interests, pronunciation observations, and next action into one canonical `learner-state.md`.
- Kept phrase and scenario ledgers separate because they have distinct growth and retrieval patterns.
- Made session closeout the only writer of session evidence and learner-state patches.

Result:

- Runtime behavior has one authority.
- A session state transition has one authority.
- The remaining dependencies are sequential rather than irregular.

### Retry 3 — Make rollover and validation terminal stages

Changed:

- Defined rollover as a consumer of completed-cycle evidence, not as part of daily generation.
- Defined validation as read-only: it reports defects and never silently rewrites artifacts.
- Treated the next cycle as a new execution instance. The feedback edge from rollover to the next evidence snapshot is temporal, not a backward dependency inside the current cycle.

Result:

- The same-cycle design matrix is lower triangular.
- No accepted irregular coupling remains.

### Retry 4 — Darwin execution and evidence hardening

Changed:

- Added a thin `SKILL.md` entrypoint that dispatches into the existing DP order without becoming a new design authority.
- Added visible checkpoints only at decisions that can materially change the learner's course.
- Added learner control cues, one-breath correction forms, a minimum viable session, and runtime recovery rules inside DP-004.
- Added evidence classes, pattern-promotion thresholds, uptake tracking, and evidence-backed retirement rules inside DP-005 and DP-006.

Result:

- The execution interface is discoverable by skills-compatible agents.
- No new same-cycle DP was introduced.
- The lower-triangular matrix remains unchanged because the new entrypoint only routes to existing authorities.

## Final Design Parameters

| ID | Design parameter | Primary artifact | Responsibility boundary |
|---|---|---|---|
| ADD-DP-001 | Cycle Evidence Contract | `contracts/cycle-evidence-contract.md` | Normalize learner input, preferences, prior evidence, defaults, and evidence gaps. It does not choose the course. |
| ADD-DP-002 | Cycle Blueprint Derivation | `playbooks/derive-cycle-blueprint.md` | Select cycle length, time budget, no more than three targets, and an ordered daily progression. It does not create the file tree. |
| ADD-DP-003 | Course Pack Materializer | `schemas/course-pack-layout.md`, `playbooks/materialize-cycle-pack.md` | Convert the blueprint into the required compact Markdown pack. It does not run a session. |
| ADD-DP-004 | Live Session Runtime Protocol | `runtime/live-session-protocol.md` | Run a time-bounded voice session with turn-taking, micro-correction, repair, and fatigue handling. It does not persist state directly. |
| ADD-DP-005 | Session Closeout Protocol | `playbooks/close-live-session.md`, `templates/session-record-template.md` | Produce the session record and a deterministic patch for canonical state files. |
| ADD-DP-006 | Cycle Rollover Protocol | `playbooks/rollover-cycle.md` | Summarize completed-cycle evidence and produce the next-cycle proposal and carry-over snapshot. |
| ADD-DP-007 | Validation Gate | `playbooks/validate-cycle-pack.md` | Read all relevant artifacts, report pass/fail and defects, and never modify them silently. |

## Final Design Matrix

`X` means the design parameter contributes to or is required by the functional requirement. `·` means no direct dependency.

| FR \ DP | DP-001 | DP-002 | DP-003 | DP-004 | DP-005 | DP-006 | DP-007 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ADD-FR-001 Normalize evidence | X | · | · | · | · | · | · |
| ADD-FR-002 Derive blueprint | X | X | · | · | · | · | · |
| ADD-FR-003 Materialize pack | X | X | X | · | · | · | · |
| ADD-FR-004 Run Live session | · | · | X | X | · | · | · |
| ADD-FR-005 Persist session evidence | · | · | X | X | X | · | · |
| ADD-FR-006 Rollover next cycle | X | X | · | · | X | X | · |
| ADD-FR-007 Reject invalid artifacts | X | X | X | X | X | X | X |

The matrix is lower triangular. The dependency order is:

```text
DP-001 → DP-002 → DP-003 → DP-004 → DP-005 → DP-006 → DP-007
```

DP-007 may inspect any completed prefix—for example after DP-003 or DP-005—but it remains read-only. It does not author upstream artifacts or create a backward dependency.

## Temporal Feedback Boundary

After DP-006 completes, its carry-over snapshot becomes an input to **DP-001 of the next cycle**:

```text
cycle N: DP-006 rollover
          ↓
cycle N+1: DP-001 evidence snapshot
```

This is intentional learning feedback across cycle instances. It is not a same-cycle matrix edge and therefore does not break the lower-triangular architecture.

## Generated Course Pack Responsibilities

| Generated artifact | Owner DP | Purpose |
|---|---|---|
| `mission.md` | DP-003 | Learner goal, assumptions, evidence basis, and cycle focus. |
| `plan/cycle-plan.md` and `plan/day-N.md` | DP-003 | Ordered, time-bounded speaking work. |
| `teacher/live-session-settings.md` | DP-003 | Course-specific parameters consumed later by DP-004. |
| `state/learner-state.md` | DP-005 | Canonical current state, active errors, interests, pronunciation notes, and next action. |
| `state/phrase-deck.md` | DP-005 | Reusable expressions and recall status. |
| `state/scenario-ledger.md` | DP-005 | Scenario evidence and next variants. |
| `sessions/session-YYYY-MM-DD-day-N.md` | DP-005 | Immutable session evidence. |
| `review/cycle-review.md` | DP-006 | Evidence-based cycle summary. |
| `review/next-cycle-proposal.md` | DP-006 | Carry-over and recommended next focus. |

## Ockham Refactor

Removed or merged from v0.3:

- `speaking-map.md` → merged into `mission.md` and `plan/cycle-plan.md`.
- `scenario-map.md` → merged into `plan/cycle-plan.md` and `state/scenario-ledger.md`.
- `phrase-bank.md` → merged into `state/phrase-deck.md`.
- `state/current-state.md`, `state/recurring-errors.md`, `state/interest-ledger.md`, `state/next-action.md` → merged into `state/learner-state.md`.
- `teacher/correction-policy.md` and `teacher/live-teaching-protocol.md` → replaced by one factory-level `runtime/live-session-protocol.md`; generated packs contain only `teacher/live-session-settings.md`.
- `teacher/teacher-notebook.md` → removed; immutable session records and canonical state are sufficient.
- `generate-weekly-speaking-okf.md` → renamed and narrowed to cycle-pack materialization; target selection moved upstream.

## Accepted Coupling

No irregular same-cycle coupling is accepted.

The only intentional coupling is the ordered dependence shown in the lower-triangular matrix and the temporal feedback from one cycle’s rollover into the next cycle’s evidence intake.

## Failure Boundaries

| Failure | Owning DP | Required response |
|---|---|---|
| Missing or conflicting learner evidence | DP-001 | Record the gap or conflict; do not invent certainty. |
| Too many cycle targets | DP-002 | Reduce to one scenario target, one fluency/discourse target, and one repair target. |
| Generic or bloated course pack | DP-003 | Regenerate from the same blueprint using the compact schema. |
| Long or repeated interruption | DP-004 | Stop after one replacement, return to speaking, and defer explanation to a natural pause. |
| Unsupported evidence promotion or missing persistence chain | DP-005 | Downgrade the claim or keep the session incomplete until record, patch, and one next action exist. |
| Next cycle ignores evidence or changes direction without confirmation | DP-006 | Reject the proposal, add evidence references, and stop at the learner checkpoint when required. |
| Validator attempts silent repair | DP-007 | Stop; report defects only. |
