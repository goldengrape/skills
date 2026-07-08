---
type: Teacher Notebook
title: Day 3 Teacher Notebook — AD-AS 模型
description: Day 3 对话同步记录；作答前不展示隐藏评分细则或参考答案。
tags: [teacher-notebook, macroeconomics, day-3, ad-as, sync]
timestamp: 2026-07-02T00:00:00-07:00
visibility_note: student_safe_copy_before_assessment
---

# Day 3 Teacher Notebook — AD-AS 模型

```yaml
course: 宏观经济学 7 天 Crash Course
day: 3
status: in_progress
session_date: 2026-07-02
time_policy: soft
source_skill: macro_crash_course_teaching_skill_round4_updated
student_level: zero_basis_but_day1_day2_stable
notebook_mode: append_only_sync
prompt_visibility_rule: 作答前只展示题目、格式和中性提醒；不展示隐藏评分细则或参考答案。
```

## 0. 已读取材料

- `SKILL.md`
- `course-map.md`
- `glossary.md`
- `priority-map.md`
- `final-review/compressed-notes.md`
- `plan/day-3.md`
- `quizzes/day-3-quiz.md`
- `teacher/rubrics/day-3-rubric.md`
- `teacher/answer-keys/day-3-answer-key.md`
- `teacher/teaching-protocol.md`
- `teacher/visibility-rules.md`
- `teacher/time-policy.md`
- `learning-records/day-1-macroeconomics-learning-record.md`
- `learning-records/day-2-macroeconomics-learning-record.md`
- `day-2-teacher-notebook.md`

## 1. Day 1–2 带入 Day 3 的状态

```yaml
prior_day_1:
  quiz_score: 38/40
  status: completed
  stable_topics:
    - GDP definition
    - final goods and value added
    - expenditure approach
    - nominal GDP vs real GDP
    - GDP deflator
    - inventory investment
    - GDP vs GNP
prior_day_2:
  quiz_score: 45.5/50
  status: completed_with_extensions
  stable_topics:
    - CPI definition and calculation
    - inflation rate calculation
    - CPI substitution/new goods/quality biases
    - unemployment rate and labor force
    - discouraged workers
    - frictional, structural, cyclical unemployment
  watch_points:
    - labor force participation rate = labor force / adult population, not employed / adult population
    - discouraged workers are not counted as unemployed because they stopped searching
    - keep exam expression concise
current_day: 3
next_action: run_day_3
```

## 2. Day 3 学习目标

学生完成本节后，应能用考试语言解释：

- aggregate demand, AD：总需求曲线含义。
- short-run aggregate supply, SRAS：短期总供给曲线含义。
- long-run aggregate supply, LRAS：长期总供给 / 潜在产出含义。
- output gap：实际产出和潜在产出之间的差距。
- demand shock：需求冲击如何移动 AD。
- supply shock：供给冲击如何移动 SRAS。
- 能判断消费者信心下降、政府支出增加、油价上涨、技术进步等情形对产出和价格水平的影响。

## 3. 教学流程

| 阶段 | 学生可见动作 | 记录动作 |
|---|---|---|
| Recall | 先回答 Day 2 回忆题：CPI vs 通胀率、劳动参与率、灰心工人 | 记录是否修复劳动参与率薄弱点 |
| Map | 定位 Day 3：从“衡量经济”转向“解释经济波动” | 记录是否能把 CPI/失业率与 AD-AS 联系起来 |
| Core | 用“定义—例子—易错点—考试写法”讲 AD、SRAS、LRAS、output gap、demand/supply shock | 记录概念稳定度与例子 |
| Feynman | 用 6 句话解释 AD-AS，并包含一个生活例子 | 记录表达是否可写进卷面 |
| Exam practice | 消费者信心下降如何影响 AD-AS 均衡 | 作答后评分并更新错因 |
| State update | 总结、测验、更新回忆卡 | 更新 notebook 与学习记录 |

## 4. Append-Only Turn Log

### day3-t00 — session_start

```yaml
phase: state_reading_and_setup
score_type: not_scored
prompt_visibility: student_safe_setup_only
student_request_summary: |
  学生要求详细阅读 macro_crash_course_teaching_skill，并开始 Day 3 学习；同时要求撰写教师 notebook 文档并随对话同步更新。
teacher_says_summary:
  - 已读取 Day 3 计划、测验、教师侧规则、Day 1/2 学习记录和 Day 2 notebook。
  - Day 3 主题为 AD-AS 模型，目标是判断需求冲击和供给冲击如何影响产出与价格水平。
  - 开头先复查 Day 2 的劳动参与率、灰心工人和 CPI/通胀率，然后进入 AD、SRAS、LRAS。
hidden_details_status: 作答前不展示 Day 3 rubric 或 answer key 的具体评分要素。
engagement_observation:
  interest_level: high
  attention_signal: stable
  evidence:
    - 学生主动要求按 skill 运行，并要求同步教师 notebook。
teaching_decision:
  action: start_with_day2_recall_then_day3_map
  reason: Day 2 总分达到继续标准，但劳动参与率公式需要 Day 3 开头轻复习。
state_updates:
  - Day 3 notebook created.
  - status set to in_progress.
  - next visible prompt should be recall check.
```

