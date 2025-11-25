# Competitive Analysis Framework

A reusable framework for enterprise-grade competitive analysis, developed from the Maia Learning project (November 2025).

## Repository Structure

```
MaiaLearningResearch/
├── docs/                        # Framework documentation
│   ├── COMPETITIVE-ANALYSIS-WORKFLOW.md   # Master workflow guide
│   ├── PROJECT-INVENTORY.md     # File inventory
│   └── plans/                   # Implementation plans
├── templates/                   # Reusable project templates
│   └── competitive-analysis/    # Start new projects here
├── skills/local/                # Version-controlled skill definitions
│   ├── competitive-analysis-quality-assurance/
│   └── competitive-research-brightdata/
├── scripts/                     # Framework utilities
│   └── install-skills.sh        # Sync skills to ~/.claude/skills/
├── MAIA-PROJECT/                # Example project instance (V2.0 complete)
├── archive/                     # Archived files from normalization
└── 06-AUTOMATION/               # Automation scripts and templates
```

## Quick Start

### For New Projects

1. Copy the template:
   ```bash
   cp -r templates/competitive-analysis /path/to/new-project/
   ```

2. Follow the workflow:
   - See `docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`
   - Reference `MAIA-PROJECT/` for examples

3. Install skills (if not already installed):
   ```bash
   ./scripts/install-skills.sh
   ```

### For Reviewing the Maia Project

The complete Maia Learning competitive analysis is in `MAIA-PROJECT/`:
- **Deliverables:** `MAIA-PROJECT/03-DELIVERABLES/current/`
- **Documentation:** `MAIA-PROJECT/README.md`

## Skills

This framework uses two custom Claude skills:

### competitive-research-brightdata
Enterprise-grade research methodology using Bright Data tools.
- 26-question research template
- Batch search/scrape strategies
- Citation generation
- Output schemas

### competitive-analysis-quality-assurance
Systematic fact-checking and quality assurance.
- Source attribution verification
- Marketing language detection
- Cross-document consistency checks
- QA report generation

### Installing/Updating Skills

```bash
# Install from repo to ~/.claude/skills/
./scripts/install-skills.sh

# With backup of existing skills
./scripts/install-skills.sh --backup

# Preview changes without installing
./scripts/install-skills.sh --dry-run
```

## Documentation

| Document | Purpose |
|----------|---------|
| `docs/COMPETITIVE-ANALYSIS-WORKFLOW.md` | Master workflow guide for all scenarios |
| `templates/competitive-analysis/README.md` | Template quick start |
| `MAIA-PROJECT/README.md` | Example project documentation |
| `archive/README.md` | Archived files reference |

## Version History

- **November 25, 2025:** Repository normalization (framework/project separation)
- **November 24, 2025:** V2.0 US-Primary strategy pivot complete
- **November 2025:** Maia Learning project completed (9.5/10 quality)

---

**Framework Version:** 1.0
**Based On:** Maia Learning Competitive Analysis (September-November 2025)
