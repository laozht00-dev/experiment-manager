# Lab Experiment Manager

> A conversational AI skill for managing laboratory experiments from start to finish

[![Version](https://img.shields.io/badge/version-1.3.0-blue.svg)](VERSION.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#)
[![Platform](https://img.shields.io/badge/platform-Claude%20%7C%20OpenClaw-purple.svg)](#)
[![Language](https://img.shields.io/badge/language-English%20%7C%20%E4%B8%AD%E6%96%87-orange.svg)](#)

**Lab Experiment Manager** is a comprehensive skill designed for life sciences researchers to create standardized experiment records, track progress, and generate searchable summaries through natural conversation with AI assistants.

## Project Note

The author does not have a formal computer science background. This project was generated and organized through vibe coding with AI assistance. Given the author's limited professional software engineering background, the project may contain imperfections or mistakes. If you find any issue, feedback through GitHub Issues or discussion is sincerely welcome; the author will learn from it and continue improving the project.

## 🎯 Key Features

- 🗣️ **Conversation-first design** - No file system assumptions, works through natural dialogue
- 📝 **Standardized naming** - Automatic experiment name generation following best practices
- 🔒 **Data integrity** - Strict documentation rules prevent fabrication or assumption
- ✅ **Mandatory confirmation** - All file generation requires explicit user approval
- 🌐 **Multi-language support** - Works in both English and Chinese (中文)
- 🔄 **Version control ready** - Git-enabled for multi-device collaboration
- 🧾 **lab-record workflow** - Stores notes, small attachments, and processed results in a separate records repository
- 🗂️ **External raw-data links** - Keeps large raw data outside Git while recording Windows paths such as `E:\实验数据\...`
- 🤖 **Universal compatibility** - Works with Claude, OpenClaw, and other AI models

## 🚀 Quick Start

### Installation

#### Option 1: From tar.gz package
```bash
cd ~/.claude/skills/
tar -xzf lab-experiment-manager-v1.3.0.tar.gz
```

#### Option 2: From Git repository
```bash
cd ~/.claude/skills/
git clone <your-repo-url> lab-experiment-manager
```

### Basic Usage

Simply start a conversation with your AI assistant using trigger phrases:

**English:**
- "start experiment"
- "record experiment"
- "update experiment"
- "experiment complete"
- "generate experiment report"

**中文:**
- "开始实验"
- "记录实验"
- "更新实验进度"
- "实验完成"
- "生成实验报告"

## 📖 Core Operations

### 1. Start Experiment (开始实验)

Begin a new experiment with standardized documentation.

**What you provide:**
- Experiment date (YYYY-MM-DD)
- Project code (e.g., PRJ, PRJ2, PRJ3)
- Target organism/cell line (e.g., SAMPLE_B, SAMPLE_C)
- Detection marker/indicator (e.g., MARKER_A, MARKER_PANEL_A, MARKER_C)
- Experiment type (e.g., WB, qPCR, Migration)
- Stage/batch (e.g., PB1, FB1, FB2)

**What you get:**
- Standardized experiment name: `[YYMMDD]_[Project]_[Target]_[Marker]_[AssayType]_[StageBatch]`
- Initial `experiment_notes.md` with template structure
- `readme.txt` for data management metadata

**Example:**
```
User: 我要开始一个新实验
AI: 请提供以下信息：
    1. 实验日期（起始日）：YYYY-MM-DD
    2. 项目代号：...

→ Generated: 260409_PRJ_SAMPLE_B_MARKER_A_Tube_FB1
```

### 2. Update Experiment (更新实验进度)

Record daily progress, observations, and data.

**What you provide:**
- Experiment name or date
- Today's operations and observations
- Any issues or notes

**What you get:**
- Updated `experiment_notes.md` with new daily entry
- Timestamped progress records

### 3. Complete Experiment (实验完成)

Mark experiment as finished and finalize documentation.

**What you provide:**
- Experiment name
- Final results summary
- Data file locations

**What you get:**
- Completed `experiment_notes.md` with end date
- Status marked as "已完成"

### 4. Generate Report (生成实验报告)

Create a searchable summary for completed experiments.

**What you provide:**
- Experiment name
- Key findings (optional, can extract from notes)

**What you get:**
- `experiment_report.md` with structured summary
- Searchable keywords and metadata
- Links to related files

### 5. Search Experiments (搜索实验)

Find past experiments by keywords or criteria.

**What you provide:**
- Search terms (cell line, date range, experiment type, etc.)
- File location (if not default)

**What you get:**
- List of matching experiments
- Quick summaries of each match

## 🔒 Data Security & Integrity

This skill follows strict data handling principles:

1. ✅ **Documentation Only** - Records ONLY what you explicitly provide
2. ❌ **Zero Fabrication** - NEVER invents data, concentrations, or results
3. ❓ **Proactive Clarification** - Asks when information is missing
4. 🔍 **Verification** - Ensures accuracy before finalization
5. ⚠️ **Mandatory Confirmation** - Requires explicit approval before creating files

### File Generation Workflow

```
1. AI gathers information through conversation
2. AI presents preview of file content
3. AI asks: "是否确认生成此文件？(Confirm file generation?)"
4. You respond: "是" / "yes" / "确认" / "ok"
5. AI creates the file
```

**The AI will NEVER auto-generate files without your explicit confirmation.**

## 📁 File Structure

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

Large raw data stays outside `lab-record`, typically on the Windows workstation under `E:\实验数据`. Experiment records keep the exact external raw-data folder path, while small supporting materials go in `attachments/` and processed outputs go in `results/`.

## 🛠️ Advanced Features

### Experiment Naming Convention

Format: `[YYMMDD]_[Project]_[Target]_[Marker]_[AssayType]_[StageBatch]`

**Components:**
- `YYMMDD`: Start date (e.g., 260409 = April 9, 2026)
- `Project`: Project code (PRJ, PRJ2, PRJ3, etc.)
- `Target`: Cell line or organism (SAMPLE_B, SAMPLE_C, etc.)
- `Marker`: Detection marker or indicator (MARKER_A, MARKER_PANEL_A, MARKER_C, etc.)
- `AssayType`: Experiment type (WB, qPCR, Tube, Migration, FC, etc.)
- `StageBatch`: Stage + batch number (PB1, FB1, FB2, RB1, etc.)

**Examples:**
- `260409_PRJ_SAMPLE_B_MARKER_A_Tube_FB1` - SAMPLE_B AssayA with MARKER_A detection, formal batch 1
- `260315_PRJ_SAMPLE_C_MARKER_B_WB_PB1` - SAMPLE_C Western blot with MARKER_B detection, pre-experiment batch 1
- `260420_PRJ_SAMPLE_A_MARKER_A_Migration_FB2` - SAMPLE_A migration assay with MARKER_A-related marker, formal batch 2

### Python Helper Script

Generate experiment names programmatically:

```python
from scripts.generate_experiment_name import generate_experiment_name

name = generate_experiment_name(
    date_str="2026-04-09",
    project="PRJ",
    target="SAMPLE_B",
    marker="MARKER_A",
    assay_type="Tube",
    stage_batch="FB1"
)
# Returns: "260409_PRJ_SAMPLE_B_MARKER_A_Tube_FB1"
```

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick Contribution Guide

1. **Fork and clone** the repository
2. **Create a branch** for your feature: `git checkout -b feature/your-feature`
3. **Make changes** and test thoroughly
4. **Update VERSION.md** with your changes
5. **Submit a pull request** with clear description

### Multi-Device Workflow

This skill supports Git-based synchronization across multiple devices:

```bash
# Device 1: Push changes
git add .
git commit -m "Add new feature"
git push origin main

# Device 2: Pull updates
git pull origin main
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed multi-device setup instructions.

## 📊 Version History

### v1.3.0 (2026-05-29) - Current

**Added:**
- Separate `lab-record` repository workflow for experiment records
- Default `logs/YYYY/[experiment-id]/` folder structure
- `attachments/` for small supporting materials and `results/` for processed outputs
- Windows external raw-data path recording for `E:\实验数据\...`

**Changed:**
- Updated default file organization away from the legacy OneDrive / `01_Sandbox` profile
- Standardized naming references around the six-field experiment ID

### v1.2.0 (2026-04-11)

**Added:**
- Day numbering rule: experiment start date = Day 0
- Optional standard Protocol reference module
- Protocol path support for PDF/TXT/MD references

**Changed:**
- Record only deviations from standard protocols when applicable

### v1.1.0 (2026-04-08)

**Added:**
- Mandatory file generation confirmation system
- Git version control support (.gitignore, VERSION.md, CONTRIBUTING.md)
- Version tracking for better change management

**Changed:**
- Enhanced Core Philosophy with file confirmation requirement
- Improved data security protocols

### v1.0.0 (Initial Release)

**Features:**
- Five core operations (Start, Update, Complete, Report, Search)
- Conversation-first design
- Standardized naming convention
- Multi-language support
- Data integrity safeguards

See [VERSION.md](VERSION.md) for complete version history.

## 📚 Documentation

- **[SKILL.md](SKILL.md)** - Complete skill definition and technical details
- **[VERSION.md](VERSION.md)** - Detailed version history and changelog
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines and Git workflow
- **[INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)** - Installation instructions
- **[references/naming_conventions.md](references/naming_conventions.md)** - Naming best practices

## 🎯 Use Cases

### Scenario 1: Starting a Multi-Day Experiment

```
Day 1: "开始实验" → Generate experiment name and initial notes
Day 2: "更新实验进度" → Add today's observations
Day 3: "更新实验进度" → Record results
Day 4: "实验完成" → Finalize documentation
Day 5: "生成实验报告" → Create searchable summary
```

### Scenario 2: Searching Past Experiments

```
User: "搜索所有 SAMPLE_B 的 AssayA 实验"
AI: Returns list of matching experiments with summaries
```

### Scenario 3: Batch Experiment Management

```
User: "开始实验" → FB1 (Formal Batch 1)
[Complete FB1]
User: "开始实验" → FB2 (Formal Batch 2)
[Complete FB2]
User: "生成实验报告" → Compare FB1 vs FB2 results
```

## ⚙️ Compatibility

**AI Platforms:**
- ✅ Claude (Anthropic)
- ✅ OpenClaw
- ✅ Other Claude-compatible platforms

**Required Tools:**
- Read, Write, Edit, Bash

**Operating Systems:**
- macOS
- Linux
- Windows (with WSL or Git Bash)

## 🐛 Troubleshooting

### Issue: Skill not recognized

**Solution:** Ensure the skill is installed in `~/.claude/skills/lab-experiment-manager/`

### Issue: File generation fails

**Solution:** Check file permissions and ensure the target directory exists

### Issue: Git conflicts on multi-device sync

**Solution:** See [CONTRIBUTING.md](CONTRIBUTING.md) "Handling Conflicts" section

## 📞 Support

- **Issues:** Report bugs or request features via GitHub Issues
- **Questions:** Ask your AI assistant for help with specific commands
- **Documentation:** Check [SKILL.md](SKILL.md) for detailed technical information

## 📄 License

MIT License - Feel free to use, modify, and distribute this skill.

## 🙏 Acknowledgments

Designed for life sciences researchers who need standardized, reproducible experiment documentation.

---

**Made with ❤️ for the research community**

*Last updated: 2026-05-29 | Version 1.3.0*
