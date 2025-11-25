# Competitive Analysis Template & Project Cleanup Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transform the Maia Learning competitive analysis project into a reusable template system while documenting all successful patterns, cleaning up project structure, and enhancing custom skills for future competitive analyses.

**Architecture:** Multi-phase iterative approach with review loops. Each phase produces documentation that feeds into the next, culminating in: (1) a reusable competitive analysis template, (2) clean project structure with clear inputs/outputs, (3) enhanced custom skills, and (4) iteration framework for quick updates.

**Tech Stack:**
- Markdown (documentation)
- Python (automation scripts)
- Pandoc (document conversion)
- Chrome Headless (PDF generation)
- Custom Claude Skills (competitive-analysis-quality-assurance, competitive-research-brightdata)

---

## PHASE 1: DISCOVERY & ITERATION REVIEW

**Objective:** Document the complete journey from initial research through V2.0, identifying successful patterns and areas for improvement.

### Task 1.1: Create Project Inventory

**Files:**
- Create: `docs/PROJECT-INVENTORY.md`

**Step 1: Catalog all files and directories**

Navigate to project root and inventory structure:

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
find . -type f -name "*.md" -o -name "*.docx" -o -name "*.pdf" -o -name "*.html" | sort > docs/file-inventory-temp.txt
```

**Step 2: Create structured inventory document**

Create `docs/PROJECT-INVENTORY.md`:

```markdown
# MaiaLearning Competitive Analysis - Project Inventory

**Date:** November 24, 2025
**Project:** Maia Learning Competitive Analysis
**Status:** Version 2.0 Complete

---

## Directory Structure

### /01-RESEARCH-INPUTS/
[List all files with descriptions]

### /02-ANALYSIS-OUTPUTS/
[List all files with descriptions]

### /03-WORKING-DOCUMENTS/
[List all files with descriptions]

### /04-QA-PROCESS/
[List all files with descriptions]

### /05-FINAL-DELIVERABLES/
[List all files with descriptions]

---

## File Categories

**Research Inputs:**
- Web scraping results
- Competitor data
- Market research

**Analysis Outputs:**
- Competitive matrices
- SWOT analyses
- Market positioning

**Working Documents:**
- Drafts
- Iterations
- QA reviews

**Final Deliverables:**
- Executive Summary (DOCX + PDF)
- Full Report (DOCX + PDF)
- 10 Visualization PDFs
```

**Step 3: Verify inventory completeness**

```bash
wc -l docs/PROJECT-INVENTORY.md
# Expected: 100+ lines documenting all major files
```

**Step 4: Commit**

```bash
git add docs/PROJECT-INVENTORY.md docs/file-inventory-temp.txt
git commit -m "docs: create project inventory for template extraction"
```

---

### Task 1.2: Document Iteration History

**Files:**
- Create: `docs/ITERATION-HISTORY.md`

**Step 1: Create iteration timeline**

Create `docs/ITERATION-HISTORY.md`:

```markdown
# Iteration History - Maia Learning Competitive Analysis

## Timeline of Major Iterations

### Iteration 1: Initial Research & Analysis (September-October 2025)
**Goal:** Gather competitive intelligence and create initial deliverables

**Inputs:**
- Web research on 7 competitors
- Market sizing data
- Pricing information

**Outputs:**
- Initial competitive analysis document
- Basic feature comparisons

**Challenges:**
- Incomplete source attribution
- Pricing inconsistencies
- Market sizing context unclear

**Duration:** ~6 weeks

---

### Iteration 2: QA Corrections & Source Attribution (November 2025)
**Goal:** Add source citations, fix pricing errors, enhance disclaimers

**Inputs:**
- Initial deliverables (HTML + DOCX)
- QA feedback identifying gaps

**Process:**
- competitive-analysis-quality-assurance skill used
- 35+ modifications across 7 HTML files
- 40+ inline citations added to Executive Summary
- 60+ inline citations added to Full Report

**Outputs:**
- Version 1.0 deliverables (9.5/10 quality)
- Executive Summary DOCX (26KB)
- Full Report DOCX (45KB)
- 10 Enterprise PDFs

**Key Fixes:**
- Naviance pricing: $6-8 → $8-12 (est.)
- SCOIR pricing: $5-6 → $4.80
- Market sizing context added
- Maia inferred rating disclaimer

**Duration:** ~3 days
**Quality Improvement:** 7.5/10 → 9.5/10

---

### Iteration 3: Tim's Strategic Revisions - V2.0 (November 24, 2025)
**Goal:** Flip strategy to US-primary, fix positioning maps, remove taglines

**Inputs:**
- Tim's strategic feedback
- Version 1.0 deliverables

**Process:**
- Created TIM-REVISIONS-PLAN.md (implementation plan)
- Created TIM-REVISIONS-INVENTORY.md (discovery phase)
- Implemented 4 major changes across 5 source files
- Regenerated 3 PDFs + created 2 new enterprise-themed PDFs

**Outputs:**
- Version 2.0 deliverables
- Executive Summary: 26KB → 28KB (strategic content added)
- Full Report: 45KB → 46KB (strategic content added)
- Strategic Recommendations PDF: 264KB → 275KB
- Market Positioning PDF: 342KB → 386KB (four-quadrant chart)
- Competitive Positioning PDF: 222KB → 241KB (pricing fix)

**Key Changes:**
1. Strategic Recommendations - US-Primary Flip
   - Reduced 7 priorities → 6 priorities
   - Priority 1: "Attack US Market" ($650K-1.25M)
   - Added "International Benefits Automatically" section
   - Total investment: $1.77M-3.4M (was $1.27M-2.35M)

2. Positioning Maps - Four-Quadrant Format
   - Replaced text ASCII chart with HTML/CSS visual
   - Visible crossbars (horizontal + vertical lines)
   - Four quadrants labeled (Q1 IDEAL = upper right)

3. Marketing Taglines - Removed
   - Removed 3 tagline options
   - Removed elevator pitch section
   - Kept positioning statement + proof points

4. Naviance Pricing - Consistency Fix
   - Fixed final instance: $6-8 → $8-12 (est.)

**Duration:** ~4 hours
**Consistency:** 100% across all documents

---

## Iteration Pattern Analysis

### What Worked Well:

**1. Skill-Based Workflow:**
- @competitive-analysis-quality-assurance for systematic review
- @competitive-research-brightdata for initial research
- @superpowers:brainstorming before implementation
- @superpowers:verification-before-completion for quality gates

**2. Phased Approach:**
- Discovery phase (inventory findings)
- Planning phase (structured approach)
- Implementation phase (bite-sized tasks)
- QA phase (verification against requirements)

**3. Documentation:**
- Clear before/after specifications
- Comprehensive change logs
- QA review reports
- README updates with version history

**4. Version Control:**
- Backups created before major changes
- Clear version naming (V1.0 → V2.0)
- Source files preserved (HTML for PDFs)

### What Could Be Improved:

**1. Initial Structure:**
- Files scattered across multiple directories
- Unclear input/output separation
- No clear iteration tracking from start

**2. Skill Usage Documentation:**
- Skills used but not documented in-process
- No "how we used skills" guide created
- Workflow not captured for reuse

**3. Template Opportunity:**
- Deliverable structure discovered organically
- Could have started with template
- Competitive analysis pattern repeatable

**4. Automation:**
- Manual PDF regeneration process
- Could script common operations
- Batch operations not automated

---

## Skills Successfully Utilized

### Custom Skills:
1. **competitive-analysis-quality-assurance**
   - Used for: Systematic fact-checking, source verification
   - Result: Quality 7.5/10 → 9.5/10
   - Would use again: YES

2. **competitive-research-brightdata**
   - Used for: Initial competitor research
   - Result: Comprehensive data gathering
   - Would use again: YES

### Superpowers Skills:
3. **superpowers:brainstorming**
   - Used for: Refining Tim's requirements before implementation
   - Result: Clear direction, no rework needed
   - Would use again: YES

4. **superpowers:verification-before-completion**
   - Used for: Final QA checks
   - Result: Caught all inconsistencies
   - Would use again: YES

5. **superpowers:writing-plans** (current)
   - Using for: Creating this implementation plan
   - Expected result: Structured multi-phase approach

6. **superpowers:executing-plans** (next)
   - Will use for: Implementing this plan task-by-task
   - Expected result: Systematic completion

### Skills NOT Used But Could Have Been:
- **superpowers:using-git-worktrees**: Could have isolated V2.0 work
- **superpowers:test-driven-development**: Could have tested document generation
- **superpowers:systematic-debugging**: Could have debugged PDF generation issues faster

---

## Lessons Learned for Next Competitive Analysis

