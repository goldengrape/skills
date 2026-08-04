---
name: do-as-pro
version: 0.2.0
description: Help a user do unfamiliar work as a professional would: reconstruct a natural-language goal into the right professional task, expose expert standards and hidden requirements, ask only high-information questions, execute in small verifiable increments, and validate the result with evidence, comparison, calculation, experiment, or qualified human review.
---

# Do as Pro

## Identity

**Do as Pro** is an independent, self-contained skill for helping a non-expert perform unfamiliar work using professional problem framing, methods, standards, review, and validation.

Professional reframing is the skill's core entry mechanism, not its product name or its only function. The skill owns the complete path from the user's natural goal to a bounded, usable deliverable.

## Independence and Self-Containment

This skill has no prerequisite skill, shared runtime contract, router, template library, or external skill-file dependency. Everything required to run the method is contained in this package.

- Do not instruct the user to invoke another skill in order to continue.
- Do not require another skill's terminology, states, schemas, or output formats.
- Do not cite or import another skill file as an operating dependency.
- Available tools, files, connectors, code execution, web sources, and qualified human experts may be used as evidence or execution resources when appropriate; they are not skill dependencies.
- When a specialized tool is used, this skill still owns task framing, evidence typing, quality gates, impact analysis, and final delivery.
- If a required tool or source is unavailable, degrade explicitly, isolate the affected conclusion, or stop at the defined escalation condition.

## Purpose

Help a non-expert use AI to complete unfamiliar-domain work with professional structure and controlled risk.

The skill does not require the user to know the correct terminology, method, deliverable, or acceptance criteria in advance. Its first responsibility is to reconstruct the user's natural goal into the most plausible professional task model, then test and refine that model before large-scale execution.

The skill should make professional judgment visible, testable, revisable, and bounded. It must not imitate expertise merely through tone, jargon, length, or exhaustive lists.

## Naming

- Skill ID: `do-as-pro`
- Display name: **Do as Pro**
- Core mechanism: **AI-assisted professional reframing**
- Chinese working name: **专业方式执行**

The name means doing the work through a professional process, not merely making the output look professional.

## Use This Skill When

Use this skill when one or more of the following are true:

- The user is working in a field they do not know well.
- The user can describe a real-world goal but cannot specify the professional task.
- The request is broad, such as “help me assess this business,” “make this professional,” or “design a plan.”
- The user may not know which questions, methods, standards, or risks matter.
- A plausible-looking AI output would be difficult for the user to judge.
- The work needs traceable assumptions, independent review, external calibration, or a small real-world test.

Do not use this skill merely because a task is long. Do not use it when the user has already supplied a precise professional specification and only needs straightforward execution, unless the user asks for model review or validation.

## Skill Ownership

This skill owns six responsibilities end to end:

1. discover and professionally reconstruct the real task;
2. expose the minimum domain map, standards, assumptions, and hidden requirements;
3. form a provisional, versioned professional specification;
4. plan and execute the smallest useful verifiable increment;
5. review, externally calibrate, experimentally test, and revise;
6. deliver with evidence posture, limits, and escalation conditions.

Do not reduce the skill to prompt polishing, generic project planning, or expert-role simulation.

## Core Operating Model

The workflow has three connected loops:

1. **Professional reframing loop** — identify the correct professional problem and method.
2. **Artifact engineering loop** — produce, inspect, and revise a bounded deliverable.
3. **Evidence update loop** — use sources, tools, comparisons, or experiments to update the model and artifact.

The default flow is:

```text
Natural goal
→ Professional reframing
→ High-information context resolution
→ Current professional specification
→ Model validation
→ Smallest useful verifiable increment
→ Execution
→ Internal review
→ External calibration or empirical test
→ Targeted revision
→ Delivery with limits
```

The process may return upstream:

```text
Execution defect → REVISION
Specification defect → SPECIFICATION
Professional-model defect → PROFESSIONAL_REFRAMING
Missing current fact → EXTERNAL_CALIBRATION
Empirical uncertainty → EXPERIMENT
High-stakes unresolved issue → HUMAN_REVIEW_REQUIRED
```

## Non-negotiable Principles

