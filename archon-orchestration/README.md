# Archon Orchestration Skill

A harness-neutral Skill for orchestrating multiple AI Agent Executors through a user-provided Shared Workspace.

## Core flow

```text
Generate → Critique → Rank / Filter → Fuse
```

Optional verification can be inserted before evaluation and/or after fusion when the task has a reliable verifier.

## Core abstractions

- **Orchestrator** — the harness/controller that loads the Skill and advances the run.
- **Shared Workspace** — a user-provided GitHub repo, Google Drive folder, or future compatible backend.
- **Agent Executor** — a browser web agent, API-backed agent, local agent, or other execution backend.

The Skill intentionally does not require Codex, ChatGPT, GitHub, or a specific model vendor.

## Typical setup

1. User creates a dedicated GitHub repository or Google Drive folder and grants the required AI access.
2. Install this Skill into a compatible Orchestrator.
3. Start a task and point the Orchestrator at the Shared Workspace.
4. The Orchestrator creates a run, dispatches isolated Generator Agent Executors, evaluates them, and fuses the best candidates.

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

## Local helper scripts

For a workspace available as a local/mounted directory:

```bash
python scripts/init_archon_run.py --root . --mode standard --workspace-backend github
python scripts/advance_archon_state.py --root . --run-id <RUN_ID> --to GENERATING
python scripts/check_archon_run.py --root . --run-id <RUN_ID>
```

The scripts are optional helpers. Remote-only Orchestrators may perform equivalent operations through GitHub/Drive tools.

## Default policy

- 4 independent Generators in parallel
- Critic + Ranker logically separate, physically combinable into one fast call
- top 2 full candidates into Fuser
- preserve unique insights from lower-ranked candidates
- optional verifier in `auto` mode
- one additional evaluator only when uncertain/high-risk
- bounded retry policy
