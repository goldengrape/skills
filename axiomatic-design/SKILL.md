---
name: axiomatic-design
description: 用于将用户需求文档转化为高内聚、低耦合的软件架构。基于公理设计(Axiomatic Design)理论，结合函数式编程(FP)与契约式设计(DbC)原则。适用于软件架构设计、模块划分及接口定义阶段。
---

# Axiomatic Design Skill

本 Skill 旨在辅助用户利用公理设计 (Axiomatic Design, AD) 理论，结合函数式编程 (Functional Programming, FP) 和契约式设计 (Design by Contract, DbC) 原则，从自然语言需求文档生成高质量、低耦合的软件架构设计。

## 适用场景 (When to Use)

请在以下场景使用本 Skill：
1.  **架构设计阶段**：用户提供需求文档（PRD/用户故事），需要设计系统架构。
2.  **解耦分析**：用户需要评估现有设计或新设计的模块耦合程度。
3.  **高可靠性模块设计**：需要为关键模块定义严格的接口契约（前置/后置条件）。
4.  **AI 辅助编程规划**：在开始编写代码前，先制定严谨的模块规划，以指导后续的代码生成。

## 核心工作流 (Core Workflow)

当收到用户需求时，请按照以下步骤进行分析与设计：

### Step 1: 域映射与之字形分解 (Domain Mapping & Zigzagging)

利用之字形 (Zigzagging) 方法，在不同设计域之间进行映射与分解。

1.  **客户域 (Customer Domain) -> 功能域 (Functional Domain)**
    *   **CN (Customer Needs)**: 从用户文档中提取原始需求。
    *   **FR (Functional Requirements)**: 将 CN 转化为具体的功能要求（必须是动词短语）。
        *   *原则*：FR 必须是**相互独立**的最小功能集。

2.  **功能域 (Functional Domain) -> 物理域 (Physical Domain)**
    *   **DP (Design Parameters)**: 定义实现对应 FR 的具体设计参数。
    *   *编程语境*: DP 对应 **模块 (Modules)**, **数据结构 (Data Structures)**, **类 (Classes)** 或 **算法策略 (Algorithms)**。
    *   *FP 原则*: 优先将 DP 设计为 **纯函数 (Pure Functions)** 或 **不可变数据类型 (Immutable Types)**。

3.  **层级分解**:
    *   对高层级的 FR/DP 进行分解，直到达到可以直接编码的粒度。确保每一层都在“之字形”中跳转验证。

### Step 2: 独立性公理验证 (Independence Analysis)

构建设计矩阵 $[A]$ 来验证 $FR = [A]DP$ 的关系，确保满足独立性公理。

1.  **构建矩阵**:
    *   行表示 FRs，列表示 DPs。
    *   元素 $A_{ij}$ 表示 $DP_j$ 对 $FR_i$ 的影响（可以用 `X` 大影响, `x` 小影响, `0` 无影响表示）。

2.  **诊断与处置**:
    *   **非耦合 (Uncoupled) - 对角阵**:
        *   理想状态。各模块完全独立。
    *   **准耦合 (Decoupled) - 三角阵**:
        *   可行设计。
        *   **Action**: 必须在文档中明确 **实现/调用顺序**。通常沿对角线从上到下及其依赖项顺序实现。
    *   **耦合 (Coupled) - 满阵/非三角阵**:
        *   **不可行**。违反独立性公理。
        *   **Action**: 必须 **拒绝** 该设计。指出具体的耦合点（例如 "FR1 和 FR2 共享了可变状态 S"）。
        *   **解耦策略**:
            *   **FP 策略**: 将共享状态提取为参数；使用 Reader Monad；将副作用推向系统边界。
            *   **AD 策略**: 增加新的 DP；重新定义 FR。

### Step 3: 模块化与契约设计 (Module Design with FP & DbC)

将验证通过的 DPs 转化为具体的模块规格，引入契约式设计。

1.  **FP 转化**:
    *   将 DP 映射为无副作用的函数签名。
    *   输入/输出应使用明确的类型。

2.  **DbC 定义**:
    *   为关键函数定义契约，作为 AI 编码的“规格说明书”。
    *   **Pre-condition (Requires)**: 输入必须满足的约束（如 range, not null, valid state）。
    *   **Post-condition (Ensures)**: 输出必须满足的承诺；函数执行后的系统状态保持的不变式 (Invariants)。

## 资源与模板 (Resources)

本 Skill 包含以下模板，用于生成标准文档：

1.  **公理设计分析文档 (Axiomatic Design Analysis Document)**
    *   路径: `resources/templates/ad_analysis_doc.md`
    *   用途: 记录 FR/DP 映射树、设计矩阵及耦合性诊断。

2.  **模块设计文档 (Module Design Document)**
    *   路径: `resources/templates/module_design_doc.md`
    *   用途: 定义详细的模块接口、类型签名及 DbC 契约。

## 指导原则 (Guidelines)

1.  **自然语言矩阵**: 在处理自然语言输入时，不需要画出庞大的完整矩阵。**仅针对关键的、复杂的、或疑似耦合的层级**（通常是 Level 1 或 Level 2）显式展示矩阵。
2.  **状态隔离**: 任何导致非对角线耦合的“共享状态”都是设计坏味道。在 FP 范式下，建议重构为参数传递。
3.  **契约优先**: 先写契约，再写实现。这有助于 AI 理解代码的预期行为。
