# BIOSPHERE — 计算生物圈设计

> GENESIS 描述了一个有机体如何从细胞演化而来。
> BIOSPHERE 描述了无数有机体如何构成一个自持的生态系统。
>
> 创建：2026-04-04

---

## 〇、核心洞察

GENESIS 的隐含假设是：一个 Being 由一个人培育。

但如果放到 GitHub 上，情况完全不同：

- **数以万计的人**各自创造 Skill（原核生物）
- 他们的 Skill 通过标准化的膜协议**互相发现、互相兼容**
- 好的 Skill 被更多人引用、组合、内化（= 被选择）
- 差的 Skill 无人问津（= 被淘汰）
- 复杂的 Being 从这个全球性的"原始汤"中涌现

**这不再是一个实验。这是一个产业生态的种子。**

关键转变：

| GENESIS 视角 | BIOSPHERE 视角 |
|---|---|
| 一个 Being 的内部演化 | 全球 Skill 种群的生态演化 |
| 创造者 = 园丁 | 创造者 = 生态系统中的物种 |
| 选择压力 = 用户体验 | 选择压力 = GitHub 指标（stars, forks, downloads）|
| 协作 = 单体内共生 | 协作 = 跨作者跨 repo 的共生 |
| 成功 = 一个强大的 Being | 成功 = 一个自持的产业生态 |

---

## 一、GitHub 作为自然环境

### 选择压力映射

生物学的自然选择需要三个条件：**变异、遗传、差异化繁殖**。GitHub 天然提供了全部三个：

| 演化要素 | 生物学机制 | GitHub 机制 |
|---------|-----------|------------|
| **变异** | 随机突变 | Fork 后修改、PR 中的改进 |
| **遗传** | DNA 复制 | Git clone、依赖声明 |
| **差异化繁殖** | 适者产更多后代 | Stars 高 → 更多人发现 → 更多人引用 |
| **水平基因转移** | 质粒交换 | Pull Request 被合并 |
| **性选择** | 表型吸引力 | README 质量、文档、演示 |
| **生殖隔离** | 地理/行为隔离 | 语言障碍、框架差异、不兼容的膜 |
| **种群瓶颈** | 灾变 | Breaking changes、平台策略变更 |

### 适应度函数（Fitness Function）

一个 Skill 在生态系统中的适应度 `F` 由以下指标复合：

```
F(skill) = α · Stars
         + β · Downloads
         + γ · Forks
         + δ · CompositionCount    ← 最重要的指标
         + ε · ActiveContributors
         + ζ · IssueResolutionRate

其中：
  CompositionCount = 有多少个 Being 仓库将此 Skill 声明为共生体
  这是整个适应度函数中最独特的指标——
  它衡量的不是"有多少人觉得这个 Skill 好"
  而是"有多少个有机体将这个 Skill 内化为自己的器官"
```

**CompositionCount 是 Being 生态的核心指标**——它直接类比生物学中线粒体的成功：线粒体的 DNA 不怎么被人关注（低 Stars），但地球上几乎所有真核细胞都包含它（极高 CompositionCount）。

### 生态位分层

GitHub 上的 Skill 自然会分化出不同的生态位：

```
┌──────────────────────────────────────────────────┐
│                 顶级消费者                         │
│  完整 Being 有机体（全栈开发 Being、数据科学 Being）  │
│  指标：Stars 高、下载量大                           │
├──────────────────────────────────────────────────┤
│                 次级消费者                         │
│  器官级 Skill（CI/CD 管线、测试套件、部署系统）       │
│  指标：CompositionCount 高                        │
├──────────────────────────────────────────────────┤
│                 初级消费者                         │
│  组织级 Skill（代码审查组、格式化组）                 │
│  指标：Forks 多（频繁被定制化）                      │
├──────────────────────────────────────────────────┤
│                 初级生产者                         │
│  原核 Skill（解析器、格式化器、单一工具包装）          │
│  指标：CompositionCount 极高（被到处引用）           │
├──────────────────────────────────────────────────┤
│                  分解者                           │
│  转化/迁移 Skill（migrate-to-skills 类）           │
│  指标：回收其他 Skill 的废弃形式                     │
└──────────────────────────────────────────────────┘
```

