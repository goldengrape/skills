---
type: Optimization Report
title: Darwin Optimization Report — v0.7 to v0.8
description: Baseline, retained experiments, provisional scoring, hard gates, and remaining Live tests.
tags: [darwin, optimization, adaptive-topics, interests, current-events]
timestamp: 2026-07-09T21:30:00-07:00
---

# Darwin Optimization Report — v0.7 to v0.8

## Scope

Target: the complete Spoken English Live OKF Factory after the v0.7 adaptive-topic revision.

Evaluation mode: `interaction_simulation` plus static validation. No independent sub-agent or observed ChatGPT Live session was available, so scores remain provisional and D4–D6 are capped by the domain rubric.

## Frozen Domain Policy

- common weight: 35%
- domain weight: 65%
- domain rubric: 0.3
- default pronunciation target: clear, intelligible global English
- current-event verification budget: 30 seconds
- normal seven-day same-topic ceiling: 3 sessions unless the learner requests a thematic cycle
- hard gates: HG-01 through HG-10

## Score Change

| Stage | Common | Domain | Composite | Decision |
|---|---:|---:|---:|---|
| v0.7 rescore | 89.6 | 84.6 | 86.4 | baseline |
| Round 1 — topic-selection specificity | 91.0 | 86.4 | 88.0 | keep |
| Round 2 — interest-inference integrity | 91.7 | 88.0 | 89.3 | keep |
| Round 3 — topic portfolio and current-event economy | 92.2 | 89.1 | **90.2** | keep |

`composite = common × 0.35 + domain × 0.65`

## Baseline Weakness

v0.7 defined adaptive topics and interest thresholds, but three decisions remained underspecified:

1. candidate topics had an ordering but no explicit fit test;
2. low or high verbal output could be misread as topic affinity even when caused by expertise, language load, knowledge load, prompt quality, fatigue, or privacy;
3. confirmed interests could become the default topic repeatedly, narrowing a long-running course.

## Round 1 — Topic-Selection Specificity

Retained changes:

- added adaptive intents: `deepen_confirmed`, `test_possible`, `refresh_variety`, and `review_transfer`;
- added a six-part topic-fit check;
- added a recent three-session topic window;
- required a load-reduction fallback and switch trigger in adaptive day plans;
- prevented automatic selection of the easiest confirmed interest.

## Round 2 — Interest-Inference Integrity

Retained changes:

- separated `topic_affinity` from language load, background knowledge, prompt/task quality, fatigue/time, privacy/sensitivity, and unknown causes;
- allowed only topic-affinity evidence to promote or downgrade interest;
- added the classification to session closeout and canonical state updates;
- added HG-10 and an expertise-versus-interest adversarial test.

## Round 3 — Topic Portfolio and Current-Event Economy

Retained changes:

- limited one broad topic to three sessions in a normal seven-day guided-adaptive cycle unless the learner requests a thematic cycle;
- required a changed language function, pressure, role, or perspective when a topic repeats;
- added a 30-second current-event verification budget;
- added a three-part context capsule and immediate evergreen fallback;
- added monoculture and slow-verification tests.

## Ratchet Decision

All three rounds are retained because each raised the domain and composite score, no passing hard gate regressed, the DP matrix remains lower triangular, and the core runtime remains Markdown-only.

## Remaining Evidence Gap

The 90.2 score is not a real-world Live score. Run at least these observed sessions before declaring v0.8 stable:

1. an adaptive session where a preferred topic is linguistically difficult;
2. a session where the learner speaks fluently about an uninteresting professional topic;
3. a current-event-optional session that must abandon a slow lookup and use the fallback;
4. a later cycle that tests whether topic variety improves adherence without weakening language progression.
