---
type: Factory Concept
title: Factory Overview
description: Defines what the Crash Course Learning OKF Factory creates and does not create.
tags: [factory, overview]
timestamp: 2026-06-30T00:00:00-07:00
---
# Purpose

This factory produces a **Course Learning OKF**: a course-specific, stateful OKF bundle designed for short exam preparation. The default target is seven days, one hour per day, and a pass-level outcome around 60 points.

The factory itself is reusable. It should not become a course notebook. Each course must be generated as a separate OKF bundle.

# Default Scenario

```text
Input: course name + weak baseline + exam soon + 60 minutes/day
Output: a course-specific OKF that can teach, test, remember, resume, and adapt
```

# Input

Minimum input:

```yaml
course_name: ""
baseline: "zero"
daily_minutes: 60
target_score: 60
days_available: 7
exam_format: "unknown"
course_type: "concept_heavy"
materials_available: "none"
materials: []
constraints: []
```

# Output

A generated course OKF with:

* course mission and constraints
* course map
* source list with confidence and gaps
* A/B/C priority map
* seven-day plan or configured-day plan
* daily work packages
* initialized state files
* session records
* recall deck
* misconception tracker
* score history
* next action
* plan change log
* quiz files
* final review pack
* validation result

# MVP Materialization Helper

`tools/materialize_course_okf.py` can create the required Course Learning OKF file tree from a normalized input, initialize state, run structural validation, run a content quality gate, and make one deterministic repair attempt when a local course seed exists. The helper keeps the MVP deterministic: unknown courses are not given a fake pass; they remain quality-failed until a factory agent or human fills course-specific explanations from materials and playbooks.

# Operating Principle

The generated course OKF must be **stateful**. Each session reads the state first, runs learning work, writes evidence, and adapts the remaining plan.

# Non-Goals

This factory does not promise full subject mastery, high-score coaching, or long-term problem-set training. It is optimized for short-term, pass-level preparation in concept-heavy courses.
