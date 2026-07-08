---
type: Course Map
title: 美国专利法概念地图、依赖关系和考试题型。
description: ['course-map', 'us-patent-law']
tags: [us-patent-law, course-okf]
timestamp: 2026-07-07T20:04:08+00:00
---

# Course Map

## 核心主线

```text
专利制度目的
→ 专利类型与申请流程
→ patentability gates: §101 / §102 / §103 / §112
→ claims 与 claim construction
→ infringement
→ remedies
→ PTAB / modern updates
```

## Likely Units

| Unit | Exam value | Source evidence | Notes |
|---|---:|---|---|
| Patent bargain 与专利类型 | high | 35 U.S.C.; USPTO patent basics | 建立“专利不是实施权，而是排他权”的入口。 |
| USPTO 申请流程 | medium-high | USPTO patent process overview; MPEP | 只需理解流程，不训练执业细节。 |
| §101 patent eligible subject matter | very high | 35 U.S.C. §101; MPEP §2106; Supreme Court cases | 软件、诊断方法、自然产品、AI 相关问题都从这里进入。 |
| §102 novelty / prior art | very high | 35 U.S.C. §102; MPEP §2131 | anticipation、printed publication、on-sale 等是基础。 |
| §103 nonobviousness | very high | 35 U.S.C. §103; MPEP §2141; Graham; KSR | 最需要训练“为什么显而易见”。 |
| §112 disclosure and claims | very high | 35 U.S.C. §112; MPEP §§2163, 2164, 2173 | written description、enablement、definiteness 与 claims 绑定。 |
| Claim construction | high | Markman; Phillips | 有效性和侵权判断都离不开 claim meaning。 |
| Infringement | high | 35 U.S.C. §271; case law | direct、induced、contributory、equivalents 的基础区分。 |
| Remedies | medium-high | 35 U.S.C. §§284–285; eBay; Halo | injunction 不再自动；enhanced damages 需要 willfulness 语境。 |
| PTAB / IPR / PGR | medium | 35 U.S.C. §§311–329; USPTO PTAB materials | 作为现代专利制度图谱的一部分。 |
| AI 与 design patent 更新 | medium | USPTO / Federal Register | 训练“如何查新规则”，不作深度政策课。 |

## Dependency Map

```text
patent right boundary
→ patent type and application posture
→ claim as legal boundary
→ patentability analysis
   → §101 eligibility
   → §102 novelty
   → §103 nonobviousness
   → §112 disclosure / claiming
→ claim construction
→ infringement analysis
→ remedies and post-grant review
```

## 易混点

| Confusion | Correction |
|---|---|
| “专利给我实施发明的权利” | 专利主要是 exclude others 的权利；实施还可能受他人专利、监管或合同限制。 |
| “新就是可专利” | 新颖性只是 §102；还要过 §101、§103、§112。 |
| “MPEP 就是法院规则” | MPEP 是 USPTO 审查资料；法院判例和法律原文要分开。 |
| “claim 越宽越好” | 太宽可能缺乏 written description / enablement 支持，也更容易遇到 prior art。 |
| “obviousness 就是主观觉得简单” | 要站在 PHOSITA 和 prior art 的基础上分析，不能事后诸葛亮。 |
| “AI 参与就不能申请专利” | 需要区分 eligibility、inventorship、human contribution、disclosure 等问题。 |

## Likely Exam Patterns

1. 名词解释：prior art、PHOSITA、enablement、claim construction、IPR。
2. 比较题：novelty vs nonobviousness；written description vs enablement；utility vs design patent。
3. 简答题：解释 Alice/Mayo、Graham factors、KSR 的意义。
4. 事实适用题：给一个发明事实，依次检查 §101 / §102 / §103 / §112。
5. 误用识别题：指出一段 flawed answer 把哪两个概念混了。

## Assumptions

- 学习者用中文学习，关键术语保留英文。
- 无学校课件和历史题库。
- 目标是快速建立稳定概念地图和基础答题能力，不是执业级训练。

## Darwin R1 operational layers

| Layer | File | Purpose |
|---|---|---|
| Source authority | resources/source-hierarchy.md | 避免把 statute、case、MPEP、casebook 混同。 |
| Update control | resources/update-tracker.md | 处理 MPEP cutoff、AI、SME、fees、design 等动态资料。 |
| Case reasoning | case-cards/core-case-cards.md | 把案名变成可用规则边界。 |
| Practice labs | practice/prior-art-search-lab.md; practice/flawed-answer-drills.md | 把 §102 / §103 / §112 / infringement 训练成事实适用。 |
| Synthetic state tests | learning-records/dry-run-day-2-synthetic.md; learning-records/dry-run-day-4-synthetic.md | 验证常见错误能写入 state 并触发下一步修复。 |

## Darwin R2 added support nodes

The following support nodes were added after zero-baseline testing:

```text
Day 2 §101
  -> alice-mayo-worked-example
  -> day-2-specific-feedback

Day 4 §103
  -> phosita-motivation-fact-bank
  -> day-4-specific-feedback

Day 5 §112
  -> broad-claim-drills
  -> day-5-specific-feedback

Final review
  -> gate-selection-checklist
```

These nodes repair observed fact-application weaknesses without changing the main seven-day sequence.
