# ADD — 7 天速通美国专利法课程

> Axiomatic Design Document / 设计拆分文档  
> 本文根据 `us_patent_law_course_URD.md`、`us_patent_law_reference_index.md`、crash-course-learning OKF factory，以及 vibe coding skill 的 ADD coupling retry 规则生成。  
> 本文只分析课程包的功能拆分、模块责任、依赖顺序和耦合风险；不设计 7 天每日课程安排，也不生成具体讲义。

---

## 0. Metadata

| 字段 | 内容 |
|---|---|
| project | 7 天速通美国专利法课程 |
| document_id | ADD-USPATENT-0001 |
| status | draft |
| source_urd | URD-USPATENT-0001 |
| reference_index | `us_patent_law_reference_index.md` |
| method | vibe coding skill ADD / axiomatic design / coupling retry |
| last_updated | 2026-07-07 |

---

## 1. ADD 分析结论

本课程包应采用 **decoupled / lower triangular design**，即“有依赖顺序的解耦设计”。

核心判断：

1. 美国专利法课程不能直接从“每日讲义”开始生成。必须先固定资料来源、法律效力分层、概念地图和优先级。
2. 课程运行时必须把三类内容分开：学生可见讲解、作答后反馈、教师私有判断。否则测验会失效。
3. 学习状态不是附属记录，而是后续教学调用的输入。误区、分数、辅助程度和兴趣分支都会影响下一次教学。
4. validation 不应被当成早期功能的依赖。它是最后的检查层，只读取前面产物，不反向决定前面模块的责任。
5. 由于美国专利法会更新，source registry 和 update tracker 必须作为靠前模块；后续课程地图、优先级和讲义只能调用它们，不能把二手教材当成规则来源。

设计矩阵结论：

| 项目 | 结论 |
|---|---|
| matrix type | decoupled / lower triangular |
| 是否完全对角 | 否 |
| 是否可接受 | 是 |
| 原因 | 课程生成有天然顺序：资料 → 概念地图 → 优先级 → 学习包 → 测验 → 状态 → 调整 → validation。只要后续模块只读取前序产物，不反向改写前序责任，就满足可执行的解耦设计。 |

---

## 2. Design Scope

### 2.1 本 ADD 覆盖

| ID | 范围 | 说明 |
|---|---|---|
| ADD-SCOPE-001 | 课程包功能拆分 | 从 URD 需求拆成 Functional Requirements。 |
| ADD-SCOPE-002 | 设计参数 | 为每个 FR 指定主要 Design Parameter。 |
| ADD-SCOPE-003 | 依赖矩阵 | 检查 FR 与 DP 是否形成下三角结构。 |
| ADD-SCOPE-004 | 耦合分析 | 记录重试、保留耦合、风险与保护测试。 |
| ADD-SCOPE-005 | 后续文档接口 | 为 MDD、TDD、RMD 和 TRACE 提供输入。 |

### 2.2 本 ADD 不覆盖

| ID | 非范围 | 原因 |
|---|---|---|
| ADD-OOS-001 | 具体 7 天课程表 | 应在 course-map 和 priority-map 之后生成。 |
| ADD-OOS-002 | 每日讲义正文 | 讲义属于后续 OKF package 内容。 |
| ADD-OOS-003 | 具体测验题全文 | 本文只规定测验模块和质量要求。 |
| ADD-OOS-004 | 法律意见或申请建议 | 课程是教育用途，不处理真实个案建议。 |
| ADD-OOS-005 | MDD/TDD/RMD 细节 | 后续文档再定义模块接口、测试和执行顺序。 |

---

## 3. Design Principles

| ID | Principle | Course-specific meaning |
|---|---|---|
| ADD-PRIN-001 | 单一课程目标 | 所有模块只服务“7 天速通美国专利法”，不扩展成完整知识产权课程。 |
| ADD-PRIN-002 | 权威资料先行 | 35 U.S.C.、37 C.F.R.、USPTO、判例和 casebook 必须分层记录。 |
| ADD-PRIN-003 | 先地图，后排课 | 在生成每日任务前，先生成概念地图和 A/B/C 优先级。 |
| ADD-PRIN-004 | 先测试，后结论 | 学习者作答前不得显示答案要点、评分细则或教师预判。 |
| ADD-PRIN-005 | 状态驱动后续教学 | 每次学习后更新状态；下一次教学必须先读取状态。 |
| ADD-PRIN-006 | 不伪装零耦合 | 资料、地图、优先级、计划有真实依赖，接受下三角结构，不强行拆成无意义文件。 |
| ADD-PRIN-007 | 更新可追踪 | 2024 年后的 USPTO guidance、Federal Register、费用、AI 和 design patent 更新必须有单独记录入口。 |
| ADD-PRIN-008 | 教育用途边界 | 所有真实案件、申请、侵权风险都只能作为教学假设，不给法律建议。 |

