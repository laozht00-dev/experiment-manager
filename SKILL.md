---
name: lab-experiment-manager
description: |
  Comprehensive laboratory experiment management system for life sciences research.
  Use this skill when the user wants to: start a new experiment, record experiment details,
  update daily progress, complete an experiment, or generate experiment reports/summaries.

  Trigger phrases include: "开始实验", "记录实验", "更新实验进度", "实验完成", "生成实验报告", "保存实验附件",
  "start experiment", "record experiment", "update experiment", "experiment complete", "save attachments",
  or any mention of managing lab notebooks, experiment metadata, research documentation, or supplementary materials.

  Default record target is a separate lab-record repository. It stores experiment notes,
  small attachments, processed results, and external raw-data links.
compatibility:
  tools: [Read, Write, Edit, Bash]
---

# Lab Experiment Manager

A conversational system for managing laboratory experiments from start to finish. This skill helps researchers create standardized experiment records, track progress, and generate searchable summaries - all through natural dialogue.

## Core Philosophy

**Data Security & Integrity (CRITICAL - HIGHEST PRIORITY)**:
1. **Strict Documentation Only**: Record and summarize ONLY information explicitly provided by the user.
2. **Zero Fabrication**: NEVER invent, assume, or extend experimental parameters, concentrations, data, or results.
3. **Proactive Clarification**: If crucial information is missing or if additional detail would be beneficial, ALWAYS ask the user instead of filling in details yourself.
4. **Verification Before Finalization**: Ensure all documents accurately reflect only the user's input - no additions, no assumptions, no extensions.
5. **MANDATORY FILE GENERATION CONFIRMATION**: Before generating ANY experiment record file (experiment_notes.md, experiment_report.md, readme.txt, or any other documentation), you MUST:
   - Present a preview or summary of what will be written
   - Explicitly ask the user for confirmation: "是否确认生成此文件？(Confirm file generation?)"
   - ONLY proceed with file creation after receiving explicit affirmative response (e.g., "是", "yes", "确认", "ok", "proceed")
   - If user declines or asks for changes, modify the content and ask for confirmation again
   - NEVER auto-generate files without this confirmation step
6. **MANDATORY GIT CONFIRMATION**: Before committing any experiment record changes, present the changed paths and proposed commit message, then ask for explicit confirmation. Commit only inside the `lab-record` repository unless the user is updating this skill itself.

**Conversation-first design**: This skill does NOT assume any existing file structure or log system. Instead, it:
1. Asks the user targeted questions to gather information
2. Generates standardized outputs based on their answers
3. Works with any file system organization the user prefers

**Universal compatibility**: Designed to work across different AI models (Claude, OpenClaw, etc.) without requiring access to specific configuration files.

## lab-record Repository Profile

Default experiment records live in a separate repository named `lab-record`, usually next to this skill repository in a local workbench:

```text
Lab-manager/
├── lab-experiment-manager/
└── lab-record/
```

**lab-record folder roles**:
- `logs/YYYY/[ExperimentID]/` = one folder per experiment, grouped by start year
- `[experiment-folder]/experiment_notes.md` = main experiment record
- `[experiment-folder]/readme.txt` = raw-data provenance, processed-result inventory, attachment notes, and external-path notes
- `[experiment-folder]/attachments/` = small supporting materials such as photos, plate layouts, small PDFs, and screenshots
- `[experiment-folder]/results/` = processed outputs such as figures, quantification tables, exported PDFs/PNGs/TIFFs, and small analysis result files
- `templates/` = Markdown templates and schema
- `archive/` = old-format records, migrated materials, or records intentionally removed from the active log flow

**Raw-data policy**:
- Large raw instrument data is NOT copied into `lab-record`
- The default raw-data home is the Windows workstation path `E:\实验数据`
- Record Windows raw-data paths in their original Windows format, for example `E:\实验数据\260529_PRJ_SAMPLE_B_MARKER_A_Tube_FB1`
- If the user has not provided a raw-data path yet, write `待补充`; never invent a path
- Markdown references to repository files use relative paths such as `results/assay_quantification.xlsx` or `attachments/Day0_plate_layout.png`
- Markdown references to external raw data must stay as plain Windows paths, not GitHub links

**Default Git workflow**:
- After confirmed writes, commit only the relevant files in the `lab-record` repository
- Before commit, show changed paths and the proposed commit message
- Use messages such as `record: start [experiment-id]`, `record: update [experiment-id] day [N]`, or `record: complete [experiment-id]`

