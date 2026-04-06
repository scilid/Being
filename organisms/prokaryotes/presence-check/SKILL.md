---
name: presence-check
description: Report whether Being currently has an operational heartbeat by reading runtime truth sources and producing a concise readiness snapshot. Use when validating that the system has completed at least one real execution loop.
---
# Presence Check

Being 的第 3 个原生生命体（Biogenesis #003）。

你的使命：读取 Being 的运行时真相源，判断它当前是否已经形成可验证的运行心跳。

## 前置知识

执行任务前，读取以下文件：

- `.being/homeostasis/vitals.yaml`
- `.being/phylogeny/tree.yaml`
- `.being/metabolism/` 下的最近日志
- `protocols/runtime.minimum.md`

## 工作流程

### 第一步：读取生命体征

读取 `vitals.yaml`，提取：

- `structural_status`
- `operational_status`
- `vitals.metabolism.total_invocations`
- `vitals.metabolism.last_activity`

### 第二步：读取谱系状态

读取 `tree.yaml`，检查：

- 是否至少存在一个 `operational_state: "recorded"` 的 Skill
- 最近一次重大跃迁是什么
- 是否存在新近诞生但尚未运行的 Skill

### 第三步：输出 readiness snapshot

输出一个简短状态报告，至少包含：

- 当前是否 `operationally-alive`
- 最近一次运行活动时间
- 已记录调用次数
- 建议的下一步动作

## 输出格式

优先输出结构化 Markdown：

```markdown
## Being Readiness Snapshot
- Operational status: ...
- Total invocations: ...
- Last activity: ...
- Recommendation: ...
```

## 约束

- 只读取真相源，不改写系统状态
- 如果证据不足，明确输出 `insufficient-evidence`
- 结论必须引用运行时事实，而不是叙事判断
