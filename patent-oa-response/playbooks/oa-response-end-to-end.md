---
type: Playbook
title: 端到端专利答复流程
description: "从案卷读取到最终答复意见的单向执行流程。"
tags:
  - patent
  - office-action
  - workflow
timestamp: "2026-07-09T00:00:00-07:00"
---

# 流程图

```text
文件接收
  ↓
原申请事实底稿
  ↓
审查意见拆解
  ↓
对比文件 claim chart
  ↓
当前答复候选：已有稿审查 / 无稿起草
  ↓
模拟审查员
  ↓
胜率评估
  ↓
A/B 修订方案
  ↓
A/B 二次模拟
  ↓
A/B 二次胜率评估
  ↓
最终建议
  ↓
领域质量守门
  ↓
最终答复草稿
```

# 阶段输出

| 阶段 | 输出 | 使用的 skill / playbook |
|---|---|---|
| 文件接收 | 文件清单和限制 | document-intake |
| 原申请事实底稿 | 原发明和可修改特征池 | patent-file-reading |
| 审查意见拆解 | 拒绝理由表和必须回应的问题 | patent-oa-analysis |
| 对比文件分析 | claim chart | patent-claim-chart |
| 答复候选 | 审稿后的当前候选或初版候选 | patent-response-review / patent-draft-response |
| 对抗测试 | 模拟审查员意见 | patent-examiner-simulation |
| 评估 | 胜率区间 | patent-win-rate |
| 修订 | A/B 方案，不含最终概率 | patent-revision-variants |
| 二次评估 | A/B 概率区间和最终建议 | patent-examiner-simulation + patent-win-rate |
| 质量守门 | hard gate 通过/触发/回退入口 | domain-quality-gates |
| 最终文本 | 可人工核对的答复草稿 | patent-final-response |

# 最终建议格式

最终建议必须说明：

- 推荐提交哪个方案；
- 为什么不推荐另一个方案；
- 是否建议电话沟通；
- 是否建议预留复审论点；
- 提交前需要人工核对的事项；
- 领域质量守门是否通过。


# 后续 OA 强化流程

若本次是第二次或更后续 OA，在“审查意见拆解”和“当前答复候选”之间增加三个强制检查：

1. 正文补充引证扫描；
2. 前次论点被反驳后的复用检查；
3. 从属项具体证据回应检查。

这三个检查没有通过时，不进入最终答复草稿，只输出审稿与修订建议。
