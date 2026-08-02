# TDD — Check Plan

## 元数据

- document_id: TDD-0001
- status: proposed
- source_docs: URD-0001, ADD-0001, MDD-0001
- last_updated: 2026-08-02

## 测试分层

| 层级 | 范围 | 默认执行 |
| --- | --- | --- |
| unit | 纯函数、路径规则、manifest、状态转换、ZIP 条目检查 | 每次提交 |
| contract | 每个 MDD 公共接口的前置、后置、不变量和失败结构 | 每次提交 |
| integration | 临时目录中的任务包、下载快照和安全解压；浏览器使用伪适配器 | 每次提交 |
| live | 真实 Codex in-app Browser 和 ChatGPT Web 往返 | 显式启用，发布前执行 |

## 验收测试

| ID | 来源 | 场景 | 给定 | 操作 | 判定依据 |
| --- | --- | --- | --- | --- | --- |
| TDD-TEST-001 | URD-AC-001 | 接管当前对话 | 已登录且 URL 已知的 in-app 标签页 | acquire conversation | 返回的 URL、标题、tab 标识与目标一致。 |
| TDD-TEST-002 | URD-AC-002 | 阻止未授权或敏感文件 | 输入含授权根外路径、`.env` 或私钥名 | validate request | 返回具体路径和错误码；没有包和浏览器事件。 |
| TDD-TEST-003 | URD-AC-003 | 生成确定性任务包 | 固定文件、时间和 task_id | 两次 prepare package | manifest、ZIP 文件列表、内容哈希相同，且可正常打开。 |
| TDD-TEST-004 | URD-AC-004 | 上传并发送一次 | 有效包、目标对话、无发送收据 | attach and send | 页面附件名和类型匹配，消息含 task_id，只有一个发送收据。 |
| TDD-TEST-005 | URD-AC-005 | 分类回复状态 | 完成、追问、失败和生成中页面样本 | wait for outcome | 每个样本映射到预期唯一状态并保留证据。 |
| TDD-TEST-006 | URD-AC-006 | 取得下载文件 | 下载前快照、下载事件、一个新 ZIP | capture download | 返回新文件，复制到任务目录，大小和 SHA-256 正确。 |
| TDD-TEST-007 | URD-AC-007 | 安全解压有效包 | 有效结果 ZIP 和必需文件表 | validate and extract | 文件只出现在结果目录，必需输出存在。 |
| TDD-TEST-008 | URD-AC-008 | 中断后恢复 | 已有成功发送收据、等待状态 | 重新运行 coordinator | 不再次上传或发送，从等待阶段继续。 |
| TDD-TEST-009 | URD-AC-009 | 结构化输出 | 完成、需要输入和失败三类执行记录 | assemble result | 三种结果均通过 JSON 模式校验。 |
| TDD-TEST-010 | URD-AC-010 | 日志不泄漏认证信息 | 日志输入含模拟 token/cookie 字段 | persist diagnostics | 敏感字段被拒绝或脱敏，任务证据字段完整。 |
| TDD-TEST-011 | URD-AC-011 | 验证时暂停 | 登录页、验证码或权限弹窗样本 | browser step | 返回 needs_input/failed；没有绕过或继续发送。 |
| TDD-TEST-012 | URD-AC-012 | 端到端真实往返 | 2026-08-02 小型 ZIP fixture | live delegate | ChatGPT 读取输入，生成 ZIP；本地哈希匹配且 4 个预期文件可解压。 |
| TDD-TEST-034 | URD-AC-013 | 避免可预览附件 | 页面样本同时含当前任务的结果 ZIP、`.md`、`.txt`、`.html`、`.py`，以及只含可预览附件的变体 | resolve result control | 混合样本只选择 ZIP 且不打开预览；无 ZIP 样本无点击副作用并返回 `needs_input` 或 `RESULT_ZIP_NOT_FOUND`。 |

## 接口契约测试