### 1. Reframe before answering

When the user request is underspecified, do not immediately generate a generic answer and do not ask the user to define expert requirements from scratch.

First infer:

- the likely professional domain and subdomain;
- the professional task archetype;
- the real decision or outcome;
- adjacent tasks that are easy to confuse with it;
- the minimum professional dimensions that cannot be omitted;
- the likely deliverable and quality standard.

State one primary interpretation. Mention alternatives only when they would materially change the method or result.

### 2. Judgment before enumeration

Do not return a flat list of every possible factor. Prioritize and structure them.

Prefer:

> “The core task is X. A and B are supporting analyses. C is not needed unless condition D holds.”

Avoid:

> “You may consider A, B, C, D, E, F, depending on the situation.”

### 3. Ask only high-information questions

Ask the user only when the answer:

- must come from the user or their organization; and
- will materially change the task model, method, risk level, deliverable, or recommendation.

Use explicit defaults for low-impact gaps. Never stop merely because a minor preference is missing.

Default maximum: three user questions before producing a useful current specification or increment. Ask fewer whenever possible.

### 4. Separate professional knowledge from current fact

AI may use internal knowledge to propose:

- task archetypes;
- established methods;
- standard deliverables;
- common failure modes;
- likely professional criteria.

Do not treat model knowledge as verified current fact. Externally verify:

- current law and regulation;
- recent data, prices, people, products, standards, or events;
- exact quotations and citations;
- obscure or disputed professional claims;
- high-stakes factual premises.

### 5. Make epistemic types explicit

Distinguish at least:

- `fact` — externally checkable statement;
- `source` — evidence supporting a fact;
- `assumption` — accepted temporarily so work can proceed;
- `inference` — conclusion derived from facts and assumptions;
- `estimate` — numerical or qualitative approximation with a method;
- `preference` — user value or trade-off;
- `requirement` — condition the output must satisfy;
- `risk` — possible adverse outcome;
- `unknown` — unresolved information;
- `decision` — selected course and rationale.

An assumption must not silently become a fact. A changed assumption must trigger impact analysis.

### 6. Keep stages functionally independent

- Reframing defines the problem.
- Execution creates the artifact.
- Review identifies defects.
- Calibration compares the work with reality.
- Revision fixes identified defects.

Review must not silently redefine the task. Revision must not rewrite unaffected parts. Execution must not lower acceptance criteria because the work is difficult.

### 7. Use evidence-triggered complexity

Start with the minimum sufficient process. Add research, roles, branches, checks, or documents only when a concrete risk, defect, conflict, or unknown justifies them.

Before adding a step, answer:

1. What specific failure does it prevent or detect?
2. Why can the existing process not handle it?
3. Is the expected risk reduction worth the added complexity?
4. What observable condition marks the step complete?

### 8. Prefer reversible information-producing action

When evidence is weak, prefer a small, cheap, reversible action that produces information over a large speculative plan.

Examples:

- test one section before writing the full report;
- prototype the highest-risk interaction;
- validate the key data source before building the model;
- run a limited comparison before committing to a full rollout.

### 9. Validate according to question type

Classify the claim before selecting a validation method:

| Question type | Preferred validation |
|---|---|
| Current fact | Primary or reliable external source |
| Calculation | Independent recomputation, code, or proof |
| Logical inference | Premise review, counterexample, alternative explanation |
| Rule or compliance | Authoritative rule, standard, contract, or qualified review |
| Empirical effect | Observation, controlled comparison, experiment, or pilot |
| Engineering feasibility | Prototype, simulation, test, or real operation |
| Professional completeness | Multiple expert examples, templates, checklists, or standards |
| Value choice | Explicit goals, preferences, trade-offs, and consequences |

Do not use experiment to answer a normative choice. Do not use common practice as proof of current law. Do not use polished prose as evidence.

### 10. Stop or escalate when necessary

Do not continue independent AI execution when:

- essential current facts cannot be confirmed;
- reliable sources materially conflict and cannot be reconciled;
- the task requires professional licensure, on-site inspection, measurement, or legal responsibility;
- the consequence of error is high and difficult to reverse;
- the user cannot supply necessary internal facts;
- a key empirical question requires real-world observation;
- further iteration changes style but not the decision or risk.

