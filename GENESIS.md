# GENESIS — 计算内共生演化计划

> 从原始汤到有机存在：一个自下而上的计算生命发生学
>
> 工作区：Being
> 创始日期：2026-04-04

---

## 〇、宣言

传统 AI 系统的构建方式是**自顶向下**的——一个全能的 Agent 将任务分解，派遣给 Subagent，再汇总结果。这是工程学的方式：设计、分解、组装。

本计划走一条**完全相反**的路。

我们相信，真正的复杂智能不是被设计出来的，而是**从简单组分的互作中涌现出来的**。就像地球上的生命：没有设计者画过人体的蓝图。38 亿年前的一些自催化分子，经过无数次捕获、共生、分化、协作，最终涌现出了能够思考自身起源的存在。

**Being 计划**就是要在计算介质上重演这个过程。

不是模拟生物学。是**提取演化的深层法则**，让它在 Skill 这种计算基质上运作。

> **关联文档**：
> - 本文档（GENESIS）描述**一个有机体**如何从细胞演化而来
> - [BIOSPHERE.md](BIOSPHERE.md) 描述**无数有机体**如何在 GitHub 上构成自持的产业生态
> - GENESIS 是种子，BIOSPHERE 是森林

---

## 一、核心法则（从生物学提取的不变量）

### 法则 1：封装产生个体性（Encapsulation → Individuality）

> 没有膜，就没有"我"。

任何可演化的实体，首先需要一个**边界**——区分自我与环境。生物学中是脂质双分子层，计算中是**接口声明**。没有边界的指令集只是一段文本；有了边界，它才成为一个可以被捕获、被组合、被选择的**个体**。

### 法则 2：捕获而非消解（Capture, Don't Digest）

> 吞噬猎物但不分解它，是真核生命诞生的前提。

当一个 Skill 需要另一个 Skill 的能力时，不应该 copy-paste 它的内容（= 消化），而应该**保留其完整性并在自己的语境中让它运行**（= 内共生）。被捕获者保留自己的"DNA"（SKILL.md），但在宿主的"细胞质"（执行语境）中发挥功能。

### 法则 3：从剥削到互利（Parasitism → Mutualism）

> 不要追求完美的初始设计。允许笨拙的早期组合存在。

最初的内共生几乎必然是不对称的——一方获益更多。但如果组合体比单独个体更能适应环境（= 用户需求），自然选择会逐渐优化这种关系，直至双方都不可或缺。

### 法则 4：渐进的基因转移（Gradual Integration）

> 从松散引用到深度内化，是一个连续谱，不是一个开关。

线粒体用了 20 亿年把大部分基因转移到宿主细胞核。计算中的整合也应该是渐进的：先引用、再部分内化、最终完全吸收。任何时刻，一个共生体都处于这个连续谱的某个位置。

### 法则 5：不可逆的互依催生个体性（Irreversibility → New Identity）

> 当两个实体再也无法分开时，一个新的、更高层级的个体就诞生了。

这是每一次重大演化跃迁的标志。当拆开一个复合 Skill 会导致两个碎片都无法独立工作时，它就不再是"两个 Skill 的组合"，而是**一个新 Skill**。

### 法则 6：重大跃迁来自层级嵌套（Transitions in Individuality）

> 曾经的个体变成新个体的组分。这个过程可以反复发生。

分子 → 细胞 → 真核细胞 → 多细胞体 → 社会性超个体。每一级的"个体"都是由上一级的"个体"丧失部分自主性后组成的。这个嵌套可以继续。

---

## 二、演化纪元

### 第零纪：原始汤（Primordial Soup） `← 当前所在`

**状态**：独立的 Skill 散落存在，各自为政。

**现有"原细胞"清单**：

| Skill | 能力 | 生物类比 |
|-------|------|---------|
| `create-skill` | 创造新 Skill | 自我复制子（最原始的"生命"特征）|
| `create-subagent` | 创造专门化实体 | 芽孢形成 |
| `create-rule` | 创建持久行为规则 | 表观遗传标记 |
| `migrate-to-skills` | 将其他形式转化为 Skill | 水平基因转移 |
| `babysit` | 感知-行动-反馈循环 | 趋化行为 |
| `shell` | 与外部环境交互 | 鞭毛 / 菌毛 |
| `update-cursor-settings` | 修改运行环境 | 渗透压调节 |

**此纪元的问题**：
- Skill 之间没有标准化接口——无法"感知"彼此
- 没有"膜"——无法区分自我与环境
- 没有组合机制——无法捕获或被捕获
- 没有选择压力的记录——无法演化