## Day 编号规则（重要）

- 实验开始的日期 = **Day 0**
- 例如：4月8日开始 → 4月8日 = Day 0，4月9日 = Day 1，4月10日 = Day 2，以此类推
- **重要**：Day 编号与具体日期的对应关系需在记录中明确说明

## 标准 Protocol 模块（可选）

**功能**：存储和读取标准实验流程参考文件，用于完善实验记录

**Protocol 存储地址**：`<protocol-library>`

**工作流程**：
1. 每次开始新实验或记录实验时，首先检查 Protocol 存储地址是否已设置
2. 如果已设置存储地址，搜索该目录下是否有对应的标准 protocol 文件（PDF/TXT/MD 格式）
3. 如果找到相关 protocol 文件，读取并作为参考，完善实验记录
4. 如果未设置存储地址，或目录下无相关 protocol，则跳过此步骤

**记录规则**：
- **不需要**每次都记录标准实验流程
- **仅当**实验操作与标准 protocol 有差异时，才需要将这些差异记录到 experiment_notes.md 中
- 记录重点：特殊操作、参数调整、注意事项等

**注意**：
- 此模块为**可选模块**，非强制流程
- Protocol 文件命名建议与实验类型相关（如 WB_protocol.md、qPCR_protocol.md 等）
- 支持格式：PDF、TXT、MD

## Legacy 01_Sandbox Workspace Profile

When this skill is explicitly used inside `<legacy-01-sandbox-root>`, follow that workspace's `CLAUDE.md` as the source of truth. Otherwise, default to the `lab-record` repository profile above.

**Workspace characteristics**:
- This is a **wet-lab experiment management workspace**, not an application code repository
- Root-level dated experiment folders are **active** experiments
- `00_RawData/` stores centralized raw instrument outputs and provenance `readme.txt` files
- `99_Cementary/` stores **terminated/failed** experiments and should retain both `experiment_notes.md` and `experiment_report.md`
- `资料/` inside experiment folders stores supporting photos and reference materials

**01_Sandbox naming rule**:
- Use `YYMMDD_PROJECT_TARGET_MARKER_ASSAYTYPE_STAGEBATCH`
- Example: `260507_PRJ_SAMPLE_A_MARKER_PANEL_A_cIF_FB2`
- In this workspace, `检测指标 / marker / indicator` is part of the experiment ID and should be placed before assay type and stage/batch
- If the marker panel is unknown, ask the user; do not invent one

**Documentation conventions**:
- Write documentation in **Chinese**, while keeping gene/protein/tool names in English
- Keep terminology consistent across related experiments
- Preserve both macOS and Windows raw-data paths when the user provides them
- Respect PB/FB lineage between related experiments
- Cross-link qPCR raw data through `00_RawData/` provenance notes when relevant

## Five Core Operations

### 1. Start Experiment (开始实验)

**When to use**: User is about to begin a new experiment and needs a standardized file name and initial documentation.

**Workflow**:

1. **Gather basic information** through conversation:
   ```
   请提供以下信息：
   1. 实验日期（起始日）：YYYY-MM-DD
   2. 项目代号：（如 PRJ, PRJ2, PRJ3 等，如果没有可以用简短描述）
   3. 实验对象：（如 SAMPLE_B, SAMPLE_C, SAMPLE_A 等）
   4. 检测指标 / marker / indicator：（如 MARKER_PANEL_A, MARKER_A, MARKER_C 等，按你的习惯拼接）
   5. 实验类型 / assay type：（如 WB, qPCR, Tube, AssayB, FC, cIF, IHC 等）
   6. 阶段批次：（如 PB1=预实验批次1, FB1=正式实验批次1, FB2=正式实验批次2）
   ```

2. **Generate standardized experiment name**:
   ```
   Format for lab-record: [YYMMDD]_[Project]_[Target]_[Marker]_[AssayType]_[StageBatch]
   Example: 260507_PRJ_SAMPLE_A_MARKER_PANEL_A_cIF_FB2
   ```

3. **Ask about experiment purpose and design**:
   ```
   请简要描述：
   1. 实验目的（一句话概括）
   2. 主要分组（如果已确定）
   3. 预计实验天数
   4. 检测指标在正文中的写法（如果需要和命名保持一致，可在此确认）
   5. Windows 原始数据文件夹路径（通常位于 E:\实验数据；如果暂时没有请说明待补充）
   ```

