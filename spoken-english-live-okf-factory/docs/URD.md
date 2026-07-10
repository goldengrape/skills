---
type: User Requirement Document
title: Spoken English Live OKF Factory URD
description: Confirmed user needs and acceptance criteria for a continuous, interest-aware spoken-English course-cycle factory.
tags: [urd, english, speaking, chatgpt-live, continuous-learning, adaptive-topics]
timestamp: 2026-07-09T21:30:00-07:00
---

# URD — Spoken English Live OKF Factory

## Context

The learner wants to practice spoken English with ChatGPT Live over an extended period. The learning unit is a short cycle—normally seven days, or three days for a focused sprint—not a one-time crash course. Each cycle must be usable on its own and preserve enough evidence to shape later sessions and cycles.

Spoken practice is cognitively tiring. The default session therefore lasts 15 minutes and prioritizes sustained speaking, timely coaching, and a short closeout.

Long-term adherence also depends on interest. A cycle should therefore stabilize **what language ability is being trained** while allowing some flexibility in **what the learner talks about**. ChatGPT Live may discover interests from conversation evidence, use those interests in later sessions, and optionally introduce freshly verified current events when they are suitable for the learner and the timebox.

## Roles

| ID | Role | Responsibility |
|---|---|---|
| URD-ROLE-001 | Learner | Speaks, repairs, repeats, expresses topic preferences, and manually saves records when desired. |
| URD-ROLE-002 | Factory agent | Reads learner input and prior evidence, then generates the next course cycle and topic policy. |
| URD-ROLE-003 | Live coach | Runs real-time voice sessions, selects adaptive topics, and gathers interest evidence without turning the lesson into an interview. |
| URD-ROLE-004 | Reviewer | Checks whether the pack, topic adaptations, and saved records are specific, usable, truthful, and continuous. |

## Goals

| ID | Goal |
|---|---|
| URD-GOAL-001 | Make short spoken-English practice sustainable over many cycles. |
| URD-GOAL-002 | Use ChatGPT Live’s real-time conversational ability as the main training medium. |
| URD-GOAL-003 | Improve clarity, fluency, naturalness, interaction, and scenario readiness through speaking and repair. |
| URD-GOAL-004 | Continue from explicit Markdown evidence instead of unstated model memory. |
| URD-GOAL-005 | Generate each new cycle from prior performance, learner interests, and current goals. |
| URD-GOAL-006 | Preserve learning interest through evidence-based topic adaptation without allowing the curriculum to drift into unguided chat. |

## Confirmed Functional Requirements

| ID | Requirement | Measurable success condition |
|---|---|---|
| URD-REQ-001 | Accept a learner brief, cycle preferences, correction preferences, topic preferences, and optional prior evidence. | Missing non-critical information is defaulted explicitly; assumptions, conflicts, and evidence gaps are visible before course generation. |
| URD-REQ-002 | Generate a focused three-day or seven-day spoken-English cycle that fits the learner’s goal, evidence, interests, and available time. | The cycle has no more than three primary language targets; every day contains a language objective, a speaking task, a repair or transfer task, and a time budget. |
| URD-REQ-003 | Separate stable language objectives from adaptable conversation topics. | Every day declares a fixed language function. Adaptive days also declare a topic mode, selection rule, and concrete fallback topic. |
| URD-REQ-004 | Let ChatGPT Live run natural real-time practice rather than a written worksheet. | The learner speaks for most of the session; the coach asks one useful question at a time, uses short follow-ups, and moves into English quickly. |
| URD-REQ-005 | Allow brief live correction for clarity, recurring errors, and more idiomatic expression without turning the session into a lecture. | A live correction is one-breath, actionable, and followed immediately by continued speaking or one brief repetition; the learner can request more correction, less correction, explanation, skipping, or wrap-up. |
| URD-REQ-006 | Discover and maintain learner interests from explicit preference and repeated conversational evidence. | Interest state distinguishes explicit/confirmed, possible, low-engagement, avoided, and retired topics; topic affinity is separated from language load, background knowledge, prompt/task quality, fatigue/time, and privacy; one casual mention or one difficult session is not overinterpreted. |
| URD-REQ-007 | Optionally use relevant news or current events as short conversation material. | A current event is used only when enabled, verified within a short runtime budget, aligned with the language objective and interest policy, presented as a compact context capsule, and accompanied by an evergreen fallback. |
| URD-REQ-008 | Produce a copyable Markdown record after every session. | The record contains the completed task, topic-selection basis, evidence class, strengths and blockers, high-value corrections, learner uptake, interest signals, current-event provenance when used, reusable expressions, and exactly one next action. |
| URD-REQ-009 | Continue sessions and cycles from saved evidence rather than model memory. | The next session or cycle cites prior evidence for at least two planning decisions when prior records exist. |
| URD-REQ-010 | Adapt the next session and cycle from progress, recurring errors, scenario coverage, learner interests, and fatigue or time preference. | Session closeout may recommend the next adaptive topic without silently rewriting files; cycle rollover states what to continue, change, retire, and test next. |
| URD-REQ-011 | Reject packs or records that are incomplete, generic, overlong, overcorrecting, falsely precise, or factually unsafe in their use of current events. | Validation returns pass/fail with concrete defects and does not silently repair or approve an invalid artifact. |