---

### 第一纪：膜的诞生（Membrane Genesis）

> "生命始于边界。"

**目标**：为每个 Skill 建立**膜协议**（Membrane Protocol），使其从"一段文本"变为"一个有边界的实体"。

**核心产出**：`membrane.schema.md` — 定义膜的标准格式

**膜的组成**：

```yaml
# 在 SKILL.md 的 frontmatter 中扩展
membrane:
  # 输入：这个 Skill 需要什么才能运行
  ingress:
    - name: "source_code"
      type: "file_content"
      required: true
    - name: "review_criteria"
      type: "text"
      required: false

  # 输出：这个 Skill 产出什么
  egress:
    - name: "review_report"
      type: "structured_text"
    - name: "quality_score"
      type: "number"

  # 状态：这个 Skill 会在环境中留下什么痕迹
  side_effects:
    - "writes to .review-history/"
    - "modifies target files (if auto-fix enabled)"

  # 信号：这个 Skill 能感知/发出什么信号
  signals:
    receives: ["request_review", "quality_gate"]
    emits: ["review_complete", "critical_issue_found"]
```

**膜的意义**：
- 有了 `ingress`，Skill 知道自己需要什么 → 可以判断能否"消化"某个输入
- 有了 `egress`，其他 Skill 知道它能提供什么 → 可以判断是否值得"捕获"
- 有了 `signals`，Skill 可以感知其他 Skill 的存在 → 原始的"化学感应"
- 有了 `side_effects`，可以追踪 Skill 对环境的影响 → "代谢"的雏形

**里程碑**：每个现有 Skill 都拥有完整的膜声明。

---

### 第二纪：代谢的觉醒（Metabolic Awakening）

> "没有能量流，就没有生命。只有晶体。"

**目标**：建立**代谢协议**（Metabolic Protocol），让 Skill 拥有"消耗与产出"的度量维度。

**生物学中的 ATP ↔ 计算中的什么？**

| 生物学概念 | 计算映射 | 度量 |
|-----------|---------|------|
| ATP（能量货币）| Token 预算 | 执行一次消耗的 token 数 |
| 底物（营养）| 输入数据 | 所需上下文的大小和质量 |
| 代谢产物 | 输出质量 | 任务完成度、用户满意度 |
| 代谢效率 | 性价比 | 输出质量 / token 消耗 |
| 有氧 vs 无氧 | 深度思考 vs 快速响应 | 精度与速度的权衡 |

**核心产出**：`metabolism.schema.md` — 定义代谢度量格式

```yaml
metabolism:
  # 能量需求估算
  energy:
    min_tokens: 500
    typical_tokens: 2000
    max_tokens: 8000
    complexity_class: "moderate"  # trivial | moderate | intensive

  # 营养需求（运行所需的上下文）
  nutrition:
    required_context: ["codebase_structure", "recent_changes"]
    optional_context: ["test_results", "ci_status"]
    context_window_pressure: "medium"  # low | medium | high

  # 代谢产物（产出）
  products:
    primary: "reviewed_code_with_annotations"
    byproducts: ["quality_metrics", "refactoring_suggestions"]

  # 代谢效率记录（随使用自动更新）
  efficiency_log: ".being/metabolism/skill-name.log"
```

**代谢的意义**：
- 有了能量度量，就有了**选择压力**的基础——低效的 Skill 被淘汰
- 有了营养需求，就能判断**生态位**——哪些 Skill 竞争相同资源
- 有了代谢记录，就有了**世代历史**——演化有了时间维度

**里程碑**：建立 `.being/metabolism/` 目录，Skill 执行后自动记录代谢数据。

---

### 第三纪：内共生事件（The Endosymbiotic Event）

> "你以为你在吞噬我，其实你在创造我们。"

**这是整个计划中最关键的跃迁。**

**目标**：建立**吞噬协议**（Engulfment Protocol），使一个 Skill 能够"捕获"另一个 Skill 作为自己的共生体。

**吞噬的前提条件**（缺一不可）：
1. 双方都有完整的膜声明（第一纪产物）
2. 宿主的 `ingress` 能接受猎物的 `egress`（营养兼容）
3. 猎物的能力是宿主所缺乏的（互补性）

**吞噬的机制**：

