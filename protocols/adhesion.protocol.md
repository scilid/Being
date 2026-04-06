# 粘附协议（Adhesion Protocol）

> Being 第五纪核心协议
> 版本：0.1.0
> 创建：2026-04-05
> 依赖：membrane.schema.md, organelle.protocol.md

---

## 概述

多细胞生命的前提是细胞能**粘在一起**。单独的真核细胞再强大，如果无法与其他细胞稳定结合，就永远只是单细胞生物。

粘附协议定义了 Skill 之间如何声明稳定的协作关系，形成"组织"。

---

## 粘附类型

| 类型 | 生物学 | 计算含义 | 耦合强度 |
|------|--------|---------|---------|
| **紧密连接（Tight）** | 紧密连接蛋白 | 两个 Skill 必须一起调用，数据直接传递 | 强 |
| **间隙连接（Gap）** | 间隙连接蛋白 | 两个 Skill 通过信号通道通信，可独立调用 | 中 |
| **锚定连接（Anchoring）** | 桥粒 | 共享结构性依赖（如同一配置文件），松散关联 | 弱 |

---

## 粘附声明

在 Skill 的膜声明中添加 `adhesion` 区：

```yaml
adhesion:
  tissue: ""                    # 所属组织名称
  position: ""                  # 在组织中的位置/角色
  binds_to:
    - skill: ""                 # 粘附目标
      junction_type: ""         # tight | gap | anchoring
      data_exchange:            # 数据交换规格
        sends: []               # 向对方发送什么
        receives: []            # 从对方接收什么
```

---

## 组织形成规则

一个"组织"（Tissue）的最低要求：

1. **三个以上 Skill** 通过粘附声明互相关联
2. 至少一对 **tight junction**（否则只是松散群落，不是组织）
3. 所有成员声明相同的 `tissue` 名称
4. 组织有一个 **manifest**，定义组织级的输入输出

### 组织清单（Tissue Manifest）

```yaml
# organisms/tissues/{tissue-name}/tissue.yaml
identity:
  name: ""
  description: ""
  formed: ""                     # 形成日期

cells:                           # 组成细胞
  - skill: ""
    position: ""
    grade: ""                    # prokaryote | eukaryote

collective_membrane:             # 组织级膜——整体对外的接口
  ingress: []
  egress: []

internal_topology:               # 内部连接拓扑
  - from: ""
    to: ""
    junction: ""                 # tight | gap | anchoring
```

---

*一个细胞是一滴水。一个组织是一条河。*
