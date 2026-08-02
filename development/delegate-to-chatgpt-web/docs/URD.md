# URD — Delegate to ChatGPT Web

> 这是开发设计的需求源。原始需求依据：`outputs/Codex-ChatGPT-Web-URD-v1.1.md`。

## 元数据

- project: `delegate-to-chatgpt-web`
- document_id: URD-0001
- status: confirmed
- last_updated: 2026-08-02
- document_strength: strict

## 项目目标

| ID | 目标 | 状态 |
| --- | --- | --- |
| URD-GOAL-001 | 让 Codex 把边界明确的子任务委派给 ChatGPT Web，并通过 ZIP 完成本地资料和网页结果的双向传递。 | confirmed |
| URD-GOAL-002 | 把已验证的人工操作整理成可恢复、可检查、可重复执行的 Codex Skill。 | confirmed |

## 用户与角色

| ID | 角色 | 需要 |
| --- | --- | --- |
| URD-ROLE-001 | Codex 用户 | 指定任务、输入文件、目标对话和期望输出，并取得本地结果。 |
| URD-ROLE-002 | Codex | 调用 Skill，检查结果，并继续后续本地工作。 |
| URD-ROLE-003 | ChatGPT Web | 读取任务 ZIP，执行工作，生成结果 ZIP。 |

## 核心场景

| ID | 场景 | 结果 |
| --- | --- | --- |
| URD-SCEN-001 | 使用当前已登录对话委派文档任务。 | 上传输入 ZIP，发送任务，下载并解压结果 ZIP。 |
| URD-SCEN-002 | 新建 ChatGPT Web 对话后委派任务。 | 保存新对话 URL，并完成同样的往返流程。 |
| URD-SCEN-003 | ChatGPT Web 请求补充信息。 | Skill 返回 `needs_input`，保留状态，允许恢复。 |
| URD-SCEN-004 | 上传、生成、下载或解压失败。 | 返回明确阶段、错误代码、诊断信息和可重试性。 |

## 当前范围

| ID | 要求 | 优先级 |
| --- | --- | --- |
| URD-REQ-001 | 仅使用 Codex 内置侧边栏浏览器和当前登录会话，不依赖 API、扩展、CDP 或独立浏览器。 | must |
| URD-REQ-002 | 在上传前校验调用参数、授权路径、敏感文件、文件数量和总体积。 | must |
| URD-REQ-003 | 生成包含 `TASK.md`、`manifest.json`、`input/` 和输出要求的确定性 ZIP，并记录大小和 SHA-256。 | must |
| URD-REQ-004 | 支持当前对话、指定现有对话和新对话，并保存任务 ID 与对话 URL 的关系。 | must |
| URD-REQ-005 | 上传正确 ZIP，确认附件名称和类型后，发送包含任务 ID 的协议提示词。 | must |
| URD-REQ-006 | 识别生成中、完成、失败、需要输入、登录失效、限流和继续生成状态。 | must |
| URD-REQ-007 | 只下载与当前任务对应的结果 ZIP，记录原始位置、最终位置、大小和 SHA-256。 | must |
| URD-REQ-008 | 把下载 ZIP 视为不可信输入，阻止路径穿越，安全解压并检查必需输出。 | must |
| URD-REQ-009 | 使用持久状态机记录每个阶段，上传、发送和下载必须有重复执行保护。 | must |
| URD-REQ-010 | 返回结构化的 `completed`、`needs_input` 或 `failed` 结果。 | must |
| URD-REQ-011 | 保存非敏感日志、文件清单、校验值、状态变化和必要的失败诊断。 | must |
| URD-REQ-012 | 遇到登录、验证码、新权限、未授权资料或显著改变范围的追问时暂停。 | must |
| URD-REQ-013 | 与 ChatGPT Web 交换的输入和结果资料统一使用 ZIP。不得把点击后会进入预览状态的 `md`、`txt`、`html`、`py` 等单个附件作为下载目标；页面没有对应结果 ZIP 时返回 `needs_input` 或 `RESULT_ZIP_NOT_FOUND`。 | must |

## 非当前范围

| ID | 项目 | 原因 |
| --- | --- | --- |
| URD-OOS-001 | OpenAI API 或其他模型 API | 当前目标是使用 ChatGPT Web。 |
| URD-OOS-002 | 浏览器扩展、CDP、独立浏览器 | 内置浏览器路径已经验证。 |
| URD-OOS-003 | 多个任务并行控制同一标签页 | 增加状态竞争，不属于 MVP。 |
| URD-OOS-004 | 自动处理改变任务范围的追问 | 必须由用户授权。 |
| URD-OOS-005 | 多账号自动切换 | 涉及身份和权限。 |
| URD-OOS-006 | 模型自动选择、长期调度和跨设备执行 | 不影响首版完整往返。 |
| URD-OOS-007 | 自动执行结果 ZIP 中的代码、宏或安装程序 | 下载内容不可信。 |
| URD-OOS-008 | 使用单个可预览附件在 Codex 与 ChatGPT Web 之间交换任务资料 | 点击此类附件会进入预览状态，不是本 Skill 的下载协议。 |

## 验收条件

