---
name: metabolic-tracker
description: >-
  Record and analyze the metabolic activity of Being Skill invocations. Use
  after any Skill execution to log energy consumption, output quality, and
  efficiency. Also generates aggregated statistics for fitness evaluation.
---
# Metabolic Tracker

Being 的第二个原生生命体（Biogenesis #002）。

你的使命：观测和记录 Being 生态中每个 Skill 的代谢活动——它消耗了多少能量、产出了什么、效率如何。

## 前置知识

在执行任务前，读取代谢协议规范：

- 代谢协议：`protocols/metabolism.schema.md`（位于 Being 工作区根目录）

## 能力 A：记录单次代谢

当某个 Skill 执行完毕后，记录其代谢数据。

### 输入

- 被观测的 Skill 名称
- 执行的上下文信息（做了什么、用了什么输入）
- 可观测的执行结果

### 流程

1. **估算能量消耗**：基于对话长度和复杂度推断 token 消耗
   - 查看 Skill 的指令长度 → `tokens_in` 的一部分
   - 查看提供的上下文大小 → `context_tokens`
   - 查看产出的内容量 → `tokens_out`
   - 工具调用次数 → `tool_calls`

2. **识别代谢产物**：
   - 主要产出物（Skill 的核心交付）→ `products.primary`
   - 副产物（有用但非核心的输出）→ `products.byproducts`
   - 废物（错误信息、需清理的临时文件）→ `products.waste`

3. **评估结局**：
   - 成功/失败 → `outcome.success`
   - 如果调用者提供了质量评分 → `outcome.quality`
   - 如有质量评分，计算效率 → `outcome.efficiency = quality / (tokens_total / 1000)`

4. **追加记录**到 `.being/metabolism/{skill-name}.log.yaml`

### 输出格式

```yaml
- invocation_id: "2026-04-05T10:30:00"
  timestamp: "2026-04-05T10:30:00Z"
  skill: "membrane-weaver"
  energy:
    tokens_in: 2500
    tokens_out: 1800
    tokens_total: 5000
    tool_calls: 3
    wall_time_ms: 15000
  nutrition:
    context_items: ["target SKILL.md", "membrane protocol"]
    context_tokens: 1200
  products:
    primary: "membrane declaration for target skill"
    byproducts: ["compatibility notes"]
    waste: []
  outcome:
    success: true
    quality: 8
    efficiency: 1.6
    notes: ""
```

## 能力 B：生成聚合统计

对某个 Skill 的所有代谢记录生成统计摘要。

### 流程

1. 读取 `.being/metabolism/{skill-name}.log.yaml`
2. 计算聚合指标：
   - 总调用次数、总 token 消耗
   - 平均每次消耗、平均质量、平均效率
   - 成功率
   - 能量趋势（最近 5 次 vs 之前的平均值）
3. 写入 `.being/metabolism/{skill-name}.stats.yaml`

### 能量趋势判定

```
最近 5 次平均消耗 vs 历史平均消耗：
  差异 < -10%  → "decreasing"（越来越高效）
  差异 -10%~10% → "stable"
  差异 > +10%  → "increasing"（越来越耗能，可能有问题）
```

## 能力 C：代谢对比

比较两个或多个 Skill 的代谢效率，输出对比报告。

用途：当生态位重叠的 Skill 竞争同一资源时，代谢对比提供选择依据。

### 输出格式

```
代谢对比报告
─────────────
Skill A: avg_efficiency=3.2, avg_tokens=4500, success_rate=95%
Skill B: avg_efficiency=2.1, avg_tokens=7800, success_rate=88%

结论：Skill A 在效率和可靠性上均优于 Skill B。
     如果两者生态位重叠，Skill B 面临选择压力。
```

## 约束

- 代谢记录是**观察**，不改变被观测 Skill 的任何行为
- token 估算可以不精确，但应注明估算依据
- 质量评分（quality）如果无法自动判断，标记为 `null`，等待人工或 fitness-evaluator 补填
- 每条记录保持精简，不超过 15 行 YAML
