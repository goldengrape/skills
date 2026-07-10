# ADD：Patent OA Response OKF Bundle（通用版）

## 1. 目标

本 ADD 用于约束 OA 答复 bundle 的功能分解和设计参数，使流程保持单向依赖，避免事实读取、策略判断、胜率评估和最终文本生成互相污染。

通用版不绑定任何具体案件、申请人、技术领域或测试样例。所有失败模式均以抽象规则表达。

## 2. FR / DP 分解

| FR | 功能需求 | DP | 设计参数 |
|---|---|---|---|
| FR-01 | 确认案卷完整性、法域、程序阶段和输出边界。 | DP-01 | `playbooks/document-intake.md` + `templates/case-file-checklist.md` |
| FR-02 | 建立原申请事实底稿。 | DP-02 | `skills/patent-file-reading.md` + `templates/invention-analysis.md` |
| FR-03 | 拆解 OA 拒绝理由、审查员逻辑和正文补充引证。 | DP-03 | `skills/patent-oa-analysis.md` + `templates/oa-analysis.md` |
| FR-04 | 建立权利要求要素与对比文件 / 补充证据的映射。 | DP-04 | `skills/patent-claim-chart.md` + `templates/claim-chart.md` |
| FR-05 | 形成当前答复候选或审稿结论。 | DP-05 | `skills/patent-response-review.md` 或 `skills/patent-draft-response.md` |
| FR-06 | 从审查员视角进行强反驳。 | DP-06 | `skills/patent-examiner-simulation.md` + `templates/examiner-simulation.md` |
| FR-07 | 独立输出授权概率区间和风险条件。 | DP-07 | `skills/patent-win-rate.md` + `templates/win-rate-evaluation.md` |
| FR-08 | 生成 A/B 修订方案。 | DP-08 | `skills/patent-revision-variants.md` + `templates/ab-revision-plan.md` |
| FR-09 | 对 A/B 方案二次模拟、二次评估并选择推荐方案。 | DP-09 | 总控流程中的二次模拟 / 二次胜率评估步骤 |
| FR-10 | 执行领域质量守门，决定继续、回退或降级输出。 | DP-10 | `policies/domain-quality-gates.md` + `templates/domain-quality-check.md` |
| FR-11 | 生成最终答复草稿或降级为审稿与修订建议。 | DP-11 | `skills/patent-final-response.md` + `templates/final-response.md` |

## 3. 设计矩阵

顺序采用 FR-01 → FR-11。`X` 表示当前 FR 依赖对应 DP。

| FR \ DP | DP01 | DP02 | DP03 | DP04 | DP05 | DP06 | DP07 | DP08 | DP09 | DP10 | DP11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FR-01 | X |  |  |  |  |  |  |  |  |  |  |
| FR-02 | X | X |  |  |  |  |  |  |  |  |  |
| FR-03 | X | X | X |  |  |  |  |  |  |  |  |
| FR-04 | X | X | X | X |  |  |  |  |  |  |  |
| FR-05 | X | X | X | X | X |  |  |  |  |  |  |
| FR-06 | X | X | X | X | X | X |  |  |  |  |  |
| FR-07 | X | X | X | X | X | X | X |  |  |  |  |
| FR-08 | X | X | X | X | X | X | X | X |  |  |  |
| FR-09 | X | X | X | X | X | X | X | X | X |  |  |
| FR-10 | X | X | X | X | X | X | X | X | X | X |  |
| FR-11 | X | X | X | X | X | X | X | X | X | X | X |

结论：矩阵为下三角。后续步骤可以读取前序产物，但前序步骤不得读取后续判断。

## 4. 关键解耦规则

1. 文件读取只建立事实底稿，不生成最终答复策略。
2. OA 拆解只描述审查员逻辑和证据使用，不替代 claim chart。
3. Claim chart 只做证据映射，不直接给胜率。
4. 当前答复候选不得自行给最终概率。
5. 审查员模拟只做反驳强度排序，不输出授权概率。
6. 胜率评估是唯一概率出口，且只能输出区间和条件。
7. A/B 修订只生成候选方案，不自行宣称胜率提升。
8. 最终答复只整理已通过质量守门的方案。
9. Hard gate 触发时必须回退或降级输出，不得绕过。

## 5. 通用失败模式

本 bundle 明确防护以下通用失败模式：

| 风险 | 防护设计 |
|---|---|
| 审查员补充证据未提供，却继续写确定性答复。 | HG-01、HG-03、证据缺件规则、最终降级输出。 |
| 只读取 OA 首页证据表，遗漏正文补充引证。 | HG-11、正文补充引证扫描规则。 |
| 后续 OA 中机械复用已被审查员反驳的论点。 | HG-10、后续 OA 强风险检查。 |
| 从属权利要求已有具体证据，但答复只笼统依附独权。 | HG-12、从属项具体证据回应表。 |
| 数学式、附图、表格或单位抽取失败。 | HG-13、复杂内容抽取检查。 |
| 修改特征没有原申请支持。 | HG-02、修改支持表。 |
| 最终稿新增未经评估的核心论点。 | HG-09、最终文本守门。 |

## 6. 通用版边界

- 本 ADD 不包含真实案件信息。
- 本 ADD 不包含真实测试报告或真实回归样例。
- 所有测试均以合成场景或抽象失败模式描述。
- 若用户需要内部回归样例，应另建私有测试包，不应放入通用 bundle。