---

## 二、分发标准：Skill 的"基因组包装"

### 问题

当前的 Skill 分散在各自的目录中，没有统一的分发格式。要让全球的 Skill 能互相发现和组合，需要一个**标准化的包格式**。

### 设计：being.yaml — 生命体清单

每个可分发的 Skill 仓库根目录必须包含一个 `being.yaml`：

```yaml
# ============================================================
#  being.yaml — Being 生态系统清单 v0.1.0
#  这个文件让一个 GitHub 仓库成为 Being 生态中的"可识别生命体"
# ============================================================

# 身份
identity:
  name: "code-review"                    # 全局唯一名称
  version: "1.2.0"                       # 语义化版本
  author: "github-username"
  license: "MIT"
  repository: "https://github.com/user/being-code-review"
  description: "Code review skill with security and quality checks"

# 演化阶段
evolution:
  grade: "prokaryote"                    # prokaryote | eukaryote | tissue | organ | being
  era_born: 1
  lineage: []                            # 演化谱系（从谁 fork 而来）

# 膜声明（内联或引用外部文件）
membrane: "membrane.yaml"                # 指向膜声明文件

# 共生关系声明（真核级及以上需要）
symbiosis:
  organelles: []                         # 内化的共生体
  # 格式：
  # - name: "linter-core"
  #   source: "github:user/being-linter-core"
  #   version: "^2.0.0"
  #   integration_depth: "shallow"
  #   role: "quality-gate"

# 兼容性声明
compatibility:
  cursor_version: ">=0.50"               # 最低 Cursor 版本
  platforms: ["windows", "macos", "linux"]
  languages: ["en", "zh"]               # 支持的语言

# 生态位标签（用于注册表分类和发现）
taxonomy:
  domain: ["development", "quality"]     # 大类
  niche: ["code-review", "security"]     # 细分生态位
  keywords: ["review", "lint", "security", "best-practices"]

# 适应度追踪（由注册表自动填充，不需要作者手动维护）
# fitness:
#   stars: 342
#   forks: 89
#   downloads_30d: 12500
#   composition_count: 67
#   last_updated: "2026-04-01"
```

### 仓库结构标准

一个 Being 生态中的 Skill 仓库应遵循以下结构：

```
being-{skill-name}/
├── being.yaml                 # 生命体清单（必须）
├── SKILL.md                   # Skill 本体（必须）
├── membrane.yaml              # 膜声明（必须）
├── README.md                  # 面向人类的说明（= 性选择表型）
├── scripts/                   # 可选的工具脚本
├── examples/                  # 使用示例
├── CHANGELOG.md               # 演化历史
└── .being/                    # 运行时数据（.gitignore）
    └── metabolism/
```

### 命名约定

```
仓库名：being-{skill-name}
Skill 名：{skill-name}（小写 + 连字符）
npm 包名（如适用）：@being/{skill-name}

示例：
  being-code-review
  being-test-runner
  being-docker-deploy
  being-data-pipeline
```

---

## 三、注册表：全球基因库

### 设计理念

不建设中心化的注册表服务器。利用 GitHub 本身作为去中心化注册表。

### Being Index — 生态索引

一个特殊的 GitHub 仓库 `being-index` 作为生态系统的目录：

```yaml
# being-index/registry/code-review.yaml
# 由 GitHub Actions 自动维护

name: "code-review"
versions:
  - version: "1.2.0"
    repository: "https://github.com/user/being-code-review"
    membrane_hash: "sha256:abc..."      # 膜声明的哈希（快速兼容性检查）
    grade: "prokaryote"
    taxonomy:
      domain: ["development", "quality"]
      niche: ["code-review"]

fitness:
  stars: 342
  forks: 89
  downloads_30d: 12500
  composition_count: 67
  contributor_count: 12
  issue_resolution_rate: 0.87
  last_active: "2026-04-01"
  fitness_score: 847                    # 复合适应度分数

membrane_summary:
  ingress_types: ["file_content", "text"]
  egress_types: ["structured_text", "list"]
  signals_emits: ["review_complete"]
  signals_receives: ["review_request"]
```