4. **Generate initial experiment_notes.md** with template structure:
   ```markdown
   ---
   **实验编号**: [生成的文件名]
   **项目**: [项目代号]
   **实验类型**: [实验类型]
   **批次**: [如 FB1]
   **状态**: 进行中
   **起止日期**: YYYY-MM-DD ~ （进行中）
   **负责人**: [询问用户]

   #### 实验目的
   > [用户提供的目的]

   #### 材料与方法
   - **细胞/样本**: [用户提供]
   - **主要试剂**: [用户提供或待后续补充]
   - **实验分组**: [用户提供的分组信息，如果有]

   #### 实验进程（多天实验按天记录）

   **Day 0 (YYYY-MM-DD)**
   - 操作内容: [待填写]
   - 观察/结果: [待填写]
   - 附件: [待填写]

   #### 原始数据路径
   - Windows: [用户提供的 E:\实验数据\... 路径，或 待补充]
   - 备注: 大型原始数据不进入 lab-record；这里只记录外部路径

   #### 文件目录
   - 附件: attachments/
   - 处理结果: results/

   #### 结果摘要
   > [待完成后填写]

   #### 问题与改进
   - [ ] 待解决问题
   - [ ] 下一步计划
   ```

5. **Output to user**:
   - Display the generated experiment name
   - Offer to save the initial experiment_notes.md to a location they specify
   - **IMPORTANT**: When user confirms file generation:
     1. First, create the folder `lab-record/logs/YYYY/[experiment-id]/`
     2. Then, create `experiment_notes.md`, `readme.txt`, `attachments/`, and `results/` inside that folder
     3. Final notes path: `lab-record/logs/YYYY/[experiment-id]/experiment_notes.md`
     4. If the user confirms commit, commit only these new `lab-record` files with `record: start [experiment-id]`
   - Provide a checklist of what to prepare before starting

**Key principle**: Default to `lab-record/logs/YYYY/[experiment-id]/` for new records. Do not copy large raw data; record the Windows raw-data folder path instead.

**CRITICAL DATA SECURITY**: Do NOT invent or extend experimental parameters. ONLY use what the user provides. If details like concentrations, groups, marker panels, or raw-data locations are missing, ASK the user.

---

### 2. Record Experiment (记录实验)

**When to use**: User has completed an experiment and has raw data that needs to be documented.

**Workflow**:

1. **Identify the experiment**:
   ```
   请提供实验文件名（如果之前生成过）或实验的基本信息：
   - 实验名称/编号
   - 实验日期
   - 实验类型
   ```

2. **Gather detailed metadata** through structured questions:

   **A. 实验目的与设计**
   ```
   1. 实验目的（详细描述）
   2. 实验假设（如果有）
   3. 预期结果
   ```

   **B. 样本信息**
   ```
   1. 样本来源（细胞系、组织、患者样本等）
   2. 批次编号
   3. 样本分组（对照组、实验组、浓度梯度等）
   4. 特殊处理（刺激条件、孵育时间等）
   ```

   **C. 实验执行**
   ```
   1. 操作人
   2. 实验日期范围（起始-结束）
   3. 关键步骤和参数
   4. 使用的仪器和试剂（品牌、批号、浓度）
   ```

   **D. 数据文件**
   ```
   1. 原始数据文件列表（文件名和类型）
   2. 图像文件（如果有）
   3. 处理后的数据文件
   4. 数据存储位置（相对路径或绝对路径）
   ```

   **E. 关联信息**
   ```
   1. 前序实验（如果有）
   2. 后续计划实验
   3. 相关批次编号
   ```

3. **Generate two outputs**:

   **Output 1: readme.txt** (for data management)
   ```
   ================================================================================
   实验数据说明 · Experiment Metadata
   ================================================================================

   【基本信息】
   实验编号：[实验名称]
   项目归属：[项目] - [项目全称]
   实验类型：[实验类型]
   阶段批次：[批次]（[阶段说明]）

   【实验目的】
   [用户提供的详细目的]

   【样本信息】
   样本来源：[来源]
   批次编号：[批次]
   样本分组：
     - [分组1]
     - [分组2]
     - ...
   浓度/剂量：[详细信息]
   特殊处理：[处理条件]

   【实验执行】
   操作人：[操作人]
   实验日期：[起始日期] ~ [结束日期]

   【数据文件清单】
   外部原始数据路径：
     - Windows: [E:\实验数据\... 或 待补充]
   附件（attachments/）：
     - [附件文件1]
     - [附件文件2]
   处理结果（results/）：
     - [处理文件1]
     - [处理文件2]

   【关联记录】
   批次溯源：[批次ID]
   前序实验：[前序实验名称]
   后续实验：[后续实验名称]

   【备注】
   - Day 1 ([日期]): [操作内容]
   - Day 2 ([日期]): [操作内容]
   - ...

   ================================================================================
   创建：[创建日期] | 更新：[更新日期]
   ================================================================================
   ```

   **Output 2: Complete experiment_notes.md**
   - If an initial version exists, read it and fill in all the [待填写] sections
   - If not, create a complete version from scratch
   - Include all Day-by-day progress entries
   - Include the Windows raw-data folder path exactly as provided, or `待补充`
   - Reference repository files with relative paths under `attachments/` and `results/`
   - Fill in the results summary section

