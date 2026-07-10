# URD — 7 天速通美国专利法课程

> User Requirement Document / 用户需求文档  
> 本文只记录用户意图、课程目标、范围、约束和验收标准。  
> 不在本文中设计具体 7 天课程表、模块架构、每日讲义或测试题。  

---

## 0. Metadata

| 字段 | 内容 |
|---|---|
| project | 7 天速通美国专利法课程 |
| document_id | URD-USPATENT-0001 |
| status | draft |
| owner | Z / AI course designer |
| last_updated | 2026-07-07 |
| document_strength | standard |
| 依据 | crash-course-learning OKF factory；vibe coding skill URD checklist；`us_patent_law_reference_index.md` |

---

## 1. Project Goal

| ID | Goal | Status |
|---|---|---|
| URD-GOAL-001 | 为“美国专利法”生成一个 7 天速通课程的需求定义，使后续能够继续生成课程 OKF 包、课程地图、优先级、每日学习包、测验、学习记录和教师 notebook。 | draft |
| URD-GOAL-002 | 课程应帮助基础较弱学习者在短时间内建立美国专利法的核心概念地图，能解释主要规则，并能处理基础案例型或短答型问题。 | draft |
| URD-GOAL-003 | 课程应以权威资料为依据，区分法律条文、USPTO 审查政策、判例和教材解释，避免把旧资料或二手总结当作当前规则。 | draft |
| URD-GOAL-004 | 课程输出应可恢复、可测试、可记录、可调整，符合 Course Learning OKF 的 stateful learning 要求。 | draft |

---

## 2. Target Users / Roles

| ID | Role | Need / Motivation | Notes |
|---|---|---|---|
| URD-ROLE-001 | 主要学习者 | 需要在 7 天左右快速理解美国专利法核心框架，并能完成基础复习、讨论或考试型回答。 | 默认中文讲解，保留关键英文术语。 |
| URD-ROLE-002 | 课程设计者 / AI 教师 | 需要一份明确需求文档，后续据此生成 OKF 课程包，而不是直接堆砌资料。 | 应读取状态、记录学习证据、调整后续安排。 |
| URD-ROLE-003 | 课程维护者 | 需要知道哪些资料必须更新，哪些内容不能写死。 | 尤其关注 USPTO guidance、Federal Register、费用、PTAB 和 AI 相关更新。 |
| URD-ROLE-004 | 未来评估者 | 需要依据验收标准判断课程包是否可用。 | 不以“文件齐全”代替“学习质量合格”。 |

---

## 3. Core User Task

| ID | Core Task | Expected Result |
|---|---|---|
| URD-TASK-001 | 学习者进入课程后，能按 7 天速通模式学习美国专利法核心内容。 | 能说清专利制度目的、专利类型、申请流程、可专利性四大门槛、claims、侵权、救济和授权后程序。 |
| URD-TASK-002 | 学习者能回答基础考试型问题。 | 能用“规则 → 条件 → 事实适用 → 结论”的形式回答短答题、比较题和简单 issue-spotting 题。 |
| URD-TASK-003 | AI 教师能根据学习表现更新状态。 | 每次学习后更新 session record、score history、recall deck、misconception tracker、topic ledger 和 next action。 |
| URD-TASK-004 | 课程能在资料更新或学习者误解出现时调整。 | 新资料、误区、低分或兴趣分支会进入记录，并影响后续教学。 |

---

## 4. Core Scenarios

