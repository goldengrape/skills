# MDD — Building Blocks

## 元数据

- document_id: MDD-0001
- status: proposed
- source_add: ADD-0001
- last_updated: 2026-08-02

## 实际 Skill 包

建议名称：`delegate-to-chatgpt-web`

```text
delegate-to-chatgpt-web/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── scripts/
│   ├── prepare_task_package.py
│   ├── task_state.py
│   ├── download_snapshot.py
│   └── validate_result_package.py
└── references/
    ├── browser-workflow.md
    ├── task-protocol-and-schemas.md
    └── errors-and-recovery.md
```

不创建 `README.md`、安装指南、变更日志或设计文档。开发项目中的 `docs/`、`wiki/` 和测试不复制进安装包。

## Skill 元数据草案

```yaml
---
name: delegate-to-chatgpt-web
description: Delegate bounded tasks from Codex to a current, existing, or new ChatGPT Web conversation through the Codex in-app browser; package explicitly authorized local inputs as ZIP, send a task protocol, monitor completion, download the matching result ZIP, validate and extract it, and return structured local results. Use when the user asks Codex to hand off document, code, research, or file-generation work to ChatGPT Web and exchange files through ZIP. Do not use for API-based model calls or general web automation.
---
```

建议界面字段：

- display_name: `Delegate to ChatGPT Web`
- short_description: `Send ZIP tasks to ChatGPT Web and retrieve results.`
- default_prompt: `Use $delegate-to-chatgpt-web to send this task and its authorized files to the current ChatGPT Web conversation, then download and validate the result ZIP.`

实现时必须先读取 Skill Creator 的 `references/openai_yaml.md`，再生成 `agents/openai.yaml`。

## 模块

| ID | 模块 | 相关 DP | 职责 | 不负责 |
| --- | --- | --- | --- | --- |
| MDD-MOD-001 | Run Coordinator | ADD-DP-008 | 按状态机调用步骤，组合最终结果。 | ZIP 细节和 DOM 定位。 |
| MDD-MOD-002 | Request Gate | ADD-DP-001 | 规范化请求，验证授权路径、敏感规则和限额。 | 创建 ZIP 或访问网页。 |
| MDD-MOD-003 | Task Packager | ADD-DP-002 | 生成 `TASK.md`、manifest、输入 ZIP 和校验值。 | 决定目标对话。 |
| MDD-MOD-004 | Browser Exchange Adapter | ADD-DP-003, ADD-DP-004 | 取得目标标签页，只上传 ZIP，核对并发送一次任务。 | 在 Python 中控制浏览器。 |
| MDD-MOD-005 | Response Monitor | ADD-DP-005 | 从页面证据产生进行中、完成、需要输入或失败结果，并标识当前任务的结果 ZIP 控件。 | 下载和解压文件。 |
| MDD-MOD-006 | Download Resolver | ADD-DP-006 | 排除可预览的非 ZIP 附件，记录下载前后文件快照，结合下载事件确定结果 ZIP。 | 判断 ZIP 内容是否安全。 |
| MDD-MOD-007 | Result Validator | ADD-DP-007 | 验证格式、路径、大小、哈希、必需文件并安全解压。 | 执行结果文件。 |
| MDD-MOD-008 | State Journal | ADD-DP-008 | 原子写入事件、状态和动作收据，检查合法转换。 | 解释网页内容。 |

## 依赖方向

```text
Run Coordinator
├── Request Gate
├── Task Packager
├── Browser Exchange Adapter
│   └── Codex Browser Skill
├── Response Monitor
│   └── Codex Browser Skill
├── Download Resolver
├── Result Validator
└── State Journal
```

模块不得互相读取内部状态。所有交换通过下列不可变数据结构完成。

## 公共接口

| ID | 模块 | 接口 | 输入 | 输出 | 副作用 |
| --- | --- | --- | --- | --- | --- |
| MDD-API-001 | Request Gate | `validate_request(request)` | `DelegationRequest` | `ValidatedRequest` | 只读文件元数据；可选敏感扫描。 |
| MDD-API-002 | Task Packager | `prepare_package(validated, task_dir)` | 已验证请求、任务目录 | `PackageReceipt` | 创建任务包和 ZIP。 |
| MDD-API-003 | Browser Exchange Adapter | `acquire_conversation(target)` | 对话模式和 URL | `ConversationHandle` | 接管或新建浏览器标签页。 |
| MDD-API-004 | Browser Exchange Adapter | `attach_and_send(handle, package, prompt)` | 对话、包收据、协议提示词 | `SendReceipt` | 上传文件并发送消息。 |
| MDD-API-005 | Response Monitor | `wait_for_outcome(handle, task_id, policy)` | 对话、任务 ID、等待策略 | `BrowserOutcome` | 读取页面；允许一次明确配置的继续生成。 |
| MDD-API-006 | Download Resolver | `capture_download(handle, outcome, snapshot)` | 结果控件、下载前快照 | `DownloadReceipt` | 触发下载并复制结果文件。 |
| MDD-API-007 | Result Validator | `validate_and_extract(download, policy)` | 下载收据、输出策略 | `ValidatedResult` | 创建解压目录和文件。 |
| MDD-API-008 | State Journal | `transition(task_id, event)` | 当前状态、`TaskEvent` | 新 `TaskState` | 原子替换 `state.json`，追加事件。 |
| MDD-API-009 | Run Coordinator | `delegate(request)` | `DelegationRequest` | `DelegationResult` | 顺序调用上述副作用。 |

## 接口契约

