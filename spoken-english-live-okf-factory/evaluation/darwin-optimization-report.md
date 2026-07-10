---
type: Optimization Report
title: Darwin Optimization Report — v0.5 to v0.6
description: Baseline, retained changes, provisional scoring, hard-gate status, and remaining tests.
tags: [darwin, optimization, scoring]
timestamp: 2026-07-09T20:40:00-07:00
---

# Darwin Optimization Report — v0.5 to v0.6

## Scope

Target: the complete Spoken English Live OKF Factory, with `SKILL.md` as the executable Agent Skill entrypoint and the existing DP files as authoritative references.

Evaluation mode: `interaction_simulation`. Scores are provisional because no real ChatGPT Live session or independent judge was available.

## Frozen Domain Policy

- common weight: 35%
- domain weight: 65%
- default pronunciation target: clear, intelligible global English
- rubric quality: 94/100
- research confidence: medium
- rubric status: frozen for this optimization round

## Score Change

| Stage | Common | Domain | Composite | Hard gates | Decision |
|---|---:|---:|---:|---|---|
| v0.5 baseline | 73.6 | 79.1 | 77.2 | pass, provisional | baseline |
| Round 1 — executable entrypoint | 88.8 | 79.4 | 82.7 | pass | keep |
| Round 2 — Live orchestration | 91.0 | 82.5 | 85.5 | pass | keep |
| Round 3 — evidence integrity | 92.5 | 86.3 | 88.4 | pass | keep |

`composite = common × 0.35 + domain × 0.65`

## Common Rubric

| Dimension | Weight | Before | After | Main evidence |
|---|---:|---:|---:|---|
| Frontmatter quality | 7 | 5.5 | 9.5 | Added runtime-neutral `SKILL.md` with purpose, use cases, and Chinese/English triggers. |
| Workflow clarity | 12 | 8.5 | 9.5 | Added one executable seven-step workflow and task-specific read order. |
| Failure-mode encoding | 12 | 8.0 | 9.7 | Added trigger → first response → fallback tables at skill, runtime, closeout, and rollover levels. |
| Checkpoint design | 6 | 3.0 | 9.3 | Added visible checkpoints for materialization conflicts and materially new cycle directions. |
| Executable specificity | 17 | 8.5 | 9.6 | Added correction modes, control cues, evidence thresholds, minimum viable session, and exact output order. |
| Resource integration | 4 | 8.0 | 9.0 | `SKILL.md` maps each task to only the required files. |
| Overall architecture | 12 | 8.5 | 9.2 | Preserved lower-triangular DP authority while adding a thin skill entrypoint. |
| Tested performance | 23 | 7.5 | 8.9 | Three common and four domain prompts passed dry-run or interaction simulation; no full Live test. |
| Anti-pattern blacklist | 6 | 5.0 | 9.6 | Added a single explicit blacklist covering overcorrection, false persistence, pronunciation overclaim, and automatic carry-over. |

## Domain Rubric

| Dimension | Weight | Before | After | Main improvement |
|---|---:|---:|---:|---|
| D1 evidence fidelity | 12 | 8.3 | 9.0 | Added evidence classes, provenance, and confidence-preserving normalization. |
| D2 cycle focus | 12 | 8.5 | 8.7 | Kept the three-target limit and clarified when learner confirmation is required. |
| D3 authentic speaking | 14 | 8.0 | 8.8 | Added learner-output target, coach-turn limits, fast scenario entry, and no plan-reading aloud. |
| D4 Live orchestration | 14 | 7.2 | 8.0 | Added control cues, one-breath intervention forms, cooldown rule, and recovery paths. Capped by simulation mode. |
| D5 correction and idiomatic coaching | 15 | 7.5 | 8.0 | Added naturalness/register coaching, self-repair, uptake tracking, and selective correction under fatigue. Capped by simulation mode. |
| D6 timebox and fatigue | 8 | 8.0 | 8.0 | Added minimum viable session and timer-independent fallback. Capped by simulation mode. |
| D7 state integrity | 10 | 7.8 | 9.3 | Added observed/reported/inferred/uncertain classes and pattern/stability thresholds. |
| D8 cross-cycle adaptation | 10 | 8.0 | 9.2 | Added evidence tables, retirement thresholds, test-next behavior, and learner checkpoint for new directions. |
| D9 runtime truthfulness | 5 | 8.4 | 9.2 | Added a compact entrypoint, selective file loading, explicit no-write claims, and no timer dependency. |

## Retained Changes

### Round 1

- Added `SKILL.md`.
- Added three common test prompts.
- Froze the accepted domain rubric for the first optimization round.

### Round 2

- Reworked Live correction into four concise intervention forms.
- Added learner control phrases.
- Added learner speaking-share and coach-turn targets.
- Added fatigue/time compression and runtime recovery.

### Round 3

- Added evidence provenance and operational thresholds.
- Strengthened the session record and state patch.
- Added evidence-backed retirement, relapse, and next-cycle rules.

## Ratchet Decision

All three rounds are retained because:

1. common score increased each round;
2. domain score did not regress;
3. composite score increased each round;
4. no hard gate regressed;
5. bundle size remains compact and no runtime dependency was introduced.

## Important Limitation

The 88.4 composite score is provisional. D4–D6 are capped by the rubric because this run used interaction simulation rather than an observed Live session. Real Live evidence can raise or lower the score.