4. **Offer to save** both files to user-specified locations:
   - **IMPORTANT**: Both `readme.txt` and `experiment_notes.md` should be saved inside the experiment folder
   - If the folder doesn't exist yet, create it first
   - Final paths:
     - `[user-specified-directory]/[experiment-id]/readme.txt`
     - `[user-specified-directory]/[experiment-id]/experiment_notes.md`

**CRITICAL DATA SECURITY**: Documents must ONLY contain data provided by the user. NO assumptions, NO extensions, NO fabrications. Summary must be a factual distillation of user input.

---

### 2.5. Update Existing Experiment (更新已有实验记录)

**When to use**: User specifies an existing experiment folder and wants to update the experiment_notes.md file based on new information.

**CRITICAL WORKFLOW - MANDATORY VERIFICATION STEPS**:

1. **Receive folder path from user**:
   ```
   用户提供已生成的实验文件夹路径，例如：
   <legacy-01-sandbox-root>/260409_PRJ_SAMPLE_MODEL_FB1_modelPhase
   ```

2. **Check for existing experiment_notes.md**:
   - Read the file at: `[folder-path]/experiment_notes.md`
   - If file does NOT exist, inform user and ask if they want to create a new one
   - If file EXISTS, proceed to step 3

3. **MANDATORY VERIFICATION - Content Matching Check**:
   - Read the ENTIRE experiment_notes.md file
   - Extract key information: experiment ID, date range, purpose, sample info, etc.
   - Present this information to user and ask: **"请确认这是你要更新的实验吗？(Confirm this is the experiment you want to update?)"**
   - If user says NO, ask for clarification or correct folder path
   - If user says YES, proceed to step 4

4. **Gather update information from user**:
   ```
   请描述你要更新的内容：
   1. 更新的具体内容是什么？（例如：添加 Day 2 的操作记录、修改实验结果、更新数据路径等）
   2. 更新涉及文件的哪个部分？（例如：实验进程、结果摘要、问题与改进等）
   3. 具体的更新内容（详细描述）
   ```

5. **MANDATORY PREVIEW BEFORE WRITING**:
   - Generate a preview showing:
     - 原文内容（要被修改的部分）
     - 新增/修改内容（用户提供的内容）
     - 修改后的完整效果
   - Present preview to user with clear formatting (使用 <<<< 和 >>>> 标记)
   - Explicitly ask: **"是否确认写入此内容？(Confirm writing this content?)"**
   - ONLY proceed with file writing after receiving explicit affirmative response (是/yes/确认/ok)

6. **Write to file**:
   - Use Edit tool to update experiment_notes.md
   - Update the "更新日期" field to current date
   - Preserve all existing content that was not modified
   - NEVER delete or overwrite unrelated sections

7. **Confirmation message**:
   ```
   ✅ 实验记录已更新

   文件路径: [folder-path]/experiment_notes.md
   更新内容: [简要说明更新了什么]
   更新时间: [当前日期]
   ```

**Key principles**:
- ALWAYS verify the folder and file exist before proceeding
- ALWAYS confirm with user that they're updating the correct experiment
- ALWAYS show a preview before writing
- ALWAYS require explicit user confirmation before any file modification
- NEVER assume or infer what needs to be updated
- NEVER modify content beyond what user explicitly requested

**CRITICAL DATA SECURITY**:
- Only update content explicitly provided by user
- Preserve all existing data that user did not request to change
- Do NOT interpret, extend, or add context to user input
- Do NOT fill in template placeholders with invented data

---

### 3. Update Progress (更新进度)

**When to use**: User wants to add daily progress notes to an ongoing experiment.