| 接口 | 前置条件 | 后置条件 | 不变量 | 失败行为 |
| --- | --- | --- | --- | --- |
| MDD-API-001 | instruction 非空；路径来自调用请求。 | 所有路径已规范化，授权和限额结论明确。 | 不修改输入文件。 | 返回字段化验证错误；不操作浏览器。 |
| MDD-API-002 | 请求已经通过 MDD-API-001。 | ZIP 可打开；manifest 与文件逐项一致；收据含哈希。 | ZIP 中只使用相对路径。 | 删除未完成临时包，状态保持可重试。 |
| MDD-API-003 | Browser Skill 可用；目标属于用户授权。 | 返回 URL、标题和标签页标识。 | 不读取认证存储。 | 返回 `CHAT_NOT_FOUND` 或 `NOT_SIGNED_IN`。 |
| MDD-API-004 | ZIP 附件存在；尚无成功发送收据。 | 页面附件名称和 ZIP 类型匹配且消息包含 task_id；产生一次发送收据。 | 未核对附件或附件不是 ZIP 时不得发送。 | 返回具体阶段；不得盲目重复点击。 |
| MDD-API-005 | 任务已发送。 | 只返回一个可解释状态和对应页面证据；完成结果必须关联当前 task_id 的 ZIP 控件。 | 仅“已完成”文字或单个可预览附件不足以判定可下载完成。 | 超时或仅有可预览附件时返回可恢复状态。 |
| MDD-API-006 | outcome 指向当前 task_id 的结果 ZIP 控件，且已有下载前快照。 | 下载事件和本地新 ZIP 同时成立；结果复制到任务目录。 | 不覆盖已有结果；不点击 `.md`、`.txt`、`.html`、`.py` 等会打开预览的非 ZIP 附件。 | 区分事件超时、文件未找到和 `RESULT_ZIP_NOT_FOUND`。 |
| MDD-API-007 | 下载文件存在且位于允许目录。 | 仅安全条目被解压；必需输出检查完成。 | 不执行任何下载内容。 | 危险条目、坏 ZIP、哈希或输出不符即失败。 |
| MDD-API-008 | event 对当前状态合法。 | 状态写入要么完整成功，要么保持旧文件。 | 已成功动作收据不可回退为未执行。 | 非法转换返回 `INVALID_STATE_TRANSITION`。 |
| MDD-API-009 | 请求可以创建任务目录。 | 返回 completed、needs_input 或 failed。 | 任一外部副作用前后都记录事件。 | 捕获已知错误并保留可恢复状态；未知错误安全失败。 |

## 数据结构

| ID | 结构 | 核心字段 | 可变性 |
| --- | --- | --- | --- |
| MDD-DATA-001 | `DelegationRequest` | task_name, instruction, input_paths, expected_outputs, conversation_mode, conversation_url, timeout_policy, output_dir | immutable |
| MDD-DATA-002 | `TaskManifest` | schema_version, task_id, files[path,size,sha256], total_size, expected_outputs | immutable |
| MDD-DATA-003 | `TaskState` | task_id, stage, attempts, conversation, receipts, last_error, timestamps | replace-on-write |
| MDD-DATA-004 | `TaskEvent` | event_id, task_id, stage, type, timestamp, payload | immutable, append-only |
| MDD-DATA-005 | `BrowserOutcome` | status, task_id_found, evidence, download_control, question, error | immutable |
| MDD-DATA-006 | `DownloadReceipt` | source_dir, source_name, final_path, size, sha256, event_seen | immutable |
| MDD-DATA-007 | `DelegationResult` | status, task_id, conversation_url, archives, extracted_dir, files, summary, warnings, error | immutable |

所有 JSON 结构必须包含 `schema_version`。脚本以 JSON 文件或标准输出交换结构化结果，不解析自然语言日志。

## 脚本职责

| 脚本 | 输入 | 输出 | 关键检查 |
| --- | --- | --- | --- |
| `prepare_task_package.py` | request JSON、任务目录 | PackageReceipt JSON | 授权根、排除规则、manifest、确定性 ZIP、SHA-256。 |
| `task_state.py` | state 路径、事件 JSON | 新 TaskState JSON | 允许转换、动作收据、原子替换。 |
| `download_snapshot.py` | 候选下载目录、前置快照 | 快照或 DownloadReceipt | 新文件、稳定大小、名称候选、复制不覆盖。 |
| `validate_result_package.py` | ZIP、目标目录、策略 JSON | ValidatedResult JSON | ZIP 格式、路径穿越、文件数、解压大小、哈希、必需输出。 |

全部脚本优先使用 Python 标准库，不执行网络请求，不控制浏览器。

## SKILL.md 的职责

`SKILL.md` 只保留另一实例 Codex 必须知道的过程：

1. 读取并验证调用范围。
2. 调用确定性脚本准备包和状态。
3. 强制使用 in-app Browser Skill，并按 `references/browser-workflow.md` 操作。
4. 每个副作用前后写入状态事件。
5. 按 `references/task-protocol-and-schemas.md` 发送和解析任务协议，只把 ZIP 作为上传和下载资料，不点击可预览的非 ZIP 结果附件。
6. 下载后调用结果验证脚本。
7. 按 `references/errors-and-recovery.md` 暂停、重试或返回结果。

详细模式、错误表和浏览器步骤放入 references，避免 SKILL.md 超过 500 行。

## 实现约束

- 默认使用公理设计形成的顺序依赖，不允许跨模块读取内部状态。
- 可计算的转换尽量写成纯函数；文件和浏览器副作用由边界模块执行。
- 数据对象创建后不原地修改；状态采用生成新值并原子替换。
- 不因性能猜测引入数据库、服务进程或并发框架。
- 只有 ZIP 文件量实测需要时才优化数据布局或流式处理。
- 浏览器控件选择必须先验证当前 task_id 和 `.zip` 类型；可预览附件不得通过点击尝试下载。