| ID | Scenario | Primary Actor | Expected Outcome |
|---|---|---|---|
| URD-SCEN-001 | 从零或弱基础开始学习美国专利法。 | 学习者 | 课程先建立整体地图，再进入核心规则，避免一上来阅读大量判例。 |
| URD-SCEN-002 | 学习者混淆法律条文、MPEP、USPTO guidance 与法院判例的效力。 | AI 教师 | 课程明确解释不同资料的地位，并用例子纠正。 |
| URD-SCEN-003 | 学习者需要判断一个发明是否可能获得美国专利。 | 学习者 | 能依次检查 §101、§102、§103、§112，而不是只凭“新不新”判断。 |
| URD-SCEN-004 | 学习者需要理解 claims 为什么是专利法核心。 | 学习者 | 能解释 claim scope、claim construction、说明书支持和侵权判断之间的关系。 |
| URD-SCEN-005 | 学习者答题后暴露误区。 | AI 教师 | 误区被记录；后续必须通过新题或迁移题验证后才能标记为解决。 |
| URD-SCEN-006 | 用户上传学校课件、考试题或教师提示。 | 课程维护者 / AI 教师 | 用户材料优先于通用资料；课程地图和优先级随之更新。 |
| URD-SCEN-007 | USPTO 或 Federal Register 出现新政策。 | 课程维护者 | 课程资料索引和相关讲义必须重新核对，不得继续沿用过时说明。 |

---

## 5. Confirmed Inputs

| ID | Input | Value / Evidence | Status |
|---|---|---|---|
| URD-IN-001 | course_name | 美国专利法 | confirmed |
| URD-IN-002 | course_duration | 7 天速通 | confirmed |
| URD-IN-003 | reference_materials | 已有 `us_patent_law_reference_index.md`，包含 35 U.S.C.、37 C.F.R.、MPEP、USPTO guidance、PTAB、开源 casebook、核心判例和近年更新。 | confirmed |
| URD-IN-004 | generation_method | 使用 factory OKF，并参考 vibe coding skill 的 URD → ADD → MDD → TDD → RMD 文档链。 | confirmed |
| URD-IN-005 | current_task | 当前只设计 URD，不生成课程安排。 | confirmed |

---

## 6. In Scope

### 6.1 Course Product Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| URD-REQ-001 | 课程必须面向一个单独课程目标：7 天速通美国专利法。 | must | 不混入版权法、商标法或商业秘密作为主线。 |
| URD-REQ-002 | 课程必须是 stateful course OKF，能记录、恢复和调整学习状态。 | must | 符合 factory OKF 的核心要求。 |
| URD-REQ-003 | 课程必须有明确学习目标、范围、假设、资料来源和 source gaps。 | must | 后续进入 mission、course-map、resources。 |
| URD-REQ-004 | 课程必须使用 A/B/C 优先级，而不是平均铺开所有专利法主题。 | must | A 为必须掌握，B 为应掌握，C 为可跳过或只作背景。 |
| URD-REQ-005 | 课程必须包含测验、答题反馈、错因记录和复习卡片。 | must | 不能只有讲义。 |
| URD-REQ-006 | 课程必须有教师 notebook，用于记录教学判断、学习证据、误区和后续调整。 | must | 教师私有信息不得提前泄露给学习者。 |
| URD-REQ-007 | 课程必须保留关键英文术语，并用中文解释。 | must | 如 patentability、prior art、obviousness、enablement、claim construction、infringement。 |
| URD-REQ-008 | 课程必须声明不是法律意见。 | must | 不为具体案件、申请、诉讼或商业决策提供法律意见。 |

