# Execution Policy

Load this file when initializing policy, changing budget, handling quorum, deciding verification, or escalating evaluation. Policy keys below match `manifest.json` exactly.

## Standard mode

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

## Policy variants

A compatible Orchestrator may expose named modes, but must record the concrete policy in `manifest.json`.

### fast

Use when latency matters and the user accepts less redundancy.

```yaml
generator_count: 4
minimum_usable_generators: 3
combine_critic_ranker: true
max_extra_evaluators: 0
max_fusion_retries: 0
max_schema_repairs_per_result: 1
```

### strict

Use when candidate independence and review separation matter more than speed.

```yaml
generator_count: 4
minimum_usable_generators: 4
combine_critic_ranker: false
max_extra_evaluators: 1
max_fusion_retries: 1
max_schema_repairs_per_result: 1
```

## Budget counters

Track these counters in `manifest.json`:

* `generator_replacements_used`
* `extra_evaluators_used`
* `fusion_retries_used`
* `schema_repairs_used`

The Orchestrator may not exceed the configured maximums without a CHECKPOINT. `max_schema_repairs_per_result` is a separate budget from evaluator escalation: do not count a schema repair as an extra evaluator unless a new evaluator is dispatched.

## Latency-aware policy

The expensive stages should normally be:

```text
max(Generator wall-clock) + Fuser wall-clock
```

Evaluation should usually be shorter. Do not add fixed long-running Critic ensembles unless the task justifies the time.

## Generator replacement policy

A replacement is allowed by default only when:

* a scheduled Generator fails, is cancelled, is contaminated, or returns an unusable result;
* the usable candidate count would otherwise fall below policy or important coverage is missing;
* replacement budget remains.

Use a new candidate ID, for example `G3R1`, and record:

```json
{
  "candidate_id": "G3R1",
  "replaces": "G3",
  "reason": "contaminated",
  "replacement_attempt": 1
}
```

Do not overwrite the original failed or contaminated namespace.

## Return-only normalization policy

A return-only Executor may produce useful content without direct workspace access. The Orchestrator must normalize it before evaluation:

1. Persist safe raw return content.
2. Extract or create the durable candidate artifact.
3. Write `generation/<ID>/result.json`.
4. Record normalization status in the manifest.
5. Mark the execution `failed` if normalization cannot produce a stable artifact reference.

A transient page, message, or console response is not enough for `completed`.

## Candidate quorum

Default barrier decisions:

* all scheduled Generators usable with adequate coverage: continue.
* exactly one failure/cancellation and at least 3 usable: continue and record degraded quorum.
* fewer than 3 usable: replace failed/contaminated candidates once within budget; otherwise CHECKPOINT or fail/partial.
* contaminated candidate: never count as independent; replace once if policy allows.

A failed, cancelled, timed-out, or contaminated execution must remain visible in manifest history. A timeout is recorded as `failed` with `failure_reason: "timeout"` unless the Executor can still be observed and recovered.

## Evaluation escalation triggers

Use at most one extra evaluator by default when one or more are true:

* ranking confidence is below the configured threshold
* top candidates are near-tied on important criteria
* verifier evidence conflicts with Critic/Ranker judgment
* the task is high-risk and failure cost is material
* Critic identifies a critical unresolved assumption
* evaluation output is valid but internally inconsistent

Malformed Critic/Ranker output should first use one schema repair if policy permits. Do not use extra evaluators to mask missing input. If the Ranker lacks candidates, critique, or evidence it claims to use, rebuild the input instead.

## Fuser policy

Standard mode performs fusion. A low-latency policy may intentionally adopt a clear winner only when:

* ranking confidence is high
* verifier evidence strongly separates candidates when applicable
* lower-ranked candidates offer no unique useful insight
* user or configured policy prefers lower latency

Record intentional winner adoption in manifest (`decisions.winner_adoption`) and final outcome. Do not silently skip fusion.

## Verification policy hook

Verification mode values:

* `auto`: run only when a reliable, scoped verifier exists in the current environment.
* `enabled`: attempt verification and record pass/fail/error/unavailable.
* `disabled`: do not run verification; record the reason if the task would normally benefit.

Verification cannot replace Critic/Ranker unless the task is purely deterministic and the user explicitly wants that behavior.

## Executor preference

Default priority for high-value roles:

1. capable Agent Executor with direct Shared Workspace access
2. capable API-backed Agent Executor with durable artifact output
3. return-only execution that the Orchestrator can normalize

This is a capability preference, not a vendor rule.