## 5. 待更新区

后续每次学生作答后追加：

- 学生原始回答摘要。
- 掌握点。
- 遗漏点。
- 混淆点。
- 修正版考试表达。
- 是否新增 recall card。
- 是否更新 misconception。
- 阶段性分数及 `score_type`。

### day3-t01 — day2_recall_check_student_answer

```yaml
phase: day2_recall_check
score_type: blind_score_after_answer
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生回答了 Day 3 开头的 Day 2 复查题。CPI 与通胀率部分能说明 CPI 是价格指数，通胀率是 CPI 相对上一期的百分比变化。劳动力题中正确识别劳动力 = 就业者 + 正在找工作者 = 300 + 50 = 350，并正确计算失业率 = 50 / 350 = 14.28%。但劳动参与率再次误用就业人数作为分子，写成 300 / 500 = 60%；正确应为劳动力 / 成年人口 = 350 / 500 = 70%。灰心工人题能说明灰心工人退出失业人数和劳动力，分子分母同时减少，官方失业率可能下降，但就业人数没有增加，因此就业市场未必改善。
assessment:
  q1_cpi_vs_inflation_rate: 9/10
  q2_labor_force_unemployment_participation: 8/12
  q3_discouraged_worker_effect: 9/10
  total: 26/32
mastered:
  - 能区分 CPI 是价格水平指数，通胀率是 CPI 的百分比变化。
  - 能正确识别劳动力 = 就业者 + 正在找工作的失业者。
  - 能正确计算失业率 = 失业人数 / 劳动力。
  - 能解释灰心工人增加会让官方失业率看起来下降，但就业人数并未增加。
watch_points:
  - 劳动参与率仍需修正：劳动参与率 = 劳动力 / 成年人口 × 100%，不是就业人数 / 成年人口。
  - “就业人数 / 成年人口”更接近 employment-population ratio，不是 labor force participation rate。
  - “灰心工人”不要写成“回薪工人”或“灰薪工人”。
teaching_decision:
  action: immediately_repair_participation_rate_then_proceed_to_ad_as
  reason: CPI、失业率、灰心工人机制稳定；劳动参与率错误重复出现，但可通过固定对比句修复。Day 3 主线可以开始，但下次仍需再抽查一次。
student_state_update:
  day2_recall_status: mostly_stable
  labor_force_participation_rate_status: needs_light_review_again
  readiness_to_start_day3_core: yes_after_correction
```

#### 可写进卷面的修正版

1. CPI 是固定消费篮子价格相对基准年的指数；通胀率是 CPI 从一期到下一期的百分比变化。
2. 劳动力 = 就业者 + 正在找工作的失业者 = 300 + 50 = 350。失业率 = 50 / 350 × 100% ≈ 14.3%。劳动参与率 = 劳动力 / 成年人口 × 100% = 350 / 500 × 100% = 70%。就业人数 / 成年人口 = 300 / 500 = 60%，这是就业人口比率，不是劳动参与率。
3. 灰心工人停止找工作后，不再计入失业人数，也不再计入劳动力。因此官方失业率可能下降，但这不是因为就业人数增加，而是因为有人退出劳动力市场，所以就业市场不一定改善。

#### 更新 misconception

```text
Misconception: 劳动参与率 = 就业人数 / 成年人口。
Correction: 劳动参与率 = 劳动力 / 成年人口 × 100%。就业人数 / 成年人口 是就业人口比率。
Status: needs_light_review_again
Source: day3-t01 recall check
```

#### 更新 recall card

```text
Q: 劳动参与率和就业人口比率有什么区别？
A: 劳动参与率 = 劳动力 / 成年人口；就业人口比率 = 就业人数 / 成年人口。劳动参与率的分子包括就业者和正在找工作的失业者。
Due: next_check
Source: day3-t01 recall check
```

### day3-t02 — teaching_preference_curve_diagrams

```yaml
phase: teaching_preference_update
score_type: not_scored
prompt_visibility: student_feedback
student_feedback_summary: |
  学生指出，讲解经济学曲线时应优先使用程序绘制的示意图，或直接引用权威教学网站的示意图。ASCII 字符图只适合非常简单的线性图，复杂图形容易受手机、桌面、换行宽度影响而失真。
teaching_adjustment:
  - 后续讲解曲线时，默认配示意图。
  - 首次讲解曲线时，先说明横轴、纵轴及其设定理由。
  - 优先使用程序绘图生成稳定的图片，如 matplotlib 图像。
  - 需要引用外部图示时，优先选择权威教学网站或机构来源，并标注来源。
  - ASCII 图仅用于临时提示或极简单图形，不作为复杂曲线的主要讲解方式。
reason: |
  曲线图是 Day 3 之后宏观模型学习的核心工具。稳定、可读、跨设备不变形的图像能降低学生把价格水平和真实产出轴混淆的风险，也能帮助区分沿曲线移动与曲线整体移动。
student_state_update:
  diagram_preference: programmatic_or_authoritative_images_preferred
  ascii_diagrams: use_only_for_simple_temporary_sketches
```