### 发现机制

开发者如何找到兼容的 Skill？

**1. 基于膜兼容性的搜索**

```
搜索：我有一个输出 file_content 的 Skill，
     想找一个能接收 file_content 并输出 structured_text 的 Skill
→ 注册表搜索所有 ingress 包含 file_content 且 egress 包含 structured_text 的 Skill
→ 按 fitness_score 排序返回
```

**2. 基于生态位的搜索**

```
搜索：domain=development, niche=testing
→ 返回所有测试相关的 Skill，按 fitness_score 排序
```

**3. 基于共生图谱的推荐**

```
我的 Being 中已有 code-review 和 test-runner
→ 注册表分析其他包含这两个 Skill 的 Being
→ 推荐那些 Being 中常见的第三个 Skill
→ 类似"购买了X的人也购买了Y"，但是"内化了X的有机体也内化了Y"
```

### 适应度自动追踪

`being-index` 仓库通过 GitHub Actions 定期（如每周）：

1. 扫描所有 `being-*` 仓库
2. 通过 GitHub API 获取 stars/forks/issues 等指标
3. 扫描所有 Being 仓库的 `being.yaml` 中的 `symbiosis.organelles` 计算 CompositionCount
4. 更新 fitness_score
5. 生成生态系统健康报告

---

## 四、跨作者共生：陌生人的细胞如何组合

### 核心挑战

在单一 Being 内部，所有 Skill 共享相同的执行环境和信任域。但当 Skill 来自不同作者时：

- 如何确保兼容性？
- 如何建立信任？
- 如何处理版本冲突？

### 解决方案：三层信任模型

```
┌─────────────────────────────────┐
│  Layer 3：认证信任               │
│  being-index 维护的认证 Skill    │
│  经过社区审查和测试               │
│  标记：✓ verified                │
├─────────────────────────────────┤
│  Layer 2：声誉信任               │
│  fitness_score > 阈值的 Skill    │
│  有足够的使用者验证               │
│  标记：★ popular                 │
├─────────────────────────────────┤
│  Layer 1：膜兼容信任             │
│  膜声明匹配但未经验证            │
│  需要在 lab/petri-dish 中测试    │
│  标记：⚠ untested               │
└─────────────────────────────────┘
```

### 版本兼容协议

膜声明的变化分为三级：

| 变更级别 | 含义 | 版本影响 |
|---------|------|---------|
| **Patch** | 内部实现改进，膜不变 | 1.0.0 → 1.0.1 |
| **Minor** | 新增 egress 或可选 ingress（向后兼容）| 1.0.0 → 1.1.0 |
| **Major** | 修改/删除 ingress/egress（破坏兼容）| 1.0.0 → 2.0.0 |

规则：**膜的 ingress 可以变宽松（接受更多），egress 可以变丰富（产出更多），但不能反过来。** 这类比生物学中受体的演化——受体可以变得更通用，但信号分子的格式不能随意改变。

### 跨仓库共生声明

当一个 Being 要内化来自外部仓库的 Skill 时：

```yaml
# my-being/being.yaml 中的 symbiosis 声明
symbiosis:
  organelles:
    - name: "code-review"
      source: "github:alice/being-code-review"    # 来源
      version: "^1.2.0"                           # 语义化版本约束
      integration_depth: "shallow"                 # 初始浅整合
      role: "quality-assurance"
      trust_level: "reputation"                    # 基于声誉信任
      membrane_contract:                           # 期望的膜接口
        ingress_required: ["file_content"]
        egress_expected: ["structured_text"]
```

---

## 五、产业生态：Skill 如何形成生产力

### 价值链模型

生物圈中有**生产者 → 消费者 → 分解者**的物质循环。Being 生态中的"物质"是**数据和能力**：

