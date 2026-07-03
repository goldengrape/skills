"""Small course seed registry for local MVP course OKF repair.

The registry is intentionally narrow: it provides tested starter content for common
concept-heavy courses. Unknown courses must be filled by the factory agent from
user materials or reconnaissance; the quality gate will not pretend that a
placeholder skeleton is ready.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Tuple

try:
    from tools.render_diagram_asset import METADATA as DIAGRAM_METADATA, render_many, write_index
except ModuleNotFoundError:  # allow running as a script from tools/
    from render_diagram_asset import METADATA as DIAGRAM_METADATA, render_many, write_index  # type: ignore


@dataclass(frozen=True)
class CourseSeed:
    seed_id: str
    aliases: List[str]
    required_terms: List[str]
    writer: Callable[[Path, str, int, int], List[str]]


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _fm(kind: str, title: str, description: str, tags: Iterable[str]) -> str:
    return (
        "---\n"
        f"type: {kind}\n"
        f"title: {title}\n"
        f"description: {description}\n"
        f"tags: [{', '.join(tags)}]\n"
        f"timestamp: {_now_iso()}\n"
        "---\n\n"
    )


def _write(root: Path, rel_path: str, content: str) -> str:
    path = root / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return rel_path


def _cycle(items: List[Dict[str, str]], day: int) -> Dict[str, str]:
    return items[(day - 1) % len(items)]


def _macro_topics() -> List[Dict[str, str]]:
    return [
        {"topic": "GDP 与国民收入核算", "terms": "GDP, nominal GDP, real GDP, GDP deflator, final goods", "question": "为什么 GDP 不等于居民生活质量？"},
        {"topic": "通货膨胀、CPI 与失业", "terms": "inflation, CPI, unemployment rate, labor force, discouraged workers", "question": "CPI 和 GDP deflator 的区别是什么？"},
        {"topic": "总需求与总供给", "terms": "aggregate demand, short-run aggregate supply, long-run aggregate supply, output gap", "question": "总需求右移会如何影响产出和价格水平？"},
        {"topic": "财政政策与乘数", "terms": "fiscal policy, government spending, taxes, multiplier, crowding out", "question": "扩张性财政政策为什么可能挤出私人投资？"},
        {"topic": "货币、银行与中央银行", "terms": "money supply, central bank, reserve ratio, interest rate, open market operations", "question": "中央银行降低利率通常如何影响总需求？"},
        {"topic": "稳定政策与菲利普斯曲线", "terms": "business cycle, stabilization policy, Phillips curve, expectations, short-run tradeoff", "question": "为什么短期失业和通胀可能存在权衡？"},
        {"topic": "开放经济基础", "terms": "net exports, exchange rate, capital flows, trade balance", "question": "汇率变化如何影响净出口？"},
    ]



def _write_macro_visual_assets(root: Path) -> List[str]:
    diagrams = [
        "ad_curve",
        "sras_curve",
        "lras_curve",
        "ad_sras_equilibrium",
        "ad_sras_four_shocks",
        "output_gaps",
        "policy_closing_output_gaps",
    ]
    output_dir = root / "assets/diagrams"
    paths = render_many(diagrams, output_dir, prefix="day3-")
    rows: List[Tuple[str, Path, str, str, str]] = []
    used_in_map = {
        "ad_curve": "plan/day-3.md; teacher/teacher-notebook.md; learning-records/day-3.md",
        "sras_curve": "plan/day-3.md; teacher/teacher-notebook.md; learning-records/day-3.md",
        "lras_curve": "plan/day-3.md; teacher/teacher-notebook.md; learning-records/day-3.md",
        "ad_sras_equilibrium": "plan/day-3.md; teacher/teacher-notebook.md; learning-records/day-3.md",
        "ad_sras_four_shocks": "plan/day-3.md; quizzes/day-3-quiz.md; final-review/compressed-notes.md",
        "output_gaps": "plan/day-3.md; final-review/compressed-notes.md",
        "policy_closing_output_gaps": "plan/day-4.md; final-review/compressed-notes.md",
    }
    for diagram, path in zip(diagrams, paths):
        meta = DIAGRAM_METADATA[diagram]
        rows.append((path.stem, path, meta["topic"], used_in_map[diagram], meta["notes"]))
    write_index(output_dir, root, rows)
    return [str(path.relative_to(root)) for path in paths] + ["assets/diagrams/index.md"]

def _write_macro(root: Path, course_name: str, days: int, daily_minutes: int) -> List[str]:
    topics = _macro_topics()
    written: List[str] = []
    written.extend(_write_macro_visual_assets(root))
    written.append(_write(root, "course-map.md", _fm("Course Map", "Macroeconomics Course Map", "Minimal pass-level macroeconomics map.", ["course-map", "macroeconomics"]) + """# Macroeconomics Course Map

