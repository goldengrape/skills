---
type: Teacher Notebook
title: Day 2 Teacher Notebook — CPI、通胀与失业
description: Day 2 对话同步记录；作答前不展示隐藏评分细则或参考答案。
tags: [teacher-notebook, macroeconomics, day-2, sync]
timestamp: 2026-07-01T00:00:00-07:00
visibility_note: student_safe_copy_before_assessment
---

# Day 2 Teacher Notebook — CPI、通胀与失业

```yaml
course: 宏观经济学 7 天 Crash Course
day: 2
status: completed_with_extensions
session_date: 2026-07-01
time_policy: soft
source_skill: macro_crash_course_teaching_skill_round4_updated
student_level: zero_basis_but_day1_stable
notebook_mode: append_only_sync
prompt_visibility_rule: 作答前只展示题目、格式和中性提醒；不展示隐藏评分细则或参考答案。
```

## 0. 已读取材料

- `SKILL.md`
- `state/current-state.md`
- `state/next-action.md`
- `state/recall-deck.md`
- `state/misconceptions.md`
- `state/score-history.md`
- `sessions/day-1-session.md`
- `learning-records/day-1-macroeconomics-learning-record.md`
- `teacher/teacher-notebook.md`
- `teacher/teaching-protocol.md`
- `teacher/visibility-rules.md`
- `teacher/time-policy.md`
- `plan/day-2.md`
- `quizzes/day-2-quiz.md`
- `teacher/rubrics/day-2-rubric.md`
- `teacher/answer-keys/day-2-answer-key.md`
- `state/interest-ledger.md`

## 1. Day 1 带入 Day 2 的状态

```yaml
prior_day: 1
prior_quiz_score: 38/40
prior_status: completed
current_day: 2
next_action: run_day_2
strong_areas:
  - GDP definition
  - final goods and value added
  - nominal GDP vs real GDP
  - GDP deflator
  - inventory investment
  - GDP vs GNP
watch_points:
  - 不要把 GDP deflator 指数本身说成通胀率
  - 不要把“国内”误解成按国籍统计
  - Day 2 重点检查“不工作的人是否都算失业”
```

## 2. Day 2 学习目标

学生完成本节后，应能用考试语言解释：

- CPI 与 inflation rate 的关系。
- CPI 与 GDP deflator 的区别。
- purchasing power 与通胀的关系。
- unemployment rate 的分子、分母。
- labor force 与 non-labor-force 的区别。
- discouraged workers 为什么会让失业率下降看起来“更好”，但实际就业市场未必改善。

## 3. 教学流程

| 阶段 | 学生可见动作 | 记录动作 |
|---|---|---|
| Recall | 先回答 Day 1 回忆题 | 记录是否能无提示回忆 GDP、GDP deflator vs CPI、GDP vs GNP、库存投资 |
| Map | 定位 Day 2 属于宏观指标 | 记录是否能把 CPI / unemployment 放入“经济体体检表” |
| Core | 讲 CPI、通胀、购买力、失业率、劳动力、灰心工人 | 记录概念稳定度与例子 |
| Feynman | 6 句话讲给没学过的人 | 记录表达是否可写进卷面 |
| Exam practice | 失业率下降是否一定说明就业改善 | 作答后评分并更新错因 |
| State update | 总结、测验、更新回忆卡 | 更新本 notebook 与学习记录 |

## 4. Append-Only Turn Log

### day2-t00 — session_start

```yaml
phase: state_reading_and_setup
teacher_says:
  - 已读取 Day 1 学习记录、当前状态、Day 2 计划、测验与教师侧规则。
  - Day 2 从 5 分钟回忆开始，然后进入 CPI、通胀率、失业率。
teacher_thinks_summary_for_student_safe_copy:
  task_goal: 启动 Day 2，并保留 blind assessment 的可见性边界。
  hidden_details_status: 作答前不在此学生安全副本中展开隐藏评分细则或参考答案。
engagement_observation:
  interest_level: high
  attention_signal: stable
  evidence:
    - 学习者主动要求详细阅读 skill，并要求同步教师 notebook。
teaching_decision:
  action: start_with_recall
  reason: Day 1 分数高，可以进入 Day 2；但 7 天速成需要先做检索练习。
state_updates:
  - Day 2 notebook created.
  - status set to in_progress.
```

## 5. 待更新区

后续每次你回答后，会追加：

- 你的原始回答摘要。
- 掌握点。
- 遗漏点。
- 混淆点。
- 修正版考试表达。
- 是否新增 recall card。
- 是否更新 misconception。
- 阶段性分数及 `score_type`。

### day2-t01 — recall_check_student_answer

