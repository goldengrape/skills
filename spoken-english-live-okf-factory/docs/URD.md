---
type: User Requirement Document
title: Spoken English Live OKF Factory URD
description: Confirmed user needs and acceptance criteria for a continuous spoken-English course-cycle factory.
tags: [urd, english, speaking, chatgpt-live, continuous-learning]
timestamp: 2026-07-09T18:10:00-07:00
---

# URD — Spoken English Live OKF Factory

## Context

The learner wants to practice spoken English with ChatGPT Live over an extended period. The learning unit is a short cycle—normally seven days, or three days for a focused sprint—not a one-time crash course. Each cycle must be usable on its own and must also preserve enough evidence to shape the next cycle.

Spoken practice is cognitively tiring. The default session therefore lasts 15 minutes and should prioritize sustained speaking, timely coaching, and a short closeout rather than a large volume of exercises.

## Roles

| ID | Role | Responsibility |
|---|---|---|
| URD-ROLE-001 | Learner | Speaks, repairs, repeats, reviews, and manually saves session records when desired. |
| URD-ROLE-002 | Factory agent | Reads learner input and prior evidence, then generates the next course cycle. |
| URD-ROLE-003 | Live coach | Runs a real-time voice session in ChatGPT Live using the generated pack. |
| URD-ROLE-004 | Reviewer | Checks whether the generated pack and saved records are specific, usable, and continuous. |

## Goals

| ID | Goal |
|---|---|
| URD-GOAL-001 | Make short spoken-English practice sustainable over many cycles. |
| URD-GOAL-002 | Use ChatGPT Live’s real-time conversational ability as the main training medium. |
| URD-GOAL-003 | Improve clarity, fluency, naturalness, and scenario readiness through speaking and repair. |
| URD-GOAL-004 | Continue from explicit Markdown evidence instead of unstated model memory. |
| URD-GOAL-005 | Generate each new cycle from prior performance, learner interests, and current goals. |

## Confirmed Functional Requirements

| ID | Requirement | Measurable success condition |
|---|---|---|
| URD-REQ-001 | Accept a learner brief, cycle preferences, correction preferences, and optional prior learning evidence. | Missing non-critical information is defaulted explicitly; assumptions and evidence gaps are visible before course generation. |
| URD-REQ-002 | Generate a focused three-day or seven-day spoken-English cycle that fits the learner’s goal, evidence, interests, and available time. | The cycle has no more than three primary targets; each day contains a named scenario, a speaking task, a repair or transfer task, and a time budget. |
| URD-REQ-003 | Let ChatGPT Live run natural real-time practice rather than a written worksheet. | The learner speaks for most of the session; the coach asks one useful question at a time, uses short follow-ups, and moves into English quickly. |
| URD-REQ-004 | Allow brief live correction for clarity, recurring errors, and more idiomatic expression without turning the session into a lecture. | A live correction is one-breath, actionable, and followed immediately by continued speaking or one brief repetition; the learner can request more correction, less correction, explanation, skipping, or immediate wrap-up. |
| URD-REQ-005 | Produce a copyable Markdown record after every session. | The record contains the completed task, evidence class, observed strengths and blockers, high-value corrections, learner uptake, reusable expressions, pronunciation confidence where relevant, and exactly one next action. |
| URD-REQ-006 | Continue sessions and cycles from saved evidence rather than model memory. | The next session or cycle cites prior evidence for at least two planning decisions when prior records exist. |
| URD-REQ-007 | Adapt the next cycle from progress, recurring errors, scenario coverage, learner interests, and fatigue or time preference. | The cycle-end proposal states what to continue, change, retire, and test next, then recommends a three-day or seven-day focus. |
| URD-REQ-008 | Reject course packs or session records that are incomplete, generic, overlong, overcorrecting, or falsely precise. | Validation returns pass/fail with concrete defects and does not silently repair or approve an invalid pack. |

## Constraints

| ID | Constraint |
|---|---|
| URD-CON-001 | The default cycle length is 7 days; a focused 3-day cycle is supported. |
| URD-CON-002 | The default daily session is 15 minutes. The learner may explicitly select 10, 20, or 30 minutes. |
| URD-CON-003 | The selected session duration is a hard limit; activity timing inside the session may flex. |
| URD-CON-004 | Persistent artifacts are Markdown. The course must not require Python, hooks, a virtual machine, or a hidden local database. |
| URD-CON-005 | The system must not claim that ChatGPT Live saved, committed, or uploaded files unless the learner actually performs that action. |
| URD-CON-006 | Practice is mostly English. Chinese may be used for brief setup, difficult explanations, and debrief. |
| URD-CON-007 | The system must distinguish clear audio evidence, a likely issue, and uncertainty. It must not claim phoneme-level certainty without evidence. |
| URD-CON-008 | The system must not infer intelligence, diligence, personality, or motivation from language errors. |
| URD-CON-009 | The generated artifact set must remain compact enough for a voice agent to read without operational clutter. |
| URD-CON-010 | The system optimizes communicative performance and natural expression, not perfect written grammar. |
| URD-CON-011 | Runtime plans must remain useful without exact timer tooling; sequence and turn budgets provide the fallback. |
| URD-CON-012 | A one-off slip, candidate pattern, recurring pattern, and stable phrase must not be treated as equivalent evidence. |