## Exam Goal

在有限时间内形成宏观经济学及格线所需的最小地图：会解释核心指标、会画出政策冲击的方向、会用 3-5 个得分点回答简答题。

## Minimal Knowledge Map

1. **GDP 与国民收入核算**：名义 GDP、实际 GDP、GDP deflator、最终产品、支出法。
2. **通货膨胀与失业**：CPI、inflation rate、unemployment rate、劳动力与失业类型。
3. **Aggregate Demand / Aggregate Supply**：AD、SRAS、LRAS、产出缺口、价格水平。
4. **Fiscal Policy**：政府支出、税收、乘数、自动稳定器、crowding out。
5. **Monetary Policy**：中央银行、货币供给、利率、公开市场操作、银行准备金。
6. **Business Cycle and Stabilization**：衰退、扩张、需求冲击、供给冲击、短期和长期调整。
7. **Open Economy Basics**：net exports、exchange rate、trade balance、capital flows。

## Dependency Order

GDP / CPI / unemployment → AD-AS model → fiscal and monetary policy → stabilization essay answers → final mock exam.

## Visual Teaching Requirements

AD-AS, LRAS, output gap, policy shift, Phillips curve, and money-market topics require diagrams. Use `assets/diagrams/index.md` to reuse generated images when possible.

## High-Risk Confusions

- 名义 GDP vs 实际 GDP。
- CPI vs GDP deflator。
- unemployment rate vs labor-force participation。
- AD shift vs SRAS shift。
- fiscal policy vs monetary policy。
- short-run effect vs long-run adjustment。
"""))
    written.append(_write(root, "priority-map.md", _fm("Priority Map", "Macroeconomics Priority Map", "A/B/C exam-value classification for pass-level macroeconomics.", ["priority", "macroeconomics", "exam"]) + """# Priority Map

## A — Must Know

| Topic | Why it is A | Minimum exam answer |
|---|---|---|
| GDP 与国民收入核算 | 名词解释、简答、计算解释都常见。 | 定义 GDP，区分 nominal GDP / real GDP，说明只计最终产品。 |
| Inflation and CPI | 宏观指标题高频。 | 解释 CPI、inflation rate，并指出购买力变化。 |
| Unemployment | 常与经济周期、政策题连用。 | 说明 unemployment rate 的分母和 discouraged workers 问题。 |
| Aggregate Demand / Aggregate Supply | 政策分析的主图。 | 判断 AD/SRAS/LRAS 移动方向，说明产出和物价变化。 |
| Fiscal Policy | 及格线论述题核心。 | 说明政府支出、税收、乘数和 crowding out。 |
| Monetary Policy | 及格线论述题核心。 | 说明中央银行、利率、货币供给和总需求的关系。 |

## B — Stabilizers

| Topic | Why it is B | Minimum exam answer |
|---|---|---|
| Phillips Curve | 可提高论述题稳定性。 | 说明短期通胀和失业权衡，长期受预期影响。 |
| Economic Growth | 常见但短期可压缩。 | 区分短期波动和长期增长，提到生产率。 |
| Open Economy | 课程涉及时可能进入简答。 | 说明汇率、净出口和贸易余额的基本关系。 |

## C — Short-Term Low Value

| Topic | Reason to defer |
|---|---|
| 复杂宏观模型推导 | 一周及格目标下收益低。 |
| 高级动态优化模型 | 不属于概念型期末及格线。 |
| 大量历史争论细节 | 只保留能服务政策题的关键词。 |
"""))
    written.append(_write(root, "glossary.md", _fm("Glossary", "Macroeconomics Glossary", "Concise exam definitions for macroeconomics.", ["glossary", "macroeconomics"]) + """# Glossary

