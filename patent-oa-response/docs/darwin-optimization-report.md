# Darwin Optimization Report：OA Bundle v0.2

## 1. 输入

优化对象：`patent-oa-response-okf-refactored`。

优化方法：按 Darwin skill 的流程执行 dry-run 优化：领域研究 → 领域评分标准 → rubric 质量评估 → 主要短板修复 → 回归检查。

## 2. 基线诊断

| 项 | 观察 | 风险 |
|---|---|---|
| 主流程 | 已按 ADD 重构为单向下三角流程。 | 流程方向可接受。 |
| 领域评分 | 尚未写入 bundle 文件。 | Darwin 后续无法复用领域评分原则。 |
| hard gate 执行 | 证据规则和法律边界存在，但没有最终输出前的统一守门动作。 | 高风险错误可能只停留在提醒层。 |
| 胜率唯一出口 | 大体清楚，但审查员模拟仍允许“概率排序”。 | 与 win-rate 唯一概率出口轻微冲突。 |
| 法域处理 | URD 保留法域开放问题，但 intake 未要求确认法域。 | 具体程序路径可能错配。 |

## 3. 本轮优化动作

| ID | 修改 | 文件 |
|---|---|---|
| OPT-001 | 新增领域研究、领域评分原则、测试 prompt、rubric 质量评估和元数据。 | `docs/domain-*` |
| OPT-002 | 新增领域质量守门规则和模板。 | `policies/domain-quality-gates.md`, `templates/domain-quality-check.md` |
| OPT-003 | 总控流程加入质量守门检查点。 | `skills/patent-oa-response.md` |
| OPT-004 | 最终答复 skill 要求读取质量守门结果。 | `skills/patent-final-response.md` |
| OPT-005 | 审查员模拟取消概率排序，改为定性排序。 | `skills/patent-examiner-simulation.md` |
| OPT-006 | 胜率评估禁止单点数字，默认封顶到 85%。 | `skills/patent-win-rate.md` |
| OPT-007 | 文件接收和法律边界加入法域/程序阶段确认。 | `playbooks/document-intake.md`, `policies/legal-safety-boundaries.md` |
| OPT-008 | 更新 URD、ADD、TRACE、usage、index 和目录索引。 | `docs/*.md`, `usage.md`, `index.md` |

## 4. 评分变化（dry-run）

| 评分 | 优化前 | 优化后 | 说明 |
|---|---:|---:|---|
| 公共 9 维评分 | 82 | 88 | 增强失败模式、检查点、反例和可执行性。 |
| 领域评分 | 78 | 88 | 增加领域 rubric、hard gates、法域检查和最终质量守门。 |
| 综合评分 | 80 | 88 | 采用 dry-run 判断，未使用真实 OA 样本 full_test。 |

## 5. 保留理由

本轮优化应保留，理由：

1. 没有改变已满足下三角矩阵的主流程；
2. 新增质量守门作为后置检查，不反向污染事实读取、OA 拆解和方案生成；
3. 修复了概率输出口径的残留冲突；
4. 领域评分原则和测试 prompt 已写入 bundle，后续可复用。

## 6. 剩余限制

- 本轮没有真实 OA 样本 full_test；
- 法域只做到确认和错配防护，尚未拆成 CN/US/EP 三套完整流程；
- 胜率区间仍是辅助性风险表达，不能替代代理师判断。
