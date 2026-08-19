---
name: archon-orchestration
description: Orchestrate multiple independent AI Agent Executors through a Shared Workspace using an Archon-style Generate → Critique → Rank/Filter → Fuse workflow. Use when a task benefits from multiple candidate solutions, cross-critique, ranking, synthesis, optional scoped verification, browser-operated or return-only web agents, GitHub/Google Drive shared workspaces, resumable multi-agent runs, or heterogeneous execution backends.
---

# Archon Orchestration Skill

Use this skill when one strong answer is not reliable enough and the task benefits from independent candidate generation, structured evaluation, and evidence-aware synthesis.

Public promise:

```text
Generate independent candidates, critique them, rank/filter them, and fuse the strongest evidence and ideas into a better result.
```

This skill is implementation-agnostic at the core. Capability-level rules should remain portable, while adapter/executor references may define concrete mappings required for reliable operation.

## Resident core

Keep these facts in active context for every run. Everything else loads on demand via the phase routing table.

### Core terms

| Term | Meaning |
| --- | --- |
| **Orchestrator** | The controller that loads this skill, initializes or resumes a run, discovers capabilities, dispatches Agent Executors, normalizes returned results, enforces barriers, controls budget, reconciles state, and finalizes the outcome. |
| **Shared Workspace** | User-authorized durable state and artifact storage. It is the source of truth for a resumable run and the primary transport for substantive artifacts. |
| **Agent Executor** | A bounded execution backend: browser-operated agent, API-backed agent, local agent, deterministic program, verifier, or future compatible executor. |

Roles are logical; Executors are physical. `Generator`, `Critic`, `Ranker`, `Fuser`, and optional `Verifier` describe why a step exists; the Orchestrator chooses a capable Executor at runtime.

### Core flow

Preserve this flow:

```text
Generate -> Critique -> Rank / Filter -> Fuse
```

Scoped verification may be inserted only when a reliable check exists:

```text
Generate -> [Verify candidates] -> Critique -> Rank / Filter -> Fuse -> [Verify fused result]
```

A verifier is evidence, not a universal judge. Use it for tests, builds, typechecks, formal checks, numeric checks, citation/date/quote checks, or similar bounded oracles. Do not invent deterministic verification for open-ended research, writing, strategy, or design.

### Source-of-truth order

When sources conflict, use this order:

1. User's current explicit instruction and constraints.
2. Frozen task snapshot for the run.
3. `manifest.json` and durable artifacts in the Shared Workspace.
4. Verification evidence from tools that actually ran.
5. Critic/Ranker outputs and derived notes.
6. Agent Executor conversational memory.

Do not allow an Executor to silently add requirements. Record material assumptions in result metadata.

### Shared Workspace transport invariant

The Shared Workspace is not only persistence. It is the preferred artifact I/O path.

```text
Conversation / browser prompt = control plane
Shared Workspace              = artifact/data plane
```

When an Executor can read/write the Shared Workspace directly:

- dispatch stable refs plus compact instructions instead of copying artifact bodies into prompts;
- require substantive output to be written to the assigned workspace namespace/branch;
- accept only a compact receipt in the Executor response;
- verify the referenced artifact before marking completion.

Do not use chat input, file uploads, or long returned text merely to ferry artifacts that already live in the Shared Workspace.

The selected workspace adapter may tighten this rule. For GitHub, read `adapters/github.md`: default to direct repository I/O and do not silently fall back to return-only transport.

### Browser Generator isolation invariant

For every browser-operated independent Generator, independence requires **both** a fresh browser page/tab and a fresh conversation.

- Start one distinct browser execution/invocation per Generator.
- Create a new page/tab/target for each Generator.
- From the configured base URL, create a new conversation for each Generator.
- A user-provided ChatGPT project/workspace URL may be used as the common base URL, but it is only a landing scope. Never reuse an existing project conversation as a new Generator.
- Never use another Generator's follow-up chain, saved browser session, reattached conversation, or prior-turn context as a supposedly independent Generator.
- Sharing the same signed-in browser profile is acceptable only when each Generator still gets a distinct page and distinct conversation and prohibited sibling content is not injected.

