# Competitive Analysis Workflow

**Purpose:** Step-by-step workflow for enterprise-grade competitive analysis
**Target Quality:** 9.5/10 (client-ready)
**Based On:** Maia Learning competitive analysis project (November 2025)

---

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COMPETITIVE ANALYSIS WORKFLOW                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
│  │  1. SETUP &     │    │  2. ANALYSIS    │    │  3. DELIVERABLES │        │
│  │     RESEARCH    │───▶│                 │───▶│     CREATION     │        │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘         │
│         │                      │                      │                     │
│         │                      │                      │                     │
│         ▼                      ▼                      ▼                     │
│  • Brainstorm scope     • Competitive matrices  • Executive summary        │
│  • Research competitors • SWOT analyses         • Full report              │
│  • Gather data          • Positioning maps      • 10 visualizations        │
│                         • Recommendations                                   │
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐                                │
│  │  4. QA &        │    │  5. CLIENT      │                                │
│  │     REFINEMENT  │───▶│     FEEDBACK &  │──┐                             │
│  └─────────────────┘    │     ITERATIONS  │  │                             │
│         │               └─────────────────┘  │                             │
│         │                      │             │                             │
│         ▼                      ▼             │                             │
│  • QA Pass 1            • Receive feedback   │                             │
│  • Fix issues           • Brainstorm changes │                             │
│  • QA Pass 2            • Plan → Execute     │                             │
│  • Final verification   • Verify & deliver   │                             │
│                                │              │                             │
│                                └──────────────┘                             │
│                                (iterate as needed)                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase Summary

| Phase | Key Output | Skills Used |
|-------|------------|-------------|
| 1. Setup & Research | Competitor data, sources | `superpowers:brainstorming`, `competitive-research-brightdata` |
| 2. Analysis | Matrices, SWOTs, positioning | Manual analysis |
| 3. Deliverables | Exec summary, report, 10 PDFs | Manual + automation |
| 4. QA & Refinement | 9.5/10 quality score | `competitive-analysis-quality-assurance` |
| 5. Iterations | Client-approved deliverables | All skills as needed |

---

## Phase 1: Setup & Research

### 1.1 Brainstorm & Scope

**Skill:** `superpowers:brainstorming`

Use brainstorming to clarify:
- **Project Objectives:** What decisions will this analysis inform?
- **Competitor List:** Which companies to analyze (typically 5-8)
- **Key Questions:** What specific questions must be answered?
- **Deliverables:** What format does the client need?
- **Timeline:** When are deliverables due?
- **Audience:** Who will read this (executives, sales, product)?

**Output:** Project scope document with clear requirements

---

### 1.2 Setup Project Structure

**Actions:**
1. Copy template from `templates/competitive-analysis/`
2. Initialize git repository (if not already)
3. Create feature branch for this analysis
4. Set up directory structure per template

**Directory Structure:**
```
ProjectName/
├── 00-PROJECT-MANAGEMENT/
├── 01-RESEARCH-INPUTS/
├── 02-ANALYSIS-OUTPUTS/
├── 03-DELIVERABLES/
├── 04-QA-DOCUMENTATION/
├── 05-ITERATIONS/
├── 06-AUTOMATION/
└── docs/
```

---

### 1.3 Research Planning

**Create Research Plan:**
- List all competitors to research
- Define 20-24 research questions per competitor (see template)
- Identify data sources (company sites, G2, Crunchbase, etc.)
- Set up research tracker

**Outputs Expected:**
- [ ] Project scope document
- [ ] Competitor list (5-8 companies)
- [ ] Deliverables checklist
- [ ] Research question template filled out
- [ ] Data sources identified

---

## Phase 1 (continued): Research Execution

### 1.4 Automated Research

**Skill:** `competitive-research-brightdata`

Use the research skill to gather data systematically:

```
Skill: competitive-research-brightdata
```

**Research Process:**
1. **Batch Search:** 3-4 queries per batch (respect 25k token limit)
2. **Batch Scrape:** 2-3 URLs per batch
3. **Document Sources:** Capture URL, access date, publication date

**Data to Gather:**
- Company overview (founded, HQ, ownership, funding)
- Product/service details (features, integrations, technology)
- Pricing information (model, range, confidence level)
- Market position (customers, market share, geography)
- Customer satisfaction (ratings, reviews, sentiment)

---

### 1.5 Manual Research

**Supplement automated research with:**
- Company websites (About, Products, Pricing, Newsroom)
- Review sites (G2, Capterra, TrustRadius)
- Funding databases (Crunchbase, PitchBook)
- Industry reports (Gartner, Forrester if available)
- News articles (recent announcements, acquisitions)
- SEC filings (if public company)

