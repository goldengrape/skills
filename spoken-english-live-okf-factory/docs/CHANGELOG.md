---
type: Changelog
title: Spoken English Live OKF Factory Changelog
description: Version history for the factory bundle.
tags: [changelog]
timestamp: 2026-07-09T21:30:00-07:00
---

# Changelog

## 0.8 — 2026-07-09

- Added adaptive topic intents: deepen a confirmed interest, test a possible interest, refresh variety, or review transfer.
- Added a six-part topic-fit check covering language-objective fit, consent/safety, knowledge accessibility, evidence basis, recent-topic balance, and time fit.
- Separated topic affinity from language load, background knowledge, prompt/task quality, fatigue/time, and privacy/sensitivity before interest updates.
- Added recent-topic history and a default ceiling of three sessions per broad topic in a normal seven-day guided-adaptive cycle unless the learner requests a thematic cycle.
- Added load-reduction fallbacks and explicit switch triggers to adaptive day plans.
- Added a 30-second current-event verification budget and three-part context capsule before immediate fallback.
- Added HG-10 for interest-inference integrity plus adversarial tests for expertise confounds, topic monoculture, and slow current-event verification.
- Re-ran the Darwin ratchet from a v0.7 provisional baseline of 86.4 to a v0.8 provisional composite score of 90.2.
- Preserved the seven-DP lower-triangular architecture and Markdown-only runtime.


## 0.7 — 2026-07-09

- Added `guided_adaptive` topic policy as the default: stable language objectives with a mix of anchored and adaptive-capable conversation topics.
- Added evidence thresholds for explicit, confirmed, possible, low-engagement, avoided, and retired interests without creating a separate interest-ledger authority.
- Added optional current-event slots with runtime verification, source/date provenance, sensitive-topic preferences, short context limits, and evergreen fallbacks.
- Added runtime topic selection, two-choice behavior, low-engagement topic switching, and interest discovery without preference interrogation.
- Extended session closeout with topic-selection basis, engagement signals, current-event provenance, and a non-destructive next-topic recommendation.
- Extended cycle rollover and validation to assess topic mix, interest evidence, news suitability, and preservation of fixed language objectives.
- Preserved the seven-DP lower-triangular architecture and Markdown-only runtime.

## 0.6 — 2026-07-09

- Added a runtime-neutral `SKILL.md` entrypoint with trigger phrases, task-specific read order, visible checkpoints, fallback tables, output contracts, and an anti-pattern blacklist.
- Added common Darwin test prompts and froze the accepted domain rubric for the first optimization round.
- Reworked Live orchestration around one-breath corrections, learner control cues, speaking-share and coach-turn targets, timer-independent sequencing, and a minimum viable session for fatigue or short time.
- Added correction modes for direct replacement, naturalness, self-repair, and clarification.
- Added evidence provenance classes, learner-uptake recording, and operational thresholds for one-off slips, candidate patterns, recurring patterns, and stable phrases.
- Added evidence-backed retirement and relapse rules plus a rollover checkpoint for materially new learning directions.
- Added provisional Darwin baseline, dry-run validation, optimization report, and `results.tsv`.
- Preserved the lower-triangular DP architecture and Markdown-only runtime.

## 0.5 — 2026-07-09

- Added a Darwin 2.0 domain research record and metadata.
- Added a nine-dimension, 100-point domain rubric for factory generation, Live session quality, closeout, and rollover.
- Added eight hard gates for speaking-first behavior, pronunciation evidence, timebox, persistence, evidence truthfulness, continuity, runtime compatibility, and validation integrity.
- Added eight domain test prompts covering cold start, conflicting evidence, actual Live correction, fatigue, closeout, rollover, adversarial runtime requests, and naturalness coaching.
- Added RQ1–RQ9 rubric-quality evaluation with a 94/100 result.
- Kept the rubric unfrozen pending user confirmation.

## 0.4 — 2026-07-09

- Rewrote the URD to separate user needs from implementation details.
- Derived seven functional requirements and seven design parameters.
- Ran three structural coupling retries and reached a lower-triangular design matrix.
- Split evidence normalization from blueprint derivation and pack materialization.
- Consolidated Live teaching and correction rules into one runtime protocol.
- Consolidated fragmented learner-state files into one canonical learner-state file plus phrase and scenario ledgers.
- Made session closeout the only state-transition writer.
- Made rollover a separate terminal stage and validation read-only.
- Reduced the generated course-pack file set.
- Renamed weekly-only concepts to cycle-based concepts.
