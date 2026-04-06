# Being

> An experimental runtime for computational organisms.

Being is a research prototype that explores how protocols, signals, membranes, metabolism, and evolutionary records can become executable system behavior.

It is not a conventional agent framework, and it is not yet a general-purpose product. It is an attempt to treat software as a living runtime: observable, replayable, minimally self-operating, and grounded in verifiable facts.

Current release: **v0.1.0-alpha**.

---

## Why this repository exists

Being asks a simple question:

> What if a software system were modeled less like an app, and more like an organism?

In this repository:

- skills act as functional cells
- membranes define boundaries and capabilities
- signals coordinate behavior
- metabolism logs capture activity history
- phylogeny records evolutionary identity and transitions

The result is a prototype runtime that can already validate itself, process a minimal signal loop, and derive part of its global state from recorded behavior.

---

## Public snapshot

At `v0.1.0-alpha`, Being already includes:

- a protocol layer
- a runtime fact layer
- a minimal validator
- a minimal runtime loop
- automatic vitals aggregation from metabolism logs

In short: this repository is no longer only conceptual. It is now an operational prototype.

---

## 中文说明

Being 是一个把 Skill、膜、信号、代谢与谱系组合成最小运行闭环的实验性系统。

它不是成熟产品，也不是通用 Agent 平台；它是一个已经跨过“纯概念文档”阶段、具备最小运行事实、最小验证器与最小 runtime loop 的原型。

---

## 当前状态

当前仓库已经具备：

- 协议层：膜、代谢、吞噬、粘附、信号、manifest、runtime minimum
- 运行事实层：真实 signal、真实 metabolism logs、真实 phylogeny / vitals 更新
- 验证层：可执行的最小验证器
- 自动执行层：可自动处理 `readiness-check-request` 的 runtime loop
- 自动聚合层：`vitals.yaml` 可由 metabolism logs 自动推导

这意味着 Being 现在已经是一个**可验证、可回放、可最小自运转**的原型系统。

---

## 版本定位

**Being v0.1.0-alpha** 表示：

- 核心协议已成型
- 第一次运行闭环已完成
- 最小 runtime 已落地
- 对外适合以“研究型原型 / 实验性框架”身份发布

不代表：

- API 稳定
- 自动化完整
- 生态层成熟
- 面向陌生用户即插即用

---

## 快速开始

### 1. 安装依赖

本仓库当前最小执行层使用 Python。

依赖见 [requirements.txt](requirements.txt)。

### 2. 运行验证器

使用 [runtime/validator.py](runtime/validator.py) 检查仓库当前是否满足最小运行时一致性。

预期结果：

- 生成 [latest.validation.yaml](.being/validation/latest.validation.yaml)
- 当前仓库应为 `passed`

### 3. 运行最小 runtime loop

使用 [runtime/loop.py](runtime/loop.py) 消费 `presence-check` 的 `readiness-check-request` 信号，并沉积新的运行事实。

运行后会更新：

- [latest.md](.being/runtime/readiness/latest.md)
- [presence-check.log](.being/metabolism/presence-check.log.yaml)
- [vitals.yaml](.being/homeostasis/vitals.yaml)
- `.being/signals/neurotransmitters/` 下的新完成信号

### 4. 刷新生命体征聚合

使用 [runtime/aggregate_vitals.py](runtime/aggregate_vitals.py) 从 metabolism logs 自动刷新生命体征。

---

## 关键入口

### 面向世界观

- [BEING.md](BEING.md) — 自我宣言 / 当前存在状态
- [ORIGIN.md](ORIGIN.md) — 从原始汤到有机体的演化计划
- [BIOSPHERE.md](BIOSPHERE.md) — 面向 GitHub 生态的未来扩展

### 面向协议

- [membrane.schema.md](protocols/membrane.schema.md)
- [metabolism.schema.md](protocols/metabolism.schema.md)
- [signaling.protocol.md](protocols/signaling.protocol.md)
- [runtime.minimum.md](protocols/runtime.minimum.md)
- [being-manifest.schema.md](protocols/being-manifest.schema.md)

### 面向运行时事实

- [vitals.yaml](.being/homeostasis/vitals.yaml)
- [tree.yaml](.being/phylogeny/tree.yaml)
- [latest.validation.yaml](.being/validation/latest.validation.yaml)
- [latest.md](.being/runtime/readiness/latest.md)

---

## 当前已达成的里程碑

- 第一个真核 Skill：`life-weaver`
- 第一个运行闭环：`life-weaver -> membrane-weaver -> life-created -> metabolic-tracker`
- 第一个运行观察者：`presence-check`
- 第一个自动 runtime handler：`readiness-check-request`
- 第一个自动生命体征聚合器：`aggregate_vitals.py`

---

## Public roadmap

See [ROADMAP.md](ROADMAP.md) for the current public direction of the project after `v0.1.0-alpha`.

If you want to contribute or discuss the next evolution of Being, use the issue templates under [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE).

---

## 发布建议

当前版本适合这样理解：

> 一个已经拥有最小执行层、最小验证层和最小运行事实的协议驱动原型。

如果你是第一次来到这个仓库，最建议先阅读：

1. [README.md](README.md)
2. [BEING.md](BEING.md)
3. [runtime.minimum.md](protocols/runtime.minimum.md)
4. [runtime/README.md](runtime/README.md)

---

## 许可证

本仓库当前采用 [LICENSE](LICENSE) 中声明的 MIT License。

---

## 变更记录

首个版本的变更说明见 [CHANGELOG.md](CHANGELOG.md) 与 [RELEASE_v0.1.0-alpha.md](RELEASE_v0.1.0-alpha.md)。