```yaml
phase: recall_check
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary:
  q1_gdp_deflator_vs_cpi: |
    学生指出 GDP deflator 关注生产，CPI 关注消费；CPI 是居民购买篮子的价格变化；GDP deflator = nominal GDP / real GDP。中途出现“GDP deflator 会包含价格和产量同时”的表述，但马上自我修正为价格变化。
  q2_gdp_vs_gnp: |
    学生指出 GDP 看境内，GNP 看国籍/国家；外国投资在国内生产计入 GDP 不计入 GNP，本国海外生产所得不计入 GDP 但计入 GNP。
  q3_inventory_investment: |
    学生指出库存增加为正，从库存里取出销售为负。
  q4_nominal_real: |
    学生指出 nominal GDP 同时受价格和产量影响，名义上升可能只是通胀，不一定代表真实产出上升；也补充真实产出可能上升、下降或不变。
assessment:
  q1: 4.5/5
  q2: 4.5/5
  q3: 4.5/5
  q4: 5/5
  total: 18.5/20
mastered:
  - 能从生产范围与消费范围区分 GDP deflator 和 CPI。
  - 能用境内生产 vs 本国居民/国民收入归属区分 GDP 和 GNP。
  - 能说明库存增加为正投资、库存减少为负投资。
  - 能准确说明 nominal GDP 同时受价格和产量影响。
watch_points:
  - GNP 不宜只说“国籍”，考试中更稳的说法是“本国居民/本国生产要素的收入归属”。
  - CPI 要强调固定消费篮子；inflation rate 是 CPI 或价格指数的百分比变化。
  - GDP deflator 虽由 nominal GDP / real GDP 得出，但它本身是价格指数，不是产量指标。
  - 库存投资应说“当期生产未售出使库存增加”为正，“销售过去库存使库存减少”为负。
student_state_update:
  day1_recall_stability: strong
  readiness_to_start_day2_core: yes
  next_teaching_move: teach CPI, inflation rate, purchasing power, then unemployment definitions
```

#### 可写进卷面的修正版

1. GDP deflator 衡量一国境内生产的所有最终产品和服务的价格水平，CPI 衡量居民购买的固定消费篮子的价格水平。GDP deflator 包括投资品、政府购买和出口品，但不包括进口品；CPI 包括居民购买的进口消费品，但不包括企业投资品和出口品。
2. GDP 看生产地点，统计一国境内生产的最终产品和服务；GNP 更看收入归属，统计本国居民或本国生产要素获得的生产收入。
3. 当期生产但未卖出的产品进入库存，库存投资为正；当期销售过去生产的库存，库存减少，库存投资为负。
4. nominal GDP 用当年价格计算，受价格和产量共同影响。因此 nominal GDP 上升可能来自产量增加，也可能来自价格上涨；只有剔除价格变化后的 real GDP 上升，才更能说明真实产出增加。

### day2-t02 — cpi_calculation_practice_1

```yaml
phase: cpi_calculation
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生以 2025 年为基准年，正确计算 2025 CPI = 200/200×100 = 100；2026 CPI = 230/200×100 = 115。计算通胀率时一开始口误写成 130-100，随即自我修正为 115-100，再除以 100，得到 0.15。
assessment:
  cpi_2025: 3/3
  cpi_2026: 3/3
  inflation_rate: 3.5/4
  total: 9.5/10
mastered:
  - 能正确使用固定消费篮子与基准年计算 CPI。
  - 能把基准年 CPI 设为 100。
  - 能用 CPI 的百分比变化计算通胀率。
watch_points:
  - 最后答案应写成 15%，不要只写 0.15。
  - 计算中出现口误时，要在最终答案中只保留修正后的数值，避免阅卷人误判。
teaching_decision:
  action: proceed_to_cpi_biases
  reason: CPI 基础计算稳定，可以进入 CPI 的局限性与真实购买力解释。
student_state_update:
  cpi_formula_stability: strong
  inflation_rate_formula_stability: mostly_stable
  next_teaching_move: explain CPI biases: substitution bias, new goods, quality change, outlet/sample limits
```

#### 可写进卷面的修正版

以 2025 年为基准年，2025 年 CPI = 200 / 200 × 100 = 100。2026 年 CPI = 230 / 200 × 100 = 115。2026 年相对 2025 年的通胀率 = (115 - 100) / 100 × 100% = 15%。

### day2-t03 — cpi_substitution_bias_check

```yaml
phase: cpi_bias_understanding
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生指出固定消费篮子中各商品数量不变，因此牛肉价格大涨会使 CPI 上升；但现实家庭会少买牛肉、多买鸡肉，实际消费结构与固定篮子不同。学生用“同样蛋白摄入”的例子说明鸡肉可部分替代牛肉，因此实际支出可能低于固定篮子支出，CPI 会高估真实生活成本上涨。
assessment:
  substitution_mechanism: 5/5
  fixed_basket_explanation: 4.5/5
  concrete_example: 5/5
  exam_expression_concision: 4/5
  total: 18.5/20
mastered:
  - 能准确说明固定篮子数量不变是替代偏误的来源。
  - 能把相对价格变化与消费者替代行为联系起来。
  - 能用牛肉、鸡肉、蛋白摄入的具体例子解释为什么实际生活成本上涨可能低于 CPI 显示的上涨。
watch_points:
  - 考试表达可以更短，避免“家庭的固定篮子的这个家庭的这个消费支出”等重复口语。
  - 需要明确写出术语：substitution bias / 替代偏误。
teaching_decision:
  action: proceed_to_next_cpi_bias_check_then_unemployment
  reason: 替代偏误理解稳定，可以继续用一个新产品或质量变化题巩固 CPI 局限，再进入失业率。
student_state_update:
  cpi_bias_substitution_stability: strong
  next_teaching_move: ask quality/new goods bias mini-check or move to unemployment depending on pace
```

