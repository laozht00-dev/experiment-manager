# Lab Experiment Manager - 安装和使用指南

## 📦 安装步骤

### 方式 1: 直接使用（推荐）

1. **在 Claude Code 中激活技能**
   ```bash
   # 技能已预装在以下位置：
   <claude-skills-dir>/lab-experiment-manager
   ```

2. **在任何对话中触发技能**
   - 说：**"开始实验"** - 启动"开始新实验"流程
   - 说：**"记录实验"** - 启动"记录已完成实验"流程
   - 说：**"更新进度"** - 启动"更新日常进度"流程
   - 说：**"完成实验"** - 启动"完成实验"流程
   - 说：**"生成报告"** - 启动"生成实验报告"流程

### 方式 2: 与现有系统集成

如果你已有 `00_ExperimentLog.md` 系统，可以这样集成：

1. **保持现有文件不变**
   - 现有的 `00_ExperimentLog.md` 继续用作总索引
   - 但不再需要在其中维护详细的实验记录块

2. **使用 lab-experiment-manager 生成文件**
   - 每个实验生成独立的 `experiment_notes.md` 和 `readme.txt`
   - 存储在各自的实验文件夹中

3. **定期更新索引表**
   - 新实验完成后，手动添加一行到 `00_ExperimentLog.md` 的总记录表
   - 或者请 AI 帮助自动更新

---

## 🚀 快速开始

### 场景 1：开始第一个实验

```
你: 我要开始一个新实验。研究处理条件 A 下 SAMPLE_A 的 MARKER_PANEL_A 检测。
    项目：PRJ
    对象：SAMPLE_A
    检测指标：MARKER_PANEL_A
    实验类型：cIF
    批次：FB2
    日期：2026-05-07

AI:
✅ 实验文件名已生成：260507_PRJ_SAMPLE_A_MARKER_PANEL_A_cIF_FB2

请确认以下信息：
- 日期：2026-05-07 ✓
- 项目：PRJ ✓
- 对象：SAMPLE_A ✓
- 检测指标：MARKER_PANEL_A ✓
- 实验类型：cIF ✓
- 批次：FB2 (正式实验-批次2) ✓

现在为你生成初始的 experiment_notes.md 模板...

[生成的文件内容]

请告诉我你想把这个文件保存到哪里？
```

### 场景 2：记录已完成的实验

```
你: 我完成了 SAMPLE_B 的 AssayA 实验。
    实验编号：260409_PRJ_SAMPLE_B_MARKER_A_Tube_FB1
    实验日期：2026-04-09 到 2026-04-11
    样本分组：[提供详细信息]
    原始数据：[提供文件列表]

AI:
✅ 已生成完整的实验记录

📄 readme.txt - 用于数据管理
📝 experiment_notes.md - 详细实验笔记

[显示生成的文件]

你想把这些文件保存到哪里？
```

### 场景 3：每天更新进度

```
你: 更新实验进度。
    实验编号：260507_PRJ_SAMPLE_C_MARKER_A_AssayB_FB1
    今天是第 2 天
    完成的操作：[描述]
    观察到：[描述]
    明天计划：[描述]

AI:
✅ Day 2 进度已记录

**Day 2 (2026-05-09)**
- 操作内容：[你提供的内容]
- 观察/结果：[你提供的观察]
- 明天计划：[你提供的计划]

[提示如何保存]
```

---

## 📚 完整的命名规范参考

### 项目代号 (Projects)
- `PRJ` - 示例项目
- `PRJ2` - 示例项目 2
- `PRJ3` - 示例项目 3
- `PRJ4` - 示例项目 4
- 自定义：任何 2-4 字母的缩写

### 阶段批次 (Stage + Batch)
- `PB1/PB2` - 预实验 (Pre-experiment)
- `FB1/FB2` - 正式实验 (Formal)
- `RB1/RB2` - 补充优化 (Refinement)

### 常用实验类型 (Experiment Types)
- `Tube` - AssayA (AssayA)
- `Migration` / `Migr` - 细胞迁移
- `WB` - Western Blot
- `qPCR` - 定量 PCR
- `FC` - 流式细胞术
- `scRNA` - 单细胞转录组
- `Cell` - 细胞培养
- 更多见 `references/naming_conventions.md`

### 常用样本占位符
- `SAMPLE_A` - 示例样本 A
- `SAMPLE_B` - 示例样本 B
- `SAMPLE_C` - 示例样本 C
- `SAMPLE_D` - 示例样本 D
- `SAMPLE_A0` - 示例样本 A 的处理状态 0
- 更多见 `references/naming_conventions.md`