**Research Documentation:**
- Save all sources to `01-RESEARCH-INPUTS/sources.md`
- Use "(Source, YYYY)" format for all citations
- Note confidence level: Verified, Estimated, Unknown

---

### 1.6 Research Completion Check

**Before moving to Analysis, verify:**

| Criterion | Target | Status |
|-----------|--------|--------|
| All competitors researched | 100% | [ ] |
| Research questions answered | 80%+ | [ ] |
| Sources documented | All | [ ] |
| Pricing data gathered | All competitors | [ ] |
| Feature data complete | Core features | [ ] |
| Satisfaction ratings | Where available | [ ] |

**If gaps exist:** Document as "Data not available" with explanation.

---

## Phase 2: Analysis

### 2.1 Competitive Matrices

**Create comparison matrices:**

| Matrix Type | Content | Output Location |
|-------------|---------|-----------------|
| Feature Comparison | 50+ features across all competitors | `02-ANALYSIS-OUTPUTS/competitive-matrices/` |
| Pricing Comparison | Price ranges, models, confidence | `02-ANALYSIS-OUTPUTS/competitive-matrices/` |
| Positioning Comparison | Target segment, value prop, differentiators | `02-ANALYSIS-OUTPUTS/competitive-matrices/` |

**Matrix Format:**
- Rows: Features/attributes
- Columns: Competitors (including client)
- Values: Yes/No/Partial, or numeric scores

---

### 2.2 SWOT Analyses

**Create SWOT for each entity:**
- Client company SWOT
- Each competitor SWOT (5-8 SWOTs total)

**SWOT Format:**
| Strengths | Weaknesses |
|-----------|------------|
| - Item 1  | - Item 1   |
| - Item 2  | - Item 2   |

| Opportunities | Threats |
|---------------|---------|
| - Item 1      | - Item 1|
| - Item 2      | - Item 2|

---

### 2.3 Market Positioning

**Create Four-Quadrant Positioning Map:**

```
                    HIGH INNOVATION
                          │
        Innovation        │        Innovation
        Leaders           │        + Market Leaders
        (Low Market)      │        (Ideal Position)
                          │
    ──────────────────────┼──────────────────────
                          │
        Niche/            │        Market
        Legacy Players    │        Leaders
        (Low Both)        │        (Low Innovation)
                          │
                    LOW INNOVATION

    ◄─── LOW MARKET COVERAGE ───── HIGH MARKET COVERAGE ───►
```

**Positioning Criteria:**
- Define X-axis dimension (e.g., Market Coverage)
- Define Y-axis dimension (e.g., Innovation)
- Score each competitor (1-10 scale)
- Document scoring methodology

---

### 2.4 Strategic Recommendations

**Develop 5-7 strategic priorities:**

| Priority | Title | Investment | Timeline | Impact |
|----------|-------|------------|----------|--------|
| 1 | [CRITICAL] | $XXK-$XXK | Q1-Q2 | [Impact] |
| 2 | [CRITICAL] | $XXK-$XXK | Q2-Q3 | [Impact] |
| 3 | [HIGH] | $XXK-$XXK | Q3-Q4 | [Impact] |
| ... | ... | ... | ... | ... |

**For each recommendation:**
- Objective (one sentence)
- Strategic rationale (why this matters)
- Investment estimate (range)
- Timeline (quarters)
- Success metrics

---

## Phase 3: Deliverables Creation

### 3.1 Executive Summary

**Use Template:** `templates/competitive-analysis/deliverables-templates/executive-summary-template.md`

**Target Length:** 15-20 pages

**Sections:**
1. Executive Overview (1-2 pages)
2. Competitive Landscape (2-3 pages)
3. Key Findings (5-7 pages) - 5 findings with evidence
4. Strategic Recommendations (4-6 pages) - 5-7 priorities
5. Implementation Timeline (1 page)
6. Investment Summary (1 page)
7. Sources & References (1-2 pages)

---

### 3.2 Full Report

**Use Template:** `templates/competitive-analysis/deliverables-templates/full-report-template.md`

**Target Length:** 50-70 pages

**Structure:**
- Part I: Executive Overview
- Part II: Market Landscape
- Part III: Competitor Profiles (detailed, one per competitor)
- Part IV: Strategic Analysis
- Part V: Strategic Implications
- Part VI: Appendices

---

### 3.3 Visualizations

**Create 10 HTML visualization files:**