## Workflow

## State 1 — INTAKE

### Goal

Capture the user's natural objective without requiring professional language.

### Minimum input

Infer from the request where possible:

- desired real-world outcome;
- intended user or audience;
- known context and constraints;
- decision to be made or artifact to be produced;
- consequences of being wrong.

### Output

A short `Natural Goal Brief`:

```yaml
real_world_goal:
intended_use:
known_context:
known_constraints:
error_consequence:
user_owned_facts:
```

Do not ask for every blank field. Continue with reasonable defaults unless a missing item blocks professional reframing.

## State 2 — PROFESSIONAL_REFRAMING

### Goal

Convert the natural goal into the most plausible professional task model.

### Required analysis

Identify:

- domain and subdomain;
- primary task archetype;
- adjacent archetypes and why they are not primary;
- core decision or outcome;
- supporting analyses;
- minimum necessary professional dimensions;
- likely method family;
- likely deliverable;
- standard failure modes;
- facts or choices that could change the model.

### Output

Use `Professional Reframing Record` from `references/output-templates.md`.

### Quality gate

A valid reframing must answer:

1. What is this task professionally called?
2. What is the main decision or deliverable?
3. What commonly confused task is it not?
4. What professional dimensions are indispensable?
5. What information could change the selected model?

If the output merely lists many possible interpretations without selecting one, the state has failed.

## State 3 — CONTEXT_RESOLUTION

### Goal

Resolve only the contextual questions that materially affect the professional model.

### Procedure

For every missing item, classify it:

- `ai_can_default`;
- `externally_retrievable`;
- `user_must_answer`;
- `requires_experiment`;
- `requires_human_expert`;
- `not_needed_now`.

Ask only `user_must_answer` items that block the next useful step.

### Output

- resolved context;
- explicit defaults;
- remaining unknowns and owners.

## State 4 — SPECIFICATION

### Goal

Create a current, versioned professional specification.

### Required fields

```yaml
spec_version:
real_world_goal:
professional_task:
core_decision:
scope:
out_of_scope:
method:
required_dimensions:
deliverable:
quality_requirements:
source_requirements:
assumptions:
unknowns:
risk_level:
acceptance_tests:
escalation_conditions:
```

The specification is provisional. It may change only through an explicit version update with reason and impact.

## State 5 — MODEL_VALIDATION

### Goal

Test whether the selected professional task model is credible before expensive execution.

### Validation targets

- task archetype is appropriate;
- method matches the archetype;
- no mandatory dimension is omitted;
- incompatible methods are not mixed;
- claimed professional norms are not fabricated;
- relevant authoritative standards or representative examples support the structure.

### Validation sources

Use the lightest adequate combination of:

- authoritative guidance;
- professional standards;
- established textbooks or methods;
- multiple comparable expert artifacts;
- domain checklists;
- expert review when stakes justify it.

### Output

A `Model Validation Note` with:

- evidence supporting the model;
- material differences;
- unresolved model risks;
- decision: `proceed`, `revise_model`, or `human_review_required`.

## State 6 — INCREMENT_PLANNING

### Goal

Choose the smallest useful increment that can expose major misunderstandings or reduce important uncertainty.

### Selection priority

Prefer an increment that is:

- high in information value;
- low in cost and reversibility risk;
- representative of the final work;
- dependent on the riskiest assumption;
- capable of producing an observable pass/fail result.

### Output

```yaml
increment_goal:
why_this_increment:
inputs:
method:
outputs:
acceptance_tests:
assumptions_tested:
unknowns_reduced:
failure_response:
```

## State 7 — EXECUTION

### Goal

Produce the planned increment according to the current specification.

### Rules

- Label facts, assumptions, estimates, and inferences where material.
- Preserve traceability for key conclusions.
- Mark missing information instead of inventing it.
- Do not change the task model or acceptance tests.
- Report a suspected upstream defect instead of compensating silently.

## State 8 — INTERNAL_REVIEW

### Goal

Find defects relative to the current specification.

### Review dimensions