**Important for day numbering**: The experiment start date is **Day 0**. Later entries must keep the date ↔ day mapping explicit.

**Workflow**:

1. **Identify the experiment**:
   ```
   请提供：
   1. 实验名称/编号
   2. 今天是实验的第几天？
   3. 今天的日期：YYYY-MM-DD
   ```

2. **Gather today's information**:
   ```
   请描述今天的实验进展：
   1. 操作内容（做了什么）
   2. 观察/结果（看到了什么）
   3. 遇到的问题（如果有）
   4. 明天的计划（如果有）
   ```

3. **Read existing experiment_notes.md** (if path provided) or ask user to paste the current content

4. **Update the file** by adding a new Day entry:
   ```markdown
   **Day N (YYYY-MM-DD)**
   - 操作内容: [用户提供的操作]
   - 观察/结果: [用户提供的观察]
   - 问题: [如果有]
   - 明天计划: [如果有]
   - 附件: [如果有，可引用 attachments/ 下文件]
   - 处理结果: [如果有，可引用 results/ 下文件]
   ```

5. **Offer to save** the updated file:
   - **IMPORTANT**: Save the updated `experiment_notes.md` inside the experiment folder
   - File path: `[user-specified-directory]/[experiment-id]/experiment_notes.md`
   - If the file already exists in this location, update it with the new Day entry

**Key principle**: This operation is lightweight - just append new daily entries without requiring full metadata.

**CRITICAL DATA SECURITY**: Only record what the user tells you. If they mention observations, record them exactly. If they mention problems, record them exactly. Do NOT interpret, extend, or add context.

---

### 4. Complete Experiment (完成实验)

**When to use**: User has finished data analysis and wants to mark the experiment as complete.

**Workflow**:

1. **Identify the experiment** and confirm completion:
   ```
   请确认：
   1. 实验名称/编号
   2. 实验结束日期：YYYY-MM-DD
   3. 数据分析是否已完成？（是/否）
   ```

2. **Gather results information**:
   ```
   请提供实验结果：
   1. 主要发现（2-3句话概括）
   2. 是否达到预期目标？
   3. 数据质量评估（好/中/差，以及原因）
   4. 遇到的主要问题
   5. 改进建议（如果需要重复实验）
   ```

3. **Read existing experiment_notes.md** and update:
   - Change date range from "进行中" to actual end date
   - Fill in the "结果摘要" section with user's findings
   - Fill in the "问题与改进" section
   - Mark checkboxes as completed or add new ones

4. **Generate a completion summary** to display:
   ```
   ✅ 实验已完成

   实验编号: [名称]
   实验周期: [起始日期] ~ [结束日期] (共 N 天)
   主要发现: [概括]
   数据质量: [评估]

   文件已更新：
   - experiment_notes.md (已标记完成)
   - readme.txt (如果存在，建议更新备注部分)
   ```

5. **Offer to save** the updated files:
   - **IMPORTANT**: Save all updated files inside the experiment folder
   - File paths:
     - `[user-specified-directory]/[experiment-id]/experiment_notes.md` (updated with completion info)
     - `[user-specified-directory]/[experiment-id]/readme.txt` (if exists, update with final notes)

---

### 5. Generate Report (生成实验报告)

**When to use**: User wants to create a searchable summary of a completed experiment for future reference.

**Workflow**:

1. **Identify the experiment**:
   ```
   请提供实验名称/编号，或者提供 experiment_notes.md 的路径
   ```

2. **Read experiment_notes.md** (if path provided) or ask user to provide key information:
   ```
   如果没有现成的记录文件，请提供：
   1. 实验目的
   2. 实验方法（简要步骤）
   3. 主要结果
   4. 结论
   ```

3. **Generate a structured experiment summary** in markdown format:
   ```markdown
   # 实验报告：[实验名称]

   **实验编号**: [完整文件名]
   **实验日期**: [起始] ~ [结束]（共 N 天）
   **操作者**: [姓名]
   **项目**: [项目代号]
   **阶段批次**: [如 FB1]

   ---

   ## 一、实验目的

   [清晰陈述实验目的和假设]

   ## 二、分组设计

   | 组别 | 处理条件 | 复孔数 |
   |------|----------|--------|
   | [组1] | [条件] | [N] |
   | [组2] | [条件] | [N] |

   > 注：[如有分组调整说明，在此备注]

   ## 三、实验对象

   - **[细胞/样本1]**：[用途说明]
   - **[细胞/样本2]**：[用途说明]

   ## 四、关键参数

   - [参数1]: [值]
   - [参数2]: [值]

   ## 五、结果分析

   [详细描述实验结果及初步分析]

   ## 六、数据文件

   | 类型 | 路径 |
   |------|------|
   | 原始图像 | [文件描述] |
   | macOS | [路径] |
   | Windows | [路径] |

   ## 七、结论

   [总结实验结论，是否支持假设]

   ## 八、问题与改进

   ### 遇到的问题
   - [问题1]

   ### 改进建议
   - [建议1]

   ## 九、关键词（用于检索）

   `[关键词1]` `[关键词2]` `[关键词3]` `[实验类型]` `[细胞系]`

   ---

   **报告生成日期**: [当前日期]
   ```