| # | Visualization | Template |
|---|---------------|----------|
| 1 | SWOT Analysis | `visualization-template.html` |
| 2 | Competitive Positioning | Custom |
| 3 | Feature Comparison Matrix | Custom |
| 4 | Pricing Analysis | Custom |
| 5 | Market Positioning | Custom |
| 6 | Target Segments | Custom |
| 7 | Technology Stack | Custom |
| 8 | Market Trends | Custom |
| 9 | Strategic Recommendations | Custom |
| 10 | Threats & Opportunities | Custom |

**Convert to Enterprise PDFs:**
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu \
  --print-to-pdf="output-ENTERPRISE.pdf" \
  "file://$(pwd)/visualization.html"
```

---

## Phase 4: QA & Refinement

### 4.1 QA Pass 1

**Skill:** `competitive-analysis-quality-assurance`

```
Skill: competitive-analysis-quality-assurance
```

**Run Standard Review:**
- Verify key claims (20-30 claims)
- Validate major sources (10-15 sources)
- Cross-document consistency check
- Gap identification

**Expected Findings Categories:**
- Missing citations
- Inconsistent data across documents
- Marketing language
- Unsupported claims
- Outdated information

---

### 4.2 Fix Issues

**Address findings by priority:**

| Priority | Action | Example |
|----------|--------|---------|
| Critical | Must fix before delivery | Factual errors, missing sources |
| High | Should fix | Inconsistencies, unclear language |
| Medium | Nice to fix | Minor formatting, optional enhancements |

**Common Fixes:**
- Add "(Source, YYYY)" citations
- Standardize numbers across documents
- Add disclaimers for inferred data
- Remove marketing language
- Update outdated information

---

### 4.3 QA Pass 2

**Re-run QA skill to verify fixes:**

**Target:** 0 Critical issues, <3 High issues

**Verification Checklist:**
- [ ] All critical issues resolved
- [ ] Cross-document consistency: 100%
- [ ] All numeric claims have citations
- [ ] No marketing language remaining
- [ ] Disclaimers added where needed

---

### 4.4 Final Verification

**Skill:** `superpowers:verification-before-completion`

**Before claiming "done":**
1. Run all verification commands
2. Confirm expected outputs match
3. Document completion evidence
4. Get sign-off (if required)

**Quality Score Target:** 9.5/10

---

## Phase 5: Client Feedback & Iterations

### 5.1 Receive Feedback

**Skill:** `superpowers:brainstorming`

When client feedback arrives:
1. **Clarify:** Use brainstorming to understand feedback fully
2. **Categorize:** Quick update vs. major revision
3. **Scope:** Identify all affected files
4. **Plan:** Determine workflow needed

---

### 5.2 Plan Changes

**Skill:** `superpowers:writing-plans`

For major changes:
1. Create detailed implementation plan
2. Break into atomic tasks
3. Add verification commands
4. Group into batches

**Plan File Location:** `docs/plans/[date]-[description].md`

---

### 5.3 Execute Changes

**Skill:** `superpowers:executing-plans`

1. Load plan file
2. Execute in 3-task batches
3. Verify each task
4. Report after each batch
5. Stop on verification failure

---

### 5.4 Verify & Deliver

**Final Steps:**
1. Run QA skill on changed documents
2. Use verification skill to confirm complete
3. Update VERSION-HISTORY.md
4. Deliver to client

**Iteration Loop:** Repeat 5.1-5.4 as needed until client approves.

---

## Quality Standards

**Target: 9.5/10 Client-Ready Quality**

- All claims cite sources with "(Source, YYYY)" format
- Cross-document consistency: 100%
- No marketing language or unsupported claims
- All numeric data has confidence levels
- Professional enterprise formatting
- All visualizations print-ready

---

## Automation Scripts

### Available Scripts

**Location:** `06-AUTOMATION/scripts/`

---

### generate-pdfs.sh

**Purpose:** Generate all 10 enterprise PDFs from HTML visualizations

**Usage:**
```bash
./06-AUTOMATION/scripts/generate-pdfs.sh
```

**What it does:**
1. Finds all `*-viz.html` files in visualization directory
2. Converts each to PDF using Chrome headless
3. Names output `*-ENTERPRISE.pdf`
4. Reports success/failure for each file

**Expected Output:**
```
Generating PDFs...
✓ swot-analysis-viz.html → swot-analysis-viz-ENTERPRISE.pdf
✓ competitive-positioning-viz.html → competitive-positioning-viz-ENTERPRISE.pdf
...
Complete: 10/10 PDFs generated
```

---

### docx-to-html.py

**Purpose:** Convert DOCX files to styled HTML with enterprise theme

**Usage:**
```bash
python 06-AUTOMATION/scripts/docx-to-html.py input.docx output.html
```

**What it does:**
1. Reads DOCX file using python-docx
2. Converts to HTML structure
3. Applies enterprise-styles.css
4. Outputs styled HTML file

**Expected Output:**
```
Converting: executive-summary.docx
Applying enterprise theme...
Output: executive-summary.html (15 pages)
```

---

### qa-consistency-check.py

**Purpose:** Automated consistency checks across documents

**Usage:**
```bash
python 06-AUTOMATION/scripts/qa-consistency-check.py --directory 03-DELIVERABLES/current/
```

**What it does:**
1. Scans all documents in directory
2. Extracts key data points (pricing, market share, etc.)
3. Compares across documents
4. Reports inconsistencies

**Expected Output:**
```
Consistency Check Report
========================
Files scanned: 4
Data points extracted: 127
Inconsistencies found: 0

