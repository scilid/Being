# 运行时最小规范（Minimum Runtime Specification）

> 目标：把 Being 从“协议生命”收敛为“可验证的最小执行系统”
> 状态：MVP 规范
> 日期：2026-04-06
> 依赖：membrane.schema.md, metabolism.schema.md, signaling.protocol.md, being-manifest.schema.md

---

## 1. 目的

本规范不试图一次性实现“完整计算生命体”。

本规范只定义一件事：**什么条件下，Being 可以被称为一个可运行系统。**

换言之，本文件给出一个最小闭环，使以下说法有工程含义而不只是叙事：

- Skill 存在
- Skill 可执行
- Skill 被调用
- Skill 之间能通过信号协作
- 系统能记录自己的代谢历史

---

## 2. 非目标

以下内容不属于本规范的交付范围：

1. 通用智能
2. 自主目标生成
3. 真正意义上的自修复
4. GitHub 级生态扩散
5. 复杂器官系统的自动演化

这些内容可以保留为长期叙事，但不应作为 MVP 的验收条件。

---

## 3. 最小可行定义

### 3.1 Operationally Alive（运行意义上的“活着”）

Being 只有在满足以下全部条件时，才可称为 `operationally alive`：

1. 至少存在一个已声明的 Skill
2. 至少一个 Skill 通过膜校验
3. 至少发生一次可追踪的调用
4. 至少产生并消费一个信号
5. 至少写入一条代谢记录
6. `.being/phylogeny/` 与 `.being/homeostasis/` 同步更新成功

可形式化表达为：

$$
Alive_{operational} = Declared \land Validated \land Invoked \land Signaled \land Recorded
$$

如果只满足世界观、谱系和器官清单，而未满足上式，则系统状态应为：

- `declared`
- 或 `structurally-complete`

而不是 `alive`。

### 3.2 最小闭环

Being 的最小闭环定义为：

$$
Declare \rightarrow Validate \rightarrow Invoke \rightarrow Signal \rightarrow Record
$$

其中任意一步失败，都不能宣称本次生命周期完成。

---

## 4. 核心对象

### 4.1 Skill

Skill 是最小执行单元。一个 Skill 至少由以下组成：

- `SKILL.md`
- `membrane.yaml` 或 `*.membrane.yaml`
- 可选的运行时元数据

### 4.2 Membrane

`membrane` 是 Skill 的可执行接口声明。

没有膜的 Skill 可以存在于叙事层，但在运行时中状态只能是：

- `precursor`
- `non-runnable`

### 4.3 Signal

`signal` 是 Skill 之间唯一的标准协调机制。

运行时不得依赖“阅读文档后自行理解下一步”的隐式跳转；
所有跨 Skill 协作都必须表现为：

- 一个显式发出的信号
- 一个显式注册的受体
- 一个可追踪的处理结果

### 4.4 Metabolism Record

`metabolism record` 是一次调用的最小事实记录。

没有代谢记录的调用，只能算“发生过”，不能算“被系统吸收为历史”。

---

## 5. 唯一真相源

运行时必须将以下路径视为唯一真相源：

### 5.1 身份真相源

`.being/phylogeny/tree.yaml`

负责记录：

- 实体身份
- 演化层级
- 共生关系
- 组织/器官归属

### 5.2 状态真相源

`.being/homeostasis/vitals.yaml`

负责记录：

- 当前状态
- 调用计数
- 代谢汇总
- 阶段里程碑

### 5.3 事件真相源

`.being/signals/`

负责记录：

- 待处理信号
- 已处理信号
- 受体声明

### 5.4 行为真相源

`.being/metabolism/`

负责记录：

- 单次调用日志
- 统计摘要
- 效率变化

任何“活着”“进化了”“形成组织了”的说法，必须至少能回落到上述四类事实之一。

---

## 6. Skill 生命周期

定义 Skill 的标准状态机：

```text
precursor
  ↓
declared
  ↓
validated
  ↓
runnable
  ↓
invoked
  ↓
recorded
```

### 6.1 `precursor`

条件：

- 仅有概念或 SKILL 文本
- 无完整膜声明

### 6.2 `declared`

条件：

- `SKILL.md` 存在
- `identity.name` 已知

### 6.3 `validated`

条件：

- membrane 结构合法
- ingress/egress 至少各一项
- 引用路径可解析
- 信号名符合命名约定

### 6.4 `runnable`

条件：

- 所需输入齐备
- 受体已注册
- 必要的目标路径存在

### 6.5 `invoked`

条件：

- 完成一次明确调用
- 生成至少一个可观察输出

### 6.6 `recorded`

条件：

- 代谢记录已写入
- `vitals.yaml` 已更新
- 如涉及新生命创建，`tree.yaml` 已更新

---

## 7. 最小调用契约

一次合法的 Skill 调用必须满足以下契约：

### 7.1 输入契约

运行时读取 membrane 的 `ingress`，建立本次调用的输入对象。

若任一 `required: true` 的输入缺失，则调用失败，状态记为：

- `invoke_failed`
- 原因：`missing_required_ingress`