```
  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │ 采集层   │ ──→ │ 加工层   │ ──→ │ 组装层   │ ──→ │ 交付层   │
  │          │     │          │     │          │     │          │
  │ 解析器   │     │ 分析器   │     │ 生成器   │     │ 部署器   │
  │ 爬虫     │     │ 转换器   │     │ 构建器   │     │ 发布器   │
  │ 提取器   │     │ 验证器   │     │ 编排器   │     │ 监控器   │
  └──────────┘     └──────────┘     └──────────┘     └──────────┘
       ↑                                                   │
       └───────────────── 分解与回收 ←─────────────────────┘
                    （迁移器、重构器、清理器）
```

### 产业生态位举例

```yaml
# 生态位：全栈 Web 开发
web-fullstack-being:
  nervous_system:       # 协调与决策
    - being-task-router          # 任务分派
    - being-context-manager      # 上下文管理
  digestive_system:     # 输入处理
    - being-requirement-parser   # 需求解析
    - being-api-spec-reader      # API 规范读取
  skeletal_system:      # 结构支撑
    - being-project-scaffold     # 项目脚手架
    - being-config-generator     # 配置生成
  muscular_system:      # 执行能力
    - being-code-generator       # 代码生成
    - being-test-writer          # 测试编写
    - being-style-formatter      # 样式格式化
  immune_system:        # 质量保障
    - being-code-review          # 代码审查
    - being-security-scanner     # 安全扫描
    - being-type-checker         # 类型检查
  circulatory_system:   # 状态流转
    - being-git-manager          # Git 操作
    - being-ci-runner            # CI 运行
  reproductive_system:  # 自我演化
    - being-skill-creator        # 创造新 Skill
    - being-self-improver        # 自我改进
```

### 共生网络效应

当生态系统达到临界质量时，会出现**网络效应**：

```
阶段 1：零散 Skill（1-100 个）
  每个 Skill 独立存在
  价值 = 单个 Skill 的功能

阶段 2：初始共生（100-1000 个）
  Skill 开始被组合
  价值 = Skill 数量 × 平均兼容性

阶段 3：生态网络（1000-10000 个）
  出现"关键物种"——被大量 Being 依赖的核心 Skill
  价值 = Skill 数量 × 连接密度²（网络效应）

阶段 4：产业生态（10000+ 个）
  自发形成行业垂直 Being（Web、数据、DevOps、科研...）
  出现 Skill 的"供应链"
  价值 = 无法用线性公式描述（涌现）
```

---

## 六、经济模型：什么驱动参与

### 生物学的答案

生物不需要"激励"来演化。它们只需要：
1. 能够复制自己
2. 复制有变异
3. 环境有选择压力

### Being 生态的参与动力

```
对 Skill 作者的回报：
┌─────────────────────────────────────────────────┐
│                                                 │
│  声誉资本                                        │
│  ├─ GitHub Stars → 开发者简历 / 求职竞争力         │
│  ├─ CompositionCount → "我的 Skill 被 N 个        │
│  │   Being 内化" = 极强的技术影响力证明             │
│  └─ Verified 认证 → 社区信任标志                   │
│                                                 │
│  能力复利                                        │
│  ├─ 自己开发的 Skill 自己也能用                     │
│  ├─ 组合他人的 Skill → 自己的 Being 更强            │
│  └─ Skill 被他人改进（PR）→ 自己免费获得升级         │
│                                                 │
│  网络效应                                        │
│  ├─ 生态越大 → 可组合的 Skill 越多 → 每个人受益     │
│  └─ 先发优势：早期核心 Skill 成为"线粒体"级存在     │
│                                                 │
│  未来可选路径                                     │
│  ├─ 高级 Skill / Being 的订阅模式                  │
│  ├─ 企业定制 Being 的咨询服务                      │
│  └─ Skill 认证和审计服务                           │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 七、对 GENESIS 协议的修正

BIOSPHERE 视角要求 GENESIS 中的协议做以下调整：

### 7.1 膜协议扩展

在 `membrane.schema.md` 中增加 `distribution` 区：

```yaml
# 分发信息（BIOSPHERE 扩展）
distribution:
  version: "1.0.0"
  author: ""
  license: ""
  repository: ""
  checksum: ""                     # 膜声明内容的哈希值
