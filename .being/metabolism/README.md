# `.being/metabolism/`

> 运行时行为真相源
> 创建：2026-04-06

本目录用于记录 Being 的真实代谢活动。

当前状态：**已有首次真实调用记录**。

这意味着：

- `total_invocations` 应从本目录中的日志聚合得出
- 系统现在可以被标记为 `operationally-alive`
- 后续每次真实闭环都应继续在此目录中追加：
  - `{skill-name}.log.yaml`
  - 可选的 `{skill-name}.stats.yaml`

## 最小要求

任一 Skill 完成一次真实调用后，至少追加一条记录，字段应符合：

- `invocation_id`
- `timestamp`
- `skill`
- `energy.tokens_total`
- `products.primary`
- `outcome.success`

目前首批日志已经写入：

- `skill-genesis.log.yaml`
- `membrane-weaver.log.yaml`
- `metabolic-tracker.log.yaml`
