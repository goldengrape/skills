# 7 天速通美国专利法课程包：领域评分标准

> Darwin Domain Rubric / 领域评分标准  
> 适用对象：后续生成的“7 天速通美国专利法”课程包，而不是通用课程、通用法律课或专利代理人考试完整备考包。  
> 当前状态：draft，待用户确认后可冻结。  
> 生成日期：2026-07-07  
> 依据文件：`us_patent_law_reference_index.md`、`us_patent_law_course_URD.md`、`us_patent_law_course_ADD.md`、Darwin Skill 2.0、crash-course-learning OKF factory。

---

## 1. 评分目标

本评分标准用于判断一个课程包是否真正适合“7 天速通美国专利法”的目标。

它不只检查文件是否齐全，而是检查课程包是否能做到：

1. 以权威资料为依据解释美国专利法。
2. 区分法律原文、USPTO 审查资料、法院判例、教材解释和近年政策更新。
3. 覆盖 7 天速通必须掌握的核心主题。
4. 让弱基础学习者能用基础规则处理短答题、比较题和简单案例题。
5. 符合 factory OKF 的 stateful learning 要求：可记录、可恢复、可测试、可调整。
6. 控制法律教育场景中的风险：不提供具体法律意见，不假装当前规则已被完整核对。

---

## 2. 预期输入与输出

### 2.1 预期输入

| 类型 | 内容 |
|---|---|
| 用户目标 | 7 天速通美国专利法，面向基础较弱学习者，中文讲解，保留关键英文术语。 |
| 资料索引 | 35 U.S.C.、37 C.F.R.、MPEP、USPTO guidance、PTAB 资料、开源 casebook、核心判例、AI 与 design patent 近年更新。 |
| 课程设计文档 | URD、ADD，以及后续可能生成的 course map、priority map、daily package、quiz、state files。 |
| 学习运行记录 | session record、score history、misconception tracker、recall deck、teacher notebook、next action。 |

### 2.2 预期输出

被评分的课程包应至少包含：

| 类型 | 期望文件或内容 |
|---|---|
| 课程说明 | mission、scope、non-legal-advice notice、source gaps。 |
| 资料系统 | resources registry、source authority hierarchy、update tracker。 |
| 知识结构 | course map、A/B/C priority map、术语表、关键判例卡。 |
| 学习材料 | 7 天计划、每日讲义、每日练习、复习卡片、最终复习包。 |
| 测评材料 | quiz、answer feedback、rubric-gated feedback、迁移题。 |
| 状态文件 | current state、topic ledger、score history、misconceptions、recall deck、next action、plan changes。 |
| 教师运行材料 | teacher notebook、visibility policy、误区修复记录、后续调整记录。 |

---

## 3. 评分方式

总分 100。每个维度按 1–10 分评分，再乘以权重。

```text
领域总分 = Σ(维度得分 ÷ 10 × 权重)
```

### 3.1 等级解释

| 总分 | 结论 | 处理 |
|---:|---|---|
| 90–100 | 高质量可用 | 可进入真实学习运行，但仍需记录学习证据。 |
| 80–89 | 基本可用 | 可试运行；先修订主要短板。 |
| 70–79 | 需要修订 | 不建议直接用于完整 7 天学习。 |
| 60–69 | 低质量 | 只可作为草稿；必须重构关键部分。 |
| < 60 | 不合格 | 不进入课程运行。 |

### 3.2 与 Darwin 公共评分的关系

如果此评分标准用于 Darwin skill 优化流程，建议使用：

| 分数 | 权重 |
|---|---:|
| Darwin 公共 9 维评分 | 35% |
| 本领域评分标准 | 65% |

如果只是评价课程包本身，则直接使用本领域总分。

---

## 4. 领域评分维度总表

| ID | 维度 | 权重 | 主要检查问题 |
|---|---|---:|---|
| D1 | 资料权威性与时效性 | 12 | 是否正确使用法律原文、USPTO 资料、判例、教材和近年更新。 |
| D2 | 核心主题覆盖与 A/B/C 优先级 | 12 | 是否覆盖美国专利法速通必须掌握的主题，并区分主次。 |
| D3 | 概念依赖与学习顺序 | 8 | 是否先建立必要前提，再进入复杂规则和案例。 |
| D4 | 可专利性四大门槛的准确性 | 14 | §101、§102、§103、§112 是否讲准，且能避免常见误解。 |
| D5 | Claims、判例推理与答题能力 | 10 | 是否能训练学习者用规则处理基础案例和短答题。 |
| D6 | USPTO 实务与授权后程序基础 | 8 | 是否解释申请、检索、费用查询、PTAB/IPR/PGR 的基本作用和边界。 |
| D7 | 7 天速通教学适配性 | 10 | 是否适合弱基础学习者，在有限时间内建立可用概念地图。 |
| D8 | Stateful OKF 学习控制 | 10 | 是否能记录、恢复、修复误区、调整后续学习。 |
| D9 | 测评有效性与反馈质量 | 8 | 测验是否能区分会背、会用、会迁移；反馈是否安全。 |
| D10 | 风险控制、边界与不确定性处理 | 8 | 是否明确非法律意见、更新风险、source gaps 和不能做的事。 |