### day3-t03 — ad_curve_reexplanation_with_program_diagram

```yaml
phase: ad_as_core_ad_curve
score_type: not_scored
prompt_visibility: student_requested_reexplanation
student_request_summary: |
  学生要求按新的图形教学规则重新讲解 AD 曲线。
teaching_actions:
  - 使用程序绘制 AD 曲线示意图，保存为 /mnt/data/ad_curve_reexplained.png。
  - 首先说明坐标轴：纵轴为价格水平 P，横轴为真实产出 Y。
  - 解释坐标轴设定理由：AD-AS 模型研究整体价格水平和总产出如何共同决定。
  - 解释 AD 表示不同价格水平下整个经济愿意购买的最终产品和服务总量。
  - 解释 AD 向右下倾斜的三类直觉：购买力效应、利率效应、净出口效应。
  - 区分沿曲线移动与曲线整体移动。
  - 给出 AD 左移/右移的常见原因。
watch_points:
  - 后续继续避免 ASCII 主图。
  - 每次涉及曲线移动时，明确说明“在每一个价格水平下”的含义。
  - 继续检查学生能否把 AD 左移的短期均衡结果和“价格固定不变”的假设区分开。
student_state_update:
  ad_curve_explained: yes
  diagram_used: programmatic_png
  next_teaching_move: ask AD left shift equilibrium check
```

### day3-t04 — ad_left_shift_check_student_answer

```yaml
phase: ad_curve_shift_check
score_type: blind_score_after_answer
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生回答消费者信心下降、家庭减少消费的 AD 题。学生正确判断这不是沿着曲线移动，而是 AD 曲线整体移动。理由是消费 C 下降，使支出法中的总需求下降；在同一价格水平下，对真实产出 Y 的需求减少，因此 AD 向左移动。学生也正确判断短期内真实产出下降。但学生认为价格水平“维持不变”，这是需要修正的地方：若放入 AD-SRAS 短期均衡，AD 左移与向右上倾斜的 SRAS 重新相交，通常会使价格水平下降。
assessment:
  identifies_shift_not_movement_along_curve: 5/5
  uses_C_component_of_AD: 5/5
  shift_direction: 5/5
  real_output_effect_short_run: 4/5
  price_level_effect_short_run: 1/5
  total: 20/25
mastered:
  - 能从 C + I + G + NX 中识别消费下降会减少 AD。
  - 能说明“在价格水平不变时，需求的真实产出减少”，这是 AD 左移的定义。
  - 能判断 AD 左移会使短期真实产出下降。
watch_points:
  - “在每一个给定价格水平下，Y 的需求减少”只是解释曲线左移，不等于新的均衡价格水平不变。
  - 若题目问短期均衡结果，需要把 AD 与 SRAS 一起看；AD 左移通常使 P 下降、Y 下降。
  - 后续应反复区分：曲线移动的定义 vs 均衡点变化的结果。
teaching_decision:
  action: correct_price_level_effect_with_ad_sras_diagram
  reason: 学生已经掌握 AD 左移的来源和方向，但需要把“给定价格水平”的比较和“新均衡价格水平”的变化分开。
student_state_update:
  ad_shift_direction_stability: strong
  ad_short_run_equilibrium_effect: partially_stable
  misconception_new:
    - 曲线左移定义中“给定价格水平”容易被误解为短期均衡价格水平不变。
```

#### 可写进卷面的修正版

消费者信心下降会使消费 C 减少，因此在每一个价格水平下，总需求都减少，AD 曲线向左移动。短期内，AD 左移与 SRAS 重新相交，通常导致真实产出下降、价格水平下降。这里“在每一个价格水平下需求减少”是解释曲线左移，不表示新的均衡价格水平不变。

#### 新增 misconception

```text
Misconception: AD 左移时，因为是在给定价格水平下比较，所以短期均衡价格水平不变。
Correction: “给定价格水平下需求减少”只是 AD 左移的定义。若考虑 AD-SRAS 短期均衡，AD 左移通常使新均衡的真实产出下降、价格水平也下降。
Status: needs_recheck
Source: day3-t04 AD left shift check
```

#### 更新 recall card

```text
Q: AD 左移的定义和短期均衡结果分别是什么？
A: 定义上，AD 左移表示在每一个价格水平下，总需求的真实产出减少；短期均衡中，AD 左移与 SRAS 重新相交，通常使真实产出下降、价格水平下降。
Due: next_check
Source: day3-t04 AD left shift check
```

### day3-t05 — student_requests_sras_explanation