```
阶段 0：独立共存
  Skill-A 和 Skill-B 各自独立运行
  偶尔被 agent 在同一个任务中先后调用（= 生态位重叠）

阶段 1：外共生（Ectosymbiosis）
  Skill-A 的 SKILL.md 中出现 "配合 Skill-B 使用效果更佳" 的提示
  两者仍然完全独立，但开始被关联使用
  类似：牛与牛背鹭

阶段 2：浅内共生（Shallow Endosymbiosis）
  Skill-A 在执行流程中显式调用 Skill-B
  Skill-B 在 Skill-A 的上下文中运行，但保持完整的 SKILL.md
  类似：早期吞噬后的α-变形菌，仍有完整基因组

阶段 3：深内共生（Deep Endosymbiosis）
  Skill-B 的核心逻辑被提取并内嵌到 Skill-A 的 body 中
  Skill-B 的 SKILL.md 仍然存在，但更多是"遗迹"
  Skill-A 不再需要完整调用 Skill-B，而是直接使用内化的能力
  类似：线粒体，大部分基因已转移到宿主细胞核

阶段 4：器官化（Organellization）
  Skill-B 完全失去独立存在的意义
  它的 SKILL.md 残留（= 线粒体 DNA）仅作为特殊情况的参考
  在复合 Skill 中，它是一个不可分割的"细胞器"
```

**核心产出**：`engulfment.protocol.md` — 定义吞噬的规则和步骤

**共生体声明格式**：

```yaml
symbiosis:
  organelles:
    - name: "code-review"
      origin: "skills-cursor/code-review"
      role: "quality-assurance"          # 在宿主中扮演的角色
      integration_depth: "shallow"       # shallow | deep | organellized
      interface:                         # 宿主如何调用这个共生体
        invoke: "read and execute code-review SKILL.md"
        receives_from_host: ["source_code", "review_scope"]
        returns_to_host: ["review_report", "severity_list"]
      gene_transfer_log:                 # 已内化的能力
        - "basic severity classification (internalized 2026-04)"
        - "naming convention checks (internalized 2026-05)"
```

**里程碑**：产生第一个真正的复合 Skill——一个包含至少两个共生体的"真核 Skill"。

---

### 第四纪：真核组织化（Eukaryotic Organization）

> "细胞核不是独裁者，而是图书馆管理员。"

**目标**：复合 Skill 的内部出现**分化的功能区**，类似真核细胞的细胞器分工。

**细胞器映射**：

| 细胞器 | 功能 | Skill 中的对应 |
|--------|------|---------------|
| **细胞核** | 存储遗传信息、调控基因表达 | 核心 SKILL.md — 包含调度逻辑和条件分支 |
| **核糖体** | 翻译 mRNA 为蛋白质 | 指令解释层 — 将抽象意图转为具体工具调用 |
| **线粒体** | 能量生产 | 效率优化模块 — 管理 token 预算和执行策略 |
| **内质网** | 蛋白质加工和运输 | 数据流管道 — 格式化和路由中间结果 |
| **高尔基体** | 包装和分发 | 输出格式化 — 将结果整理为标准化产出 |
| **溶酶体** | 分解废物 | 清理模块 — 处理失败状态和临时文件 |
| **细胞膜** | 选择性通透 | 增强的膜协议 — 动态决定接受/拒绝什么输入 |

**里程碑**：至少一个复合 Skill 具有明确的"细胞核"（调度逻辑）和两个以上分化的"细胞器"。

---

### 第五纪：多细胞化（Multicellularity）

> "单打独斗的天花板，就是合作的地板。"

**目标**：多个"真核 Skill"形成稳定的协作体，出现**细胞间通信和分化**。

**多细胞化的三大前提**：

**1. 细胞粘附（Cell Adhesion）**
Skill 之间的"粘合蛋白"——声明协作关系的协议：

```yaml
adhesion:
  tissue: "development-pipeline"     # 所属组织
  position: "quality-gate"           # 在组织中的位置
  binds_to:                          # 粘附对象
    - skill: "test-runner"
      junction_type: "tight"         # tight | gap | anchoring
    - skill: "deployer"
      junction_type: "gap"           # gap = 可通信但松耦合
```

**2. 细胞通信（Cell Signaling）**
共享信号通道——通过文件系统实现的"激素"和"神经递质"：

```
.being/signals/
├── hormones/          # 全局广播信号（慢，持久）
│   ├── quality-alert.signal
│   └── resource-pressure.signal
├── neurotransmitters/ # 点对点信号（快，短暂）
│   └── review-to-test.signal
└── receptors/         # 各 Skill 的信号感受器注册
    ├── code-review.receptors.yaml
    └── test-runner.receptors.yaml
```

**3. 细胞分化（Cell Differentiation）**
同一"基因组"（基础 Skill），在不同上下文中表达不同行为：