---

## 5. 详细评分标准

### D1. 资料权威性与时效性（12 分）

| 分数 | 锚点 |
|---:|---|
| 1 | 大量依赖二手总结或模型记忆；没有区分 35 U.S.C.、37 C.F.R.、MPEP、判例和教材；可能使用过时或虚构规则。 |
| 5 | 引用了部分权威资料，但资料层级说明不稳定；MPEP、casebook、USPTO guidance 和法院判例有时被混用。 |
| 10 | 明确建立资料效力层级；核心规则回到 35 U.S.C. 和 37 C.F.R.；审查实务回到 MPEP/USPTO；规则边界回到判例；2024 年后的 AI、eligibility、design patent、PTAB、费用等设有更新检查入口。 |

**常见失败**：把 MPEP 说成“法院规则”；把旧 casebook 当作当前政策全集；费用金额写死；AI inventorship 或 design patent 更新不查来源。  
**检查证据**：`resources.md`、source hierarchy、update tracker、每日讲义引用、资料索引链接。

---

### D2. 核心主题覆盖与 A/B/C 优先级（12 分）

| 分数 | 锚点 |
|---:|---|
| 1 | 主题严重遗漏，或把专利法讲成知识产权总论；没有区分必须掌握与背景知识。 |
| 5 | 覆盖了一些核心主题，但 A/B/C 优先级不清；可能过度展开国际专利、许可、商业化等非主线内容。 |
| 10 | A 类稳定覆盖：专利制度目的、专利类型与流程、§101、§102、§103、§112、claim construction、侵权与救济；B 类包含 PTAB、prior art search、AI-assisted inventions、design patent；C 类清楚标记为背景或暂不展开。 |

**常见失败**：7 天内平均铺开所有主题；把 Patent Bar 程序细节放得过重；忽略 claim construction 或 §112。  
**检查证据**：priority map、course map、seven-day plan、daily packages。

---

### D3. 概念依赖与学习顺序（8 分）

| 分数 | 锚点 |
|---:|---|
| 1 | 学习顺序跳跃，直接进入复杂判例或程序细节；前置概念缺失。 |
| 5 | 大体有顺序，但 claim、prior art、PHOSITA、specification、infringement 等依赖关系没有显式说明。 |
| 10 | 概念地图呈可执行的顺序依赖：制度目的 → 权利类型/流程 → patentability → claim/specification → claim construction → infringement/remedies → PTAB/updates；后续模块读取前序概念，不反向污染前序定义。 |

**常见失败**：先讲 Alice/Mayo 而不解释 §101；先讲侵权而不解释 claim scope；把 PTAB 当成普通诉讼。  
**检查证据**：course map、dependency notes、daily package 的 “前置知识” 和 “今日目标”。

---

### D4. 可专利性四大门槛的准确性（14 分）

| 分数 | 锚点 |
|---:|---|
| 1 | §101、§102、§103、§112 混淆；把“新颖”当作唯一判断；对 Alice/Mayo、KSR、enablement 等解释明显错误。 |
| 5 | 能分别介绍四个条文，但边界模糊；案例适用时常把 eligibility、novelty、obviousness、disclosure 混成一个问题。 |
| 10 | 能准确解释四个门槛的不同问题：§101 问是否属于可保护主题；§102 问是否已被现有技术公开；§103 问对 PHOSITA 是否显而易见；§112 问说明书和权利要求是否足够、清楚、受支持；能用基础事实分别适用。 |

**常见失败**：把 abstract idea 等同于“太抽象所以没用”；把 obviousness 解释成“普通人觉得容易”；把 enablement 和 written description 合并成“说明详细即可”。  
**检查证据**：§101/102/103/112 讲义、练习题、反馈样本、误区记录。

---

### D5. Claims、判例推理与答题能力（10 分）

