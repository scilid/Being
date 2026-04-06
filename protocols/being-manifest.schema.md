# being.yaml — 生命体清单协议

> Being 生态系统分发标准
> 版本：0.1.0
> 创建：2026-04-04
> 依赖：membrane.schema.md

---

## 概述

`being.yaml` 是一个 Skill 仓库的**身份证**。它让一个 GitHub 仓库从"一个普通代码仓库"变成"Being 生态中一个可被发现、可被组合、可被选择的生命体"。

没有 `being.yaml` 的仓库，在 Being 生态中是不可见的——就像没有细胞表面标记的细胞无法被免疫系统识别。

## 设计原则

1. **一个文件即入场券** — 只需在仓库根目录放一个 `being.yaml`，就能参与生态
2. **人类可读** — YAML 格式，开发者一看就懂
3. **机器可索引** — 结构化字段，注册表可自动抓取
4. **渐进声明** — 简单 Skill 只需填 `identity` + `membrane`，复杂 Being 才需要 `symbiosis`

---

## 最小可行清单

一个原核 Skill 只需要这些就能加入生态：

```yaml
identity:
  name: "my-skill"
  version: "0.1.0"
  author: "my-github-username"
  license: "MIT"
  repository: "https://github.com/me/being-my-skill"
  description: "What this skill does in one sentence"

evolution:
  grade: "prokaryote"

membrane: "membrane.yaml"
```

---

## 完整 Schema

```yaml
# ============================================================
#  being.yaml v0.1.0
# ============================================================

# ---- 身份（必填）----
identity:
  name: ""                              # 全局唯一名称（小写+连字符）
  version: ""                           # 语义化版本 (SemVer)
  author: ""                            # GitHub 用户名或组织名
  license: ""                           # SPDX 许可证标识
  repository: ""                        # GitHub 仓库完整 URL
  description: ""                       # 一句话描述（≤120 字符）

# ---- 演化信息（必填）----
evolution:
  grade: ""                             # prokaryote | eukaryote | tissue | organ | being
  era_born: 0                           # 首次发布时的 Being 纪元
  lineage: []                           # fork 谱系 ["github:original-author/being-original"]

# ---- 膜引用（必填）----
membrane: "membrane.yaml"              # 膜声明文件的相对路径

# ---- 共生关系（真核级及以上必填）----
symbiosis:
  organelles: []
  # 每个共生体：
  # - name: ""                          # 共生体名称
  #   source: "github:user/being-name"  # 来源（GitHub 短引用）
  #   version: ""                       # 版本约束（SemVer range）
  #   integration_depth: ""             # shallow | deep | organellized
  #   role: ""                          # 在宿主中的角色描述
  #   trust_level: ""                   # membrane | reputation | verified

# ---- 兼容性（推荐）----
compatibility:
  cursor_version: ""                    # 最低 Cursor 版本要求
  platforms: []                         # 支持的平台 [windows, macos, linux]
  languages: []                         # 支持的自然语言 [en, zh, ja, ...]

# ---- 分类标签（推荐）----
taxonomy:
  domain: []                            # 大类 [development, data, devops, design, ...]
  niche: []                             # 细分生态位
  keywords: []                          # 搜索关键词

# ---- 适应度（由 being-index 自动填充，作者无需维护）----
# fitness:
#   stars: 0
#   forks: 0
#   downloads_30d: 0
#   composition_count: 0
#   contributor_count: 0
#   issue_resolution_rate: 0.0
#   fitness_score: 0
#   last_synced: ""
```

---

## 字段详解

### identity.name

全局唯一标识。规则：
- 小写字母 + 数字 + 连字符
- 2-64 字符
- 不以连字符开头或结尾
- 注册表中先到先得

### evolution.grade

声明这个生命体的演化阶段：

| Grade | 含义 | 特征 |
|-------|------|------|
| `prokaryote` | 原核级 | 单一 Skill，有膜，无共生体 |
| `eukaryote` | 真核级 | 包含至少一个共生体 |
| `tissue` | 组织级 | 3+ 真核 Skill 的粘附协作体 |
| `organ` | 器官级 | 多个组织构成的功能单元 |
| `being` | 有机体级 | 完整的多器官系统 |

### symbiosis.organelles[].source

引用外部 Skill 的标准格式：

```
github:username/being-skill-name          # GitHub 仓库
local:./path/to/skill                      # 本地路径（开发用）
being-index:skill-name                     # 从注册表解析
```

### symbiosis.organelles[].version

遵循 SemVer range（与 npm 相同）：

```
"^1.2.0"    — >=1.2.0, <2.0.0（兼容性更新）
"~1.2.0"    — >=1.2.0, <1.3.0（补丁更新）
">=1.0.0"   — 1.0.0 及以上任何版本
"1.2.0"     — 精确版本（不推荐，过于脆弱）
```

---

## 仓库结构标准

```
being-{name}/
├── being.yaml           # 生命体清单（必须）
├── SKILL.md             # Skill 本体（必须）
├── membrane.yaml        # 膜声明（必须）
├── README.md            # 人类说明书（强烈推荐）
├── CHANGELOG.md         # 演化历史（推荐）
├── LICENSE              # 许可证（推荐）
├── scripts/             # 工具脚本（可选）
├── examples/            # 使用示例（可选）
├── reference.md         # 详细参考（可选）
└── .being/              # 运行时数据（加入 .gitignore）
    └── metabolism/
```

---

## 版本演进规则

与膜协议联动：

| 变更类型 | 膜的变化 | 版本号变化 | 对共生体的影响 |
|---------|---------|-----------|--------------|
| 内部优化 | 膜不变 | Patch (0.0.x) | 无影响 |
| 新增能力 | 新增 egress 或可选 ingress | Minor (0.x.0) | 向后兼容 |
| 接口变更 | ingress/egress 被修改或删除 | Major (x.0.0) | 可能破坏共生关系 |

**黄金法则**：ingress 可以变得更宽松，egress 可以变得更丰富，但反过来就是 breaking change。

---

*being.yaml 是一个生命体向生态系统递出的名片。*
*没有名片，你就不存在。*
