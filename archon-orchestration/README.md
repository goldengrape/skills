# Archon Orchestration Skill

A harness-neutral Skill for orchestrating multiple AI Agent Executors through a user-provided Shared Workspace.

## Core flow

```text
Generate → Critique → Rank / Filter → Fuse
```

Optional verification can be inserted before evaluation and/or after fusion when the task has a reliable, scoped verifier.

## Design shape

`SKILL.md` is intentionally a compact control card. It keeps the always-live facts an Orchestrator needs immediately: trigger purpose, core flow, source-of-truth order, Shared Workspace artifact transport, browser Generator isolation, default policy, CHECKPOINT/STOP/anti-pattern guardrails, the resumable state model, and a phase routing table. Detailed stage execution lives in `references/phase-cards.md` (the primary runbook) and in topical references loaded on demand, so a trigger loads less boilerplate and late-stage detail is not in context before it is needed.

## Core abstractions

- **Orchestrator** — the harness/controller that loads the Skill and advances the run.
- **Shared Workspace** — a user-approved repo, folder, or compatible backend that stores run state and substantive artifacts and acts as the preferred artifact transport.
- **Agent Executor** — a browser-operated agent, API-backed agent, local agent, deterministic tool, or other execution backend.
- **Role** — the logical work being performed: Generator, Critic, Ranker, Fuser, optional Verifier, or optional extra Evaluator.

The Skill keeps its core provider-neutral while allowing concrete executor mappings where operational details matter. `references/executor-contract.md` includes an Oracle/ChatGPT browser mapping because browser-page/conversation isolation must be executable rather than implied.

## Typical setup

1. The user creates or approves a dedicated Shared Workspace.
2. The Orchestrator loads `SKILL.md`.
3. The Orchestrator reads only the reference files required for the current phase (see the phase routing table).
4. The Orchestrator creates or resumes a run, freezes the task, records workspace I/O policy and browser execution policy, dispatches isolated Generators, evaluates candidates, and fuses the best evidence.
5. Browser-operated independent Generators each get a new browser page/tab **and** a new conversation. A user-provided ChatGPT Project URL may be used as the common base URL, but an existing project conversation is never reused as a fresh Generator.
6. With the GitHub adapter, substantive inputs/outputs move through GitHub by stable refs and isolated branches/namespaces. Browser prompts and responses carry compact control metadata/receipts rather than copies of repository artifacts.
7. The final response points to stable artifacts and records limitations.

## GitHub + browser example

For a GitHub Shared Workspace with Oracle driving ChatGPT Web, the intended shape is:

```text
zcode / Orchestrator
  ├─ freezes task + base refs in GitHub
  ├─ G1 Oracle invocation -> fresh tab/conversation -> reads GitHub -> writes G1 branch -> returns receipt
  ├─ G2 Oracle invocation -> fresh tab/conversation -> reads GitHub -> writes G2 branch -> returns receipt
  ├─ G3 Oracle invocation -> fresh tab/conversation -> reads GitHub -> writes G3 branch -> returns receipt
  └─ G4 Oracle invocation -> fresh tab/conversation -> reads GitHub -> writes G4 branch -> returns receipt
```

If the user supplies a ChatGPT Project URL, pass it as the browser base URL for each invocation. Do not use Oracle follow-up/session reuse to create independent Generators. Do not use Oracle `--file`, browser attachments, or giant pasted prompts merely to duplicate artifacts already available to the Executor in GitHub.

If a browser Executor cannot read/write the authorized GitHub workspace, it is incompatible with GitHub `direct_required` mode. Reconfigure/replace it or explicitly obtain permission for degraded return-only fallback; do not silently turn the chat into the artifact transport.

## Package layout

```text
SKILL.md
README.md
REFERENCES.md
manifest.txt
adapters/
checklists/
references/
scripts/
templates/
test-prompts.json
```

Important references:

- `references/architecture.md` — conceptual model and context boundaries.
- `references/workspace-contract.md` — Shared Workspace operations, artifact/data-plane rules, namespaces, and resume behavior.
- `references/executor-contract.md` — Agent Executor capability, fresh browser page/conversation isolation, Oracle mapping, dispatch, and artifact-normalization contract.
- `references/execution-policy.md` — default policy, budget counters, escalation, retries, and latency choices.
- `references/phase-cards.md` — the phase-by-phase operational runbook.
- `references/role-prompts.md` — role contracts for Generator, Critic, Ranker, Fuser, and optional evaluator.
- `references/verifier-policy.md` — when and how verification is used.
- `references/failure-recovery.md` — recovery from contamination, timeout, malformed output, and restart.

## Local helper scripts

For a workspace available as a local or mounted directory:

```bash
python scripts/init_archon_run.py --root . --mode standard --workspace-backend github
python scripts/advance_archon_state.py --root . --run-id <RUN_ID> --to GENERATING
python scripts/check_archon_run.py --root . --run-id <RUN_ID>
```

For browser-controlled runs, initialization can record the landing URL:

```bash
python scripts/init_archon_run.py \
  --root . \
  --workspace-backend github \
  --browser-base-url 'https://chatgpt.com/g/.../project'
```

GitHub initialization defaults to direct workspace I/O with return-only fallback disabled. Use `--allow-return-only-fallback` only when that degraded path is intentional.

The scripts are optional helpers for local/mounted workspaces. Remote-only Orchestrators may perform equivalent operations through their backend tools. `check_archon_run.py` also validates package consistency (manifest.txt vs file tree, SKILL.md references) when run from the package root.

## Default policy

- 4 independent Generators in parallel when executor/browser concurrency permits it.
- Minimum 3 usable Generators by default.
- Browser Generators require fresh page + fresh conversation isolation.
- Critic + Ranker logically separate, physically combinable into one fast call.
- Top 2 full candidates go to Fuser.
- Unique insights from lower-ranked candidates are preserved.
- Verification is optional and scoped (`auto` mode).
- One extra evaluator by default, only when escalation criteria are met.
- One Generator replacement, one fusion repair retry, and one schema repair per result by default.
- Resume uses manifest plus artifact reconciliation; completed expensive stages are never rerun because Orchestrator memory was lost.

## Operational guarantees

- Generator isolation until the generation barrier, including fresh browser page/conversation isolation for browser agents.
- Shared Workspace is the preferred artifact/data plane; stable refs replace routine prompt/response file ferrying.
- GitHub adapter defaults to direct read/write and isolated branch/namespace output.
- Durable manifest as the source of truth; no completion claim without an observable artifact.
- Return-only Executor outputs are normalized only when the active workspace policy allows that fallback.
- Bounded retries/replacements/schema repairs/escalations with budget counters.
- Partial failures and transport/isolation degradations are reported, not hidden.