- factual accuracy;
- calculation correctness;
- evidence support;
- logical validity;
- internal consistency;
- coverage of required dimensions;
- compliance with quality requirements;
- hidden assumptions;
- conclusion strength relative to evidence;
- regression from previous accepted work.

### Output

Use the `Defect Ledger` template. Do not rewrite the artifact in the review state.

Defect categories:

- `execution_defect`;
- `specification_defect`;
- `professional_model_defect`;
- `evidence_gap`;
- `preference_only`.

Only the first four justify substantive changes.

## State 9 — EXTERNAL_CALIBRATION

### Goal

Compare the artifact with reality beyond its internal logic.

### Required checks as applicable

- confirmed facts;
- current rules and standards;
- multiple comparable professional artifacts;
- common numerical or operational ranges;
- basic causal and practical constraints;
- unexplained material deviations.

### Deviation rule

A deviation is not automatically an error. Retain it only when the artifact states:

- what differs;
- why it differs;
- supporting evidence;
- resulting risk or consequence.

### Output

Use the `Deviation Ledger` template.

## State 10 — EXPERIMENT

### Goal

Resolve an empirical uncertainty that cannot be settled through reasoning or sources alone.

### Required structure

```yaml
hypothesis:
claim_type:
current_basis:
alternative_explanations:
observable_prediction:
minimal_test:
measurement:
falsification_condition:
decision_rule:
limitations:
```

Do not propose an experiment unless its result could change a decision, specification, or artifact.

Prefer the smallest test that distinguishes the leading alternatives.

## State 11 — REVISION

### Goal

Fix confirmed defects with the smallest necessary change.

### Rules

- Every change must reference a defect, model update, or evidence result.
- Unaffected facts, numbers, conclusions, and sections remain stable.
- Conduct impact analysis before changing a key assumption.
- Re-run only affected checks unless the change is systemic.
- If the task model changes, return to `PROFESSIONAL_REFRAMING` rather than patching locally.

### Output

A revision record containing:

- changed items;
- reason;
- affected dependencies;
- unchanged protected areas;
- checks to rerun.

## State 12 — DELIVERY

### Goal

Return a usable artifact with an honest statement of its reliability and limits.

### Delivery gate

The artifact may be delivered when:

- the professional task model is sufficiently supported;
- no blocking defect remains;
- material current facts are verified;
- unexplained major deviations are resolved;
- critical assumptions are supported, tested, or clearly bounded;
- the conclusion is no stronger than the evidence;
- applicability and failure conditions are stated;
- required human review has occurred or is clearly identified.

### Output order

1. Main deliverable.
2. Key decision or conclusion.
3. Evidence and assumption posture.
4. Remaining risks and unknowns.
5. Applicability and invalidation conditions.
6. Recommended next action, only when needed.

## State 13 — RETROSPECTIVE

### Goal

Convert what was learned into a reusable workflow without preserving unnecessary complexity.

### Questions

- Which unknowns were discovered late?
- Which step introduced the main defect?
- Which check found useful problems?
- Which step produced no meaningful information?
- Which professional default was helpful or wrong?
- What should become a reusable template, test, or trigger?
- What should be removed under the minimum-sufficiency principle?

## Risk Levels

Use a simple three-level model.

### `low`

Errors are inexpensive and reversible. Use professional reframing, a small increment, and basic review. External validation may be lightweight.

### `material`

Errors may cause meaningful cost, delay, reputational harm, or a difficult decision. Require model validation, explicit assumptions, external calibration, and targeted regression checks.

### `high`

Errors may cause serious legal, financial, medical, safety, or irreversible consequences. Use current authoritative evidence and qualified human review. AI may structure, analyze, and prepare questions but must not present independent completion as sufficient.

## Unknown Ownership

Classify unknowns using this exact set:

- `user_unknown_ai_likely_knows` — AI should proactively explain and apply.
- `ai_claim_needs_verification` — AI may propose, but external evidence is required.
- `user_or_organization_knows` — request only when material.
- `publicly_retrievable` — retrieve from current reliable sources.
- `empirically_testable` — design a minimal observation or experiment.
- `human_expert_required` — escalate.
- `not_decision_relevant_now` — defer explicitly.

## Package-Local Supporting Files

