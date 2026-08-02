# 运行时模块

- page_id: WIKI-PAGE-003
- source_ids: ADD-DP-001–008, MDD-MOD-001–008
- status: derived

## 回答的问题

一次运行由哪些部分负责？

## 当前事实

- Request Gate：授权和限额。
- Task Packager：TASK、manifest 和输入 ZIP。
- Browser Exchange Adapter：目标对话、上传和发送。
- Response Monitor：页面状态分类。
- Download Resolver：下载事件和本地新文件。
- Result Validator：不可信 ZIP 的校验与解压。
- State Journal：原子状态和动作收据。
- Run Coordinator：只负责顺序和结果组合。

模块通过不可变数据和事件交换，不读取彼此内部状态。