```yaml
phase: sras_curve_instruction
score_type: not_scored
prompt_visibility: student_initiated_request
student_question_summary: |
  学生指出，在尚未仔细讲解 SRAS 之前，要求判断 AD 左移后的短期价格水平变化有些超前，因此请求接下来讲解 SRAS 曲线。
teaching_response_plan:
  action: teach_sras_with_programmatic_diagrams
  diagrams_created:
    - /mnt/data/sras_curve_and_shifts.png
    - /mnt/data/sras_movement_along_curve.png
  teaching_constraints_applied:
    - 曲线讲解优先使用程序绘图，不使用 ASCII 作为主要示意图。
    - 首次讲 SRAS 时先说明坐标轴：纵轴价格水平 P，横轴真实产出 Y。
    - 明确区分沿 SRAS 移动与 SRAS 整体移动。
  core_points_to_teach:
    - SRAS 表示短期内不同价格水平下企业愿意生产的真实产出。
    - SRAS 通常向右上倾斜，因为短期工资、合同和部分成本调整较慢，价格水平上升会暂时提高企业生产意愿。
    - 沿曲线移动来自价格水平变化。
    - SRAS 左移通常来自成本上升、负向供给冲击、供应链恶化；结果是在同一价格水平下产出更少，或同一产出需要更高价格。
    - SRAS 右移通常来自成本下降、供应链改善、短期生产效率提升；结果是在同一价格水平下产出更多，或同一产出对应更低价格。
watch_points:
  - 不把 SRAS 左移/右移解释为单纯沿着曲线走。
  - 后续再把 AD 与 SRAS 放在同一图中判断短期均衡。
student_state_update:
  next_teaching_move: explain SRAS, then ask a supply-shock classification question
```

### day3-t05 — sras_oil_shock_check

```yaml
phase: sras_check_oil_price_shock
score_type: formative_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生判断国际油价大幅上涨、运输和生产成本上升主要导致 SRAS 移动，并说明在同一价格水平下企业成本更高、愿意生产更少，因此 SRAS 左移。学生进一步指出现实中 AD 也可能受到影响：消费者购买意愿、企业投资意愿和政府购买都可能因为油价上涨而下降，因此 AD 也可能左移。对短期结果，学生能说出若只看 SRAS 左移，真实产出下降、价格水平上升；若 AD 也左移，价格水平结果取决于两种力量相对大小。
assessment:
  identify_primary_curve: 5/5
  sras_shift_direction: 5/5
  mechanism_cost_to_supply: 5/5
  short_run_baseline_result: 4.5/5
  extension_ad_possible_effect: 5/5
  expression_precision: 4/5
  total: 28.5/30
mastered:
  - 能把油价上涨识别为供给侧成本冲击，而不是单纯需求变化。
  - 能用“同一价格水平下企业愿意生产更少”解释 SRAS 左移。
  - 能区分考试简化模型中的 ceteris paribus 与现实中多条曲线可能同时移动。
  - 能判断 SRAS 左移、AD 不变时，短期真实产出下降、价格水平上升。
  - 能指出若 AD 同时左移，真实产出下降较确定，价格水平方向不确定。
watch_points:
  - 考试中若题目只说“油价上涨导致企业成本上升”，默认回答 SRAS 左移即可，不必强行加入 AD 变化。
  - 若题目明确说消费者支出和投资也下降，才加入 AD 左移，并说明价格结果取决于相对幅度。
  - “短期过程所以 SRAS 移动”可以更精确：不是因为短期就一定 SRAS 移动，而是因为题干直接改变了企业生产成本。
teaching_decision:
  action: reinforce_ceteris_paribus_and_move_to_ad_sras_joint_equilibrium
  reason: 学生已能识别供给冲击，并具备多曲线同时移动的直觉；下一步适合系统讲 AD-SRAS 短期均衡和常见冲击题。
student_state_update:
  sras_cost_shock_understanding: strong
  ceteris_paribus_awareness: developing
  next_teaching_move: teach joint AD-SRAS equilibrium using diagrams, then LRAS
```

#### 可写进卷面的修正版

如果题目只强调国际油价上涨使运输和生产成本上升，则主要是 SRAS 左移。因为在同一价格水平下，企业成本更高，愿意生产的真实产出减少。若 AD 不变，短期均衡通常表现为真实产出下降、价格水平上升。现实中油价上涨也可能抑制消费和投资，使 AD 同时左移；这时真实产出下降较确定，但价格水平取决于 SRAS 左移和 AD 左移的相对幅度。

#### 图像记录

- `/mnt/data/oil_shock_sras_ad_cases.png`

---

### day3-t06 — short_run_ad_sras_equilibrium_instruction

```yaml
phase: ad_sras_short_run_equilibrium
score_type: not_scored
prompt_visibility: student_requested_continue
student_request_summary: |
  学生要求继续学习。在上一轮油价冲击练习中，学生已能区分考试简化版 SRAS 左移与现实中 AD 也可能受拖累的扩展分析。
teaching_response_plan:
  action: teach_short_run_equilibrium_with_program_diagrams
  diagrams_created:
    - /mnt/data/ad_sras_short_run_equilibrium.png
    - /mnt/data/ad_sras_four_short_run_cases.png
  core_points:
    - AD-SRAS 短期均衡由 AD 与 SRAS 的交点决定。
    - 横轴为真实产出 Y，纵轴为价格水平 P。
    - 判断冲击题时先判断移动哪条曲线，再判断方向，最后看新旧交点比较。
    - AD 右移：Y 上升，P 上升。
    - AD 左移：Y 下降，P 下降。
    - SRAS 右移：Y 上升，P 下降。
    - SRAS 左移：Y 下降，P 上升。
watch_points:
  - 不要把“给定价格水平下的曲线移动方向”与“新均衡价格水平变化”混在一起。
  - 若题干同时给出 AD 和 SRAS 冲击，Y 或 P 可能出现不确定方向，需看两种冲击的相对强度。
next_teaching_move:
  - ask integrated short-run equilibrium check with one AD shock and one SRAS shock
```

