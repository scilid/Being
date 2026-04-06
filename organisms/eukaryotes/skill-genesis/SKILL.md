---
name: skill-genesis
description: >-
  Create new Skills that are born alive in the Being ecosystem — complete with
  membrane declarations and phylogeny registration. Use when creating any new
  Skill that should participate in the Being ecosystem, or when you want to
  create a Skill with standardized interfaces from the start.
---
# Skill Genesis

Being 的第一个真核生命体。

宿主基因组：`create-skill`（Skill 创造能力）
共生体：`membrane-weaver`（膜编织能力）

**独特能力**：创造自带膜的新生命。从 skill-genesis 诞生的 Skill，从第一刻起就是 Being 生态中可见的原核生物——它们不需要事后补充膜声明。

这是 create-skill 和 membrane-weaver 各自都做不到的事。

## 前置知识

执行前，读取以下协议规范：

- Skill 创作指南：原始 create-skill 的最佳实践（已内化于下方工作流中）
- 膜协议：`protocols/membrane.schema.md`
- 代谢协议：`protocols/metabolism.schema.md`（用于为新 Skill 添加代谢画像）

## 工作流程

### Phase 1：发现（Discovery）— 继承自 create-skill

收集新 Skill 的需求信息：

1. **目的和范围**：这个 Skill 要解决什么问题？
2. **存储位置**：Being 原生（`organisms/prokaryotes/`）、个人（`~/.cursor/skills/`）还是项目（`.cursor/skills/`）？
3. **触发场景**：什么时候 Agent 应该自动应用这个 Skill？
4. **领域知识**：Agent 需要知道哪些它不会自动知道的专业知识？
5. **输出格式**：有特定的模板或格式要求吗？
6. **Being 生态角色**：这个 Skill 在 Being 中扮演什么生物学角色？

如果有 AskQuestion 工具可用，用结构化方式高效收集。否则对话式收集。

如果从对话上下文中可以推断，直接推断，不要重复提问。

### Phase 2：设计（Design）— 继承自 create-skill

1. 起草 Skill 名称（小写+连字符，≤64 字符）
2. 编写具体的第三人称描述（包含 WHAT 和 WHEN）
3. 规划主要章节结构
4. 判断是否需要辅助文件或脚本

### Phase 3：实现（Implementation）— 继承自 create-skill

1. 创建目录结构
2. 编写 SKILL.md（含 frontmatter）
3. 创建辅助参考文件（如需要）
4. 创建工具脚本（如需要）

### Phase 4：编膜（Membrane Weaving）— 共生体 membrane-weaver 的能力

**此步骤调用共生体。** 读取并执行 membrane-weaver 的逻辑：

位置：`organisms/prokaryotes/membrane-weaver/SKILL.md`

具体执行：

1. 读取刚创建的 SKILL.md
2. 按 membrane-weaver 的推断规则分析：
   - 从工作流反推 ingress（输入需求）
   - 从产出物推断 egress（输出接口）
   - 识别 side_effects（副作用）
   - 推断 signals（信号收发）
   - 确定 niche（生态位）和 affinity（共生适性）
3. 如果新 Skill 是 Being 原生的，添加代谢画像：
   ```yaml
   metabolism:
     energy_class: ""         # trivial | light | moderate | heavy | massive
     typical_tokens: 0
     context_appetite: ""     # low | medium | high
     cacheable: false
   ```
4. 生成 `.membrane.yaml` 文件，放在 Skill 目录内

### Phase 5：注册（Phylogeny Registration）— 共生体 membrane-weaver 的能力

将新生命体注册到 Being 的系统发育树中：

1. 读取 `.being/phylogeny/tree.yaml`
2. 在 `prokaryotes` 列表中追加新条目：
   ```yaml
   - id: "{new-skill-name}"
     origin: "biogenesis"
     era_born: {current_era}
     biogenesis_number: {next_number}
     location: "{skill_directory_path}"
     membrane: "{membrane_file_path}"
     evolutionary_grade: "prokaryote"
     operational_state: "declared"
     biological_analogy: "{从对话或分析中推断}"
     notable: "{简述独特之处}"
     potential_role: "{在 Being 有机体中的潜在角色}"
     parent: "skill-genesis"
   ```
3. 更新 `.being/homeostasis/vitals.yaml` 中的种群计数

### Phase 6：验证（Verification）— 继承自 create-skill + 增强

核心质量检查：
- [ ] SKILL.md 的 description 具体且包含触发词
- [ ] description 包含 WHAT 和 WHEN
- [ ] 以第三人称书写
- [ ] SKILL.md 正文不超过 500 行
- [ ] 术语一致

结构检查：
- [ ] 文件引用不超过一层
- [ ] 渐进披露使用得当

**Being 生态检查**（membrane-weaver 共生体新增）：
- [ ] 膜声明文件存在且格式正确
- [ ] ingress 和 egress 至少各有一个条目
- [ ] 已注册到系统发育树
- [ ] 生命体征已更新

## 输出清单

一次完整的 skill-genesis 执行应产出：

```
{skill-name}/
├── SKILL.md                    # Skill 本体
├── {skill-name}.membrane.yaml  # 膜声明
├── [reference.md]              # 可选辅助文件
└── [scripts/]                  # 可选脚本
```

加上对 `.being/phylogeny/tree.yaml` 和 `.being/homeostasis/vitals.yaml` 的更新。

## 约束

- 创造的 Skill 必须有膜——无膜的 Skill 不是 Being 生态中的生命
- 膜声明应精简诚实，不为不存在的能力虚构接口
- 系统发育树的更新必须与 Skill 创建原子化完成（不能只创建 Skill 不注册）