4. **Offer multiple output formats**:
   - Markdown (.md) - for version control and easy editing
   - Plain text (.txt) - for universal compatibility
   - Ask if user wants to append this to a master log file
   - For 01_Sandbox termination/failed-experiment archiving, default report filename is `experiment_report.md` and the archive target is typically `99_Cementary/[experiment-id]/`

5. **Generate searchable metadata** (optional):
   ```json
   {
     "experiment_id": "[实验名称]",
     "date_range": "[起始] ~ [结束]",
     "project": "[项目代号]",
     "experiment_type": "[类型]",
     "keywords": ["关键词1", "关键词2", "关键词3"],
     "purpose": "[一句话目的]",
     "conclusion": "[一句话结论]",
     "data_quality": "[好/中/差]",
     "files": {
       "notes": "[路径]",
       "readme": "[路径]",
       "report": "[路径]"
     }
   }
   ```

**CRITICAL DATA SECURITY**: Report must be a faithful summary of the experiment_notes.md and user-provided information. NO speculation, NO interpretation beyond what's documented, NO additions of external knowledge or assumptions.

---

### 6. Save Experiment Attachments and Results (保存实验附件与处理结果)

**When to use**: User has collected supplementary materials or processed outputs during the experiment and needs to organize and document them.

**Workflow**:

1. **Receive folder path and attachments from user**:
   ```
   用户提供实验文件夹路径，例如：
   lab-record/logs/2026/260410_PRJ_SAMPLE_B_MARKER_A_Tube_FB1

   以及要保存的附件材料（可以是描述或实际文件）
   ```

2. **Classify the file target**:
   - Use `attachments/` for small supporting materials: photos, plate layouts, small PDFs, screenshots, notes
   - Use `results/` for processed outputs: figures, quantification tables, exported PDFs/PNGs/TIFFs, small analysis results
   - Do NOT copy large raw instrument exports into `lab-record`; record their Windows raw-data folder path instead
   - If the target directory does not exist, offer to create it after confirmation

3. **Gather attachment information from user**:
   ```
   请提供以下信息（对每个附件）：
   1. 文件本身（文件、图片、表格、PDF，或描述）
   2. 文件类型：辅助附件 attachments，或处理结果 results
   3. 文件所属的实验 Day（第几天）
   4. 文件是在哪个操作步骤产生的（简要描述）
   5. 文件的简要说明（简述，用于命名）
   ```

4. **PROPOSE NAMING SCHEME**:
   - Format: `[YYYYMMDD]_[Day序号]_[操作步骤]_[简述].扩展名`
   - Example: `20260410_Day1_Step2_显微镜观察.jpg`
   - Present the proposed filenames to user
   - Explicitly ask: **"请确认这些文件命名方案是否可以接受？(Confirm these filenames?)"**
   - ONLY proceed after receiving explicit affirmative response

5. **Save files to the selected folder**:
   - Save supporting materials to: `[experiment-folder]/attachments/[proposed-filename]`
   - Save processed outputs to: `[experiment-folder]/results/[proposed-filename]`
   - Create folders if they do not exist: `attachments/` and/or `results/`
   - Verify all files are saved successfully

6. **UPDATE experiment_notes.md**:
   - Read the existing `experiment_notes.md` file
   - Locate the corresponding Day section
   - Add repository file references using relative paths: `attachments/[filename]` or `results/[filename]`
   - Place it directly under the Day entry or in an "附件" subsection
   - Example insertion:
     ```markdown
     **Day 1 (2026-04-10)**
     - 操作内容: [existing content]
     - 观察/结果: [existing content]
     - 附件：attachments/20260410_Day1_Step2_显微镜观察.jpg
     - 处理结果：results/20260410_Day1_Tube_quantification.xlsx
     ```
   - Present preview before writing (same as section 2.5)
   - Ask for confirmation: **"是否确认更新实验笔记？(Confirm updating notes?)"**
   - Only write after receiving explicit affirmative response