✓ All documents consistent
```

---

### Script Templates

**Location:** `06-AUTOMATION/templates/`

| Template | Purpose |
|----------|---------|
| `enterprise-styles.css` | Standard enterprise styling for HTML/PDF |
| `visualization-base.html` | Base HTML template for visualizations |

---

## Common Scenarios

### Scenario 1: New Competitive Analysis (From Scratch)

**Use Full Workflow**

**When:** Starting a brand new competitive analysis project

**Steps:**
1. **Setup:** Brainstorm scope, set up project structure
2. **Research:** Use `competitive-research-brightdata`, gather all competitor data
3. **Analysis:** Create matrices, SWOTs, positioning maps, recommendations
4. **Deliverables:** Write exec summary, full report, create 10 visualizations
5. **QA:** Run QA skill twice, fix all issues
6. **Iterate:** Handle client feedback as needed
7. **Deliver:** Final verification, deliver to client

**Skills Used:** All

---

### Scenario 2: Quick Competitive Update (Existing Analysis)

**Use Abbreviated Workflow**

**When:** Updating an existing analysis with new data (new funding round, pricing change, feature update)

**Steps:**
1. **Identify Change:** What data needs updating?
2. **Find Affected Files:** Use grep to locate all references
3. **Update Source Files:** Edit DOCX/HTML files (not PDFs)
4. **Regenerate PDFs:** Run `generate-pdfs.sh`
5. **Quick QA:** Spot-check consistency
6. **Document:** Update VERSION-HISTORY.md
7. **Deliver:** Provide updated files

**Skills Used:** None (or quick QA skill check)

**Example:**
```bash
# Find all references to SCOIR funding
grep -r "SCOIR.*funding" 03-DELIVERABLES/current/

# Update in all files
# Regenerate PDFs
./06-AUTOMATION/scripts/generate-pdfs.sh

# Document change
echo "- Updated SCOIR funding to $XXM" >> 03-DELIVERABLES/VERSION-HISTORY.md
```

---

### Scenario 3: Strategic Pivot (Like V2.0)

**Use Major Iteration Workflow**

**When:** Client requests significant strategic changes (repositioning, different focus, major additions)

**Steps:**
1. **Brainstorm:** Use `superpowers:brainstorming` to fully understand the pivot
2. **Plan:** Use `superpowers:writing-plans` to create detailed plan
3. **Execute:** Use `superpowers:executing-plans` in 3-task batches
4. **QA:** Run full QA skill after changes complete
5. **Verify:** Use `superpowers:verification-before-completion`
6. **Deliver:** Update version, deliver to client

**Skills Used:** All superpowers skills + QA skill

**Example (V2.0 Pivot):**
- Client: "Flip recommendations from international-first to US-first"
- Impact: Executive summary, full report, 3 visualizations
- Approach: Create plan → execute in batches → verify consistency → deliver

---

## Quick Reference

### Workflow Decision Matrix

| Situation | Scenario |
|-----------|----------|
| New project from scratch | Scenario 1: Full Workflow |
| Single data point update | Scenario 2: Quick Update |
| New competitor added | Scenario 1: Full (partial) |
| Typo/formatting fix | Scenario 2: Quick Update |
| Strategic direction change | Scenario 3: Strategic Pivot |
| Client says "change everything" | Scenario 3: Strategic Pivot |
| Quarterly refresh | Scenario 2: Quick Update |

---

**Document Created:** November 25, 2025
**Based On:** Maia Learning Competitive Analysis Project

