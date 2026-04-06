# Runtime

这个目录承载 Being 的最小执行层原型。

当前包含：

- [aggregation.py](aggregation.py)：从 metabolism 日志聚合运行时生命体征的共享逻辑
- [aggregate_vitals.py](aggregate_vitals.py)：手动触发 `vitals.yaml` 聚合刷新的脚本
- [loop.py](loop.py)：最小 runtime loop，用于消费可处理信号并沉积新的运行时事实
- [validator.py](validator.py)：最小 Python 验证器，用于检查当前仓库是否满足运行时一致性

## 验证器当前职责

`validator.py` 会检查：

1. 必要真相源路径是否存在
2. receptor 文件是否可解析
3. membrane 是否具备最小字段
4. signal 名是否符合 `kebab-case`
5. phylogeny 中的 membrane 路径是否存在
6. metabolism 日志是否与 `vitals.yaml` 的调用计数一致
7. `operationally-alive` 是否有真实调用支撑

## Runtime loop 当前职责

`loop.py` 当前会处理：

1. 发给 `presence-check` 的 `readiness-check-request`
2. 生成 readiness snapshot
3. 写入 `presence-check` 的代谢日志
4. 追加 `readiness-check-complete` 信号
5. 通过聚合器自动刷新 `vitals.yaml`
6. 更新 `tree.yaml`

## Vitals 聚合职责

`aggregate_vitals.py` / `aggregation.py` 当前会从 `.being/metabolism/*.log.yaml` 自动推导：

1. `total_invocations`
2. `total_tokens_consumed`
3. `average_efficiency`
4. `last_activity`
5. `operational_status`

## 输出

运行后会生成：

- [.being/validation/latest.validation.yaml](../.being/validation/latest.validation.yaml)

## 设计定位

这不是完整 runtime。

它是第一块硬执行层：

> 让 Being 至少能检验自己是否自洽。

而 `loop.py` 则是第二块执行层：

> 让 Being 至少能自动消费一个真实信号，并把结果沉积为新的系统事实。

`aggregation.py` 则是第三块执行层：

> 让生命体征尽量从行为事实自动长出来，而不是手工维护。
