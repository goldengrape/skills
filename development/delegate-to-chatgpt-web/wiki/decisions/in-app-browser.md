# 只使用 Codex 内置浏览器

- page_id: WIKI-PAGE-002
- source_ids: DEC-001, URD-REQ-001, URD-CON-001, URD-CON-002
- status: derived

## 回答的问题

为什么浏览器自动化不写进 Python 脚本？

## 当前事实

现有登录会话、标签页接管、附件上传和结果下载已经在 Codex in-app Browser 上验证。Python 脚本只做确定性本地文件和状态处理。

## 不要假设

- 不读取 Cookie、密码或浏览器配置。
- 不切换到外部浏览器作为静默后备。
- 页面定位失败时返回 `PAGE_CHANGED`。
