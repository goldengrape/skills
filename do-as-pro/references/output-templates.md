# Output Templates

Use only the templates needed for the current task. Keep records short enough to remain readable.

## Professional Reframing Record

```yaml
natural_goal:
primary_domain:
primary_task_archetype:
professional_name:
core_decision_or_deliverable:
why_this_model:
commonly_confused_with:
why_not_the_adjacent_model:
supporting_workstreams:
indispensable_dimensions:
method_family:
expected_deliverable:
professional_defaults:
material_model_changers:
current_confidence: high | medium | low
```

## Current Professional Specification

```yaml
spec_version:
real_world_goal:
professional_task:
core_decision:
audience_or_user:
scope:
out_of_scope:
method:
required_dimensions:
deliverable:
quality_requirements:
source_requirements:
assumptions:
unknowns:
risk_level: low | material | high
acceptance_tests:
escalation_conditions:
```

## Unknown Register

| ID | Unknown | Owner class | Why it matters | Blocks now? | Resolution method | Affected outputs | Status |
|---|---|---|---|---|---|---|---|

Owner classes:

- `user_unknown_ai_likely_knows`
- `ai_claim_needs_verification`
- `user_or_organization_knows`
- `publicly_retrievable`
- `empirically_testable`
- `human_expert_required`
- `not_decision_relevant_now`

## Assumption Register

| ID | Assumption | Type | Current basis | Confidence | Dependent conclusions | Validation method | Falsification condition | Status |
|---|---|---|---|---|---|---|---|---|

Suggested assumption types:

- factual
- causal
- behavioral
- numerical
- operational
- design
- normative

Suggested statuses:

- proposed
- accepted_for_now
- supported
- weakened
- rejected
- deferred

## Defect Ledger

| ID | Category | Location | Violated requirement | Evidence | Severity | Impact | Required change | Return state | Status |
|---|---|---|---|---|---|---|---|---|---|

Categories:

- `execution_defect`
- `specification_defect`
- `professional_model_defect`
- `evidence_gap`
- `preference_only`

Severities:

- blocking
- major
- minor
- suggestion

## Deviation Ledger

| ID | Dimension | Current result | External reference | Deviation | Explanation | Evidence | Risk | Disposition |
|---|---|---|---|---|---|---|---|---|

Dispositions:

- accept
- revise
- investigate
- convert_to_assumption
- human_review

## Minimal Experiment Record

```yaml
hypothesis:
claim_type:
current_basis:
alternative_explanations:
observable_prediction:
minimal_test:
sample_or_inputs:
measurement:
falsification_condition:
decision_rule:
limitations:
result:
model_update:
```

## Revision Record

```yaml
revision_id:
trigger_defects_or_evidence:
changes:
affected_dependencies:
protected_unchanged_areas:
checks_to_rerun:
result:
```

## Delivery Note

```yaml
professional_task_completed:
main_result:
evidence_posture:
critical_assumptions:
remaining_unknowns:
external_deviations:
applicability:
invalidation_conditions:
human_review_status:
```
