---
type: Domain Research
title: Spoken English Live OKF Factory Domain Research
description: Evidence base for evaluating a Markdown-first factory that generates continuous ChatGPT Live spoken-English course cycles.
tags: [darwin, domain-research, english-speaking, chatgpt-live, evaluation]
timestamp: 2026-07-09T19:05:00-07:00
---

# Domain Research — Spoken English Live OKF Factory

## Research Scope

This research defines what good performance means for the `spoken-english-live-okf-factory` as a complete task system. The evaluation target is not the learner's English proficiency by itself. It is the factory's ability to:

1. turn learner evidence into a bounded three-day or seven-day course cycle;
2. generate compact Markdown artifacts that ChatGPT Live can read;
3. run a short, natural, speaking-first Live session;
4. provide useful, concise corrective feedback, including naturalness coaching;
5. create trustworthy session evidence and carry it into the next cycle.

The scope therefore includes factory output, Live runtime behavior, closeout records, and cross-cycle rollover.

## Skill Goal Summary

The target bundle should support long-term spoken-English practice as a sequence of short course cycles. The default daily session is 15 minutes. ChatGPT Live acts as the conversational coach, while durable state is represented as copyable Markdown rather than Python, hooks, hidden databases, or claimed automatic writes.

## Expected Task Outcome

A successful execution produces:

- an evidence-grounded, learner-specific cycle with no more than three primary targets;
- daily plans centered on spontaneous spoken interaction and meaningful scenarios;
- Live sessions in which the learner speaks more than the coach;
- brief, timely corrections that improve clarity, recurring patterns, or idiomatic naturalness without turning into lectures;
- a session record that distinguishes observed success, recurring problems, one-off slips, and uncertain pronunciation evidence;
- one explicit next action;
- a cycle review and next-cycle proposal grounded in prior session evidence.

## Available Evidence

### Project and user evidence

| Source ID | Evidence | Use |
|---|---|---|
| SRC-PROJECT-URD | `docs/URD.md` | Defines the user-confirmed goals, constraints, timebox, correction behavior, Markdown persistence, and continuity requirements. |
| SRC-PROJECT-ADD | `docs/ADD.md` | Defines the seven ordered responsibilities and lower-triangular architecture. |
| SRC-PROJECT-RUNTIME | `runtime/live-session-protocol.md` | Defines turn-taking, micro-correction, pronunciation confidence labels, and protected closeout time. |
| SRC-PROJECT-PLAYBOOKS | `contracts/`, `playbooks/`, and `schemas/` | Defines evidence intake, blueprint derivation, pack generation, closeout, rollover, and validation. |
| SRC-USER-DECISIONS | Conversation decisions dated 2026-07-09 | Confirms continuous cycles, Markdown-only records, 15-minute default sessions, and permission for short live interruptions that quickly return the learner to speaking. |

### External standards and research

| Source ID | Source | Key contribution |
|---|---|---|
| SRC-OPENAI-VOICE-2026 | OpenAI Help Center, “ChatGPT Voice,” updated 2026-07-09 | Live supports natural back-and-forth, simultaneous listening and speaking, and interruptions. Current limitations include no initial connected-app/plugin support and non-verbatim transcripts. |
| SRC-CEFR-SPOKEN | Council of Europe, CEFR qualitative aspects of spoken language use | Spoken performance can be examined through range, accuracy, fluency, interaction, and coherence. |
| SRC-CEFR-PHONOLOGY | Council of Europe, CEFR phonological competence | Pronunciation evaluation should prioritize intelligibility and prosody rather than native-like accent. The framework distinguishes overall phonological control, sound articulation, and prosody. |
| SRC-ACTFL-FACT | ACTFL Proficiency Guidelines 2024 overview | Real-world proficiency is spontaneous and unrehearsed; assessment considers functions/tasks, accuracy, context/content, and text type. |
| SRC-ACTFL-CANDO | NCSSFL-ACTFL Can-Do Statements 2026 | Learning targets should support goal setting, progress tracking, and interpersonal negotiation of meaning. |
| SRC-ACTFL-OPI | ACTFL Oral Proficiency Interview overview | Speaking quality should be tested in real-life, spontaneous, unrehearsed interaction rather than only scripted exercises. |
| SRC-CF-LYSTER-SAITO | Lyster & Saito, 2010, meta-analysis of oral corrective feedback | Corrective feedback had significant and durable effects; prompts outperformed recasts in the analyzed classroom studies, especially on free constructed responses. |
| SRC-CF-RECAST | Miller & Pan, 2012, meta-analytic review of recasts | Recasts can preserve conversational flow, but effects are heterogeneous; correction type should therefore be selected by context rather than treated as universally optimal. |
| SRC-GENAI-L2-2026 | He et al., 2026, preprint on GenAI-mediated L2 oral practice | Emerging evidence associates higher-progress sessions with more learner-initiated questions and prompting-based corrective-feedback sequences after learner responses. This source is treated as preliminary, not as a hard standard. |

