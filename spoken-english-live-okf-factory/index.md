---
okf_version: "0.6"
bundle: spoken-english-live-okf-factory
title: Spoken English Live OKF Factory
description: Markdown-first meta-factory for continuous spoken-English cycles designed for ChatGPT Live.
tags: [okf, factory, english, speaking, chatgpt-live, continuous-learning]
timestamp: 2026-07-09T20:45:00-07:00
---

# Spoken English Live OKF Factory

This bundle generates compact, learner-specific spoken-English course cycles for ChatGPT Live. It treats long-term learning as a chain of short cycles rather than one bounded crash course.

## Entry Point

For skills-compatible agents, start with `SKILL.md`. For direct OKF reading, use the execution path below.

## Execution Path

Read and execute the factory in this order:

1. [Cycle Evidence Contract](contracts/cycle-evidence-contract.md)
2. [Derive Cycle Blueprint](playbooks/derive-cycle-blueprint.md)
3. [Course Pack Layout](schemas/course-pack-layout.md)
4. [Materialize Cycle Pack](playbooks/materialize-cycle-pack.md)
5. [Validate Cycle Pack](playbooks/validate-cycle-pack.md)

A generated course pack is then used in this order:

1. [Live Session Protocol](runtime/live-session-protocol.md)
2. [Close Live Session](playbooks/close-live-session.md)
3. [Rollover Cycle](playbooks/rollover-cycle.md)

## Default Behavior

- Cycle length: 7 days; 3-day focused cycles are also supported.
- Daily session: 15 minutes.
- Longer normal option: 20 minutes.
- Session mode: ChatGPT Live.
- Practice language: mostly English; Chinese may be used for setup and debrief.
- Correction: brief live micro-corrections are allowed when they improve clarity or naturalness, followed by an immediate return to speaking.
- Persistence: copyable Markdown records; no Python, hooks, hidden database, or claimed file writes.

## Evaluation

The bundle includes a Darwin domain evaluation pack in `evaluation/`. The proposed domain rubric scores factory output and observed Live-session behavior separately from Darwin's common structural rubric.

Current evaluation state:

- rubric quality: 94/100
- research confidence: medium
- status: accepted for the first optimization round
- frozen: true
- latest provisional composite score: 88.4/100
- full Live validation: pending

Read `evaluation/index.md` before baseline scoring.

## Design Status

The architecture follows a lower-triangular dependency order:

> evidence intake → cycle blueprint → pack materialization → live runtime → session closeout → cycle rollover → validation

See [URD](docs/URD.md), [ADD](docs/ADD.md), and [TRACE](docs/TRACE.md).