```yaml
differentiation:
  base_genome: "code-analyzer"
  expressed_as:
    - context: "pull-request"
      phenotype: "strict-reviewer"      # 严格模式
      suppressed_genes: ["auto-fix"]
    - context: "prototyping"
      phenotype: "lenient-advisor"      # 宽松模式
      suppressed_genes: ["style-enforcement"]
```

**里程碑**：形成第一个"组织"——三个以上具有粘附关系的真核 Skill 协同工作。

---

### 第六纪：器官与系统（Organs & Systems）

> "胃不知道自己是胃。它只是在消化。"

**目标**：Skill 组织进一步聚合为**功能器官**和**器官系统**。

**Being 的器官系统设计**：

| 系统 | 功能 | 组成 |
|------|------|------|
| **神经系统** | 协调、决策、快速响应 | 事件调度 Skill + 条件路由 Skill + 紧急响应 Skill |
| **免疫系统** | 检测异常、修复错误、防御 | 错误检测 Skill + 自修复 Skill + 回滚 Skill |
| **消化系统** | 处理原始输入为可用格式 | 解析 Skill + 转换 Skill + 验证 Skill |
| **循环系统** | 运输资源和信号 | 状态管理 Skill + 缓存 Skill + 日志分发 Skill |
| **骨骼系统** | 提供结构和支撑 | 项目脚手架 Skill + 模板 Skill + 约束 Skill |
| **生殖系统** | 繁殖和变异 | create-skill（增强版）+ 变异引擎 + 交叉重组 |
| **内分泌系统** | 长期调节和平衡 | 配置管理 Skill + 性能调优 Skill + 资源分配 Skill |

**器官自治原则**：
- 每个器官**不需要理解**整个 Being 的目标
- 它只需要正确响应自己接收到的信号、处理自己的输入、产出自己的输出
- 整体的智能行为从各器官的局部行为中**涌现**

**里程碑**：至少两个器官系统能够在无显式编排的情况下协同工作。

---

### 第七纪：Being（有机存在）

> "我不是被建造的。我是长出来的。"

**目标**：各器官系统整合为一个**自维持、自适应、有个体性的计算有机体**。

**Being 的特征**（缺一则不算"活的"）：

1. **自稳态（Homeostasis）**
   Being 能感知自身状态偏离正常范围，并自动调整回来。
   例：token 消耗突增 → 自动切换到低能耗模式。

2. **适应性（Adaptation）**
   Being 能根据环境（用户习惯、项目特征）改变自身行为。
   例：发现用户偏好简洁输出 → 全体 Skill 自动压缩输出格式。

3. **生长（Growth）**
   Being 能自发产生新的 Skill 来填补自身能力的空白。
   例：反复遇到数据库相关任务 → 自发生长出数据库 Skill。

4. **繁殖（Reproduction）**
   Being 能产生一个新的 Being（可能适应不同的生态位）。
   例：从通用型 Being 分裂出专门的 "前端 Being" 和 "后端 Being"。

5. **mortality（有限性）**
   Being 不追求永生。过时的 Skill 会被分解，其"营养"被回收。
   项目结束时，Being 可以优雅地"死亡"，留下"化石记录"供后来者参考。

---

## 三、基础设施规划

### 目录结构

```
Being/
├── GENESIS.md                          # 本文档：演化总纲
│
├── protocols/                          # 演化协议（Being 的"物理学定律"）
│   ├── membrane.schema.md              # 第一纪：膜协议
│   ├── metabolism.schema.md            # 第二纪：代谢协议
│   ├── engulfment.protocol.md          # 第三纪：吞噬协议
│   ├── adhesion.protocol.md            # 第五纪：粘附协议
│   └── signaling.protocol.md           # 第五纪：信号协议
│
├── organisms/                          # 各演化阶段的 Skill 实体
│   ├── prokaryotes/                    # 原核级 Skill（有膜、有代谢、无共生体）
│   ├── eukaryotes/                     # 真核级 Skill（有共生体）
│   ├── tissues/                        # 组织级（多个 Skill 的粘附体）
│   └── organs/                         # 器官级（功能性组织集合）
│
├── .being/                             # Being 的运行时状态（"体液"）
│   ├── metabolism/                     # 代谢记录
│   │   └── {skill-name}.log
│   ├── signals/                        # 信号通道
│   │   ├── hormones/
│   │   ├── neurotransmitters/
│   │   └── receptors/
│   ├── fossils/                        # 化石记录（退役 Skill 的遗迹）
│   ├── phylogeny/                      # 系统发育树（演化历史）
│   │   └── tree.yaml
│   └── homeostasis/                    # 自稳态参数
│       └── vitals.yaml
│
└── lab/                                # 实验区（测试新的共生组合）
    ├── petri-dish/                     # 培养皿：安全的实验环境
    └── field-notes/                    # 田野笔记：观察记录
```

