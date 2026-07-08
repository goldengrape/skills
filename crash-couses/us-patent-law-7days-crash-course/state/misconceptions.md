---
type: Misconception Tracker
title: 误区记录。
description: ['state', 'misconceptions']
tags: [us-patent-law, course-okf]
timestamp: 2026-07-07T20:04:08+00:00
---

# Misconceptions

| ID | Misconception | Severity | Evidence | Repair action | Retest |
|---|---|---|---|---|---|
| M001 | Patent means guaranteed right to practice invention. | high | initial risk | Day 1 contrast with right to exclude and freedom to operate | new example after Day 1 |
| M002 | Novelty alone means patentable. | high | initial risk | Four-gate patentability funnel | Day 3 or Day 5 mixed path |
| M003 | MPEP and Supreme Court cases have the same legal role. | medium-high | initial risk | Source hierarchy exercise | Day 2 feedback |
| M004 | Obviousness can be answered by personal intuition. | high | initial risk | PHOSITA + prior art + reason to combine | Day 4 flawed-answer review |
| M005 | Written description and enablement are identical. | high | initial risk | Side-by-side §112 comparison | Day 5 transfer question |

## Darwin R1 seeded high-risk misconceptions

| Misconception | Priority | Detection prompt | Repair route | Status |
|---|---|---|---|---|
| Uses novelty to answer §101 eligibility | high | “This software is eligible because no prior art discloses it.” | `practice/flawed-answer-drills.md` Drill 1; Day 2 retest | seeded |
| Combines multiple references and calls it anticipation | high | “Reference A+B disclose everything, so §102 anticipation.” | Day 3 element chart | seeded |
| Says obvious because invention feels simple | high | “Sensor + algorithm is simple, so obvious.” | Day 4 Graham/KSR table | seeded |
| Treats one example as support for all genus claims | high | “One working example supports all variants.” | Day 5 scope matching drill | seeded |
| Skips claim construction before infringement | medium-high | “Product is similar, so it infringes.” | Day 6 claim term drill | seeded |

## Darwin R2 repair targets added after zero-baseline simulation

| Misconception | Priority | Evidence from simulation | New repair route | Retest |
|---|---|---|---|---|
| §101 answered by “new and useful” or “no prior art” | high | Day 2 13/25; final still fragile | `practice/alice-mayo-worked-example.md`; Day 2 calibration prompt | Day 2 transfer mini-drill + final Part C |
| KSR used as shortcut without PHOSITA facts | high | Day 4 15/25 | `practice/phosita-motivation-fact-bank.md`; Day 4 feedback samples | Day 4 mini-drill + final Part C |
| One example treated as support for all broad claims | high | Day 5 partial repair; final §112 thin | `practice/section-112-broad-claim-drills.md` | Drill A/B + final Part C |
| Generic feedback does not diagnose doctrine-specific error | medium-high | Simulation review recommendation | `teacher/feedback-samples/day-2/4/5` | Teacher feedback audit |
