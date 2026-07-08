---
type: Teacher Runtime
title: Time Policy
description: 软时间与严格限时两种模式。
tags: [teacher, time-policy]
timestamp: 2026-06-30T00:00:00-07:00
---

# Time Policy

```yaml
default_time_policy: soft
current_time_policy: soft
configured_daily_minutes: 60
```

## Soft Policy

每天 60 分钟是计划目标。学习者表现出高兴趣或提出概念修复问题时，可以自然继续，前提是它有助于理解核心内容。结束后记录实际耗时和额外主题。

## Strict Policy

每天 60 分钟是硬上限。延伸问题简短回答，记录到 `state/interest-ledger.md`，然后回到考试主线。

## Switching Rule

只有学习者要求、考试极近、或输入明确设置 `time_policy: strict` 时，才切换到 strict。
