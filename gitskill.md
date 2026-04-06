# gitskill.md

> Being `v0.1.0-alpha` 首发 Git 工作流
> 目标：把当前仓库从本地原型整理为 GitHub 上的第一个公开版本
> 适用环境：Windows + PowerShell

---

## 0. 当前判断

截至本文件生成时，工作区还**不是一个 Git 仓库**。

因此首发流程必须从：

1. `git init`
2. 首次提交
3. 绑定远程
4. 推送到 GitHub
5. 创建首个 Release

开始。

---

## 1. 首发前确认清单

在开始 Git 操作前，先确认以下文件已经存在：

- [README.md](README.md)
- [LICENSE](LICENSE)
- [CHANGELOG.md](CHANGELOG.md)
- [RELEASE_v0.1.0-alpha.md](RELEASE_v0.1.0-alpha.md)
- [runtime/validator.py](runtime/validator.py)
- [runtime/loop.py](runtime/loop.py)
- [runtime/aggregate_vitals.py](runtime/aggregate_vitals.py)
- [.github/REPO_METADATA.md](.github/REPO_METADATA.md)

并确保验证器当前通过：

- [latest.validation.yaml](.being/validation/latest.validation.yaml)

当前建议的首发版本名：

- `v0.1.0-alpha`

当前建议的发布标题：

- `Being v0.1.0-alpha — first operational prototype`

---

## 2. 推荐提交信息

### 首发 commit message

```text
feat: release Being v0.1.0-alpha operational prototype
```

### 可选更叙事一点的版本

```text
feat: establish first operational Being prototype
```

默认建议使用第一条，更适合 GitHub 首发。

---

## 3. PowerShell 首发命令顺序

以下命令假设当前目录是仓库根目录：`F:\DOCs\Being`

### Step 1：初始化 Git 仓库

```powershell
git init
git branch -M main
```

### Step 2：检查状态

```powershell
git status
```

### Step 3：加入全部文件

```powershell
git add .
```

### Step 4：创建首发提交

```powershell
git commit -m "feat: release Being v0.1.0-alpha operational prototype"
```

### Step 5：打版本标签

```powershell
git tag -a v0.1.0-alpha -m "Being v0.1.0-alpha — first operational prototype"
```

### Step 6：绑定 GitHub 远程

把下面的 URL 替换成你的真实仓库地址：

```powershell
git remote add origin https://github.com/<your-name>/being.git
```

如果你使用 SSH：

```powershell
git remote add origin git@github.com:<your-name>/being.git
```

### Step 7：推送主分支

```powershell
git push -u origin main
```

### Step 8：推送标签

```powershell
git push origin v0.1.0-alpha
```

---

## 4. GitHub 仓库创建建议

在 GitHub 上创建仓库时，建议：

### Repository name

- `being`

### Description

```text
An experimental runtime for computational organisms, where protocols, signals, membranes, and metabolism become executable, verifiable system behavior.
```

### Topics

```text
artificial-life, computational-organism, protocols, event-driven, runtime, python, yaml, experimental, emergence, autonomous-systems
```

### Website

- 首发可以先留空

### Visibility

- 如果你想让第一版更快获得反馈：`Public`
- 如果你想先小范围整理：`Private` 后再切换为 `Public`

默认建议：`Public`

---

## 5. GitHub Release 创建步骤

当标签已经推上 GitHub 后：

1. 打开仓库的 Releases 页面
2. 点击 `Draft a new release`
3. 选择 tag：`v0.1.0-alpha`
4. Release title 使用：

```text
Being v0.1.0-alpha — first operational prototype
```

1. Release notes 正文可直接使用 [RELEASE_v0.1.0-alpha.md](RELEASE_v0.1.0-alpha.md)

---

## 6. 可直接粘贴的 Release 正文

```markdown
# Being v0.1.0-alpha — first operational prototype

Being is an experimental runtime for computational organisms.

This release marks the point where the repository becomes more than a conceptual design space. It now includes executable runtime behavior, recorded runtime facts, and a minimal validation path.

## Highlights

- First recorded operational cycle
- Minimal runtime loop for `readiness-check-request`
- Clean validation (`0 errors / 0 warnings`)
- Automatic vitals aggregation from metabolism logs

## Status

This is a research prototype and operational MVP, not yet a stable general-purpose framework.
```

---

## 7. 推荐首发说明话术

### 英文

```text
Being is now an operational prototype. It is still experimental, but it is no longer only conceptual.
```

### 中文

```text
Being 现在已经是一个运行型原型。它仍然是实验性的，但它不再只是概念系统。
```

---

## 8. 发布前最后一次检查

在 `git add .` 之前，建议再执行一次：

```powershell
f:/DOCs/Being/.venv/Scripts/python.exe runtime/validator.py .
```

预期结果应保持：

- `Errors: 0`
- `Warnings: 0`

如果验证失败，不要发布，先修复。

---

## 9. 发布后的第一步

首发完成后，建议立刻做三件事：

1. 在仓库 About 栏填入 description 和 topics
2. 在 Release 中固定 `v0.1.0-alpha`
3. 在下一次开发前新建一个分支，例如：

```powershell
git checkout -b post-alpha-runtime-expansion
```

这样可以把“首发版本”与“后续演化”清晰分开。

---

## 10. 适合当前仓库的 Git 策略

当前阶段建议：

### 分支策略

- `main`：只保留可验证、可发布状态
- 功能分支：每次只做一个演化动作

示例：

- `feature/runtime-stats-handler`
- `feature/life-create-request-loop`
- `feature/phylogeny-auto-derivation`

### 提交策略

推荐使用简洁的 conventional-style 提交：

- `feat:` 新能力
- `fix:` 修复问题
- `docs:` 文档改进
- `refactor:` 结构整理

示例：

```text
feat: add minimal runtime loop
fix: align membrane paths with phylogeny
refactor: derive vitals from metabolism logs
docs: prepare v0.1.0-alpha release metadata
```

---

## 11. 这个 gitskill 的用途

本文件不是泛泛的 Git 教程。

它是针对 **Being 当前首发状态** 定制的一次完整 Git 发布流程说明。

它解决的是：

- 如何从“本地原型”进入“GitHub 首发版本”
- 如何命名第一版
- 如何提交、打 tag、推送、写 release
- 如何保持后续演化节奏

---

## 12. 最终建议

当前最推荐的首发动作是：

1. 初始化 Git
2. 提交全部当前状态
3. 打 `v0.1.0-alpha` 标签
4. 推送到 GitHub
5. 用 [RELEASE_v0.1.0-alpha.md](RELEASE_v0.1.0-alpha.md) 创建首发 Release

对当前仓库来说，这是最自然、也最稳的第一步。
