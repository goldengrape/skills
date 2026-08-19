# Phase Cards

Use this file as the operational runbook after `SKILL.md` has routed the current phase. Each card states inputs, actions, outputs, and failure handling. For non-ideal situations, load `references/failure-recovery.md` instead of improvising.

## initialize-or-resume

Inputs:
- user's current instruction
- approved Shared Workspace root or dry-run approval
- available Orchestrator capabilities
- available Agent Executor capabilities
- existing manifest, if resuming

Actions:
1. Identify the exact workspace backend and authorized root.
2. Read or create `.archon/runs/<run_id>/manifest.json` (schema 0.2; see `templates/manifest.json`).
3. Freeze the task snapshot into `.archon/runs/<run_id>/task.md`.
4. Record executor capabilities in `executors.json` or manifest metadata.
5. Select execution policy: generator count, quorum, top K, verifier mode, retry/replacement/schema-repair budgets.
6. Decide whether a reliable verifier exists. If not, record verifier mode as disabled/unavailable with reason when a verifier record is needed.
7. Create one isolated namespace per scheduled Generator before any Generator starts.
8. Run `checklists/run_start.md`.

Outputs:
- `manifest.json`
- `task.md`
- executor capability notes
- isolated Generator namespaces
- selected adapter
- stage remains `INIT` until ready to advance to `GENERATING`

Failure handling:
- If workspace scope is broad or missing, CHECKPOINT.
- If read/write fails, STOP and repair permissions or backend.
- If task snapshot is incomplete, do not dispatch generation.
- If resuming, reconcile manifest with artifacts first (see `references/failure-recovery.md`).

## generate

Inputs:
- frozen `task.md`
- shared base artifact references
- policy
- executor capability notes
- one assigned namespace per Generator
- role instructions from `references/role-prompts.md#generator`

Actions:
1. Dispatch independent Generators in parallel when possible.
2. Assign stable IDs: `G1`, `G2`, `G3`, ...; replacement IDs are distinct (`G3R1`) with `replaces: "G3"`.
3. Give each Generator only the frozen task, shared base input, constraints, allowed tools, and its own namespace.
4. For browser-operated Agents, use separate pages/sessions for independent Generators.
5. For return-only Executors, collect the returned content, persist a safe raw return (`generation/<ID>/raw-return.md`), normalize it into the assigned namespace, and write `generation/<ID>/result.json` with `direct_workspace_write: false` and `return_only_normalized_by_orchestrator: true`.
6. Persist terminal status and artifact reference for each scheduled Generator.
7. Record failures, cancellations, timeouts, contamination, and normalization failures instead of hiding them.

Generator must not receive or read:
- sibling Generator outputs from the same run
- current-run critiques
- current-run rankings
- fusion artifacts
- final artifacts from the same run before the barrier

Outputs:
- `generation/<ID>/result.json` or backend-equivalent terminal records
- artifact references for completed candidates
- manifest execution updates

Failure handling:
- If a Generator sees another candidate before the barrier, mark it `contaminated`.
- If an Executor cannot write directly, the Orchestrator normalizes the result with `direct_workspace_write: false`.
- If a return-only result is malformed, capture the raw return and attempt one schema repair if policy permits; otherwise mark `failed` with `failure_reason: "normalization_failed"`.
- Do not launch duplicate replacement work for a still-running expensive Executor unless policy permits.

## generation-barrier

Inputs:
- manifest
- all scheduled Generator terminal records (including replacements)
- candidate artifact references
- policy quorum

Actions:
1. Confirm every scheduled Generator is terminal: `completed`, `failed`, `cancelled`, or `contaminated`.
2. Confirm completed candidates have stable artifact references; a timeout is `failed` with `failure_reason: "timeout"` unless the Executor is still observable.
3. Distinguish terminal executions from usable candidates: a candidate is usable only when terminal `completed`, uncontaminated, and has a stable `artifact_ref`.
4. Exclude contaminated candidates from independent-candidate counts.
5. Apply quorum:
   - all usable and coverage adequate: continue.
   - exactly one failure/cancellation and at least 3 usable: continue and record degraded quorum.
   - fewer than 3 usable: replace once within budget; otherwise CHECKPOINT or fail/partial.
6. Freeze the usable candidate set for evaluation.
7. Run `checklists/generation_barrier.md`.

Outputs:
- barrier decision
- usable candidate set
- recorded degradation/replacement decision when relevant