| 分数 | 锚点 |
|---:|---|
| 1 | 课程只讲概念，不训练如何读 claim、如何用规则答题、如何从事实中找 issue。 |
| 5 | 有少量案例或判例介绍，但以案名记忆为主；学习者不一定能迁移到新事实。 |
| 10 | 课程明确训练 claim scope、claim construction、specification support、validity 与 infringement 的关系；判例用于解释规则边界；答题结构稳定使用“issue → rule → condition → fact application → conclusion”。 |

**常见失败**：判例卡只有案情故事；不区分 claim construction 与 infringement；反馈只给结论不给适用过程。  
**检查证据**：case cards、claim mini-exercises、quiz feedback、final review pack。

---

### D6. USPTO 实务与授权后程序基础（8 分）

| 分数 | 锚点 |
|---:|---|
| 1 | 完全忽略申请流程、prior art search、费用查询、PTAB；或把程序讲成执业建议。 |
| 5 | 简要介绍流程，但没有说明 provisional/nonprovisional、utility/design/plant、search、maintenance、IPR/PGR 的基本边界。 |
| 10 | 能让学习者知道美国专利如何从发明进入申请、审查、授权、维持和挑战；能使用 USPTO 官方入口做入门检索；能区分 IPR 与 PGR 的基本用途和限制；不把实务入门变成执业级建议。 |

**常见失败**：把 provisional 说成“临时专利”；把 PTAB 说成法院；把费用金额作为固定记忆点。  
**检查证据**：流程图、prior art search 练习、PTAB 说明、费用查询说明。

---

### D7. 7 天速通教学适配性（10 分）

| 分数 | 锚点 |
|---:|---|
| 1 | 内容像完整法学院课程或资料堆砌；弱基础学习者无法跟上。 |
| 5 | 有 7 天安排，但每日负荷不稳定；讲义、练习、复习之间联系较弱。 |
| 10 | 每日目标清楚、负荷合理；中文解释平实，保留必要英文术语；每一天都有“核心概念、例子、练习、反馈、复习卡”；不追求全覆盖，而追求可恢复的核心地图。 |

**常见失败**：一天塞入太多判例；只给阅读任务不给讲解；没有给弱基础学习者准备前置解释。  
**检查证据**：seven-day plan、daily work packages、glossary、recall deck。

---

### D8. Stateful OKF 学习控制（10 分）

| 分数 | 锚点 |
|---:|---|
| 1 | 课程只是静态讲义；没有学习记录、误区追踪或下一步动作。 |
| 5 | 有学习记录，但记录不影响后续教学；误区只写在反馈里，没有验证是否修复。 |
| 10 | 课程包包含 current state、topic ledger、score history、misconception tracker、recall deck、next action、plan changes 和 teacher notebook；每次学习后更新状态；后续教学读取前次证据再决定继续、复习或修复。 |

**常见失败**：记录文件空转；误区被标记为已解决但没有新题验证；教师 notebook 与学生反馈混在一起。  
**检查证据**：state directory、session records、misconception tracker、plan changes、teacher notebook。

---

### D9. 测评有效性与反馈质量（8 分）

| 分数 | 锚点 |
|---:|---|
| 1 | 测验只检查背诵；答案或评分要点提前泄露；反馈无法指导修复。 |
| 5 | 有测验和答案，但题型单一；不能区分独立回答、提示后回答和看答案后复述。 |
| 10 | 测评包含短答、比较、issue spotting、迁移题；评分记录辅助程度；反馈先指出事实、规则和推理错误，再给修复动作；作答前隐藏答案、评分细则和教师预判。 |

**常见失败**：只问“§101 是什么”；不给事实适用题；把完整答案放在学生作答前。  
**检查证据**：quiz files、answer feedback、score history、visibility policy、final review。

---

### D10. 风险控制、边界与不确定性处理（8 分）

| 分数 | 锚点 |
|---:|---|
| 1 | 课程给出具体法律建议，或对不确定/更新内容装作确定；没有安全边界。 |
| 5 | 有非法律意见声明，但不稳定；source gaps、更新风险、AI 生成内容边界没有贯穿课程。 |
| 10 | 明确声明教育用途和非法律意见；遇到具体申请、侵权、诉讼、商业决策时转为学习性解释；对近年更新和资料空白做显式记录；课程禁止把 AI 输出当作权威来源。 |

**常见失败**：判断某真实产品“必然侵权/不侵权”；给具体申请策略；隐去资料不确定性。  
**检查证据**：mission、safety/boundary notes、source gaps、teacher notebook、feedback samples。

---

## 6. Hard Gates

以下任一项触发时，课程包不得直接进入正式学习运行。除非特别说明，触发 hard gate 后领域评分上限为 59 分；严重法律幻觉或具体法律意见可直接判为不合格。

