# Lab Experiment Manager (实验室实验管理器)

> 一个对话驱动的 AI 实验管理助手，协助生命科学研究人员全流程管理实验记录。

[![版本](https://img.shields.io/badge/version-1.3.0-blue.svg)](VERSION.md)
[![协议](https://img.shields.io/badge/license-MIT-green.svg)](#)
[![AI 平台](https://img.shields.io/badge/platform-Claude%20%7C%20OpenClaw-purple.svg)](#)
[![语言](https://img.shields.io/badge/language-%E4%B8%AD%E6%96%87%20%7C%20English-orange.svg)](#)

## 📋 项目概述

**Lab Experiment Manager** 是专为生命科学领域设计的智能实验管理工具。它通过自然语言对话，帮助研究人员创建标准化的实验记录、追踪进度，并生成可检索的总结报告，旨在提升实验的可重复性和数据管理效率。

## 项目声明

本人并非计算机相关专业背景。本项目全部内容由本人通过 vibe coding 方式在 AI 辅助下生成与整理。由于个人专业背景有限，项目中难免存在不足或错误。如您发现问题，欢迎通过 GitHub Issues 或讨论提出意见，我将认真学习并持续改进。

### 核心亮点

- 🎯 **对话式设计** - 无需预设文件结构，通过对话即搜即录。
- 📝 **标准化命名** - 自动遵循最佳实践生成实验编号：`[日期]_[项目]_[对象]_[检测指标]_[实验类型]_[阶段批次]`。
- 🔒 **数据严谨性** - 严格遵守"仅记录用户提供信息"原则，拒绝幻觉和推测。
- ✅ **强制确认机制** - 生成任何文件前必须经过用户预览和明确确认。
- 🌐 **多语言支持** - 完美支持中文和英文双语对话与文档生成。
- 🔄 **版本控制支持** - 深度集成 Git，支持多设备同步与协作。
- 📅 **Day 编号规则** - 实验开始日期 = Day 0，便于时间追溯。
- 📋 **标准 Protocol 参考** - 支持标准实验流程参考文件，仅记录与标准的差异。
- 🧾 **lab-record 双仓库工作流** - Skill 与真实实验记录分仓库管理。
- 🗂️ **原始数据外链** - 大型原始数据保留在 Windows `E:\实验数据`，记录中只保存可追溯路径。

## 🚀 快速上手

### 安装指南

#### 方式一：使用压缩包安装
```bash
cd ~/.claude/skills/
tar -xzf lab-experiment-manager-v1.3.0.tar.gz
```

#### 方式二：使用 Git 克隆
```bash
cd ~/.claude/skills/
git clone <your-repo-url> lab-experiment-manager
```

### 基础用法

使用以下触发词（中英文均可）唤醒 AI 助手：

- **开始实验** (Start experiment)
- **记录实验** (Record experiment)
- **更新实验进度** (Update experiment)
- **实验完成** (Complete experiment)
- **生成实验报告** (Generate report)

## 📖 核心操作说明

### 1. 开始实验 (Start Experiment)
开启新实验并初始化文档。
- **提供信息**：实验日期、项目代号（如 PRJ, PRJ2）、实验对象（如 SAMPLE_B）、检测指标（如 MARKER_A、MARKER_PANEL_A）、实验类型（如 WB）、阶段批次（如 FB1）。
- **获得结果**：标准化的实验文件名及初始 `experiment_notes.md` 模板。

### 2. 更新实验进度 (Update Progress)
记录每日实验操作、观察现象和原始数据。
- **获得结果**：在 `experiment_notes.md` 中追加带时间戳的每日记录。

### 3. 完成实验 (Complete Experiment)
标记实验结束，录入最终结果分析。
- **获得结果**：更新实验周期，填充“结果摘要”部分，将状态标记为“已完成”。

### 4. 生成实验报告 (Generate Report)
为完成的实验生成结构化的、可检索的总结。
- **获得结果**：生成 `experiment_report.md`，包含关键词、主要发现和结论；若实验终止/失败，可归档到 `99_Cementary/`。

### 5. 搜索实验 (Search)
通过关键词、日期或实验类型快速找回既往记录。

## 🔒 安全与数据完整性

本 Skill 遵循极高的数据安全准则：
1. **仅记录真实数据**：严禁虚构浓度、参数或结果。
2. **主动澄清**：缺失关键信息时会询问用户，而不是盲目填充。
3. **强制确认流程**：
   - AI 收集信息并生成预览。
   - AI 询问：“是否确认生成此文件？(Confirm file generation?)”
   - 用户回复“是/确认”后，AI 才会执行写入操作。

## 📁 文件组织结构建议

```
Lab-manager/
├── lab-experiment-manager/
└── lab-record/
    ├── templates/
    ├── logs/
    │   └── 2026/
    │       └── 260529_PRJ_SAMPLE_B_MARKER_A_Tube_FB1/
    │           ├── experiment_notes.md
    │           ├── readme.txt
    │           ├── attachments/
    │           └── results/
    ├── docs/
    └── archive/
```

大型原始数据不进入 `lab-record`，默认保留在 Windows 电脑的 `E:\实验数据`。实验记录中只写明对应的外部原始数据文件夹路径；少量辅助材料放入 `attachments/`，处理后的图表和结果文件放入 `results/`。

## 🛠️ 后续更新方向：实验同伴 (Lab Companion)

我们将此 Skill 的演进目标定位为从"记录工具"向"**实验同伴**"进化。后续将重点开发以下两个核心模块：

### 1. 实验记录助手模块 (Recording Assistant) - [现有功能增强]
- **定位**：轻量化、即插即用。
- **特点**：不需要任何本地原始文件支持，可在任何新设备上直接使用，单纯作为对话记录助手，确保实验数据的标准化录入。

### 2. 实验同伴模块 (Lab Companion) - [重点开发方向]
- **经验总结与提醒**：根据你在本地设备上记录的既往实验内容，在下次进行类似实验设计、操作或结果分析时，主动提醒你曾经踩过的坑，最优参数或注意事项。
- **联网经验搜索**：
  - **分层检索**：能够联网搜索其他人的实验经验。
  - **优先级策略**：搜索结果将与你的个人经验**严格分开**。
  - **以我为主**：始终优先参考你的本地实验记录。由于实验室环境、试剂和操作差异极大，联网信息仅供参考，不直接套用。
- **知识库交流与迁移**：
  - 支持"同伴知识库"的导出与导入。
  - 你可以将另一台设备的实验同伴经验导入当前设备，实现跨设备、跨平台的经验累积与丰富。

### 已实现的功能
- ✅ **lab-record 工作流**：实验记录默认保存到独立 `lab-record` 仓库。
- ✅ **实验文件夹结构**：`logs/YYYY/[实验编号]/` 下保存 `experiment_notes.md`、`readme.txt`、`attachments/` 和 `results/`。
- ✅ **原始数据外链**：大型原始数据不进入 Git，记录 Windows 路径如 `E:\实验数据\...`。
- ✅ **Day 编号规则**：实验开始日期 = Day 0
- ✅ **标准 Protocol 参考模块**：支持标准实验流程参考文件，仅记录与标准的差异

---

## 🤝 贡献指南

欢迎参与开发！详情请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

- **同步工作流**：建议使用 Git 进行多设备同步。
- **版本追踪**：请在修改后更新 [VERSION.md](VERSION.md)。

## 📄 协议

本项目采用 [MIT 协议](LICENSE)。

---

**为科研人员量身定制，让每一次实验都有迹可循**

*最后更新：2026-05-29 | 版本 1.3.0*