## In Scope

| ID | In-scope capability |
|---|---|
| URD-SCOPE-001 | Learner-specific cycle generation. |
| URD-SCOPE-002 | Real-time role-play, guided conversation, free response, repair, repetition, and transfer. |
| URD-SCOPE-003 | Brief live corrections, including naturalness upgrades. |
| URD-SCOPE-004 | Markdown session records and learner state. |
| URD-SCOPE-005 | Cycle review and next-cycle proposal. |
| URD-SCOPE-006 | Structural and learning-quality validation. |

## Out of Scope for This Version

| ID | Out-of-scope item |
|---|---|
| URD-OOS-001 | Automatic audio recording or storage. |
| URD-OOS-002 | Precise phoneme scoring or accent certification. |
| URD-OOS-003 | Automatic GitHub commits, calendar integration, or LMS integration. |
| URD-OOS-004 | Multi-user classroom management. |
| URD-OOS-005 | High-stakes exam score prediction or guaranteed CEFR improvement. |
| URD-OOS-006 | A general-purpose written English curriculum. |

## Acceptance Criteria

| ID | Traces to | Acceptance criterion |
|---|---|---|
| URD-AC-001 | URD-REQ-001 | Given incomplete learner input, the factory produces an explicit normalized brief with defaults and evidence gaps. |
| URD-AC-002 | URD-REQ-002 | Given `cycle_days=7` and `daily_minutes=15`, the factory generates seven distinct, usable daily speaking plans that fit the time limit. |
| URD-AC-003 | URD-REQ-002, URD-REQ-007 | Given prior recurring errors and interests, the next cycle addresses the top one to three repair needs and uses at least one relevant interest or target scenario. |
| URD-AC-004 | URD-REQ-003 | A Live session can begin from the generated pack without requiring code execution or a written exercise engine. |
| URD-AC-005 | URD-REQ-004 | The runtime protocol permits a short cue such as “Quick fix: say X. Go on,” while rejecting long or repeated lecture-like interruptions. |
| URD-AC-006 | URD-REQ-005 | Every completed session produces one self-contained Markdown record and one explicit next action. |
| URD-AC-007 | URD-REQ-006 | A new session can identify the current day, recent evidence, active repair targets, and next action from saved files alone. |
| URD-AC-008 | URD-REQ-007 | A cycle-end review produces a concrete next-cycle proposal with evidence-backed priorities. |
| URD-AC-009 | URD-REQ-008 | A generic plan with no named scenarios or speaking tasks fails validation. |
| URD-AC-010 | URD-REQ-008 | A default plan longer than 15 minutes, a missing closeout, unsupported pronunciation certainty, or a hidden runtime dependency fails validation. |
| URD-AC-011 | URD-REQ-004 | During a simulated correction sequence, every live intervention fits one breath, corrects one item, and returns immediately to the learner. |
| URD-AC-012 | URD-REQ-005, URD-REQ-006 | A session record cannot promote a recurring pattern or stable phrase without threshold evidence or an explicit high-impact exception. |
| URD-AC-013 | URD-REQ-007 | A materially new next-cycle direction triggers a visible learner checkpoint before materialization. |

## Assumptions

| ID | Assumption |
|---|---|
| URD-ASM-001 | ChatGPT Live can read the course files supplied in the current project, upload context, or accessible repository. |
| URD-ASM-002 | The learner is willing to copy or save the session record when continuity across chats is desired. |
| URD-ASM-003 | Voice recognition and transcripts may be imperfect; therefore pronunciation notes require confidence labels. |
| URD-ASM-004 | A cycle may be regenerated when the learner’s available time, interests, or goals change. |

## Open Questions

| ID | Question | Current default |
|---|---|---|
| URD-Q-001 | Which English variety is the target? | Clear global English unless the learner selects American, British, or another target. |
| URD-Q-002 | How much state should remain active before older records are archived? | Keep the current cycle, the previous cycle review, active errors, active phrases, and scenario history; archive older session records manually. |


## Confirmation Summary

Confirmed:

- continuous learning is represented as linked 3-day or 7-day cycles;
- the default Live session is 15 minutes;
- brief real-time correction and naturalness coaching are allowed;
- every session ends with a Markdown record and next action;
- continuity comes from saved evidence, not assumed model memory;
- the factory and generated packs require no executable runtime.

Still configurable rather than blocking:

- target English variety;
- when older session records should be archived.