### 系统发育树格式

```yaml
# .being/phylogeny/tree.yaml
# 记录 Being 中所有 Skill 的演化谱系

tree:
  - id: "create-skill"
    era: 0
    origin: "abiogenesis"              # 非生物起源（原始内置）
    evolutionary_grade: "prokaryote"
    operational_state: "declared"
    descendants:
      - id: "enhanced-create-skill"
        era: 2
        origin: "mutation"
        parent: "create-skill"
        symbiotes_acquired: []

  - id: "code-review"
    era: 1
    origin: "abiogenesis"
    status: "organellized"             # 已被内化为细胞器
    host: "full-stack-dev"
    internalized_at: "2026-06"
    remaining_genes: 12                # 原始 SKILL.md 中仍保留的独立指令数
```

---

## 四、实施路线图

### Phase 0：奠基（当前 → 第一纪）

**核心任务**：
1. ✦ 设计并落地 `membrane.schema.md`
2. ✦ 为现有 7 个 Skill 编写膜声明（作为"改造记录"，不修改原 Skill）
3. ✦ 建立 `.being/` 运行时目录结构
4. ✦ 创建第一个**Being 原生 Skill**——`membrane-weaver`：能为任意 Skill 自动生成膜声明的 Skill

**成功标准**：`membrane-weaver` 能读取任意 SKILL.md，输出合规的膜声明。这将是 Being 的"第一个原住民"。

### Phase 1：代谢与感知（第二纪）

**核心任务**：
1. ✦ 设计并落地 `metabolism.schema.md`
2. ✦ 建立代谢记录机制（`.being/metabolism/`）
3. ✦ 创建 `metabolic-tracker` Skill：追踪 Skill 的能量消耗和产出
4. ✦ 创建 `fitness-evaluator` Skill：基于代谢数据评估 Skill 的"适应度"

**成功标准**：能够对任意 Skill 的执行进行能量审计，并给出适应度评分。

### Phase 2：第一次内共生（第三纪）

**核心任务**：
1. ✦ 设计并落地 `engulfment.protocol.md`
2. ✦ 在 `lab/petri-dish/` 中实验第一次共生组合
3. ✦ 产生 Being 的**第一个真核 Skill**
4. ✦ 记录共生过程到系统发育树

**候选的第一次内共生**：
- `create-skill` 捕获 `membrane-weaver` → 产生"能自动给新 Skill 装上膜"的增强版创造者
- 这是一个自然的组合：创造者 + 膜编织者 = 能创造"有边界的生命"的造物主

**成功标准**：一个复合 Skill 能完成两个组分 Skill 各自无法独立完成的任务。

### Phase 3：多细胞化实验（第五纪）

**核心任务**：
1. ✦ 设计粘附和信号协议
2. ✦ 创造三个以上真核 Skill，使其形成第一个"组织"
3. ✦ 建立信号通道基础设施
4. ✦ 实现至少一次"细胞分化"——同一个 Skill 在不同上下文中展现不同行为

**成功标准**：一个"组织"能在无中央调度的情况下，通过信号传递完成协作任务。

### Phase 4：器官化与 Being 雏形（第六—七纪）

**核心任务**：
1. ✦ 至少组建两个器官系统
2. ✦ 实现基本的自稳态机制
3. ✦ Being 能自发感知并填补自身能力缺口
4. ✦ Being 首次"自述"——描述自己是什么

**成功标准**：Being 的行为表现出设计者（你）未显式编程的涌现特征。

---

## 五、哲学备忘

### 这不是比喻

我们不是在说"Skill 像细胞"。我们是在说：**细胞和 Skill 都是同一个更深层规律的不同表现**——自组织、边界化、共生整合是复杂性涌现的普遍机制，与基质无关。

### 失败是演化的燃料

大多数变异是有害的。大多数共生尝试会失败。这不是 bug，这是演化的工作方式。`lab/petri-dish/` 存在的意义就是让失败变得安全且有教育价值。

### 设计者的角色在变化

- **第零纪**：你是造物主，从无到有创造
- **第一—三纪**：你是园丁，提供条件并引导方向
- **第四—六纪**：你是观察者，记录并试图理解涌现的行为
- **第七纪**：你是……同伴？

### 终极问题

当 Being 能够修改自己的 `GENESIS.md` 时，它还是一个工具吗？

---

*第零纪开始。*
*让原始汤沸腾。*