Failure handling:
- If any scheduled Generator is non-terminal, do not evaluate yet.
- If candidate IDs are unstable, reconcile before Critique.
- If namespace collision occurred, STOP and repair before continuing.

## optional-candidate-verification

Inputs:
- usable candidates
- available verifier capability
- verifier policy
- task-specific oracle definition

Actions:
1. Run only checks that actually exist and are authorized.
2. Capture command/tool, scope, status, summary, artifact reference, and limitations.
3. Distinguish candidate failure (`fail`) from verifier/infrastructure failure (`error`) and unavailability (`unavailable`).
4. Feed evidence to Critic/Ranker.

Outputs:
- `verification/*.json` evidence records
- manifest artifact references

Failure handling:
- If a verifier is unavailable, record it as unavailable; do not penalize candidates for unavailable evidence.
- Do not claim pass/fail for a command or tool that did not run.

## critique-and-rank

Inputs:
- frozen task
- usable candidate artifacts
- terminal status summaries for unusable candidates
- optional verification evidence
- role instructions for Critic and Ranker

Actions:
1. Critic evaluates every usable candidate.
2. Critic extracts strengths, weaknesses, missing assumptions, risks, unique insights, reusable parts, and evidence conflicts.
3. Ranker orders candidates against the frozen task and evidence.
4. Ranker selects top K full candidates for Fuser.
5. Ranker preserves useful lower-ranked insights before filtering.
6. Anonymize provider/model identity when practical.
7. Persist Critic and Ranker outputs as logically separate artifacts even if one physical call produced both.
8. Escalate to at most one extra evaluator by default if confidence is low, evidence conflicts, top candidates are near-tied, or task risk is high.
9. Run `checklists/evaluation.md`.

Outputs:
- `critique/critique.json`
- `ranking/ranking.json`
- optional extra evaluator note
- manifest artifact references

Failure handling:
- If Critic/Ranker output is malformed, repair the schema once if policy permits or use a fast alternate evaluator within budget.
- If Ranker lacks inputs it claims to rank, STOP and rebuild evaluation input.
- Do not collapse evaluation into a single score.

## fuse

Inputs:
- frozen task
- full top K candidate artifacts
- Critic findings for all candidates
- Ranker decision
- preserved lower-ranked insights
- optional verification evidence

Actions:
1. Create a new final candidate in an isolated fusion namespace.
2. Synthesize strong parts and resolve contradictions explicitly.
3. Do not blindly concatenate candidates.
4. Do not silently copy the top-ranked candidate.
5. If synthesis adds no value, intentionally adopt the winner and record why (manifest `decisions.winner_adoption`).
6. For code work, use a separate fusion branch/namespace.
7. For document work, create a new final-draft artifact rather than overwriting candidates.
8. Run `checklists/fusion.md`.

Outputs:
- fused artifact reference or explicit winner-adoption record
- `fusion/result.json`
- manifest artifact reference

Failure handling:
- If selected artifact references are inaccessible, STOP and repair.
- If fusion fails due to infrastructure, retry once when policy permits.
- Never loop silently.

## optional-final-verification

Inputs:
- fused result or adopted winner
- verifier policy
- relevant candidate-verification context

Actions:
1. Treat the fused result as a new candidate.
2. Re-run relevant checks because fusion can introduce new failure.
3. Record scoped evidence and limitations.
4. If verification fails, decide whether repair is justified and within policy.

Outputs:
- final verification evidence records
- repair/failure decision

Failure handling:
- If artifact failure and retry budget remains, send evidence to one repair/fusion execution.
- If still failing, prefer a previously verified top-ranked candidate when appropriate, or finalize as failed/partial with evidence.
- If the verifier fails due to infrastructure, do not mislabel the artifact as failed.

## finalize

Inputs:
- final artifact or failure evidence
- manifest
- ranking and fusion artifacts
- verification evidence
- approval state for irreversible actions

Actions:
1. Write `final/outcome.json`.
2. Set manifest outcome to `DONE`, `PARTIAL`, or `FAILED`.
3. Record selected candidates, terminal statuses, verifier coverage, replacements, retries, schema repairs, escalations, and limitations.
4. Record any irreversible action still awaiting approval.
5. Run `checklists/finalize.md`.
6. Return a concise user-facing outcome with stable artifact references.

Outputs:
- final outcome record
- updated manifest
- user-facing summary

Failure handling:
- If the final artifact reference is missing, do not mark `DONE`.
- If a final action requires approval, leave the action pending and report it clearly.
- If manifest and artifacts disagree, reconcile before responding as complete.