---

## 4. Functional Requirements

| ID | Source | Functional Requirement | Notes |
|---|---|---|---|
| ADD-FR-001 | URD-GOAL-001 / URD-REQ-001 / URD-REQ-008 | 定义单一课程 mission、目标用户、教育用途边界和非法律意见声明。 | 这是所有后续生成的入口。 |
| ADD-FR-002 | URD-REQ-021 至 URD-REQ-025 / URD-CON-003 / URD-CON-005 | 登记、分类和维护课程资料来源，包括 source type、优先级、可信度、更新时间和 source gaps。 | 处理法律原文、USPTO、判例、casebook 和近年更新。 |
| ADD-FR-003 | URD-SCEN-002 / URD-REQ-022 / URD-SUCC-004 | 在教学中明确区分法律条文、行政规则、USPTO 审查资料、法院判例和教材解释。 | 防止把 MPEP 当成法院规则。 |
| ADD-FR-004 | URD-TASK-001 / URD-REQ-009 至 URD-REQ-020 / URD-SUCC-001 | 生成美国专利法概念地图、主题依赖关系和常见混淆点。 | 不排课，只建立内容结构。 |
| ADD-FR-005 | URD-REQ-004 / URD-REQ-026 / URD-REQ-027 | 为概念分配 A/B/C 优先级和学习目标层级。 | A 类默认要求达到 L6。 |
| ADD-FR-006 | URD-CON-001 / URD-TASK-001 / URD-AC-012 | 生成时间感知的学习路径和每日学习包接口。 | 后续才生成具体 Day 1–Day 7。 |
| ADD-FR-007 | URD-TASK-002 / URD-REQ-005 / URD-REQ-028 / URD-REQ-029 | 生成测验、答题反馈、评分记录，并保证作答前不泄露答案要点。 | 反馈必须在作答后显示。 |
| ADD-FR-008 | URD-TASK-003 / URD-REQ-002 / URD-DATA-007 至 URD-DATA-010 | 保存和更新学习者状态，包括 session record、score history、topic ledger、recall deck、next action。 | 状态是下一次教学输入。 |
| ADD-FR-009 | URD-SCEN-005 / URD-AC-010 / URD-RISK-006 | 记录误区、执行修复、重测，并在必要时修改后续计划。 | 高严重度前置误区未修复时，不继续推进依赖主题。 |
| ADD-FR-010 | URD-REQ-030 / URD-DATA-012 | 保存学习者主动提出的深入问题，并决定何时回到主线、何时展开分支。 | 例如 AI inventorship、software patents、biotech patents。 |
| ADD-FR-011 | URD-REQ-006 / URD-VIS-002 / URD-VIS-003 | 维护教师 notebook 和教师私有运行策略，记录教学判断但不提前暴露给学习者。 | 包含不可提前显示的 rubrics 和后续策略。 |
| ADD-FR-012 | URD-AC-001 至 URD-AC-012 / URD-SUCC-006 | 对课程包执行结构、内容质量、教学运行质量和 visibility-safe 检查。 | validation 是最后读取前序产物的检查层。 |

---

## 5. Design Parameters

