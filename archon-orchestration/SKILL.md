---
name: archon-orchestration
description: Orchestrate multiple independent AI Agent Executors through a Shared Workspace using an Archon-style Generate → Critique → Rank/Filter → Fuse workflow. Use when a task benefits from multiple candidate solutions, cross-critique, ranking, synthesis, optional verification, browser-operated web agents, GitHub/Google Drive shared workspaces, resumable multi-agent runs, or heterogeneous model execution.
---

# Archon Orchestration Skill

Use this skill when one strong answer may not be reliable enough and the task benefits from inference-time search and synthesis across multiple Agent Executors.

The public promise is simple:

```text
Generate several independent solutions, critique them, rank them, and fuse the best evidence into a stronger result.
```

This skill is implementation-agnostic. Do not bind the workflow to Codex, ChatGPT, GitHub, Google Drive, or any single model vendor.

## Core abstractions

Use exactly these architecture-level terms:

| Term | Meaning |
| --- | --- |
| **Orchestrator** | Loads this skill, discovers capabilities, creates/resumes a run, dispatches Agent Executors, enforces barriers, controls budget, and finalizes state. |
| **Shared Workspace** | External shared state and artifact store supplied by the user, normally a dedicated GitHub repo or Google Drive folder. |
| **Agent Executor** | A task execution backend that performs one role or subtask. It may be a browser-operated web agent, API-backed agent, local agent, or another compatible executor. |

Roles are not Executors. `Generator`, `Critic`, `Ranker`, and `Fuser` are logical roles. A specific Agent Executor is chosen at runtime to perform each role.

## Archon Core

The default logical flow is:

```text
Generate → Critique → Rank / Filter → Fuse
```

Optional evidence modules may be inserted when they are reliable:

```text
Generate → [Verify] → Critique → Rank / Filter → Fuse → [Verify]
```

`Verifier` is not a universal prerequisite. For programming, numerical math, formal checks, or fact validation, it can provide strong evidence. For open research, writing, strategy, or design, do not invent a fake objective verifier.

## Default execution policy

Unless the user or task constraints require another policy:

```text
Generators: 4, parallel, isolated
Critic: 1 logical stage
Ranker: 1 logical stage
Critic + Ranker physical execution: may be combined into one fast evaluation call
Top K full candidates to Fuser: 2
Lower-ranked candidates: pass only critic-extracted unique insights
Fuser: 1 Agent Executor
Verifier: auto / optional
Extra evaluators: at most 1, only when evaluation is uncertain or high-risk
Fusion retry: at most 1 when final verification fails and repair is justified
```

Prefer long-running, high-capability Agent Executors for `Generator` and complex `Fuser` work. Prefer faster/cheaper execution for `Critic` and `Ranker` when quality is sufficient.

## Shared Workspace requirement

The user should provide a dedicated Shared Workspace before a substantive run:

- GitHub repository for code-, diff-, branch-, commit-, or PR-heavy work.
- Google Drive folder for research, writing, planning, documents, spreadsheets, presentations, or mixed artifacts.

Do not silently use unrelated user repositories or folders. If no Shared Workspace is available, ask for one or run only a clearly labeled non-persistent dry run.

The Shared Workspace is the source of truth for run state. Orchestrator memory is not sufficient for a resumable run.

Read `references/workspace-contract.md` when initializing or resuming a workspace. Read the matching adapter only after the backend is known.

## Source-of-truth order

When information conflicts, use this order:

1. User's current explicit instruction and constraints.
2. Frozen task snapshot for the current run.
3. `manifest.json` and authoritative artifacts in the Shared Workspace.
4. Verification evidence produced by approved tools.
5. Critic/Ranker summaries and derived notes.
6. Agent Executor conversational memory.

Do not allow an Agent Executor to silently introduce new requirements. Record material assumptions in its result metadata.

# Operating guardrails

## 🔴 CHECKPOINT moments

Pause for user approval when any of these occurs:

| Moment | Show | Continue only when |
| --- | --- | --- |
| No dedicated Shared Workspace exists | required repo/folder and permission scope | the user provides/authorizes one, or accepts a non-persistent dry run |
| Orchestrator would access a broad pre-existing workspace | exact repo/folder and intended namespace | the user confirms scope |
| Budget escalation exceeds configured policy | extra Agent Executors, expected reason, current evidence | the user approves extra budget |
| Final action is irreversible or affects a protected/shared destination | merge/delete/overwrite/publish target and evidence | user or workspace policy approves |
| Isolation cannot be guaranteed | what candidate cross-read risk exists | user accepts the limitation or execution is reconfigured |

Routine writes inside a user-dedicated Archon workspace do not require repeated approval.

## 🛑 STOP conditions

Stop the current stage and repair state when any of these is true:

