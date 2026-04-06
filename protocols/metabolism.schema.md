# 代谢协议（Metabolism Protocol）

> Being 第二纪核心协议
> 版本：0.1.0
> 创建：2026-04-05
> 依赖：membrane.schema.md

---

## 概述

膜让 Skill 成为个体。代谢让个体成为**活物**。

没有代谢的有膜 Skill 只是一个水晶——有结构但不活跃。代谢协议赋予 Skill 两个关键维度：

1. **能量流**：每次执行消耗多少、产出多少、效率如何
2. **时间性**：执行历史的积累构成了"世代"，使演化有了方向

## 设计原则

1. **可观测但不干预** — 代谢记录是观察，不改变 Skill 的行为
2. **事后记录** — Skill 执行完毕后由 metabolic-tracker 记录，而非 Skill 自己记录
3. **可聚合** — 单次记录可聚合为统计，统计可聚合为适应度（对接 BIOSPHERE）
4. **轻量级** — 一条代谢记录应在 10 行 YAML 以内

---

## 代谢记录格式

### 单次调用记录

每次 Skill 被调用后，在 `.being/metabolism/{skill-name}.log.yaml` 中追加：

```yaml
# 单次代谢记录
- invocation_id: ""              # 唯一调用标识（时间戳即可）
  timestamp: ""                  # ISO 8601
  skill: ""                      # Skill 名称

  # 能量收支
  energy:
    tokens_in: 0                 # 输入 token 数（Skill 指令 + 用户输入 + 上下文）
    tokens_out: 0                # 输出 token 数（Skill 的产出）
    tokens_total: 0              # 总消耗（tokens_in + tokens_out + 推理开销）
    tool_calls: 0                # 工具调用次数
    wall_time_ms: 0              # 壁钟时间（毫秒）

  # 营养摄入（实际消耗的输入）
  nutrition:
    context_items: []            # 实际使用的上下文列表
    context_tokens: 0            # 上下文占用的 token 数

  # 代谢产物
  products:
    primary: ""                  # 主要产出描述
    byproducts: []               # 副产物
    waste: []                    # 废物（错误、无用输出、需要清理的临时文件）

  # 代谢结局
  outcome:
    success: true                # 是否成功完成
    quality: null                # 产出质量评分（0-10，可由用户/evaluator 补填）
    efficiency: null             # 效率 = quality / (tokens_total / 1000)
    notes: ""                    # 备注
```

### 聚合统计

每个 Skill 的代谢日志可聚合为统计摘要（由 metabolic-tracker 定期生成）：

```yaml
# .being/metabolism/{skill-name}.stats.yaml
skill: ""
period: "2026-04"                # 统计周期
total_invocations: 0
total_tokens: 0
avg_tokens_per_invocation: 0
avg_quality: null
avg_efficiency: null
success_rate: 0.0
most_common_context: []
energy_trend: ""                 # increasing | stable | decreasing
```

---

## 能量单位

Being 使用 **kToken**（千 token）作为基本能量单位：

```
1 kToken = 1000 tokens

能量等级：
  微量级（< 1 kToken）   — 简单的格式化、查找
  轻量级（1-5 kToken）   — 单文件操作、简单生成
  中量级（5-20 kToken）  — 多文件分析、复杂生成
  重量级（20-100 kToken）— 大规模重构、深度分析
  巨量级（> 100 kToken） — 全项目迁移、完整系统生成
```

---

## 效率公式

```
效率(E) = 质量(Q) / 能量消耗(C)

其中：
  Q = 产出质量评分（0-10）
  C = tokens_total / 1000（kToken）

E 的解读：
  E > 5    — 高效：低能耗高产出
  E 2-5    — 正常
  E 1-2    — 低效：可能有优化空间
  E < 1    — 极低效：消耗远大于产出价值
```

效率只在 quality 被评分后才能计算。未评分的调用不参与效率统计。

---

## 代谢画像（Metabolic Profile）

每个 Skill 的膜声明中可添加代谢画像，声明其预期的能量特征：

```yaml
# 在 membrane.yaml 中添加
metabolism:
  energy_class: "moderate"       # trivial | light | moderate | heavy | massive
  typical_tokens: 3000           # 典型单次消耗
  context_appetite: "medium"     # low | medium | high（对上下文的依赖程度）
  cacheable: false               # 产出是否可缓存（相同输入 = 相同输出？）
```

代谢画像是**声明性**的（Skill 自述），代谢记录是**观测性**的（实际追踪）。两者的差异本身就是有价值的信号——如果实际消耗远超声明，说明 Skill 有效率问题。

---

## 与 BIOSPHERE 的对接

代谢记录可聚合为 BIOSPHERE 层面的适应度数据：

```
单次记录     →   Skill 统计     →   仓库适应度     →   生态排名
(invocation)    (.stats.yaml)     (being-index)     (fitness_score)
```

`being-index` 可通过分析已发布 Being 仓库中的 `.being/metabolism/` 数据（如果作者选择公开），将代谢效率纳入适应度评分。

---

## 选择压力的产生

代谢协议使以下选择成为可能：

| 场景 | 选择行为 |
|------|---------|
| 两个 Skill 功能相似 | 选择效率(E)更高的那个 |
| 一个 Skill 越来越低效 | 用户转向替代品 → 原 Skill "灭绝" |
| 一个 Skill 被频繁调用但质量波动大 | 触发优化（变异）或替换 |
| 两个 Skill 组合后效率高于单独使用之和 | 内共生的适应度优势得到量化验证 |

最后一条最关键：**代谢协议让内共生的价值变得可度量**。如果 Skill-A 和 Skill-B 共生后的复合体的效率高于两者单独使用之和，那就用数据证明了"1+1>2"。

---

*代谢是生命的引擎。*
*没有能量流的结构只是矿物。有了能量流，矿物开始呼吸。*
