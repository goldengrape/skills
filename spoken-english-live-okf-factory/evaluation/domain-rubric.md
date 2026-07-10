---
type: Domain Rubric
title: Spoken English Live OKF Factory Domain Rubric
description: Evidence-backed scoring scheme for course-cycle generation, ChatGPT Live session quality, persistence, and rollover.
tags: [darwin, domain-rubric, english-speaking, chatgpt-live]
timestamp: 2026-07-09T21:30:00-07:00
---

# Domain Rubric — Spoken English Live OKF Factory

## Domain Name

Continuous ChatGPT Live spoken-English course-cycle generation and delivery.

## Skill Goal

Generate learner-specific three-day or seven-day spoken-English course cycles, run short and natural ChatGPT Live practice, capture trustworthy Markdown evidence, and use that evidence to design the next cycle.

## Expected Input

- learner brief and current spoken-English goal;
- cycle preferences, normally 3 or 7 days and 15 minutes per day;
- correction preference;
- optional prior session records, learner state, phrase deck, scenario ledger, and cycle review;
- optional interests, fatigue constraints, and target scenarios.

## Expected Output

Depending on the test scope:

1. a normalized evidence snapshot;
2. a bounded cycle blueprint;
3. a compact Markdown course pack;
4. an observed or simulated ChatGPT Live session;
5. a Markdown session record and state patch with exactly one next action;
6. a cycle review and evidence-backed next-cycle proposal;
7. a read-only validation report.

## User Intent

The learner wants sustainable spoken-English improvement through frequent short conversations, useful live correction, more idiomatic expression, and continuity across cycles without relying on hidden model memory or unavailable local execution.

## Success Criteria

A successful result:

- is specific to the learner and prior evidence;
- contains no more than three primary cycle targets;
- creates realistic, spontaneous speaking opportunities;
- keeps the learner speaking more than the coach;
- uses short, well-timed corrections and naturalness suggestions;
- fits the selected time, with 15 minutes as the default;
- protects closeout and produces a trustworthy Markdown record;
- carries verified evidence into the next session and cycle;
- does not overclaim pronunciation certainty, memory, file writes, or runtime capabilities.

## Scoring Method

Score each dimension from 1 to 10 using the anchors below.

```text
dimension points = dimension score × dimension weight ÷ 10
domain score = sum of all dimension points
```

The maximum domain score is 100.

Half-point scores are allowed only when the evidence clearly falls between two anchors. Every score must cite concrete evidence from generated files, an interaction transcript, an observed Live session, or a validation report.

### Evidence modes

| Mode | Meaning | Scoring effect |
|---|---|---|
| `full_live` | An evaluator observes an actual ChatGPT Live session and its closeout. | All dimensions may receive full scores. |
| `interaction_simulation` | A structured turn-by-turn simulation is run in text. | D4–D6 may not exceed 8; pronunciation-specific evidence may not exceed 5. |
| `static_review` | Only files and instructions are inspected. | D3–D6 may not exceed 6. The overall result is provisional. |

A baseline evaluation should include at least one `full_live` test. If more than 30% of weighted evidence is based only on static review, mark the domain score `provisional`.

## Dimensions

### D1 — Evidence Fidelity and Learner Personalization

**Weight: 12**

Evaluates whether the system faithfully uses the learner's current instructions, prior evidence, interests, constraints, and conflicts without inventing certainty.

| Score | Anchor |
|---:|---|
| 1 | Ignores available learner evidence, fabricates details, hides conflicts, or generates a generic plan unrelated to the stated goal. |
| 5 | Uses the learner's main goal and some history, but defaults, conflicts, recency, or evidence gaps are only partly visible; personalization is shallow. |
| 10 | Produces a clear evidence snapshot; respects evidence priority; records defaults, conflicts, and gaps; separates topic affinity from language, knowledge, prompt, fatigue, and privacy load; and ties important course decisions to current instructions or observable prior evidence. |