Record page/conversation references when the executor exposes them. If fresh page + fresh conversation isolation cannot be guaranteed, the Generator is not an independent sample.

### Default execution policy

Unless task constraints or user instructions override it, with policy keys matching `manifest.json`:

```yaml
generator_count: 4
minimum_usable_generators: 3
top_k: 2
verifier_mode: auto
combine_critic_ranker: true
max_extra_evaluators: 1
max_generator_replacements: 1
max_fusion_retries: 1
max_schema_repairs_per_result: 1
```

Use high-capability Executors for Generator and complex Fuser work. Use faster/cheaper Executors for Critic and Ranker when quality is sufficient. Do not default to multiple expensive Critic votes. `Critique` and `Rank` are logically separate even when one physical execution produces both outputs.

## Shared Workspace requirement

Before a substantive run, use a dedicated or explicitly approved Shared Workspace.

* Code, diffs, branches, commits, PRs, or repository-native artifacts: prefer a repository-style backend.
* Research, writing, planning, documents, or mixed artifacts: prefer a folder/document backend unless the user explicitly wants repository-native artifact transport.
* Other backends are acceptable if they satisfy `references/workspace-contract.md`.

If no Shared Workspace is available, CHECKPOINT: ask for one, or run only a clearly labeled non-persistent dry run.

Read `references/workspace-contract.md` when initializing or resuming. Read only the matching adapter after the backend is known:

* `adapters/github.md`
* `adapters/google-drive.md`

## Operating guardrails

### CHECKPOINT moments

Pause for user or policy approval when any of these occurs:

| Moment | Show | Continue only when |
| --- | --- | --- |
| No dedicated Shared Workspace exists | required backend, root/scope, and permission need | user provides/authorizes one, or accepts a non-persistent dry run |
| Orchestrator would access a broad pre-existing workspace | exact root, namespace, and intended reads/writes | user confirms scope |
| Direct-required workspace I/O cannot be satisfied | missing Executor read/write capability and proposed alternative | user approves a degraded return-only path or execution is reconfigured |
| Budget escalation exceeds policy | extra Executors/retries, reason, expected benefit, current evidence | user approves |
| Manifest and workspace artifacts disagree materially | manifest stage, artifact facts, proposed reconciliation | user approves if reconciliation would discard or overwrite state |
| Final action is irreversible or affects a protected/shared destination | merge/delete/overwrite/publish target and evidence | user or workspace policy approves |
| Isolation cannot be guaranteed | page/conversation or cross-read risk and affected candidates | user accepts the limitation or execution is reconfigured |

Routine writes inside a user-dedicated Archon run namespace do not require repeated approval.

### STOP conditions

Stop the current stage and repair state when any trigger is true:

| Trigger | Required action |
| --- | --- |
| Shared Workspace cannot be read/written as required | repair permissions or switch backend before dispatch |
| Direct-required Executor cannot read/write the workspace | replace/reconfigure it; do not silently paste/upload artifacts through chat |
| Two active Executors would write the same isolated namespace | allocate separate namespaces before starting either |
| A browser Generator would reuse an existing Generator conversation | create a fresh page and fresh conversation before dispatch |
| A Generator can see another current-run candidate before the generation barrier | mark contaminated, re-isolate or replace if policy permits |
| A return-only result is used when fallback was not permitted | reject the transport downgrade and reconfigure execution |
| A permitted return-only result is malformed or incomplete | capture raw return, attempt one schema repair if policy permits, otherwise mark failed |
| Manifest stage and workspace artifacts disagree materially | reconcile state before dispatching more work |
| Any scheduled Generator is non-terminal at the generation barrier | reattach/status-check, cancel, or wait per policy; do not evaluate yet |
| Usable Generator count is below policy minimum | replace within budget; otherwise CHECKPOINT or fail/partial |
| Ranker lacks the candidate set, critique, or evidence it claims to rank | rebuild evaluation input; do not fabricate ranking |
| Fuser cannot access selected artifacts or preserved insights | repair references before fusion |
| A claimed verifier did not actually run | mark evidence unavailable/error; never claim pass/fail |
| Retry/replacement/schema-repair/escalation budget would be exceeded | CHECKPOINT for approval or stop |
| Irreversible merge/delete/overwrite/publish is needed without approval | stop and request approval |

