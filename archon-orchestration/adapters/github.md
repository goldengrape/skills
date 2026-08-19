# GitHub Shared Workspace Adapter

Use GitHub when code versioning, branches, commits, diffs, PRs, or repository-native artifacts matter.

## Transport rule: GitHub is the data plane

When this adapter is active, treat GitHub as the primary input/output transport for substantive artifacts. The Orchestrator conversation and browser prompt are a control plane, not a file-transfer channel.

Default GitHub policy:

```yaml
workspace_io_mode: direct_required
inline_artifact_transport: false
allow_return_only_fallback: false
```

This means:

- Freeze the task and shared inputs in GitHub first, then dispatch stable refs/URLs plus compact instructions.
- Do not paste repository files, large task bodies, candidate artifacts, diffs, critiques, rankings, or fused output into a browser composer when the Executor can read them from GitHub.
- Do not ask an Executor to return a full candidate through the chat response when it can write GitHub directly.
- A Generator completes by writing its candidate to its assigned branch/namespace and returning only a compact receipt containing stable refs, commit/version identity, summary, tests/evidence, and limitations.
- The Orchestrator verifies the referenced GitHub artifact before marking the execution `completed`.

If a proposed Executor cannot read and write the authorized GitHub workspace, it is not a compatible direct-write Generator for this adapter. Do not silently downgrade to chat/file transfer. Use another Executor, or set `allow_return_only_fallback: true` only when the user explicitly accepts the degraded transport path.

## Recommended mapping

Control state can live on a dedicated orchestration branch or in a serialized control namespace managed by Orchestrator.

```text
base ref: <frozen task base SHA when relevant>

Generator branches:
  archon/<run_id>/G1
  archon/<run_id>/G2
  archon/<run_id>/G3
  archon/<run_id>/G4

Fuser branch:
  archon/<run_id>/F
```

The control namespace stores small files such as:

```text
.archon/runs/<run_id>/manifest.json
.archon/runs/<run_id>/task.md
.archon/runs/<run_id>/critique/critique.json
.archon/runs/<run_id>/ranking/ranking.json
.archon/runs/<run_id>/final/outcome.json
```

Candidate code or document artifacts should remain in candidate branches/namespaces. Store branch/commit/file refs in result metadata instead of copying whole files or diffs into control files.

## Input delivery

For each Generator, dispatch only the minimum control message needed to locate its inputs:

```text
run_id
candidate_id
task_ref
base_ref / allowed input refs
assigned branch or namespace
output contract
constraints
```

The Executor reads the frozen task and substantive base inputs from GitHub itself. A public GitHub URL/raw URL or an authorized GitHub connector/tool may be used as the read path. For private repositories, verify authorized repository access before dispatch.

Do not use browser upload/attachment flags or giant inline prompts merely to duplicate artifacts that already exist in the Shared Workspace.

## Output delivery

A direct-write Generator should:

1. Work only in `archon/<run_id>/<ID>` or the mapped isolated namespace.
2. Write or modify the candidate artifact there.
3. Commit/version the result when the backend supports it.
4. Return a compact receipt, for example:

```json
{
  "candidate_id": "G1",
  "status": "completed",
  "artifact_ref": "branch:archon/run-017/G1@<sha>",
  "version": "<sha>",
  "summary": "...",
  "evidence": [],
  "limitations": []
}
```

The receipt is metadata, not the artifact itself. The Orchestrator then reads/verifies the GitHub ref and writes normalized control metadata as needed.

## Isolation

- All Generator branches start from the same frozen base ref unless the task explicitly needs otherwise.
- A Generator must not inspect sibling `archon/<run_id>/G*` branches before the barrier.
- Browser-page isolation and GitHub-branch isolation are both required for an independent browser Generator; one does not substitute for the other.
- Fuser may inspect candidates only after barrier/evaluation.

## Return-only degraded mode

Return-only normalization remains available to the generic Archon protocol, but it is not the normal GitHub path. Enable it for a GitHub run only when the user explicitly accepts that the Orchestrator must ferry artifact content through the Executor return channel.

When enabled, record the downgrade in manifest/history and keep it bounded to Executors that genuinely cannot write GitHub. Never choose return-only merely because it is easier than configuring direct repository access.

## Final integration

Do not merge candidate branches directly into the protected/default branch during generation. Final merge/PR follows user/repo approval policy.
