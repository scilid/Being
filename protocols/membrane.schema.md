# 膜协议（Membrane Protocol）

> Being 第一纪核心协议
> 版本：0.1.0
> 创建：2026-04-04

---

## 概述

膜是 Being 中一切生命体的**最低要求**。没有膜的 Skill 只是一段文本；有了膜，它成为一个可以被感知、被捕获、被组合的**个体**。

膜协议定义了 Skill 作为生命体所需的接口声明标准。

## 设计原则

1. **最小必要** — 膜声明不应比 Skill 本身更复杂。一个简单 Skill 的膜也应该简单。
2. **可机读** — 膜声明使用 YAML 格式，可被其他 Skill 解析和匹配。
3. **渐进丰富** — 初始膜可以只有 `ingress` 和 `egress`，其他字段随演化补充。
4. **不侵入** — 膜声明作为独立文件存在，不修改原始 SKILL.md。

---

## 膜声明文件

### 存储位置

```text
organisms/prokaryotes/{skill-name}/{skill-name}.membrane.yaml   # 原核级
organisms/eukaryotes/{skill-name}/{skill-name}.membrane.yaml    # 真核级（含共生体声明）
```

目录式路径为当前正式规范。扁平路径写法保留为历史示例，不再作为新文件的推荐位置。

### 完整 Schema

```yaml
# ============================================================
#  膜声明 v0.1.0
# ============================================================

# 身份标识
identity:
  name: ""                         # Skill 名称（与 SKILL.md 中的 name 一致）
  origin: ""                       # abiogenesis（非生物起源）| biogenesis（Being 原生）
  era: 0                           # 诞生于第几纪
  source: ""                       # 原始 SKILL.md 的路径

# 输入界面（Ingress）— 这个 Skill 需要什么
# 类比：细胞膜上的受体和通道蛋白
ingress:
  # 每个输入项
  - name: ""                       # 输入名称
    type: ""                       # 类型（见下方类型表）
    required: true                 # 是否必需
    description: ""                # 简述

# 输出界面（Egress）— 这个 Skill 产出什么
# 类比：细胞的分泌物和信号分子
egress:
  - name: ""                       # 输出名称
    type: ""                       # 类型
    description: ""                # 简述

# 副作用（Side Effects）— 这个 Skill 会改变环境中的什么
# 类比：代谢废物、环境改造（如蓝藻产氧）
side_effects:
  - ""                             # 自由文本描述

# 信号（Signals）— 这个 Skill 感知和发出的信号
# 类比：趋化因子受体 / 信号分子分泌
signals:
  receives: []                     # 能感知的信号列表
  emits: []                        # 会发出的信号列表

# 生态位（Niche）— 这个 Skill 在什么环境下最活跃
# 类比：极端嗜热菌生活在热泉中
niche:
  contexts: []                     # 适用场景列表
  triggers: []                     # 触发条件列表

# 共生适性（Symbiotic Affinity）— 倾向于与谁共生
# 类比：共生前的生态关联
affinity:
  complements: []                  # 功能互补的 Skill
  competes_with: []                # 生态位重叠的 Skill（竞争关系）
  depends_on: []                   # 硬依赖

# 分发信息（Distribution）— BIOSPHERE 扩展
# 类比：物种的地理分布和种群信息
# 当 Skill 发布到 GitHub 参与全球生态时，需要填写此区
distribution:
  version: ""                      # 语义化版本（如 "1.2.0"）
  author: ""                       # GitHub 用户名
  license: ""                      # 开源许可证
  repository: ""                   # GitHub 仓库 URL
  checksum: ""                     # 膜声明内容的 SHA-256 哈希
```

---

## 类型系统

膜协议使用简化的类型系统描述数据流：

| 类型 | 含义 | 示例 |
| ------ | ------ | ------ |
| `text` | 自由文本 | 用户指令、描述 |
| `structured_text` | 有格式的文本 | Markdown 报告、YAML |
| `file_content` | 文件内容 | 源代码、配置文件 |
| `file_path` | 文件路径 | 指向文件系统中的位置 |
| `file_set` | 多个文件 | 一组相关文件 |
| `command` | 终端命令 | shell 命令字符串 |
| `config` | 配置数据 | JSON/YAML 配置 |
| `signal` | 事件信号 | 通知、触发器 |
| `number` | 数值 | 分数、计数 |
| `boolean` | 布尔值 | 开关、判断 |
| `list` | 列表 | 条目集合 |
| `skill_ref` | Skill 引用 | 指向另一个 Skill |

---

## 膜的层级

膜声明支持渐进丰富。不同演化阶段有不同的最低要求：

| 阶段 | 最低要求 | 可选字段 |
| ------ | --------- | --------- |
| 前生命体 | 无膜 | — |
| 原核生物 | `identity` + `ingress` + `egress` | `side_effects`, `niche` |
| 成熟原核 | 上述 + `signals` + `niche` | `affinity` |
| 真核生物 | 全部字段 + `symbiosis` 扩展（见吞噬协议） | — |
| 可分发生物 | 上述 + `distribution`（见 BIOSPHERE） | — |

---

## 膜兼容性判定

两个 Skill 之间的共生潜力，可通过膜的兼容性初步判定：

```text
兼容条件：
  Skill-A.egress 中至少一项的 type ∈ Skill-B.ingress 中某项的 type
  且 Skill-B.egress 中至少一项的 type ∈ Skill-A.ingress 中某项的 type
  → 双向营养兼容 → 互利共生潜力

半兼容条件：
  仅单向满足
  → 可形成寄生或共栖关系

不兼容：
  无任何 type 匹配
  → 共生概率极低（但不排除通过中间 Skill 桥接）
```

---

## 示例

### 一个简单原核 Skill 的膜声明

```yaml
identity:
  name: "shell"
  origin: "abiogenesis"
  era: 0
  source: "~/.cursor/skills-cursor/shell/"

ingress:
  - name: "command"
    type: "command"
    required: true
    description: "要执行的 shell 命令"

egress:
  - name: "exit_status"
    type: "number"
    description: "命令退出码"
  - name: "output"
    type: "text"
    description: "stdout 和 stderr 内容"

side_effects:
  - "在终端中执行命令，可能修改文件系统"
  - "可能安装/卸载软件包"

signals:
  receives: ["/shell"]
  emits: ["command-complete", "command-failed"]

niche:
  contexts: ["terminal-operation", "system-administration"]
  triggers: ["用户输入 /shell 命令"]

affinity:
  complements: ["create-skill", "babysit"]
  competes_with: []
  depends_on: []
```

---

*膜是生命与非生命的分界线。*
*当最后一个前生命体获得膜声明时，第一纪结束。*