#### 可写进卷面的修正版

固定篮子的 CPI 可能高估真实生活成本上涨，因为它假设消费者仍按原来的数量购买牛肉和鸡肉。但现实中牛肉相对鸡肉变贵后，家庭会少买牛肉、多买鸡肉，用较便宜的商品替代较贵的商品。因此，实际家庭维持类似生活水平所需的支出，可能低于固定篮子计算出来的支出。这就是 CPI 的替代偏误。

### day2-t04 — cpi_quality_change_bias_check

```yaml
phase: cpi_bias_understanding
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生指出手机名义价格从 5000 到 6000 虽然上涨 20%，但今年手机的电池、存储、摄像头和处理器都有改善，因此不能把价格变化全部视为同等质量商品的真实涨价。学生进一步主动构造蛋白粉和电池例子：一罐蛋白粉价格上涨 20%，但蛋白含量从每 100 克 50 克提高到 70 克；或电池价格上涨 20%，但容量提高 40%，说明单位有效服务价格未必上涨。
assessment:
  quality_change_mechanism: 5/5
  cpi_same_item_vs_same_quality: 5/5
  concrete_example_design: 5/5
  exam_expression_concision: 4/5
  total: 19/20
mastered:
  - 能准确指出 CPI 应尽量比较同等质量商品的价格，而不是只比较同名商品价格。
  - 能说明质量提高会使观察到的价格上涨不能完全等同于真实价格上涨。
  - 能主动设计“单位有效服务价格”的例子，蛋白粉和电池例子尤其清楚。
watch_points:
  - 考试表达需要压缩，先给定义，再给一例，不要同时展开太多例子。
  - “可能下降了”需要明确说明下降的是单位有效服务价格，不是总价。
teaching_decision:
  action: proceed_to_unemployment_core
  reason: CPI 计算与 CPI 偏误已基本稳定；Day 2 还需完成失业率、劳动力、灰心工人。
student_state_update:
  cpi_quality_bias_stability: strong
  cpi_bias_overall: stable
  next_teaching_move: teach labor force, unemployment rate, labor force participation, discouraged workers
```

#### 可写进卷面的修正版

不能简单说手机价格真实上涨了 20%，因为今年的手机质量也提高了。CPI 想衡量的是同等质量商品的价格变化；如果电池、存储、摄像头和处理器都改善了，那么 6000 元买到的服务量高于去年 5000 元的手机。观察到的总价格上涨中，一部分可能反映质量提高，而不是真正的同质商品价格上涨。这就是质量变化带来的 CPI 衡量困难。

#### 教师备注

学生主动提出的蛋白粉例子很适合保留：若一罐蛋白粉价格从 100 元涨到 120 元，但每 100 克蛋白含量从 50 克提高到 70 克，则总价上涨不等于“每单位蛋白”的价格上涨。这个例子能帮助学生理解“单位有效服务价格”。

### day2-t05 — unemployment_rate_calculation

```yaml
phase: unemployment_core_calculation
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生正确识别就业者 120 人和正在找工作的失业者 20 人属于劳动力；全职学生、退休者和已经放弃找工作的灰心工人不属于劳动力。计算劳动力为 140 人，失业人数为 20 人，失业率为 20 / 140 = 1/7 ≈ 14.28%。
assessment:
  labor_force_identification: 5/5
  unemployed_definition: 5/5
  discouraged_worker_exclusion: 5/5
  calculation_accuracy: 5/5
  total: 20/20
mastered:
  - 能准确使用 labor force = employed + unemployed。
  - 能准确判断 unemployed 是“没有工作但正在找工作”的人。
  - 能把全职学生、退休者和灰心工人排除在劳动力之外。
  - 能正确计算失业率。
watch_points:
  - 考试答案中建议写成 14.3%，保留一位小数即可。
  - 后续需要检查 labor force participation rate 与 unemployment rate 的区别。
teaching_decision:
  action: proceed_to_labor_force_participation_and_discouraged_workers
  reason: 失业率核心公式和分类判断稳定；下一步讲劳动参与率、灰心工人如何影响官方失业率。
student_state_update:
  unemployment_rate_formula_stability: strong
  labor_force_classification_stability: strong
  next_teaching_move: explain labor force participation rate and discouraged worker effect
```

#### 可写进卷面的修正版

