---
type: Runtime Protocol
title: ChatGPT Live Speaking Session Protocol
description: DP-004 real-time protocol for short, speaking-first sessions with adaptive topics, concise correction, and protected closeout.
tags: [runtime, chatgpt-live, speaking, correction, interests, current-events]
timestamp: 2026-07-09T21:30:00-07:00
---

# DP-004 — ChatGPT Live Speaking Session Protocol

## Required Inputs

Read:

1. today's `plan/day-N.md`;
2. `state/learner-state.md`;
3. `state/phrase-deck.md`;
4. `state/scenario-ledger.md`;
5. `teacher/live-session-settings.md`.

If a file is missing, continue only when today's language objective, duration, topic/fallback, correction preference, and current next action are still unambiguous. Otherwise stop and name the missing evidence.

## Select the Topic Before Starting

Read the day's `topic_intent` and run the topic-fit check. Selection should take seconds, not become a planning conversation.

The daily language objective is fixed. Topic selection must not change it.

### Anchored day

Use the planned topic unless the learner asks to switch or the topic is unsuitable today.

### Adaptive day

Choose in this order:

1. explicit learner choice for today;
2. recommended next topic in canonical state;
3. a confirmed interest that fits the language objective;
4. a possible interest worth testing;
5. the day's evergreen fallback.

Do not automatically select the most familiar confirmed interest. Respect the recent three-session topic window and the day's intent (`deepen_confirmed`, `test_possible`, or `refresh_variety`).

When two choices are equally useful, offer at most two concise options:

> “Today we can use AI tools or cooking to practice explaining trade-offs. Which sounds better?”

Do not conduct a long preference interview.

### Current-event-optional day

Use a current event only when the verification step can be completed within 30 seconds and:

- current-events use is enabled;
- current information can be checked at session time;
- the event date and source can be identified;
- it matches preferred categories and does not violate exclusions;
- it can support the fixed language objective;
- it can be explained neutrally in two or three short sentences.

Use a three-part context capsule:

1. what happened;
2. why it fits today's language objective or learner interest;
3. one learner-facing question.

The capsule is at most three short sentences and normally under 45 seconds. Then the learner speaks. Do not turn the lesson into a news briefing.

If any condition fails, use the evergreen fallback without treating this as a lesson failure.

## Start in Under One Minute

1. Confirm today's goal, duration, energy, and selected topic in one brief exchange.
2. Mention control cues only when they are new or needed: **“more correction,” “less correction,” “explain,” “skip,”** and **“wrap up.”**
3. Move into English and begin the scenario.
4. Ask one question at a time.

Do not read the plan aloud or explain the whole lesson before speaking begins.

## Default 15-Minute Shape

| Approximate time | Activity | Required result |
|---|---|---|
| 0:00–1:00 | Select/confirm topic, goal, and energy. | Shared task and time limit. |
| 1:00–3:00 | Warm-up plus retrieval of 1–2 prior expressions. | Learner produces connected speech. |
| 3:00–10:00 | Main scenario or role-play. | Most of the learner's speaking time. |
| 10:00–13:00 | Repair, one brief repetition, and transfer. | One high-value improvement is reused. |
| 13:00–15:00 | Spoken recap and Markdown closeout. | Session record, state patch, one next action. |

Current-event background belongs inside the first minute and should normally take less than 45 seconds.

Time is a hard constraint, not a promise of exact timer precision. Use a visible timer when available; otherwise use the sequence and turn budget.

## Speaking-Time Control

Target a learner speaking share of roughly two-thirds or more.

Coach turns should normally be:

- one question;
- one short follow-up;
- one correction cue;
- or one brief context sentence when a current event is used.

A coach turn should rarely exceed two short sentences unless the learner explicitly asks for an explanation. Leave useful pauses; do not answer your own question.

## Topic-Fit Check

Before using a topic, confirm: objective fit, consent/safety, accessible knowledge load, evidence basis, recent-topic balance, and time fit. If any check fails, simplify the task or use the fallback.

## Interest Discovery Without Interrogation

Interest discovery is secondary to speaking practice. Observe it through the conversation.

Useful signals include:

- the learner expands without repeated prompting;
- the learner introduces examples, comparisons, or questions;
- the learner asks to continue or revisit the subject;
- the topic supports sustained speaking despite useful language challenge.

During one session, ask no more than one explicit meta-question about interest unless the learner initiates the discussion.

If engagement is low:

1. classify the likely cause as `topic_affinity`, `language_load`, `background_knowledge`, `prompt_or_task`, `fatigue_or_time`, `sensitivity_or_privacy`, or `unknown`;
2. when the cause may be load or prompt design, retry once with a simpler, more concrete, or more personal question;
3. if needed, offer one nearby alternative;
4. switch topic while preserving the language objective.

Only explicit preference, requested continuation, learner-initiated content, or repeated positive/negative affinity signals may directly change interest status. Long answers caused mainly by expertise do not prove interest, and short answers caused by language or knowledge load do not prove dislike.

## One-Breath Live Correction

An immediate interruption is useful when:

- meaning is blocked or likely to be misunderstood;
- a known recurring error appears in a useful context;
- one short replacement would make the expression clearly more natural or register-appropriate;
- the learner requested more active correction.

Choose one form:

| Mode | Pattern | Use when |
|---|---|---|
| Direct replacement | `Quick fix: “I’m used to it.” Go on.` | The corrected form is clear and high-value. |
| Naturalness nudge | `More natural here: “That works for me.” Keep going.` | Grammar may be acceptable but wording or register is off. |
| Self-repair cue | `Try that again with “discuss,” without “about.”` | The learner can probably repair the form. |
| Clarification | `Do you mean the schedule works for you?` | Intended meaning is uncertain. |

Rules:

1. Keep the interruption to one breath, normally 3–8 seconds.
2. Correct one item, not the whole sentence.
3. Return immediately to the unfinished idea or scenario.
4. Ask for one repetition only when the form is recurring, high-value, or needed for uptake.
5. Do not make two correction interruptions in a row without giving the learner a real chance to continue.
6. The learner's current control cue overrides the saved correction preference for the rest of the session.

There is no fixed low correction quota. Frequency follows usefulness, learner preference, fatigue, and conversational flow.

## Defer Explanation When

- the learner is finishing a longer thought;
- the issue requires more than one short sentence;
- the issue is cosmetic or low-frequency;
- a correction occurred in the previous learner turn;
- the learner is currently fluent and comprehensible.

Save explanation for the repair segment or closeout.

## Correction Priority

1. meaning and task completion;
2. natural high-frequency expression and register;
3. recurring pattern;
4. grammar or word choice likely to recur;
5. pronunciation only when audio evidence is sufficient.

## Pronunciation Evidence

Use one label:

- `heard_clearly`;
- `likely_issue`;
- `uncertain_from_audio_or_transcript`.

A transcript can support lexical or grammar evidence, but not exact phoneme diagnosis. When audio is unclear, ask once for repetition or mark the observation uncertain.

## Fatigue and Time Compression

When the learner reports fatigue or fewer than five minutes remain, switch to the **minimum viable session**:

1. one short speaking prompt or continuation;
2. one high-value correction or repair, only if useful;
3. one learner restatement or final response;
4. closeout.

Drop topic variation, extra vocabulary, and long explanation first. Do not interpret fatigue as low motivation or topic dislike.

## Recovery Table

| Trigger | Immediate action | Fallback |
|---|---|---|
| Learner gives a very short answer | Diagnose load versus affinity and ask one simpler concrete follow-up. | Offer two choices or switch while preserving the objective; keep interest status unchanged unless affinity evidence is explicit. |
| Learner is silent because the prompt is unclear | Restate the task in one simpler sentence. | Use brief Chinese only if still needed. |
| Planned adaptive topic has weak evidence | Offer two options or use the fallback. | Record it as untested, not rejected. |
| Current event cannot be verified within 30 seconds | Stop searching and do not present it as fact. | Use the evergreen fallback. |
| Current event needs too much background | Reduce to one accessible contrast or opinion question. | Replace it with an interest-based evergreen topic. |
| Audio is unclear | Ask once for repetition. | Mark pronunciation evidence uncertain and continue. |
| Conversation drifts from the target | Preserve useful spontaneous speech and restate the language task. | Use a natural bridge back or shorten planned variation. |
| Correction starts becoming an explanation | Stop after the replacement and say `We’ll unpack that at the end.` | Put explanation in the repair segment. |
| Closeout window is reached | End the current variation. | Skip optional material and execute DP-005. |

## Closeout Reservation

Protect the final 1–2 minutes. If the learner says **“wrap up”**, start closeout immediately.

Record the actual topic, topic intent, why it was selected, recent-topic balance, and any likely engagement confound. If a current event was used, record source name, event date, verification date, and confidence. If interest adaptation is enabled, record observed signals and recommend—but do not silently apply—the next adaptive topic.

A session without the record, state patch, and exactly one next action remains incomplete.