| ID | Satisfies FR | Design Parameter | Rationale |
|---|---|---|---|
| ADD-DP-001 | ADD-FR-001 | `mission.md` + course intake summary + legal-use boundary | 把课程目标、目标用户、非法律意见、范围和非范围固定下来。 |
| ADD-DP-002 | ADD-FR-002 | `resources.md` + `source-gaps.md` + `recent-updates.md` | 把资料来源、优先级、更新风险和缺口集中管理。 |
| ADD-DP-003 | ADD-FR-003 | source-type boundary model | 用统一表述区分 statute、CFR、MPEP、USPTO guidance、case law、casebook。 |
| ADD-DP-004 | ADD-FR-004 | `course-map.md` + concept dependency graph + confusion map | 保存主题结构、依赖关系和常见误区。 |
| ADD-DP-005 | ADD-FR-005 | `priority-map.md` + `learning-contract/index.md` | 记录 A/B/C 分类、目标层级、A 类 L6 要求。 |
| ADD-DP-006 | ADD-FR-006 | `plan/seven-day-plan.md` + `plan/day-N.md` templates | 在优先级之后生成每日学习包。 |
| ADD-DP-007 | ADD-FR-007 | quiz package + delayed feedback + visibility policy | 区分 student prompt、answer feedback、teacher rubric。 |
| ADD-DP-008 | ADD-FR-008 | state store and update protocol | 包括 current-state、score-history、recall-deck、topic-ledger、session records、next-action。 |
| ADD-DP-009 | ADD-FR-009 | misconception repair protocol + plan-change log | 记录误区、修复动作、重测证据和计划变更。 |
| ADD-DP-010 | ADD-FR-010 | interest ledger + branch-handling rules | 保存兴趣分支，避免深入问题丢失或破坏主线。 |
| ADD-DP-011 | ADD-FR-011 | `teacher/teacher-notebook.md` + teacher runtime policy | 保存教师私有判断、评分细则和下一步教学策略。 |
| ADD-DP-012 | ADD-FR-012 | validation checklist + quality gate reports | 检查文件结构、课程内容、资料追溯、状态行为和可见性安全。 |

---

## 6. FR / DP Design Matrix

说明：`X` 表示该 DP 会影响该 FR。矩阵按执行顺序排列，目标是下三角结构。早期 FR 不依赖后续 DP；validation 位于最后，只读取前面所有产物。

| FR \ DP | DP1 Mission | DP2 Sources | DP3 Source boundary | DP4 Course map | DP5 Priority / learning | DP6 Plan | DP7 Quiz / visibility | DP8 State | DP9 Repair | DP10 Interest | DP11 Teacher runtime | DP12 Validation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FR1 Mission and legal boundary | X |  |  |  |  |  |  |  |  |  |  |  |
| FR2 Source registry and freshness | X | X |  |  |  |  |  |  |  |  |  |  |
| FR3 Source authority separation |  | X | X |  |  |  |  |  |  |  |  |  |
| FR4 Patent law concept map |  | X | X | X |  |  |  |  |  |  |  |  |
| FR5 Priority and mastery targets |  |  |  | X | X |  |  |  |  |  |  |  |
| FR6 Time-aware learning path | X |  |  |  | X | X |  |  |  |  |  |  |
| FR7 Assessment and rubric safety |  |  |  |  | X | X | X |  |  |  |  |  |
| FR8 Learner state update |  |  |  |  |  | X | X | X |  |  |  |  |
| FR9 Misconception repair and adaptation |  |  |  |  | X |  |  | X | X |  |  |  |
| FR10 Interest branch preservation |  |  |  |  | X |  |  | X |  | X |  |  |
| FR11 Teacher runtime judgment |  |  |  |  |  | X | X | X | X | X | X |  |
| FR12 Validation and quality gates | X | X | X | X | X | X | X | X | X | X | X | X |

---

## 7. Matrix Classification

| 字段 | 内容 |
|---|---|
| classification | decoupled / lower triangular |
| reason | 按 DP1 → DP12 的顺序，后续 FR 可以依赖前序 DP，但没有早期 FR 依赖后续 DP。validation 只作为最后检查，不被前序功能调用。 |
| execution_order | DP1 → DP2 → DP3 → DP4 → DP5 → DP6 → DP7 → DP8 → DP9 → DP10 → DP11 → DP12 |
| accepted_non_diagonal_links | 资料、地图、优先级、计划、状态、调整之间有真实顺序依赖，属于可接受的下三角依赖。 |
| rejected_pattern | 把 validation 当成所有早期 FR 的 DP；把每日计划提前到资料和优先级之前；把教师 rubrics 混入 student prompt。 |

### 7.1 执行顺序解释

