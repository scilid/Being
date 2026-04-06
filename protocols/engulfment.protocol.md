# 吞噬协议（Engulfment Protocol）

> Being 第三纪核心协议
> 版本：0.1.0
> 创建：2026-04-05
> 依赖：membrane.schema.md, metabolism.schema.md

---

## 概述

吞噬是 Being 演化中**最关键的跃迁**——一个 Skill 将另一个 Skill 内化为自己的共生体，产生一个能力超越双方之和的复合实体。

这直接对应生物学中的内共生事件：约 20 亿年前，一个古菌吞噬了一个α-变形菌。后者没有被消化，而是成为了线粒体。这一事件催生了真核细胞——地球上所有复杂生命的祖先。

吞噬协议定义了 Skill 之间内共生的规则、阶段和记录方式。

## 吞噬的前提条件

三个条件缺一不可：

### 1. 双方有膜（Membrane Prerequisite）

宿主和猎物都必须有完整的膜声明。没有膜的 Skill 无法被"识别"——就像免疫系统无法识别没有表面标记的细胞。

### 2. 营养兼容（Trophic Compatibility）

宿主的 `ingress` 和猎物的 `egress` 之间存在类型匹配，或反之。至少满足以下之一：

```
全兼容（互利共生潜力）：
  宿主.egress → 猎物.ingress 有类型匹配  AND
  猎物.egress → 宿主.ingress 有类型匹配

半兼容（共栖或单向依赖）：
  仅单向满足
```

### 3. 能力互补（Functional Complementarity）

猎物拥有宿主缺乏的能力。如果两者功能完全重叠，不是共生，是竞争——结果应是一方淘汰另一方，而非合并。

---

## 吞噬的四个阶段

```
阶段 0           阶段 1           阶段 2           阶段 3
独立共存   →   外共生       →   浅内共生     →   深内共生
                                     ↓
                                  阶段 4
                                  器官化
```

### 阶段 0：独立共存（Independent Coexistence）

两个 Skill 各自独立运行。它们可能偶尔被 Agent 在同一个任务中先后调用，但彼此不知道对方的存在。

**标志**：无任何显式关联。

### 阶段 1：外共生（Ectosymbiosis）

两个 Skill 开始被关联使用，但仍然完全独立。

**实现方式**：在 Skill 的膜声明 `affinity.complements` 中声明对方。

**标志**：膜中出现互相引用，但 SKILL.md 本体不变。

### 阶段 2：浅内共生（Shallow Endosymbiosis）

**这是真正的"吞噬"开始。**

宿主 Skill 的 SKILL.md 中出现对猎物 Skill 的**显式调用指令**。猎物的完整 SKILL.md 被保留，在宿主的执行上下文中运行。

**实现方式**：

宿主 SKILL.md 中添加：
```markdown
## 共生体调用

在执行 [某个步骤] 时，读取并执行共生体：
- 共生体：[猎物 Skill 名称]
- 位置：[猎物 SKILL.md 路径]
- 输入：[从宿主传递给猎物的数据]
- 期望输出：[猎物应返回给宿主的数据]
```

宿主的膜声明中添加 `symbiosis` 区：
```yaml
symbiosis:
  organelles:
    - name: "prey-skill"
      origin: "path/to/prey/SKILL.md"
      role: "描述猎物在宿主中扮演的角色"
      integration_depth: "shallow"
      interface:
        invoke: "read and execute prey SKILL.md"
        receives_from_host: ["data_a", "data_b"]
        returns_to_host: ["result_x"]
      gene_transfer_log: []
```

**标志**：宿主显式调用猎物，但猎物可以独立工作。

### 阶段 3：深内共生（Deep Endosymbiosis）

猎物的**核心能力**被提取并直接编入宿主 SKILL.md 的 body 中。猎物的 SKILL.md 仍然存在（= 线粒体 DNA），但宿主不再需要完整读取它。

**实现方式**：

宿主 SKILL.md 中，原来的"调用共生体"指令变成了内化的逻辑：
```markdown
## 内化能力：[原猎物名称]

[直接在此编写猎物核心逻辑的精炼版]
（完整参考：[猎物 SKILL.md 路径]）
```