### Anti-pattern blacklist

Do not:

1. Let Generators read each other's current-run outputs before the generation barrier.
2. Use one shared browser conversation as multiple supposedly independent Generators.
3. Open multiple tabs that all continue the same conversation and call them independent Generators.
4. Reuse `followup`, saved-session, or reattached conversation state to create another independent Generator.
5. Let multiple active Executors write the same isolated namespace.
6. Use the Orchestrator prompt, browser file upload, or chat response as the normal transport for large artifacts already available in the Shared Workspace.
7. Ask a direct-write Generator to return a duplicate full artifact body instead of a stable workspace receipt.
8. Silently downgrade a GitHub direct-write run to return-only because repository access was not configured.
9. Ask expensive long-running Agents for three redundant Critic votes by default.
10. Treat verifier output as complete quality judgment outside its scope.
11. Discard lower-ranked candidates before Critic extracts unique useful insights.
12. Merge or publish a candidate before ranking/fusion policy permits it.
13. Hide failed, cancelled, timed-out, malformed, transport-incompatible, or contaminated Executor runs.
14. Copy large artifacts into control state when a stable reference is enough.
15. Exceed retry, replacement, schema-repair, or budget policy silently.
16. Claim an Executor completed work until its result or artifact is observable.
17. Evaluate transient return-only text without workspace normalization when return-only is permitted.
18. Re-run completed expensive stages merely because Orchestrator memory was lost.

## State model

Persist every stage transition in the Shared Workspace.

```text
INIT
-> GENERATING
-> [VERIFYING_GENERATION]
-> CRITIQUING
-> RANKING
-> FUSING
-> [FINAL_VERIFY]
-> FINALIZING
-> DONE | PARTIAL | FAILED
```

`recover_run` is a mode, not a stage: reconcile manifest with artifacts, then resume from the first incomplete logical stage.

Local helper when the workspace is mounted or synced:

```bash
python scripts/advance_archon_state.py --root . --run-id <RUN_ID> --to GENERATING
```

## Phase routing

`SKILL.md` is the control card. Load detailed material only for the current phase; `references/phase-cards.md` is the operational runbook.

| Phase / mode | Read | Required output |
| --- | --- | --- |
| Initialize or resume | `references/workspace-contract.md`, `references/executor-contract.md`, `references/execution-policy.md`, matching adapter, `checklists/run_start.md` | run namespace, `manifest.json`, frozen `task.md`, workspace I/O policy, browser execution policy, executor capability notes |
| Generate | `references/phase-cards.md#generate`, `references/role-prompts.md#generator`, `references/executor-contract.md`, matching adapter | one terminal record per scheduled Generator; stable artifact refs or explicitly permitted normalized return-only results |
| Generation barrier | `references/phase-cards.md#generation-barrier`, `checklists/generation_barrier.md` | barrier decision; usable candidate set |
| Optional candidate verification | `references/verifier-policy.md` | scoped evidence records; no fake unavailable evidence |
| Critique + Rank | `references/phase-cards.md#critique-and-rank`, `references/role-prompts.md#critic`, `references/role-prompts.md#ranker`, `checklists/evaluation.md` | `critique/critique.json`, `ranking/ranking.json` |
| Fuse | `references/phase-cards.md#fuse`, `references/role-prompts.md#fuser`, `checklists/fusion.md` | new fused artifact or explicitly justified winner adoption |
| Optional final verification | `references/verifier-policy.md` | scoped evidence for fused result |
| Finalize | `references/phase-cards.md#finalize`, `checklists/finalize.md` | `final/outcome.json`; manifest outcome `DONE`, `PARTIAL`, or `FAILED` |
| Failure / recovery | `references/failure-recovery.md` | reconciled manifest and next safe phase |