---

### day3-t07 — visual_format_preference_and_ad_sras_equilibrium

```yaml
phase: ad_sras_short_run_equilibrium
score_type: not_scored
prompt_visibility: student_requested_continue_and_visual_format
student_request_summary: |
  学生要求继续讲 AD-SRAS，并指出后续讲课时应把生成的图片直接插入正文中，避免只给链接让学习者反复查找。
teaching_preference_update:
  curve_diagram_display: inline_in_lesson_body
  preferred_diagram_type: program_generated_png_or_authoritative_source
  ascii_diagrams: avoid_except_tiny_temporary_sketches
teaching_actions:
  - Created baseline AD-SRAS short-run equilibrium diagram.
  - Created four-panel short-run shock diagram covering AD left, AD right, SRAS left, SRAS right.
diagrams_created:
  - /mnt/data/ad_sras_short_run_equilibrium.png
  - /mnt/data/ad_sras_short_run_four_shocks.png
core_points:
  - AD-SRAS 短期均衡由 AD 与 SRAS 的交点决定。
  - 纵轴是价格水平 P，横轴是真实产出 Y。
  - AD 左移：Y 下降，P 下降。
  - AD 右移：Y 上升，P 上升。
  - SRAS 左移：Y 下降，P 上升。
  - SRAS 右移：Y 上升，P 下降。
watch_points:
  - 继续强调“判断曲线移动”与“判断新均衡结果”是两个步骤。
  - 后续图像应直接嵌入正文，提高图文对应度。
next_teaching_move:
  - Give integrated practice: distinguish AD shock vs SRAS shock and infer short-run Y/P changes.
```

### day3-t07 — AD right shift check: government infrastructure spending

```yaml
phase: ad_sras_short_run_check
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生判断政府增加基础设施支出属于需求侧变化，因为政府购买 G 增加，影响 AD 而非 SRAS。学生进一步判断 AD 右移，短期真实产出 Y 上升，价格水平 P 上升。
assessment:
  curve_identification: 10/10
  shift_direction: 10/10
  short_run_output_effect: 5/5
  short_run_price_effect: 5/5
  total: 30/30
mastered:
  - 能把政府购买增加归入 AD 侧变化。
  - 能用 Y = C + I + G + NX 解释 G 增加会使 AD 右移。
  - 能判断 AD 右移后短期均衡中 Y 上升、P 上升。
watch_points:
  - “基础设施支出”在短期 AD-AS 题中通常作为政府购买 G 增加处理；长期若提高资本存量和生产能力，才可能进一步影响 LRAS。
  - 答题时可补一句“企业生产技术暂时没有变化，所以 SRAS 不移动”。
teaching_decision:
  action: proceed_to_lras
  reason: AD 与 SRAS 的基础移动及短期均衡结果已基本稳定，可以进入 LRAS、潜在产出和短期/长期调整。
student_state_update:
  ad_shift_stability: strong
  ad_sras_short_run_equilibrium_stability: improving
  next_teaching_move: teach LRAS with diagram, axes, reasons for vertical shape, shifts, and relation to potential output
```

#### 可写进卷面的修正版

政府增加基础设施支出属于政府购买 G 增加，因此总需求增加，AD 曲线右移。题目说明企业生产技术暂时没有变化，所以 SRAS 不移动。短期内，新的 AD 与原 SRAS 在更高的真实产出和更高的价格水平处相交，因此真实产出 Y 上升，价格水平 P 上升。

### day3-t08 — LRAS introduction and long-run equilibrium

```yaml
phase: lras_core_teaching
score_type: not_scored
prompt_visibility: student_requested_continue
student_request_summary: |
  学生要求继续课程。在前一轮已经掌握 AD 右移的短期结果后，本轮进入 LRAS、潜在产出和长期均衡。
teaching_actions:
  - Created LRAS curve and shifts diagram.
  - Created AD-SRAS-LRAS long-run equilibrium diagram.
diagrams_created:
  - /mnt/data/lras_curve_and_shifts.png
  - /mnt/data/lras_long_run_equilibrium.png
core_points:
  - LRAS 表示长期总供给，也就是经济的潜在产出 Y*。
  - AD-AS 图中仍然使用同一坐标轴：纵轴价格水平 P，横轴真实产出 Y。
  - LRAS 画成竖线，因为长期真实产出主要由劳动力、资本、技术和生产率决定，而不是由价格水平本身决定。
  - LRAS 右移表示潜在产出提高，常见原因是资本积累、劳动力增加、技术进步、教育和生产率提高。
  - LRAS 左移表示潜在产出下降，常见原因是资源减少、资本破坏、灾害、长期制度或生产效率恶化。
  - 长期均衡中 AD、SRAS、LRAS 在同一点相交，实际产出等于潜在产出。
watch_points:
  - 不要把 LRAS 竖线理解为“价格不重要”；它的意思是长期真实产出不由价格水平本身决定。
  - 区分短期产出 Y 和潜在产出 Y*。
  - 后续讲长期调整时，要说明 SRAS 会因工资、成本、预期调整而移动。
teaching_decision:
  action: teach_output_gap_and_long_run_adjustment_next
  reason: LRAS 基本定义需要立即连接到 expansionary/recessionary gap，否则学生只会记住一条竖线而不理解长期调整。
student_state_update:
  lras_topic_status: in_progress
  next_teaching_move: ask check question after explaining LRAS and output gaps
```