| Term | Exam Definition | Common Confusion |
|---|---|---|
| GDP | 一国一定时期内生产的最终产品和服务的市场价值。 | GDP 不是福利总和，也不包含所有非市场活动。 |
| Nominal GDP | 按当期价格计算的 GDP。 | 会受价格和数量同时影响。 |
| Real GDP | 按基期价格计算的 GDP。 | 更适合比较实际产出变化。 |
| CPI | 反映固定消费篮子价格变化的指数。 | 与 GDP deflator 覆盖范围不同。 |
| Inflation | 总体价格水平持续上升。 | 不是单个商品涨价。 |
| Unemployment Rate | 失业人数 / 劳动力人口。 | 不在劳动力中的人不进入分母。 |
| Aggregate Demand | 经济中总支出需求。 | 与单个市场需求曲线不同。 |
| Aggregate Supply | 经济中总产出供给。 | 短期和长期斜率不同。 |
| Fiscal Policy | 政府通过支出和税收影响经济。 | 不等于中央银行调利率。 |
| Monetary Policy | 中央银行通过货币供给和利率影响经济。 | 不等于财政预算。 |
| Multiplier | 初始支出变化导致总产出更大幅变化的机制。 | 乘数大小受边际消费倾向等影响。 |
| Crowding Out | 政府借款推高利率并压低私人投资的可能效应。 | 不是所有财政扩张都会同等程度发生。 |
"""))
    plan_rows = []
    for day in range(1, days + 1):
        t = _cycle(topics, day)
        if day == days:
            main = "final review: compressed notes, must-know list, answer templates, 60-point mock exam"
        elif day == 1:
            main = "GDP, inflation, CPI, unemployment baseline"
        else:
            main = f"{t['topic']}: {t['terms']}"
        plan_rows.append(f"| {day} | {main} | quiz + recall deck + next-action update |")
    written.append(_write(root, "plan/seven-day-plan.md", _fm("Plan", "Macroeconomics Crash-Course Plan", "Configured-day pass-level macroeconomics plan.", ["plan", "macroeconomics"]) + "# Macroeconomics Crash-Course Plan\n\n" + f"Configured days: `{days}`\nDaily minutes: `{daily_minutes}`\nTarget: pass-level / 60 points\n\n| Day | Main use | State requirement |\n|---:|---|---|\n" + "\n".join(plan_rows) + "\n"))
    for day in range(1, days + 1):
        t = _cycle(topics, day)
        if day == days:
            goal = "finish final review and 60-point mock exam"
            core = "integrated comparison: GDP/CPI/unemployment, AD-AS, fiscal policy, monetary policy, stabilization"
            practice = "write one 8-point policy essay comparing fiscal policy and monetary policy in a recession"
        else:
            goal = f"make `{t['topic']}` usable in short-answer exam form"
            core = f"Core terms: {t['terms']}"
            practice = t["question"]
        written.append(_write(root, f"plan/day-{day}.md", _fm("Daily Work Package", f"Macroeconomics Day {day}", "One time-boxed macroeconomics learning session.", ["plan", "daily", "macroeconomics"]) + f"""# Day {day}

## Goal

{goal}.

## Exam Value

This session protects A/B priority macroeconomics content needed for a pass-level exam answer.

## Time Box

| Minutes | Activity |
|---:|---|
| 0-5 | Recall due cards: GDP, CPI, unemployment, AD-AS, fiscal policy, monetary policy as applicable |
| 5-10 | Place today's topic on the macro course map |
| 10-25 | Core explanation: {core} |
| 25-35 | Feynman task: explain the topic to a classmate without notes, then add one example and one counterexample |
| 35-45 | Exam practice: {practice} |
| 45-55 | Feedback: check definition accuracy, causal chain, and policy direction |
| 55-60 | State update: update score-history, recall-deck, misconceptions, and next-action |

## Visual Requirements

- If the session explains a curve, graph shift, equilibrium model, or output gap, use a diagram.
- Prefer generated Python/matplotlib diagrams from `assets/diagrams/`.
- Insert the image near the matching explanation and record it in `teacher/teacher-notebook.md`.
- Do not use complex ASCII diagrams as the main explanation.

## Must Produce