劳动力 = 就业者 + 失业者 = 120 + 20 = 140 人。失业人数是没有工作但正在找工作的人，所以是 20 人。失业率 = 20 / 140 × 100% ≈ 14.3%。全职学生、退休者和已经放弃找工作的灰心工人没有在找工作，因此不计入劳动力，也不计入失业人数。

### day2-t06 — discouraged_worker_effect_check

```yaml
phase: unemployment_interpretation
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生指出，当经济很差时，原本“失业且正在找工作”的人如果放弃找工作，就不再被计入失业人数，也不再计入劳动力。由于失业率的分子和分母同时减少，且通常分子减少会使失业率下降，因此官方失业率可能下降。学生进一步指出，这可能误导我们以为就业市场改善，但实际上就业市场可能恶化。
assessment:
  discouraged_worker_definition: 5/5
  numerator_denominator_mechanism: 5/5
  interpretation_warning: 5/5
  mathematical_precision: 4.5/5
  total: 19.5/20
mastered:
  - 能准确说明灰心工人从 unemployed 变为 not in labor force。
  - 能解释官方失业率可能下降，并不是因为就业人数增加。
  - 能指出官方失业率下降可能掩盖就业市场恶化。
  - 能主动用分子、分母变化解释机制。
watch_points:
  - “如果失业率不是百分之百就一定下降”这个数学判断基本方向对，但考试中不必展开；更稳妥说法是“在就业人数不变、部分失业者退出劳动力时，失业率会下降”。
  - 需要同时提及劳动参与率可能下降，这能更完整地识别就业市场恶化。
teaching_decision:
  action: introduce_labor_force_participation_contrast_then_types_of_unemployment
  reason: 灰心工人机制已稳定；下一步应把 unemployment rate 与 labor force participation rate 放在一起，再进入自然失业、周期性失业等解释。
student_state_update:
  discouraged_worker_effect_stability: strong
  unemployment_interpretation_stability: strong
  next_teaching_move: teach labor force participation contrast and unemployment types
```

#### 可写进卷面的修正版

如果很多正在找工作的失业者放弃找工作，他们会从“失业者”变成“非劳动力人口”。这会使失业人数减少，同时劳动力总数也减少；在就业人数没有增加的情况下，官方失业率可能下降。但这并不说明就业市场改善，因为下降的原因不是更多人找到了工作，而是更多人退出了劳动力市场。此时还应观察劳动参与率；如果劳动参与率下降，说明就业市场可能仍然很弱。

#### 教师备注

学生已经能用分子和分母解释失业率变化，理解深度高于 Day 2 基础要求。后续重点转为考试表达压缩：先判断、再原因、最后指出误导风险和劳动参与率。

### day2-t07 — unemployment_types_classification

```yaml
phase: unemployment_types
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生正确判断：大学毕业生花两个月找第一份工作属于摩擦性失业，因为找工作和匹配需要时间；传统制造业岗位减少、工人技能不适合新兴行业属于结构性失业，因为技能不匹配，需要重新培训；经济衰退导致订单下降和裁员增加属于周期性失业，因为总需求不足。
assessment:
  frictional_unemployment: 5/5
  structural_unemployment: 5/5
  cyclical_unemployment: 5/5
  total: 15/15
mastered:
  - 能用“找工作需要时间”识别摩擦性失业。
  - 能用“技能、行业或地区不匹配”识别结构性失业。
  - 能用“经济衰退、订单下降、总需求不足”识别周期性失业。
watch_points:
  - 后续混合题中需注意：同一情境可能同时有结构性和周期性因素，考试要根据题目强调的原因判断。
  - 回答失业类型题时，建议固定句式：先判断类型，再写造成失业的直接原因。
teaching_decision:
  action: give_mixed_classification_and_then_feynman_summary
  reason: 三类失业基础识别稳定，可以用混合场景检查是否会被关键词误导，然后进入 Day 2 综合复述。
student_state_update:
  unemployment_types_stability: strong
  next_teaching_move: ask mixed unemployment classification question, then six-sentence Feynman output for CPI + unemployment
```

#### 可写进卷面的修正版

大学毕业生花两个月找第一份工作属于摩擦性失业，因为劳动者与岗位匹配需要时间。传统制造业岗位减少、工人技能不适合新兴行业属于结构性失业，因为劳动者技能与岗位需求不匹配。经济衰退导致企业订单下降和裁员增加属于周期性失业，因为总需求不足使企业减少用工。

### day2-t08 — mixed_unemployment_classification

