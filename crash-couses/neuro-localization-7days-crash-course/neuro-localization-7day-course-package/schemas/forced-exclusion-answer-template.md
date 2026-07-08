---
type: Schema
title: Forced Exclusion Answer Template
description: Student-facing answer template added after low-baseline simulation showed repeated omission of exclusion reasoning.
tags: [schema, answer-template, exclusion]
timestamp: 2026-07-07T11:47:00-07:00
---

# Forced Exclusion Answer Template

Use this for every practice case and quiz case.

```text
1. 定位结论：
2. 支持证据 A：
3. 支持证据 B：
4. 我排除的第一个错误定位：
5. 排除理由：
6. 还要补充的一个查体/病史：
```

## Minimum Passing Form

```yaml
must_have_localization_level: true
must_have_two_supporting_evidence_items: true
must_have_one_exclusion: true
if_exclusion_missing: max_score_fraction = 0.70
```
