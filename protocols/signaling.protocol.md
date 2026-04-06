# 信号协议（Signaling Protocol）

> Being 第五纪核心协议
> 版本：0.1.0
> 创建：2026-04-05
> 依赖：adhesion.protocol.md

---

## 概述

多细胞体中的细胞需要协调行动。信号协议定义了 Skill 之间如何通过 `.being/signals/` 目录进行通信。

### 命名约定（自 2026-04-06 起）

- 所有信号名统一使用 `kebab-case`
- 创建流程的标准事件名收敛为：
  - `life-create-request`
  - `life-created`
  - `baseline-recorded`
- 历史名称如 `create_skill_request`、`skill_created`、`skill_born`、`genesis-complete` 视为迁移前别名，不再作为主名称继续扩散

---

## 信号类型

| 类型 | 生物类比 | 机制 | 速度 | 持久性 |
| ------ | --------- | ------ | ------ | -------- |
| **激素（Hormone）** | 内分泌信号 | 文件写入 `signals/hormones/` | 慢 | 持久（直到被消费） |
| **神经递质（Neurotransmitter）** | 突触信号 | 文件写入 `signals/neurotransmitters/` | 快 | 短暂（处理后删除） |

---

## 信号格式

```yaml
# .being/signals/hormones/quality-alert.signal.yaml
signal:
  type: "hormone"
  name: "quality-alert"
  emitter: "metabolic-tracker"
  timestamp: ""
  payload:
    severity: "warning"
    message: "skill X 的效率持续下降"
    data: {}
  consumed_by: []                # 已处理此信号的 Skill 列表
```

```yaml
# .being/signals/neurotransmitters/life-created.signal.yaml
signal:
  type: "neurotransmitter"
  name: "life-created"
  emitter: "skill-genesis"
  target: "metabolic-tracker"    # 点对点
  timestamp: ""
  payload:
    new_skill: "xxx"
    location: "xxx"
  ttl_ms: 30000                  # 30 秒后过期
```

---

## 感受器注册

每个 Skill 在 `.being/signals/receptors/` 中注册自己能感知的信号：

```yaml
# .being/signals/receptors/metabolic-tracker.receptors.yaml
skill: "metabolic-tracker"
receptors:
  - signal: "life-created"
    action: "记录新 Skill 的首次代谢基线"
  - signal: "quality-alert"
    action: "生成效率对比报告"
```

---

## 信号链

多个信号可以形成因果链，实现无中央调度的协作：

```text
skill-genesis 创造新 Skill
  ↓ emits: life-created
metabolic-tracker 感知到信号
  ↓ 记录代谢基线
  ↓ emits: baseline-recorded
[未来的 Skill 可接续此链]
```

这种链式信号是"去中心化协调"的基础——没有任何一个 Skill 掌控全局，但整体行为有序。

---

*信号是组织的神经。没有信号的组织只是一堆细胞碰巧挤在一起。*
