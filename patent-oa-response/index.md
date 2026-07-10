# Patent OA Response Skill Bundle

通用专利 OA 答复 OKF bundle。它不绑定任何具体案号、客户、申请人、技术领域或历史测试案例。

* [URD](docs/URD.md) - 用户需求、范围、约束和验收标准。
* [ADD](docs/ADD.md) - FR/DP 分解、矩阵检查和重构记录。
* [TRACE](docs/TRACE.md) - URD → ADD → OKF 文件追踪。
* [领域研究](docs/domain-research.md) - Darwin 领域评分依据和证据空白。
* [领域评分原则](docs/domain-rubric.md) - OA 答复质量维度、权重和 hard gates。
* [领域评分质量评估](docs/domain-rubric-evaluation.md) - rubric 自身的 RQ1–RQ9 质量检查。
* [通用版发布报告](docs/generic-release-report.md) - 从内部优化版转为通用发行版的修改记录。
* [隐私检查报告](docs/privacy-audit.md) - 通用版发布前的脱敏检查记录。
* [使用说明](usage.md) - 如何把这套 OKF bundle 用于专利审查意见答复。
* [总控流程](skills/patent-oa-response.md) - 用户调用的端到端专利答复流程。
* [Skills](skills/index.md) - 可组合的子 skill。
* [Playbooks](playbooks/index.md) - 端到端流程、文件接收和迭代规则。
* [Templates](templates/index.md) - 每个阶段的输出模板。
* [Policies](policies/index.md) - 证据、循环、法律风险、领域质量守门和输出边界。
* [References](references/index.md) - OKF 和 skill 设计原则的来源说明。
* [回归测试套件](tests/regression-suite.md) - 合成场景和结构检查要求。

## 通用版说明

本版本只保留从测试和评估中抽象出的通用失败模式，例如：

- 审查员正文补充引证遗漏；
- 补充证据缺件；
- 已被审查员反驳的论点被机械复用；
- 从属权利要求已有具体证据但未逐项回应；
- 数学式、附图、表格等复杂内容抽取失败；
- 最终答复在 hard gate 触发时仍输出可提交稿。

本版本不包含真实案号、申请人名称、真实文件名、真实申请号、真实测试报告或真实回归样例。