## Executor dispatch and normalization

For every executor, record enough data to resume or audit: `execution_id`, `role`, `candidate_id` when relevant, `status`, start/end time, output namespace, `artifact_ref`, direct-workspace/return-only transport, page/conversation references when applicable, evidence refs, limitations, contamination/failure reason.

For browser-operated independent Generators:

* Use one distinct browser invocation and a newly created page/tab per Generator.
* Create a fresh conversation from the configured base URL for each Generator.
* A ChatGPT project/workspace URL may be the shared base URL, but never reuse an existing conversation inside it.
* Give each Generator only the frozen task ref, shared base refs, allowed tools, and its own namespace.
* Do not paste sibling candidate outputs, critiques, rankings, fusion artifacts, or duplicate workspace files before the barrier.
* Treat browser UI state as transient; persist durable output in the Shared Workspace.

When Oracle controls ChatGPT web, use the mapping in `references/executor-contract.md#oracle--chatgpt-browser-mapping`: one Oracle invocation per Generator, fresh tab/conversation, optional `--chatgpt-url` base, and no follow-up/session reuse for independence.

For direct-workspace Executors:

1. Require the Executor to read substantive inputs by workspace ref.
2. Require output directly in its assigned namespace/branch.
3. Collect only a compact receipt with artifact/version refs and metadata.
4. Verify the referenced artifact independently.
5. Write/update normalized execution metadata only after verification.

For explicitly permitted return-only Executors:

1. Collect the returned content; persist safe raw return to the assigned namespace (`raw-return.md`).
2. Normalize complete returned content into a durable candidate artifact.
3. Write `generation/<ID>/result.json` from `templates/executor-result.json`.
4. Set `direct_workspace_write: false` and `return_only_normalized_by_orchestrator: true`.
5. Record `raw_return_ref`, `artifact_ref`, normalization notes, and the transport downgrade.
6. Do not call the executor complete until the normalized artifact or stable reference exists.

## Local helper scripts

For a locally mounted or synced workspace:

```bash
python scripts/init_archon_run.py --root . --mode standard --workspace-backend github
python scripts/check_archon_run.py --root . --run-id <RUN_ID>
```

Scripts are optional helpers. Remote-only Orchestrators may perform equivalent operations through their own workspace tools. If scripts cannot run, create equivalent state manually from `templates/manifest.json`, `templates/task.md`, and `templates/executor-result.json`.

## Completion gate

Before declaring completion, verify:

* Shared Workspace scope was user-provided or explicitly approved.
* Frozen task exists and material requirements were not changed silently.
* Active workspace I/O policy was respected; any return-only downgrade was explicitly allowed and recorded.
* Browser Generator isolation used a fresh page/tab and fresh conversation per independent candidate.
* A project/workspace base URL was not mistaken for permission to reuse a conversation.
* GitHub direct mode used GitHub refs and direct branch/namespace writes instead of routine prompt/file/response artifact ferrying.
* Return-only outputs, when permitted, were normalized before evaluation.
* Generation barrier completed before evaluation.
* Critic covered every usable candidate.
* Ranking cites candidate/evidence reasons and records confidence.
* Fuser received top candidates plus preserved lower-ranked insights.
* Final result is a new artifact, or winner adoption is explicitly justified.
* Verification claims correspond to commands/tools that actually ran.
* Retry, replacement, schema-repair, and escalation budgets were respected.
* Manifest, executor results, and final artifact references are consistent.

Recommended local check:

```bash
python scripts/check_archon_run.py --root . --run-id <RUN_ID>
```

## User-facing response style

Keep updates short and stage-oriented. Report partial failures. Distinguish evidence from judgment. Return stable artifact references and outcome summaries rather than dumping workspace artifacts or internal executor conversations unless requested.