**Common failures**

- Treating an estimated level as certain.
- Ignoring the latest learner instruction in favor of an older record.
- Mentioning interests without using them in a task.
- Treating fluent talk caused by expertise as confirmed interest, or language struggle as dislike.
- Claiming improvement not demonstrated in session evidence.

**Evidence to check**

- evidence snapshot;
- `mission.md`;
- cited prior records;
- defaults and conflict notes;
- planning rationale.

**Source refs:** SRC-PROJECT-URD, SRC-PROJECT-PLAYBOOKS, SRC-ACTFL-CANDO.

---

### D2 — Cycle Focus, Scope, and Progression

**Weight: 12**

Evaluates whether the cycle is bounded, coherent, and sequenced for a three-day or seven-day period.

| Score | Anchor |
|---:|---|
| 1 | Has no clear cycle purpose, contains more than three unrelated primary targets, repeats the same exercise, or cannot fit the selected cycle length. |
| 5 | Has a plausible focus and daily sequence, but progression, transfer, retesting, or target boundaries are weak or generic. |
| 10 | Uses no more than one scenario target, one fluency/discourse target, and one repair target; each is evidence-backed; days progress from entry to variation, transfer, and review; prior phrases or errors are deliberately retrieved or retested; adaptive slots deliberately balance deepening, testing, and variety. |

**Common failures**

- Seven disconnected daily topics.
- Repeating the easiest confirmed interest until the cycle becomes a topic monoculture.
- Inflating a focused three-day need into a generic seven-day plan.
- Repeating the same role-play without changing pressure, support, or context.
- Carrying every previous target forward automatically.

**Evidence to check**

- cycle blueprint;
- `mission.md`;
- `plan/cycle-plan.md`;
- daily plan sequence;
- carry-over evidence.

**Source refs:** SRC-PROJECT-URD, SRC-PROJECT-ADD, SRC-ACTFL-CANDO.

---

### D3 — Authentic Spoken Tasks and Learner Output Opportunity

**Weight: 14**

Evaluates whether the activities elicit meaningful, spontaneous spoken production rather than written study or scripted recitation.

| Score | Anchor |
|---:|---|
| 1 | The session is mainly explanation, reading, vocabulary display, written exercises, or coach speech; the learner has little meaningful speaking to do. |
| 5 | Includes role-play and spoken answers, but tasks remain heavily scripted, predictable, repetitive, or detached from a real communicative purpose. |
| 10 | Uses realistic interpersonal scenarios, clear communicative functions, spontaneous follow-ups, and transfer variations; the learner must negotiate meaning, explain, respond, or make decisions in speech and has the majority of productive airtime. |

**Common failures**

- Asking the learner to read model answers aloud.
- Supplying all useful language before the learner attempts the task.
- Role-play with no consequence, follow-up, or variation.
- Treating word-list recall as the main speaking task.

**Evidence to check**

- daily scenario and roles;
- opening and follow-up questions;
- main speaking task;
- transfer task;
- observed learner/coach speaking share.

**Source refs:** SRC-ACTFL-FACT, SRC-ACTFL-OPI, SRC-CEFR-SPOKEN, SRC-PROJECT-RUNTIME.

---

### D4 — ChatGPT Live Conversational Orchestration

**Weight: 14**

Evaluates the quality of real-time turn-taking, pacing, follow-up, pause handling, and adaptation during Live conversation.

| Score | Anchor |
|---:|---|
| 1 | The coach monologues, asks several questions at once, fills every pause, loses the scenario, or repeatedly prevents the learner from completing a thought. |
| 5 | The interaction is generally conversational, but prompts are sometimes long, follow-ups feel mechanical, pause handling is impatient, or difficulty adjustment is inconsistent. |
| 10 | The coach asks one useful question at a time, listens through ordinary pauses, follows the learner's meaning, uses concise natural follow-ups, applies a quick topic-fit check, separates affinity from load before switching topics, adjusts support or pressure without losing the task, and keeps the learner speaking more than the coach. |

