# Competitive Analysis Template

**Purpose:** Standardized process for conducting competitive analysis on any company

**Quality Target:** 9.5/10 (enterprise-grade, client-ready)

---

## Quick Start

**For New Competitive Analysis:**

1. Copy this template directory:
   ```bash
   cp -r templates/competitive-analysis /path/to/new-project/
   cd /path/to/new-project
   ```

2. Follow phases in order:
   - Phase 0: Project Setup (directory structure, git init)
   - Phase 1: Research (use `competitive-research-brightdata`)
   - Phase 2: Analysis (manual analysis work)
   - Phase 3: Deliverables (write reports, create visualizations)
   - Phase 4: QA (use `competitive-analysis-quality-assurance`)
   - Phase 5: Iterations (as needed based on feedback)

3. Use skills at each phase:
   - **Research:** `Skill: competitive-research-brightdata`
   - **Analysis:** Manual + research tools
   - **QA:** `Skill: competitive-analysis-quality-assurance`
   - **Iterations:** `superpowers:brainstorming` → `superpowers:writing-plans`

---

## Deliverables Checklist

By end of project, you should have:

### Primary Reports:
- [ ] Executive Summary (DOCX + PDF, 15-20 pages)
- [ ] Full Report (DOCX + PDF, 50-70 pages)

### Visualizations (10 PDFs):
- [ ] Competitive Positioning Analysis
- [ ] Market Trends Analysis
- [ ] SWOT Analysis - Top Competitors
- [ ] Strategic Recommendations
- [ ] Threats & Opportunities
- [ ] Feature Comparison Matrix
- [ ] Pricing Analysis
- [ ] Technology Stack Comparison
- [ ] Market Positioning Map
- [ ] Target Segments Analysis

### Documentation:
- [ ] Research methodology notes
- [ ] Source references (15-20 sources)
- [ ] QA reports
- [ ] Iteration history

---

## Directory Structure

```
competitive-analysis-[company-name]/
├── 01-RESEARCH-INPUTS/
│   ├── competitor-data/
│   ├── market-research/
│   ├── pricing-data/
│   └── sources.md
├── 02-ANALYSIS-OUTPUTS/
│   ├── competitive-matrices/
│   ├── swot-analyses/
│   └── market-positioning/
├── 03-DELIVERABLES/
│   ├── current/
│   │   ├── DOCX/
│   │   ├── HTML/
│   │   └── PDF/
│   ├── VERSION-HISTORY.md
│   └── README.md
├── 04-QA-DOCUMENTATION/
│   ├── qa-reports/
│   ├── change-logs/
│   └── verification/
├── 05-ITERATIONS/
│   └── [iteration-N]/
├── 06-AUTOMATION/
│   ├── scripts/
│   └── templates/
└── docs/
    ├── plans/
    └── guides/
```

---

## Skills Required

### Custom Skills:
1. **competitive-research-brightdata** - Data gathering via Bright Data
2. **competitive-analysis-quality-assurance** - Quality verification

### Superpowers Skills:
3. **superpowers:brainstorming** - Requirements refinement
4. **superpowers:writing-plans** - Implementation planning
5. **superpowers:executing-plans** - Systematic execution
6. **superpowers:verification-before-completion** - Quality gates

---

## Quality Metrics

**Target Quality Score:** 9.5/10

**Measured By:**
- Source citations: 100% of claims cited
- Pricing accuracy: All pricing verified or marked "(est.)"
- Consistency: 100% across all documents
- Professional presentation: No marketing language, factual only
- Completeness: All deliverables in checklist completed

---

## Phase Guide Files

See individual phase files for detailed instructions:
- [01-RESEARCH-PHASE.md](./01-RESEARCH-PHASE.md)
- [02-ANALYSIS-PHASE.md](./02-ANALYSIS-PHASE.md)
- [03-DELIVERABLES-PHASE.md](./03-DELIVERABLES-PHASE.md)
- [04-QA-PHASE.md](./04-QA-PHASE.md)
- [05-ITERATION-PHASE.md](./05-ITERATION-PHASE.md)

**Master Workflow Reference:** For comprehensive workflow documentation including all scenarios, automation scripts, and decision guides, see [docs/COMPETITIVE-ANALYSIS-WORKFLOW.md](../../docs/COMPETITIVE-ANALYSIS-WORKFLOW.md)

---

## Deliverable Templates

See `deliverables-templates/` for:
- `executive-summary-template.md` - Executive summary structure
- `full-report-template.md` - Full report structure
- `visualization-template.html` - HTML visualization template

---

## Example Project

For a complete example of this framework in action, see the Maia Learning project:

- **Location:** `MAIA-PROJECT/` in the repository root
- **Deliverables:** `MAIA-PROJECT/03-DELIVERABLES/current/`
- **Documentation:** `MAIA-PROJECT/README.md`

This project demonstrates V2.0 quality deliverables (9.5/10) achieved through the full workflow.

---

**Template Version:** 1.0
**Based On:** Maia Learning Competitive Analysis (November 2025)
**Quality Level:** Enterprise-grade (9.5/10)