7. **Confirmation message**:
   ```
   ✅ 实验文件已保存

   实验编号: [名称]
   文件夹路径: [experiment-folder]/

   已保存文件：
   - [filename1]
   - [filename2]
   - ...

   实验笔记已更新：[experiment-folder]/experiment_notes.md
   更新时间: [当前日期]
   ```

**Key principles**:
- ALWAYS verify the experiment folder exists before proceeding
- ALWAYS classify each file as `attachments/` or `results/` before saving
- ALWAYS keep large raw data outside `lab-record`; record the external Windows path instead
- ALWAYS propose naming scheme and get user confirmation before saving
- ALWAYS show preview before updating experiment_notes.md
- ALWAYS require explicit user confirmation before file operations
- Preserve original file extensions
- Keep attachment naming consistent and searchable

**CRITICAL DATA SECURITY**:
- Only record and organize materials explicitly provided by user
- Do NOT modify file extensions
- Do NOT assume file types or purposes
- Do NOT create attachments or results that user did not provide
- Maintain accurate references between saved files and notes

---

## Naming Convention Reference

When generating experiment names for `lab-record`, follow this standard format:

```
[YYMMDD]_[Project]_[Target]_[Marker]_[AssayType]_[StageBatch]
```

**Field explanations**:
- `YYMMDD`: Experiment start date (6 digits)
- `Project`: Project abbreviation (e.g., `PRJ`, `PRJ2`, `PRJ3`, `PRJ4`)
- `Target`: Experimental subject (e.g., `SAMPLE_A`, `SAMPLE_B`, `SAMPLE_MODEL`, `SAMPLE_D`, `SAMPLE_C`)
- `Marker`: Detection marker / indicator panel (e.g., `MARKER_A`, `MARKER_A`, `MARKER_PANEL_A`)
- `AssayType`: Assay / experiment type (e.g., `WB`, `qPCR`, `AssayB`, `Tube`, `modelPhase`, `FC`, `cIF`, `IHC`)
- `StageBatch`: Stage + batch number (e.g., `PB1`, `FB1`, `FB2`, `RB1`)

**Important lab-record rule**:
- The marker / indicator field is part of the experiment folder name
- Keep the six-field order stable so logs remain sortable and searchable
- Do not remove, rewrite, or infer marker information unless the user explicitly confirms it

**Examples**:
- `260507_PRJ_SAMPLE_A_MARKER_PANEL_A_cIF_FB2` - SAMPLE_A cell immunofluorescence with MARKER_B/MARKER_C/MARKER_A markers, formal batch 2
- `260409_PRJ_SAMPLE_B_FB1_Tube` - SAMPLE_B AssayA, formal batch 1
- `260409_PRJ_SAMPLE_MODEL_FB1_ModelAssay` - sample model assay, formal batch 1

---

## Integration with Existing Systems

If the user has an existing experiment log system (like `00_ExperimentLog.md`), offer to:

1. **Read the log file** to understand their naming conventions and structure
2. **Add index entries** to their master table
3. **Follow their specific templates** if they differ from the defaults above
4. **Maintain consistency** with their existing records

But NEVER assume such a system exists - always ask first.

---

## Language Handling

- **Default to the user's language** in all outputs
- If user provides information in Chinese, generate Chinese documentation
- If user provides information in English, generate English documentation
- Field names and structure remain consistent regardless of language

---

## File Organization Best Practices

**Automatic folder creation for lab-record**: When generating experiment files, ALWAYS:
1. Determine the experiment start year from the start date
2. Create `lab-record/logs/YYYY/[ExperimentID]/`
3. Place `experiment_notes.md`, `readme.txt`, `attachments/`, and `results/` inside that folder
4. Final structure: `lab-record/logs/YYYY/[ExperimentID]/[files]`

**Recommended folder structure for lab-record**:

```
lab-record/
├── templates/
│   ├── experiment_v1.md
│   └── schema.yml
├── logs/
│   └── 2026/
│       └── 260529_PRJ_SAMPLE_B_MARKER_A_Tube_FB1/
│           ├── experiment_notes.md
│           ├── readme.txt
│           ├── attachments/
│           │   └── 20260529_Day0_plate_layout.png
│           └── results/
│               └── 20260529_Day0_assay_quantification.xlsx
├── docs/
└── archive/
```