### 6.2 Content Scope Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| URD-REQ-009 | 课程必须覆盖美国专利制度的基本交换逻辑：公开换取有限期排他权。 | must | 作为全课入口概念。 |
| URD-REQ-010 | 课程必须覆盖专利类型与基础流程：utility、design、plant、provisional、nonprovisional、examination、issuance、maintenance。 | must | 以理解为主，不训练正式执业。 |
| URD-REQ-011 | 课程必须覆盖 §101 patent eligible subject matter。 | must | 包括 process、machine、manufacture、composition of matter，以及 Alice/Mayo 框架。 |
| URD-REQ-012 | 课程必须覆盖 §102 novelty 和 prior art。 | must | 包括 anticipation、on-sale bar、AIA 基本变化。 |
| URD-REQ-013 | 课程必须覆盖 §103 nonobviousness。 | must | 包括 PHOSITA、Graham factors、KSR。 |
| URD-REQ-014 | 课程必须覆盖 §112 disclosure and claiming。 | must | 包括 written description、enablement、definiteness、claim。 |
| URD-REQ-015 | 课程必须覆盖 claim construction 的基础。 | must | 至少包含 Markman / Phillips 的核心意义。 |
| URD-REQ-016 | 课程必须覆盖基础侵权和救济。 | must | 包括 direct infringement、doctrine of equivalents、injunction、damages、willfulness。 |
| URD-REQ-017 | 课程必须覆盖 PTAB 与授权后挑战的基础。 | should | 包括 IPR、PGR 的用途和边界。 |
| URD-REQ-018 | 课程必须覆盖 AI-assisted inventions 和 design patent 的近年更新入口。 | should | 不要求深入政策论文，但要知道如何查最新资料。 |
| URD-REQ-019 | 课程应包含 prior art search 的入门训练。 | should | 使用 USPTO Patent Public Search 等官方入口。 |
| URD-REQ-020 | 课程可包含知识产权总论背景。 | could | 仅用于区分 patent、copyright、trademark、trade secret，不作为主线。 |

### 6.3 Source and Evidence Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| URD-REQ-021 | 法律原文优先使用 35 U.S.C. 和 37 C.F.R.。 | must | 不得只靠教材总结。 |
| URD-REQ-022 | USPTO 审查资料必须与法院判例分开说明。 | must | MPEP 是审查资料，不等同于最高法院规则本身。 |
| URD-REQ-023 | 开源 casebook 可作为结构来源，但不能替代法律原文和当前政策核对。 | must | 建议主参考 Masur & Ouellette。 |
| URD-REQ-024 | 2024 年以后的 AI、eligibility、design patent、PTAB、费用等更新必须单独追踪。 | must | 不得把旧 casebook 当作当前政策全集。 |
| URD-REQ-025 | 所有资料必须记录优先级、用途、可信度或 source gap。 | must | 后续写入 `resources.md`。 |

### 6.4 Learning Control Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| URD-REQ-026 | A 类概念默认要求达到 L6：不仅会复述，还能识别误用。 | must | 符合 factory learning-control 要求。 |
| URD-REQ-027 | 若目标提升到 L7，必须有迁移题或 barehand check。 | should | 例如给新事实判断 §101/102/103/112。 |
| URD-REQ-028 | 分数记录必须区分辅助程度。 | must | 例如独立回答、提示后回答、看答案后复述。 |
| URD-REQ-029 | 不能在学习者作答前泄露答案要点或评分 rubrics。 | must | 符合 visibility-safe 要求。 |
| URD-REQ-030 | 学习者主动提出的深入问题应进入 interest ledger，而不是打断主线后消失。 | should | 例如 AI inventorship、software patents、biotech patents。 |

---

## 7. Out of Scope

| ID | Item | Reason |
|---|---|---|
| URD-OOS-001 | 本文不设计具体 7 天课程安排。 | 当前任务是 URD；课程安排应在后续 OKF / plan 阶段完成。 |
| URD-OOS-002 | 不提供具体法律意见、申请策略、侵权风险意见或诉讼建议。 | 课程是教育用途，不替代律师或专利代理人。 |
| URD-OOS-003 | 不以美国专利代理人考试 Patent Bar 为完整目标。 | Patent Bar 涉及大量程序细节，7 天速通不能覆盖完整备考。 |
| URD-OOS-004 | 不追求法学院 3–4 学分专利法课程的完整深度。 | 目标是速通核心地图和基础应用。 |
| URD-OOS-005 | 不深入展开专利许可、转让、FRAND、ITC、国际 PCT、商业化和估值。 | 可列为 C 类或未来扩展。 |
| URD-OOS-006 | 不系统训练正式 claim drafting。 | 可解释 claim 的结构和作用，但不训练执业级撰写。 |
| URD-OOS-007 | 不把 USPTO 费用金额写成固定记忆点。 | 费用会更新，应训练如何查当前费用表。 |
| URD-OOS-008 | 不把 AI 生成内容作为权威法律来源。 | AI 可帮助解释、组织和测试，但必须回到权威资料核对。 |

