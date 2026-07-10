---
type: Course OKF Entrypoint
title: 7 天速通美国专利法课程包
version: clean-v1
visibility: public
---

# 7 天速通美国专利法课程包

这是一个自包含的 Course OKF 课程包，用于帮助中文学习者在 7 天左右建立美国专利法的基础概念图，并训练基础短答、比较题和简单 issue spotting。

本包不是法律意见，也不替代美国专利律师或专利代理人的专业判断。

## 适合谁

- 零基础或近零基础学习者。
- 需要快速理解美国专利法核心结构的人。
- 想先建立概念地图，再继续读 casebook、MPEP 或正式课程的人。

## 不适合谁

- 需要处理真实专利申请、侵权风险、FTO、诉讼或商业决策的人。
- 已经需要执业级 claim drafting 或 prosecution strategy 的人。
- 想用 7 天替代法学院专利法课程或 patent bar preparation 的人。

## 文件入口

### 学生先读

1. `mission.md`：课程目标、范围和边界。
2. `resources.md`：资料入口与可信度说明。
3. `course-map.md`：概念地图。
4. `priority-map.md`：A/B/C 优先级。
5. `plan/day-1.md`：从第一天开始学习。

### 每日运行

每天建议按这个顺序执行：

1. 读取 `state/current-state.md`、`state/next-action.md`、`state/recall-deck.md`、`state/misconceptions.md`。
2. 学习当天 `plan/day-N.md`。
3. 完成 `quizzes/day-N-quiz.md`，不要提前看 `teacher/`。
4. 学习结束后更新 `sessions/` 和 `state/` 中相关文件。
5. 第 7 天后完成 `final-review/mock-exam.md`。

### 教师或助教使用

教师材料在 `teacher/` 中，包括：

- `teacher/answer-keys/`：每日答案要点。
- `teacher/rubrics/`：每日评分规则。
- `teacher/feedback-samples/`：针对 Day 2 / Day 4 / Day 5 的反馈样本。
- `teacher/final-review-answer-key.md`：期末模拟题答案要点。
- `teacher/teaching-protocol.md`：带学流程。
- `teacher/visibility-rules.md`：答案可见性规则。

### 重点补强练习

- `practice/alice-mayo-worked-example.md`：§101 Alice/Mayo 示例。
- `practice/phosita-motivation-fact-bank.md`：§103 PHOSITA 与组合动机事实库。
- `practice/section-112-broad-claim-drills.md`：§112 broad claim 与 full-scope enablement 练习。
- `practice/prior-art-search-lab.md`：prior art 检索实务练习。
- `practice/flawed-answer-drills.md`：错误答案修复练习。

## 资料边界

课程核心资料包括：35 U.S.C.、37 C.F.R.、USPTO MPEP、USPTO subject matter eligibility materials、USPTO Patent Public Search、PTAB materials、开放 casebook 和核心判例。详细索引见：

- `resources.md`
- `resources/source-hierarchy.md`
- `resources/update-tracker.md`
- `resources/affected-topics.md`
- `package-meta/design-basis/reference-index.md`

专利法资料会更新。正式使用前，尤其是 §101、AI-assisted inventorship、design patent、USPTO fees、PTAB 程序，应按上述资料入口重新核对。

## 当前质量状态

见 `package-meta/quality-status.md`。

简要说：本包可用于 beta 运行；R2 文档检查估计为 88.5 / 100，但尚未对 R2 做完整第二轮零基础模拟。
