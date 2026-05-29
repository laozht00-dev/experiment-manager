# Contributing to Lab Experiment Manager

## Multi-Device Workflow

This skill is designed to work across multiple devices using Git version control.

### Initial Setup

#### Device 1 (First time setup)
```bash
cd ~/.claude/skills/lab-experiment-manager
git init
git add .
git commit -m "Initial commit: Lab Experiment Manager v1.1.0"

# Add remote repository (GitHub/GitLab/etc.)
git remote add origin <your-repo-url>
git push -u origin main
```

#### Device 2+ (Clone existing repository)
```bash
cd ~/.claude/skills/
git clone <your-repo-url> lab-experiment-manager
```

### Daily Workflow

#### Before making changes
```bash
cd ~/.claude/skills/lab-experiment-manager
git pull origin main
```

#### After making changes
```bash
git add .
git commit -m "Description of changes"
git push origin main
```

### Handling Conflicts

If you modify the skill on multiple devices simultaneously:

1. **Pull first**: Always `git pull` before making changes
2. **Resolve conflicts**: If conflicts occur, Git will mark them in files
3. **Test after merge**: Verify the skill still works after resolving conflicts
4. **Commit resolution**: `git add .` and `git commit` after fixing conflicts

### Version Control Best Practices

1. **Commit frequently**: Small, focused commits are easier to track
2. **Descriptive messages**: Use clear commit messages
   - Good: "Add confirmation prompt before file generation"
   - Bad: "Update SKILL.md"
3. **Test before pushing**: Ensure the skill works on your device before pushing
4. **Pull before editing**: Reduce merge conflicts by staying up-to-date

### File Structure

```
lab-experiment-manager/
├── .gitignore              # Excludes temporary/system files
├── VERSION.md              # Version history and changelog
├── CONTRIBUTING.md         # This file
├── SKILL.md                # Main skill definition
├── README.md               # User documentation
├── INSTALLATION_GUIDE.md   # Installation instructions
├── references/             # Reference documentation
│   └── naming_conventions.md
└── scripts/                # Helper scripts
    └── generate_experiment_name.py
```

### Making Changes

#### Minor updates (documentation, typos)
- Edit directly and commit
- Increment PATCH version (e.g., 1.1.0 → 1.1.1)

#### New features
- Create a feature branch: `git checkout -b feature/new-feature`
- Make changes and test thoroughly
- Update VERSION.md with new features
- Increment MINOR version (e.g., 1.1.0 → 1.2.0)
- Merge to main: `git checkout main && git merge feature/new-feature`

#### Breaking changes
- Create a branch: `git checkout -b breaking/major-change`
- Update VERSION.md with migration notes
- Increment MAJOR version (e.g., 1.1.0 → 2.0.0)
- Test extensively before merging

### Syncing Across Devices

#### Scenario 1: Work laptop → Home desktop
```bash
# On work laptop (after changes)
git add .
git commit -m "Add new experiment template"
git push

# On home desktop (before starting work)
git pull
```

#### Scenario 2: Forgot to pull, made changes
```bash
# You made local changes, but remote has updates
git stash                    # Save your local changes
git pull                     # Get remote updates
git stash pop                # Reapply your changes
# Resolve any conflicts
git add .
git commit -m "Your changes"
git push
```

### Troubleshooting

#### "Your branch is behind"
```bash
git pull origin main
```

#### "Your branch is ahead"
```bash
git push origin main
```

#### "Merge conflict"
1. Open conflicted files (Git marks them with `<<<<<<<`, `=======`, `>>>>>>>`)
2. Choose which version to keep or combine both
3. Remove conflict markers
4. `git add <resolved-files>`
5. `git commit -m "Resolve merge conflict"`
6. `git push`

#### "Accidentally committed sensitive data"
```bash
# Remove from last commit (if not pushed yet)
git reset --soft HEAD~1
# Edit files to remove sensitive data
git add .
git commit -m "Fixed commit"
```

### Questions?

If you encounter issues with Git workflow, check:
- Git documentation: https://git-scm.com/doc
- GitHub guides: https://guides.github.com/
- Or ask Claude Code for help with specific Git commands