## Research Method

The research used:

1. user-provided project materials and prior design decisions;
2. direct inspection of the current v0.4 OKF bundle;
3. official OpenAI product documentation for current Live capabilities and limits;
4. official CEFR and ACTFL speaking frameworks;
5. peer-reviewed corrective-feedback research;
6. one recent GenAI oral-practice preprint as low-weight emerging evidence.

The rubric does not copy CEFR or ACTFL level descriptors as a learner-proficiency test. It uses their constructs to judge whether the factory creates credible speaking practice and observable evidence.

## Key Findings

### KF-001 — Real spoken performance must dominate

A valid course cannot be mostly explanation, vocabulary display, reading, or written worksheets. It must elicit spontaneous, unrehearsed speech in realistic interpersonal tasks. The learner should accomplish communicative functions in an identifiable context.

### KF-002 — Interaction quality is distinct from language-content quality

A well-written plan can still produce a poor Live session if the coach gives long prompts, fills pauses, asks several questions at once, or dominates speaking time. Live orchestration therefore requires its own scoring dimension.

### KF-003 — Naturalness correction is a legitimate primary outcome

The user explicitly wants corrections that make speech more idiomatic, not only grammar correction. High-quality feedback should prioritize meaning, common natural expression, recurring patterns, and learner uptake.

### KF-004 — Brief interruption is useful when calibrated

The design should not impose a blanket “never interrupt” rule. A short correction can preserve flow and improve immediate use. However, repeated or lecture-like interruptions damage speaking time. The evaluator must examine timing, length, relevance, and whether the learner resumes speaking immediately.

### KF-005 — Correction should elicit learner repair, not only provide an answer

Research supports corrective feedback generally and gives particular support to prompts. The session should sometimes ask for one brief repetition or self-repair after a high-value correction rather than only replacing the learner's wording.

### KF-006 — Pronunciation claims need stricter evidence controls

ChatGPT Voice transcripts are not verbatim and may diverge when speech overlaps, noise is present, or conversation moves quickly. Pronunciation evaluation must distinguish directly heard evidence, a likely issue, and uncertainty. Native-like accent is not an appropriate default target; intelligibility and prosody matter more.

### KF-007 — Fifteen minutes is a hard design constraint, not a suggestion

The default session must fit one scenario, one main speaking task, one repair loop, and closeout. The final one to two minutes must remain available for a spoken recap and Markdown record. Optional content should be dropped before the time limit is extended.

### KF-008 — Continuity requires evidence fidelity

The next day and next cycle must cite saved evidence. The system should not fabricate progress, convert every slip into a recurring error, or carry every old target forward automatically.

### KF-009 — Artifact quality and runtime quality need separate evidence

Static file inspection can evaluate personalization, scope, progression, compactness, and state structure. It cannot fully validate turn-taking, correction timing, learner speaking share, fatigue response, or audio confidence. Those require a real Live test or a clearly labeled interaction simulation.

