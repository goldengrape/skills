---
okf_version: "0.8"
bundle: spoken-english-live-okf-factory
title: Spoken English Live OKF Factory
description: Markdown-first meta-factory for continuous, interest-aware, confound-aware spoken-English cycles designed for ChatGPT Live.
tags: [okf, factory, english, speaking, chatgpt-live, continuous-learning, adaptive-topics]
timestamp: 2026-07-09T21:30:00-07:00
---

# Spoken English Live OKF Factory

This bundle generates compact, learner-specific spoken-English course cycles for ChatGPT Live. It treats long-term learning as a chain of short cycles and separates stable language objectives from adaptable conversation topics.

## Entry Point

For skills-compatible agents, start with `SKILL.md`.

## Execution Path

1. [Cycle Evidence Contract](contracts/cycle-evidence-contract.md)
2. [Derive Cycle Blueprint](playbooks/derive-cycle-blueprint.md)
3. [Course Pack Layout](schemas/course-pack-layout.md)
4. [Materialize Cycle Pack](playbooks/materialize-cycle-pack.md)
5. [Validate Cycle Pack](playbooks/validate-cycle-pack.md)

A generated pack is used through:

1. [Live Session Protocol](runtime/live-session-protocol.md)
2. [Close Live Session](playbooks/close-live-session.md)
3. [Rollover Cycle](playbooks/rollover-cycle.md)

## Default Behavior

- Cycle length: 7 days; 3-day focused cycles supported.
- Daily session: 15 minutes.
- Practice language: mostly English; Chinese for brief setup/debrief.
- Correction: concise live micro-corrections and naturalness coaching.
- Topic policy: `guided_adaptive`, approximately 60% planned and 40% adaptive-capable.
- Interest discovery: explicit or repeated evidence, never one casual mention alone; topic affinity is separated from fatigue, language load, background knowledge, and prompt quality.
- Adaptive-topic balance: confirmed interests may deepen, possible interests may be tested, and variety is deliberately refreshed instead of repeating the easiest topic indefinitely.
- Current events: disabled by default; when enabled they require a fast verification budget, a compact context capsule, and an evergreen fallback.
- Persistence: copyable Markdown; no Python, hooks, hidden database, or claimed file writes.

## Design Status

The architecture remains lower triangular:

> evidence intake → cycle blueprint → pack materialization → Live runtime/topic choice → session closeout → cycle rollover → validation

See [URD](docs/URD.md), [ADD](docs/ADD.md), and [TRACE](docs/TRACE.md).

## Evaluation Status

The v0.8 provisional interaction-simulation score is 90.2/100 under domain rubric v0.3. The optimization added a topic-fit decision card, confound-aware engagement evidence, topic-diversity controls, and a strict current-event verification budget. Full Live validation remains pending, so real-time pacing and correction scores remain capped.