---
type: Version Note
title: 版本说明
version: clean-v1
---

# 版本说明

- 包名：`us-patent-law-7day-course-okf-clean`
- 课程：7 天速通美国专利法
- 语言：中文
- 目标：零基础学习者建立美国专利法核心概念图，并能完成基础 issue spotting。
- 基础版本：Darwin R2 修订版
- 清理版本：clean-v1

## 清理范围

已保留：

- 学生学习材料：`plan/`、`quizzes/`、`practice/`、`case-cards/`、`final-review/`
- 状态文件：`state/`、`sessions/`、`learning-records/`
- 教师材料：`teacher/`
- 资料与边界：`resources.md`、`resources/`、`package-meta/design-basis/`
- 图示资源：`assets/`

已移除：

- `analysis/` 过程评审目录
- `generation-output.json`
- `quality-report.json`
- `validation-report*.json`
- 旧版 validation summary
- synthetic dry-run 学习记录

## 资料边界

本课程包包含资料索引与官方入口链接，但不内嵌完整法律数据库、完整 MPEP、完整 casebook 或商业数据库内容。使用者应通过 `resources.md` 与 `resources/` 中列出的入口核对最新资料。