### Do From Start:
1. Create clear directory structure (inputs/outputs/iterations)
2. Use competitive-research-brightdata for initial research
3. Start with deliverables template (don't discover organically)
4. Document skill usage as you go
5. Create automation scripts for repetitive tasks
6. Use git worktrees for major iterations
7. Keep source files (HTML) for all PDFs

### Don't:
1. Scatter files across directories without structure
2. Skip brainstorming phase (leads to rework)
3. Forget to create backups before major changes
4. Skip verification steps (catches errors early)
5. Wait until end to document process

### Automation Opportunities:
1. PDF generation from all HTML files (single command)
2. DOCX → HTML → PDF pipeline (standardized)
3. Batch QA checks (consistent formatting, citations)
4. Version bumping (automated V1.0 → V2.0)
5. Combined PDF regeneration (include all updates)

---

## Next Steps

Use this iteration history to:
1. Extract reusable patterns → Competitive Analysis Template
2. Document skill workflows → Skill Usage Guide
3. Create automation scripts → Process Efficiency
4. Restructure project → Clear Inputs/Outputs
5. Update custom skills → Enhanced Capabilities
```

**Step 2: Verify iteration history completeness**

```bash
grep "### Iteration" docs/ITERATION-HISTORY.md | wc -l
# Expected: 3 (three major iterations documented)
```

**Step 3: Commit**

```bash
git add docs/ITERATION-HISTORY.md
git commit -m "docs: document complete iteration history with lessons learned"
```

---

### Task 1.3: Skills Usage Report

**Files:**
- Create: `docs/SKILLS-USAGE-REPORT.md`

**Step 1: Document each skill used**

Create `docs/SKILLS-USAGE-REPORT.md`:

```markdown
# Skills Usage Report - Maia Learning Competitive Analysis

**Project:** Maia Learning Competitive Analysis
**Date:** November 24, 2025
**Purpose:** Document which skills were used, how, and outcomes

---

## Custom Skills Used

### 1. competitive-research-brightdata

**When Used:** Initial research phase (September-October 2025)

**How Used:**
```bash
# Invoked skill for company research
Skill: competitive-research-brightdata

# Typical usage pattern:
1. Identify competitors (Naviance, SCOIR, SchooLinks, Xello, Cialfo, etc.)
2. Skill gathered data via Bright Data web scraping
3. Output: Competitor profiles with pricing, features, market positioning
```

**Inputs:**
- List of competitor names
- Research questions (pricing, features, positioning, funding)

**Outputs:**
- Competitor data (CSV/JSON format)
- Website content (scraped and structured)
- Market intelligence (funding, growth, reviews)

**Outcome:** Comprehensive competitive data gathered efficiently

**Would Use Again:** YES - Essential for initial research

**Improvements Needed:**
- Document output format expectations
- Create template for research questions
- Standardize data schema

---

### 2. competitive-analysis-quality-assurance

**When Used:** QA phase (November 2025, Iteration 2)

**How Used:**
```bash
# Invoked skill for systematic review
Skill: competitive-analysis-quality-assurance

# Typical usage pattern:
1. Skill reviewed deliverables systematically
2. Identified gaps (missing citations, pricing errors, disclaimers)
3. Generated QA report with specific findings
4. Guided implementation of fixes
```

**Inputs:**
- Draft deliverables (DOCX, HTML, PDF)
- Source materials for fact-checking

**Outputs:**
- QA report with findings (35+ issues identified)
- Prioritized fix list
- Before/after verification

**Outcome:** Quality improved from 7.5/10 to 9.5/10

**Would Use Again:** YES - Critical for quality assurance

**Improvements Needed:**
- Add "consistency check" across all documents
- Include source attribution verification
- Check for marketing language vs. factual claims

---

## Superpowers Skills Used

### 3. superpowers:brainstorming

**When Used:** Before implementing Tim's revisions (V2.0)

**How Used:**
```bash
# Invoked skill before coding/implementation
Skill: superpowers:brainstorming

# Typical usage pattern:
1. Presented Tim's requirements (rough)
2. Skill asked clarifying questions
3. Refined requirements into clear specifications
4. Got user approval before proceeding
```

**Inputs:**
- Tim's feedback (verbal/rough notes)
- Current deliverables state

**Outputs:**
- 6 clarifying questions asked
- User answers documented
- Clear implementation direction
- No rework needed

**Outcome:** Perfect alignment with Tim's vision, zero rework

**Would Use Again:** YES - Essential before major changes

**Improvements Needed:**
- None - worked perfectly as designed

---

### 4. superpowers:verification-before-completion

**When Used:** End of each phase (QA verification)

**How Used:**
```bash
# Used before marking tasks complete
Skill: superpowers:verification-before-completion

# Typical usage pattern:
1. Before claiming "complete", ran verification
2. Checked actual output against requirements
3. Confirmed tests pass, builds succeed
4. Evidence before assertions
```

**Inputs:**
- Completed work (deliverables)
- Original requirements

**Outputs:**
- Verification checklist (all items checked)
- Evidence of completion (file sizes, checksums)
- QA report

**Outcome:** 100% confidence in deliverable quality

**Would Use Again:** YES - Prevents premature "done" claims

**Improvements Needed:**
- None - critical quality gate

---

### 5. superpowers:writing-plans (CURRENT)

**When Used:** Creating this meta-project plan

**How Used:**
```bash
# Invoked for complex multi-phase planning
Skill: superpowers:writing-plans

# Expected usage pattern:
1. Define goal, architecture, tech stack
2. Break into bite-sized tasks (2-5 min each)
3. Provide exact file paths, code, commands
4. Include verification steps
5. Save to docs/plans/<filename>.md
```

**Inputs:**
- User's request for template creation + cleanup
- Current project state

**Outputs:**
- This implementation plan (comprehensive, multi-phase)
- Exact tasks with file paths
- Code examples and verification steps

**Expected Outcome:** Systematic completion of meta-project

---

## Skills NOT Used (But Could Have Been)

### 6. superpowers:using-git-worktrees

**When Could Have Used:** Before V2.0 implementation

**Why Not Used:**
- Working directly in main directory
- No isolation of V2.0 work from V1.0

**Benefit If Used:**
- V2.0 work isolated in separate worktree
- Could switch between V1.0 and V2.0 easily
- Safer for major changes

**Recommendation:** Use for next major iteration

---

### 7. superpowers:test-driven-development

**When Could Have Used:** Document generation automation

**Why Not Used:**
- Not writing traditional code
- Document generation was manual

**Benefit If Used:**
- Could have tested PDF generation
- Verified document structure programmatically
- Caught formatting issues earlier

**Recommendation:** Use when creating automation scripts

---

### 8. superpowers:systematic-debugging

**When Could Have Used:** PDF conversion troubleshooting

**Why Not Used:**
- PDF conversion errors were straightforward
- Switched approaches instead of debugging

**Benefit If Used:**
- Could have debugged pdflatex issues
- Might have found solution faster

**Recommendation:** Use when encountering complex technical issues

---

## Skill Workflow Patterns Discovered

### Pattern 1: Research → QA → Revise

```
competitive-research-brightdata (gather data)
    ↓
competitive-analysis-quality-assurance (verify quality)
    ↓
superpowers:verification-before-completion (final check)
```

**Use For:** Any competitive analysis project

---

### Pattern 2: Brainstorm → Plan → Execute

```
superpowers:brainstorming (refine requirements)
    ↓
superpowers:writing-plans (create implementation plan)
    ↓
superpowers:executing-plans (systematic implementation)
```

**Use For:** Major feature additions or strategic changes

---

### Pattern 3: Iterate → Verify → Document

```
[Make changes]
    ↓
superpowers:verification-before-completion (verify)
    ↓
[Update documentation]
    ↓
competitive-analysis-quality-assurance (consistency check)
```

**Use For:** Ensuring quality across iterations

---

## Recommendations for Skill Enhancement

### For competitive-analysis-quality-assurance:

**Add to skill:**
1. Consistency check across all documents (verify same data everywhere)
2. Source attribution verification (all claims cited)
3. Marketing language detector (flag subjective claims)
4. Cross-reference validator (ensure internal consistency)
5. Version comparison (V1.0 vs V2.0 what changed)

**Implementation:**
```markdown
## New QA Checklist Items

### Consistency Verification:
- [ ] Strategic recommendations identical across Executive Summary, Full Report, Viz PDF
- [ ] Pricing data consistent across all references
- [ ] Investment totals match across documents
- [ ] Company descriptions consistent everywhere

### Source Attribution:
- [ ] All pricing claims cited
- [ ] All market share claims cited
- [ ] All funding amounts cited
- [ ] All satisfaction ratings cited

### Language Check:
- [ ] No marketing hyperbole ("best", "leading", "revolutionary")
- [ ] Factual claims only
- [ ] Disclaimers for estimates/inferences
- [ ] Professional tone throughout
```

---

### For competitive-research-brightdata:

**Add to skill:**
1. Output format standardization (always JSON with schema)
2. Research question templates (pricing, features, positioning)
3. Data validation rules (check for completeness)
4. Citation formatting (auto-generate source references)

**Implementation:**
```markdown
## Research Output Schema

```json
{
  "competitor": {
    "name": "Company Name",
    "website": "https://...",
    "pricing": {
      "model": "per-student",
      "range": "$X-Y",
      "source": "URL",
      "date_verified": "YYYY-MM-DD",
      "confidence": "verified|estimated|unknown"
    },
    "features": [...],
    "positioning": {...},
    "funding": {...}
  }
}
```

## Standard Research Questions

1. Pricing: What is the per-student cost?
2. Features: What are the top 10 features?
3. Positioning: How do they describe themselves?
4. Funding: Latest funding round and amount?
5. Reviews: Customer satisfaction ratings?
```

---

## Next Steps

Use this skills usage report to:
1. Update competitive-analysis-quality-assurance skill
2. Update competitive-research-brightdata skill
3. Create "Skill Usage Guide" for future projects
4. Document workflow patterns in template
```

**Step 2: Verify skills coverage**

```bash
grep "^### " docs/SKILLS-USAGE-REPORT.md | wc -l
# Expected: 8+ (all skills documented)
```

**Step 3: Commit**

```bash
git add docs/SKILLS-USAGE-REPORT.md
git commit -m "docs: document all skills used and workflow patterns"
```

---

## PHASE 2: TEMPLATE CREATION

**Objective:** Extract successful patterns into a reusable competitive analysis template that can be used for any company.

### Task 2.1: Create Competitive Analysis Template Structure

**Files:**
- Create: `templates/competitive-analysis/README.md`
- Create: `templates/competitive-analysis/00-PROJECT-SETUP.md`
- Create: `templates/competitive-analysis/01-RESEARCH-PHASE.md`
- Create: `templates/competitive-analysis/02-ANALYSIS-PHASE.md`
- Create: `templates/competitive-analysis/03-DELIVERABLES-PHASE.md`
- Create: `templates/competitive-analysis/04-QA-PHASE.md`
- Create: `templates/competitive-analysis/05-ITERATION-PHASE.md`

**Step 1: Create template directory**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mkdir -p templates/competitive-analysis/deliverables-templates
mkdir -p templates/competitive-analysis/automation-scripts
```

**Step 2: Create main template README**

Create `templates/competitive-analysis/README.md`:

```markdown
# Competitive Analysis Template

**Purpose:** Standardized process for conducting competitive analysis on any company

**Duration:** 4-8 weeks (depending on complexity)

**Quality Target:** 9.5/10 (enterprise-grade, client-ready)

---

## Quick Start

**For New Competitive Analysis:**

1. Copy this template directory:
   ```bash
   cp -r templates/competitive-analysis /path/to/new-analysis/
   cd /path/to/new-analysis
   ```

2. Follow phases in order:
   - Phase 0: Project Setup
   - Phase 1: Research
   - Phase 2: Analysis
   - Phase 3: Deliverables
   - Phase 4: QA
   - Phase 5: Iterations (as needed)

3. Use skills at each phase:
   - Research: @competitive-research-brightdata
   - Analysis: Manual + research tools
   - QA: @competitive-analysis-quality-assurance
   - Iterations: @superpowers:brainstorming → @superpowers:writing-plans

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
│   └── sources.md
├── 02-ANALYSIS-OUTPUTS/
│   ├── competitive-matrices/
│   ├── swot-analyses/
│   └── market-positioning/
├── 03-WORKING-DOCUMENTS/
│   ├── drafts/
│   ├── iterations/
│   └── qa-reviews/
├── 04-DELIVERABLES/
│   ├── DOCX/
│   ├── HTML/
│   ├── PDF/
│   └── README.md
├── 05-QA-DOCUMENTATION/
│   ├── qa-reports/
│   ├── change-logs/
│   └── version-history.md
└── docs/
    ├── plans/
    ├── iterations/
    └── templates/
```

---

## Skills Required

### Custom Skills:
1. **competitive-research-brightdata** (data gathering)
2. **competitive-analysis-quality-assurance** (quality verification)

### Superpowers Skills:
3. **superpowers:brainstorming** (requirements refinement)
4. **superpowers:writing-plans** (implementation planning)
5. **superpowers:executing-plans** (systematic execution)
6. **superpowers:verification-before-completion** (quality gates)

---

## Time Estimates

| Phase | Duration | Key Activities |
|-------|----------|----------------|
| 0. Setup | 1-2 days | Structure, tools, initial research questions |
| 1. Research | 2-3 weeks | Competitor data, market research, source gathering |
| 2. Analysis | 1-2 weeks | SWOT, positioning, feature comparison, recommendations |
| 3. Deliverables | 1-2 weeks | Write reports, create visualizations, generate PDFs |
| 4. QA | 3-5 days | Source verification, consistency checks, quality review |
| 5. Iterations | 1-2 weeks | Client feedback, revisions, final polish |

**Total:** 6-10 weeks

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

## Next Steps

See individual phase files for detailed instructions:
- [00-PROJECT-SETUP.md](./00-PROJECT-SETUP.md)
- [01-RESEARCH-PHASE.md](./01-RESEARCH-PHASE.md)
- [02-ANALYSIS-PHASE.md](./02-ANALYSIS-PHASE.md)
- [03-DELIVERABLES-PHASE.md](./03-DELIVERABLES-PHASE.md)
- [04-QA-PHASE.md](./04-QA-PHASE.md)
- [05-ITERATION-PHASE.md](./05-ITERATION-PHASE.md)
```

**Step 3: Verify template README created**

```bash
cat templates/competitive-analysis/README.md | head -20
# Expected: See template README header
```

**Step 4: Commit**

```bash
git add templates/competitive-analysis/
git commit -m "feat: create competitive analysis template structure"
```

---

### Task 2.2: Create Research Phase Template

**Files:**
- Create: `templates/competitive-analysis/01-RESEARCH-PHASE.md`

**Step 1: Create research phase guide**

Create `templates/competitive-analysis/01-RESEARCH-PHASE.md`:

```markdown
# Phase 1: Research

**Duration:** 2-3 weeks
**Objective:** Gather comprehensive competitive intelligence
**Skill:** @competitive-research-brightdata

---

## Pre-Research Checklist

Before starting research:

- [ ] Identify 5-7 primary competitors
- [ ] Identify 3-5 secondary competitors (comparison/context)
- [ ] Define research questions (see template below)
- [ ] Set up research tracking spreadsheet
- [ ] Create sources.md file for citations

---

## Research Questions Template

Copy these questions for each competitor:

### Company Overview:
1. What is the company's official name and website?
2. When was the company founded?
3. Who are the founders/key executives?
4. What is their mission statement/positioning?

### Pricing:
5. What is the per-student cost? (verify or estimate)
6. What pricing model do they use? (per-student, per-school, tiered)
7. Are there setup fees or contracts?
8. What discounts are available? (volume, multi-year, etc.)

### Features:
9. What are the top 10 core features?
10. What AI capabilities do they have?
11. What integrations do they offer?
12. What makes them unique/differentiated?

### Market Position:
13. What is their estimated market share?
14. How many students/schools do they serve?
15. What geographic markets do they serve?
16. What customer segments do they target?

### Funding & Growth:
17. What is their latest funding round? (amount, date, investors)
18. What is their estimated revenue?
19. What is their growth rate? (if known)
20. Are they profitable or burning cash?

### Customer Satisfaction:
21. What are their public review ratings? (G2, Capterra, etc.)
22. What do customers praise?
23. What do customers complain about?
24. What is their NPS score? (if available)

---

## Using @competitive-research-brightdata

### Step 1: Prepare competitor list

Create `01-RESEARCH-INPUTS/competitor-list.md`:

```markdown
# Competitor List

## Primary Competitors:
1. [Competitor 1] - [Website]
2. [Competitor 2] - [Website]
3. [Competitor 3] - [Website]
4. [Competitor 4] - [Website]
5. [Competitor 5] - [Website]

## Secondary Competitors:
1. [Competitor 6] - [Website]
2. [Competitor 7] - [Website]
```

### Step 2: Invoke skill

```bash
# Use competitive-research-brightdata skill
Skill: competitive-research-brightdata

# Provide:
- Competitor names
- Research questions (from template above)
- Output format preference (JSON/CSV/Markdown)
```

### Step 3: Organize research outputs

```bash
# Create directory structure
mkdir -p 01-RESEARCH-INPUTS/competitor-data/
mkdir -p 01-RESEARCH-INPUTS/market-research/
mkdir -p 01-RESEARCH-INPUTS/pricing-data/
mkdir -p 01-RESEARCH-INPUTS/feature-data/

# Move skill outputs to appropriate directories
mv competitor-*.json 01-RESEARCH-INPUTS/competitor-data/
```

---

## Manual Research Tasks

**Not everything can be automated. Manually research:**

### 1. Review Sites:
- G2.com (search for each competitor)
- Capterra.com (CCR platforms category)
- TrustRadius (education software)
- ProductHunt (for new/innovative platforms)

**Record:**
- Rating (X.X/5)
- Number of reviews
- Recent review themes
- Source URL + date accessed

### 2. Funding Databases:
- Crunchbase (company profiles, funding rounds)
- PitchBook (private company data)
- CB Insights (market intelligence)

**Record:**
- Latest funding round (amount, date, investors)
- Total funding raised
- Valuation (if public)
- Source URL + date accessed

### 3. Company Websites:
- Read "About Us" pages
- Review pricing pages (screenshot if available)
- Explore feature lists
- Read case studies/testimonials
- Download any public materials (whitepapers, brochures)

**Record:**
- Official positioning statement
- Pricing (screenshot + transcribe)
- Feature lists
- Source: [Company Name] website, accessed [Date]

### 4. Industry Reports:
- Search for "college readiness platform market report"
- Search for "EdTech market sizing"
- Look for analyst reports (Gartner, Forrester if available)

**Record:**
- Market size estimates
- Growth projections
- Trends identified
- Source: [Report Name], [Publisher], [Date]

---

## Research Tracking Spreadsheet

Create `01-RESEARCH-INPUTS/research-tracker.csv`:

```csv
Competitor,Pricing Verified,Features Listed,Reviews Found,Funding Found,Website Scraped,Completeness %
Competitor 1,Yes,Yes,Yes,Yes,Yes,100%
Competitor 2,Estimated,Yes,Yes,No,Yes,80%
...
```

---

## Sources.md Template

Create `01-RESEARCH-INPUTS/sources.md`:

```markdown
# Research Sources

**Project:** [Company Name] Competitive Analysis
**Research Period:** [Start Date] - [End Date]

---

## Competitor-Specific Sources

### [Competitor 1]

1. **Company Website**
   - URL: https://...
   - Date Accessed: YYYY-MM-DD
   - Data Gathered: Pricing, features, positioning

2. **G2 Reviews**
   - URL: https://g2.com/products/[competitor]
   - Date Accessed: YYYY-MM-DD
   - Rating: X.X/5 (N reviews)

3. **Crunchbase**
   - URL: https://crunchbase.com/organization/[competitor]
   - Date Accessed: YYYY-MM-DD
   - Funding: $XM (Series A, Date)

---

## Market Research Sources

1. **EdTech Market Report**
   - Publisher: [Name]
   - Date: YYYY
   - Key Findings: Market size $X.XB, CAGR X%

---

## Citation Format

Use this format in deliverables:
- `(Company Name, YYYY)` - for company-reported data
- `(G2, YYYY)` - for review ratings
- `(Crunchbase, YYYY)` - for funding data
- `(Industry Report Name, YYYY)` - for market data
```

---

## Research Phase Completion Checklist

Before moving to Analysis Phase:

- [ ] All competitors researched (5-7 primary)
- [ ] Research questions answered (20 per competitor)
- [ ] All sources documented in sources.md
- [ ] Research tracker shows 80%+ completeness
- [ ] Data organized in directory structure
- [ ] Gaps identified and documented (some data unavailable is OK)

---

## Common Research Challenges

### Challenge 1: Pricing Not Public

**Solution:**
- Mark as "(est.)" or "not publicly disclosed"
- Use ranges from industry reports
- Check for old pricing pages (Wayback Machine)
- Note in disclaimer: "Estimated from industry sources"

### Challenge 2: Conflicting Data

**Solution:**
- Document all sources
- Use most recent data
- Note discrepancy in footnote
- Prefer official company sources over third-party

### Challenge 3: Incomplete Feature Data

**Solution:**
- Use "Features advertised on website"
- Note: "Full feature list may not be public"
- Compare only advertised features
- Mark unknown features as "Unknown/Not Advertised"

---

## Output Format

By end of Research Phase, you should have:

```
01-RESEARCH-INPUTS/
├── competitor-list.md (5-7 competitors)
├── sources.md (15-20 sources)
├── research-tracker.csv (completeness tracker)
├── competitor-data/
│   ├── competitor-1.json
│   ├── competitor-2.json
│   └── ...
├── market-research/
│   ├── market-sizing.md
│   ├── growth-trends.md
│   └── industry-reports/
├── pricing-data/
│   ├── pricing-comparison.csv
│   └── pricing-screenshots/
└── feature-data/
    ├── feature-comparison.csv
    └── feature-lists/
```

---

## Next Phase

Once research is complete, move to:
**[02-ANALYSIS-PHASE.md](./02-ANALYSIS-PHASE.md)**
```

**Step 2: Verify research phase template created**

```bash
wc -l templates/competitive-analysis/01-RESEARCH-PHASE.md
# Expected: 200+ lines (comprehensive research guide)
```

**Step 3: Commit**

```bash
git add templates/competitive-analysis/01-RESEARCH-PHASE.md
git commit -m "feat: create research phase template with skill integration"
```

---

### Task 2.3: Create Deliverables Templates

**Files:**
- Create: `templates/competitive-analysis/deliverables-templates/executive-summary-template.md`
- Create: `templates/competitive-analysis/deliverables-templates/full-report-template.md`
- Create: `templates/competitive-analysis/deliverables-templates/visualization-template.html`

**Step 1: Create executive summary template**

Create `templates/competitive-analysis/deliverables-templates/executive-summary-template.md`:

```markdown
# Executive Summary: [Company Name] Competitive Analysis

**Company:** [Company Name]
**Industry:** [Industry]
**Analysis Date:** [Month Year]
**Analyst:** [Your Name]

---

## Executive Overview

[Company Name] operates in the [industry] space serving [target customers]. This competitive analysis examines [Company Name]'s position relative to [N] primary competitors across [key dimensions: pricing, features, market share, etc.].

**Key Finding:** [One sentence summary of most important finding]

---

## Competitive Landscape

[Company Name] competes against [N] primary platforms:

1. **[Competitor 1]** - [Brief positioning: market leader, innovation challenger, etc.]
2. **[Competitor 2]** - [Brief positioning]
3. **[Competitor 3]** - [Brief positioning]
4. **[Competitor 4]** - [Brief positioning]
5. **[Competitor 5]** - [Brief positioning]

**Market Characteristics:**
- Total Addressable Market (TAM): $[X]M-[Y]M
- Growth Rate: [X]% CAGR (Source, Year)
- Market Leader: [Competitor Name] with [X]% share

---

## Key Findings

### 1. [Finding Category 1: e.g., Pricing Position]

**Summary:** [Company Name] is priced [comparatively: higher/lower/middle] at $[X]/[unit] versus competitors ranging $[Y]-[Z]/[unit].

**Implications:**
- [Implication 1]
- [Implication 2]
- [Implication 3]

**Source:** ([Company Website, Year]; [Competitor Website, Year])

---

### 2. [Finding Category 2: e.g., Feature Parity]

**Summary:** [Company Name] [leads/matches/lags] in [feature category] with [specific features].

**Competitive Gaps:**
- [Gap 1]: [Competitor X] has [feature] that [Company Name] lacks
- [Gap 2]: [Competitor Y] has [feature] that [Company Name] lacks

**Competitive Advantages:**
- [Advantage 1]: [Company Name] has [unique feature] that competitors lack
- [Advantage 2]: [Company Name] has [unique feature] that competitors lack

**Source:** ([Feature Comparison, Date])

---

[Continue for 5-7 key findings total]

---

## Strategic Recommendations

### Priority 1: [Recommendation Title] - [CRITICAL/HIGH/MEDIUM]

**Objective:** [What this achieves in one sentence]

**Rationale:** [Why this is important - 2-3 sentences with data]

**Implementation:**
- **Action 1:** [Specific action] ([Timeline], $[Investment])
- **Action 2:** [Specific action] ([Timeline], $[Investment])
- **Action 3:** [Specific action] ([Timeline], $[Investment])

**Investment:** $[X]K-[Y]K
**Timeline:** Q[X] 20XX - Q[Y] 20XX
**Expected Return:** [Quantified outcome]

**Source:** ([Analysis Reference])

---

### Priority 2: [Recommendation Title] - [CRITICAL/HIGH/MEDIUM]

[Same structure as Priority 1]

---

[Continue for 5-7 recommendations total]

---

## Implementation Timeline

**Q1 20XX (Month-Month):**
- Start [Priority 1, Action 1]
- [Milestone 2]
- [Milestone 3]

**Q2 20XX (Month-Month):**
- Complete [Priority 1]
- Start [Priority 2]
- [Milestone]

**Q3 20XX (Month-Month):**
- [Milestones]

**Q4 20XX (Month-Month):**
- [Milestones]

---

## Critical Decision Points

### Decision 1: [Title]

**Context:** [Situation requiring decision]

**Options:**
- **Option A:** [Description] - [Pros/Cons]
- **Option B:** [Description] - [Pros/Cons]
- **Option C:** [Description] - [Pros/Cons]

**Recommendation:** [Which option and why]

---

## Competitive Positioning Summary

[Company Name] is positioned as [positioning statement]. Current competitive position:

**Strengths:**
- [Unique strength 1]
- [Unique strength 2]
- [Unique strength 3]

**Weaknesses:**
- [Gap vs. competitors 1]
- [Gap vs. competitors 2]
- [Gap vs. competitors 3]

**Opportunities:**
- [Market opportunity 1]
- [Market opportunity 2]
- [Market opportunity 3]

**Threats:**
- [Competitive threat 1]
- [Competitive threat 2]
- [Competitive threat 3]

---

## Investment Summary

**Total Recommended Investment:** $[X]M-[Y]M over [N] months

**Priority Breakdown:**
| Priority Level | Investment | Timeline | Expected Return |
|----------------|-----------|----------|-----------------|
| Critical | $[X]K-[Y]K | Q[X]-Q[Y] 20XX | [Outcome] |
| High | $[X]K-[Y]K | Q[X]-Q[Y] 20XX | [Outcome] |
| Medium | $[X]K-[Y]K | Q[X]-Q[Y] 20XX | [Outcome] |
| **Total** | **$[X]M-[Y]M** | **[Timeline]** | **[Total Outcome]** |

---

## Sources & References

### Competitor Data:
1. [Competitor 1] - [Website URL], accessed [Date]
2. [Competitor 2] - [Website URL], accessed [Date]
3. [Competitor 3] - [Website URL], accessed [Date]

### Market Research:
4. [Industry Report Name] - [Publisher], [Date]
5. [Market Sizing Report] - [Publisher], [Date]

### Review Sites:
6. G2 - [Category], accessed [Date]
7. Capterra - [Category], accessed [Date]

### Funding Data:
8. Crunchbase - [Company Profiles], accessed [Date]
9. PitchBook - [Industry Analysis], accessed [Date]

[Continue for 15-20 total sources]

---

**Report Length:** 15-20 pages
**Analysis Period:** [Start Date] - [End Date]
**Version:** [1.0, 2.0, etc.]
**Status:** [Draft, Final, Client-Ready]
```

**Step 2: Verify template created**

```bash
grep "^## " templates/competitive-analysis/deliverables-templates/executive-summary-template.md | wc -l
# Expected: 10+ sections
```

**Step 3: Commit**

```bash
git add templates/competitive-analysis/deliverables-templates/
git commit -m "feat: create executive summary template structure"
```

---

## PHASE 3: PROJECT RESTRUCTURING

**Objective:** Reorganize the Maia Learning project into clean input/output structure with clear iteration tracking.

### Task 3.1: Design New Directory Structure

**Files:**
- Create: `docs/NEW-STRUCTURE-DESIGN.md`

**Step 1: Design ideal structure**

Create `docs/NEW-STRUCTURE-DESIGN.md`:

```markdown
# New Project Structure Design

**Current Problem:** Files scattered across multiple directories, unclear organization

**Proposed Solution:** Clear input/output separation with iteration tracking

---

## New Directory Structure

```
MaiaLearningResearch/
│
├── 00-PROJECT-MANAGEMENT/
│   ├── README.md (project overview)
│   ├── TIMELINE.md (project timeline)
│   ├── STAKEHOLDERS.md (Tim, team, client)
│   └── STATUS.md (current status dashboard)
│
├── 01-RESEARCH-INPUTS/
│   ├── README.md (what's in this directory)
│   ├── sources.md (all sources catalog)
│   │
│   ├── competitor-data/
│   │   ├── naviance.json
│   │   ├── scoir.json
│   │   ├── schoolinks.json
│   │   └── ...
│   │
│   ├── market-research/
│   │   ├── market-sizing.md
│   │   ├── growth-trends.md
│   │   └── industry-reports/
│   │
│   ├── pricing-data/
│   │   ├── pricing-comparison.csv
│   │   └── pricing-screenshots/
│   │
│   └── feature-data/
│       ├── feature-matrix.csv
│       └── feature-lists/
│
├── 02-ANALYSIS-OUTPUTS/
│   ├── README.md
│   │
│   ├── competitive-matrices/
│   │   ├── feature-comparison.csv
│   │   ├── pricing-comparison.csv
│   │   └── positioning-comparison.csv
│   │
│   ├── swot-analyses/
│   │   ├── naviance-swot.md
│   │   ├── scoir-swot.md
│   │   └── maia-swot.md
│   │
│   ├── market-positioning/
│   │   ├── positioning-map.md
│   │   ├── strategic-groups.md
│   │   └── competitive-landscape.md
│   │
│   └── strategic-recommendations/
│       ├── recommendations.md
│       ├── investment-estimates.md
│       └── implementation-roadmap.md
│
├── 03-DELIVERABLES/
│   ├── README.md (what's deliverable, what's WIP)
│   ├── VERSION-HISTORY.md (V1.0 → V2.0 tracking)
│   │
│   ├── current/ (V2.0 - most recent)
│   │   ├── DOCX/
│   │   │   ├── executive-summary-CORRECTED.docx
│   │   │   └── full-report-CORRECTED.docx
│   │   │
│   │   ├── HTML/
│   │   │   ├── executive-summary-CORRECTED.html
│   │   │   ├── full-report-CORRECTED.html
│   │   │   └── visualizations/
│   │   │       ├── strategic-recommendations-viz.html
│   │   │       ├── market-positioning-top4-viz.html
│   │   │       └── ...
│   │   │
│   │   └── PDF/
│   │       ├── executive-summary-CORRECTED.pdf
│   │       ├── full-report-CORRECTED.pdf
│   │       └── visualizations/
│   │           ├── strategic-recommendations-viz-ENTERPRISE.pdf
│   │           └── ...
│   │
│   ├── v1.0/ (archived)
│   │   ├── DOCX/
│   │   ├── HTML/
│   │   └── PDF/
│   │
│   └── v0.9/ (initial drafts - archived)
│
├── 04-QA-DOCUMENTATION/
│   ├── README.md
│   │
│   ├── qa-reports/
│   │   ├── v1.0-qa-report.md
│   │   ├── v2.0-qa-report.md
│   │   └── tim-revisions-qa-review.md
│   │
│   ├── change-logs/
│   │   ├── v1.0-changes.md
│   │   ├── v2.0-changes.md
│   │   └── tim-revisions-changes.md
│   │
│   └── verification/
│       ├── consistency-checks.md
│       ├── source-verification.md
│       └── quality-metrics.md
│
├── 05-ITERATIONS/
│   ├── README.md (iteration history overview)
│   │
│   ├── iteration-1-initial-research/
│   │   ├── NOTES.md
│   │   ├── outputs/
│   │   └── lessons-learned.md
│   │
│   ├── iteration-2-qa-corrections/
│   │   ├── NOTES.md
│   │   ├── qa-findings.md
│   │   ├── fixes-applied.md
│   │   └── lessons-learned.md
│   │
│   └── iteration-3-tim-revisions/
│       ├── NOTES.md
│       ├── TIM-REVISIONS-PLAN.md
│       ├── TIM-REVISIONS-INVENTORY.md
│       ├── TIM-REVISIONS-QA-REVIEW.md
│       └── lessons-learned.md
│
├── 06-AUTOMATION/
│   ├── README.md (how to use scripts)
│   │
│   ├── scripts/
│   │   ├── generate-pdfs.sh
│   │   ├── docx-to-html.py
│   │   ├── html-to-pdf.sh
│   │   ├── qa-consistency-check.py
│   │   └── batch-operations.sh
│   │
│   └── templates/
│       ├── executive-summary-template.md
│       ├── visualization-template.html
│       └── enterprise-styles.css
│
├── docs/
│   ├── README.md
│   │
│   ├── plans/
│   │   ├── 2025-11-24-competitive-analysis-template-and-cleanup.md
│   │   └── ...
│   │
│   ├── guides/
│   │   ├── SKILLS-USAGE-GUIDE.md
│   │   ├── WORKFLOW-PATTERNS.md
│   │   └── TROUBLESHOOTING.md
│   │
│   └── reference/
│       ├── PROJECT-INVENTORY.md
│       ├── ITERATION-HISTORY.md
│       └── SKILLS-USAGE-REPORT.md
│
└── templates/
    └── competitive-analysis/ (reusable template for next project)
        ├── README.md
        ├── 00-PROJECT-SETUP.md
        ├── 01-RESEARCH-PHASE.md
        ├── 02-ANALYSIS-PHASE.md
        ├── 03-DELIVERABLES-PHASE.md
        ├── 04-QA-PHASE.md
        └── 05-ITERATION-PHASE.md
```

---

## Migration Plan

### Phase 1: Create New Structure (No Moving Yet)

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch

# Create all directories
mkdir -p 00-PROJECT-MANAGEMENT
mkdir -p 01-RESEARCH-INPUTS/{competitor-data,market-research,pricing-data,feature-data}
mkdir -p 02-ANALYSIS-OUTPUTS/{competitive-matrices,swot-analyses,market-positioning,strategic-recommendations}
mkdir -p 03-DELIVERABLES/{current,v1.0,v0.9}/{DOCX,HTML,PDF}
mkdir -p 03-DELIVERABLES/current/{HTML/visualizations,PDF/visualizations}
mkdir -p 04-QA-DOCUMENTATION/{qa-reports,change-logs,verification}
mkdir -p 05-ITERATIONS/{iteration-1-initial-research,iteration-2-qa-corrections,iteration-3-tim-revisions}/{outputs}
mkdir -p 06-AUTOMATION/{scripts,templates}
mkdir -p docs/{plans,guides,reference}
```

### Phase 2: Copy Files to New Structure (Preserve Originals)

```bash
# Copy current deliverables
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/current-enterprise-cleaned-report-documents/*.docx 03-DELIVERABLES/current/DOCX/
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/current-enterprise-cleaned-report-documents/*.html 03-DELIVERABLES/current/HTML/
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/current-enterprise-cleaned-report-documents/*.pdf 03-DELIVERABLES/current/PDF/

# Copy visualizations
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/*.html 03-DELIVERABLES/current/HTML/visualizations/
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/*-ENTERPRISE.pdf 03-DELIVERABLES/current/PDF/visualizations/

# Copy QA documentation
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/current-enterprise-cleaned-report-documents/TIM-REVISIONS-*.md 05-ITERATIONS/iteration-3-tim-revisions/
cp 05-FINAL-DELIVERABLES/PROCESS-DOCS/QA-*.md 04-QA-DOCUMENTATION/qa-reports/

# Copy templates
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/enterprise-styles.css 06-AUTOMATION/templates/
```

### Phase 3: Create README Files

For each top-level directory, create README explaining contents:

```markdown
# [Directory Name]

**Purpose:** [What this directory contains]

**Contents:**
- [File/subdirectory 1]: [Description]
- [File/subdirectory 2]: [Description]

**When to Use:**
[Guidance on when/how to use this directory]

**Related Directories:**
- [Link to related directory]
```

### Phase 4: Update Documentation

Create VERSION-HISTORY.md tracking V1.0 → V2.0:

```markdown
# Version History

## V2.0 (November 24, 2025) - US-Primary Strategy

**Changes:**
- Strategic recommendations flipped to US-primary
- Positioning maps converted to four-quadrant format
- Marketing taglines removed
- Enterprise-themed PDFs generated

**Files Changed:** [List]

---

## V1.0 (November 2025) - QA Corrections

**Changes:**
- Added 100+ source citations
- Fixed pricing inconsistencies
- Enhanced disclaimers

**Files Changed:** [List]

---

## V0.9 (September-October 2025) - Initial Deliverables

**Initial creation of deliverables**
```

---

## Benefits of New Structure

**Clear Separation:**
- Inputs vs. Outputs clearly separated
- Research data separate from analysis
- Deliverables versioned and archived

**Iteration Tracking:**
- Each iteration documented in 05-ITERATIONS/
- Lessons learned captured
- Easy to review project history

**Automation-Ready:**
- Scripts in dedicated directory
- Templates accessible
- Reproducible workflows

**Maintenance:**
- Easy to find files
- Clear what's current vs. archived
- Documentation co-located with files

---

## Next Steps

1. Review this structure design
2. Get approval before migration
3. Create migration script (automated)
4. Test migration on copy first
5. Execute migration
6. Update all documentation paths
7. Archive old structure
```

**Step 2: Verify design document created**

```bash
grep "^## " docs/NEW-STRUCTURE-DESIGN.md | wc -l
# Expected: 5+ major sections
```

**Step 3: Commit**

```bash
git add docs/NEW-STRUCTURE-DESIGN.md
git commit -m "docs: design new project structure for clarity"
```

---

## PHASE 4: SKILL ENHANCEMENT

**Objective:** Update custom skills (competitive-analysis-quality-assurance and competitive-research-brightdata) based on lessons learned, and document usage of all skills utilized.

### Task 4.1: Update competitive-analysis-quality-assurance Skill

**Files:**
- Modify: `~/.claude/skills/competitive-analysis-quality-assurance.md`
- Create: `docs/guides/SKILL-UPDATES-competitive-analysis-qa.md`

**Step 1: Document skill enhancements needed**

Create `docs/guides/SKILL-UPDATES-competitive-analysis-qa.md`:

```markdown
# Skill Updates: competitive-analysis-quality-assurance

**Current Version:** [Check ~/.claude/skills/]
**Proposed Updates:** Based on Maia Learning project lessons

---

## Enhancements to Add

### 1. Consistency Verification Across Documents

**Current:** Skill checks individual documents

**Enhancement:** Add cross-document consistency check

**Implementation:**
```markdown
## Cross-Document Consistency Check

After reviewing individual documents, verify consistency:

### Strategic Recommendations Consistency:
- [ ] Priority order same in: Executive Summary, Full Report, Strategic Viz PDF
- [ ] Investment amounts match across all references
- [ ] Timeline dates consistent everywhere
- [ ] Wording of recommendations identical (not just similar)

### Data Consistency:
- [ ] Pricing data same across: Executive Summary, Full Report, All Visualizations
- [ ] Market share figures consistent everywhere
- [ ] Company descriptions identical across documents
- [ ] Funding amounts match all references

### Methodology:
1. Extract key data points from each document
2. Create comparison matrix
3. Flag any discrepancies
4. Report: "Found N inconsistencies across M documents"
```

---

### 2. Source Attribution Verification

**Current:** Skill checks for citations present

**Enhancement:** Verify citation completeness and format

**Implementation:**
```markdown
## Source Attribution Verification

### Required Citations:

**Pricing Claims:**
- Format: "($X/student, Company Website, YYYY)" or "($X-Y est., Industry Source, YYYY)"
- Check: All pricing mentions have source
- Flag: Any "$X" without citation

**Market Share Claims:**
- Format: "(X% market share, Publisher, YYYY)"
- Check: All market share percentages have source
- Flag: Any "X%" without citation

**Satisfaction Ratings:**
- Format: "(X.X/5, Review Site, YYYY)"
- Check: All ratings have source
- Flag: Any "X.X/5" without citation

**Funding Amounts:**
- Format: "($XM Series A, Crunchbase, YYYY)"
- Check: All funding mentions have source
- Flag: Any "$XM" without citation

### Citation Audit Process:
1. Search for all numeric claims (regex: \$\d+|\d+%|\d\.\d/5)
2. Check if followed by citation (regex: \([^)]+, \d{4}\))
3. Report: "X/Y claims properly cited (Z% coverage)"
```

---

### 3. Marketing Language Detection

**Current:** Not included in skill

**Enhancement:** Flag subjective/marketing language

**Implementation:**
```markdown
## Marketing Language Detection

### Red Flag Words:
- Superlatives: "best", "leading", "revolutionary", "game-changing", "cutting-edge"
- Absolute claims: "only", "first", "always", "never", "guaranteed"
- Hype words: "innovative" (without specifics), "world-class", "next-generation"
- Unverified claims: "rapidly growing", "industry leader" (without data)

### Process:
1. Scan all text for red flag words
2. For each instance, check if:
   - Backed by data/citation? (OK if cited)
   - Factual statement? (OK if verifiable)
   - Marketing opinion? (FLAG for revision)

3. Report:
   ```
   Found N instances of marketing language:
   - Line 42: "best platform" → SUGGEST: "highest-rated platform (4.7/5, G2, 2024)"
   - Line 89: "revolutionary AI" → SUGGEST: "AI features launched (Company, 2025)"
   ```

### Acceptable Exceptions:
- "leading" when supported by market share data
- "innovative" when describing specific new feature
- "only" when factually unique (and verified)
```

---

### 4. Version Comparison

**Current:** Not included in skill

**Enhancement:** Compare versions to track changes

**Implementation:**
```markdown
## Version Comparison (V1.0 vs V2.0)

When reviewing a new version:

### Automatic Checks:
1. File size changes (flag >20% increase/decrease)
2. Section additions/removals
3. Data changes (pricing, market share, ratings)
4. Structural changes (priority order, recommendations count)

### Diff Report Format:
```
## V1.0 → V2.0 Changes

### Structural:
- Recommendations: 7 → 6 (Priority 7 removed)
- Priority 1: Changed from "Close AI Gap" to "Attack US Market"

### Data:
- Investment total: $1.27M-2.35M → $1.77M-3.4M (+39% at midpoint)
- Naviance pricing: No changes
- Market positioning: Text chart → Four-quadrant visual chart

### Content:
- Added: "International Benefits Automatically" section (Executive Summary p.8)
- Removed: 3 marketing taglines (Market Positioning PDF)
- Modified: Strategic framing (US-primary vs international-primary)
```
```

---

## Updated Skill Checklist

Add these items to competitive-analysis-quality-assurance checklist:

```markdown
## Enhanced QA Checklist

### Consistency Verification:
- [ ] Strategic recommendations identical across Executive Summary, Full Report, Viz PDF
- [ ] Pricing data consistent across all documents
- [ ] Investment totals match everywhere
- [ ] Company descriptions consistent

### Source Attribution:
- [ ] All pricing claims cited
- [ ] All market share claims cited
- [ ] All satisfaction ratings cited
- [ ] All funding amounts cited
- [ ] Citation format consistent: "(Source, YYYY)"

### Language Quality:
- [ ] No marketing hyperbole without data
- [ ] No superlatives without verification
- [ ] Professional tone throughout
- [ ] Factual claims only

### Disclaimers Present:
- [ ] Estimated pricing marked "(est.)"
- [ ] Inferred ratings explained
- [ ] Market sizing context provided
- [ ] Data recency noted

### Version Tracking (if applicable):
- [ ] Version number updated
- [ ] Change log created
- [ ] Version comparison documented
- [ ] Backward compatibility checked
```

---

## Implementation Plan

To update the skill:

1. Locate skill file:
   ```bash
   cd ~/.claude/skills/
   ls -la competitive-analysis-quality-assurance.md
   ```

2. Back up current version:
   ```bash
   cp competitive-analysis-quality-assurance.md competitive-analysis-quality-assurance-backup-$(date +%Y%m%d).md
   ```

3. Add enhancements from this document

4. Test skill on Maia Learning deliverables (V2.0)

5. Verify improvements caught issues we manually found

6. Commit updated skill

---

## Testing Checklist

Test updated skill by running it on:

- [ ] Maia Learning V2.0 deliverables
- [ ] Should catch 100% consistency (already verified)
- [ ] Should verify all citations present (100% in V2.0)
- [ ] Should find zero marketing language (already cleaned)
- [ ] Should generate V1.0 vs V2.0 comparison report

If all tests pass, skill is ready for next competitive analysis project.
```

**Step 2: Verify skill update guide created**

```bash
grep "^### " docs/guides/SKILL-UPDATES-competitive-analysis-qa.md | wc -l
# Expected: 4+ enhancement sections
```

**Step 3: Commit**

```bash
git add docs/guides/SKILL-UPDATES-competitive-analysis-qa.md
git commit -m "docs: create skill enhancement guide for competitive-analysis-qa"
```

---

### Task 4.2: Create Skills Usage Guide

**Files:**
- Create: `docs/guides/SKILLS-USAGE-GUIDE.md`

**Step 1: Create comprehensive skills guide**

Create `docs/guides/SKILLS-USAGE-GUIDE.md`:

```markdown
# Skills Usage Guide - Competitive Analysis Projects

**Purpose:** How to use Claude skills effectively for competitive analysis

**Audience:** Anyone conducting competitive analysis using Claude

---

## Overview

Competitive analysis projects benefit from systematic use of Claude skills. This guide documents which skills to use, when, and how based on the Maia Learning project.

---

## Skill Categories

### Custom Skills (Domain-Specific):
1. **competitive-research-brightdata** - Data gathering
2. **competitive-analysis-quality-assurance** - Quality verification

### Superpowers Skills (Process/Workflow):
3. **superpowers:brainstorming** - Requirements refinement
4. **superpowers:writing-plans** - Implementation planning
5. **superpowers:executing-plans** - Systematic execution
6. **superpowers:verification-before-completion** - Quality gates
7. **superpowers:using-git-worktrees** - Work isolation
8. **superpowers:test-driven-development** - Testing automation

---

## Workflow: When to Use Each Skill

### Phase 1: Project Setup

**Skill:** @superpowers:brainstorming

**When:** At project start, before research begins

**Purpose:** Refine requirements, scope, deliverables

**How to Use:**
```
User: "I need to do competitive analysis for [Company]"

Claude: "I'm using the brainstorming skill to refine your requirements"

[Skill asks questions like:]
- Who are the primary competitors?
- What's the purpose of this analysis?
- What deliverables do you need?
- What's the timeline?
- Who's the audience?
```

**Output:** Clear project scope, competitor list, deliverables checklist

---

### Phase 2: Research

**Skill:** @competitive-research-brightdata

**When:** After scope is defined, before analysis begins

**Purpose:** Gather competitor data systematically

**How to Use:**
```
1. Prepare competitor list (5-7 companies)
2. Define research questions (pricing, features, positioning, etc.)
3. Invoke skill:

   Skill: competitive-research-brightdata

   Provide:
   - Competitor names
   - Research questions
   - Output format (JSON/CSV/Markdown)
```

**Output:** Structured competitor data (pricing, features, reviews, funding)

**Next Step:** Organize outputs in 01-RESEARCH-INPUTS/ directory

---

### Phase 3: Analysis (Manual)

**Skills:** None (manual analysis phase)

**Tasks:**
- Create competitive matrices (feature comparison, pricing comparison)
- Perform SWOT analyses
- Develop market positioning
- Draft strategic recommendations

**Output:** Analysis documents in 02-ANALYSIS-OUTPUTS/

---

### Phase 4: Deliverables Creation (Manual)

**Skills:** None initially (manual writing phase)

**Tasks:**
- Write Executive Summary
- Write Full Report
- Create Visualizations (HTML/charts)

**Output:** Draft deliverables

---

### Phase 5: Quality Assurance

**Skill:** @competitive-analysis-quality-assurance

**When:** After deliverables drafted, before client delivery

**Purpose:** Systematic quality verification

**How to Use:**
```
1. Ensure all deliverables are complete
2. Invoke skill:

   Skill: competitive-analysis-quality-assurance

   Provide:
   - Deliverable files (DOCX, HTML, PDF)
   - Source materials for fact-checking
```

**Output:** QA report with findings (missing citations, pricing errors, inconsistencies)

**Next Step:** Fix all issues identified, then re-run skill to verify

---

### Phase 6: Client Feedback / Iterations

**Skill:** @superpowers:brainstorming (before changes)

**When:** Receiving client feedback (like Tim's revisions)

**Purpose:** Clarify requirements before implementing changes

**How to Use:**
```
User: "[Client] wants changes: [rough notes]"

Claude: "I'm using the brainstorming skill to clarify requirements"

[Skill asks clarifying questions]
```

**Output:** Clear change specifications

---

**Skill:** @superpowers:writing-plans (after brainstorming)

**When:** After requirements clarified, before implementation

**Purpose:** Create systematic implementation plan

**How to Use:**
```
User: "Create a plan for these changes"

Claude: "I'm using the writing-plans skill to create implementation plan"

[Skill creates detailed task-by-task plan]
```

**Output:** Implementation plan saved to docs/plans/[date]-[feature].md

---

**Skill:** @superpowers:executing-plans (implementation)

**When:** After plan created, ready to implement

**Purpose:** Execute plan systematically with checkpoints

**How to Use:**
```
[Open new session or use current]

User: "/superpowers:execute-plan [plan-file]"

[Skill executes plan task-by-task, pausing for review between batches]
```

**Output:** Changes implemented systematically, reviewed, committed

---

**Skill:** @superpowers:verification-before-completion

**When:** Before marking iteration complete

**Purpose:** Verify all changes implemented correctly

**How to Use:**
```
[After implementing changes]

Claude: "Using verification skill before marking complete"

[Skill checks:]
- All tasks from plan completed?
- All files modified as specified?
- Tests pass? (if applicable)
- Documentation updated?
```

**Output:** Verification checklist, confidence in completion

---

## Advanced Workflows

### Workflow 1: Major Iteration (like V2.0)

```
1. @superpowers:brainstorming
   → Clarify client feedback
   → Ask 6-8 questions
   → Get clear requirements

2. @superpowers:writing-plans
   → Create detailed implementation plan
   → Bite-sized tasks (2-5 min each)
   → Save to docs/plans/

3. @superpowers:using-git-worktrees (optional but recommended)
   → Create isolated worktree for V2.0 work
   → Keep V1.0 accessible
   → Safer for major changes

4. @superpowers:executing-plans
   → Execute plan task-by-task
   → Review between batches
   → Commit frequently

5. @competitive-analysis-quality-assurance
   → Run QA on updated deliverables
   → Verify 100% consistency
   → Check all changes applied

6. @superpowers:verification-before-completion
   → Final verification
   → Evidence of completion
   → Mark iteration complete
```

---

### Workflow 2: Quick Updates

```
1. Make changes directly (no brainstorming needed if clear)

2. @competitive-analysis-quality-assurance
   → Quick QA check
   → Ensure consistency

3. @superpowers:verification-before-completion
   → Verify changes correct
   → Commit
```

---

## Skill Invocation Syntax

### Launching a Skill:

```
Skill: skill-name
```

Example:
```
Skill: competitive-research-brightdata
```

### Using Slash Commands (Superpowers):

```
/superpowers:skill-name
```

Example:
```
/superpowers:brainstorm
/superpowers:write-plan
/superpowers:execute-plan docs/plans/2025-11-24-feature.md
```

---

## Common Mistakes

### Mistake 1: Skipping Brainstorming

**Problem:** Implementing changes without clarifying requirements

**Example:** Tim says "change strategy" but doesn't specify exactly how

**Solution:** ALWAYS use @superpowers:brainstorming first to ask questions

**Result:** Zero rework (Maia Learning V2.0 had perfect alignment)

---

### Mistake 2: Not Using QA Skill

**Problem:** Manually checking quality, missing consistency issues

**Example:** Naviance pricing $6-8 in one file, $8-12 in another

**Solution:** Run @competitive-analysis-quality-assurance on ALL deliverables

**Result:** Caught all consistency issues before client delivery

---

### Mistake 3: Skipping Verification

**Problem:** Claiming "done" without checking

**Example:** Saying "PDFs generated" but not verifying file sizes/content

**Solution:** Use @superpowers:verification-before-completion always

**Result:** 100% confidence in deliverable quality

---

## Skill Combinations (Power Patterns)

### Pattern 1: Research + QA Loop

```
@competitive-research-brightdata (gather data)
    ↓
[Manual analysis]
    ↓
[Create deliverables]
    ↓
@competitive-analysis-quality-assurance (verify quality)
    ↓
[Fix issues found]
    ↓
@competitive-analysis-quality-assurance (verify fixes)
    ↓
@superpowers:verification-before-completion (final check)
```

**Use For:** Initial deliverables creation (V1.0)

---

### Pattern 2: Feedback + Implementation Loop

```
@superpowers:brainstorming (clarify feedback)
    ↓
@superpowers:writing-plans (plan implementation)
    ↓
@superpowers:executing-plans (implement systematically)
    ↓
@competitive-analysis-quality-assurance (verify changes)
    ↓
@superpowers:verification-before-completion (final check)
```

**Use For:** Client revisions (like Tim's V2.0 feedback)

---

## Next Steps

**When starting new competitive analysis:**
1. Review this guide
2. Use skills in order recommended
3. Document any new patterns discovered
4. Update this guide with lessons learned

**When encountering issues:**
1. Check "Common Mistakes" section
2. Verify skill workflow followed
3. Add new troubleshooting to guide
```

**Step 2: Verify skills guide created**

```bash
wc -l docs/guides/SKILLS-USAGE-GUIDE.md
# Expected: 300+ lines (comprehensive guide)
```

**Step 3: Commit**

```bash
git add docs/guides/SKILLS-USAGE-GUIDE.md
git commit -m "docs: create comprehensive skills usage guide"
```

---

## PHASE 5: PROCESS DOCUMENTATION

**Objective:** Lock down the complete workflow for next competitive analysis project.

### Task 5.1: Create Master Workflow Document

**Files:**
- Create: `docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`

**Step 1: Document end-to-end workflow**

Create `docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`:

```markdown
# Competitive Analysis Workflow - Complete Process

**Purpose:** Step-by-step workflow for conducting enterprise-grade competitive analysis

**Target Quality:** 9.5/10 (client-ready)

**Duration:** 6-10 weeks

---

## Workflow Overview

```
Week 1-2: Setup & Research
    ↓
Week 3-4: Analysis
    ↓
Week 5-6: Deliverables Creation
    ↓
Week 7: QA & Refinement
    ↓
Week 8-10: Client Feedback & Iterations
```

---

## WEEK 1: Project Setup

### Day 1: Brainstorm & Scope

**Skill:** @superpowers:brainstorming

**Tasks:**
1. Clarify project requirements
2. Identify competitors (5-7 primary)
3. Define deliverables needed
4. Set timeline and milestones
5. Identify stakeholders

**Outputs:**
- Project scope document
- Competitor list
- Deliverables checklist
- Timeline

---

### Day 2: Setup Project Structure

**Tasks:**
1. Create directory structure (use template)
2. Initialize git repository
3. Create README files for each directory
4. Set up sources.md file

**Commands:**
```bash
# Copy template
cp -r templates/competitive-analysis /path/to/new-project/
cd /path/to/new-project

# Initialize git
git init
git add .
git commit -m "feat: initialize competitive analysis project"

# Create branch for research phase
git checkout -b research-phase
```

**Outputs:**
- Organized directory structure
- Git repo initialized
- Ready for research

---

### Day 3-5: Initial Research Planning

**Tasks:**
1. Create research questions (20 per competitor)
2. Identify data sources (websites, review sites, funding databases)
3. Set up research tracker spreadsheet
4. Prepare for skill invocation

**Outputs:**
- Research questions document
- Data sources list
- Research tracker ready

---

## WEEK 2-3: Research Phase

### Automated Research

**Skill:** @competitive-research-brightdata

**Tasks:**
1. Invoke skill with competitor list and research questions
2. Receive structured data (JSON/CSV)
3. Organize outputs in 01-RESEARCH-INPUTS/ directory
4. Document sources in sources.md

**Commands:**
```bash
# Organize skill outputs
mkdir -p 01-RESEARCH-INPUTS/competitor-data/
mv competitor-*.json 01-RESEARCH-INPUTS/competitor-data/

# Track completion
# Update research-tracker.csv as data comes in
```

**Outputs:**
- Competitor data files (JSON)
- Sources documented
- 70-80% of research questions answered

---

### Manual Research

**Tasks:**
1. Review sites (G2, Capterra, TrustRadius)
2. Funding databases (Crunchbase, PitchBook)
3. Company websites (pricing, features, positioning)
4. Industry reports (market sizing, growth trends)

**Outputs:**
- Review ratings documented
- Funding data collected
- Pricing screenshots saved
- Market research gathered

---

### Research Completion Check

**Before proceeding to analysis:**

- [ ] All 5-7 competitors researched
- [ ] 80%+ of research questions answered
- [ ] All sources documented in sources.md
- [ ] Research tracker shows complete status
- [ ] Gaps documented (some data unavailable is OK)

---

## WEEK 4-5: Analysis Phase

### Competitive Matrices

**Tasks:**
1. Create feature comparison matrix (50+ features)
2. Create pricing comparison table
3. Create market positioning comparison

**Outputs:**
- `02-ANALYSIS-OUTPUTS/competitive-matrices/feature-comparison.csv`
- `02-ANALYSIS-OUTPUTS/competitive-matrices/pricing-comparison.csv`
- `02-ANALYSIS-OUTPUTS/competitive-matrices/positioning-comparison.csv`

---

### SWOT Analyses

**Tasks:**
1. SWOT for each primary competitor (5-7 total)
2. SWOT for client company
3. Identify competitive threats and opportunities

**Outputs:**
- `02-ANALYSIS-OUTPUTS/swot-analyses/[competitor]-swot.md` (×7)
- `02-ANALYSIS-OUTPUTS/swot-analyses/client-swot.md`

---

### Market Positioning

**Tasks:**
1. Create positioning map (Innovation × Market Coverage)
2. Identify strategic groups
3. Analyze competitive landscape

**Outputs:**
- `02-ANALYSIS-OUTPUTS/market-positioning/positioning-map.md`
- `02-ANALYSIS-OUTPUTS/market-positioning/strategic-groups.md`
- `02-ANALYSIS-OUTPUTS/market-positioning/competitive-landscape.md`

---

### Strategic Recommendations

**Tasks:**
1. Identify 5-7 strategic recommendations
2. Estimate investment for each ($X-Y)
3. Create implementation timeline (Q1-Q4 20XX)
4. Prioritize (CRITICAL / HIGH / MEDIUM)

**Outputs:**
- `02-ANALYSIS-OUTPUTS/strategic-recommendations/recommendations.md`
- `02-ANALYSIS-OUTPUTS/strategic-recommendations/investment-estimates.md`
- `02-ANALYSIS-OUTPUTS/strategic-recommendations/implementation-roadmap.md`

---

## WEEK 6: Deliverables Creation

### Executive Summary

**Template:** `templates/competitive-analysis/deliverables-templates/executive-summary-template.md`

**Tasks:**
1. Copy template
2. Fill in all sections:
   - Executive Overview
   - Competitive Landscape
   - Key Findings (5-7)
   - Strategic Recommendations (5-7)
   - Implementation Timeline
   - Sources & References (15-20)

**Length:** 15-20 pages

**Output:** `03-DELIVERABLES/current/DOCX/executive-summary.docx`

---

### Full Report

**Template:** `templates/competitive-analysis/deliverables-templates/full-report-template.md`

**Tasks:**
1. Copy template
2. Fill in all sections:
   - PART I: Executive Overview
   - PART II: Market Landscape
   - PART III: Competitor Profiles (7 detailed profiles)
   - PART IV: Strategic Analysis (SWOT, Positioning, Threats)
   - PART V: Strategic Implications (Recommendations)
   - PART VI: Appendices (Matrices, Pricing, Tech Stack)

**Length:** 50-70 pages

**Output:** `03-DELIVERABLES/current/DOCX/full-report.docx`

---

### Visualizations (10 PDFs)

**Template:** `templates/competitive-analysis/deliverables-templates/visualization-template.html`

**Tasks:**
1. Create 10 HTML visualizations:
   - Competitive Positioning Analysis
   - Market Trends Analysis
   - SWOT Analysis - Top Competitors
   - Strategic Recommendations
   - Threats & Opportunities
   - Feature Comparison Matrix
   - Pricing Analysis
   - Technology Stack Comparison
   - Market Positioning Map
   - Target Segments Analysis

2. Generate PDFs from HTML:
```bash
cd 03-DELIVERABLES/current/HTML/visualizations/
bash /path/to/automation/generate-pdfs.sh
# Creates all PDFs in 03-DELIVERABLES/current/PDF/visualizations/
```

**Output:** 10 enterprise-themed PDF visualizations

---

## WEEK 7: QA & Refinement

### QA Pass 1: Initial Review

**Skill:** @competitive-analysis-quality-assurance

**Tasks:**
1. Run skill on all deliverables
2. Review QA report findings
3. Create fix list

**Expected Findings:**
- Missing source citations (20-40 instances)
- Pricing inconsistencies (2-5 instances)
- Disclaimer gaps (3-5 instances)
- Formatting issues (10-15 instances)

**Output:** QA report saved to `04-QA-DOCUMENTATION/qa-reports/v1.0-qa-report.md`

---

### Fix Issues

**Tasks:**
1. Add all missing source citations
2. Fix pricing inconsistencies
3. Add disclaimers (est. pricing, inferred ratings)
4. Fix formatting issues
5. Verify consistency across all documents

**Duration:** 2-3 days

**Output:** Updated deliverables (V1.0)

---

### QA Pass 2: Verification

**Skill:** @competitive-analysis-quality-assurance

**Tasks:**
1. Re-run skill on updated deliverables
2. Verify all issues fixed
3. Check for new issues

**Expected:** 0 critical issues, quality 9.5/10

**Skill:** @superpowers:verification-before-completion

**Tasks:**
1. Final verification before marking V1.0 complete
2. Check all deliverables present
3. Verify file sizes reasonable
4. Confirm quality metrics met

**Output:** V1.0 deliverables COMPLETE and client-ready

---

## WEEK 8-10: Client Feedback & Iterations

### Receive Client Feedback

**Example:** Client reviews deliverables and requests changes (like Tim's revisions)

**Skill:** @superpowers:brainstorming

**Tasks:**
1. Review client feedback
2. Ask clarifying questions (6-8 questions)
3. Document clear requirements

**Output:** Clear change specifications

---

### Plan Implementation

**Skill:** @superpowers:writing-plans

**Tasks:**
1. Create detailed implementation plan
2. Break into bite-sized tasks
3. Save to `docs/plans/[date]-[iteration-name].md`

**Output:** Implementation plan ready for execution

---

### Execute Changes

**Skill:** @superpowers:executing-plans

**Tasks:**
1. Execute plan task-by-task
2. Review between batches
3. Commit frequently

**Output:** Changes implemented systematically

---

### Verify Changes

**Skill:** @competitive-analysis-quality-assurance

**Tasks:**
1. Run QA on updated deliverables
2. Verify 100% consistency across documents
3. Check all client requests addressed

**Skill:** @superpowers:verification-before-completion

**Tasks:**
1. Final verification
2. Confirm all changes correct
3. Mark iteration complete

**Output:** V2.0 deliverables COMPLETE

---

## Deliverables Checklist (Final)

Before client delivery, ensure all present:

### Primary Reports:
- [ ] Executive Summary (DOCX + PDF) - 15-20 pages
- [ ] Full Report (DOCX + PDF) - 50-70 pages

### Visualizations:
- [ ] 10 Enterprise PDF visualizations

### Documentation:
- [ ] Sources & References (15-20 sources)
- [ ] QA Reports (all iterations)
- [ ] Version History
- [ ] README with usage instructions

---

## Quality Metrics (Final Check)

- [ ] **Source Citations:** 100% of claims cited
- [ ] **Pricing Accuracy:** All verified or marked "(est.)"
- [ ] **Consistency:** 100% across all documents
- [ ] **Professional Presentation:** No marketing language
- [ ] **Completeness:** All deliverables checklist items present
- [ ] **Quality Score:** 9.5/10 or higher

---

## Common Workflows by Scenario

### Scenario 1: New Competitive Analysis (From Scratch)

```
Follow complete workflow Week 1-10
```

---

### Scenario 2: Quick Competitive Update (Existing Analysis)

```
Week 1: Update research (new funding, pricing changes)
    ↓
Week 2: Update analysis (revised positioning, new threats)
    ↓
Week 3: Update deliverables (Executive Summary priority)
    ↓
Week 4: QA and delivery
```

**Duration:** 4 weeks (vs. 10 weeks for new)

---

### Scenario 3: Strategic Pivot (Like V2.0)

```
Day 1: @superpowers:brainstorming (clarify new strategy)
    ↓
Day 2: @superpowers:writing-plans (plan changes)
    ↓
Day 3-4: @superpowers:executing-plans (implement)
    ↓
Day 5: @competitive-analysis-quality-assurance (verify)
    ↓
Day 5: @superpowers:verification-before-completion (final check)
```

**Duration:** 1 week

---

## Automation Scripts Available

Located in: `06-AUTOMATION/scripts/`

### generate-pdfs.sh

**Purpose:** Generate all PDFs from HTML visualizations

**Usage:**
```bash
cd 03-DELIVERABLES/current/HTML/visualizations/
bash /path/to/06-AUTOMATION/scripts/generate-pdfs.sh
```

**Output:** All PDFs in `03-DELIVERABLES/current/PDF/visualizations/`

---

### docx-to-html.py

**Purpose:** Convert DOCX to styled HTML with enterprise theme

**Usage:**
```bash
python /path/to/06-AUTOMATION/scripts/docx-to-html.py \
  executive-summary.docx \
  executive-summary.html
```

**Output:** Styled HTML ready for PDF generation

---

### qa-consistency-check.py

**Purpose:** Automated consistency checks across documents

**Usage:**
```bash
python /path/to/06-AUTOMATION/scripts/qa-consistency-check.py \
  03-DELIVERABLES/current/
```

**Output:** Consistency report (pricing, investments, dates, etc.)

---

## Next Competitive Analysis

**To start new project using this workflow:**

1. Copy template:
   ```bash
   cp -r templates/competitive-analysis /path/to/new-analysis/
   cd /path/to/new-analysis
   ```

2. Follow workflow Week 1-10

3. Use skills at each phase (documented in SKILLS-USAGE-GUIDE.md)

4. Track progress in project STATUS.md

5. Document lessons learned for next iteration

---

**Workflow Last Updated:** November 24, 2025 (based on Maia Learning project)
```

**Step 2: Verify workflow document created**

```bash
grep "^## " docs/COMPETITIVE-ANALYSIS-WORKFLOW.md | wc -l
# Expected: 15+ major sections
```

**Step 3: Commit**

```bash
git add docs/COMPETITIVE-ANALYSIS-WORKFLOW.md
git commit -m "docs: create master workflow for competitive analysis projects"
```

---

## PHASE 6: ITERATION FRAMEWORK

**Objective:** Create system for quick edits/additions to current project going forward.

### Task 6.1: Create Quick Iteration Guide

**Files:**
- Create: `docs/guides/QUICK-ITERATIONS-GUIDE.md`

**Step 1: Document quick iteration process**

Create `docs/guides/QUICK-ITERATIONS-GUIDE.md`:

```markdown
# Quick Iterations Guide

**Purpose:** How to make quick updates to existing deliverables without full workflow

**Use For:**
- Minor data updates (pricing changes, new funding rounds)
- Small content additions (new competitor emerges)
- Formatting fixes
- Quick client requests

---

## When to Use Quick Iterations vs Full Workflow

### Use Quick Iterations For:
- ✅ Update single data point (e.g., competitor raised Series B)
- ✅ Fix typo or formatting issue
- ✅ Add missing source citation
- ✅ Small content addition (1-2 paragraphs)
- ✅ Regenerate PDFs after HTML fix

### Use Full Workflow For:
- ❌ Major strategic changes (like V2.0 flip)
- ❌ Adding new competitor to analysis
- ❌ Restructuring recommendations
- ❌ Significant content rewrite

---

## Quick Iteration Process

### Step 1: Identify Change Needed

**Example Changes:**
- "Update SCOIR pricing from $4.80 to $5.00"
- "Add SchooLinks Series C funding ($100M, Oct 2025)"
- "Fix typo in Executive Summary page 12"
- "Add new source citation for Naviance market share"

---

### Step 2: Locate All Files Affected

**Use grep to find all references:**

```bash
cd /path/to/project/

# Find all files mentioning specific data
grep -r "4.80" 03-DELIVERABLES/current/

# Expected output shows all files with that data
# Example:
# 03-DELIVERABLES/current/DOCX/executive-summary.docx
# 03-DELIVERABLES/current/HTML/pricing-analysis.html
# 03-DELIVERABLES/current/PDF/pricing-analysis.pdf
```

**Create change checklist:**
```
Files to update:
- [ ] executive-summary.docx
- [ ] full-report.docx
- [ ] pricing-analysis.html
- [ ] competitive-positioning.html
- [ ] (PDFs will regenerate from HTML)
```

---

### Step 3: Make Changes to Source Files

**Priority: Update DOCX and HTML sources (not PDFs)**

### DOCX Files:

```bash
# For DOCX, convert to markdown first
cd 03-DELIVERABLES/current/DOCX/
pandoc executive-summary.docx -o executive-summary-temp.md

# Edit markdown
# Change: $4.80 → $5.00
# Update date: (SCOIR, 2024) → (SCOIR, 2025)

# Convert back to DOCX
pandoc executive-summary-temp.md -o executive-summary.docx

# Verify change
grep "$5.00" executive-summary-temp.md
# Should show: "$5.00 (SCOIR, 2025)"
```

### HTML Files:

```bash
# For HTML, edit directly
cd 03-DELIVERABLES/current/HTML/visualizations/

# Edit pricing-analysis.html
# Find: <td>$4.80</td>
# Replace: <td>$5.00</td>

# Verify change
grep "$5.00" pricing-analysis.html
# Should show updated value
```

---

### Step 4: Regenerate PDFs

**Use automation script:**

```bash
cd /path/to/project/

# Regenerate individual PDFs from updated HTML
cd 03-DELIVERABLES/current/HTML/visualizations/
bash /path/to/06-AUTOMATION/scripts/generate-pdfs.sh pricing-analysis.html

# Or regenerate DOCX to PDF
cd 03-DELIVERABLES/current/DOCX/
python /path/to/06-AUTOMATION/scripts/docx-to-html.py executive-summary.docx executive-summary.html
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --print-to-pdf="../PDF/executive-summary.pdf" "file://$(pwd)/executive-summary.html"
```

**Verify PDFs:**
```bash
ls -lh 03-DELIVERABLES/current/PDF/
# Check file sizes updated (timestamp should be recent)
```

---

### Step 5: Quick Consistency Check

**Use automation script:**

```bash
python /path/to/06-AUTOMATION/scripts/qa-consistency-check.py \
  03-DELIVERABLES/current/ \
  --check "SCOIR pricing" \
  --expected "$5.00"

# Output: "✅ SCOIR pricing consistent across 5 files: $5.00"
```

**Manual check (if no script):**
```bash
grep -r "$5.00" 03-DELIVERABLES/current/ | grep -i scoir
# Verify all references updated
```

---

### Step 6: Document Change

**Update version history:**

Add to `03-DELIVERABLES/VERSION-HISTORY.md`:

```markdown
## V2.1 (November 30, 2025) - Minor Update

**Changes:**
- Updated SCOIR pricing: $4.80 → $5.00 (SCOIR website, Nov 2025)

**Files Changed:**
- executive-summary.docx, executive-summary.pdf
- full-report.docx, full-report.pdf
- pricing-analysis.html, pricing-analysis.pdf
- competitive-positioning.html, competitive-positioning.pdf

**Duration:** 30 minutes
```

---

### Step 7: Commit Changes

```bash
git add 03-DELIVERABLES/current/
git add 03-DELIVERABLES/VERSION-HISTORY.md
git commit -m "update: SCOIR pricing $4.80 → $5.00 (v2.1)"
```

---

## Quick Iteration Templates

### Template 1: Update Single Data Point

```bash
# 1. Find all references
grep -r "[old value]" 03-DELIVERABLES/current/

# 2. Update source files (DOCX + HTML)
# [Edit files]

# 3. Regenerate PDFs
bash /path/to/06-AUTOMATION/scripts/generate-pdfs.sh [files]

# 4. Verify consistency
grep -r "[new value]" 03-DELIVERABLES/current/ | wc -l
# Expected: N files (same as old value count)

# 5. Document in VERSION-HISTORY.md

# 6. Commit
git commit -m "update: [description] (v2.X)"
```

**Duration:** 15-30 minutes

---

### Template 2: Add Missing Citation

```bash
# 1. Locate claim needing citation
grep -r "[uncited claim]" 03-DELIVERABLES/current/

# 2. Add citation in source files
# Before: "40% market share"
# After: "40% market share (PowerSchool, 2024)"

# 3. Regenerate PDFs

# 4. Verify citation added
grep "(PowerSchool, 2024)" 03-DELIVERABLES/current/DOCX/executive-summary-temp.md

# 5. Document + commit
git commit -m "docs: add citation for market share claim (v2.X)"
```

**Duration:** 10-15 minutes

---

### Template 3: Fix Formatting Issue

```bash
# 1. Identify formatting problem
# Example: Table alignment off in PDF

# 2. Fix in HTML source
# Adjust CSS or table structure

# 3. Regenerate PDF only
bash /path/to/06-AUTOMATION/scripts/generate-pdfs.sh [file].html

# 4. Verify formatting fixed (open PDF)

# 5. Document + commit
git commit -m "fix: table alignment in [file] (v2.X)"
```

**Duration:** 10-20 minutes

---

## Automation Scripts for Quick Iterations

### generate-single-pdf.sh

**Purpose:** Regenerate one PDF without regenerating all

**Usage:**
```bash
bash /path/to/06-AUTOMATION/scripts/generate-single-pdf.sh \
  03-DELIVERABLES/current/HTML/visualizations/pricing-analysis.html \
  03-DELIVERABLES/current/PDF/visualizations/pricing-analysis.pdf
```

---

### bulk-replace.py

**Purpose:** Replace text across all source files

**Usage:**
```bash
python /path/to/06-AUTOMATION/scripts/bulk-replace.py \
  --find "$4.80" \
  --replace "$5.00" \
  --files "03-DELIVERABLES/current/**/*.{md,html}" \
  --dry-run  # Preview changes first

# After verifying preview:
python /path/to/06-AUTOMATION/scripts/bulk-replace.py \
  --find "$4.80" \
  --replace "$5.00" \
  --files "03-DELIVERABLES/current/**/*.{md,html}"
```

---

### verify-consistency.py

**Purpose:** Check that change applied everywhere

**Usage:**
```bash
python /path/to/06-AUTOMATION/scripts/verify-consistency.py \
  --search "SCOIR pricing" \
  --expected "$5.00" \
  --path 03-DELIVERABLES/current/

# Output:
# ✅ Found "SCOIR pricing: $5.00" in 5 files
# ✅ No inconsistencies found
```

---

## When Quick Iteration Becomes Full Iteration

**Signs you need full workflow:**

- Change affects 5+ files
- Requires strategic thinking (not just data update)
- Client requests major revision
- Change takes >2 hours
- Requires new research or analysis

**Action:** Switch to full iteration workflow:
1. @superpowers:brainstorming (clarify requirements)
2. @superpowers:writing-plans (plan changes)
3. @superpowers:executing-plans (implement systematically)
4. @competitive-analysis-quality-assurance (verify)

---

## Quick Iteration Checklist

Before committing quick iteration:

- [ ] All source files updated (DOCX + HTML)
- [ ] PDFs regenerated from sources
- [ ] Consistency verified (same data everywhere)
- [ ] VERSION-HISTORY.md updated
- [ ] Commit message descriptive
- [ ] Version bumped (v2.0 → v2.1)

---

## Common Quick Iterations

### Update Competitor Funding

```bash
# Add: "SchooLinks raised $100M Series C (Nov 2025)"
# Files: executive-summary, full-report, swot-analysis, threats-opportunities
# Duration: 20 minutes
```

### Update Review Ratings

```bash
# Change: "SCOIR 4.5/5 → 4.6/5 (G2, 2025)"
# Files: competitive-positioning, swot-analysis
# Duration: 15 minutes
```

### Add New Feature to Comparison

```bash
# Add: "Direct Admissions Support" to feature matrix
# Files: feature-comparison-matrix, full-report Appendix
# Duration: 30 minutes
```

---

**Next Steps:**

For any update to current deliverables:
1. Assess: Quick iteration or full workflow?
2. If quick: Use templates above
3. If full: Use COMPETITIVE-ANALYSIS-WORKFLOW.md
4. Always document in VERSION-HISTORY.md
5. Always verify consistency before committing
```

**Step 2: Verify quick iterations guide created**

```bash
grep "^### Template" docs/guides/QUICK-ITERATIONS-GUIDE.md | wc -l
# Expected: 3+ iteration templates
```

**Step 3: Commit**

```bash
git add docs/guides/QUICK-ITERATIONS-GUIDE.md
git commit -m "docs: create quick iterations guide for minor updates"
```

---

## EXECUTION OPTIONS

Plan complete and saved to `docs/plans/2025-11-24-competitive-analysis-template-and-cleanup.md`.

**Two execution options:**

**1. Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration
   - Use @superpowers:subagent-driven-development
   - Stay in this session
   - Fresh subagent per task + code review

**2. Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints
   - Open new session in project directory
   - Use @superpowers:executing-plans
   - Systematic batch execution

**Which approach would you prefer?**
