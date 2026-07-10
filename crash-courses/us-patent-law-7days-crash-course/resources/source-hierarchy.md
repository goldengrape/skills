---
type: Source Hierarchy
title: 美国专利法资料效力分层与使用规则
description: ['resources', 'source-hierarchy', 'us-patent-law']
tags: [us-patent-law, sources, darwin-r1]
timestamp: 2026-07-07T20:20:08Z
---

# Source Hierarchy

## 目的

本文件解决课程包 v1 的一个短板：资料虽然列出来了，但没有明确“不同资料发生冲突时如何处理”。美国专利法课程尤其需要这个文件，因为 MPEP、USPTO guidance、casebook、blog summary 的法律地位不同。

## 资料效力顺序

| Rank | Source type | Examples | Course use | Conflict rule |
|---:|---|---|---|---|
| 1 | Statute | 35 U.S.C. §§101, 102, 103, 112, 154, 271, 284, 285, 311–329 | 法律规则的起点 | 条文优先于教材概括。 |
| 2 | Binding Supreme Court / Federal Circuit precedent | Alice, Mayo, KSR, Graham, Markman, Phillips, eBay, Halo 等 | 解释条文和审查边界 | 课程必须把规则讲成判例实际支持的范围。 |
| 3 | Regulations | 37 C.F.R. Title 37 | USPTO 程序、期限、PTAB practice | 与 MPEP 冲突时，法规优先。 |
| 4 | USPTO MPEP and official guidance | MPEP Chapter 2100, SME guidance, PTAB Trial Practice Guide | 审查视角与实务操作 | 作为 USPTO 审查口径，不得说成法院最终规则。 |
| 5 | Federal Register / USPTO notices after MPEP cutoff | AI-assisted inventorship, SME updates, fee changes | 更新追踪 | 对 MPEP 截止日后的政策，必须单独标记。 |
| 6 | Open casebooks | Masur & Ouellette, open-access casebook | 教学结构、案例问题 | 可作为二级解释，不可覆盖原始法源。 |
| 7 | Secondary summaries | articles, blogs, videos | 背景补充 | 不进入 A 类主规则，除非被官方资料或判例核对。 |

## 使用动作

1. 每次讲 A 类规则时，先定位到 statute / case / MPEP 中至少一种高效力来源。
2. 每次涉及 2024-01-31 之后的 USPTO 审查政策，必须查看 `resources/update-tracker.md`。
3. 每次讲 MPEP 时，教师应提醒：MPEP 是 USPTO 审查资料，不等于法院必然采用的全部规则。
4. 每次讲案例时，必须区分：holding、reasoning、exam-use takeaway、常见误读。

## 禁止动作

| Do not | Why |
|---|---|
| 把 MPEP 当作最高法律来源 | 它是审查手册，不是国会制定的 statute，也不是法院判决。 |
| 把 casebook 的课堂问题当作法律规则 | casebook 是教学资料。 |
| 背固定费用金额 | USPTO fees 会变化，应训练查表。 |
| 把 AI 相关 guidance 写成永久不变规则 | 该领域正在更新，必须保留日期。 |
| 用“这个发明有商业价值”替代 patentability 分析 | 商业价值不等于通过 §101 / §102 / §103 / §112。 |