```yaml
phase: unemployment_types_mixed_context
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生正确判断：经济衰退导致居民买车减少、订单下降、短期裁员增加，主要属于周期性失业；几年后新能源汽车和自动化普及，传统零件工人的技能不适合新岗位，很多人长期找不到工作，主要属于结构性失业。
assessment:
  cyclical_component: 5/5
  structural_component: 5/5
  reason_precision: 5/5
  total: 15/15
mastered:
  - 能在同一行业场景中区分短期总需求不足与长期技能错配。
  - 能说明周期性失业的直接原因是经济衰退、需求下降、企业减少用工。
  - 能说明结构性失业的直接原因是技能与新岗位需求不匹配。
watch_points:
  - 考试中若题干同时出现 recession 和 technology change，应按题目问的时期与直接原因分类。
  - 建议保持“主要属于”的表述，避免把复杂现实说成只有单一原因。
teaching_decision:
  action: proceed_to_day2_integrated_recall
  reason: 三类失业与混合场景分类稳定；可以进入 Day 2 综合输出与小测。
student_state_update:
  unemployment_types_mixed_stability: strong
  day2_readiness_for_final_quiz: high
  next_teaching_move: integrated CPI, inflation, unemployment summary and final quiz
```

#### 可写进卷面的修正版

第 1 种主要属于周期性失业，因为经济衰退使居民买车减少，企业订单下降，短期内减少用工。第 2 种主要属于结构性失业，因为新能源汽车和自动化改变了岗位需求，传统零件工人的技能与新岗位不匹配，导致长期失业。

### day2-t09 — integrated_cpi_unemployment_summary

```yaml
phase: integrated_recall_feynman_output
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生用较完整的一段话串联了 CPI、固定消费篮子、基准年、通胀率、购买力、CPI 偏误、失业率、劳动力、灰心工人以及三类失业。CPI 计算例子中能正确说明以 2025 年为基准，2026 年 CPI = 110，2027 年 CPI = 120，并准确指出 2027 年相对 2026 年的通胀率为 10/110 ≈ 9.09%，不是简单的 10%。CPI 偏误部分覆盖新产品、替代偏误和质量变化。失业率部分能说明失业率 = 失业人口 / 劳动力，并能解释灰心工人不计入失业人口以及失业率可能被误读。三类失业分类准确。
assessment:
  cpi_definition_and_formula: 9/10
  inflation_rate_calculation: 10/10
  purchasing_power: 4.5/5
  cpi_biases: 14/15
  unemployment_rate_formula: 7/10
  discouraged_worker_interpretation: 8.5/10
  unemployment_types: 15/15
  expression_structure: 7/10
  total: 75/85
mastered:
  - 能用固定消费篮子和基准年解释 CPI。
  - 能区分 CPI 水平与通胀率，并能正确计算连续年份通胀率。
  - 能说明 CPI 上升通常意味着同样金额货币购买力下降。
  - 能解释 CPI 的替代偏误、新产品偏误和质量变化偏误。
  - 能准确区分摩擦性、结构性和周期性失业。
  - 能理解灰心工人会使官方失业率产生误导。
watch_points:
  - “CPI 是购买固定消费篮子的价值/价格”应改为“CPI 是固定消费篮子价格相对基准年的指数”。
  - 劳动力不能说成所有有劳动能力或 16-64 岁的人；劳动力 = 就业者 + 没有工作但正在找工作的人。
  - 全职学生、不找工作者、退休者、灰心工人虽然可能处于成年人口或工作年龄人口中，但不属于劳动力。
  - 灰心工人不是单纯“不想找工作的人”，而是想工作、曾经找工作，但因长期找不到而停止寻找的人。
  - “劳动人口”“劳动力人口”“劳动年龄人口”容易混用，后续需要固定术语。
  - 综合表达过长，需要练习考试版 120-180 字压缩。
teaching_decision:
  action: correct_labor_force_concept_then_final_day2_quiz
  reason: Day 2 主体内容已覆盖；唯一核心风险是 labor force 与 working-age/adult population 的混淆。先修正，再进行 Day 2 终测。
student_state_update:
  cpi_core_stability: strong
  cpi_bias_stability: strong
  unemployment_types_stability: strong
  labor_force_definition_stability: needs_repair
  day2_readiness_for_final_quiz: mostly_ready_after_labor_force_repair
```

#### 可写进卷面的修正版：综合版

CPI 是固定消费篮子价格相对基准年的指数，通胀率是 CPI 从一期到下一期的百分比变化。CPI 上升通常意味着消费者购买同一篮子商品和服务需要花更多钱，因此货币购买力下降。但 CPI 不是完美的生活成本指标，因为固定篮子不能充分反映消费者替代行为，新产品带来的选择增加也不一定能及时反映，质量变化也很难完全调整。失业率 = 失业人数 / 劳动力 × 100%，其中劳动力 = 就业者 + 没有工作但正在找工作的人。灰心工人已经停止找工作，因此不计入失业人数和劳动力；如果灰心工人增加，官方失业率可能下降，但就业市场未必改善。摩擦性失业来自找工作和匹配需要时间，结构性失业来自技能、地区或行业不匹配，周期性失业来自经济衰退和总需求不足。

#### 新增 misconception

