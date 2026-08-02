# 完整往返

- page_id: WIKI-PAGE-001
- source_ids: URD-GOAL-001, URD-REQ-001, URD-REQ-003–010, URD-REQ-013, URD-AC-012–013
- status: derived

## 回答的问题

什么才算一次成功的 ChatGPT Web 委派？

## 当前事实

请求通过授权检查后，Skill 生成输入 ZIP，使用内置浏览器上传并发送任务，等待对应 task_id 的结果，下载 ZIP，校验并安全解压，最后返回结构化本地路径。

输入和结果资料统一使用 ZIP。`md`、`txt`、`html`、`py` 等可预览附件不作为下载目标；若没有结果 ZIP，Skill 不点击附件并返回 `needs_input` 或 `RESULT_ZIP_NOT_FOUND`。

成功不能只依据网页文字；必须同时有下载文件、哈希和解压后的必需输出。

## 不要假设

- 不假设 API、扩展、CDP 或独立浏览器可用。
- 不假设任何下载 ZIP 安全。
- 不假设重试可以重复发送消息。
- 不假设点击可预览附件可以稳定得到本地下载文件。
