# 发布检查

- page_id: WIKI-PAGE-005
- source_ids: TDD-TEST-001–033, RMD-TASK-011, RMD-STOP-009
- status: derived

## 回答的问题

什么时候可以安装或发布 Skill？

## 当前事实

默认离线测试、ruff、Skill Creator quick validation 和 Vibe 文档检查必须通过。真实 ChatGPT Web 往返在用户允许后执行，并记录输入/输出哈希、对话 URL 和文件清单。

若页面变化，只有得到明确的 `PAGE_CHANGED` 诊断也可视为自动化安全失败；不得靠坐标猜测继续。