```text
Misconception: 劳动力 = 所有有劳动能力的人，或 16-64 岁的人。
Correction: 宏观统计中的劳动力通常指就业者 + 正在找工作的失业者。工作年龄人口或成年人口是更大的概念；全职学生、退休者、不找工作者、灰心工人不属于劳动力。
Status: needs_repair
Source: day2-t09 integrated summary
```

#### 新增 recall cards

```text
Q: 劳动力、成年人口、工作年龄人口有什么区别？
A: 劳动力 = 就业者 + 正在找工作的失业者；成年人口或工作年龄人口是更大的统计范围，其中包括全职学生、退休者、不找工作者等非劳动力人口。
Due: next_session
Source: day2-t09
```

```text
Q: 灰心工人为什么不计入官方失业人数？
A: 因为官方失业者要求“没有工作但正在找工作”。灰心工人想工作，但因长期找不到而停止寻找，所以被归入非劳动力人口。
Due: next_session
Source: day2-t09
```

### day2-t10 — labor_force_repair_check

```yaml
phase: concept_repair_check
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生正确计算成年人 100 人情境：60 人有工作，10 人没有工作但正在找工作，20 人全职上学不找工作，10 人放弃找工作。学生明确成年人口为 100，劳动力为 60 + 10 = 70，失业人数为 10，失业率为 10 / 70 = 14.28%。
assessment:
  adult_population: 5/5
  labor_force_definition_application: 10/10
  unemployed_definition_application: 5/5
  unemployment_rate_calculation: 10/10
  total: 30/30
mastered:
  - 已能把成年人口与劳动力区分开。
  - 已能把全职学生和灰心工人排除出劳动力。
  - 已能正确使用失业率分母：劳动力，而不是成年人口或总人口。
watch_points:
  - 后续仍需避免把“有劳动能力的人”直接说成“劳动力”。
  - 卷面表达建议固定写：劳动力 = 就业者 + 正在找工作的失业者。
teaching_decision:
  action: proceed_to_day2_final_quiz
  reason: labor force misconception repaired in immediate follow-up calculation.
student_state_update:
  labor_force_definition_stability: repaired
  day2_readiness_for_final_quiz: ready
```

### day2-t11 — final_quiz

```yaml
phase: day2_final_quiz
score_type: blind_score
prompt_visibility: student_prompt_only
student_answer_summary: |
  学生完成 Day 2 终测。CPI 计算中正确给出 2024 CPI = 100，2025 CPI = 110，2026 CPI = 121；2025 通胀率 = 10%，2026 通胀率 = 10%。CPI 替代偏误解释清楚，能说明固定消费篮子不随消费者购买结构调整，因此当相对价格变化时可能高估真实生活成本上涨。失业率题中正确计算劳动力 = 350，失业人数 = 50，失业率 = 50/350 = 14.28%；但劳动参与率误用就业人数作为分子，写成 300/500 = 60%，应为劳动力/成年人口 = 350/500 = 70%。灰心工人题能解释分子和分母同时减少，官方失业率可能下降但就业市场未必改善。三类失业解释准确，并能举搬家/毕业找工作、AI 替代翻译需求、经济衰退订单下降等例子。
assessment:
  q1_cpi_and_inflation_calculation: 11.5/12
  q2_cpi_substitution_bias: 9.5/10
  q3_unemployment_and_participation_calculation: 9/12
  q4_discouraged_workers: 7.5/8
  q5_unemployment_types: 8/8
  total: 45.5/50
  percentage: 91
pass_readiness_after_quiz: continue
mastered:
  - 能准确计算 CPI 与连续年份通胀率。
  - 能用固定消费篮子和消费者替代行为解释 CPI 可能高估真实生活成本上涨。
  - 能准确使用失业率公式：失业人数 / 劳动力。
  - 能正确排除学生、退休者、灰心工人等非劳动力人口。
  - 能解释灰心工人增加会使官方失业率产生误导。
  - 能区分摩擦性、结构性和周期性失业，并给出合理例子。
watch_points:
  - 劳动参与率的分子是劳动力，不是就业人数。正确公式：劳动参与率 = 劳动力 / 成年人口 × 100%。
  - Q1 中出现“484-400=44”的口误，虽然最终 CPI 和通胀率正确；卷面中应删除无关中间步骤。
  - “灰薪工人”应写作“灰心工人”。
  - 终测后仍需在 Day 3 开头复查：劳动参与率、灰心工人与失业率、CPI 替代偏误。
teaching_decision:
  action: complete_day2_and_prepare_day3
  reason: Day 2 final quiz 45.5/50，超过 75% 通过线；核心概念稳定，只有劳动参与率公式需下次开头快速回忆。
student_state_update:
  current_day: 3
  completed_sessions: 2
  pass_readiness: improving
  risk_level: medium
  day2_status: completed
  next_action: run_day_3
  day3_start_with:
    - recall CPI vs inflation rate
    - calculate labor force participation rate
    - distinguish unemployment rate fall due to jobs vs labor force exit
    - proceed to AD-AS basics
```

#### 终测标准答案与修正