---

## 8. Priority Map Requirement Draft

> 这里不是正式课程地图，只是 URD 层面的优先级约束。正式 A/B/C 图谱应在后续 course-map / priority-map 中生成。

### A — Must Learn

| ID | Topic | Reason |
|---|---|---|
| URD-A-001 | 专利制度基本目的与专利权边界 | 没有这个入口，后续规则会变成碎片。 |
| URD-A-002 | 专利类型与申请流程基础 | 帮助区分实体法与程序法。 |
| URD-A-003 | §101 patent eligibility | 美国专利法高频难点，尤其软件、生命科学、AI。 |
| URD-A-004 | §102 novelty / prior art | 判断可专利性的基础门槛。 |
| URD-A-005 | §103 nonobviousness | 最核心、最容易误解的专利性门槛之一。 |
| URD-A-006 | §112 disclosure / claims | 连接说明书、权利要求和专利范围。 |
| URD-A-007 | Claim construction | 侵权判断和有效性判断的共同入口。 |
| URD-A-008 | Infringement and remedies basics | 理解专利权实际如何被执行。 |

### B — Should Learn

| ID | Topic | Reason |
|---|---|---|
| URD-B-001 | PTAB / IPR / PGR 基础 | 现代美国专利制度中很重要，但速通可先掌握框架。 |
| URD-B-002 | Prior art search 入门 | 有助于理解 §102 和 §103。 |
| URD-B-003 | AI-assisted inventions | 近年重要更新，适合作为现代问题入口。 |
| URD-B-004 | Design patent 基础与 GUI/icon 更新 | 重要但不宜压过 utility patent 主线。 |
| URD-B-005 | Key cases card set | 用判例理解规则边界，而不是背全部事实。 |

### C — Can Skip / Background

| ID | Topic | Reason |
|---|---|---|
| URD-C-001 | 专利许可、转让与商业化 | 对速通核心规则不是必要前提。 |
| URD-C-002 | 国际专利、PCT、EPO 比较 | 容易拉宽范围。 |
| URD-C-003 | ITC 程序 | 偏高级争议解决。 |
| URD-C-004 | 高级损害赔偿计算 | 7 天内不宜深入。 |
| URD-C-005 | 全量 prosecution strategy | 偏执业训练。 |

---

## 9. Data Created / Stored / Updated

| ID | Data | Created / Updated By | Visibility | Notes |
|---|---|---|---|---|
| URD-DATA-001 | course mission | 课程生成阶段 | student-visible | 说明目标、范围、假设、非目标。 |
| URD-DATA-002 | resources registry | 课程生成与维护阶段 | student-visible | 记录资料来源、优先级、可信度、source gaps。 |
| URD-DATA-003 | course map | 课程生成阶段 | student-visible | 记录核心单元、依赖关系和易混点。 |
| URD-DATA-004 | priority map | 课程生成阶段 | student-visible | A/B/C 优先级。 |
| URD-DATA-005 | daily work packages | 课程生成阶段 | student-visible | 后续生成，不在本 URD 细写。 |
| URD-DATA-006 | quizzes and answer feedback | 学习过程中 | partly gated | 作答前不能泄露答案要点。 |
| URD-DATA-007 | session records | 每次学习后 | mixed | 学生可见学习记录；教师私有判断分开保存。 |
| URD-DATA-008 | score history | 每次测验后 | student-visible summary | 应记录题型、辅助程度、分数和证据。 |
| URD-DATA-009 | misconception tracker | 每次反馈后 | student-visible where useful | 误区需通过新题验证后才可关闭。 |
| URD-DATA-010 | recall deck | 每次学习后 | student-visible | 用于复习。 |
| URD-DATA-011 | teacher notebook | AI 教师维护 | teacher-private by default | 包含教学判断、后续策略、不可提前显示的 rubrics。 |
| URD-DATA-012 | interest ledger | 学习者提出分支问题时 | student-visible summary | 保存兴趣分支，防止主线被完全打断。 |
| URD-DATA-013 | update tracker | 资料维护阶段 | maintainer-visible | 追踪 USPTO / Federal Register 等更新。 |