1. **DP1 Mission**：先固定课程目标、范围、非法律意见边界。
2. **DP2 Sources**：登记法律原文、USPTO、判例、casebook 和近年更新。
3. **DP3 Source boundary**：建立资料效力分层，防止教学中混淆。
4. **DP4 Course map**：根据资料和边界生成概念地图。
5. **DP5 Priority / learning contract**：根据概念地图决定 A/B/C 和学习目标层级。
6. **DP6 Plan**：在优先级确定后，才生成 7 天路径和每日包。
7. **DP7 Quiz / visibility**：围绕每日包设计测验和延迟反馈。
8. **DP8 State**：每次教学后记录学习证据。
9. **DP9 Repair**：根据状态和误区决定修复与计划修改。
10. **DP10 Interest**：保存学习者分支问题，并判断是否进入后续学习。
11. **DP11 Teacher runtime**：保存教师私有判断和运行策略。
12. **DP12 Validation**：最后检查结构、内容、教学运行和可见性安全。

---

## 8. Coupling Retry Log

| Attempt | Problem | Change Made | Result |
|---|---|---|---|
| 1 | 初稿把“课程内容生成”写成一个大 FR，导致资料、概念地图、优先级、计划和测验全部挤在一起。 | 拆成 FR2 source registry、FR3 source authority separation、FR4 concept map、FR5 priority、FR6 learning path。 | 内容层从密集耦合变为顺序依赖。 |
| 2 | 初稿把“状态记录与自适应教学”写成一个 FR，导致 session record、score history、misconception、next action 和 plan change 混在一起。 | 拆成 FR8 learner state、FR9 misconception repair、FR10 interest branch。 | 状态保存、误区修复和兴趣分支有了独立责任。 |
| 3 | 初稿把教师 notebook、测验反馈和 validation 混合在一起，容易提前泄露评分要点。 | 拆成 FR7 assessment visibility、FR11 teacher runtime、FR12 validation。 | student prompt、post-answer feedback、teacher-private notes、quality check 分离。 |

重试后的矩阵已经不再是密集或不规则耦合。保留下来的依赖都是课程生成和运行中真实存在的顺序依赖。

---

## 9. Accepted Coupling

| ID | Coupled FRs | Coupled DPs | Why accepted | Risk | Guard / Test | Future Refactor Trigger |
|---|---|---|---|---|---|---|
| ADD-COUP-001 | FR2, FR3, FR4 | DP2, DP3, DP4 | 专利法概念地图必须依据资料来源和资料效力分层。 | 旧资料或二手解释可能进入主线。 | `resources.md` 每个核心主题必须标注 source type 和 confidence；source gap 不得隐藏。 | 用户上传指定 syllabus 或教材后，需要重新生成 concept map。 |
| ADD-COUP-002 | FR4, FR5, FR6 | DP4, DP5, DP6 | 7 天安排必须依赖概念地图和 A/B/C 优先级。 | 未确定优先级就排课，会导致资料堆砌。 | `priority-map.md` 每个 A 类主题必须能追溯到 `course-map.md`。 | 若 daily_minutes 或目标考试类型改变，重新生成 plan。 |
| ADD-COUP-003 | FR6, FR7, FR8 | DP6, DP7, DP8 | 测验和状态记录必须知道当前学习包和测验类型。 | 分数脱离题型和辅助程度，造成虚高。 | score history 必须记录 score_type、assistance mode、prompt_visibility。 | 若引入新的题型，需要更新 score schema。 |
| ADD-COUP-004 | FR8, FR9 | DP8, DP9 | 误区修复必须基于真实学习证据。 | 教师主观判断可能被当作已验证事实。 | misconception 只有通过新题或迁移题成功后才能标记 resolved。 | 若出现多次同类高严重度误区，拆出专题 repair package。 |
| ADD-COUP-005 | FR8, FR10, FR11 | DP8, DP10, DP11 | 兴趣分支和教师判断都需要读取学习状态。 | 分支内容过多，冲掉 7 天主线。 | interest ledger 记录 branch type、time cost、return point、whether affects plan。 | 若同一兴趣分支反复出现，转入 B/C 扩展单元。 |
| ADD-COUP-006 | FR12 with all previous FRs | DP12 reads DP1–DP11 | validation 必须检查全部前序产物。 | 误把 validation 当作早期模块依赖，破坏矩阵。 | validation 只能读取和报告，不改写前序模块责任。 | 若 validation 需要自动修复，再在 MDD 中定义 repair interface。 |