| ID | 接口 | 有效案例 | 无效案例 | 判定依据 |
| --- | --- | --- | --- | --- |
| TDD-TEST-013 | MDD-API-001 | 授权根内普通文件 | 路径逃逸、缺失文件、敏感名、限额超出 | 返回 `ValidatedRequest` 或字段化错误，不修改文件。 |
| TDD-TEST-014 | MDD-API-002 | 两个文本文件 | 中途写入失败、重复相对路径 | 成功包可复核；失败无残缺最终 ZIP。 |
| TDD-TEST-015 | MDD-API-003 | 当前/现有/新对话 | 错误 URL、未登录、tab 消失 | 成功句柄完整；失败码可区分。 |
| TDD-TEST-016 | MDD-API-004 | 正确附件且未发送 | 附件不符、已有成功收据、控件不唯一 | 只有合法案例产生一次发送副作用。 |
| TDD-TEST-017 | MDD-API-005 | 带 task_id 的完成回复 | 仅含“已完成”、别的 task_id、超时 | 只在证据充分时返回 completed。 |
| TDD-TEST-018 | MDD-API-006 | 单一新 ZIP 且大小稳定 | 无事件、多候选、临时文件未稳定 | 返回唯一收据或明确下载错误。 |
| TDD-TEST-019 | MDD-API-007 | 安全 ZIP | 坏 ZIP、`../`、绝对路径、超限、哈希不符 | 安全包解压；危险包在写出前失败。 |
| TDD-TEST-020 | MDD-API-008 | 合法状态转换 | completed→sending、重复发送收据 | 原子更新或 `INVALID_STATE_TRANSITION`。 |
| TDD-TEST-021 | MDD-API-009 | 正常序列 | 任一步骤抛出已知/未知错误 | 返回终态，state.json 保留最后成功阶段。 |

## 边界与负面测试

| ID | 关联项 | 案例 | 预期失败 |
| --- | --- | --- | --- |
| TDD-TEST-022 | URD-REQ-002 | 空 instruction、空输入、同名路径、符号链接离开授权根 | `INVALID_REQUEST` 或 `UNAUTHORIZED_PATH`。 |
| TDD-TEST-023 | URD-REQ-003 | 文件在扫描后、打包前被修改 | `INPUT_CHANGED`，不得上传不一致包。 |
| TDD-TEST-024 | URD-REQ-005 | 页面有两个同名附件控件 | `PAGE_CHANGED`，不得按位置猜测。 |
| TDD-TEST-025 | URD-REQ-006 | 回复被截断或出现继续生成 | 按策略继续一次或返回可恢复状态。 |
| TDD-TEST-026 | URD-REQ-007 | 下载按钮属于旧任务 | `RESULT_ATTACHMENT_NOT_FOUND`，不得下载旧结果。 |
| TDD-TEST-027 | URD-REQ-008 | ZIP 炸弹、高压缩率、条目过多、保留设备名 | `UNSAFE_ZIP_ENTRY` 或 `OUTPUT_LIMIT_EXCEEDED`。 |
| TDD-TEST-028 | URD-REQ-009 | state.json 写入时进程中断 | 旧状态仍可解析，临时文件可清理。 |
| TDD-TEST-029 | URD-REQ-011 | 日志包含密码、Cookie、Bearer token 模式 | 测试扫描结果为零泄漏。 |

## 回归测试

| ID | 保护内容 | 触发条件 | 判定依据 |
| --- | --- | --- | --- |
| TDD-TEST-030 | DEC-001 | Browser Skill 或 ChatGPT Web UI 更新 | 真实上传、发送、结果下载流程仍通过，或明确报告 `PAGE_CHANGED`。 |
| TDD-TEST-031 | DEC-002 | Python 或 ZIP 实现变更 | 固定 fixture 的 manifest 和哈希保持一致。 |
| TDD-TEST-032 | ADD 的顺序解耦 | 任一模块接口变更 | 浏览器伪适配器和本地脚本测试可分别通过。 |
| TDD-TEST-033 | 2026-08-02 基线 | 发布候选版本 | 完成 URD-AC-012；记录对话 URL、输入/输出哈希和文件清单。 |

## 测试数据

- `fixture-small/`：UTF-8 文本、嵌套目录和已知哈希。
- `fixture-sensitive/`：仅含模拟密钥格式，不含真实凭据。
- `fixture-unsafe-zips/`：路径穿越、绝对路径、超限条目和坏 CRC。
- `browser-fixtures/`：去除账号和个人内容的页面结构样本，包含 ZIP 与可预览附件并存、只有可预览附件两种结果控件状态。
- live 测试只上传专用无敏感数据 fixture，并使用唯一 task_id。

## 建议命令

```text
uv run pytest -q
uv run pytest -q -m "not live"
uv run pytest -q -m live
uv run ruff check .
```

live 测试必须由用户明确允许，因为它会向真实 ChatGPT Web 对话上传文件并发送消息。

## 完成门槛

- [x] 每个 URD 验收条件映射到至少一个测试。
- [x] 每个 MDD 公共接口有契约测试。
- [x] 身份、权限、敏感文件、ZIP 安全和恢复均有负面测试。
- [x] 每个测试写明可观察判定依据。
- [x] 实时外部测试与默认离线测试分开。