---

## 10. Access and Visibility Rules

| ID | Rule | Priority | Notes |
|---|---|---|---|
| URD-VIS-001 | 学习者可见课程目标、资料索引、课程地图、优先级、每日任务、自己的学习记录和反馈。 | must | 提高可恢复性。 |
| URD-VIS-002 | 作答前不得展示答案、评分细则、标准答案要素或教师预判。 | must | 防止测试失效。 |
| URD-VIS-003 | 教师 notebook 可以记录私有教学判断，但不能把学习者未验证的能力判断说成事实。 | must | 避免伪精确评分。 |
| URD-VIS-004 | 资料更新、source gap 和不确定性应对学习者可见。 | should | 课程可信度来自明确边界，而不是假装确定。 |

---

## 11. Constraints

| ID | Type | Constraint | Impact |
|---|---|---|---|
| URD-CON-001 | time | 默认 7 天完成；每日学习时间暂按 60 分钟假设。 | 后续课程设计必须压缩主题，不做全量法学院课程。 |
| URD-CON-002 | language | 默认中文讲解，关键英文法律术语保留。 | 讲义需中英术语并列，避免翻译丢失法律含义。 |
| URD-CON-003 | source | 权威资料优先级：用户材料 > 法律原文 / USPTO / 判例 > 开源 casebook > 其他资料。 | 后续生成 resources 时必须记录 source confidence。 |
| URD-CON-004 | legal | 不提供法律意见。 | 具体案件、申请、侵权风险只能作为教学假设，不作建议。 |
| URD-CON-005 | freshness | 美国专利法、USPTO guidance、费用和程序会变化。 | 近年更新必须单独追踪，使用前复核。 |
| URD-CON-006 | assessment | 若考试形式未知，默认混合：术语解释、短答、比较题、简单案例分析。 | 不假设只有选择题。 |
| URD-CON-007 | teaching | A 类概念默认需要误用识别，不只要求背定义。 | 测验应包含反例、边界案例和混淆项。 |
| URD-CON-008 | visibility | 答案和 rubrics 必须延迟显示。 | 课程包要区分 teacher_says 与 teacher_thinks。 |
| URD-CON-009 | adaptability | 若学习证据显示误区严重，后续计划必须调整。 | 不得机械推进 7 天表。 |
| URD-CON-010 | simplicity | URD 不写实现架构，不提前生成冗余文件内容。 | 后续进入 ADD/MDD 时再讨论结构。 |

---

## 12. Acceptance Criteria

| ID | Related Requirement | Statement | Oracle |
|---|---|---|---|
| URD-AC-001 | URD-REQ-001 | 后续课程包只服务“7 天速通美国专利法”这一个课程目标。 | `mission.md` 和 `course-map.md` 未混入其他 IP 法主线。 |
| URD-AC-002 | URD-REQ-002 | 课程包包含 stateful OKF 所需状态文件，并规定每次学习后更新。 | 存在 current-state、topic-ledger、recall-deck、misconceptions、score-history、next-action、session records。 |
| URD-AC-003 | URD-REQ-004 | 后续课程必须有 A/B/C 优先级图。 | `priority-map.md` 中每个 A/B/C 项都有理由。 |
| URD-AC-004 | URD-REQ-009 至 URD-REQ-018 | 核心内容覆盖 patent system、patent types、§101、§102、§103、§112、claims、infringement、remedies、PTAB 和近年更新入口。 | `course-map.md` 和 `resources.md` 能逐项对应。 |
| URD-AC-005 | URD-REQ-021 至 URD-REQ-025 | 每个核心主题都能追溯到至少一个权威或高质量资料。 | `resources.md` 记录来源、用途、优先级和 confidence。 |
| URD-AC-006 | URD-REQ-026 | A 类概念不只用定义题测试，还包含误用识别或边界判断。 | quiz / assessment 中存在 misuse-discrimination 项。 |
| URD-AC-007 | URD-REQ-029 | 学习者作答前看不到答案要素。 | 教师 notebook 与 student prompt 分离；feedback 在作答后显示。 |
| URD-AC-008 | URD-REQ-008 | 课程明确声明教育用途，不构成法律意见。 | `mission.md` 或课程入口出现免责声明。 |
| URD-AC-009 | URD-CON-005 | 课程对 2024 年以后更新有单独追踪位置。 | 存在 recent updates tracker 或 resources 中有更新区。 |
| URD-AC-010 | URD-CON-009 | 学习者严重误解时，课程不会继续推进依赖性强的 A 类主题。 | misconception tracker 与 plan-change log 能显示调整。 |
| URD-AC-011 | URD-GOAL-002 | 学习者在最终复习中能完成基础案例分析。 | mock exam 或 final review 中至少包含 2 道事实型分析题，并按规则适用评分。 |
| URD-AC-012 | URD-GOAL-004 | 课程不是静态讲义，而是能教、测、记、改。 | 存在 daily work package、quiz、session record、state update rules、next action。 |

