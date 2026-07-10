---
name: spoken-english-live-okf-factory
description: "Generate, run, adapt, close, validate, and roll over compact 3-day or 7-day spoken-English course cycles for ChatGPT Live. Use when the user wants continuous English speaking practice, interest-aware weekly speaking plans, Live role-play sessions, concise real-time corrections, current-event discussion grounded in verified sources, Markdown learning records, or a next-cycle plan based on prior sessions. Trigger phrases include: 英语口语训练, ChatGPT Live 口语, 口语课程包, 兴趣话题英语, 新闻英语讨论, 下一周英语课程, speaking practice cycle, live English coach, adaptive speaking plan."
---

# Spoken English Live OKF Factory

Generate a compact Markdown course cycle, run short Live sessions from it, adapt conversation topics from evidence without confusing interest with fatigue, language difficulty, subject knowledge, or prompt quality, and turn each session into input for the next session and cycle. The default is a 7-day cycle with one 15-minute session per day. A focused 3-day cycle is supported.

The stable unit is the **language objective**. The conversation topic may adapt when doing so preserves the objective and improves engagement.

## Read Order

Read only the files needed for the current task:

| Task | Required files |
|---|---|
| Generate a cycle | `contracts/cycle-evidence-contract.md` → `playbooks/derive-cycle-blueprint.md` → `schemas/course-pack-layout.md` → `playbooks/materialize-cycle-pack.md` → `playbooks/validate-cycle-pack.md` |
| Run today's Live session | generated `index.md`, `mission.md`, `plan/cycle-plan.md`, today's `plan/day-N.md`, state files, `teacher/live-session-settings.md`, then `runtime/live-session-protocol.md` |
| Close a session and adapt the next topic | `playbooks/close-live-session.md` + `templates/session-record-template.md` |
| Finish a cycle | `playbooks/rollover-cycle.md` |
| Evaluate the package | `evaluation/index.md` |

Do not load the entire bundle into a Live session when today's plan and current state are sufficient.

## Workflow

### 1. Normalize the evidence

Execute `DP-001` and return a **Cycle Evidence Snapshot**. Distinguish:

- current learner instructions,
- observed speaking evidence,
- learner-reported interests and preferences,
- cautious inference,
- uncertainty.

Use explicit defaults for missing non-critical information. One casual mention is not automatically a confirmed long-term interest.

### 2. Derive one bounded cycle blueprint

Execute `DP-002`.

- Select no more than three primary language targets.
- Use 7 days for normal continuity and 3 days for one focused repair or scenario sprint.
- Default to `guided_adaptive` topic policy.
- Keep the language objective fixed while allowing some topic slots to adapt.
- Give every adaptive slot a concrete evergreen fallback.
- Assign each adaptive slot one intent: `deepen_confirmed`, `test_possible`, or `refresh_variety`.
- Apply the topic-fit check before selection: objective fit, consent/safety, accessible knowledge load, evidence basis, recent-topic balance, and time fit.
- Use current events only when enabled, relevant, freshly verified within the runtime budget, and simple enough for a short speaking session.

### 🔴 CHECKPOINT — Confirm before materialization when needed

Stop and show the evidence snapshot plus blueprint when any of these is true:

- current instructions conflict in a way that changes the course purpose;
- a custom duration or unsupported cycle length is requested;
- the learner asks for a pronunciation diagnosis that exceeds available audio evidence;
- the topic policy would introduce sensitive or explicitly excluded current-event categories;
- more than one important planning assumption remains unresolved;
- the requested cycle would replace the learner's explicit current goal.

If none applies and the user requested direct generation, continue without an extra confirmation turn.

### 3. Materialize the Markdown course pack

Execute `DP-003` using `schemas/course-pack-layout.md`.

Return complete file contents with paths. Do not claim that files were saved, uploaded, or committed.

### 4. Validate before presenting

Execute `DP-007` as a read-only gate.

- `PASS`: no blocking or major defects.
- `FAIL`: list each defect, evidence, and required fix.

An adaptive day is invalid when it has no fixed language objective, no selection rule, or no fallback topic.

### 5. Run a Live session

Execute `runtime/live-session-protocol.md`.

- Default duration: 15 minutes.
- Keep the learner speaking most of the time.
- Use brief, one-breath corrections when useful.
- Include naturalness and register improvements, not only grammar fixes.
- On adaptive days, select a topic quickly from current evidence or offer two concise choices. Do not automatically choose the most familiar confirmed interest.
- Distinguish topic affinity from fatigue, language load, background-knowledge load, and prompt/task mismatch before changing interest state.
- When using current events, verify them at session time within the fast verification budget and keep the background to a compact three-part capsule.
- Protect the final 1–2 minutes for closeout.

