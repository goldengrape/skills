---
type: Resource Registry
title: 课程资源登记
description: 登记内容来源、优先级、资料缺口和 C 类扩展材料规则。
tags: [resources, source-aware]
timestamp: 2026-07-04T00:00:00-07:00
---


# Resources

## 已使用资源

| 资源 | 类型 | 用途 | 优先级 | 备注 |
|---|---|---|---|---|
| crash-course-learning-okf-factory-darwin-round7 | OKF 工厂方法 | 课程包结构、状态文件、测验机制、可见性规则 | primary | 用作方法来源，不作为哲学内容来源。 |
| 用户提供的课程需求 | 课程说明 | 定义 7 天骨架、A/B/C 范围、学习目标、AI 边界 | primary | 本课程包内容围绕该需求生成。 |
| 标准哲学课程常识 | 背景知识 | 梳理笛卡尔、休谟、康德、Gettier、波普尔、奎因、库恩 | secondary | 用于自学理解；仍需在教学中保持概念边界。 |
| 用户上传 epub《休谟、康德与 DeepSeek：从经验归纳到可检验推理》 | C 类案例库 | 设计 AI 迁移题，帮助检查 L7 迁移与边界感 | optional_C | 已接入为案例索引：`assets/cases/deepseek-epub-case-library.md`。不作为主教材，不作为哲学解释依据。 |

## 建议后续补充资源

| 资源类型 | 推荐用途 | 是否必需 |
|---|---|---|
| 认识论导论教材章节 | 细化 JTB、怀疑论、Gettier、证成理论 | 非必需，但有助于延伸。 |
| 科学哲学导论教材章节 | 细化归纳主义、证伪主义、奎因、库恩 | 非必需，但有助于 Day 5-6。 |
| 原典短选段 | 用于 Day 7 复盘或 L7 迁移 | 可选。 |

## epub 接入状态

用户上传的 epub 已接入，但只提取为 C 类案例主题，未把全文复制进课程包。课程包中的处理方式是：

- 在 `assets/cases/deepseek-epub-case-library.md` 中登记章节索引和可用案例主题。
- 在 Day 7 quiz 中加入 C 类迁移题。
- 在教师侧答案和评分规则中加入边界要求。
- 在 `state/interest-ledger.md` 中把该资源状态从 `source_gap` 改为 `active_C_case_library`。

## AI 材料使用规则

- AI 案例只用于检验迁移能力。
- 不要求掌握 DeepSeek 或其他模型的工程细节。
- 不把 AI 工程机制直接等同于休谟、康德、波普尔、奎因或库恩的哲学概念。
- 若使用 AI benchmark 案例，必须说明它是有限测试环境，不自动等于科学理论的严格证伪。
- 若使用康德类比，必须明确这只是功能结构层面的有限类比，不能说 AI 已经实现了先验范畴、统觉、意识或主体性。