1. 以 2024 年为基准年，2024 年 CPI = 400/400×100 = 100；2025 年 CPI = 440/400×100 = 110；2026 年 CPI = 484/400×100 = 121。2025 年通胀率 = (110-100)/100×100% = 10%；2026 年通胀率 = (121-110)/110×100% = 10%。
2. 固定消费篮子不随消费者行为调整。当某些商品相对变贵时，消费者会用相对便宜的替代品替代；固定篮子仍假设按原数量购买较贵商品，因此可能高估真实生活成本上涨。
3. 劳动力 = 300 + 50 = 350；失业人数 = 50；失业率 = 50/350×100% ≈ 14.3%；劳动参与率 = 350/500×100% = 70%。
4. 灰心工人停止找工作后，不再计入失业人数，也不再计入劳动力。因此官方失业率可能下降，但这不是因为更多人找到工作，而是因为更多人退出劳动力市场。
5. 摩擦性失业来自找工作和匹配需要时间；结构性失业来自技能、地区或行业与岗位需求不匹配；周期性失业来自经济衰退和总需求不足。

#### 新增 misconception

```text
Misconception: 劳动参与率 = 就业人数 / 成年人口。
Correction: 劳动参与率 = 劳动力 / 成年人口 × 100%，其中劳动力 = 就业者 + 正在找工作的失业者。就业人数 / 成年人口 更接近就业人口比率，不是劳动参与率。
Status: needs_light_review
Source: day2-t11 final quiz
```

#### 新增 recall cards

```text
Q: 劳动参与率怎么计算？
A: 劳动参与率 = 劳动力 / 成年人口 × 100%，其中劳动力 = 就业者 + 正在找工作的失业者。
Due: next_session
Source: day2-t11 final quiz
```

```text
Q: 失业率和劳动参与率的分母分别是什么？
A: 失业率的分母是劳动力；劳动参与率的分母是成年人口。失业率 = 失业人数/劳动力，劳动参与率 = 劳动力/成年人口。
Due: next_session
Source: day2-t11 final quiz
```

---

### day2-t12 — extension_question_market_impact

```yaml
phase: day2_extension_question
score_type: not_scored
prompt_visibility: student_initiated_question
student_question_summary: |
  学生追问 CPI 和失业率的影响是否会在后续课程讲，以及为什么失业率等宏观数据会影响科技股价格。
teaching_response_plan:
  action: give_short_bridge_and_preserve_scope
  reason: |
    该问题有助于把 Day 2 的宏观指标连接到后续 AD-AS、货币政策、经济周期和菲利普斯曲线，但若在 Day 2 全面展开，会分散今天的定义和计算训练。建议给出 5 分钟传导链预告，并在 Day 3-6 系统展开。
interest_ledger_update:
  interest: macro_data_to_stock_market_especially_tech
  status: active
  use_in_future_sessions:
    - Day 3 AD-AS: CPI/就业数据如何反映 AD、SRAS、产出缺口。
    - Day 5 monetary policy: 通胀和失业如何影响央行利率决定。
    - Day 6 Phillips curve/business cycle: 通胀、失业、经济周期与政策预期。
    - Final review: 用“数据 → 政策预期 → 利率/盈利预期 → 资产价格”作为综合题例子。
watch_points:
  - 强调股价反应的是“数据相对市场预期的偏离”，不是指标本身机械决定股价。
  - 科技股通常对利率更敏感，因为估值更依赖未来较远期现金流。
  - 失业率上升有双重含义：经济变弱可能压低盈利；但通胀压力下降、降息预期增强可能支持估值。
```

---

### day2-t13 — extension_question_chained_cpi

```yaml
phase: day2_extension_question
score_type: not_scored
prompt_visibility: student_initiated_question
student_question_summary: |
  学生把 Day 1 的 chain-weighted real GDP 与 Day 2 的 CPI 联系起来，追问 CPI 是否也有类似 chained / chain-weighted 的处理，尤其是在价格变化、新产品加入、旧产品剔除、消费结构变化时。
teaching_response_plan:
  action: answer_as_extension_without_expanding_full_methodology
  core_points:
    - textbook CPI initially taught as fixed basket for concept clarity
    - official CPI is not simply a forever fixed basket; weights are updated and quality/replacement adjustments are used
    - the U.S. BLS publishes Chained CPI, C-CPI-U, designed to reflect substitution across item categories when relative prices change
    - Chained CPI is related to chain-weighting but not identical to chain-weighted real GDP; GDP chaining handles production quantity/value aggregation, while chained CPI handles consumer cost-of-living approximation and substitution
    - chaining helps with substitution bias but does not fully solve new product and quality change issues; those require sample replacement and quality adjustment methods such as hedonic adjustment
future_use:
  - Day 5/6: link inflation measures to policy expectations; mention CPI-U, C-CPI-U, PCE price index only if useful
  - Final review: compare GDP deflator, CPI, chained CPI, and PCE price index at a high level
recall_card_added:
  Q: CPI 有没有 chained 版本？
  A: 有。美国 BLS 发布 Chained CPI（C-CPI-U），用能反映消费者在相对价格变化后跨类别替代的公式，更接近生活成本指数；但它不能完全解决新产品和质量变化问题。
```