---

## 13. Success Criteria

| ID | Criterion | Measurement |
|---|---|---|
| URD-SUCC-001 | 学习者能画出美国专利法核心地图。 | 能把 patentability、disclosure、claims、infringement、remedies、PTAB 放入一张逻辑图。 |
| URD-SUCC-002 | 学习者能解释四个可专利性门槛。 | 对 §101、§102、§103、§112 各给出定义、判断问题和常见误区。 |
| URD-SUCC-003 | 学习者能处理基础事实题。 | 对新事实能按“issue → rule → application → conclusion”写出短答。 |
| URD-SUCC-004 | 学习者能区分资料地位。 | 能说明 35 U.S.C.、37 C.F.R.、MPEP、USPTO guidance、case law、casebook 的不同用途。 |
| URD-SUCC-005 | 课程包能被继续使用和更新。 | 状态文件、资料索引、误区记录、学习记录和更新追踪存在且可读。 |
| URD-SUCC-006 | 后续生成的课程包能通过 factory validation。 | 结构、内容质量、教学运行质量均通过；没有关键占位符。 |

---

## 14. Risks

| ID | Risk | Impact | Mitigation |
|---|---|---|---|
| URD-RISK-001 | 美国专利法内容过多，7 天内无法完整覆盖。 | 学习者负担过重，课程失焦。 | 使用 A/B/C 优先级；C 类只作背景。 |
| URD-RISK-002 | 学习者把 MPEP 当成法院判例或法律原文。 | 对法律效力理解错误。 | 每次使用资料时标明 source type。 |
| URD-RISK-003 | 旧 casebook 未覆盖最新 USPTO guidance。 | AI、design patent、eligibility 等主题过时。 | recent updates tracker 单独维护。 |
| URD-RISK-004 | 课程变成判例背诵。 | 初学者无法形成规则结构。 | 判例只服务规则边界，每案做“问题—规则—用途”卡片。 |
| URD-RISK-005 | 课程误导为法律服务。 | 产生合规和使用风险。 | 入口和练习均标注教育用途，不处理真实个案建议。 |
| URD-RISK-006 | 学习者短期记住术语但不会适用。 | 速通效果虚高。 | A 类概念要求误用识别和事实适用。 |
| URD-RISK-007 | 资料堆砌导致学习路径不清。 | 后续课程难以运行。 | URD 后续必须进入 ADD / course-map / priority-map，而不是直接扩写资料。 |

---

## 15. Assumptions