## Constraints

| ID | Constraint |
|---|---|
| URD-CON-001 | The default cycle length is 7 days; a focused 3-day cycle is supported. |
| URD-CON-002 | The default daily session is 15 minutes. The learner may explicitly select 10, 20, or 30 minutes. |
| URD-CON-003 | The selected duration is a hard limit; activity timing may flex. |
| URD-CON-004 | Persistent artifacts are Markdown. The course must not require Python, hooks, a virtual machine, or a hidden local database. |
| URD-CON-005 | The system must not claim that ChatGPT Live saved, committed, or uploaded files unless the learner actually performs that action. |
| URD-CON-006 | Practice is mostly English. Chinese may be used for brief setup, difficult explanations, and debrief. |
| URD-CON-007 | The system must distinguish clear audio evidence, a likely issue, and uncertainty. It must not claim phoneme-level certainty without evidence. |
| URD-CON-008 | The system must not infer intelligence, diligence, personality, or motivation from language errors or topic engagement. |
| URD-CON-009 | The generated artifact set must remain compact enough for a voice agent to read without operational clutter. |
| URD-CON-010 | The system optimizes communicative performance and natural expression, not perfect written grammar. |
| URD-CON-011 | Runtime plans must remain useful without exact timer tooling; sequence and turn budgets provide the fallback. |
| URD-CON-012 | A one-off slip, candidate pattern, recurring pattern, and stable phrase must not be treated as equivalent evidence. |
| URD-CON-013 | The default topic policy is `guided_adaptive`: language targets remain stable while some topic slots adapt. |
| URD-CON-014 | A single mention is only a possible interest unless the learner explicitly identifies it as an interest. |
| URD-CON-015 | Low engagement must not be treated as topic dislike when fatigue, language load, background knowledge, prompt/task quality, or privacy is a plausible cause. |
| URD-CON-016 | A future adaptive day must include an evergreen fallback and must not depend on a news event being available. |
| URD-CON-017 | Current-event facts must be verified at session time. If verification is unavailable or uncertain, use the fallback topic. |
| URD-CON-018 | Current-event verification should stop after 30 seconds; context should take no more than two or three short sentences before learner speech begins. |
| URD-CON-019 | Sensitive categories are opt-in or learner-configured; popularity alone does not make a topic suitable. |

## In Scope

| ID | In-scope capability |
|---|---|
| URD-SCOPE-001 | Learner-specific cycle generation. |
| URD-SCOPE-002 | Real-time role-play, guided conversation, free response, repair, repetition, and transfer. |
| URD-SCOPE-003 | Brief live corrections, including naturalness upgrades. |
| URD-SCOPE-004 | Evidence-based interest discovery and adaptive topic choice. |
| URD-SCOPE-005 | Optional, verified current-event discussion as conversation material. |
| URD-SCOPE-006 | Markdown session records and learner state. |
| URD-SCOPE-007 | Cycle review and next-cycle proposal. |
| URD-SCOPE-008 | Structural and learning-quality validation. |

## Out of Scope for This Version

| ID | Out-of-scope item |
|---|---|
| URD-OOS-001 | Automatic audio recording or storage. |
| URD-OOS-002 | Precise phoneme scoring or accent certification. |
| URD-OOS-003 | Automatic GitHub commits, calendar integration, or LMS integration. |
| URD-OOS-004 | Multi-user classroom management. |
| URD-OOS-005 | High-stakes exam score prediction or guaranteed CEFR improvement. |
| URD-OOS-006 | A general-purpose written English curriculum. |
| URD-OOS-007 | A general news briefing service or political persuasion system. |