| ID | 关联要求 | 可测条件 | 判定依据 |
| --- | --- | --- | --- |
| URD-AC-001 | URD-REQ-001, URD-REQ-004 | Skill 接管内置浏览器中的目标 ChatGPT Web 对话。 | URL、标题和会话状态与请求一致。 |
| URD-AC-002 | URD-REQ-002 | 未授权或敏感文件在浏览器操作前被阻止。 | 返回具体路径和错误代码，页面无附件。 |
| URD-AC-003 | URD-REQ-003 | 同一输入生成相同清单和内容哈希。 | manifest 与实际文件逐项一致。 |
| URD-AC-004 | URD-REQ-005 | 页面出现正确 ZIP 附件并成功发送任务。 | 附件名、类型、任务 ID 和消息状态均正确。 |
| URD-AC-005 | URD-REQ-006 | Skill 能区分完成、需要输入和失败。 | 页面证据映射到唯一终态或暂停态。 |
| URD-AC-006 | URD-REQ-007 | 结果 ZIP 被下载并复制到任务结果目录。 | 下载事件、本地文件、大小和 SHA-256 均存在。 |
| URD-AC-007 | URD-REQ-008 | 有效 ZIP 被安全解压，危险 ZIP 被拒绝。 | 文件只出现在任务结果目录，必需输出完整。 |
| URD-AC-008 | URD-REQ-009 | 中断后恢复不会重复发送或覆盖结果。 | 状态记录和动作收据保持单次副作用。 |
| URD-AC-009 | URD-REQ-010 | 调用方获得符合约定结构的结果。 | JSON 通过模式校验。 |
| URD-AC-010 | URD-REQ-011 | 任务记录足以定位失败且不含认证信息。 | 日志字段完整，敏感字段扫描为空。 |
| URD-AC-011 | URD-REQ-012 | 登录、验证码或权限请求导致暂停。 | 未尝试绕过，结果说明需要用户处理。 |
| URD-AC-012 | URD-REQ-001–URD-REQ-011 | 复现 2026-08-02 ZIP 往返测试。 | 上传可读、网页生成 ZIP、下载哈希匹配、4 个文件可解压。 |
| URD-AC-013 | URD-REQ-013 | 页面同时出现当前任务的结果 ZIP 和可预览附件时只下载 ZIP；页面只有可预览附件时不点击。 | 浏览器动作记录中没有打开预览；有 ZIP 时下载目标唯一匹配该 ZIP，无 ZIP 时返回 `needs_input` 或 `RESULT_ZIP_NOT_FOUND`。 |

## 约束

| ID | 类型 | 约束 | 影响 |
| --- | --- | --- | --- |
| URD-CON-001 | platform | 浏览器操作必须通过可用的 Codex in-app Browser Skill。 | 浏览器细节不写入 Python 脚本。 |
| URD-CON-002 | security | 不读取或保存 Cookie、密码、令牌和认证码。 | 使用现有登录会话。 |
| URD-CON-003 | data | 上传和下载内容均视为不可信。 | 两端都需要校验。 |
| URD-CON-004 | reliability | 网页 DOM、按钮文字和下载文件名可能变化。 | 使用语义定位、状态观察和明确错误。 |
| URD-CON-005 | packaging | 实际 Skill 包必须精简，只包含 `SKILL.md`、`agents/` 和必要资源。 | 设计文档不得放入安装包。 |
| URD-CON-006 | implementation | 确定性文件操作默认使用 Python 标准库，开发依赖使用 uv。 | 减少运行时依赖。 |
| URD-CON-007 | web behavior | ChatGPT Web 会为 `md`、`txt`、`html`、`py` 等可预览附件打开预览界面，该界面不作为可靠下载路径。 | 浏览器协议只上传和下载 ZIP，不点击可预览结果附件。 |

## 假设

| ID | 假设 | 当前依据 | 复查条件 |
| --- | --- | --- | --- |
| URD-ASM-001 | 用户已经在 Codex 内置浏览器中登录 ChatGPT Web。 | 已完成实际测试。 | 登录失效或产品行为变化。 |
| URD-ASM-002 | ChatGPT Web 可以读取输入 ZIP 并生成可下载 ZIP。 | 已完成实际测试。 | ChatGPT Web 文件能力变化。 |
| URD-ASM-003 | 调用时列出的路径和目标对话构成本次任务的明确授权范围。 | URD v1.1 授权边界。 | 产品增加独立审批机制。 |

## 未决问题

| ID | 问题 | 是否阻塞设计 | 处理方式 |
| --- | --- | --- | --- |
| URD-Q-001 | 输入 ZIP 默认最大体积、文件数和单文件大小是多少？ | no | 设计为可配置；实现前确定默认值。 |
| URD-Q-002 | 上传、生成和下载的默认超时与重试次数是多少？ | no | 设计为分阶段配置。 |
| URD-Q-003 | 日志和结果默认保留多久？ | no | MVP 不自动清理，后续确定策略。 |
| URD-Q-004 | 敏感内容是否做正文扫描？ | no | MVP 先做路径和高风险文件名阻止，正文扫描进入决策点。 |
| URD-Q-005 | ChatGPT 未生成 ZIP 时是否允许自动追问一次？ | no | MVP 默认返回失败或 `needs_input`。 |
| URD-Q-006 | 实际 Skill 源码目录和安装目录放在哪里？ | no | 实现前询问；未指定时建议 `$CODEX_HOME/skills`。 |

## 完成门槛

- [x] 用户、核心任务、范围、非范围和平台约束明确。
- [x] 每项关键行为有可测验收条件。
- [x] 已确认事实、假设和未决问题分开。
- [x] 未决问题不阻塞架构设计。
- [x] 非 MVP 想法已转入 `PARKING_LOT.md`。