- One 3-5 point short answer.
- One easy-confusion comparison.
- One recall card for a missed term.
"""))
        written.append(_write(root, f"quizzes/day-{day}-quiz.md", _fm("Quiz", f"Macroeconomics Day {day} Quiz", "Short pass-level macroeconomics quiz.", ["quiz", "macroeconomics"]) + f"""# Day {day} Quiz

## Items

1. 名词解释：解释 `{t['topic']}` 中任意两个关键词，并各写一个容易混淆点。
2. 简答题：{practice}
3. 易混对比：从 nominal GDP / real GDP、CPI / GDP deflator、AD shift / SRAS shift、fiscal policy / monetary policy 中选一组，写出差异和例子。

## Scoring

| Result | Meaning | Next action |
|---|---|---|
| 0-40% | 宏观概念还不能用于答题 | repair |
| 41-59% | 接近及格但不稳定 | review |
| 60-74% | 可进入下一天，但要保留检索卡 | continue |
| 75%+ | 当前主题较稳 | continue or simulate |
"""))
    written.append(_write(root, "final-review/compressed-notes.md", _fm("Final Review", "Macroeconomics Compressed Notes", "Compressed pass-level macroeconomics notes.", ["final-review", "macroeconomics"]) + """# Macroeconomics Compressed Notes

## One-Page Spine

GDP measures output. CPI measures consumer-price inflation. Unemployment measures unused labor within the labor force. AD-AS explains short-run output and price movements. Fiscal policy changes government spending and taxes. Monetary policy changes money, interest rates, and aggregate demand. Stabilization policy tries to reduce recessions and overheating, but short-run gains can have long-run tradeoffs.

## Reusable Diagram Assets

Use `assets/diagrams/day3-ad-sras-four-shocks.png`, `assets/diagrams/day3-output-gaps.png`, and `assets/diagrams/day3-policy-closing-output-gaps.png` for AD-AS and policy review when available.

## Default Short-Answer Structure

1. Define the concept.
2. State the causal mechanism.
3. Mention the short-run effect.
4. Mention one limitation or long-run adjustment.
5. Give one example.
"""))
    written.append(_write(root, "final-review/must-know-list.md", _fm("Final Review", "Macroeconomics Must-Know List", "Must-know list for a 60-point macroeconomics target.", ["final-review", "macroeconomics"]) + """# Must-Know List

## A-Level Terms

- GDP, nominal GDP, real GDP, GDP deflator.
- CPI, inflation rate, purchasing power.
- Unemployment rate, labor force, discouraged workers.
- Aggregate demand, SRAS, LRAS, output gap.
- Fiscal policy, multiplier, crowding out.
- Monetary policy, central bank, interest rate, money supply.

## A-Level Comparisons

- Nominal GDP vs real GDP.
- CPI vs GDP deflator.
- Fiscal policy vs monetary policy.
- Demand shock vs supply shock.
- Short-run Phillips curve vs long-run adjustment.
"""))
    written.append(_write(root, "final-review/answer-templates.md", _fm("Final Review", "Macroeconomics Answer Templates", "Exam answer templates for macroeconomics.", ["final-review", "templates", "macroeconomics"]) + """# Answer Templates

## 名词解释

`概念 = 定义 + 衡量对象 + 一个边界 + 一个例子`。

Example: Real GDP is GDP measured using base-year prices, so it better reflects changes in output rather than changes in prices.

## 简答题

`结论句 → 机制 1 → 机制 2 → 图形/方向 → 限制条件`。

## 论述题

`定义问题 → 选择模型 → 分析政策工具 → 说明短期效果 → 说明长期或副作用 → 小结`。
"""))
    written.append(_write(root, "final-review/mock-exam.md", _fm("Final Review", "Macroeconomics 60-Point Mock Exam", "Pass-level mock exam for macroeconomics.", ["final-review", "mock-exam", "macroeconomics"]) + """# 60-Point Mock Exam

## Part A — Terms, 20 points

1. GDP and real GDP. 5 points.
2. CPI and inflation. 5 points.
3. Unemployment rate. 5 points.
4. Aggregate demand. 5 points.

## Part B — Short Answers, 24 points