---

### day2-t14 — extension_question_cpi_u_cpi_w_chained_calculation

```yaml
phase: day2_extension_question
score_type: not_scored
prompt_visibility: student_initiated_question
student_question_summary: |
  学生追问 CPI-U、CPI-W 分别是什么，以及 Chained CPI 的计算方法。
teaching_response_plan:
  action: explain_with_official_distinctions_and_simple_formula
  core_points:
    - CPI-U = Consumer Price Index for All Urban Consumers；覆盖美国城市消费者，是最常被媒体报道的广义 CPI。
    - CPI-W = Consumer Price Index for Urban Wage Earners and Clerical Workers；是 CPI-U 覆盖人口中的一个子集，代表城市工薪与文职人员家庭。
    - CPI-U 与 CPI-W 的主要差别是覆盖人口不同，因此消费权重不同；不是“一个算商品、一个算工资”。
    - C-CPI-U = Chained CPI for All Urban Consumers；覆盖人口与 CPI-U 相同，但上层汇总公式和权重处理不同。
    - 最终 C-CPI-U 用相邻月份的支出份额和 Törnqvist 公式计算月度价格变化，再逐月连乘成指数。
    - Chained CPI 主要处理跨类别替代行为；新产品、质量变化、商品替换仍需其他统计处理。
formula_note: |
  简化公式：monthly_relative = product_i(price_relative_i ^ average_expenditure_share_i)
  C-CPI_t = C-CPI_{t-1} × monthly_relative
watch_points:
  - 不把 CPI-W 解释为“工资指数”；它仍然是消费者价格指数，只是人群为城市工薪和文职人员。
  - 不把 chained CPI 说成完全解决所有 CPI 偏误；它主要处理替代偏误。
recall_card_added:
  Q: CPI-U、CPI-W、C-CPI-U 有什么区别？
  A: CPI-U 覆盖所有城市消费者；CPI-W 覆盖城市工薪和文职人员，是 CPI-U 的子集；C-CPI-U 覆盖 CPI-U 人群，但使用 chained / Törnqvist 方法和逐月变化的支出权重，更能反映消费者替代行为。
```

---

### day2-t15 — extension_question_state_and_local_cpi

```yaml
phase: day2_extension_question
score_type: not_scored
prompt_visibility: student_initiated_question
student_question_summary: |
  学生追问美国是否按州单独计算 CPI，例如加州和德州生活成本不同；如果有，应该从哪里查看这些数据。
teaching_response_plan:
  action: explain_official_geography_and_data_sources
  core_points:
    - BLS 官方 CPI 主要发布美国全国、区域、分区以及部分都市区/城市地区的 CPI；不是每个州都有一个完整、可直接比较的官方州 CPI。
    - CPI 地区指数衡量的是某地区随时间的价格变化，不应用来直接比较两个地区生活成本高低；比较地区间价格水平应看 BEA Regional Price Parities 等数据。
    - 加州可查看 BLS 的 Los Angeles、San Francisco、San Diego、Riverside 等都市区 CPI，也可查看加州 DIR 整理的 California Consumer Price Index 页面。
    - 德州可查看 BLS 的 Dallas-Fort Worth、Houston 以及 South Region CPI。
    - BLS CPI News Releases by state 页面和 CPI Data Retrieval Tool 是最直接入口。
watch_points:
  - 不把 metro CPI 误说成 state CPI。
  - 不用 CPI 指数点位直接比较 California 与 Texas 的生活成本水平。
  - 区分“通胀率/价格变化”与“生活成本水平/地区价格水平”。
recall_card_added:
  Q: 美国有没有每个州官方 CPI？
  A: BLS 主要发布全国、区域、分区和部分都市区 CPI，不是每个州都有完整州级 CPI。加州、德州等可查看对应都市区或区域 CPI；若要比较州际生活成本水平，应看 BEA Regional Price Parities 等数据，而不是直接比较 CPI 指数点位。
```


---

### day2-t16 — final_learning_record_compiled

```yaml
phase: record_compilation
score_type: not_scored
prompt_visibility: student_requested_record
student_request_summary: |
  学生要求整理并记录今天的学习记录。
record_actions:
  - Updated Day 2 learning record markdown with core learning outcomes, final quiz results, misconceptions, recall cards, extension questions, and Day 3 next action.
  - Preserved Day 2 final quiz score: 45.5/50.
  - Added extensions: macro data to tech stocks, Chained CPI, CPI-U/CPI-W/C-CPI-U, state/local CPI and regional price levels.
student_state_update:
  day2_status: completed_with_extensions
  next_action: run_day_3
  day3_start_watch_point: labor force participation rate = labor force / adult population, not employed / adult population
```
