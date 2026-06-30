---
type: Factory Lifecycle
title: Instantiation Lifecycle
description: The full lifecycle from user input to generated stateful course OKF.
tags: [factory, lifecycle]
timestamp: 2026-06-30T00:00:00-07:00
---
# Lifecycle

```text
user input
→ validate intake
→ run reconnaissance
→ build course map
→ classify A/B/C priorities
→ create course OKF directory
→ initialize state
→ create seven-day plan
→ create Day 1 work package
→ run session
→ update state
→ adapt future plan
→ repeat
→ export final review
```

# Phase 1: Validate Intake

Check course name, baseline, available days, daily minutes, target, and exam format. If missing fields are not critical, use defaults and write assumptions into `mission.md`.

# Phase 2: Reconnaissance

Gather enough information to identify likely units, high-frequency concepts, and exam patterns.

# Phase 3: Instantiate Files

Create the generated bundle using [Course Instance Layout](/schemas/course-instance-layout.md).

# Phase 4: Initialize State

Write the first version of:

* `state/current-state.md`
* `state/topic-ledger.md`
* `state/recall-deck.md`
* `state/misconceptions.md`
* `state/score-history.md`
* `state/next-action.md`

# Phase 5: Run and Adapt

Every session must read state, teach, test, write evidence, then adapt future work.