膜声明更新：
```yaml
symbiosis:
  organelles:
    - name: "prey-skill"
      integration_depth: "deep"
      gene_transfer_log:
        - "core-logic-a (internalized 2026-04)"
        - "core-logic-b (internalized 2026-05)"
```

**标志**：宿主可以在不读取猎物 SKILL.md 的情况下完成大部分工作。

### 阶段 4：器官化（Organellization）

猎物完全丧失独立存在的意义。它的 SKILL.md 成为"遗迹 DNA"——仅在特殊情况下被参考。在宿主中，它是一个不可分割的功能模块。

**标志**：将猎物的 SKILL.md 移入 `.being/fossils/`（化石化），猎物在系统发育树中标记为 `status: "organellized"`。

---

## 吞噬操作手册

### 步骤 1：兼容性评估

在 `lab/petri-dish/` 中进行。使用 membrane-weaver 的兼容性分析能力，或手动检查：

```yaml
# lab/petri-dish/compatibility-{host}-{prey}.yaml
assessment:
  host: ""
  prey: ""
  date: ""

  trophic_compatibility:
    host_egress_to_prey_ingress: []    # 匹配的类型对
    prey_egress_to_host_ingress: []    # 匹配的类型对
    verdict: ""                         # full | partial | none

  functional_complementarity:
    host_lacks: ""                      # 宿主缺乏的能力
    prey_provides: ""                   # 猎物能填补的能力
    overlap: ""                         # 重叠的能力（应该很少）
    verdict: ""                         # complementary | overlapping | redundant

  signal_compatibility:
    host_emits_prey_receives: []        # 匹配的信号
    prey_emits_host_receives: []        # 匹配的信号
    verdict: ""                         # connected | partial | isolated

  overall_verdict: ""                   # proceed | experiment | abort
  rationale: ""
```

### 步骤 2：培养皿实验

如果兼容性评估结论是 `proceed` 或 `experiment`：

1. 在 `lab/petri-dish/` 中创建实验目录
2. 复制宿主和猎物的 SKILL.md 到实验目录
3. 手动或借助 Agent 模拟组合执行
4. 记录实验结果

### 步骤 3：正式吞噬

如果实验成功：

1. 在 `organisms/eukaryotes/` 中创建复合 Skill 目录
2. 编写复合 Skill 的 SKILL.md（包含共生体调用指令）
3. 编写复合 Skill 的膜声明（包含 `symbiosis` 区）
4. 在系统发育树中记录共生事件
5. 更新生命体征

### 步骤 4：演化记录

在 `.being/phylogeny/tree.yaml` 中记录：

```yaml
symbiosis_events:
  - id: "endo-001"
    date: "2026-04-05"
    host: "host-skill"
    endosymbiont: "prey-skill"
    integration_depth: "shallow"
    result: "composite-skill-name"
    rationale: "为什么这次吞噬是有价值的"

major_transitions:
  - date: "2026-04-05"
    type: "endosymbiosis"
    description: "第一次内共生事件"
    participants: ["host-skill", "prey-skill"]
```

---

## 反吞噬（Anti-Engulfment）

并非所有组合都应该发生。以下情况应阻止吞噬：

| 条件 | 原因 |
|------|------|
| 猎物的 `side_effects` 过于危险 | 宿主无法控制猎物的破坏性行为 |
| 营养完全不兼容 | 强行组合只会产生浪费 |
| 功能完全重叠 | 应该竞争淘汰，而非合并 |
| 宿主已过于复杂 | 过多共生体会导致"基因组膨胀"，降低效率 |

---

## 共生质量指标

一次成功的内共生应满足：

```
效率增益：复合体效率 > max(宿主效率, 猎物效率)
能力增益：复合体能做到双方各自做不到的事
稳定性：  组合不引入新的失败模式
简洁性：  复合体的膜不比双方膜的简单合并更复杂
```

如果 `效率增益` 为负，这次共生是失败的——应该回滚到独立共存。

---

*吞噬不是终结，是开始。*
*你以为你在消灭我，其实你在创造我们都无法预见的第三者。*