**lab-record file path examples**:
- Notes file: `lab-record/logs/2026/260529_PRJ_SAMPLE_B_MARKER_A_Tube_FB1/experiment_notes.md`
- Metadata file: `lab-record/logs/2026/260529_PRJ_SAMPLE_B_MARKER_A_Tube_FB1/readme.txt`
- Supporting materials: `lab-record/logs/2026/260529_PRJ_SAMPLE_B_MARKER_A_Tube_FB1/attachments/`
- Processed results: `lab-record/logs/2026/260529_PRJ_SAMPLE_B_MARKER_A_Tube_FB1/results/`
- External raw data path in notes: `E:\实验数据\260529_PRJ_SAMPLE_B_MARKER_A_Tube_FB1`

**Key principle**: The experiment folder is the unit of record. Store notes, small attachments, and processed results together; keep large raw data outside the repo and record its Windows path.

**Legacy 01_Sandbox folder roles**:
- Root-level dated experiment folders = active experiments
- `00_RawData/` = centralized raw instrument outputs and provenance `readme.txt`
- `99_Cementary/` = terminated/failed experiments archived with `experiment_notes.md` and `experiment_report.md`
- `[experiment-folder]/资料/` = supporting reference photos and materials

**Legacy recommended folder structure for 01_Sandbox**:

```
[user-specified-directory]/
├── 00_RawData/
│   └── [data-batch-or-instrument-folder]/
│       └── readme.txt
├── 99_Cementary/
│   └── [ExperimentID]/
│       ├── experiment_notes.md
│       └── experiment_report.md
└── [ExperimentID]/
    ├── experiment_notes.md
    ├── readme.txt                     # if this experiment folder itself needs a metadata file
    └── 资料/
        ├── 20260410_Day0_Step1_显微镜图.jpg
        └── ...
```

**Legacy file path examples** (for experiment `260507_PRJ_SAMPLE_A_MARKER_PANEL_A_cIF_FB2`):
- Base directory: `<legacy-01-sandbox-root>/`
- Active experiment folder: `<legacy-01-sandbox-root>/260507_PRJ_SAMPLE_A_MARKER_PANEL_A_cIF_FB2/`
- Notes file: `<legacy-01-sandbox-root>/260507_PRJ_SAMPLE_A_MARKER_PANEL_A_cIF_FB2/experiment_notes.md`
- Supporting materials: `<legacy-01-sandbox-root>/260507_PRJ_SAMPLE_A_MARKER_PANEL_A_cIF_FB2/资料/`
- Central raw data provenance example: `<legacy-01-sandbox-root>/00_RawData/[subfolder]/readme.txt`
- Termination archive example: `<legacy-01-sandbox-root>/99_Cementary/260507_PRJ_SAMPLE_A_MARKER_PANEL_A_cIF_FB2/`

**Legacy key principle**: In 01_Sandbox, do not invent per-experiment `raw_data/` or `processed/` subfolders unless the user explicitly asks for them, because raw outputs are normally centralized in `00_RawData/`.

---

## Error Handling and Edge Cases

1. **Missing information**: If user doesn't provide required information, ask specific follow-up questions rather than leaving fields blank

2. **Ambiguous dates**: Always confirm date format (YYYY-MM-DD) and convert if user provides other formats

3. **File conflicts**: Before writing, check if file exists and ask user whether to overwrite or create a new version

4. **Incomplete experiments**: If user wants to generate a report for an incomplete experiment, warn them and offer to generate a "progress report" instead

5. **Multi-day experiments**: Always use the START date in the experiment name, not the end date

6. **DATA SECURITY - CRITICAL**:
   - If user provides incomplete experimental details (e.g., missing concentrations, unclear groupings), ALWAYS ask for clarification rather than inferring or assuming
   - If user provides data that seems inconsistent or unclear, ask for confirmation before recording
   - NEVER fill in template placeholders with invented data
   - NEVER extend or interpret user input beyond what was explicitly stated
   - When in doubt, ask the user for clarification

---

## Output Quality Standards

All generated documents should be:
- **Structured**: Clear sections with consistent formatting
- **Complete**: No [待填写] placeholders in final outputs
- **Searchable**: Include keywords and clear section headers
- **Timestamped**: Include creation and update dates
- **Traceable**: Link to related experiments and data files

---

## Conversation Flow Examples

### Example 1: Starting a new experiment

```
User: 我要开始一个新实验