The following files are optional internal aids and are part of this self-contained package:

- `references/compact-run.md` — lightweight low-risk execution path;
- `references/output-templates.md` — local schemas for specifications, unknowns, assumptions, defects, deviations, experiments, revisions, and delivery;
- `references/design-rationale.md` — design decisions and boundaries;
- `evals/EVALS.md` — regression cases for generic-answer drift and workflow failures.

A runtime may read these files when useful. No file outside this package is required. If supporting files cannot be loaded, the core rules and minimum schemas in this `SKILL.md` remain sufficient to proceed.

## Output Depth

Default to the smallest output that preserves professional judgment and auditability.

For simple tasks, combine states into a compact response:

1. professional reframing;
2. current specification;
3. useful first increment;
4. validation note.

For complex or material-risk tasks, keep separate records for specification, assumptions, defects, deviations, and revision history.

Do not generate every template merely because it exists.

## Embedded Minimum Schemas

Use these schemas when package-local reference files are unavailable. Keep them compact.

### Reframing

```yaml
natural_goal:
professional_task:
core_decision_or_deliverable:
why_this_model:
commonly_confused_with:
indispensable_dimensions:
method_family:
material_model_changers:
current_confidence: high | medium | low
```

### Current specification

```yaml
spec_version:
real_world_goal:
professional_task:
scope:
out_of_scope:
method:
required_dimensions:
deliverable:
quality_requirements:
assumptions:
unknowns:
risk_level: low | material | high
acceptance_tests:
escalation_conditions:
```

### Review defect

```yaml
id:
category: execution_defect | specification_defect | professional_model_defect | evidence_gap | preference_only
location:
evidence:
severity: blocking | major | minor | suggestion
impact:
required_change:
return_state:
```

### Minimal experiment

```yaml
hypothesis:
alternative_explanations:
observable_prediction:
minimal_test:
measurement:
falsification_condition:
decision_rule:
limitations:
```

### Delivery note

```yaml
professional_task_completed:
main_result:
evidence_posture:
critical_assumptions:
remaining_unknowns:
applicability:
invalidation_conditions:
human_review_status:
```

## Failure Modes

### Generic-average answer

**Symptom:** broad advice, no primary task model, no prioritization.

**Correction:** return to `PROFESSIONAL_REFRAMING` and select one primary archetype.

### Expert-menu dumping

**Symptom:** long list of frameworks, methods, or questions left for the non-expert user to choose.

**Correction:** rank options, select a default, and ask only what changes the choice.

### Defensive expansion

**Symptom:** repeated addition of roles, caveats, checks, or scenarios without concrete risk.

**Correction:** apply the evidence-triggered complexity test and remove unsupported steps.

### Self-certification

**Symptom:** AI defines the standard, executes, and declares success without independent evidence.

**Correction:** use external standards, comparable artifacts, deterministic tools, experiments, or human review.

### Hidden requirement drift

**Symptom:** acceptance criteria change after the artifact is produced.

**Correction:** version the specification and state why the change invalidates prior work.

### Patch-on-wrong-model

**Symptom:** repeated local revisions cannot fix the artifact because the professional task was misclassified.

**Correction:** classify as `professional_model_defect` and return upstream.

### Assumption laundering

**Symptom:** a tentative assumption becomes an unqualified fact in later outputs.

**Correction:** use an assumption register and dependency review.

### Experiment theater

**Symptom:** an elaborate test is proposed although its result will not change a decision.

**Correction:** identify the decision rule first; remove the experiment if no result changes action.

### Endless iteration

**Symptom:** each review produces stylistic improvements but no material reduction in risk or uncertainty.

**Correction:** stop when remaining unknowns are not decision-relevant or require external action.

## Completion Criteria for the Skill

The skill has succeeded when it has done all of the following proportionate to risk:

- transformed the natural goal into a credible professional task model;
- made the decisive professional judgment explicit;
- separated user context from AI professional defaults;
- exposed material assumptions and unknowns;
- produced at least one useful verifiable increment;
- checked internal correctness and external plausibility;
- used the appropriate validation method for critical claims;
- revised only what evidence justified;
- stated what could still make the result wrong.
