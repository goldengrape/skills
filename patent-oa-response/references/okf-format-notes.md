---
type: Reference
title: OKF 格式说明
description: "说明本 bundle 如何遵循 Open Knowledge Format v0.1 的 Markdown + YAML frontmatter 约定。"
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
tags:
  - OKF
  - format
  - reference
timestamp: "2026-07-09T00:00:00-07:00"
---


# 本 bundle 采用的 OKF 规则

本 bundle 使用普通目录树组织知识文件。除 `index.md` 和 `log.md` 外，每个 `.md` 文件都是一个 concept document，包含 YAML frontmatter。

# Frontmatter 字段

每个 concept document 至少包含：

```yaml
type: <概念类型>
```

并尽量包含：

```yaml
title: <标题>
description: <一句话说明>
tags: [<标签>]
timestamp: <ISO 8601 时间>
```

# 本 bundle 的 concept 类型

- `Agent Skill`：可被代理执行的技能说明；
- `Playbook`：端到端或阶段性流程；
- `Template`：阶段输出模板；
- `Policy`：约束规则；
- `Reference`：外部来源或设计依据；
- `Usage Guide`：使用说明。

# Citations

- OKF repository: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
- OKF SPEC: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