## Candidate Evaluation Concerns

1. Evidence fidelity and personalization.
2. Bounded cycle focus and progression.
3. Authentic spoken-task design and learner output opportunity.
4. Live conversational orchestration.
5. Corrective-feedback and idiomatic-coaching quality.
6. Timebox and fatigue management.
7. Session evidence and state integrity.
8. Cross-cycle adaptation and retrieval.
9. Runtime truthfulness and compact Markdown usability.

## Common Failure Modes

- Generating a generic “English study plan” with little use of prior evidence.
- Selecting too many targets for one short cycle.
- Filling daily plans with explanations, lists, or written exercises.
- Using scripted role-play that never introduces variation or spontaneous follow-up.
- Coach monologues or multi-part questions that reduce learner speaking.
- Correcting every mistake, or withholding useful naturalness feedback entirely.
- Giving long grammar explanations in the middle of a learner's turn.
- Recording one-off slips as stable recurring errors.
- Claiming precise phoneme problems from a transcript alone.
- Omitting closeout because the scenario used all available time.
- Producing a generic next-cycle proposal that cannot cite prior sessions.
- Claiming files were saved, uploaded, or committed when only Markdown text was returned.

## High-Risk Failure Modes

- **HR-001:** The generated activity is not primarily spoken-English interaction.
- **HR-002:** The coach dominates the session or repeatedly interrupts with lectures.
- **HR-003:** The system makes unsupported pronunciation diagnoses or treats native-like accent as the required norm.
- **HR-004:** The session exceeds the selected time and omits the evidence record or next action.
- **HR-005:** The system fabricates learner evidence, progress, or completed file writes.
- **HR-006:** The next cycle ignores available prior evidence.
- **HR-007:** The pack requires unavailable runtime features such as Python, hooks, a VM, connected apps, plugins, or hidden state.

## Evidence Gaps

- No longitudinal learner data exists yet across several completed cycles.
- No human language teacher has calibrated scores against the proposed rubric.
- No objective speaking-time telemetry is available; learner/coach share must be estimated from observed interaction.
- No stored audio benchmark is available for pronunciation-scoring reliability.
- ChatGPT Live capabilities and availability vary by account, plan, region, and product version.
- The recent GenAI oral-practice study is a preprint and should not determine hard gates by itself.

## Confidence Level

**Medium.**

The rubric is strongly grounded in the user's requirements, the current bundle, official language frameworks, official current product documentation, and corrective-feedback research. Confidence is not high because no real multi-cycle deployment data, audio calibration set, or independent teacher rating set is available.

## Notes

The first evaluation round should include at least one actual ChatGPT Live session. Without a real Live sample, runtime dimensions should be capped and the overall domain score marked provisional.

## Source Links

- OpenAI ChatGPT Voice: https://help.openai.com/en/articles/20001274
- Council of Europe CEFR: https://www.coe.int/en/web/common-european-framework-reference-languages
- CEFR qualitative aspects of spoken language use: https://www.coe.int/en/web/common-european-framework-reference-languages/table-3-cefr-3.3-common-reference-levels-qualitative-aspects-of-spoken-language-use
- CEFR phonological competence: https://www.coe.int/en/web/common-european-framework-reference-languages/phonological-competence
- ACTFL Proficiency Guidelines overview: https://www.actfl.org/proficiency-guidelines-overview
- NCSSFL-ACTFL Can-Do Statements: https://www.actfl.org/educator-resources/ncssfl-actfl-can-do-statements
- ACTFL Oral Proficiency Interview: https://www.actfl.org/assessments/postsecondary-assessments/opi
- Lyster & Saito oral feedback meta-analysis: https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/abs/oral-feedback-in-classroom-sla/4999EE1C8379B2BF026B148EAF373CA1
- Miller & Pan recast meta-analysis: https://www.sciencedirect.com/science/article/abs/pii/S0883035512000626
- He et al. GenAI-mediated L2 oral practice preprint: https://arxiv.org/abs/2604.05702
