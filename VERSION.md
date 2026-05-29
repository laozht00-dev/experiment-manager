# Version History

## v1.3.0 (2026-05-29)

### Added
- **lab-record repository workflow**: Default experiment records now live in a separate `lab-record` repository next to this skill repository
- **Experiment folder layout**: New default structure `logs/YYYY/[experiment-id]/` with `experiment_notes.md`, `readme.txt`, `attachments/`, and `results/`
- **External raw-data linking**: Large raw data remains outside Git, with Windows paths recorded in original format such as `E:\实验数据\...`
- **Processed result management**: Small supporting files go to `attachments/`; processed figures, tables, and analysis outputs go to `results/`
- **Git confirmation rule**: Experiment record commits require changed-path preview and explicit user confirmation

### Changed
- Updated README and naming references to make `lab-record` the default workflow
- Reframed legacy OneDrive / `01_Sandbox` behavior as an explicit legacy profile
- Standardized experiment naming around `YYMMDD_PROJECT_TARGET_MARKER_ASSAYTYPE_STAGEBATCH`

### Migration Notes
- Recommended local workbench is now `Lab-manager/lab-experiment-manager` plus `Lab-manager/lab-record`
- Existing OneDrive-based records can remain in place or be migrated gradually
- Large raw data should not be copied into `lab-record`; record the external path instead

---

## v1.2.0 (2026-04-11)

### Added
- **Day 编号规则**: 实验开始的日期 = Day 0（如：4月8日开始 → 4月8日 = Day 0）
- **标准 Protocol 模块（可选）**: 新增标准实验流程参考功能，支持 PDF/TXT/MD 格式
- **Protocol 存储地址**: `<protocol-library>`

### Changed
- 记录规则更新：仅记录与标准 protocol 的差异，无需每次记录完整流程

### Migration Notes
- Day 编号规则为新增约定，建议后续实验记录遵循
- Protocol 模块为可选，不影响现有工作流程

---

## v1.1.0 (2026-04-08)

### Added
- **Mandatory file generation confirmation**: All file writes now require explicit user approval before execution
- **Git version control support**: Added .gitignore, VERSION.md, and CONTRIBUTING.md for multi-device collaboration
- Version tracking system for better change management

### Changed
- Updated Core Philosophy section with file generation confirmation requirement (Rule #5)
- Enhanced data security protocols

### Migration Notes
- No breaking changes
- Existing workflows remain compatible
- New confirmation step adds one interaction before file generation

---

## v1.0.0 (Initial Release)

### Features
- Five core operations: Start, Update, Complete, Report, Search
- Conversation-first design (no file system assumptions)
- Standardized experiment naming convention
- Multi-language support (中文/English)
- Data security and integrity safeguards
- Universal AI model compatibility (Claude, OpenClaw, etc.)

### File Templates
- experiment_notes.md (daily progress tracking)
- experiment_report.md (searchable summaries)
- readme.txt (data management metadata)

### Scripts
- generate_experiment_name.py (standardized naming)

---

## Version Numbering

This skill follows Semantic Versioning (SemVer):
- **MAJOR.MINOR.PATCH**
- MAJOR: Breaking changes to workflow or file formats
- MINOR: New features, backward-compatible
- PATCH: Bug fixes, documentation updates