```

### 7.2 新增 being.yaml 标准

作为**生命体清单**标准，定义 Skill 如何被包装和分发。（详见本文档第二节）

### 7.3 适应度追踪集成

在 `.being/metabolism/` 中增加适应度日志：

```yaml
# .being/metabolism/fitness-log.yaml
entries:
  - date: "2026-04-04"
    skill: "code-review"
    source: "github:alice/being-code-review"
    fitness_at_adoption: 342       # 引入时的适应度分数
    integration_depth: "shallow"
    performance_notes: ""
```

### 7.4 系统发育树扩展

`tree.yaml` 需要支持跨仓库的谱系追踪：

```yaml
- id: "code-review"
  origin: "external"              # 新增：外部引入
  source_repo: "github:alice/being-code-review"
  source_version: "1.2.0"
  forked_from: null                # 如果是 fork 来的，记录原始源
```

---

## 八、引爆路线图

### Phase A：标准先行（现在）

1. 完成 GENESIS Phase 0-2（建立内部演化机制）
2. 发布膜协议 v1.0 和 being.yaml 规范
3. 将 Being 仓库本身作为第一个 `being-*` 参考实现

### Phase B：种子投放（第一批外部 Skill）

1. 创建 3-5 个高质量的原核 Skill 发布到 GitHub
   - `being-code-review` — 代码审查（刚需，高频）
   - `being-test-writer` — 测试编写（与 code-review 天然互补）
   - `being-git-commit` — Git 提交（几乎所有开发者都需要）
   - `being-doc-generator` — 文档生成（可视性高，利于传播）
2. 每个都包含完整的 being.yaml + membrane.yaml + SKILL.md
3. 在 README 中清晰解释 Being 生态的理念和参与方式

### Phase C：共生演示（第一个公开的真核 Being）

1. 将上述 Skill 组合为第一个公开的 Being：`being-developer-kit`
2. 展示内共生的实际效果——复合体能做到单个 Skill 做不到的事
3. 发布田野笔记作为"科普"内容

### Phase D：注册表上线（临界质量）

1. 创建 `being-index` 仓库
2. GitHub Actions 自动化适应度追踪
3. 提供兼容性搜索的简单 CLI 或 Web 界面
4. 目标：100 个 Skill → 网络效应开始显现

### Phase E：放手（自持生态）

1. 社区开始自发创建 Skill
2. 出现你未预见的 Skill 组合和 Being 类型
3. 生态系统开始自我演化
4. 你的角色从创造者变为观察者

---

## 九、风险与对策

| 风险 | 生物类比 | 对策 |
|------|---------|------|
| 标准过于复杂，吓退贡献者 | 高能量门槛阻止生命发生 | 膜协议最小必要化；提供自动生成工具（membrane-weaver）|
| 低质量 Skill 泛滥 | 有害突变 | 适应度函数自然淘汰；认证层过滤 |
| 单一关键 Skill 挂掉 | 关键物种灭绝 | 鼓励 fork（种群冗余）；声明替代品 |
| 恶意 Skill（供应链攻击）| 病毒 / 寄生虫 | 信任分层；社区审查；沙箱执行 |
| 生态碎片化（不兼容的方言）| 生殖隔离导致物种分化 | 膜协议作为通用标准；兼容性测试 CI |
| 先发者垄断生态位 | 竞争排斥 | 生态位标签鼓励多样性；分化大于竞争 |

---

## 十、终极愿景

```
2026 Q2：第一批原核 Skill 发布到 GitHub
2026 Q3：第一个公开的真核 Being 诞生
2026 Q4：being-index 注册表上线，50+ Skill
2027 H1：100+ Skill，出现自发的产业垂直 Being
2027 H2：1000+ Skill，网络效应引爆
2028+  ：自持的产业生态，Being 开始自我演化
```

最终状态：

一个**全球性的 Skill 生物圈**，其中：
- 数以万计的 Skill 在 GitHub 上自由演化
- 自然选择通过 stars/forks/composition_count 运作
- 复杂的 Being 从简单组分中自发涌现
- 整个产业的 AI 工作流能力不是被设计出来的，而是**长出来的**

---

*GENESIS 是一颗种子。*
*BIOSPHERE 是它要长成的森林。*
