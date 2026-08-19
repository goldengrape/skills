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
4. Record executor capabilities in `executors.json` or manifest metadata, including workspace read/write transport and browser isolation unit.
5. Select execution policy: generator count, quorum, top K, verifier mode, retry/replacement/schema-repair budgets.
6. Select workspace I/O policy. For GitHub, default to `workspace_io_mode: direct_required`, `inline_artifact_transport: false`, and `allow_return_only_fallback: false` unless the user explicitly approves a degraded path.
7. For browser-operated Generators, record `browser_base_url` when supplied. A ChatGPT project/workspace URL is a base/landing URL only; it does not identify a conversation to reuse.
8. Decide whether a reliable verifier exists. If not, record verifier mode as disabled/unavailable with reason when a verifier record is needed.
9. Create one isolated namespace per scheduled Generator before any Generator starts.
10. Confirm each planned browser Generator can create a fresh page/tab and fresh conversation and can access the required workspace refs/tools from that fresh context.
11. Run `checklists/run_start.md`.

Outputs:
- `manifest.json`
- `task.md`
- executor capability notes
- isolated Generator namespaces
- selected adapter
- workspace I/O policy and browser execution policy
- stage remains `INIT` until ready to advance to `GENERATING`

Failure handling:
- If workspace scope is broad or missing, CHECKPOINT.
- If read/write fails, STOP and repair permissions or backend.
- If task snapshot is incomplete, do not dispatch generation.
- If a direct-required Executor cannot read/write the workspace, replace/reconfigure the Executor or CHECKPOINT; do not silently paste/upload the workspace through chat.
- If browser fresh-page/fresh-conversation isolation cannot be guaranteed, CHECKPOINT or reconfigure before generation.
- If resuming, reconcile manifest with artifacts first (see `references/failure-recovery.md`).

## generate

Inputs:
- frozen `task.md`
- shared base artifact references
- workspace I/O policy
- browser execution policy when applicable
- policy
- executor capability notes
- one assigned namespace per Generator
- role instructions from `references/role-prompts.md#generator`

Actions:
1. Dispatch independent Generators in parallel when possible.
2. Assign stable IDs: `G1`, `G2`, `G3`, ...; replacement IDs are distinct (`G3R1`) with `replaces: "G3"`.
3. Give each Generator only compact control metadata: frozen task ref, allowed shared base refs, constraints, allowed tools, and its own namespace. Do not duplicate substantive workspace artifacts into the prompt when the Executor can read them from the workspace.
4. For browser-operated Agents, start one distinct browser invocation per independent Generator, create a fresh page/tab, and create a fresh conversation from `browser_base_url`. Never use another Generator's existing page, conversation, follow-up chain, or saved session.
5. If `browser_base_url` is a user-provided ChatGPT project/workspace URL, use that same base for each Generator if desired, but still create a new page and new conversation for every Generator.
6. For GitHub `direct_required` mode, require the Generator to read task/base inputs from GitHub refs and write the substantive candidate directly to its assigned GitHub branch/namespace. The browser response is only a compact receipt with stable artifact/version refs and metadata.
7. After a direct-write Generator returns a receipt, independently fetch/verify the referenced workspace artifact before marking it complete.
8. Use return-only normalization only when workspace policy explicitly allows it. When allowed, collect the returned content, persist a safe raw return (`generation/<ID>/raw-return.md`), normalize it into the assigned namespace, and write `generation/<ID>/result.json` with `direct_workspace_write: false` and `return_only_normalized_by_orchestrator: true`.
9. Persist terminal status, page/conversation isolation metadata when available, and artifact reference for each scheduled Generator.
10. Record failures, cancellations, timeouts, contamination, capability mismatch, and normalization failures instead of hiding them.

Generator must not receive or read:
- sibling Generator outputs from the same run
- current-run critiques
- current-run rankings
- fusion artifacts
- final artifacts from the same run before the barrier

For direct GitHub transport, Generator should not receive through the browser composer:
- copies of repository files already available by GitHub ref
- full candidate artifacts as previous-turn context
- large diffs or prior outputs copied from the workspace

Outputs:
- `generation/<ID>/result.json` or backend-equivalent terminal records
- stable artifact references for completed candidates
- page/conversation isolation metadata when available
- manifest execution updates

Failure handling:
- If a Generator sees another candidate before the barrier, mark it `contaminated`.
- If a browser Generator reused another Generator's conversation or follow-up chain, mark it `contaminated` unless equivalent isolation can be proven.
- If a fresh page/conversation cannot access required direct-workspace tools, mark capability mismatch and reconfigure/replace; do not automatically turn on inline artifact transport.
- If an Executor cannot write directly and return-only fallback was not explicitly allowed, do not dispatch it as a compatible direct-write Generator.
- If an explicitly allowed return-only result is malformed, capture the raw return and attempt one schema repair if policy permits; otherwise mark `failed` with `failure_reason: "normalization_failed"`.
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
3. For browser Generators, confirm required page/conversation isolation was satisfied; a candidate without independent conversation isolation is not counted as an independent usable sample.
4. Distinguish terminal executions from usable candidates: a candidate is usable only when terminal `completed`, uncontaminated, artifact-backed, and compliant with required transport/isolation policy.
5. Exclude contaminated candidates from independent-candidate counts.
6. Apply quorum:
   - all usable and coverage adequate: continue.
   - exactly one failure/cancellation and at least 3 usable: continue and record degraded quorum.
   - fewer than 3 usable: replace once within budget; otherwise CHECKPOINT or fail/partial.
7. Freeze the usable candidate set for evaluation.
8. Run `checklists/generation_barrier.md`.

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
8. Prefer workspace references for candidate delivery to capable evaluators instead of copying all candidate bodies into the Orchestrator conversation.
9. Escalate to at most one extra evaluator by default if confidence is low, evidence conflicts, top candidates are near-tied, or task risk is high.
10. Run `checklists/evaluation.md`.

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
8. When the Fuser has direct workspace access, give it refs to top candidates/critique/ranking and require direct output to the fusion namespace; do not round-trip large artifacts through chat.
9. Run `checklists/fusion.md`.

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
3. Record selected candidates, terminal statuses, verifier coverage, replacements, retries, schema repairs, escalations, transport downgrades, browser-isolation limitations, and other limitations.
4. Record any irreversible action still awaiting approval.
5. Run `checklists/finalize.md`.
6. Return a concise user-facing outcome with stable artifact references rather than dumping workspace artifacts into the conversation.

Outputs:
- final outcome record
- updated manifest
- user-facing summary

Failure handling:
- If the final artifact reference is missing, do not mark `DONE`.
- If a final action requires approval, leave the action pending and report it clearly.
- If manifest and artifacts disagree, reconcile before responding as complete.
