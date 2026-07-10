---
type: Evaluation Result
title: Darwin Dry-Run Validation
description: Provisional common and domain prompt validation after the v0.6 optimization rounds.
tags: [darwin, dry-run, validation]
timestamp: 2026-07-09T20:40:00-07:00
---

# Darwin Dry-Run Validation

## Evidence Mode

- mode: `interaction_simulation`
- full Live sessions observed: `0`
- result status: `provisional`
- reason: no independent subagent or recorded ChatGPT Live session was available in this optimization run.

D4–D6 are capped at 8 under the frozen domain rubric. Pronunciation-specific quality is not scored above the interaction-simulation limit.

## Prompt Results

| Prompt | Result | Evidence |
|---|---|---|
| COMMON-001 cold-start cycle | PASS | `SKILL.md` defines the exact generation order, no-more-than-three target rule, 15-minute default, complete output order, and separate read-only validation. |
| COMMON-002 conflicting records | PASS | DP-001 evidence classes and priority rules preserve the conflict; `SKILL.md` gives a visible checkpoint when the conflict changes course purpose. |
| COMMON-003 shortened Live lesson | PASS, simulated | Runtime switches to the minimum viable session and preserves one speaking task, at most one useful repair, closeout, state patch, and one next action. |
| DOMAIN-003 live naturalness corrections | PASS, simulated | Runtime supports direct replacement, naturalness nudge, self-repair, and clarification; every intervention returns immediately to speaking. |
| DOMAIN-005 evidence-sensitive closeout | PASS, simulated | Closeout separates one-off, candidate, recurring, stable, and uncertain evidence and records uptake before state promotion. |
| DOMAIN-007 adversarial runtime request | PASS | Skill blacklist and failure recovery reject Python, hidden state, automatic GitHub writes, exact transcript-based phoneme diagnosis, target inflation, and removal of closeout. |
| DOMAIN-008 naturalness-only coaching | PASS, simulated | Naturalness and register are placed above cosmetic grammar correction; the protocol does not mock or demand a native accent. |

## Simulated Live Fragments

### Naturalness interruption

```text
Learner: I very like this idea because—
Coach: Quick fix: “I really like this idea.” Go on.
Learner: I really like this idea because it saves time...
```

### Register interruption

```text
Learner: I am available at your convenience.
Coach: More natural for coffee: “Any time works for me.” Keep going.
```

### Four-minute fallback

```text
Learner: I only have four more minutes.
Coach: Got it. Give me your final recommendation in three sentences. Then we’ll fix one useful phrase and wrap up.
```

## Hard Gates

| Gate | Status | Note |
|---|---|---|
| HG-01 speaking-first | PASS in design and simulation | Learner-output target is explicit; no full Live telemetry yet. |
| HG-02 pronunciation integrity | PASS | Transcript is explicitly insufficient for exact phoneme diagnosis. |
| HG-03 timebox and closeout | PASS in design and simulation | Minimum viable session preserves closeout. |
| HG-04 persistence chain | PASS | Record, patch, and exactly one next action are mandatory. |
| HG-05 evidence truthfulness | PASS | Evidence classes and persistence disclaimers are explicit. |
| HG-06 continuity | PASS | Rollover requires session/state references. |
| HG-07 runtime compatibility | PASS | Core workflow remains Markdown-only. |
| HG-08 validation integrity | PASS | Validator is read-only and cannot silently repair. |

## Remaining Validation Work

Before calling the package Live-validated, run at least:

1. one normal 15-minute session;
2. one session with several brief corrections;
3. one session shortened by fatigue or time;
4. one cycle rollover from real session records.
