# Archon Orchestration Skill

A harness-neutral Skill for orchestrating multiple AI Agent Executors through a user-provided Shared Workspace.

## Core flow

```text
Generate → Critique → Rank / Filter → Fuse
```

Optional verification can be inserted before evaluation and/or after fusion when the task has a reliable, scoped verifier.

## Design shape

`SKILL.md` is intentionally a compact control card. It keeps only the always-live facts an Orchestrator needs immediately: trigger purpose, core flow, source-of-truth order, default policy, CHECKPOINT/STOP/anti-pattern guardrails, the resumable state model, and a phase routing table. Detailed stage execution lives in `references/phase-cards.md` (the primary runbook) and in topical references loaded on demand, so a trigger loads less boilerplate and late-stage detail is not in context before it is needed.

## Core abstractions

- **Orchestrator** — the harness/controller that loads the Skill and advances the run.
- **Shared Workspace** — a user-approved repo, folder, or compatible backend that stores run state and artifacts.
- **Agent Executor** — a browser-operated agent, API-backed agent, local agent, deterministic tool, or other execution backend.
- **Role** — the logical work being performed: Generator, Critic, Ranker, Fuser, optional Verifier, or optional extra Evaluator.

The Skill intentionally does not require any specific model vendor, product UI, repo host, or document service.

## Typical setup

1. The user creates or approves a dedicated Shared Workspace.
2. The Orchestrator loads `SKILL.md`.
3. The Orchestrator reads only the reference files required for the current phase (see the phase routing table).
4. The Orchestrator creates or resumes a run, freezes the task, dispatches isolated Generators, evaluates candidates, and fuses the best evidence.
5. The final response points to stable artifacts and records limitations.

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
- `references/workspace-contract.md` — Shared Workspace operations, namespaces, and resume rules.
- `references/executor-contract.md` — Agent Executor capability, dispatch, and artifact-normalization contract.
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

The scripts are optional helpers for local/mounted workspaces. Remote-only Orchestrators may perform equivalent operations through their backend tools. `check_archon_run.py` also validates package consistency (manifest.txt vs file tree, SKILL.md references) when run from the package root.

## Default policy

- 4 independent Generators in parallel.
- Minimum 3 usable Generators by default.
- Critic + Ranker logically separate, physically combinable into one fast call.
- Top 2 full candidates go to Fuser.
- Unique insights from lower-ranked candidates are preserved.
- Verification is optional and scoped (`auto` mode).
- One extra evaluator by default, only when escalation criteria are met.
- One Generator replacement, one fusion repair retry, and one schema repair per result by default.
- Resume uses manifest plus artifact reconciliation; completed expensive stages are never rerun because Orchestrator memory was lost.

## Operational guarantees

- Generator isolation until the generation barrier.
- Durable manifest as the source of truth; no completion claim without an observable artifact.
- Return-only Executor outputs are normalized into the workspace before evaluation.
- Bounded retries/replacements/schema repairs/escalations with budget counters.
- Partial failures are reported, not hidden.