## Acceptance Criteria

| ID | Traces to | Acceptance criterion |
|---|---|---|
| URD-AC-001 | URD-REQ-001 | Given incomplete input, the factory produces an explicit normalized brief with defaults and evidence gaps. |
| URD-AC-002 | URD-REQ-002 | Given `cycle_days=7` and `daily_minutes=15`, the factory generates seven distinct, usable daily speaking plans that fit the time limit. |
| URD-AC-003 | URD-REQ-002, URD-REQ-003 | A seven-day guided-adaptive cycle normally contains both anchored and adaptive-capable days, while every day retains a fixed language objective. |
| URD-AC-004 | URD-REQ-003 | An adaptive day has a concrete fallback topic, selection inputs, and a rule for preserving the original language objective. |
| URD-AC-005 | URD-REQ-004 | A Live session can begin from the generated pack without requiring code execution or a written exercise engine. |
| URD-AC-006 | URD-REQ-005 | The runtime permits “Quick fix: say X. Go on,” while rejecting long or repeated lecture-like interruptions. |
| URD-AC-007 | URD-REQ-006 | An explicit interest may be confirmed immediately; an observed but unrequested interest requires repeated evidence before confirmation. |
| URD-AC-008 | URD-REQ-006 | One low-energy, language-heavy, knowledge-heavy, poorly prompted, or privacy-sensitive session cannot move a topic into low-engagement or retired status. |
| URD-AC-009 | URD-REQ-007 | A current-event slot states verification and fallback rules rather than hardcoding an unverified future news item. |
| URD-AC-010 | URD-REQ-007 | When a current event is used, the session record includes event date, verification date, source name, relevance, and confidence. |
| URD-AC-011 | URD-REQ-008 | Every completed session produces one self-contained Markdown record, one state patch, and one explicit next action. |
| URD-AC-012 | URD-REQ-009 | A new session can identify the current day, active language target, topic policy, recent evidence, and next action from saved files alone. |
| URD-AC-013 | URD-REQ-010 | A cycle-end review produces evidence-backed language and topic decisions for the next cycle. |
| URD-AC-014 | URD-REQ-011 | A generic plan with no named fallback scenario or speaking task fails validation. |
| URD-AC-015 | URD-REQ-011 | A default plan longer than 15 minutes, a missing closeout, unsupported pronunciation certainty, or a hidden runtime dependency fails validation. |
| URD-AC-016 | URD-REQ-011 | A plan that requires unverified news, searches beyond the verification budget, ignores excluded categories, or spends most of the session on background explanation fails validation. |
| URD-AC-017 | URD-REQ-008, URD-REQ-009 | A session record cannot promote a recurring pattern, stable phrase, or confirmed interest without threshold evidence or an explicit learner statement. |
| URD-AC-018 | URD-REQ-010 | A materially new next-cycle direction triggers a visible learner checkpoint before materialization. |
| URD-AC-019 | URD-REQ-003, URD-REQ-006, URD-REQ-010 | A seven-day guided-adaptive cycle does not let one broad topic occupy more than three sessions unless the learner explicitly requests a thematic cycle; repeated topics use a different language function, pressure, or perspective. |

## Assumptions

| ID | Assumption |
|---|---|
| URD-ASM-001 | ChatGPT Live can read supplied course files or an accessible repository. |
| URD-ASM-002 | The learner is willing to copy or save the session record when continuity across chats is desired. |
| URD-ASM-003 | Voice recognition and transcripts may be imperfect; pronunciation notes require confidence labels. |
| URD-ASM-004 | A cycle may be regenerated when available time, interests, or goals change. |
| URD-ASM-005 | Current-event use depends on current web access; the course remains usable without it. |

## Open Questions

| ID | Question | Current default |
|---|---|---|
| URD-Q-001 | Which English variety is the target? | Clear global English unless the learner selects another target. |
| URD-Q-002 | How much state remains active before older records are archived? | Current cycle, previous review, active errors, active phrases, scenario history, and current interest state. |
| URD-Q-003 | Which current-event categories are welcome? | Disabled until the learner enables it; then technology, science, culture, and lifestyle are suggested defaults. |
| URD-Q-004 | Which categories should be avoided? | None assumed; the factory asks or records exclusions before using sensitive subjects. |