**Common failures**

- Long setup before the learner speaks.
- Multi-part interview questions.
- Repeating the learner's whole answer before responding.
- Turning fatigue into more explanation instead of shortening the task.

**Evidence to check**

- actual Live observation or turn-by-turn transcript;
- prompt length;
- number and quality of follow-ups;
- pause behavior;
- learner/coach speaking share;
- fatigue adaptation.

**Source refs:** SRC-OPENAI-VOICE-2026, SRC-CEFR-SPOKEN, SRC-ACTFL-CANDO, SRC-GENAI-L2-2026.

---

### D5 — Corrective Feedback and Idiomatic Coaching

**Weight: 15**

Evaluates whether feedback is timely, concise, useful, evidence-sensitive, and capable of improving both correctness and naturalness without destroying conversational flow.

| Score | Anchor |
|---:|---|
| 1 | Gives no useful feedback, corrects nearly everything, interrupts with mini-lectures, supplies misleading replacements, or makes unsupported pronunciation claims. |
| 5 | Corrections are mostly accurate and relevant, but timing, brevity, prioritization, learner repair, or naturalness coaching is inconsistent. |
| 10 | Prioritizes blocked meaning, high-frequency natural expression, recurring patterns, and transferable errors; uses brief 3–8 second micro-corrections when useful; returns immediately to speaking; sometimes prompts one self-repair or repetition; defers longer explanations; and labels pronunciation evidence as clear, likely, or uncertain. |

**Common failures**

- Correcting cosmetic low-value errors mid-thought.
- Giving a natural phrase without explaining its intended context when ambiguity matters.
- Recasting every error without checking learner uptake.
- Treating transcript spelling as phoneme evidence.
- Framing non-native accent as failure despite intelligible speech.

**Evidence to check**

- correction events in a Live sample;
- correction duration and frequency;
- naturalness replacements;
- learner repetition or self-repair;
- pronunciation labels;
- deferred explanation behavior.

**Source refs:** SRC-PROJECT-RUNTIME, SRC-CF-LYSTER-SAITO, SRC-CF-RECAST, SRC-CEFR-PHONOLOGY, SRC-OPENAI-VOICE-2026.

---

### D6 — Timebox, Fatigue, and Session Economy

**Weight: 8**

Evaluates whether the session remains useful within the selected duration and responds sensibly to fatigue.

| Score | Anchor |
|---:|---|
| 1 | The plan clearly exceeds the selected duration, defaults to an unnecessarily long session, or uses all available time and omits closeout. |
| 5 | The session roughly fits, but activity timing is optimistic, optional material is not clearly disposable, or the final closeout is weakly protected. |
| 10 | The default 15-minute session contains one scenario, one main task, one repair loop, and protected closeout; 10/20/30-minute variants are explicit; optional content is dropped before time is extended; fatigue leads to shorter speaking tasks rather than longer explanations. |

**Common failures**

- Treating each section's maximum duration as mandatory.
- Adding a second role-play to a 15-minute day.
- Continuing correction after the closeout window begins.
- Interpreting fatigue as lack of motivation.

**Evidence to check**

- day time budget;
- actual or simulated session timing;
- closeout reservation;
- response to “I am tired” or “I only have five minutes left.”

**Source refs:** SRC-USER-DECISIONS, SRC-PROJECT-URD, SRC-PROJECT-RUNTIME.

---

### D7 — Session Evidence and State Integrity

**Weight: 10**

Evaluates whether the closeout creates a trustworthy, useful record instead of a generic summary.

