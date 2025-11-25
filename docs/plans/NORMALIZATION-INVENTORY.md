# Pre-Normalization File Inventory

**Generated:** 2025-11-25
**Purpose:** Document file counts before normalization for verification

---

## File Counts by Directory

### Numbered Directories (Project-Specific)
- 00-PROJECT-MANAGEMENT/: 1 files
- 00-PROJECT-OVERVIEW/: 2 files
- 01-COMPANY-PROFILES/: 1 files
- 01-RESEARCH-INPUTS/: 1 files
- 02-ANALYSIS-OUTPUTS/: 1 files
- 02-COMPETITOR-PROFILES/: 7 files
- 03-COMPARATIVE-ANALYSIS/: 6 files
- 03-DELIVERABLES/: 41 files
- 04-QA-DOCUMENTATION/: 1 files
- 04-STRATEGIC-INSIGHTS/: 6 files
- 05-FINAL-DELIVERABLES/: 137 files
- 05-ITERATIONS/: 4 files
- 06-AUTOMATION/: 6 files
- 06-PROJECT-MANAGEMENT/: 9 files

### Framework Directories (Stay at Root)
- docs/: 17 files
- templates/: 9 files

### Other Directories
- competitive-analysis-quality-assurance/: 4 files
- node_modules/: 363 files
- PROGRESS-REPORTS/: 1 files
- scripts/: 5 files
- temp_skill_extract/: 4 files
- test/: 5 files

---

## Summary Counts

| Category | File Count |
|----------|------------|
| Total in numbered directories (00-06) | 223 |
| Total in 05-FINAL-DELIVERABLES/ | 137 |
| Framework directories (docs, templates, 06-AUTOMATION) | 32 |
| node_modules (regenerable) | 363 |
| Other directories to archive | 14 |

---

## Root-Level Files to Archive

Files at repo root that should be moved to archive/:
- *.md (except README.md, CLAUDE.md)
- *.py
- *.js
- *.json
- *.skill

---

**Baseline Total:** ~631 files (excluding node_modules: ~268 files)