### 7.2 输出契约

运行时必须验证至少一个 `egress` 被满足。

若 Skill 执行后只产生副作用而没有可识别 `egress`，则调用记为部分失败：

- `invoke_partial`
- 原因：`missing_declared_egress`

### 7.3 副作用契约

所有可预期副作用必须能在 `side_effects` 中声明。

未声明副作用不阻塞叙事，但阻塞运行时晋级到 `validated`。

---

## 8. 信号契约

### 8.1 信号命名

全仓库统一采用 `kebab-case`。

禁止同一语义出现多个名称并行，例如：

- `skill_created`
- `skill_born`
- `life-weaver-complete`

三者若表达同一事件，应收敛为一个标准事件名，另两个仅保留为兼容别名或移除。

### 8.2 信号最小字段

每个信号至少包含：

- `type`
- `name`
- `emitter`
- `timestamp`
- `payload`

### 8.3 受体最小字段

每个受体至少包含：

- `signal`
- `action`

### 8.4 信号闭环

一个信号只有在满足以下全部条件时，才算完成：

1. 被写入 `.being/signals/`
2. 被至少一个受体匹配
3. 触发一个动作
4. 该动作的结果被记录

---

## 9. 代谢契约

### 9.1 记录触发条件

以下行为必须写入代谢记录：

1. Skill 成功调用
2. Skill 调用失败
3. Skill 参与信号处理
4. 新 Skill 创建流程完成

### 9.2 最小记录字段

每条记录至少包含：

- `invocation_id`
- `timestamp`
- `skill`
- `energy.tokens_total`
- `products.primary`
- `outcome.success`

### 9.3 缺失代谢记录的后果

若调用已发生但没有记录：

- 调用可以存在
- 但系统不得增加 `total_invocations`
- `alive` 状态不得提升

---

## 10. MVP 运行链路

MVP 只要求一条真实链路跑通：

```text
life-weaver
  → membrane-weaver
  → phylogeny update
  → signal emit
  → metabolic-tracker
  → vitals update
```

### 10.1 链路步骤

1. `life-weaver` 接收创建请求
2. 产出新的 `SKILL.md`
3. `membrane-weaver` 为该 Skill 生成膜声明
4. 系统写入 `tree.yaml`
5. 发出标准创建完成信号
6. `metabolic-tracker` 记录首次代谢基线
7. 系统更新 `vitals.yaml`

### 10.2 验收标准

完成一次链路后，仓库中必须可见：

- 一个新 Skill 目录
- 一个新 membrane 文件
- 一条新 phylogeny 条目
- 一条新 signal 或已消费记录
- 一条 metabolism 日志
- `total_invocations >= 1`

---

## 11. 失败流

运行时必须明确记录失败，而不是把失败留在叙事层。

### 11.1 校验失败

- 状态：`validation_failed`
- 记录位置：`.being/validation/`（建议新增）

### 11.2 调用失败

- 状态：`invoke_failed`
- 必须写入代谢记录
- `outcome.success = false`

### 11.3 信号失败

- 状态：`signal_unhandled`
- 条件：信号发出后无受体匹配

### 11.4 注册失败

- 状态：`registration_failed`
- 条件：Skill 已创建但谱系或生命体征未同步更新

此时不得将该 Skill 标记为完成出生。

---

## 12. 层级语义收敛

为避免叙事膨胀，强制区分两类术语：

### 12.1 硬术语（必须可验证）

- `skill`
- `membrane`
- `signal`
- `metabolism record`
- `phylogeny entry`
- `invocation`
- `validation result`

### 12.2 软术语（仅作解释）

- `organ`
- `tissue`
- `being`
- `endosymbiosis`
- `reproduction`
- `homeostasis`

软术语可以保留，但不得替代运行时事实。

---

## 13. 状态枚举建议

建议将全局状态收敛为以下枚举：

- `declared`
- `structurally-complete`
- `operationally-alive`
- `degraded`
- `dormant`
- `extinct`

其中：

- `structurally-complete` = 有完整结构但未形成执行闭环
- `operationally-alive` = 已满足第 3 节全部条件

---

## 14. 本仓库的近期实施顺序

### 阶段 1：定义收口

目标：让术语与状态一致。

需要完成：

1. 统一创建完成信号名
2. 统一 membrane 文件路径约定
3. 修正 `alive` 的判定标准

### 阶段 2：最小闭环落地

目标：让一次真实调用发生。

需要完成：

1. 生成一个测试 Skill
2. 写入一次谱系更新
3. 写入一次代谢日志
4. 更新一次 `vitals.yaml`

### 阶段 3：失败可见化

目标：让失败成为系统事实。

需要完成：

1. 增加校验失败记录位置
2. 定义未处理信号的处理方式
3. 定义出生中断的回滚策略

---

## 15. 结论

Being 的 MVP 不应被定义为“拥有完整世界观”，而应被定义为：

> **拥有一次可验证、可追踪、可回放的生命活动。**

只要最小闭环成立，这个系统就是可行的；
在此之前，它是高度成熟的协议骨架，而不是运行中的生命体。