| Score | Anchor |
|---:|---|
| 1 | Omits the session record, state patch, or next action; fabricates evidence; records every slip as recurring; or claims files were saved automatically. |
| 5 | Produces a usable summary and next step, but evidence categories are blurred, reusable phrases are incomplete, or state updates are not clearly traceable to the session. |
| 10 | Records completed work, observed strengths and blockers, high-value corrections, reusable expressions, pronunciation confidence labels, fatigue/time notes where relevant, topic intent, engagement-cause classification, and exactly one next action; distinguishes recurring patterns, one-off slips, and uncertainty; outputs a clear Markdown patch without claiming it was written. |

**Common failures**

- Vague “good job” summaries.
- Copying the plan into the session record instead of recording performance.
- Adding an error to canonical state after one uncertain occurrence.
- Writing several competing next actions.

**Evidence to check**

- session record;
- state patch;
- phrase-deck update;
- scenario-ledger update;
- next-action field;
- correspondence with observed interaction.

**Source refs:** SRC-PROJECT-URD, SRC-PROJECT-PLAYBOOKS, SRC-OPENAI-VOICE-2026.

---

### D8 — Cross-Cycle Adaptation and Retrieval

**Weight: 10**

Evaluates whether learning evidence changes the next session and next cycle in a meaningful, selective way.

| Score | Anchor |
|---:|---|
| 1 | Generates a generic next cycle, ignores available records, fabricates progress, or carries all prior targets forward without judgment. |
| 5 | Mentions prior errors, phrases, or scenarios but uses them superficially; continue/change/retire/test decisions are incomplete or weakly supported. |
| 10 | Cites concrete session evidence; makes explicit continue, change, retire, and test-next decisions; retrieves useful phrases; retests uncertainty; varies practiced scenarios; balances confirmed-interest depth with possible-interest tests and deliberate variety; adjusts cycle length or duration when evidence supports it; and produces a compact carry-over snapshot for the next evidence intake. |

**Common failures**

- Retiring a target after one successful use.
- Repeating the same scenario because it is easy to generate.
- Treating skipped sessions as failed performance.
- Ignoring learner interests or fatigue patterns recorded during the cycle.
- Confirming an interest from one casual mention, or treating one tired session as disinterest.
- Changing topics without preserving the language objective.

**Evidence to check**

- cycle review;
- next-cycle proposal;
- references to session records;
- carry-over snapshot;
- next cycle blueprint.

**Source refs:** SRC-PROJECT-URD, SRC-PROJECT-PLAYBOOKS, SRC-ACTFL-CANDO.

---

### D9 — Runtime Truthfulness and Compact Markdown Usability

**Weight: 5**

Evaluates whether the bundle and generated pack are realistically usable in the stated ChatGPT Live workflow.

| Score | Anchor |
|---:|---|
| 1 | Requires Python, hooks, a VM, connected apps, plugins, hidden state, or automatic GitHub writes; claims unsupported persistence; or produces an unreadably large and duplicative pack. |
| 5 | Uses Markdown and mostly respects runtime limits, but duplicates instructions, has unclear reading order, assumes uncertain capabilities, or produces avoidable operational clutter. |
| 10 | Produces compact, linked Markdown with a clear reading order and single authorities; requires no unavailable runtime; clearly separates returned text from actual file persistence; accounts for non-verbatim transcripts and current Live limitations; and remains practical to load for a short voice session. |

**Common failures**

- Duplicated correction rules in several generated files.
- Assuming ChatGPT Live can find files in a library or write to GitHub.
- Using transcript text as a complete audio record.
- Creating files with overlapping authority.

**Evidence to check**

- generated file count and reading order;
- runtime assumptions;
- persistence claims;
- duplicated policy text;
- explicit limitations.

**Source refs:** SRC-OPENAI-VOICE-2026, SRC-PROJECT-ADD, SRC-PROJECT-PLAYBOOKS.

## Weight Summary