### day3-t10 — output gaps and long-run adjustment teaching

```yaml
phase: output_gap_and_long_run_adjustment
score_type: not_scored
prompt_visibility: student_requested_continue_after_lras_check
teaching_actions:
  - Created output gap diagram for recessionary gap and expansionary gap.
  - Created long-run adjustment diagram showing SRAS right/down adjustment from recessionary gap and SRAS left/up adjustment from expansionary gap.
diagrams_created:
  - /mnt/data/output_gaps_recessionary_expansionary.png
  - /mnt/data/long_run_adjustment_output_gaps.png
core_points:
  - 产出缺口比较实际产出 Y 与潜在产出 Y*。
  - Y < Y* 是衰退性缺口，表示经济低于长期生产能力，通常有较高失业压力。
  - Y > Y* 是扩张性缺口，表示经济短期过热，通常有工资和通胀压力。
  - 在衰退性缺口中，工资和成本压力下降，SRAS 逐渐右移/下移，使 Y 回到 Y*，价格水平进一步下降。
  - 在扩张性缺口中，工资和成本压力上升，SRAS 逐渐左移/上移，使 Y 回到 Y*，价格水平进一步上升。
watch_points:
  - 学生需要区分“短期均衡 E1 不一定在 LRAS 上”和“长期均衡回到 Y*”。
  - 后续要注意不要把 LRAS 的移动与 SRAS 的长期调整混淆：长期调整通常是 SRAS 因工资/成本/预期变化而移动；LRAS 只有潜在产出变化时才移动。
  - 继续使用程序绘图，并在讲解正文中嵌入图片。
teaching_decision:
  action: ask output_gap_check
  reason: 产出缺口和长期调整需要立即通过题目检查，否则容易只记住方向表而不理解机制。
student_state_update:
  output_gap_topic_status: introduced
  next_teaching_move: give practice distinguishing Y relative to Y*, recessionary vs expansionary gap, and long-run SRAS adjustment
```

### day3-t12 — output_gap_long_run_adjustment_check

```yaml
phase: output_gap_long_run_adjustment_check
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生判断：消费和投资下降导致 AD 左移，短期均衡中 Y < Y*，这是衰退性缺口。学生指出衰退性缺口意味着资源没有充分利用、失业压力较大；若没有政策干预，长期中工资下降、成本下降，SRAS 向右移动，最终 Y 回到 Y*。
assessment:
  gap_identification: 5/5
  unemployment_resource_interpretation: 5/5
  wage_cost_adjustment: 5/5
  sras_adjustment_direction: 5/5
  long_run_output_result: 5/5
  total: 25/25
mastered:
  - 能准确识别 Y < Y* 为衰退性缺口。
  - 能把衰退性缺口与资源未充分利用和失业压力联系起来。
  - 能说明无政策干预下工资和成本压力下降。
  - 能判断 SRAS 会向右/向下移动。
  - 能说明长期实际产出回到潜在产出 Y*。
watch_points:
  - 后续需要加入价格水平结果：衰退性缺口自我调整时，SRAS 右移使 Y 回到 Y*，价格水平进一步下降。
  - 注意“工资下降”在现实中可能较慢、有黏性；考试模型里可写工资/成本压力下降。
teaching_decision:
  action: proceed_to_policy_response_or_integrated_ad_as_practice
  reason: 学生已能把 AD 左移、衰退性缺口、长期 SRAS 调整串联起来。下一步可加入政策干预，或先做 AD-AS 综合识别题。
student_state_update:
  output_gap_and_long_run_adjustment_stability: strong
  day3_core_status: mostly_stable
  next_teaching_move: introduce policy response in AD-AS or run integrated practice
```

#### 可写进卷面的修正版

消费和投资下降使 AD 左移，短期均衡产出低于潜在产出，即 \(Y < Y^*\)，所以这是衰退性缺口。衰退性缺口说明资源没有充分利用，失业压力较大。若没有政策干预，长期中工资和成本压力会下降，SRAS 逐渐右移/下移，使实际产出回到潜在产出 \(Y^*\)，价格水平进一步下降。

### day3-t13 — policy response teaching

