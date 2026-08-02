# RMD — Build Path

## 元数据

- document_id: RMD-0001
- status: proposed
- source_docs: URD-0001, ADD-0001, MDD-0001, TDD-0001
- last_updated: 2026-08-02

## 开发项目与安装包

开发项目保存文档、测试和 Skill 源文件：

```text
delegate-to-chatgpt-web-project/
├── pyproject.toml
├── .gitignore
├── tests/
├── skill/
│   └── delegate-to-chatgpt-web/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── scripts/
│       └── references/
├── docs/
├── wiki/
└── .vibe/
```

安装时只复制 `skill/delegate-to-chatgpt-web/`。开始实现前必须询问源码目录和安装目录；未指定时建议安装到 `$CODEX_HOME/skills`。

## 项目设置

| ID | 项目 | 决定 | 完成条件 |
| --- | --- | --- | --- |
| RMD-SETUP-001 | 文档强度 | strict | 本设计集通过检查。 |
| RMD-SETUP-002 | 语言 | Python 标准库；浏览器由 Codex Browser Skill 执行 | 技术边界写入 MDD。 |
| RMD-SETUP-003 | 包和测试 | uv、pytest、ruff | `pyproject.toml` 和测试命令可用。 |
| RMD-SETUP-004 | Skill 骨架 | 必须运行 Skill Creator 的 `init_skill.py` | SKILL.md 与 agents/openai.yaml 生成。 |
| RMD-SETUP-005 | Git | 一项任务一个分支和检查点 | 开始实现前取得干净状态。 |

## 实施原则

- risk posture: strict
- 顺序：先契约和危险文件处理，再做浏览器副作用。
- 先写失败测试和接口壳，再实现每个低自由度脚本。
- 每个切片只改变一个模块或一个接口族。
- 当前尚未提供远程仓库；PR 和合并在有远程且用户批准前记为 `skipped: no approved remote`。

## 有序任务

| ID | 任务 | 依赖 | 主要产物 | 检查 | 分支 | 完成条件 |
| --- | --- | --- | --- | --- | --- | --- |
| RMD-TASK-001 | 确认源码/安装目录，初始化 uv 开发项目和 Skill 骨架 | SETUP | pyproject、gitignore、Skill 空骨架 | `uv run pytest -q` | `feat/rmd-001-init` | Skill Creator init 完成，无多余安装包文件。 |
| RMD-TASK-002 | 固化 JSON 模式、状态枚举、错误码和 fixtures，先写失败测试 | 001 | schemas、测试 fixture、接口壳 | `uv run pytest -q tests/test_contracts.py` | `feat/rmd-002-contracts` | TDD-013–021 初始失败原因符合预期。 |
| RMD-TASK-003 | 实现 Request Gate 和 Task Packager | 002 | `prepare_task_package.py` | `uv run pytest -q tests/test_prepare_package.py` | `feat/rmd-003-package` | TDD-002、003、013、014、022、023 通过。 |
| RMD-TASK-004 | 实现 State Journal 和恢复规则 | 002 | `task_state.py` | `uv run pytest -q tests/test_task_state.py` | `feat/rmd-004-state` | TDD-008、020、028 通过。 |
| RMD-TASK-005 | 实现 Result Validator | 002 | `validate_result_package.py` | `uv run pytest -q tests/test_result_package.py` | `feat/rmd-005-result` | TDD-007、019、027 通过。 |
| RMD-TASK-006 | 实现 Download Resolver | 002, 004 | `download_snapshot.py` | `uv run pytest -q tests/test_download_snapshot.py` | `feat/rmd-006-download` | TDD-006、018、026 通过。 |
| RMD-TASK-007 | 编写 Browser workflow、任务协议和恢复 reference | 002–006 | 3 个 reference 文件 | 文档契约检查 | `feat/rmd-007-references` | 每个网页副作用有前置观察、唯一定位和后置收据。 |
| RMD-TASK-008 | 编写精简 SKILL.md 和 agents/openai.yaml | 007 | 可触发 Skill | `quick_validate.py` | `feat/rmd-008-skill` | SKILL.md <500 行；触发描述覆盖范围和非范围。 |
| RMD-TASK-009 | 用伪 Browser Adapter 完成 coordinator 集成 | 003–008 | 端到端离线测试 | `uv run pytest -q -m "not live"` | `feat/rmd-009-integration` | TDD-001–011、021、032 通过。 |
| RMD-TASK-010 | 在真实 ChatGPT Web 上进行一次受控往返 | 009 | live 测试记录 | `uv run pytest -q -m live` | `test/rmd-010-live` | TDD-012、030、033 通过或明确报告页面变化。 |
| RMD-TASK-011 | 全量校验、前向测试和安装候选版本 | 010 | 验证报告、安装包 | pytest、ruff、quick_validate、check_project_docs | `chore/rmd-011-release` | 所有门槛通过，用户批准安装位置。 |