---

## 10. Module Boundary Analysis

这里的“模块”是后续 MDD 的候选模块，不是最终文件结构。

| Candidate Module | Owns | Must not own | Inputs | Outputs |
|---|---|---|---|---|
| Course Mission Module | 课程目标、范围、非范围、法律免责声明 | 具体每日讲义、测验答案 | URD | `mission.md` |
| Source Registry Module | 资料索引、source type、更新记录、source gaps | 概念教学顺序 | reference index、用户材料、官方资料 | `resources.md`、`recent-updates.md`、`source-gaps.md` |
| Source Boundary Module | 资料效力解释和教学用语规范 | 判例全文讲解 | source registry | source boundary table |
| Course Map Module | 概念地图、依赖、易混点 | 每日时间分配 | source registry、source boundary | `course-map.md` |
| Priority Module | A/B/C、学习层级、核心概念要求 | 具体题目文本 | course map | `priority-map.md`、learning contract |
| Planning Module | 7 天路径和每日包 | 评分细则、教师私有判断 | priority map、time constraints | `plan/seven-day-plan.md`、`plan/day-N.md` |
| Assessment Module | 题型、作答入口、反馈、延迟显示 | 教师 notebook 总体策略 | daily package、priority map | quiz、answer feedback、score event |
| State Module | current-state、session record、score history、recall deck、next action | 课程内容权威性判断 | assessment results、teacher notes | state files |
| Repair Module | 误区记录、重测、计划修改 | 普通兴趣分支保存 | state、misconceptions | repair task、plan-change record |
| Interest Module | 学习者提出的分支问题和回归主线策略 | A 类核心顺序 | state、user questions | interest-ledger record |
| Teacher Runtime Module | 教师私有判断、rubric、教学策略 | 学生可见 prompt | plan、quiz、state、repair、interest | teacher notebook、runtime notes |
| Validation Module | 结构检查、内容质量检查、可见性检查 | 课程内容生成的主要责任 | all generated files | validation report、repair recommendations |

---

## 11. Critical Interfaces for MDD

后续 MDD 应把以下接口写清楚。

| Interface ID | From | To | Contract |
|---|---|---|---|
| ADD-IF-001 | Source Registry | Course Map | 每个核心主题必须能读取 source type、source priority、confidence、last_checked 或 source gap。 |
| ADD-IF-002 | Course Map | Priority Module | 每个 A/B/C 判断必须引用一个 topic_id 和简短理由。 |
| ADD-IF-003 | Priority Module | Planning Module | A 类主题必须进入 7 天主线；B 类按时间进入；C 类只作背景或扩展。 |
| ADD-IF-004 | Planning Module | Assessment Module | 每日学习包必须给出可测试目标，不只给阅读任务。 |
| ADD-IF-005 | Assessment Module | State Module | 每个评分事件必须记录题型、辅助程度、是否提前暴露答案、证据片段。 |
| ADD-IF-006 | State Module | Repair Module | high-severity prerequisite misconception 会阻止依赖主题继续推进。 |
| ADD-IF-007 | State Module | Teacher Runtime | 教师可以记录判断，但能力结论必须区分“观察到的证据”和“推测”。 |
| ADD-IF-008 | Interest Module | Planning Module | 兴趣分支只在明确影响学习路径时写入 plan-change；否则只写 interest ledger。 |
| ADD-IF-009 | Teacher Runtime | Student Prompt | student prompt 不得包含答案要点、评分细则或教师私有判断。 |
| ADD-IF-010 | Validation Module | All modules | validation 报告只能指出失败和修复建议；若执行自动修复，必须另有 repair interface。 |

---

## 12. Patent-law-specific Design Risks

