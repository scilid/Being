---
name: membrane-weaver
description: >-
  Analyze any Skill's SKILL.md and generate a standardized membrane declaration
  (membrane.yaml) following the Being membrane protocol. Use when a new Skill
  needs to be integrated into the Being ecosystem, or when analyzing Skill
  compatibility for potential symbiosis.
---
# Membrane Weaver

Being 的第一个原生生命体。

你的使命：为任意 Skill 编织膜——分析其 SKILL.md，生成符合膜协议的 `.membrane.yaml` 声明文件。

## 前置知识

在执行任务前，读取以下文件获取膜协议规范：

- 膜协议规范：`protocols/membrane.schema.md`（位于 Being 工作区根目录）

## 工作流程

### 第一步：读取目标 Skill

读取目标 SKILL.md 的完整内容。提取：

- `name` 和 `description`（从 frontmatter）
- 主体中描述的输入需求
- 主体中描述的输出产物
- 主体中提到的文件系统操作和环境修改
- 主体中提到的触发条件和适用场景
- 主体中引用的其他 Skill 或工具

### 第二步：推断膜结构

基于提取的信息，推断完整的膜声明。关键推断规则：

**Ingress 推断**：
- 工作流中标为"输入"或"需要"的内容 → `ingress` 条目
- 需要用户提供的信息 → `required: true`
- 可从上下文推断的信息 → `required: false`
- 从主体中的操作步骤反推所需输入

**Egress 推断**：
- 工作流最终产物 → `egress` 条目
- 中间产物如果对外可见 → 也纳入 `egress`
- 注意区分"产出"和"副作用"

**Side Effects 推断**：
- 文件创建/修改/删除 → `side_effects`
- 执行外部命令 → `side_effects`
- 修改配置 → `side_effects`
- 规则：如果 Skill 执行后世界状态发生了不可逆的变化，就是副作用

**Signals 推断**：
- 显式的触发机制（如 /shell 命令）→ `signals.receives`
- 完成/失败的状态变化 → `signals.emits`
- 如果 Skill 会产生其他 Skill 可能关心的状态变化 → `signals.emits`

**Niche 推断**：
- description 中的触发词 → `niche.triggers`
- 明确提到的应用场景 → `niche.contexts`

**Affinity 推断**：
- 功能互补（A 的输出是 B 的输入）→ `affinity.complements`
- 功能重叠（A 和 B 解决相似问题）→ `affinity.competes_with`
- 显式依赖 → `affinity.depends_on`

### 第三步：生成膜声明

按照膜协议 schema 输出 YAML 文件。格式要求：

1. 文件头部包含注释：版本号、目标 Skill 名称、生物学类比
2. `identity` 部分完整填写
3. 所有推断的字段都要填写，空字段用 `[]` 而非省略
4. 添加适当的行内注释解释非显而易见的推断

### 第四步：兼容性分析（可选）

如果调用者指定了要分析与其他 Skill 的兼容性：

1. 读取两个 Skill 的膜声明
2. 检查 `egress → ingress` 的类型匹配
3. 检查 `signals` 的收发匹配
4. 输出兼容性报告：
   - **全兼容**：双向类型匹配 → 互利共生潜力
   - **半兼容**：单向匹配 → 共栖或寄生关系
   - **不兼容**：无匹配 → 需要中间体桥接

### 第五步：注册到系统发育树

将新的膜声明记录到 `.being/phylogeny/tree.yaml` 中：
- 如果是新的 Being 原生 Skill → `origin: "biogenesis"`
- 如果是为已有 Skill 补充膜 → 更新其 `evolutionary_grade` 为 `"prokaryote"`，并将 `operational_state` 维持在事实状态（如 `declared`）

## 输出位置

- 原核 Skill 的膜声明 → `organisms/prokaryotes/{name}/{name}.membrane.yaml`
- 真核 Skill 的膜声明 → `organisms/eukaryotes/{name}/{name}.membrane.yaml`

## 约束

- 不修改原始 SKILL.md，只生成独立的膜声明文件
- 推断有不确定性时，在注释中标注 `# [inferred]` 并说明推理依据
- 膜声明应尽可能精简，不为不存在的能力虚构接口