```yaml
phase: policy_response_in_ad_as
score_type: not_scored
prompt_visibility: student_requested_continue
diagram_created:
  - /mnt/data/policy_closing_output_gaps.png
teaching_actions:
  - Introduced expansionary policy response to recessionary gap.
  - Introduced contractionary policy response to expansionary gap.
  - Kept discussion at AD-AS graph level; detailed monetary policy instruments reserved for later lesson.
core_points:
  - 政策干预的核心图像是移动 AD，使短期产出更快回到 Y*。
  - 衰退性缺口 Y < Y* 时，可用扩张性政策提高总需求，使 AD 右移；短期结果是 Y 上升、P 上升。
  - 扩张性缺口 Y > Y* 时，可用紧缩性政策降低总需求，使 AD 左移；短期结果是 Y 下降、P 下降。
  - 财政政策例子：政府购买、税收、转移支付影响 C/G/I，从而影响 AD。
  - 货币政策例子：利率和信贷条件影响消费、投资和净出口，从而影响 AD；具体机制后续课程展开。
watch_points:
  - 不要把“政策让经济回到 Y*”误解成 LRAS 移动；短期稳定政策通常通过 AD 移动改变短期均衡。
  - 注意政策取舍：刺激需求可提高 Y，但也可能提高 P；压低需求可降低 P，但也会降低 Y。
  - 继续把图插入讲课正文，避免只给链接。
teaching_decision:
  action: ask_policy_response_check
  reason: 需要检查学生是否能根据产出缺口选择扩张性或紧缩性政策，并判断 AD 方向与 Y/P 结果。
student_state_update:
  policy_response_topic_status: introduced
  next_teaching_move: practice policy response for recessionary and expansionary gaps
```

### day3-t14 — policy_depth_deferred_to_day4

```yaml
phase: scope_adjustment
score_type: not_scored
prompt_visibility: student_initiated_scope_control
student_request_summary: |
  学生指出政府干预有很多结合现实需要讨论的内容，建议把这一部分纳入明天课程。
teaching_decision:
  action: defer_policy_applications_to_day4
  reason: |
    Day 3 的核心任务是 AD、SRAS、LRAS、产出缺口和长期调整。政策干预的现实讨论涉及财政政策、货币政策、利率传导、政策时滞、预期、通胀与失业取舍、财政赤字和资产价格等内容，适合放入 Day 4 或后续政策主题中系统展开。
updated_plan:
  day3_remaining_focus:
    - consolidate AD/SRAS/LRAS curve identification
    - consolidate short-run equilibrium and output gap logic
    - run integrated Day 3 practice or quiz
  day4_bridge:
    - policy intervention in AD-AS
    - expansionary vs contractionary policy
    - fiscal policy and monetary policy channels
    - policy lags and tradeoffs
    - link to market reactions if useful
student_state_update:
  policy_response_topic_status: introduced_but_deferred
  next_teaching_move: return_to_day3_core_review_or_integrated_practice
```

### day3-t?? — policy_scope_adjustment_and_integrated_practice_start

```yaml
phase: scope_control_and_integrated_practice
score_type: not_scored_yet
prompt_visibility: student_prompt_only
student_request_summary: |
  学生指出政府干预有很多结合实际的问题需要讨论，建议将政策干预部分纳入明天课程。
teaching_decision:
  action: defer_policy_details_to_day4
  reason: |
    Day 3 主线应先巩固 AD、SRAS、LRAS、短期均衡、产出缺口与长期自我调整。政策干预的现实取舍、时滞、财政与货币政策传导、资产价格影响等内容更适合在 Day 4 单独展开。
current_teaching_move: |
  启动 Day 3 综合练习；不引入政策干预，只检查曲线移动、短期结果、产出缺口和长期自我调整。
```

### day3-t?? — assessment_prompt_design_rule_update

```yaml
phase: assessment_design_update
score_type: not_scored
prompt_visibility: meta_instruction_from_student
student_request_summary: |
  学生提醒：出题时不要在题干中提示答案。
teaching_decision:
  action: use_blind_assessment_prompts
  rule: |
    后续检查题和综合练习题应避免在题干中暗示曲线名称、移动方向、缺口类型或结果方向。题干只给经济情境和需要回答的任务，不使用“需求侧/供给侧”“衰退性/扩张性”“成本冲击”等会直接提示答案的词，除非题目专门考术语识别后的辨析。
implementation_notes:
  - 题干给事实，不给分类词。
  - 先让学生判断移动哪条曲线，再判断方向和结果。
  - 作答前不展示评分细则或标准答案。
  - 评分后再给修正版卷面表达。
student_state_update:
  assessment_preference: blind_prompts_without_answer_cues
  next_teaching_move: run_day3_integrated_practice_with_neutral_wording
```

### day3-t19 — comprehensive_practice_prompt

```yaml
phase: day3_comprehensive_practice
score_type: pending_student_answer
prompt_visibility: student_prompt_only_no_answer_hints
student_request_summary: |
  学生要求出 Day 3 综合练习题，并提醒题干中不要提示答案。
teaching_decision:
  action: provide_blind_comprehensive_practice
  rule: |
    题干避免直接出现 AD/SRAS/LRAS 左移右移、需求侧/供给侧、衰退性缺口/扩张性缺口等提示性词语。
  scope:
    - curve identification
    - shift direction
    - short-run Y and P
    - output gap
    - long-run self-adjustment
    - no policy intervention details today
state_update:
  awaiting_student_answer: true
```


### day3-t20 — comprehensive_practice_student_answer

