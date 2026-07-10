---
type: Agent Skill
title: patent-oa-response
description: "用户调用的总控流程：按单向顺序组织专利审查意见答复的读取、拆解、映射、候选、模拟、评估、修订和最终文本。"
tags:
  - patent
  - office-action
  - orchestrator
  - user-invoked
timestamp: "2026-07-09T00:00:00-07:00"
invocation: user-invoked
---

# 作用

当用户要求“分析审查意见”“审查答通”“起草答复”“模拟审查员”“评估胜率”或“生成 A/B 答复方案”时，使用此 skill 作为总控流程。

# 总原则

- 先建立事实底稿，再做策略判断。
- 所有创造性判断都要回到：区别特征、技术效果、实际解决的技术问题、现有技术是否给出技术启示。
- 答复策略必须同时评估授权概率、保护范围、后续复审价值和授权后稳定性。
- 执行前必须确认法域和程序阶段；未确认时只能输出通用限制，不使用具体程序路径作为最终建议。
- 若用户没有明确策略偏好，默认采用“授权优先，但避免无必要牺牲保护范围”。
- 胜率概率只能由 [patent-win-rate](patent-win-rate.md) 输出；审稿、起草和修订步骤不得自行给概率区间。

# 单向流程

## 1. 检查案卷完整性

调用 [document-intake](../playbooks/document-intake.md)。

完成标准：已列出已提供文件、缺失文件、审查员证据清单、法域/程序阶段、可继续分析的限制条件。若审查员用于核心拒绝理由的补充引证文件缺失，触发 🔴 STOP / CHECKPOINT，不得输出可提交最终稿。

## 2. 建立原申请事实底稿

调用 [patent-file-reading](patent-file-reading.md)。

完成标准：已输出原发明构思、权利要求层级、说明书支持点、可修改特征池、核心技术效果。

## 3. 拆解审查意见

调用 [patent-oa-analysis](patent-oa-analysis.md)。

完成标准：审查员每个拒绝理由、主对比文件、组合文件、区别特征、技术问题和公知常识认定已被拆解。

## 4. 制作对比文件映射表

调用 [patent-claim-chart](patent-claim-chart.md)。

完成标准：每个独立权利要求要素均已映射到审查意见、主对比文件、组合文件和其他引证文件；未公开、扩张解释和可承认内容均已标注。

## 5. 形成当前答复候选

- 如果已有代理答复稿，调用 [patent-response-review](patent-response-review.md)。
- 如果没有答复稿，调用 [patent-draft-response](patent-draft-response.md)。

完成标准：已形成统一结构的“当前答复候选”，且风险点已明确。此处不得输出授权概率区间。

随后按 [领域质量守门规则](../policies/domain-quality-gates.md) 检查 HG-01 到 HG-13；触发时回到对应上游步骤。

## 6. 模拟审查员

调用 [patent-examiner-simulation](patent-examiner-simulation.md)。

完成标准：审查员可能接受的修改、可能维持的拒绝理由、可能新增的组合路径和对我方每个核心论点的反驳均已列出。

## 7. 独立评估胜率

调用 [patent-win-rate](patent-win-rate.md)。

完成标准：已给出授权概率区间、最可能结果、失败路径、保护范围损失、复审价值和授权后稳定性风险。

随后执行领域质量守门，重点检查 HG-01、HG-02、HG-05、HG-06、HG-07、HG-08、HG-10、HG-11、HG-12、HG-13。

## 8. 生成 A/B 修订方案

调用 [patent-revision-variants](patent-revision-variants.md)。

完成标准：至少生成两组实质不同的方案：授权优先方案 A 和范围平衡方案 B。每组均包括权利要求修改、意见陈述主线、修改依据、风险变化和保护范围影响。此处不得输出最终概率区间。

## 9. 二次模拟、二次评估和选择

对 A/B 分别再次调用：

1. [patent-examiner-simulation](patent-examiner-simulation.md)；
2. [patent-win-rate](patent-win-rate.md)。

然后先执行领域质量守门，确认 A/B 没有触发 HG-02、HG-07、HG-08、HG-09、HG-10、HG-11、HG-12、HG-13，再根据二次评估选择：

- 推荐主提交方案；
- 备选方案；
- 不推荐方案；
- 是否建议电话沟通；
- 是否建议预备复审论点。

完成标准：二次胜率来自模拟和评估步骤，而不是 A/B 生成步骤。

## 10. 生成最终文本

如用户要求完整答复意见，调用 [patent-final-response](patent-final-response.md)。

完成标准：最终文本可交由专利代理人核对；不得新增未经前面步骤评估的论点或限定；必须附领域质量守门结果。若仍有审查员证据缺件、正文补充引证未扫描、从属项具体证据未回应、关键公式/附图/表格未核对、已反驳论点复用、方法权利要求未单独回应，则只输出“审稿与修订建议”或“供代理人核对的草稿”。

# 🔴 STOP / CHECKPOINT

在最终文本前，若领域质量守门任一 hard gate 触发，停止生成“可提交版本”。可继续输出的内容限于：缺件清单、审稿报告、A/B 修订建议、供代理人核对的草稿。

# 停止条件

见 [迭代停止规则](../policies/iteration-stop-rules.md)。默认最多两轮迭代。

# 输出格式

使用以下标题：

1. 案卷完整性
2. 原申请事实底稿
3. 审查意见拆解
4. 对比文件映射
5. 当前答复候选
6. 模拟审查员意见
7. 胜率评估
8. A/B 修订方案
9. 二次模拟与最终建议
10. 领域质量守门
11. 最终答复文本，如用户要求
