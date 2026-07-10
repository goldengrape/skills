# TRACE：URD → ADD → OKF 文件追踪（通用版）

## 1. 追踪原则

本文件记录用户需求、设计分解和实际 OKF 文件之间的对应关系。通用版只追踪抽象能力，不追踪任何真实案件、客户、申请号、案号或历史测试样例。

## 2. 主流程追踪

| URD / FR | 目标 | 主要文件 |
|---|---|---|
| 案卷完整性和法域确认 | 防止缺文件、错法域和错程序阶段。 | `playbooks/document-intake.md`, `templates/case-file-checklist.md`, `policies/legal-safety-boundaries.md` |
| 原申请事实底稿 | 提取权利要求结构、说明书支持、技术效果和可修改特征池。 | `skills/patent-file-reading.md`, `templates/invention-analysis.md` |
| OA 拆解 | 拆出拒绝理由、审查员组合逻辑、正文补充引证和已反驳论点。 | `skills/patent-oa-analysis.md`, `templates/oa-analysis.md` |
| Claim chart | 逐项映射权利要求要素、证据位置、原文摘录和置信度。 | `skills/patent-claim-chart.md`, `templates/claim-chart.md` |
| 当前答复候选 | 审稿或起草当前候选方案，但不输出最终概率。 | `skills/patent-response-review.md`, `skills/patent-draft-response.md` |
| 审查员模拟 | 从审查员角度强反驳，不输出概率。 | `skills/patent-examiner-simulation.md`, `templates/examiner-simulation.md` |
| 胜率评估 | 唯一概率出口，输出区间、条件和封顶理由。 | `skills/patent-win-rate.md`, `templates/win-rate-evaluation.md` |
| A/B 修订 | 形成实质不同的修订方案。 | `skills/patent-revision-variants.md`, `templates/ab-revision-plan.md` |
| 领域质量守门 | 检查 HG-01 到 HG-13，决定通过、回退或降级输出。 | `policies/domain-quality-gates.md`, `templates/domain-quality-check.md` |
| 最终答复 | 只整理已通过守门的方案；未通过时输出审稿与修订建议。 | `skills/patent-final-response.md`, `templates/final-response.md` |

## 3. 领域评分追踪

| 文件 | 作用 |
|---|---|
| `docs/domain-research.md` | 记录领域评分依据、风险假设和证据空白。 |
| `docs/domain-rubric.md` | 定义 OA 答复质量评分维度和 hard gates。 |
| `docs/domain-rubric-evaluation.md` | 对领域评分标准自身进行 RQ1–RQ9 复核。 |
| `docs/domain-test-prompts.json` | 提供合成测试场景，不包含真实案件信息。 |
| `tests/regression-suite.md` | 定义发布前结构检查和通用风险场景回归。 |
| `docs/privacy-audit.md` | 记录通用版脱敏检查。 |

## 4. Hard Gate 追踪

| 范围 | 文件 |
|---|---|
| HG-01 到 HG-13 的定义 | `policies/domain-quality-gates.md`, `docs/domain-rubric.md` |
| HG-01 到 HG-13 的执行模板 | `templates/domain-quality-check.md` |
| 最终输出前的强制检查 | `skills/patent-final-response.md`, `templates/final-response.md` |
| 总控流程中的中间检查点 | `skills/patent-oa-response.md` |

## 5. 隐私追踪

通用版不得包含：

- 真实客户、申请人、发明人或代理机构名称；
- 真实案号、申请号、审查意见日期、内部文件名；
- 真实对比文件公开号或公告号；
- 真实案件技术事实；
- 真实测试报告、截图或回归样例文件。

若后续要保留真实测试材料，应放在私有测试包中，并与通用 bundle 分离。