### 6. Close the session

Execute `DP-005`. A completed session returns:

1. one Markdown session record,
2. one state patch,
3. exactly one next action,
4. one evidence-based recommendation for the next topic slot when adaptation is enabled.

The recommendation is part of the state patch; it does not silently rewrite future plans.

### 7. Roll over the cycle

Execute `DP-006` from saved session evidence. Make explicit `continue`, `change`, `retire`, and `test next` decisions for language targets and topic interests. The proposal becomes evidence for a new `DP-001` run; it does not rewrite the completed cycle.

## Failure Recovery

| Trigger | First response | If still unresolved |
|---|---|---|
| Prior records conflict | Apply the evidence-priority rules and expose the conflict. | Stop at the checkpoint when the conflict changes cycle purpose. |
| A requested day cannot fit the selected duration | Remove optional variation and reduce correction scope. | Redesign around one speaking task, one repair, and closeout. |
| Live audio is unclear | Ask once for repetition or mark the observation uncertain. | Do not create a pronunciation diagnosis from transcript text. |
| Learner becomes tired or shortens the session | Switch to the minimum viable session. | Preserve one speaking task, one repair, and closeout. |
| The planned topic produces low engagement | Diagnose the likely cause: affinity, fatigue, language load, background knowledge, or prompt/task mismatch. | Retry once with a simpler or more personal prompt; switch topic only if useful while preserving the objective. |
| A current event cannot be freshly verified within 30 seconds | Do not use it as fact or spend more session time searching. | Use the day's evergreen fallback topic. |
| A current event needs too much background | Reduce it to one accessible question. | Replace it with an evergreen interest-based scenario. |
| A required generated file is missing | Report validation `FAIL` with the missing path. | Regenerate only the missing or invalid artifact, then validate again. |
| The user requests Python, hidden state, or automatic GitHub writes | Keep the core workflow Markdown-only and explain the unsupported operation briefly. | Return copyable artifacts and manual save instructions only. |
| No reliable prior evidence exists | Generate a diagnostic cycle and label assumptions. | Do not fabricate progress, recurring errors, or confirmed interests. |

## Output Contracts

### Cycle generation

Return in this order:

1. normalized evidence snapshot,
2. cycle blueprint,
3. file tree,
4. complete Markdown files,
5. validation report.

### Live closeout

Return one copyable Markdown block matching `templates/session-record-template.md`. Do not duplicate the same next action in competing forms.

## Anti-Patterns — Do Not Do These

- Do not lock all seven conversation topics when adaptive slots would better sustain engagement.
- Do not let topic novelty replace the cycle's language objectives.
- Do not infer a stable interest from one mention or one unusually energetic answer.
- Do not infer dislike from one tired or shortened session, difficult vocabulary, weak background knowledge, or a poorly phrased prompt.
- Do not let one confirmed interest monopolize a guided-adaptive cycle unless the learner requests a thematic cycle.
- Do not use stale, unverified, fabricated, or needlessly distressing news as conversation material.
- Do not spend most of a 15-minute session explaining news background.
- Do not turn a 15-minute session into a lecture or written worksheet.
- Do not correct every error or give multi-paragraph interruptions during speaking.
- Do not prohibit brief live corrections when a concise intervention would help.
- Do not treat grammatical correctness as sufficient when wording is unnatural for the situation.
- Do not infer recurring errors from one uncertain occurrence.
- Do not claim exact phoneme errors from a text transcript.
- Do not carry every old target into the next cycle automatically.
- Do not describe skipped sessions as completed or failed performance.
- Do not create duplicate policy files with overlapping authority.
- Do not claim files were saved, committed, or uploaded when only text was returned.

## Defaults

```yaml
cycle_days: 7
daily_minutes: 15
supported_cycle_days: [3, 7]
supported_daily_minutes: [10, 15, 20, 30]
target_english: clear_global_english
practice_language: mostly_english
feedback_language: Chinese
interruption_style: live_micro
topic_policy:
  mode: guided_adaptive
  planned_ratio: 0.6
  adaptive_ratio: 0.4
  allow_mid_cycle_topic_adjustment: true
interest_discovery:
  enabled: true
  confirmation_rule: explicit_or_repeated_evidence
  separate_affinity_from_load: true
  recent_topic_window: 3
  default_max_same_topic_sessions_per_7_day_cycle: 3
current_events:
  enabled: false
  default_frequency: up_to_one_slot_per_cycle
  require_current_verification: true
  verification_budget_seconds: 30
```