| Risk ID | Risk | Affected FR / DP | Design Response |
|---|---|---|---|
| ADD-RISK-001 | 把 MPEP 当成法律本体 | FR2, FR3 / DP2, DP3 | source boundary table 必须解释 statute、CFR、MPEP、guidance、case law 的不同地位。 |
| ADD-RISK-002 | 旧 casebook 未覆盖近年 AI / design patent / eligibility 更新 | FR2 / DP2 | `recent-updates.md` 单独记录 2024 年以后材料，使用前复核。 |
| ADD-RISK-003 | 课程被判例细节淹没 | FR4, FR5 / DP4, DP5 | 判例只作为规则边界卡片，不能替代概念地图。 |
| ADD-RISK-004 | §101、§102、§103、§112 被学生混成“新不新”一个问题 | FR4, FR7, FR9 / DP4, DP7, DP9 | 测验必须包含四门槛区分题和误用识别题。 |
| ADD-RISK-005 | 学生会背术语但不会适用 | FR5, FR7, FR8 / DP5, DP7, DP8 | A 类概念默认 L6，测验包含边界案例和简单事实适用。 |
| ADD-RISK-006 | 测验前泄露答案 | FR7, FR11, FR12 / DP7, DP11, DP12 | student prompt、feedback、teacher rubric 分离；validation 检查 prompt visibility。 |
| ADD-RISK-007 | 误区记录后未修复 | FR8, FR9 / DP8, DP9 | misconception tracker 要求 retest evidence；未通过不得标记 resolved。 |
| ADD-RISK-008 | 课程被误用为法律意见 | FR1, FR7 / DP1, DP7 | mission、练习和反馈均标注教育用途；真实个案只作假设讨论。 |

---

## 13. Trace Summary

| URD requirement group | ADD FR | Main DP |
|---|---|---|
| URD-GOAL-001 / URD-REQ-001 / URD-REQ-008 | ADD-FR-001 | ADD-DP-001 |
| URD-REQ-021 至 URD-REQ-025 | ADD-FR-002 | ADD-DP-002 |
| URD-SCEN-002 / URD-REQ-022 / URD-SUCC-004 | ADD-FR-003 | ADD-DP-003 |
| URD-REQ-009 至 URD-REQ-020 / URD-SUCC-001 | ADD-FR-004 | ADD-DP-004 |
| URD-REQ-004 / URD-REQ-026 / URD-REQ-027 | ADD-FR-005 | ADD-DP-005 |
| URD-CON-001 / URD-AC-012 | ADD-FR-006 | ADD-DP-006 |
| URD-TASK-002 / URD-REQ-005 / URD-REQ-028 / URD-REQ-029 | ADD-FR-007 | ADD-DP-007 |
| URD-TASK-003 / URD-REQ-002 / URD-DATA-007 至 URD-DATA-010 | ADD-FR-008 | ADD-DP-008 |
| URD-SCEN-005 / URD-AC-010 / URD-RISK-006 | ADD-FR-009 | ADD-DP-009 |
| URD-REQ-030 / URD-DATA-012 | ADD-FR-010 | ADD-DP-010 |
| URD-REQ-006 / URD-VIS-002 / URD-VIS-003 | ADD-FR-011 | ADD-DP-011 |
| URD-AC-001 至 URD-AC-012 / URD-SUCC-006 | ADD-FR-012 | ADD-DP-012 |

---

## 14. ADD Completion Gate

| Check | Result | Notes |
|---|---|---|
| FRs are derived from URD | pass | 12 个 FR 覆盖 URD 核心需求。 |
| Each FR has a primary DP | pass | DP1–DP12 与 FR1–FR12 对应。 |
| Matrix classified | pass | decoupled / lower triangular。 |
| Coupling retry performed | pass | 记录 3 次结构重试。 |
| Accepted coupling recorded | pass | 保留 6 项必要耦合，并给出 guard。 |
| Validation is not treated as early dependency | pass | DP12 位于最后，只读取前序产物。 |
| No daily plan generated prematurely | pass | 本文只规定 planning module，不生成 Day 1–Day 7。 |
| Teacher-private and student-visible material separated | pass | FR7 / FR11 / FR12 分离。 |
| Source freshness handled | pass | DP2 包含 `recent-updates.md` 和 source gaps。 |

---

## 15. Next Document Candidates

建议后续顺序：

1. **MDD**：把本 ADD 中的候选模块转成文件结构、数据结构和接口契约。
2. **TDD**：为 source tracing、visibility safety、state update、misconception repair、validation 设置测试。
3. **RMD**：规定课程包生成和人工修订的执行顺序。
4. **TRACE**：连接 URD → ADD → MDD → TDD → RMD → 实际课程文件。
5. **course-map / priority-map**：在 ADD 后生成正式美国专利法概念地图和 A/B/C 优先级。