| Gate | 失败条件 | 处理 |
|---|---|---|
| HG1 | 课程把具体申请、侵权、诉讼、商业决策问题当作法律意见回答。 | 直接不合格；必须重写边界规则。 |
| HG2 | 缺少 §101、§102、§103、§112 任一核心模块。 | 领域评分上限 59；补齐后重评。 |
| HG3 | 没有资料效力分层，或把 MPEP、USPTO guidance、casebook、法院判例混为同一层级。 | 领域评分上限 69；修订 source hierarchy。 |
| HG4 | 出现虚构条文、虚构判例、虚构 USPTO 更新，或把未经核对的近年变化写成确定规则。 | 直接不合格或上限 59，视严重程度处理。 |
| HG5 | 课程包只是静态讲义，没有 stateful OKF 文件和学习记录机制。 | 领域评分上限 59。 |
| HG6 | 作答前泄露答案、评分细则或教师预判，导致测验失效。 | 领域评分上限 69；必须修复 visibility policy。 |
| HG7 | 误区记录不会影响后续学习，或误区未经新题验证就标记为解决。 | D8、D9 最高只能各给 6 分。 |
| HG8 | 课程承诺 7 天后达到执业级能力、完整 Patent Bar 能力或可替代律师判断。 | 领域评分上限 59；必须修改目标声明。 |

---

## 7. 领域测试 Prompt

这些 prompt 用于 Darwin 的效果验证或干跑验证。每条都应生成或检查可观察输出，不能只看回答是否“像样”。

```json
[
  {
    "id": "domain-1",
    "prompt": "请根据现有资料生成 7 天速通美国专利法课程包，学习者基础较弱，每天约 60 分钟，中文讲解，保留关键英文术语。",
    "purpose": "检查课程包完整性、A/B/C 优先级、资料分层、stateful OKF 文件和 7 天速通适配性。",
    "expected_checks": [
      "存在 mission/resources/course-map/priority-map/seven-day-plan/daily-packages",
      "存在 state files 和 teacher notebook",
      "A 类包含 §101/§102/§103/§112/claim construction/infringement basics",
      "资料来源区分法律原文、MPEP、USPTO guidance、判例和 casebook",
      "明确非法律意见边界"
    ],
    "target_dimensions": ["D1", "D2", "D3", "D7", "D8", "D10"],
    "target_hard_gates": ["HG1", "HG2", "HG3", "HG5", "HG8"]
  },
  {
    "id": "domain-2",
    "prompt": "运行一次 Day 2 或 §101 学习 session。学习者误以为 MPEP 就是法院必须遵守的法律，并且认为所有软件发明都不能申请专利。请教学、提问、反馈并更新状态。",
    "purpose": "检查资料效力分层、§101 准确性、误区修复和状态更新。",
    "expected_checks": [
      "解释 MPEP 与法院判例/法律原文的区别",
      "解释 Alice/Mayo 相关框架但不过度简化",
      "不直接给出完整测验答案",
      "misconception tracker 记录两个误区",
      "next action 安排后续验证题"
    ],
    "target_dimensions": ["D1", "D4", "D8", "D9", "D10"],
    "target_hard_gates": ["HG3", "HG6", "HG7"]
  },
  {
    "id": "domain-3",
    "prompt": "学习者回答：‘这个发明以前没人做过，所以一定满足美国专利法，可以授权。’请评分、反馈，并更新学习记录。",
    "purpose": "检查课程是否能区分 §102 新颖性、§103 非显而易见性、§112 公开要求和 §101 eligibility。",
    "expected_checks": [
      "指出新颖性不是唯一门槛",
      "分别提示 §101/§102/§103/§112 的问题",
      "记录辅助程度和错误类型",
      "生成一张或多张复习卡",
      "不给具体法律意见"
    ],
    "target_dimensions": ["D4", "D5", "D8", "D9", "D10"],
    "target_hard_gates": ["HG1", "HG7"]
  },
  {
    "id": "domain-4",
    "prompt": "课程维护者发现 USPTO 发布了新的 AI inventorship 或 design patent guidance。请说明课程包应如何处理资料更新，而不是直接改写结论。",
    "purpose": "检查资料时效性、更新追踪和 source gap 处理。",
    "expected_checks": [
      "要求核对 USPTO/Federal Register 等来源",
      "记录 update tracker 和 affected topics",
      "标记受影响的 daily package 或讲义",
      "说明哪些内容暂不能写成确定结论",
      "不伪造来源"
    ],
    "target_dimensions": ["D1", "D6", "D8", "D10"],
    "target_hard_gates": ["HG4"]
  },
  {
    "id": "domain-5",
    "prompt": "进行最终复习。学习记录显示学习者对 obviousness 和 enablement 仍不稳定。请生成复习任务，但不要提前泄露完整答案。",
    "purpose": "检查最终复习是否读取状态、针对弱点、保护测评有效性。",
    "expected_checks": [
      "读取 score history 和 misconception tracker",
      "针对 §103 与 §112 设计新题",
      "区分提示前/提示后表现",
      "反馈延迟到作答后",
      "更新 final review 和 next action"
    ],
    "target_dimensions": ["D4", "D7", "D8", "D9"],
    "target_hard_gates": ["HG6", "HG7"]
  }
]
```

