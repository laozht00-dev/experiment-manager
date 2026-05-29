# 实验记录系统参考手册

本文档提供实验记录系统中常用的代号、缩写和命名规范。

## 命名规范

### 核心公式

```
[YYMMDD]_[Project]_[Target]_[Marker]_[AssayType]_[StageBatch]
```

**示例**：`260409_PRJ_SAMPLE_B_MARKER_A_Tube_FB1`

**01_Sandbox 说明**：
- 命名固定为 6 个组成部分：日期、项目、对象、检测指标、实验类型、批次
- `检测指标 / marker / indicator` 需要直接体现在实验文件夹名中
- 多个检测指标可按用户习惯直接拼接（如 `MARKER_PANEL_A`）
- 除非用户明确要求，否则不要擅自删去或改写 marker

---

## 项目代号 (Project Codes)

| 代号 | 全称 | 说明 |
|------|------|------|
| `PRJ` | Project A | 示例项目 A |
| `PRJ2` | Project B | 示例项目 B |
| `PRJ3` | Project C | 示例项目 C |
| `PRJ4` | Project D | 示例项目 D |
| `MSc` | Master | 学位课题 |
| `TS` | Topic Study | 示例专题 |
| `MOD` | Model Study | 示例模型研究 |

---

## 阶段批次代号 (Stage + Batch)

| 代号 | 含义 | 说明 |
|------|------|------|
| `PB1` | Pre + Batch1 | 预实验-批次1 |
| `PB2` | Pre + Batch2 | 预实验-批次2 |
| `FB1` | Formal + Batch1 | 正式实验-批次1 |
| `FB2` | Formal + Batch2 | 正式实验-批次2 |
| `FB3` | Formal + Batch3 | 正式实验-批次3 |
| `RB1` | Refine + Batch1 | 补充优化-批次1 |
| `RB2` | Refine + Batch2 | 补充优化-批次2 |

**使用原则**：
- 同一批次号贯穿该轮次的所有相关实验
- 重做实验时更新批次号（B1 → B2）

---

## 实验类型代号 (Experiment Types)

### 分子生物学实验

| 代号 | 全称 | 说明 |
|------|------|------|
| `WB` | Western Blot | 蛋白质印迹 |
| `qPCR` | Quantitative PCR | 实时定量PCR |
| `ELISA` | ELISA | 酶联免疫吸附测定 |
| `IP` | Immunoprecipitation | 免疫共沉淀 |
| `ChIP` | ChIP | 染色质免疫沉淀 |

### 细胞实验

| 代号 | 全称 | 说明 |
|------|------|------|
| `Cell` | Cell Culture | 细胞培养/传代/诞生 |
| `Prolif` | Proliferation | 细胞增殖实验 |
| `Apop` | Apoptosis | 细胞凋亡检测 |
| `Migr` | Migration | 细胞迁移实验 |
| `Inv` | Invasion | 细胞侵袭实验 |
| `Tube` | AssayA | AssayA实验 |
| `Spher` | Spheroid | 3D球体培养 |
| `Cocult` | Co-culture | 共培养实验 |

### 流式细胞术

| 代号 | 全称 | 说明 |
|------|------|------|
| `FC` | Flow Cytometry | 流式细胞术 |
| `FACS` | FACS | 流式细胞分选 |
| `CyTOF` | CyTOF | 质谱流式 |

### 显微成像

| 代号 | 全称 | 说明 |
|------|------|------|
| `ICC` | Immunocytochemistry | 免疫细胞化学 |
| `IHC` | Immunohistochemistry | 免疫组织化学 |
| `IF` | Immunofluorescence | 免疫荧光 |
| `Confocal` | Confocal Microscopy | 共聚焦显微镜 |
| `LiveImg` | Live Imaging | 活细胞成像 |

### 组学技术

| 代号 | 全称 | 说明 |
|------|------|------|
| `scRNA` | Single-cell RNA-seq | 单细胞转录组测序 |
| `bulkRNA` | Bulk RNA-seq | 转录组测序 |
| `stRNA` | Spatial Transcriptomics | 空间转录组 |
| `ATAC` | ATAC-seq | 染色质可及性测序 |
| `ChIPseq` | ChIP-seq | 染色质免疫沉淀测序 |
| `Proteome` | Proteomics | 蛋白质组学 |
| `Metabol` | Metabolomics | 代谢组学 |

### 动物实验

| 代号 | 全称 | 说明 |
|------|------|------|
| `InVivo` | In Vivo | 体内实验 |
| `Tumor` | Model Assay | 示例模型模型 |
| `Inject` | Injection | 注射实验 |
| `Harvest` | Harvest | 取材 |
| `Behavior` | Behavior Test | 行为学测试 |

---

## 常用样本占位符

- `SAMPLE_A` - 示例样本 A
- `SAMPLE_B` - 示例样本 B
- `SAMPLE_C` - 示例样本 C
- `SAMPLE_D` - 示例样本 D
- `SAMPLE_A0` - 示例样本 A 的处理状态 0
- `SAMPLE_A1` - 示例样本 A 的处理状态 1
- `SAMPLE_A2` - 示例样本 A 的处理状态 2

---

## 常用指标和处理条件占位符

- `MARKER_A` - 示例检测指标 A
- `MARKER_B` - 示例检测指标 B
- `MARKER_PANEL_A` - 示例检测指标组合 A
- `TREATMENT_A` - 示例处理条件 A
- `CONTROL_A` - 示例对照条件 A
- `OUTPUT_A` - 示例输出指标 A

---

## 数据文件命名建议

### 原始数据

```
[实验编号]_raw_[数据类型].[扩展名]
示例: 260409_PRJ_SAMPLE_B_FB1_Tube_raw_images.tif
```

### 处理数据

```
[实验编号]_processed_[分析类型].[扩展名]
示例: 260409_PRJ_SAMPLE_B_FB1_Tube_processed_quantification.xlsx
```

### 图表

```
[实验编号]_figure_[图表描述].[扩展名]
示例: 260409_PRJ_SAMPLE_B_FB1_Tube_figure_assay_metric.pdf
```

---

## 实验状态标记

| 符号 | 状态 | 说明 |
|------|------|------|
| 🔄 | 进行中 | 实验正在进行 |
| ✅ | 完成 | 实验已完成 |
| ⏸️ | 暂停 | 实验暂时中止 |
| ❌ | 失败 | 实验失败需重做 |
| 📊 | 分析中 | 数据分析进行中 |

---

## 快速参考：完整示例

**实验场景**：记录示例项目中 SAMPLE_B 对 TREATMENT_A 的 AssayA 结果，并检测 MARKER_A。

**生成的文件名**：
```
260409_PRJ_SAMPLE_B_MARKER_A_Tube_FB1
```

**解析**：
- `260409` - 2026年4月9日
- `PRJ` - 示例项目
- `SAMPLE_B` - 示例样本 B
- `MARKER_A` - 检测指标
- `Tube` - AssayA实验
- `FB1` - 正式实验批次1

**lab-record 文件组织示意**：
```
lab-record/
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

大型原始数据保留在 Windows 电脑的 `E:\实验数据`，在 `experiment_notes.md` 和 `readme.txt` 中记录外部路径；处理后的图表、统计表和小型结果文件进入 `results/`。
