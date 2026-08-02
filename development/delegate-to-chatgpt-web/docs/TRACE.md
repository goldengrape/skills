# TRACE — Project Map

> 机器可读副本：`.vibe/trace.json`。

## 主要追踪链

| 需求 | 功能与设计 | 模块 / 接口 | 测试 | 实施任务 |
| --- | --- | --- | --- | --- |
| URD-REQ-001, URD-REQ-004 | ADD-FR-003 → ADD-DP-003 | MDD-MOD-004 / MDD-API-003 | TDD-TEST-001, TDD-TEST-015 | RMD-TASK-007–010 |
| URD-REQ-002, URD-REQ-012 | ADD-FR-001 → ADD-DP-001 | MDD-MOD-002 / MDD-API-001 | TDD-TEST-002, TDD-TEST-013, TDD-TEST-022 | RMD-TASK-002–003 |
| URD-REQ-003 | ADD-FR-002 → ADD-DP-002 | MDD-MOD-003 / MDD-API-002 | TDD-TEST-003, TDD-TEST-014, TDD-TEST-023 | RMD-TASK-003 |
| URD-REQ-005 | ADD-FR-004 → ADD-DP-004 | MDD-MOD-004 / MDD-API-004 | TDD-TEST-004, TDD-TEST-016, TDD-TEST-024 | RMD-TASK-007–009 |
| URD-REQ-006 | ADD-FR-005 → ADD-DP-005 | MDD-MOD-005 / MDD-API-005 | TDD-TEST-005, TDD-TEST-017, TDD-TEST-025 | RMD-TASK-007–010 |
| URD-REQ-007 | ADD-FR-006 → ADD-DP-006 | MDD-MOD-006 / MDD-API-006 | TDD-TEST-006, TDD-TEST-018, TDD-TEST-026 | RMD-TASK-006, RMD-TASK-009–010 |
| URD-REQ-008 | ADD-FR-007 → ADD-DP-007 | MDD-MOD-007 / MDD-API-007 | TDD-TEST-007, TDD-TEST-019, TDD-TEST-027 | RMD-TASK-005, RMD-TASK-009–010 |
| URD-REQ-009 | ADD-FR-008 → ADD-DP-008 | MDD-MOD-008 / MDD-API-008 | TDD-TEST-008, TDD-TEST-020, TDD-TEST-028 | RMD-TASK-004, RMD-TASK-009 |
| URD-REQ-010 | ADD-FR-008 → ADD-DP-008 | MDD-MOD-001 / MDD-API-009 | TDD-TEST-009, TDD-TEST-021 | RMD-TASK-002, RMD-TASK-009 |
| URD-REQ-011 | ADD-FR-008 → ADD-DP-008 | MDD-MOD-008 / MDD-API-008 | TDD-TEST-010, TDD-TEST-029 | RMD-TASK-004, RMD-TASK-009 |
| URD-AC-012 | DEC-001, DEC-002, DEC-004 | 全流程 | TDD-TEST-012, TDD-TEST-030, TDD-TEST-033 | RMD-TASK-010–011 |

## 设计决定追踪

| 决定 | 影响 | 保护测试 |
| --- | --- | --- |
| DEC-001 | MDD-MOD-004, MDD-MOD-005, RMD-TASK-007–010 | TDD-TEST-001, TDD-TEST-030 |
| DEC-002 | MDD-MOD-002, MDD-MOD-003, MDD-MOD-006–008 | TDD-TEST-013–020, TDD-TEST-031 |
| DEC-003 | RMD-TASK-001, RMD-TASK-008, RMD-TASK-011 | Skill Creator quick validation |
| DEC-004 | RMD-TASK-009–010 | TDD-TEST-012, TDD-TEST-033 |

## Wiki 追踪

| 页面 | 回答的问题 | 来源 |
| --- | --- | --- |
| WIKI-PAGE-001 `wiki/requirements/end-to-end.md` | 完整往返必须满足什么？ | URD-GOAL-001, URD-REQ-001–012 |
| WIKI-PAGE-002 `wiki/decisions/in-app-browser.md` | 为什么只使用内置浏览器？ | DEC-001, URD-CON-001 |
| WIKI-PAGE-003 `wiki/modules/runtime.md` | 运行时模块怎样分工？ | ADD-DP-001–008, MDD-MOD-001–008 |
| WIKI-PAGE-004 `wiki/interfaces/contracts.md` | 哪些接口副作用最关键？ | MDD-API-001–009 |
| WIKI-PAGE-005 `wiki/tests/release-gates.md` | 发布前必须通过什么？ | TDD-TEST-001–033, RMD-TASK-011 |
| WIKI-PAGE-006 `wiki/paths/build-order.md` | 实现顺序是什么？ | RMD-TASK-001–011 |

## 更新规则

需求、设计参数、接口、测试或任务顺序改变时，同一修改中更新本文件、`.vibe/trace.json`、受影响 wiki 和 `CHANGELOG.md`。
| URD-Q-006 | resolved_by | DEC-005 | User confirmed C:\Users\golde\code\skills as the repository and operational root. |
| DEC-005 | implements | RMD-TASK-001 | The skill candidate and uv development project use separate repository subdirectories. |
| DEC-005 | summarized_by | wiki/decisions/repository-layout.md | Derived path summary for development use. |
| WIKI-PAGE-007 | derived_from | DEC-005 | Repository layout summary derives from the confirmed setup decision. |