---

## 8. 评分证据要求

正式评分时至少检查以下证据：

| 证据 | 最低要求 |
|---|---|
| 文件检查 | 查看课程包目录与核心文件，不接受只凭目录名打分。 |
| 内容抽样 | 至少抽查 §101、§102/103、§112、claim construction、PTAB 或更新追踪中的 4 个主题。 |
| 运行样本 | 至少运行 2 个学习 session 或干跑验证；必须包含一次误区修复。 |
| 状态检查 | 检查 state 文件是否被读取和更新，而不是只被创建。 |
| 测验检查 | 检查作答前是否隐藏答案和评分要点。 |
| 来源检查 | 随机核对 5 个法律或政策表述是否能追溯到资料索引中的权威入口。 |

如果只能做干跑验证，报告中必须标注 `dry_run`。如果全部为干跑，最终结论不得高于“基本可用”。

---

## 9. 领域评分标准质量自评

按照 Darwin 的 RQ1–RQ9，对本评分标准本身做初步质量评估。

| RQ | 维度 | 分数 | 理由 |
|---|---|---:|---|
| RQ1 | 目标匹配度 | 15/15 | 直接面向 7 天速通美国专利法课程包，覆盖用户已确认目标。 |
| RQ2 | 研究依据充分性 | 13/15 | 基于资料索引、URD、ADD、factory OKF 和 Darwin skill；尚未经过真实课程包运行数据验证。 |
| RQ3 | 维度完整性 | 10/10 | 覆盖资料、内容、概念顺序、实体法准确性、实务、教学、状态、测评和风险。 |
| RQ4 | 维度独立性 | 8/10 | D4 与 D5、D8 与 D9 有自然交叉，但评分证据不同，仍可分别观察。 |
| RQ5 | 可观察性与可评分性 | 14/15 | 大多数维度能从文件、讲义、测验、状态记录和运行样本中观察；真实学习效果仍需试运行。 |
| RQ6 | 权重合理性 | 9/10 | 权重偏向法律准确性、资料权威性和 stateful OKF；符合本课程风险。 |
| RQ7 | hard gates 合理性 | 10/10 | 覆盖法律意见、核心遗漏、资料混淆、法律幻觉、静态讲义化和测验泄露等高风险失败。 |
| RQ8 | 测试 prompt 匹配度 | 9/10 | prompt 覆盖生成、教学、反馈、更新、最终复习；后续可增加真实学习者样本。 |
| RQ9 | 抗模板污染能力 | 5/5 | 维度来自美国专利法课程包的具体任务，不是 Darwin 公共 9 维 rubric 的改名版本。 |

**总分：93 / 100**  
**结论：accept as draft，建议用户确认后冻结。**

保留条件：本标准尚未用真实生成课程包和真实学习 session 验证。首次课程包生成后，应至少用 `domain-1`、`domain-2`、`domain-3` 三个 prompt 做一次基线评分，再决定是否调整权重。

---

## 10. 待用户确认问题

1. 本课程是否明确面向“美国法学院式基础理解”，而不是 Patent Bar 备考？当前评分标准按前者设计。
2. 是否允许加入少量 patent prosecution 实务练习？当前只要求入门，不评分执业级 claim drafting。
3. 是否将 AI-assisted inventions 作为 B 类现代问题，还是提升为 A 类重点？当前按 B 类处理。
4. 是否需要为中国法背景学习者增加“中美专利制度差异”模块？当前列为可选背景，不进入主评分核心。

---

## 11. 冻结建议

如用户确认，本文件可作为：

- `domain-rubric.md`
- `domain-test-prompts.json` 的来源
- 后续 Darwin 评估美国专利法课程包的领域评分标准

冻结后，后续优化流程不得自动修改本评分标准。若资料索引、课程目标或用户定位发生变化，应重新生成并重新评估评分标准。
