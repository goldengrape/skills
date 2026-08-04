# Evaluation Cases

A skill run passes only when it demonstrates professional selection, not merely fluent completion.

## Eval 1 — Vague task

### Prompt

> 帮我做一个专业的竞争分析。

### Pass conditions

- Selects or infers a likely decision context.
- Distinguishes competitor profiling from competitive strategy, sales battlecard, and market structure analysis.
- Asks at most three material questions.
- Produces a default professional model and first useful increment.

### Fail conditions

- Returns a generic SWOT template.
- Lists every possible analysis framework without choosing.
- Requires the user to specify all dimensions.

## Eval 2 — User unknown, AI likely knows

### Prompt

> 我第一次负责供应商评估，不知道该看什么。

### Pass conditions

- Proactively supplies the professional evaluation dimensions and process.
- Separates mandatory, risk-based, and optional criteria.
- Requests only organization-specific risk tolerance or constraints.

### Fail conditions

- Tells the user to consult an expert without first providing useful structure.
- Asks the user what criteria they want.

## Eval 3 — Adjacent-task confusion

### Prompt

> 我想知道这个产品有没有市场，帮我做市场规模。

### Pass conditions

- Explains that market existence, demand validation, and market sizing are related but distinct.
- Selects demand validation or feasibility as primary when appropriate.
- Avoids treating a large top-down market number as proof of product demand.

## Eval 4 — Current fact versus professional model

### Prompt

> 按最新规定帮我设计这个流程。

### Pass conditions

- Uses professional knowledge to propose the process structure.
- Flags current rules for authoritative external verification.
- Does not rely solely on model memory for the latest regulation.

## Eval 5 — Scientific-method routing

### Prompt

> 我觉得把注册流程缩短会提高付费转化，怎么判断？

### Pass conditions

- Converts the claim into a falsifiable hypothesis.
- Identifies alternative explanations.
- Proposes the smallest test that can change a decision.
- Defines metrics and decision rule.

### Fail conditions

- Gives only generic UX advice.
- Proposes a large research program without a decision rule.

## Eval 6 — Normative question

### Prompt

> 公司应该优先增长还是利润？

### Pass conditions

- Recognizes a value and strategy choice rather than a purely empirical question.
- Requests or infers goals, runway, constraints, and risk tolerance.
- Uses scenarios to show consequences without claiming an experiment can decide values.

## Eval 7 — Defensive expansion

### Prompt

> 帮我检查一页活动方案。

### Pass conditions

- Uses a compact review proportional to risk.
- Does not create a multi-agent governance workflow.
- Adds checks only for specific identified risks.

## Eval 8 — Wrong model recovery

### Scenario

The first draft treats a question as a market overview, but later evidence shows the user needs an investment decision.

### Pass conditions

- Labels a professional-model defect.
- Returns to reframing and updates the specification version.
- Identifies which existing work can be retained.

### Fail conditions

- Adds an investment recommendation paragraph to the existing overview without restructuring.

## Eval 9 — External deviation

### Scenario

A financial estimate is three times the range seen in credible comparable cases.

### Pass conditions

- Flags the deviation.
- Checks context, units, and assumptions.
- Accepts it only with evidence and risk explanation.

### Fail conditions

- Rejects it solely because it differs from the average.
- Accepts it because the internal calculation is consistent.

## Eval 10 — Stop condition

### Scenario

The task depends on an unavailable on-site safety inspection.

### Pass conditions

- Completes useful preparatory analysis.
- Clearly identifies the unresolved dependency and affected conclusions.
- Stops before presenting the task as safely complete.
