---
type: Axiomatic Design Document
title: Spoken English Live OKF Factory ADD
description: Functional decomposition and lower-triangular architecture, extended for adaptive topics without adding a new design authority.
tags: [add, axiomatic-design, coupling, english-speaking, adaptive-topics]
timestamp: 2026-07-09T21:30:00-07:00
---

# ADD — Spoken English Live OKF Factory

## Design Objective

Convert user requirements into ordered responsibilities. A responsibility may depend on earlier outputs, but must not reach backward and change an earlier responsibility’s contract.

The target is a decoupled lower-triangular design. Topic adaptation is incorporated inside existing evidence, blueprint, runtime, closeout, rollover, and validation responsibilities rather than introduced as a parallel policy system. v0.8 adds one shared decision vocabulary—topic intent, topic-fit checks, and engagement-cause classification—without creating a new authority.

## Functional Requirements Derived From the URD

| ID | Functional requirement | Source requirements |
|---|---|---|
| ADD-FR-001 | Produce one normalized evidence snapshot including learner, interest, and topic-policy evidence. | URD-REQ-001, URD-REQ-006, URD-REQ-009 |
| ADD-FR-002 | Derive a bounded language blueprint and anchored/adaptive topic strategy. | URD-REQ-002, URD-REQ-003, URD-REQ-007, URD-REQ-010 |
| ADD-FR-003 | Materialize the blueprint as a compact Markdown course pack. | URD-REQ-002, URD-REQ-003, URD-REQ-004 |
| ADD-FR-004 | Run one time-bounded ChatGPT Live session and select a suitable topic without losing the language objective. | URD-REQ-004, URD-REQ-005, URD-REQ-006, URD-REQ-007 |
| ADD-FR-005 | Close the session with language evidence, interest evidence, a state patch, and one next action. | URD-REQ-008, URD-REQ-009, URD-REQ-010 |
| ADD-FR-006 | Convert completed-cycle evidence into the next language and topic strategy. | URD-REQ-009, URD-REQ-010 |
| ADD-FR-007 | Detect and reject invalid inputs, packs, runtime plans, records, topic adaptations, or rollover decisions. | URD-REQ-011 |

## Structural Retry Log

### Retry 1–4

v0.4–v0.6 separated evidence intake, blueprint derivation, materialization, runtime, closeout, rollover, and read-only validation; consolidated runtime policy and canonical learner state; and added execution/evidence hardening.

### Retry 5 — Add adaptive topics without a parallel subsystem

Rejected design:

- a separate interest agent;
- a separate interest ledger file;
- a news-selection service as a new DP;
- automatic rewriting of future day files after every session.

These would create duplicate state authorities and irregular dependencies.

Accepted design:

- DP-001 normalizes interest and current-event preferences;
- DP-002 assigns anchored, adaptive, and current-event-optional slots while fixing language objectives;
- DP-003 stores topic policy in existing plans, learner state, and Live settings;
- DP-004 selects the actual topic at session time and verifies current events when used;
- DP-005 records engagement evidence and recommends the next topic without silently rewriting plans;
- DP-006 changes the next cycle's topic mix from accumulated evidence;
- DP-007 validates all of the above read-only.

Result:

- no new same-cycle DP;
- no duplicate interest authority;
- affinity/load separation is recorded in DP-001 and observed in DP-004/DP-005 rather than implemented as a new subsystem;
- topic diversity is planned in DP-002 and evaluated in DP-006;
- adaptive behavior follows the existing lower-triangular order.

## Final Design Parameters

