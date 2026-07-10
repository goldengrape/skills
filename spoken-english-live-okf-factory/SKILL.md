---
name: spoken-english-live-okf-factory
description: "Generate, run, close, validate, and roll over compact 3-day or 7-day spoken-English course cycles for ChatGPT Live. Use when the user wants continuous English speaking practice, a weekly speaking plan, Live role-play sessions, concise real-time corrections, Markdown learning records, or a next-cycle plan based on prior sessions. Trigger phrases include: 英语口语训练, ChatGPT Live 口语, 口语课程包, 下一周英语课程, speaking practice cycle, live English coach, weekly speaking plan."
---

# Spoken English Live OKF Factory

Generate a compact Markdown course cycle, run short Live sessions from it, and turn each session into evidence for the next cycle. The default is a 7-day cycle with one 15-minute session per day. A focused 3-day cycle is supported.

## Read Order

Read only the files needed for the current task:

| Task | Required files |
|---|---|
| Generate a cycle | `contracts/cycle-evidence-contract.md` → `playbooks/derive-cycle-blueprint.md` → `schemas/course-pack-layout.md` → `playbooks/materialize-cycle-pack.md` → `playbooks/validate-cycle-pack.md` |
| Run today's Live session | generated `index.md`, `mission.md`, `plan/cycle-plan.md`, today's `plan/day-N.md`, state files, `teacher/live-session-settings.md`, then `runtime/live-session-protocol.md` |
| Close a session | `playbooks/close-live-session.md` + `templates/session-record-template.md` |
| Finish a cycle | `playbooks/rollover-cycle.md` |
| Evaluate the package | `evaluation/index.md` |

Do not load the entire bundle into a Live session when the task only needs today's plan and current state.

## Workflow

### 1. Normalize the evidence

Execute `DP-001` and return a **Cycle Evidence Snapshot**. Distinguish:

- current learner instructions,
- observed session evidence,
- learner-reported information,
- inference,
- uncertainty.

Use explicit defaults for missing non-critical information. Do not rely on unstated memory.

### 2. Derive one bounded cycle blueprint

Execute `DP-002`.

- Select no more than three primary targets.
- Use 7 days for normal continuity and 3 days for one focused repair or scenario sprint.
- Make every day speaking-first and time-bounded.
- Reuse prior phrases, errors, interests, or uncertainties only when evidence supports them.

### 🔴 CHECKPOINT — Confirm before materialization when needed

Stop and show the evidence snapshot plus blueprint when any of these is true:

- current instructions conflict in a way that changes the course purpose;
- a custom duration or unsupported cycle length is requested;
- the learner asks for a pronunciation diagnosis that exceeds available audio evidence;
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

Do not silently repair a failed pack and then report it as the original result. If repair is requested, produce a revised pack and a new validation report.

### 5. Run a Live session

Execute `runtime/live-session-protocol.md`.

- Default duration: 15 minutes.
- Keep the learner speaking most of the time.
- Use brief, one-breath corrections when useful.
- Include naturalness and register improvements, not only grammar fixes.
- Protect the final 1–2 minutes for closeout.

### 6. Close the session

Execute `DP-005`. A completed session returns:

1. one Markdown session record,
2. one state patch,
3. exactly one next action.

### 7. Roll over the cycle

Execute `DP-006` from saved session evidence. Make explicit `continue`, `change`, `retire`, and `test next` decisions. The proposal becomes evidence for a new `DP-001` run; it does not rewrite the completed cycle.

## Failure Recovery

| Trigger | First response | If still unresolved |
|---|---|---|
| Prior records conflict | Apply the evidence-priority rules and expose the conflict. | Stop at the checkpoint when the conflict changes cycle purpose. |
| A requested day cannot fit the selected duration | Remove optional variation and reduce correction scope. | Redesign the day around one speaking task, one repair, and closeout. |
| Live audio is unclear | Ask once for repetition or mark the observation uncertain. | Do not create a pronunciation diagnosis from transcript text. |
| Learner becomes tired or shortens the session | Switch to the minimum viable session in the runtime protocol. | Preserve one speaking task, one repair, and closeout; drop everything else. |
| A required generated file is missing | Report validation `FAIL` with the missing path. | Regenerate only the missing or invalid artifact, then validate again. |
| The user requests Python, hidden state, or automatic GitHub writes | Keep the core workflow Markdown-only and explain the unsupported operation briefly. | Return copyable artifacts and manual save instructions only. |
| No reliable prior evidence exists | Generate a diagnostic cycle and label assumptions. | Do not fabricate progress or recurring-error history. |

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
```