| Trigger | Required action |
| --- | --- |
| Shared Workspace cannot be read/written as required | repair permissions or switch backend before dispatch |
| Two Generators would write the same namespace | allocate isolated namespaces before starting either |
| A Generator can see another current-run candidate before the generation barrier | re-isolate or restart the contaminated candidate |
| Manifest stage and workspace artifacts disagree materially | reconcile state before dispatching more work |
| Ranker lacks the candidate set or critique/evidence it claims to rank | rebuild evaluation input; do not fabricate ranking |
| Fuser cannot access the selected artifacts | repair references before fusion |
| A claimed verifier did not actually run | mark evidence as unavailable; never claim pass/fail |
| An irreversible merge/delete/publish is needed without approval | stop and request approval |

## Anti-pattern blacklist

Do not do these things while this skill is active:

1. Do not let Generators read each other's current-run outputs before the generation barrier.
2. Do not use one shared browser conversation as multiple supposedly independent Generators.
3. Do not let multiple Executors write the same isolated namespace concurrently.
4. Do not ask expensive long-running Agents to perform three redundant Critic votes by default.
5. Do not treat a verifier as universally available or authoritative outside its coverage.
6. Do not discard lower-ranked candidates before Critic has extracted unique useful insights.
7. Do not merge a candidate into the final destination before ranking/fusion policy permits it.
8. Do not hide failed, cancelled, timed-out, or contaminated Executor runs.
9. Do not keep large duplicate artifacts in the control namespace when a stable artifact reference is enough.
10. Do not exceed configured retries or budget silently.
11. Do not claim an Agent Executor completed a task until its result/artifact is observable.
12. Do not depend on a specific vendor UI when a capability-based instruction is sufficient.

# Run lifecycle

## 0. Inspect or initialize

Before dispatch:

1. Identify the Shared Workspace backend and exact user-approved scope.
2. Discover Orchestrator capabilities: Skill loading, browser control, local shell/scripts, workspace access, API/tool access.
3. Discover available Agent Executors and capability metadata.
4. Decide whether a reliable Verifier exists for this task.
5. Create or resume a run manifest.
6. Freeze the task snapshot and shared base input.
7. Choose execution policy and budget.

For a locally mounted/synced workspace, the helper is:

```bash
python scripts/init_archon_run.py --root . --mode standard --workspace-backend github
```

If scripts cannot be run, create the equivalent state manually using `templates/manifest.json`.

Use `checklists/run_start.md` before leaving this phase.

## 1. Generate

Dispatch independent Generator Agent Executors in parallel.

Each Generator receives only:

- frozen task snapshot
- common constraints
- shared base input
- its own output namespace
- role instructions
- approved tools/capabilities

Each Generator must not receive or read:

- other Generator outputs from the same run
- current-run critiques
- current-run ranking
- current-run fusion artifacts

Default count is 4. Use distinct browser pages/sessions when browser-operated Agents are used.

Read `references/role-prompts.md` before dispatching. For each execution, persist terminal status and an artifact reference.

## 2. Generation barrier

Do not begin Critique until every scheduled Generator is terminal: `completed`, `failed`, `cancelled`, or explicitly `contaminated`.

Default recovery policy:

- If 4/4 complete: continue.
- If 3/4 complete and failed candidate adds no unique required coverage: continue and record degradation.
- If fewer than 3 complete: replace failed Generator once if budget permits; otherwise checkpoint or fail the run.
- If a Generator is contaminated by seeing another candidate: discard it and replace if possible.

Use `checklists/generation_barrier.md`.

## 3. Optional generation verification

If the task has a reliable verifier, run it against candidates before Critique so the evaluation stage receives evidence rather than guesses.

Examples:

- programming: compile, tests, typecheck, lint, static analysis
- math: numeric substitution, CAS, solver, formal checker
- research: citation existence, dates, quoted values, source consistency

Verification evidence is scoped. A passing test suite does not prove untested semantics; source existence does not prove strategic quality.

Read `references/verifier-policy.md` when verification is enabled.

## 4. Critique

Critic reads all valid candidate artifacts plus optional evidence. It must produce structured analysis for each candidate:

```text
strengths
weaknesses
missing assumptions
risks
unique insights
reusable parts
conflicts with evidence
```

Critic does not modify candidate artifacts.

## 5. Rank / Filter

Ranker uses the frozen task, candidate artifacts, Critic output, and available verification evidence.

It must output:

- ordered ranking
- rejected candidates with reasons
- top K selection
- confidence
- unresolved disagreements
- unique insights to preserve from lower-ranked candidates

Anonymize model/vendor identity when practical so ranking focuses on artifacts rather than provider labels.

Critic and Ranker may be executed in one fast physical call, but persist outputs as logically separate sections/artifacts.

If confidence is low, evidence conflicts, or the task is high-risk, dispatch at most one additional evaluator by default and reconcile. Do not default to 3 expensive Critic Agents.

Use `checklists/evaluation.md`.

## 6. Fuse