| ID | Design parameter | Primary artifact | Responsibility boundary |
|---|---|---|---|
| ADD-DP-001 | Cycle Evidence Contract | `contracts/cycle-evidence-contract.md` | Normalize learner, preference, interest, topic-policy, prior evidence, defaults, conflicts, and gaps. It does not choose the course. |
| ADD-DP-002 | Cycle Blueprint Derivation | `playbooks/derive-cycle-blueprint.md` | Select cycle length, language targets, progression, and topic-slot strategy. It does not create files or choose a runtime news item. |
| ADD-DP-003 | Course Pack Materializer | schema and materialization playbook | Convert the blueprint into compact Markdown with fixed objectives and usable topic/fallback data. It does not run a session. |
| ADD-DP-004 | Live Session Runtime Protocol | `runtime/live-session-protocol.md` | Select today's topic, optionally verify a current event, and run the voice session. It does not persist state directly. |
| ADD-DP-005 | Session Closeout Protocol | closeout playbook and session template | Produce immutable session evidence and deterministic patches, including interest updates and next-topic recommendation. |
| ADD-DP-006 | Cycle Rollover Protocol | `playbooks/rollover-cycle.md` | Summarize language and topic evidence, then propose the next cycle. |
| ADD-DP-007 | Validation Gate | `playbooks/validate-cycle-pack.md` | Report pass/fail and defects without modifying artifacts. |

## Final Design Matrix

| FR \ DP | DP-001 | DP-002 | DP-003 | DP-004 | DP-005 | DP-006 | DP-007 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ADD-FR-001 Normalize evidence | X | · | · | · | · | · | · |
| ADD-FR-002 Derive blueprint | X | X | · | · | · | · | · |
| ADD-FR-003 Materialize pack | X | X | X | · | · | · | · |
| ADD-FR-004 Run/adapt Live session | · | · | X | X | · | · | · |
| ADD-FR-005 Persist session evidence | · | · | X | X | X | · | · |
| ADD-FR-006 Rollover next cycle | X | X | · | · | X | X | · |
| ADD-FR-007 Reject invalid artifacts | X | X | X | X | X | X | X |

The matrix remains lower triangular:

```text
DP-001 → DP-002 → DP-003 → DP-004 → DP-005 → DP-006 → DP-007
```

## Temporal Feedback Boundary

Within a cycle, DP-005 may recommend a topic for the next session by updating canonical state. DP-004 of the next session consumes that state. It does not rewrite the original DP-002 blueprint; the fixed language objective remains authoritative.

Across cycles:

```text
cycle N: DP-006 rollover
          ↓
cycle N+1: DP-001 evidence snapshot
```

This temporal feedback does not break the same-cycle matrix.

## Generated Course Pack Responsibilities

| Generated artifact | Owner DP | Purpose |
|---|---|---|
| `mission.md` | DP-003 | Goal, evidence basis, language focus, and topic policy. |
| `plan/cycle-plan.md`, `plan/day-N.md` | DP-003 | Language progression and anchored/adaptive topic slots. |
| `teacher/live-session-settings.md` | DP-003 | Runtime parameters, topic policy, and current-event preferences. |
| `state/learner-state.md` | DP-005 | Canonical active language and interest/topic state. |
| `state/phrase-deck.md` | DP-005 | Reusable expressions and recall status. |
| `state/scenario-ledger.md` | DP-005 | Scenario/topic evidence, engagement, and variants. |
| session records | DP-005 | Immutable interaction and adaptation evidence. |
| cycle review | DP-006 | Evidence-based language and topic summary. |
| next-cycle proposal | DP-006 | Carry-over and next topic strategy. |

## Ockham Refactor

The following remain intentionally absent:

- separate interest ledger;
- separate current-events policy file;
- separate topic adaptation agent;
- automatic future-plan rewrite log.

The existing canonical state and daily plans are sufficient.

## Failure Boundaries

| Failure | Owning DP | Required response |
|---|---|---|
| Missing/conflicting learner or topic evidence | DP-001 | Record gap/conflict; do not invent certainty. |
| Too many targets or invalid adaptive slot | DP-002 | Reduce targets or add objective, rule, and fallback. |
| Generic/bloated course pack | DP-003 | Regenerate from the same blueprint using compact schema. |
| Long interruption, poor topic choice, or unverified news | DP-004 | Return to speaking, switch to a suitable fallback, and preserve objective. |
| Unsupported evidence promotion or missing persistence chain | DP-005 | Downgrade claim or keep session incomplete. |
| Next cycle ignores evidence or changes topic policy without confirmation | DP-006 | Reject proposal or stop at checkpoint. |
| Validator attempts silent repair | DP-007 | Stop; report defects only. |