| ID | Assumption | Why acceptable now | Review Trigger |
|---|---|---|---|
| URD-ASM-001 | 学习者默认是中文母语或更适合中文讲解。 | 用户使用中文沟通，项目中其他课程也采用中文教学。 | 用户要求英文课程或 bilingual handout。 |
| URD-ASM-002 | 学习者基础为 zero / weak。 | “速通”课程通常需要从概念地图开始。 | 用户说明已有法学或专利实务基础。 |
| URD-ASM-003 | 每日学习时间默认 60 分钟。 | factory OKF 默认场景为 7 天、每天 60 分钟。 | 用户指定不同时间。 |
| URD-ASM-004 | 当前没有学校课件、历史题或教师提示。 | 目前只有参考资料索引。 | 用户上传课程材料或考试说明。 |
| URD-ASM-005 | 目标不是高分精训，而是稳定掌握核心地图和基础答题。 | 符合 7 天速通定位。 | 用户指定 Patent Bar、法学院期末高分或律师执业训练。 |
| URD-ASM-006 | 主教材参考 Masur & Ouellette，权威校验回到法律原文、USPTO 和判例。 | 已在资料索引中作为 A 级开源教材。 | 用户选择其他指定教材。 |
| URD-ASM-007 | 考试形式未知时，默认 mixed：术语解释、短答、比较、简单事实分析。 | factory reconnaissance 对未知考试形式的默认策略。 | 用户提供考试题型。 |

---

## 16. Open Questions

| ID | Question | Blocks? | Owner | Resolution |
|---|---|---|---|---|
| URD-Q-001 | 目标学习者更接近法学生、工程背景学习者、创业者，还是 IP 从业入门者？ | no | User | 暂按基础较弱的中文学习者处理。 |
| URD-Q-002 | 是否存在具体考试日期、题型、评分标准或课程 syllabus？ | no | User | 暂按通用美国专利法速通处理。 |
| URD-Q-003 | 是否需要把判例原文阅读纳入学习任务？ | no | User | 暂按“判例卡片 + 关键段落”处理。 |
| URD-Q-004 | 是否需要最终输出为完整课程包目录？ | no | User / AI | URD 之后再决定是否生成 OKF package。 |
| URD-Q-005 | 是否要求引用格式为 Bluebook、普通链接，还是教学友好格式？ | no | User | 暂用教学友好格式；正式法律写作另行处理。 |
| URD-Q-006 | 是否需要英语答题模板？ | no | User | 暂以中文理解为主，保留英文法律术语。 |

---

## 17. Parking Lot

| ID | Idea | Reason Parked |
|---|---|---|
| PARK-001 | 设计 Patent Bar 专项版本。 | 超出 7 天游学核心范围。 |
| PARK-002 | 做美国专利法与中国专利法比较版。 | 会扩大范围，当前先专注美国法。 |
| PARK-003 | 做软件专利 / AI 专利专题课。 | 可作为后续专题，不进入基础课主线。 |
| PARK-004 | 做 claim drafting 工作坊。 | 偏执业训练，当前只讲 claim 理解。 |
| PARK-005 | 做 PTAB 深度程序课。 | 当前只需理解 IPR / PGR 基础。 |
| PARK-006 | 做专利诉讼 damages 专题。 | 复杂度过高，当前只做救济概念。 |

---

## 18. URD Completion Gate

- [x] Target user or role is known.
- [x] Core task is known.
- [x] At least one measurable success criterion exists.
- [x] Scope and non-scope are separated.
- [x] Main constraints are recorded.
- [x] Assumptions and open questions are separated from confirmed requirements.
- [x] Content not needed for current version moved to Parking Lot.
- [x] URD avoids implementation architecture and daily course arrangement.

---

## 19. Next Document Candidates

后续如果继续按 vibe coding skill 和 factory OKF 推进，建议顺序是：

1. `ADD.md`：把本 URD 中的用户需求拆成相互独立的功能需求与设计参数，检查是否过度耦合。
2. `course-map.md`：生成美国专利法概念地图、依赖关系和易混点。
3. `priority-map.md`：正式生成 A/B/C 优先级。
4. `resources.md`：从资料索引中抽出课程实际使用资料，并标明 source gaps。
5. `plan/seven-day-plan.md`：在需求、设计拆分和课程地图清楚后，再生成 7 天安排。
