# `.being/validation/`

> 校验失败与校验报告目录
> 创建：2026-04-06

本目录用于保存：

- membrane 校验结果
- signal 配置校验结果
- 路径解析失败记录
- 出生流程中断报告

当前仓库尚未有自动验证器，因此本目录仅作为协议占位。

当最小 runtime 落地后，建议至少写入：

- `latest.validation.yaml`
- `failures/{timestamp}-{entity}.yaml`

这样失败才能从叙事层沉降为系统事实。