1. Explain how expansionary fiscal policy may affect output and the price level in the short run. 8 points.
2. Explain how a central bank can use monetary policy during a recession. 8 points.
3. Distinguish a demand shock from a supply shock using AD-AS language. 8 points.

## Part C — Essay, 16 points

A recession has reduced output and increased unemployment. Compare fiscal policy and monetary policy as stabilization tools. Your answer must define both policies, explain the causal chain, mention one limitation, and state a conclusion.
"""))
    return written


def _management_topics() -> List[Dict[str, str]]:
    return [
        {"topic": "管理职能", "terms": "planning, organizing, leading, controlling", "question": "管理的四项基本职能如何相互配合？"},
        {"topic": "组织结构", "terms": "division of labor, span of control, centralization, decentralization", "question": "职能型结构和事业部型结构各有什么优缺点？"},
        {"topic": "激励理论", "terms": "Maslow, Herzberg, expectancy theory, equity theory", "question": "双因素理论如何解释员工满意与不满意？"},
        {"topic": "领导理论", "terms": "leadership style, contingency theory, transformational leadership", "question": "为什么不存在唯一最好的领导方式？"},
        {"topic": "控制与决策", "terms": "decision making, feedback control, standards, corrective action", "question": "控制过程通常包括哪些步骤？"},
    ]


def _write_management(root: Path, course_name: str, days: int, daily_minutes: int) -> List[str]:
    topics = _management_topics()
    written: List[str] = []
    written.append(_write(root, "course-map.md", _fm("Course Map", "Management Course Map", "Minimal pass-level management map.", ["course-map", "management"]) + """# Management Course Map

## Minimal Knowledge Map

1. 管理概念与管理者角色。
2. Planning, organizing, leading, controlling 四项职能。
3. 组织结构：分工、管理幅度、集权与分权。
4. 激励理论：Maslow, Herzberg, expectancy theory, equity theory。
5. 领导理论：领导风格、权变理论、变革型领导。
6. 决策与控制：决策步骤、标准、反馈控制、纠偏。

## High-Risk Confusions

- 管理职能 vs 管理者角色。
- 激励因素 vs 保健因素。
- 集权 vs 分权。
- 领导 vs 管理。
"""))
    written.append(_write(root, "priority-map.md", _fm("Priority Map", "Management Priority Map", "A/B/C exam-value classification for management.", ["priority", "management"]) + """# Priority Map

## A — Must Know

| Topic | Why it is A | Minimum exam answer |
|---|---|---|
| Planning / Organizing / Leading / Controlling | 管理学简答题主干。 | 写出四项职能并说明相互关系。 |
| 组织结构 | 高频概念和案例分析。 | 比较职能型、事业部型、矩阵型结构。 |
| 激励理论 | 名词解释和简答高频。 | 区分 Maslow、Herzberg、expectancy theory。 |
| 领导理论 | 简答和论述常见。 | 说明权变思想：情境影响领导方式。 |
| 控制过程 | 基础题常见。 | 标准、衡量、比较、纠偏。 |

## B — Stabilizers

- 企业文化。
- 沟通。
- 决策偏差。

## C — Short-Term Low Value

- 复杂管理思想史细节。
- 高级战略分析工具展开。
"""))
    written.append(_write(root, "glossary.md", _fm("Glossary", "Management Glossary", "Concise exam definitions for management.", ["glossary", "management"]) + """# Glossary

| Term | Exam Definition | Common Confusion |
|---|---|---|
| Planning | 确定目标并制定实现目标的行动方案。 | 不等于执行本身。 |
| Organizing | 配置资源、划分职责并建立结构。 | 不等于单纯排班。 |
| Leading | 影响和激励成员实现目标。 | 不等于职位权力本身。 |
| Controlling | 设定标准、衡量绩效、比较差距并纠偏。 | 不等于事后批评。 |
| Herzberg Two-Factor Theory | 区分激励因素和保健因素。 | 保健因素不足会不满，但充足不一定激励。 |
"""))
    rows = [f"| {day} | {_cycle(topics, day)['topic']} | quiz + recall deck + next-action update |" for day in range(1, days + 1)]
    written.append(_write(root, "plan/seven-day-plan.md", _fm("Plan", "Management Crash-Course Plan", "Configured-day pass-level management plan.", ["plan", "management"]) + "# Management Crash-Course Plan\n\n" + f"Configured days: `{days}`\nDaily minutes: `{daily_minutes}`\n\n| Day | Main use | State requirement |\n|---:|---|---|\n" + "\n".join(rows) + "\n"))
    for day in range(1, days + 1):
        t = _cycle(topics, day)
        written.append(_write(root, f"plan/day-{day}.md", _fm("Daily Work Package", f"Management Day {day}", "One time-boxed management learning session.", ["plan", "daily", "management"]) + f"""# Day {day}

