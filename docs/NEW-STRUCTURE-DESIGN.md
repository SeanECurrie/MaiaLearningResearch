# New Directory Structure Design

**Date:** November 25, 2025
**Purpose:** Reorganize Maia Learning project into clean, maintainable structure

---

## Current Problem

The project files are scattered across multiple directories without clear organization:
- Deliverables mixed with working files
- No clear separation between inputs and outputs
- Version history difficult to track
- Iteration documentation inconsistent
- Automation scripts not centralized

---

## Proposed New Structure

```
MaiaLearningResearch/
├── 00-PROJECT-MANAGEMENT/
│   ├── README.md
│   ├── PROJECT-STATUS.md
│   └── STAKEHOLDERS.md
│
├── 01-RESEARCH-INPUTS/
│   ├── README.md
│   ├── competitor-data/
│   ├── market-research/
│   ├── pricing-data/
│   ├── feature-data/
│   └── sources.md
│
├── 02-ANALYSIS-OUTPUTS/
│   ├── README.md
│   ├── competitive-matrices/
│   ├── swot-analyses/
│   ├── market-positioning/
│   └── strategic-recommendations/
│
├── 03-DELIVERABLES/
│   ├── README.md
│   ├── VERSION-HISTORY.md
│   ├── current/
│   │   ├── DOCX/
│   │   ├── HTML/
│   │   │   └── visualizations/
│   │   └── PDF/
│   │       └── visualizations/
│   ├── v1.0/
│   │   ├── DOCX/
│   │   ├── HTML/
│   │   └── PDF/
│   └── v0.9/
│       ├── DOCX/
│       ├── HTML/
│       └── PDF/
│
├── 04-QA-DOCUMENTATION/
│   ├── README.md
│   ├── qa-reports/
│   ├── change-logs/
│   └── verification/
│
├── 05-ITERATIONS/
│   ├── README.md
│   ├── iteration-1-initial-research/
│   ├── iteration-2-qa-corrections/
│   └── iteration-3-tim-revisions/
│
├── 06-AUTOMATION/
│   ├── README.md
│   ├── scripts/
│   └── templates/
│
├── docs/
│   ├── plans/
│   ├── guides/
│   └── reference/
│
└── templates/
    └── competitive-analysis/
        ├── deliverables-templates/
        └── automation-scripts/
```

---

## Directory Purposes

### 00-PROJECT-MANAGEMENT/
- High-level project status and stakeholder information
- Quick reference for project state
- Contains: README, STATUS, STAKEHOLDERS

### 01-RESEARCH-INPUTS/
- Raw research data collected during analysis
- Competitor profiles, market data, pricing information
- Source documentation

### 02-ANALYSIS-OUTPUTS/
- Processed analysis results (not final deliverables)
- SWOT analyses, competitive matrices, positioning maps
- Working documents before final formatting

### 03-DELIVERABLES/
- Client-ready deliverables only
- Versioned directories (current, v1.0, v0.9)
- Organized by file type (DOCX, HTML, PDF)

### 04-QA-DOCUMENTATION/
- Quality assurance reports and change logs
- Verification documentation
- Issue tracking

### 05-ITERATIONS/
- Documentation of each major iteration/revision cycle
- Preserves context and decisions for each change
- Includes plans, inventories, QA reviews

### 06-AUTOMATION/
- Scripts for PDF generation, file conversion
- Reusable templates (CSS, HTML)
- Build and deployment tools

### docs/
- Project documentation (plans, guides, reference)
- Not client-facing

### templates/
- Reusable templates for future projects
- Generic competitive analysis framework

---

## Benefits of New Structure

1. **Clear Separation:** Inputs → Analysis → Deliverables flow is explicit
2. **Version Tracking:** Each deliverable version preserved in dedicated folder
3. **Iteration History:** Full context preserved for each revision cycle
4. **Automation-Ready:** Scripts and templates centralized for reuse
5. **Client-Ready:** `03-DELIVERABLES/current/` contains only final client files
6. **Maintainable:** Easy to understand structure for future maintenance

---

## Migration Plan

### Phase 1: Create Structure
1. Create all directories (00-06, subdirectories)
2. Do not delete any existing files yet

### Phase 2: Copy Files
1. Copy current deliverables to `03-DELIVERABLES/current/`
2. Copy visualization files to appropriate subdirectories
3. Copy QA documentation to `04-QA-DOCUMENTATION/`
4. Copy iteration documentation to `05-ITERATIONS/`
5. Copy automation assets to `06-AUTOMATION/`

### Phase 3: Create Documentation
1. Create VERSION-HISTORY.md
2. Create README.md for each numbered directory
3. Update docs/ with any new guides

### Phase 4: Verification
1. Verify all files copied correctly
2. Verify no broken references
3. Optional: Archive and remove old directories

---

## Notes

- Original directories (01-MAIA-BASELINE, 02-COMPETITOR-PROFILES, etc.) preserved until migration verified
- `templates/` directory already exists with Phase 2 work
- `docs/` directory already exists with project documentation