Fuser receives:

- frozen task
- full top K candidate artifacts (default K=2)
- Critic findings for all candidates
- Ranker decision
- unique insights extracted from lower-ranked candidates
- verification evidence when available

The Fuser must create a new artifact. It must not merely declare a winner or copy candidate #1 without explaining why no synthesis is useful.

For code work, Fuser should work in its own branch/namespace. For document work, Fuser should write a new final-draft artifact rather than overwriting candidates.

Use `checklists/fusion.md`.

## 7. Optional final verification

When a reliable verifier exists, treat the fused result as a new candidate and verify it again.

If final verification fails:

1. Determine whether failure is artifact failure or verifier/infrastructure failure.
2. If artifact failure and retry budget remains, send the evidence back to one repair/fusion execution.
3. Re-run relevant verification.
4. If still failing, prefer a previously verified top-ranked candidate when appropriate, or finalize as failed/partial with evidence.

Never silently loop.

## 8. Finalize

Write the final outcome and update manifest to `DONE`, `PARTIAL`, or `FAILED`.

Final report should include:

- final artifact reference
- candidate count and terminal statuses
- selected top candidates
- whether Critic/Ranker were combined physically
- verifier coverage and exact evidence status
- retries/escalations used
- known limitations
- any irreversible action still awaiting approval

Use `checklists/finalize.md`.

# State model

Use these logical stages:

```text
INIT
→ GENERATING
→ [VERIFYING_GENERATION]
→ CRITIQUING
→ RANKING
→ FUSING
→ [FINAL_VERIFY]
→ FINALIZING
→ DONE | PARTIAL | FAILED
```

`Critique` and `Rank` are logically separate even when physically performed by one call.

Recommended helper:

```bash
python scripts/advance_archon_state.py --root . --run-id <RUN_ID> --to GENERATING
```

Always persist stage changes in the Shared Workspace.

# Modes

## mode: initialize_run

Goal: discover capabilities, bind a user-provided Shared Workspace, create a frozen task snapshot, and establish policy.

Outputs:

- run namespace
- `manifest.json`
- `task.md`
- executor capability notes
- chosen workspace adapter

## mode: dispatch_generation

Goal: launch isolated parallel Generator Agent Executors.

Outputs:

- execution IDs/statuses
- one namespace per Generator
- normalized `result.json` per terminal execution

## mode: critique_and_rank

Goal: evaluate candidates after the generation barrier.

Outputs:

- `critique/critique.json`
- `ranking/ranking.json`

Rules:

- logical Critic and Ranker outputs remain distinguishable
- one fast execution may produce both
- add only one extra evaluator by default when uncertain

## mode: fuse

Goal: synthesize the top candidates plus preserved unique insights.

Outputs:

- fused artifact
- `fusion/result.json`

## mode: recover_run

Goal: resume from Shared Workspace state after Orchestrator interruption.

Rules:

1. Read manifest first.
2. Inspect workspace artifacts and terminal execution markers.
3. Reconcile inconsistencies before dispatching new work.
4. Never repeat a completed expensive stage solely because Orchestrator memory was lost.

## mode: finalize_run

Goal: persist outcome, evidence, limitations, and final artifact reference.

# Workspace adapters

Read only the adapter matching the selected backend:

- `adapters/github.md`
- `adapters/google-drive.md`

The logical workspace contract is defined in `references/workspace-contract.md`.

# Progressive disclosure

Do not load every reference file into context at once.

- On initialization/resume: read `workspace-contract.md`, `executor-contract.md`, `execution-policy.md`.
- Before Generate/Critique/Rank/Fuse: read only the relevant section of `role-prompts.md`.
- When verification is possible: read `verifier-policy.md`.
- On failure/recovery: read `failure-recovery.md`.
- For a backend: read only its adapter.

# Shipping gates

Before declaring a run complete, verify:

- Shared Workspace scope was user-provided or explicitly approved.
- Frozen task exists and material requirements were not silently changed.
- Generator isolation was enforced or limitations are disclosed.
- Generation barrier completed before evaluation.
- Critic output covers all valid candidates.
- Ranking cites candidate/evidence reasons and records confidence.
- Fuser received top candidates plus preserved unique insights.
- Final result is a new artifact or an explicitly justified accepted winner.
- Verification claims correspond to commands/tools that actually ran.
- Retry and escalation budgets were respected.
- Manifest and final artifact references are consistent.

Recommended local check:

```bash
python scripts/check_archon_run.py --root . --run-id <RUN_ID>
```

# Response style

When using this skill:

- Keep user-facing updates short and stage-oriented.
- Report partial failures instead of hiding them.
- Distinguish evidence from model judgment.
- Do not dump internal Executor conversations unless requested.
- Prefer artifact references, decisions, and next stage over long duplicated content.
- If the user only wants the final result, keep orchestration logs in the Shared Workspace and return a concise outcome summary.