---

## 📋 生成的文件说明

### 1. experiment_notes.md
**用途**: 实验过程中的详细记录
**内容**:
- 实验基本信息（编号、日期、操作者）
- 实验目的和假设
- 材料与方法
- Day-by-day 进度记录
- 结果摘要
- 问题与改进

**何时生成**: 实验开始（初始模板）或完成（完整版本）

### 2. readme.txt
**用途**: 数据管理和元数据
**内容**:
- 基本信息（项目、实验类型、批次）
- 实验目的
- 样本信息（来源、分组、处理）
- 实验执行信息
- 数据文件清单
- 关联记录（前序/后续实验）

**何时生成**: 实验完成后，与原始数据一起存储

### 3. experiment_report.md
**用途**: 可检索的实验总结
**内容**:
- 完整的实验目的和设计
- 详细的实验步骤
- 结果与分析
- 结论
- 问题与改进
- 关键词（用于检索）

**何时生成**: 数据分析完成后

---

## 🎯 最佳实践

### 实验前（Day 0）
1. 使用"开始实验"功能
2. 保存生成的 `experiment_notes.md` 到实验文件夹
3. 如有仪器原始数据，优先规划其在 `00_RawData/` 中的集中存放与 provenance `readme.txt`

### 实验进行中（Day 1-N）
1. 每天使用"更新进度"功能
2. 记录操作内容、观察结果、问题和计划
3. 补充 `资料/` 附件引用，并保持记录及时准确

### 实验完成或终止
1. 使用"记录实验"或"完成实验"功能
2. 生成或更新 `readme.txt` 与 `experiment_notes.md`
3. 若实验终止/失败，整理 `experiment_report.md` 并归档到 `99_Cementary/`

### 数据分析后
1. 使用"生成报告"功能
2. 创建 `experiment_report.md`
3. 对 qPCR 等数据补充 `00_RawData/` 交叉引用信息

### 后续查阅
1. 使用生成的报告中的关键词快速搜索
2. 参考 `readme.txt` 中的文件清单定位原始数据
3. 查阅 `experiment_notes.md` 了解详细的实验过程

---

## ❓ 常见问题

### Q: 如果我忘记了某些信息怎么办？
A: 技能会询问具体问题来获取缺失信息。你可以提供你知道的部分，其他部分可以稍后补充或留空。

### Q: 生成的文件可以编辑吗？
A: 完全可以。所有生成的文件都是标准的 markdown 或 txt 格式，可以用任何文本编辑器编辑。

### Q: 支持哪些语言？
A: 主要支持中文和英文。输出语言会自动匹配你的输入语言。

### Q: 可以自定义项目代号吗？
A: 可以。虽然有推荐的标准代号，但你也可以使用任何对你有意义的缩写。

### Q: 这个技能可以与其他 AI 模型一起使用吗？
A: 可以。这个技能不依赖于特定的 AI 模型，可以与 Claude、OpenClaw 等多种模型配合使用。

### Q: 如何将新的实验添加到我的 00_ExperimentLog.md？
A: 你可以：
1. 手动添加（在总记录表中添加一行，并创建相应的链接）
2. 请 AI 帮助更新（告诉 AI："请将这个实验添加到我的日志中"）

---

## 🔧 技术信息

### 脚本
- `scripts/generate_experiment_name.py` - 生成标准化的实验文件名
  ```bash
  python generate_experiment_name.py <date> <project> <target> <marker> <assay_type> <stage+batch>
  # 示例
  python generate_experiment_name.py 2026-05-07 PRJ SAMPLE_A MARKER_PANEL_A cIF FB2
  # 输出: 260507_PRJ_SAMPLE_A_MARKER_PANEL_A_cIF_FB2
  ```

### 参考资料
- `SKILL.md` - 完整的技能定义和工作流程
- `README.md` - 详细的使用指南
- `references/naming_conventions.md` - 命名规范完整参考

---

## 📞 支持和反馈

如果你在使用过程中遇到问题或有改进建议，请：
1. 描述具体的场景
2. 提供遇到的错误或问题的详细信息
3. 说明你期望的行为

---

## 📄 许可和使用

这个技能面向生命科学研究人员，用于标准化实验记录管理。

**推荐用途**:
- 生命科学研究人员的日常实验管理
- 研究团队的协作和沟通
- 学位论文的实验记录
- 科研项目的数据归档

---

**版本**: 1.0  
**最后更新**: 2026-04-07  
**兼容性**: Claude Code, Claude.ai, OpenClaw 等平台
