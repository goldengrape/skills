---
type: Resource Registry
title: 资料来源、可信度和 source gaps。
description: ['resources', 'sources', 'us-patent-law']
tags: [us-patent-law, course-okf]
timestamp: 2026-07-07T20:04:08+00:00
---

# Resources

## 使用原则

用户提供材料优先于公共资料。没有学校课件和历史题库时，本课程以官方资料和开源 casebook 建立基础结构，并记录 source gaps。

## 资源注册表

| ID | Type | Title | Link / Path | Priority | Confidence | Used for | Notes |
|---|---|---|---|---|---|---|---|
| R1 | statute | 35 U.S.C. Title 35 — Patents | https://uscode.house.gov/view.xhtml?edition=prelim&path=%2Fprelim%40title35 | primary | high | §101, §102, §103, §112, §271, §284, §311 等 | 法律原文入口。 |
| R2 | regulation | 37 C.F.R. Title 37 | https://www.ecfr.gov/current/title-37 | primary | high | USPTO 程序、PTAB rules | eCFR 为动态入口，使用时核对日期。 |
| R3 | USPTO manual | MPEP, Ninth Edition, Rev. 01.2024 | https://www.uspto.gov/web/offices/pac/mpep/index.html | primary | high | 审查政策、patentability | USPTO 页面说明该版本 2024 年 11 月发布，内容更新到 2024-01-31。 |
| R4 | USPTO update | MPEP subsequent publications | https://www.uspto.gov/web/offices/pac/mpep/subsequent-publications.pdf | primary | high | 2024-01-31 后政策更新 | 涉及新政策时必须核对。 |
| R5 | MPEP | MPEP Chapter 2100 — Patentability | https://www.uspto.gov/web/offices/pac/mpep/mpep-2100.pdf | primary | high | §101, §102, §103, §112 | 实体法审查核心章节。 |
| R6 | USPTO | Patent process overview | https://www.uspto.gov/patents/basics/patent-process-overview | primary | high | 申请流程 | Day 1 流程图。 |
| R7 | USPTO | Patent search | https://www.uspto.gov/patents/search | primary | high | prior art search 入门 | Day 3 / Day 4 练习入口。 |
| R8 | USPTO | Subject matter eligibility | https://www.uspto.gov/patents/laws/examination-policy/subject-matter-eligibility | primary | high | §101 | Day 2 主资料。 |
| R9 | USPTO | PTAB Trial Practice Guide | https://www.uspto.gov/patents/ptab/trial-practice-guide | primary | high | IPR / PGR / PTAB | Day 7 基础。 |
| R10 | USPTO | Fee Schedule | https://www.uspto.gov/learning-and-resources/fees-and-payment/uspto-fee-schedule | primary | high | 费用查询训练 | 不固定背金额。 |
| R11 | casebook | Masur & Ouellette, Patent Law: Cases, Problems, and Materials | https://www.patentcasebook.org/ | secondary | high | 结构、案例、问题 | 主参考教材。 |
| R12 | casebook | Patent Law: An Open-Access Casebook | https://patentlawcasebook.com/ | secondary | medium-high | 补充结构和案例 | 可替代或补充。 |
| R13 | policy | 2024 AI subject matter eligibility update | https://www.federalregister.gov/documents/2024/07/17/2024-15377/2024-guidance-update-on-patent-subject-matter-eligibility-including-on-artificial-intelligence | primary | high | AI / §101 | 近年更新入口。 |
| R14 | policy | Revised inventorship guidance for AI-assisted inventions | https://www.federalregister.gov/documents/2025/11/28/2025-21457/revised-inventorship-guidance-for-ai-assisted-inventions | primary | high | inventorship / AI | 需核对当前生效状态。 |
| R15 | policy | Design patent GUI/icon supplemental guidance | https://www.uspto.gov/ip-policy/industrial-design-policy/supplemental-guidance-examination-design-patent-applications | primary | high | design patent | Day 7 扩展。 |

## Source gaps

| Missing item | Effect | Fallback |
|---|---|---|
| 学校课件 | 无法判断具体考试偏好 | 使用通用 law school / USPTO 结构；后续上传后重排优先级。 |
| 历史题库 | 无法精确估计题型权重 | 采用 term explanation、short answer、comparison、issue spotting 混合训练。 |
| 指定教材章节 | 无法知道授课老师偏好的判例 | 以 Masur & Ouellette 和官方资料为默认。 |
| 最新费用金额 | 费用可能变化 | 训练查 USPTO fee schedule，而不是背固定金额。 |

## Darwin R1 additions

| ID | Type | Title | Link / Path | Priority | Confidence | Used for | Notes |
|---|---|---|---|---|---|---|---|
| R16 | internal control | Source hierarchy | resources/source-hierarchy.md | primary-for-course | high | 权威性分层 | 规定 statute / case / CFR / MPEP / guidance / casebook 的使用顺序。 |
| R17 | internal control | Update tracker | resources/update-tracker.md | primary-for-course | high | 资料更新 | 记录 MPEP cutoff、SME、AI、fees、design 等动态主题。 |
| R18 | internal practice | Prior Art Search Lab | practice/prior-art-search-lab.md | teaching | high | Day 3–4 实务练习 | 训练检索记录，不训练执业结论。 |
| R19 | internal practice | Flawed Answer Drills | practice/flawed-answer-drills.md | teaching | high | 误区修复 | 支持 stateful misconception repair。 |
| R20 | internal case set | Core Case Cards | case-cards/core-case-cards.md | teaching | high | 判例推理 | 修复 v1 判例卡不足。 |