## Git 检查点

| ID | 对应任务 | 提交信息 | PR / 合并 |
| --- | --- | --- | --- |
| RMD-GIT-001 | RMD-TASK-001 | `chore: complete RMD-TASK-001 project setup` | 无已批准远程时跳过。 |
| RMD-GIT-002 | RMD-TASK-002 | `test: define RMD-TASK-002 contracts and fixtures` | 同上。 |
| RMD-GIT-003 | RMD-TASK-003 | `feat: implement RMD-TASK-003 task packaging` | 同上。 |
| RMD-GIT-004 | RMD-TASK-004 | `feat: implement RMD-TASK-004 state journal` | 同上。 |
| RMD-GIT-005 | RMD-TASK-005 | `feat: implement RMD-TASK-005 result validation` | 同上。 |
| RMD-GIT-006 | RMD-TASK-006 | `feat: implement RMD-TASK-006 download resolver` | 同上。 |
| RMD-GIT-007 | RMD-TASK-007 | `docs: define RMD-TASK-007 runtime references` | 同上。 |
| RMD-GIT-008 | RMD-TASK-008 | `feat: write RMD-TASK-008 skill instructions` | 同上。 |
| RMD-GIT-009 | RMD-TASK-009 | `test: pass RMD-TASK-009 offline integration` | 同上。 |
| RMD-GIT-010 | RMD-TASK-010 | `test: record RMD-TASK-010 live round trip` | 同上。 |
| RMD-GIT-011 | RMD-TASK-011 | `chore: prepare RMD-TASK-011 skill release` | 用户批准后提交 PR/合并。 |

## 停止条件

| ID | 条件 | 行动 |
| --- | --- | --- |
| RMD-STOP-001 | 实现前未确定源码和安装目录 | 询问用户，不运行 `init_skill.py`。 |
| RMD-STOP-002 | 新需求改变上传授权、身份或高风险边界 | 返回 URD 更新。 |
| RMD-STOP-003 | 接口无法保持 ADD 中的单向依赖 | 返回 ADD/MDD 重做拆分。 |
| RMD-STOP-004 | 测试没有明确判定依据 | 返回 TDD。 |
| RMD-STOP-005 | 工作树存在不明用户改动 | 暂停，检查重叠范围。 |
| RMD-STOP-006 | 发现真实密钥、Cookie 或个人资料 fixture | 删除测试引用并报告，不提交。 |
| RMD-STOP-007 | live 测试需要发送真实消息但未获授权 | 不执行 live 测试。 |
| RMD-STOP-008 | 登录、验证码、新权限或页面无法可靠定位 | 返回 needs_input/PAGE_CHANGED，不绕过。 |
| RMD-STOP-009 | 单元测试、ruff、Skill 验证或文档检查失败 | 不提交发布检查点。 |

## 回退点

| ID | 时点 | 回退方法 |
| --- | --- | --- |
| RMD-RB-001 | 初始化后 | 删除新建项目目录或回退设置提交；不修改现有 Skill。 |
| RMD-RB-002 | 契约确定后 | 回退接口提交，并先修改 MDD/TDD。 |
| RMD-RB-003 | 每个脚本完成后 | 回退该任务分支，不影响其他模块。 |
| RMD-RB-004 | live 测试前 | 保留离线候选版本，不安装或发布。 |
| RMD-RB-005 | 安装候选后 | 保留上一版 Skill 目录，恢复上一版并记录失败。 |

## 发布检查

```text
uv run pytest -q
uv run ruff check .
python <skill-creator>/scripts/quick_validate.py skill/delegate-to-chatgpt-web
python <vibe-coding-skill>/scripts/check_project_docs.py --root . --level strict
```

复杂 Skill 应做独立前向测试。前向测试只传 Skill 目录和真实用户式请求，不提供预期答案或本设计结论；若测试会操作真实 ChatGPT Web，必须先取得用户允许。