## Goal

Make `{t['topic']}` usable for a pass-level management exam answer.

## Time Box

| Minutes | Activity |
|---:|---|
| 0-5 | Recall prior management terms |
| 5-10 | Place today's topic on the management course map |
| 10-25 | Core explanation: {t['terms']} |
| 25-35 | Feynman task with one workplace example |
| 35-45 | Exam practice: {t['question']} |
| 45-55 | Feedback and misconception repair |
| 55-60 | State update |
"""))
        written.append(_write(root, f"quizzes/day-{day}-quiz.md", _fm("Quiz", f"Management Day {day} Quiz", "Short pass-level management quiz.", ["quiz", "management"]) + f"""# Day {day} Quiz

1. 名词解释：解释 `{t['topic']}` 中两个关键词。
2. 简答题：{t['question']}
3. 易混对比：写出一组管理学易混概念及区别。
"""))
    written.append(_write(root, "final-review/must-know-list.md", _fm("Final Review", "Management Must-Know List", "Must-know list for a 60-point management target.", ["final-review", "management"]) + "# Must-Know List\n\n- Planning, organizing, leading, controlling.\n- 组织结构：职能型、事业部型、矩阵型。\n- Maslow, Herzberg, expectancy theory.\n- 领导权变理论。\n- 控制过程：标准、衡量、比较、纠偏。\n"))
    written.append(_write(root, "final-review/mock-exam.md", _fm("Final Review", "Management 60-Point Mock Exam", "Pass-level mock exam for management.", ["final-review", "mock-exam", "management"]) + "# 60-Point Mock Exam\n\n## Terms, 20 points\n\n1. Planning. 5 points.\n2. Organizing. 5 points.\n3. Herzberg two-factor theory. 5 points.\n4. Span of control. 5 points.\n\n## Short Answers, 24 points\n\n1. Explain the four management functions. 8 points.\n2. Compare centralized and decentralized structures. 8 points.\n3. Explain why leadership style depends on context. 8 points.\n\n## Essay, 16 points\n\nA company has low morale and unclear responsibilities. Use motivation theory and organization structure to propose a management response.\n"))
    return written


SEEDS: List[CourseSeed] = [
    CourseSeed(
        seed_id="macroeconomics-v1",
        aliases=["macroeconomics", "macro economics", "宏观经济", "宏观经济学"],
        required_terms=["GDP", "inflation", "CPI", "unemployment", "aggregate demand", "aggregate supply", "fiscal policy", "monetary policy", "central bank", "interest rate"],
        writer=_write_macro,
    ),
    CourseSeed(
        seed_id="management-v1",
        aliases=["management", "管理学", "管理"],
        required_terms=["planning", "organizing", "leading", "controlling", "organization structure", "motivation", "leadership", "Herzberg", "Maslow"],
        writer=_write_management,
    ),
]


def get_course_seed(course_name: str) -> Optional[CourseSeed]:
    normalized = course_name.lower().replace(" ", "")
    for seed in SEEDS:
        for alias in seed.aliases:
            if alias.lower().replace(" ", "") in normalized:
                return seed
    return None


def apply_course_seed(root: Path, course_name: str, days: int, daily_minutes: int) -> Dict[str, object]:
    seed = get_course_seed(course_name)
    if seed is None:
        return {"applied": False, "seed_id": None, "written_files": [], "reason": "no matching course seed"}
    written = seed.writer(root, course_name, days, daily_minutes)
    return {"applied": True, "seed_id": seed.seed_id, "written_files": written, "reason": "matched course seed"}


def required_terms_for_course(course_name: str) -> List[str]:
    seed = get_course_seed(course_name)
    if seed is None:
        return []
    return seed.required_terms