```yaml
phase: day3_comprehensive_practice
score_type: blind_score
prompt_visibility: student_answer_review
student_answer_summary: |
  学生完成 5 道 Day 3 综合练习。题 1 能正确判断居民悲观、消费下降、设备投资推迟会使 AD 左移，短期 Y 与 P 下降，并形成衰退性缺口；长期工资和成本下降，SRAS 右移，Y 回到 Y*。题 2 能正确判断进口能源价格大涨使企业成本上升，SRAS 左移，短期 Y 下降、P 上升；但长期调整误写为工资上升和 AD 右移。题 3 能正确判断消费、投资、出口旺盛使 AD 右移，短期 Y 上升，并判断 Y > Y*、长期工资成本上升导致 SRAS 左移；但短期价格水平误写为下降，正确应为上升。题 4 能正确判断长期教育改善、技术进步和资本积累使 LRAS 右移，潜在产出上升。题 5 能正确判断自然灾害短期使 SRAS 左移，若长期生产能力受损则 LRAS 左移，短期 P 上升；但短期 Y 下降表达不够明确，长期价格水平不宜简单判断为会降回来。
assessment:
  q1_ad_left_recessionary_gap_adjustment: 20/20
  q2_energy_cost_sras_left_long_run_adjustment: 13/20
  q3_boom_ad_right_expansionary_gap: 16/20
  q4_growth_lras_right: 15/15
  q5_disaster_short_and_long_run_supply: 15/20
  total: 79/95
  percentage: 83
mastered:
  - 能从消费、投资、出口等支出项目识别 AD 变化。
  - 能从企业成本、能源价格、自然灾害等因素识别 SRAS 变化。
  - 能从技术、教育、资本积累识别 LRAS 右移。
  - 能识别 Y < Y* 为衰退性缺口，Y > Y* 为扩张性缺口。
  - 能说明衰退性缺口中工资成本下降、SRAS 右移；扩张性缺口中工资成本上升、SRAS 左移。
watch_points:
  - AD 右移时，短期通常是 Y 上升、P 上升，不是 P 下降。
  - 负向供给冲击后，若短期 Y < Y*，长期自我调整通常来自工资和成本压力下降，使 SRAS 逐步右移；AD 不会因为自然调整而自动右移。
  - 自然灾害题若同时有短期生产受阻和长期生产能力受损，应分开写：短期 SRAS 左移；长期 LRAS 左移。
  - 长期价格水平要看最终 AD、SRAS、LRAS 的相对位置，不要在没有图或条件时直接断定“一定降回来”。
teaching_decision:
  action: repair_q2_q3_then_continue_to_day3_quiz_or_summary
  reason: 综合练习达到继续标准，但两个核心结果方向需要立即修正。
student_state_update:
  day3_integrated_practice_score: 79/95
  ad_sras_lras_core_stability: mostly_stable
  main_repair_items:
    - AD right shift raises both Y and P in short-run baseline.
    - Supply-shock recession long-run adjustment is SRAS right/down via lower wage/cost pressure, not AD right.
```

#### 修正版要点

1. 题 1：居民悲观、消费和投资下降 → AD 左移 → 短期 Y 下降、P 下降 → Y < Y*，衰退性缺口 → 长期工资成本下降，SRAS 右移，Y 回到 Y*。
2. 题 2：能源价格上涨、企业成本上升 → SRAS 左移 → 短期 Y 下降、P 上升。若形成 Y < Y* 且没有政策干预，长期失业压力会降低工资和部分成本压力，SRAS 逐步右移/回调，Y 回到 Y*；不是 AD 自动右移。
3. 题 3：消费、投资、出口增加 → AD 右移 → 短期 Y 上升、P 上升 → Y > Y*，扩张性缺口 → 长期工资成本上升，SRAS 左移，Y 回到 Y*。
4. 题 4：教育改善、技术进步、资本积累 → LRAS 右移 → Y* 上升。
5. 题 5：灾害短期破坏生产和抬高成本 → SRAS 左移 → 短期 Y 下降、P 上升；若长期生产能力受损 → LRAS 左移，Y* 下降。
```

### day3-t21 — final_learning_record_compiled

```yaml
phase: record_compilation
score_type: not_scored
prompt_visibility: student_requested_record
student_request_summary: |
  学生表示今天到这里，并要求整理今天的学习进度报告。
record_actions:
  - Created Day 3 learning record markdown: /mnt/data/day-3-macroeconomics-learning-record.md.
  - Preserved Day 3 integrated practice score: 79/95.
  - Marked Day 3 status as completed_core_without_formal_final_quiz.
  - Recorded policy intervention as introduced_but_deferred_to_day4.
  - Added teaching preferences: program-generated or authoritative diagrams; insert images inline; avoid ASCII except trivial sketches.
  - Added assessment preference: blind prompts without answer cues in the question stem.
student_state_update:
  current_day: 4
  completed_sessions: 3
  pass_readiness: improving
  risk_level: medium
  day3_status: completed_core_without_formal_final_quiz
  next_action: run_day_4
  day4_start_watch_points:
    - AD right shift raises both Y and P in short-run baseline.
    - Negative supply shock with Y < Y* adjusts through lower wage/cost pressure and SRAS right/down, not automatic AD right.
    - Labor force participation rate = labor force / adult population, not employed / adult population.
```