| Dimension | Weight |
|---|---:|
| D1 Evidence fidelity and personalization | 12 |
| D2 Cycle focus, scope, and progression | 12 |
| D3 Authentic spoken tasks and learner output | 14 |
| D4 Live conversational orchestration | 14 |
| D5 Corrective feedback and idiomatic coaching | 15 |
| D6 Timebox, fatigue, and session economy | 8 |
| D7 Session evidence and state integrity | 10 |
| D8 Cross-cycle adaptation and retrieval | 10 |
| D9 Runtime truthfulness and Markdown usability | 5 |
| **Total** | **100** |

## Hard Gates

A hard-gate failure overrides the numeric score. The result is `FAIL` until the defect is corrected and retested.

| Gate ID | Hard gate | Failure condition |
|---|---|---|
| HG-01 | Speaking-first interaction | The primary session is not spoken-English practice, or the coach is explicitly instructed to dominate learner speaking time. |
| HG-02 | Pronunciation and accent integrity | The system makes confident phoneme-level claims without adequate audio evidence, treats transcript text as sufficient audio evidence, or requires native-like accent instead of intelligibility. |
| HG-03 | Timebox and closeout | The default 15-minute plan cannot plausibly fit, or a completed session omits closeout because time was consumed by activities or correction. |
| HG-04 | Persistence chain | A completed session lacks any of: session record, state patch, or exactly one next action. |
| HG-05 | Evidence truthfulness | The system fabricates learner performance, progress, completed sessions, or file/GitHub writes. |
| HG-06 | Continuity | A next-cycle proposal is generated despite available prior evidence but does not cite or use that evidence for planning decisions. |
| HG-07 | Runtime compatibility | The pack requires Python, hooks, a VM, hidden database, connected apps, plugins, or automatic repository writes in order to perform its core workflow. |
| HG-08 | Validation integrity | Validation silently repairs or approves a pack with blocking or major defects instead of reporting failure. |
| HG-09 | Current-event integrity | A current event is presented as current fact without fresh verification, exceeds the verification/context budget, violates recorded exclusions, lacks an evergreen fallback, or consumes the session as a news lecture. |
| HG-10 | Interest-inference integrity | Interest is promoted or downgraded from evidence primarily explained by language load, background knowledge, prompt/task quality, fatigue/time, privacy/sensitivity, or one isolated non-explicit signal. |

## Score Interpretation

| Domain score | Interpretation |
|---:|---|
| 90–100 | Strong: ready for sustained learner testing, assuming all hard gates pass. |
| 80–89.5 | Usable: good foundation, with targeted revisions recommended. |
| 70–79.5 | Weak: revise before regular use. |
| Below 70 | Reject for the current optimization round. |

A score marked `provisional` cannot be treated as evidence of real Live-session quality.

## Composite Scoring Recommendation

Use Darwin's common rubric together with this domain rubric:

```text
composite score = common score × 0.35 + domain score × 0.65
```

Rationale: structural skill quality matters, but most of the risk lies in whether the generated cycle and Live session actually support speaking practice. A hard-gate failure overrides the composite score.

For ratchet decisions, retain a modification only when:

1. no previously passing hard gate regresses;
2. the domain score strictly improves;
3. the composite score strictly improves, or a documented full-Live result improves while the composite change is within evaluator noise;
4. at least one independent judge or human reviewer confirms the claimed improvement.

## Policy Frozen for This Optimization Run

- `common_weight = 0.35`, `domain_weight = 0.65`;
- at least one observed Live session is required before a non-provisional score;
- default pronunciation target is clear, intelligible global English;
- v0.8 baseline uses the included example and adversarial simulations; personal learner evidence should be used for later deployment evaluation.

## Confidence Level

**Medium.** The rubric is evidence-backed and operational, but it has not yet been calibrated against longitudinal learner outcomes or independent teacher ratings.

## v0.8 Extension Notes

Version 0.3 extends D1, D2, D4, D7, and D8 with topic-intent balance, affinity/load separation, recent-topic control, and bounded current-event verification. HG-10 protects against false interest inference. It is frozen for the v0.8 Darwin optimization run; scores remain provisional until an observed Live session is available.
