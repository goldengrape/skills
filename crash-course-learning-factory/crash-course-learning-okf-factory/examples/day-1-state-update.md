---
type: Example
title: Day 1 State Update
description: Example of how state changes after the first session.
tags: [example, state-update]
timestamp: 2026-06-30T00:00:00-07:00
---
# Before Day 1

```yaml
current_day: 1
completed_sessions: 0
pass_readiness: very_low
next_action: run_day_1
```

# After Day 1

```yaml
current_day: 2
completed_sessions: 1
pass_readiness: low
risk_level: medium
next_action: continue
latest_summary: "Learner can roughly describe the four management functions but confuses planning with decision-making."
```

# New Recall Cards

```yaml
cards:
  - id: recall-001
    topic_id: management-functions
    prompt: "不看笔记，说出管理的四项基本职能，并各用一句话解释。"
    expected_answer_points: ["计划", "组织", "领导", "控制"]
    due_on: "Day 2"
    status: due
```

# New Misconception

```yaml
misconceptions:
  - id: misc-001
    topic_id: planning-vs-decision
    error_statement: "把计划等同于决策。"
    severity: medium
    repair_status: open
    repair_prompt: "用一个学生社团活动的例子区分计划和决策。"
```
