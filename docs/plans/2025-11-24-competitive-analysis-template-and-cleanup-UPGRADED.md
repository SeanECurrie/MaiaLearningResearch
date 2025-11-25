# Competitive Analysis Template & Project Cleanup Implementation Plan

> **Execution Requirement:** All tasks in this plan must be executed strictly using `superpowers:executing-plans` in 3‑task batches. Verification is mandatory after each task and each batch. Do not proceed to the next task or batch until verification output matches the expected result exactly.

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task in 3-task batches with review checkpoints.

**Goal:** Transform the Maia Learning competitive analysis project into a reusable template system while documenting all successful patterns, cleaning up project structure, and enhancing custom skills for future competitive analyses.

**Architecture:** Multi-phase iterative approach with review loops. Each phase produces documentation that feeds into the next, culminating in: (1) a reusable competitive analysis template, (2) clean project structure with clear inputs/outputs, (3) enhanced custom skills, and (4) iteration framework for quick updates.

**Tech Stack:**
- Markdown (documentation)
- Python (automation scripts)
- Pandoc (document conversion)
- Chrome Headless (PDF generation)
- Custom Claude Skills (competitive-analysis-quality-assurance, competitive-research-brightdata)

**Project Root:** `/Users/seancurrie/Desktop/MaiaLearningResearch`

---

## PHASE 1: DISCOVERY & ITERATION REVIEW

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Document the complete journey from initial research through V2.0, identifying successful patterns and areas for improvement.

### Task 1.1: Create Project File Inventory

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/PROJECT-INVENTORY.md`

**Step 1: Generate file listing**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
find . -type f \( -name "*.md" -o -name "*.docx" -o -name "*.pdf" -o -name "*.html" \) | sort > docs/file-inventory-temp.txt
```

**Step 2: Create inventory document with directory descriptions**

Create `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/PROJECT-INVENTORY.md` with:
- Header with project name, date, status
- Section for each top-level directory (05-FINAL-DELIVERABLES, docs, etc.)
- File counts per directory
- Status of each major file (current, archived, working)
- Cross-reference to VERSION-HISTORY

**Step 3: Verify inventory**

```bash
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/docs/PROJECT-INVENTORY.md && \
grep -c "^##" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/PROJECT-INVENTORY.md
# Expected: 5+ directory sections
```


**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.


### Task 1.2: Document Iteration 1 (Initial Research)

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/ITERATION-HISTORY.md`

**Step 1: Create iteration history header and Iteration 1 section**

Document Iteration 1 (September-October 2025) including:
- Goal: Gather competitive intelligence and create initial deliverables
- Inputs: Web research on 7 competitors, market sizing data, pricing information
- Outputs: Initial competitive analysis, basic feature comparisons
- Challenges encountered: Incomplete source attribution, pricing inconsistencies, market sizing context unclear
- Skills used: `competitive-research-brightdata` for initial data gathering

**Step 2: Verify section created**

```bash
grep "Iteration 1" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/ITERATION-HISTORY.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 1.3: Document Iteration 2 (QA Corrections)

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/ITERATION-HISTORY.md`

**Step 1: Add Iteration 2 section**

Document Iteration 2 (November 2025) including:
- Goal: Add source citations, fix pricing errors, enhance disclaimers
- Process: Used `competitive-analysis-quality-assurance` skill for systematic review
- Key fixes: 35+ modifications, 100+ inline citations added
- Pricing corrections: Naviance $6-8 → $8-12 (est.), SCOIR verified at $4.80
- Quality improvement: 7.5/10 → 9.5/10
- Outputs: Version 1.0 deliverables

**Step 2: Verify section added**

```bash
grep "Iteration 2" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/ITERATION-HISTORY.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 1.4: Document Iteration 3 (Tim's V2.0 Revisions)

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/ITERATION-HISTORY.md`

**Step 1: Add Iteration 3 section**

Document Iteration 3 (November 24, 2025) including:
- Goal: Flip strategy to US-primary, fix positioning maps, remove taglines
- Tim's direction quotes: "Attack biggest market in the world" (US market)
- Process: Used `superpowers:brainstorming` for requirements clarification, `superpowers:writing-plans` for structured implementation
- Key changes:
  1. Strategic recommendations: 7 → 6 priorities, Priority 1 = "Attack US Market" ($650K-1.25M)
  2. Positioning maps: Converted to four-quadrant format with visible crossbars
  3. Marketing taglines: Removed, kept positioning proof points
  4. Naviance pricing: Final consistency fix to $8-12 (est.)
- Outputs: Version 2.0 deliverables, 3 PDFs regenerated, 2 new enterprise-themed PDFs

**Step 2: Verify section added**

```bash
grep "Iteration 3" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/ITERATION-HISTORY.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 1.5: Document Iteration Patterns and Lessons Learned

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/ITERATION-HISTORY.md`

**Step 1: Add Pattern Analysis section**

Document what worked well:
- Skill-based workflow (research → QA → verification)
- Phased approach (discovery → planning → implementation → QA)
- Documentation (before/after specs, change logs, QA reports)
- Version control (backups before major changes)

Document what could be improved:
- Initial structure (files scattered, unclear input/output separation)
- Skill usage documentation (not documented in-process)
- Template opportunity (deliverable structure discovered organically)
- Automation (manual PDF regeneration)

**Step 2: Add Lessons Learned section**

Document actionable lessons for next project:
- Do from start: Clear directory structure, use competitive-research-brightdata first, start with template
- Don't: Scatter files, skip brainstorming, forget backups, skip verification
- Automation opportunities: Batch PDF generation, DOCX→HTML→PDF pipeline, QA consistency scripts

**Step 3: Verify sections added**

```bash
grep -E "Pattern Analysis|Lessons Learned" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/ITERATION-HISTORY.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 1.6: Create Skills Usage Report

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/SKILLS-USAGE-REPORT.md`

**Step 1: Document custom skills used**

Create skills report documenting:

**competitive-research-brightdata:**
- When used: Initial research phase
- How: Invoked with competitor list and research questions
- Inputs: Competitor names (Naviance, SCOIR, SchooLinks, Xello, Cialfo, Overgrad, BridgeU)
- Outputs: Competitor data (pricing, features, reviews, funding)
- Outcome: Comprehensive data gathered efficiently
- Improvements needed: Output format standardization, research question templates

**competitive-analysis-quality-assurance:**
- When used: QA phase after deliverables drafted
- How: Invoked with deliverable files for systematic review
- Inputs: Draft DOCX, HTML, PDF files
- Outputs: QA report with 35+ findings
- Outcome: Quality 7.5/10 → 9.5/10
- Improvements needed: Cross-document consistency check, source attribution verification, marketing language detection

**Step 2: Verify custom skills documented**

```bash
grep -c "competitive-" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/SKILLS-USAGE-REPORT.md
# Expected: 4+ references
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 1.7: Document Superpowers Skills Used

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/SKILLS-USAGE-REPORT.md`

**Step 1: Add superpowers skills section**

Document each superpowers skill:

**superpowers:brainstorming:**
- When: Before implementing Tim's revisions
- How: Presented rough feedback, skill asked 6 clarifying questions
- Outcome: Perfect alignment with Tim's vision, zero rework

**superpowers:verification-before-completion:**
- When: End of each phase
- How: Before claiming "done", verified actual output against requirements
- Outcome: 100% confidence in deliverable quality

**superpowers:writing-plans:**
- When: Creating this meta-project plan
- How: Defined goal, broke into bite-sized tasks
- Expected: Structured multi-phase approach

**superpowers:executing-plans:**
- When: Implementing plans task-by-task
- How: 3-task batches with review checkpoints
- Expected: Systematic completion

**Step 2: Add skills NOT used but should have been**

Document:
- `superpowers:using-git-worktrees`: Could have isolated V2.0 work
- `superpowers:test-driven-development`: Could have tested document generation
- `superpowers:systematic-debugging`: Could have debugged PDF conversion issues

**Step 3: Verify superpowers skills documented**

```bash
grep -c "superpowers:" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/SKILLS-USAGE-REPORT.md
# Expected: 6+ references
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 1.8: Document Skill Workflow Patterns

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/SKILLS-USAGE-REPORT.md`

**Step 1: Add workflow patterns section**

Document three proven patterns:

**Pattern 1: Research → QA → Verify**
```
competitive-research-brightdata (gather)
    ↓
competitive-analysis-quality-assurance (verify)
    ↓
superpowers:verification-before-completion (final check)
```
Use for: Initial deliverables creation (V1.0)

**Pattern 2: Brainstorm → Plan → Execute**
```
superpowers:brainstorming (refine requirements)
    ↓
superpowers:writing-plans (create plan)
    ↓
superpowers:executing-plans (implement)
```
Use for: Major feature additions or strategic changes

**Pattern 3: Iterate → Verify → Document**
```
[Make changes]
    ↓
superpowers:verification-before-completion (verify)
    ↓
competitive-analysis-quality-assurance (consistency)
```
Use for: Ensuring quality across iterations

**Step 2: Verify patterns documented**

```bash
grep "Pattern [123]" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/SKILLS-USAGE-REPORT.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

## PHASE 2: TEMPLATE CREATION

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Extract successful patterns into a reusable competitive analysis template that can be used for any company.

### Task 2.1: Create Template Directory Structure

**Files:**
- Create directory: `/Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/`
- Create subdirectories: `deliverables-templates/`, `automation-scripts/`

**Step 1: Create directories**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mkdir -p templates/competitive-analysis/deliverables-templates
mkdir -p templates/competitive-analysis/automation-scripts
```

**Step 2: Verify directories created**

```bash
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/deliverables-templates && echo "OK"
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 2.2: Create Template README

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/README.md`

**Step 1: Write template README**

Include:
- Purpose: Standardized process for conducting competitive analysis
- Quality target: 9.5/10 (enterprise-grade, client-ready)
- Quick start instructions: Copy template directory, follow phases in order
- Deliverables checklist: 2 primary reports (Executive Summary, Full Report), 10 visualization PDFs, documentation
- Directory structure template with placeholders
- Skills required: custom skills + superpowers skills
- Quality metrics: 100% citations, pricing accuracy, consistency, professional presentation

**Step 2: Verify README created**

```bash
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/README.md && \
head -5 /Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/README.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 2.3: Create Research Phase Template

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/01-RESEARCH-PHASE.md`

**Step 1: Write research phase guide**

Include:
- Objective: Gather comprehensive competitive intelligence
- Skill: `competitive-research-brightdata`
- Pre-research checklist: Identify 5-7 competitors, define research questions, set up tracking
- Research questions template (20 questions per competitor covering: company overview, pricing, features, market position, funding, satisfaction)
- How to invoke the skill with competitor list
- Manual research tasks: Review sites (G2, Capterra), funding databases (Crunchbase, PitchBook), company websites
- Research tracking spreadsheet template
- Sources.md template for citation tracking
- Completion checklist before moving to analysis

**Step 2: Verify research phase template created**

```bash
grep "competitive-research-brightdata" /Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/01-RESEARCH-PHASE.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 2.4: Create Analysis Phase Template

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/02-ANALYSIS-PHASE.md`

**Step 1: Write analysis phase guide**

Include:
- Objective: Transform raw research into strategic insights
- No specific skill (manual analysis phase)
- Competitive matrices to create: Feature comparison (50+ features), pricing comparison, market positioning
- SWOT analysis for each competitor (5-7) plus client company
- Market positioning map (Innovation × Market Coverage, four-quadrant format)
- Strategic recommendations framework: 5-7 recommendations with priority (CRITICAL/HIGH/MEDIUM), investment estimates, implementation actions
- Output directory structure
- Completion checklist before moving to deliverables

**Step 2: Verify analysis phase template created**

```bash
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/02-ANALYSIS-PHASE.md && echo "OK"
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 2.5: Create Deliverables Phase Template

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/03-DELIVERABLES-PHASE.md`

**Step 1: Write deliverables phase guide**

Include:
- Objective: Create client-ready deliverables
- Executive Summary structure (15-20 pages): Executive Overview, Competitive Landscape, Key Findings (5-7), Strategic Recommendations (5-7), Implementation Timeline, Sources
- Full Report structure (50-70 pages): Parts I-VI covering overview, market, competitor profiles, analysis, implications, appendices
- 10 visualization PDFs to create: Competitive Positioning, Market Trends, SWOT, Strategic Recommendations, Threats & Opportunities, Feature Matrix, Pricing, Tech Stack, Positioning Map, Target Segments
- HTML template references for visualizations
- PDF generation commands (Chrome headless)
- Completion checklist

**Step 2: Verify deliverables phase template created**

```bash
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/03-DELIVERABLES-PHASE.md && echo "OK"
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 2.6: Create QA Phase Template

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/04-QA-PHASE.md`

**Step 1: Write QA phase guide**

Include:
- Objective: Systematic quality verification
- Skill: `competitive-analysis-quality-assurance`
- QA Pass 1 process: Run skill, review findings, create fix list
- Expected findings categories: Missing citations, pricing inconsistencies, disclaimer gaps, formatting issues
- Fix implementation guidance
- QA Pass 2: Re-run skill, verify all fixed
- Skill: `superpowers:verification-before-completion` for final check
- Quality metrics to verify: 100% citations, pricing accuracy, consistency, no marketing language
- Completion checklist before client delivery

**Step 2: Verify QA phase template created**

```bash
grep "competitive-analysis-quality-assurance" /Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/04-QA-PHASE.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 2.7: Create Iteration Phase Template

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/05-ITERATION-PHASE.md`

**Step 1: Write iteration phase guide**

Include:
- Objective: Handle client feedback systematically
- Skill sequence: `superpowers:brainstorming` → `superpowers:writing-plans` → `superpowers:executing-plans` → `competitive-analysis-quality-assurance` → `superpowers:verification-before-completion`
- Receiving feedback process: Use brainstorming to clarify
- Planning changes: Use writing-plans for detailed task list
- Implementing changes: Use executing-plans for systematic execution
- Verifying changes: Use QA skill then verification skill
- Version control guidance: Bump version, update VERSION-HISTORY.md
- Quick iteration vs. full iteration decision guide

**Step 2: Verify iteration phase template created**

```bash
grep "superpowers:brainstorming" /Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/05-ITERATION-PHASE.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 2.8: Create Executive Summary Template

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/deliverables-templates/executive-summary-template.md`

**Step 1: Write executive summary template**

Create fill-in-the-blank template with:
- Header: [Company Name], [Industry], [Date], [Analyst]
- Executive Overview with placeholder for key finding
- Competitive Landscape section (5-7 competitors with brief positioning)
- Key Findings sections (5-7) with structure: Summary, Implications, Source
- Strategic Recommendations (5-7) with structure: Objective, Rationale, Implementation actions, Investment, Expected Return
- Critical Decision Points section
- Competitive Positioning Summary (SWOT format)
- Investment Summary table
- Sources & References section (15-20 sources)
- Metadata: Report length 15-20 pages, version, status

**Step 2: Verify executive summary template created**

```bash
grep "Strategic Recommendations" /Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/deliverables-templates/executive-summary-template.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 2.9: Create Full Report Template

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/deliverables-templates/full-report-template.md`

**Step 1: Write full report template**

Create fill-in-the-blank template with:
- PART I: Executive Overview (summary, scope, methodology)
- PART II: Market Landscape (TAM, growth, trends, disruptions)
- PART III: Competitor Profiles (7 detailed profiles with: overview, pricing, features, positioning, SWOT, threat assessment)
- PART IV: Strategic Analysis (competitive positioning map, SWOT matrix, threats & opportunities)
- PART V: Strategic Implications (recommendations with investment/timeline, implementation roadmap, decision points)
- PART VI: Appendices (feature matrix, pricing table, tech stack comparison, sources)
- Metadata: Report length 50-70 pages, version, status

**Step 2: Verify full report template created**

```bash
grep "PART VI" /Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/deliverables-templates/full-report-template.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 2.10: Create Visualization HTML Template

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/deliverables-templates/visualization-template.html`

**Step 1: Write HTML template with enterprise styling**

Create HTML template with:
- DOCTYPE and head with embedded CSS (enterprise theme)
- Header section with title, date, company placeholders
- Main content area with placeholder sections
- Chart container divs (for various visualization types)
- Footer with version and status
- Print-friendly CSS media queries
- Enterprise color scheme variables (professional blues, grays)

**Step 2: Verify HTML template created**

```bash
grep "enterprise" /Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/deliverables-templates/visualization-template.html
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 2.11: Validate Templates Against Maia Final Deliverables

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/TEMPLATE-VALIDATION-NOTES.md`

**Step 1: Compare templates to final Maia deliverables**

Using the final, corrected deliverables in:
- `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/current-enterprise-cleaned-report-documents/`

Do the following:
- Read the latest Executive Summary, Full Report, and key visualization HTML/PDF files from this directory.
- Confirm that the templates in `templates/competitive-analysis/deliverables-templates/` (executive-summary-template.md, full-report-template.md, visualization-template.html) contain placeholders for all major sections, disclaimers, citation patterns, and enterprise styling patterns present in the Maia final deliverables.
- Note any gaps where the templates are missing sections, disclaimers, or patterns that appear in the final Maia deliverables.

**Step 2: Document validation findings**

Create `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/TEMPLATE-VALIDATION-NOTES.md` including:
- A "Coverage Summary" section listing each template and whether it fully reflects the final Maia deliverables.
- A bullet list of any gaps or differences that should be addressed in future template updates.
- Specific file references (both template and final deliverable) for any notable differences.

**Step 3: Verify validation notes created**

```bash
grep "Coverage Summary" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/TEMPLATE-VALIDATION-NOTES.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

## PHASE 3: PROJECT RESTRUCTURING

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Reorganize the Maia Learning project into clean input/output structure with clear iteration tracking.

**Prerequisite:** Do not start any Phase 3 tasks until all Phase 2 tasks, including Task 2.11 (Template Validation), have been completed and verified.

### Task 3.1: Design New Directory Structure

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/NEW-STRUCTURE-DESIGN.md`

**Step 1: Document proposed structure**

Design new structure:
```
MaiaLearningResearch/
├── 00-PROJECT-MANAGEMENT/ (README, STATUS, STAKEHOLDERS)
├── 01-RESEARCH-INPUTS/ (competitor-data/, market-research/, pricing-data/, sources.md)
├── 02-ANALYSIS-OUTPUTS/ (competitive-matrices/, swot-analyses/, market-positioning/, recommendations/)
├── 03-DELIVERABLES/ (current/DOCX+HTML+PDF, v1.0/, v0.9/, VERSION-HISTORY.md)
├── 04-QA-DOCUMENTATION/ (qa-reports/, change-logs/, verification/)
├── 05-ITERATIONS/ (iteration-1/, iteration-2/, iteration-3/)
├── 06-AUTOMATION/ (scripts/, templates/)
├── docs/ (plans/, guides/, reference/)
└── templates/ (competitive-analysis/ template for next project)
```

Include:
- Current problem description (files scattered)
- Benefits of new structure (clear separation, iteration tracking, automation-ready)
- Migration plan outline (create structure → copy files → update documentation)

**Step 2: Verify design document created**

```bash
grep "03-DELIVERABLES" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/NEW-STRUCTURE-DESIGN.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 3.2: Create New Directory Structure

**Files:**
- Create directories as specified in NEW-STRUCTURE-DESIGN.md

**Step 1: Create all new directories**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mkdir -p 00-PROJECT-MANAGEMENT
mkdir -p 01-RESEARCH-INPUTS/{competitor-data,market-research,pricing-data,feature-data}
mkdir -p 02-ANALYSIS-OUTPUTS/{competitive-matrices,swot-analyses,market-positioning,strategic-recommendations}
mkdir -p 03-DELIVERABLES/{current,v1.0,v0.9}/{DOCX,HTML,PDF}
mkdir -p 03-DELIVERABLES/current/{HTML/visualizations,PDF/visualizations}
mkdir -p 04-QA-DOCUMENTATION/{qa-reports,change-logs,verification}
mkdir -p 05-ITERATIONS/{iteration-1-initial-research,iteration-2-qa-corrections,iteration-3-tim-revisions}
mkdir -p 06-AUTOMATION/{scripts,templates}
```

**Step 2: Verify directories created**

```bash
ls -d /Users/seancurrie/Desktop/MaiaLearningResearch/0*/ | wc -l
# Expected: 7 directories (00 through 06)
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 3.3: Copy Current Deliverables to New Structure

**Files:**
- Copy from: `05-FINAL-DELIVERABLES/VISUALIZATIONS/current-enterprise-cleaned-report-documents/`
- Copy to: `03-DELIVERABLES/current/`

**Step 1: Copy DOCX files**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/current-enterprise-cleaned-report-documents/*.docx 03-DELIVERABLES/current/DOCX/
```

**Step 2: Copy HTML files**

```bash
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/current-enterprise-cleaned-report-documents/*.html 03-DELIVERABLES/current/HTML/
```

**Step 3: Copy PDF files**

```bash
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/current-enterprise-cleaned-report-documents/*.pdf 03-DELIVERABLES/current/PDF/
```

**Step 4: Verify copies**

```bash
ls 03-DELIVERABLES/current/DOCX/ | wc -l
ls 03-DELIVERABLES/current/PDF/ | wc -l
# Expected: 2+ DOCX, 2+ PDF files
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 3.4: Copy Visualization Files to New Structure

**Files:**
- Copy from: `05-FINAL-DELIVERABLES/VISUALIZATIONS/`
- Copy to: `03-DELIVERABLES/current/HTML/visualizations/` and `PDF/visualizations/`

**Step 1: Copy visualization HTML files**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/*-viz.html 03-DELIVERABLES/current/HTML/visualizations/ 2>/dev/null || true
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/*-top4-viz.html 03-DELIVERABLES/current/HTML/visualizations/ 2>/dev/null || true
```

**Step 2: Copy visualization PDF files**

```bash
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/*-ENTERPRISE.pdf 03-DELIVERABLES/current/PDF/visualizations/
```

**Step 3: Verify copies**

```bash
ls 03-DELIVERABLES/current/PDF/visualizations/ | wc -l
# Expected: 10 ENTERPRISE PDF files
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 3.5: Copy QA Documentation to New Structure

**Files:**
- Copy from: `05-FINAL-DELIVERABLES/VISUALIZATIONS/current-enterprise-cleaned-report-documents/TIM-REVISIONS-*.md`
- Copy to: `05-ITERATIONS/iteration-3-tim-revisions/`

**Step 1: Copy Tim revision documentation**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/current-enterprise-cleaned-report-documents/TIM-REVISIONS-*.md 05-ITERATIONS/iteration-3-tim-revisions/
```

**Step 2: Copy enterprise styles for automation**

```bash
cp 05-FINAL-DELIVERABLES/VISUALIZATIONS/enterprise-styles.css 06-AUTOMATION/templates/
```

**Step 3: Verify copies**

```bash
ls 05-ITERATIONS/iteration-3-tim-revisions/*.md | wc -l
# Expected: 3 files (PLAN, INVENTORY, QA-REVIEW)
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 3.6: Create VERSION-HISTORY.md

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/03-DELIVERABLES/VERSION-HISTORY.md`

**Step 1: Write version history**

Document all versions:

**V2.0 (November 24, 2025) - US-Primary Strategy:**
- Strategic recommendations flipped to US-primary
- Priority 1: "Attack US Market" ($650K-1.25M)
- Positioning maps converted to four-quadrant format
- Marketing taglines removed
- Enterprise-themed PDFs generated
- Files changed: executive-summary, full-report, 3 visualization PDFs

**V1.0 (November 2025) - QA Corrections:**
- Added 100+ source citations
- Fixed pricing inconsistencies (Naviance $8-12 est., SCOIR $4.80)
- Enhanced disclaimers throughout
- Quality: 7.5/10 → 9.5/10

**V0.9 (September-October 2025) - Initial Deliverables:**
- Initial creation of all deliverables
- Working drafts for review

**Step 2: Verify version history created**

```bash
grep "V2.0" /Users/seancurrie/Desktop/MaiaLearningResearch/03-DELIVERABLES/VERSION-HISTORY.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 3.7: Create Directory README Files

**Files:**
- Create README.md in: `00-PROJECT-MANAGEMENT/`, `01-RESEARCH-INPUTS/`, `02-ANALYSIS-OUTPUTS/`, `03-DELIVERABLES/`, `04-QA-DOCUMENTATION/`, `05-ITERATIONS/`, `06-AUTOMATION/`

**Step 1: Create README for each directory**

Each README should include:
- Purpose of directory
- Contents description
- When to use guidance
- Related directories

**Step 2: Verify READMEs created**

```bash
find /Users/seancurrie/Desktop/MaiaLearningResearch/0* -name "README.md" | wc -l
# Expected: 7 README files
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

## PHASE 4: SKILL ENHANCEMENT

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Update custom skills based on lessons learned, and document usage of all skills utilized.

### Task 4.1: Document QA Skill Enhancements Needed

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/SKILL-UPDATES-competitive-analysis-qa.md`

**Step 1: Review current skill implementation and document enhancement specifications**

Before documenting enhancements, read the current `competitive-analysis-quality-assurance` skill definition from the active Claude skills directory (e.g., `~/.claude/skills/` or `.claude/skills/` under the project root) and base the enhancement specs on the actual behaviors and limitations you observe.

Document 4 enhancements needed for `competitive-analysis-quality-assurance`:

**Enhancement 1: Cross-Document Consistency Check**
- Current: Skill checks individual documents
- Enhancement: Add verification that strategic recommendations, pricing, investments are identical across Executive Summary, Full Report, and Visualization PDFs
- Implementation: Extract key data points, create comparison matrix, flag discrepancies

**Enhancement 2: Source Attribution Verification**
- Current: Checks citations present
- Enhancement: Verify citation completeness and format
- Format requirements: Pricing claims, market share, satisfaction ratings, funding amounts all require `(Source, YYYY)` format
- Implementation: Regex search for numeric claims, verify followed by citation

**Enhancement 3: Marketing Language Detection**
- Current: Not included
- Enhancement: Flag subjective/marketing language
- Red flag words: "best", "leading", "revolutionary", "only", "first"
- Implementation: Scan for red flags, suggest factual replacements

**Enhancement 4: Version Comparison**
- Current: Not included
- Enhancement: Compare V1.0 vs V2.0 changes
- Implementation: Track file size changes, section additions/removals, data changes

**Step 2: Verify enhancement guide created**

```bash
grep "Enhancement [1234]" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/SKILL-UPDATES-competitive-analysis-qa.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 4.2: Document Research Skill Enhancements Needed

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/SKILL-UPDATES-competitive-research.md`

**Step 1: Review current skill implementation and document enhancement specifications**

Before documenting enhancements, read the current `competitive-research-brightdata` skill definition from the active Claude skills directory (e.g., `~/.claude/skills/` or `.claude/skills/` under the project root) and base the enhancement specs on the actual behaviors and limitations you observe.

Document 4 enhancements needed for `competitive-research-brightdata`:

**Enhancement 1: Output Format Standardization**
- Current: Output format varies
- Enhancement: Always output JSON with defined schema
- Schema: competitor.name, pricing.range/source/date/confidence, features[], positioning, funding

**Enhancement 2: Research Question Templates**
- Current: Questions defined ad-hoc
- Enhancement: Provide 20 standard questions covering company overview, pricing, features, market position, funding, satisfaction

**Enhancement 3: Data Validation Rules**
- Current: No validation
- Enhancement: Check completeness of gathered data
- Validation: Required fields filled, confidence levels assigned

**Enhancement 4: Citation Formatting**
- Current: Manual citation creation
- Enhancement: Auto-generate source references
- Format: "(Source, YYYY)" for all data points

**Step 2: Verify enhancement guide created**

```bash
grep "Enhancement [1234]" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/SKILL-UPDATES-competitive-research.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 4.3: Create Comprehensive Skills Usage Guide

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/SKILLS-USAGE-GUIDE.md`

**Step 1: Write skills overview section**

Document:
- Purpose: How to use Claude skills effectively for competitive analysis
- Skill categories: Custom skills (domain-specific) vs. Superpowers skills (process/workflow)
- All 8 relevant skills listed with one-line descriptions

**Step 2: Write when-to-use-each-skill section**

For each phase, document which skill(s) to use:
- Project Setup: `superpowers:brainstorming`
- Research: `competitive-research-brightdata`
- Analysis: Manual (no specific skill)
- Deliverables: Manual (no specific skill)
- QA: `competitive-analysis-quality-assurance`
- Iterations: `superpowers:brainstorming` → `superpowers:writing-plans` → `superpowers:executing-plans`
- Verification: `superpowers:verification-before-completion`

**Step 3: Verify skills guide created**

```bash
grep "superpowers:" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/SKILLS-USAGE-GUIDE.md | wc -l
# Expected: 5+ references
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 4.4: Document Skill Invocation Patterns

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/SKILLS-USAGE-GUIDE.md`

**Step 1: Add invocation syntax section**

Document unified invocation syntax:
- Custom skills: `Skill: skill-name` (e.g., `Skill: competitive-research-brightdata`)
- Superpowers via slash command: `/superpowers:skill-name` (e.g., `/superpowers:brainstorm`)
- Superpowers via Skill tool: `Skill: superpowers:skill-name`

**Step 2: Add common mistakes section**

Document pitfalls:
- Mistake 1: Skipping brainstorming → leads to rework
- Mistake 2: Not using QA skill → misses consistency issues
- Mistake 3: Skipping verification → premature "done" claims

**Step 3: Verify sections added**

```bash
grep "Mistake" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/SKILLS-USAGE-GUIDE.md | wc -l
# Expected: 3 mistakes documented
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 4.5: Document Advanced Skill Workflows

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/SKILLS-USAGE-GUIDE.md`

**Step 1: Add major iteration workflow**

Document full workflow for major changes (like V2.0):
```
1. superpowers:brainstorming (clarify feedback)
2. superpowers:writing-plans (create plan)
3. superpowers:using-git-worktrees (optional: isolate work)
4. superpowers:executing-plans (implement)
5. competitive-analysis-quality-assurance (verify)
6. superpowers:verification-before-completion (final check)
```

**Step 2: Add quick update workflow**

Document abbreviated workflow for minor updates:
```
1. Make changes directly
2. competitive-analysis-quality-assurance (quick check)
3. superpowers:verification-before-completion (verify)
```

**Step 3: Verify workflows added**

```bash
grep "Workflow" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/SKILLS-USAGE-GUIDE.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

## PHASE 5: PROCESS DOCUMENTATION

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Lock down the complete workflow for next competitive analysis project.

### Task 5.1: Create Master Workflow Document - Overview

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`

**Step 1: Write workflow overview section**

Include:
- Purpose: Step-by-step workflow for enterprise-grade competitive analysis
- Target quality: 9.5/10 (client-ready)
- Workflow overview diagram:
  - Setup & Research
  - Analysis
  - Deliverables Creation
  - QA & Refinement
  - Client Feedback & Iterations

**Step 2: Verify overview created**

```bash
head -20 /Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 5.2: Document Setup Phase in Workflow

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`

**Step 1: Add setup phase details**

Document:
- Brainstorm & Scope: Use `superpowers:brainstorming` to clarify requirements, identify competitors, define deliverables
- Setup Project Structure: Copy template, initialize git, create branch
- Research Planning: Create research questions, identify data sources, set up tracker
- Outputs expected: Project scope, competitor list, deliverables checklist

**Step 2: Verify setup phase added**

```bash
grep "Setup" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 5.3: Document Research Phase in Workflow

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`

**Step 1: Add research phase details**

Document:
- Automated Research: Use `competitive-research-brightdata` with competitor list
- Manual Research: Review sites, funding databases, company websites, industry reports
- Research Completion Check: All competitors researched, 80%+ questions answered, sources documented

**Step 2: Verify research phase added**

```bash
grep "Research" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md | wc -l
# Expected: 5+ references
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 5.4: Document Analysis and Deliverables Phases in Workflow

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`

**Step 1: Add analysis phase details**

Document:
- Competitive Matrices: Feature comparison, pricing comparison, positioning comparison
- SWOT Analyses: One per competitor plus client
- Market Positioning: Four-quadrant map, strategic groups
- Strategic Recommendations: 5-7 priorities with investment estimates

**Step 2: Add deliverables phase details**

Document:
- Executive Summary: Use template, 15-20 pages
- Full Report: Use template, 50-70 pages
- Visualizations: 10 HTML files → 10 enterprise PDFs

**Step 3: Verify phases added**

```bash
grep -E "Analysis|Deliverables" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md | wc -l
# Expected: 4+ references
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 5.5: Document QA and Iteration Phases in Workflow

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`

**Step 1: Add QA phase details**

Document:
- QA Pass 1: Run `competitive-analysis-quality-assurance`, review findings, create fix list
- Fix Issues: Add citations, fix inconsistencies, add disclaimers
- QA Pass 2: Re-run skill, verify 0 critical issues
- Final Verification: Use `superpowers:verification-before-completion`

**Step 2: Add iteration phase details**

Document:
- Receive Feedback: Use `superpowers:brainstorming` to clarify
- Plan Changes: Use `superpowers:writing-plans`
- Execute: Use `superpowers:executing-plans`
- Verify: Use QA skill then verification skill

**Step 3: Verify phases added**

```bash
grep "QA Pass" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 5.6: Add Automation Scripts Section to Workflow

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`

**Step 1: Document available automation scripts**

Document:
- `generate-pdfs.sh`: Generate all PDFs from HTML visualizations
- `docx-to-html.py`: Convert DOCX to styled HTML with enterprise theme
- `qa-consistency-check.py`: Automated consistency checks across documents
- Usage examples and expected outputs for each

**Step 2: Verify automation section added**

```bash
grep "generate-pdfs" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 5.7: Add Common Scenarios to Workflow

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`

**Step 1: Document scenario workflows**

Document three scenarios:
- Scenario 1: New Competitive Analysis (from scratch) - full workflow
- Scenario 2: Quick Competitive Update (existing analysis) - abbreviated workflow
- Scenario 3: Strategic Pivot (like V2.0) - brainstorm → plan → execute → verify

**Step 2: Verify scenarios added**

```bash
grep "Scenario" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md | wc -l
# Expected: 3 scenarios
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

## PHASE 6: ITERATION FRAMEWORK

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Create system for quick edits/additions to current project going forward.

### Task 6.1: Create Quick Iterations Guide - Overview

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/QUICK-ITERATIONS-GUIDE.md`

**Step 1: Write guide overview**

Include:
- Purpose: How to make quick updates without full workflow
- When to use quick iterations: Single data point update, typo fix, missing citation, small content addition, PDF regeneration
- When NOT to use: Major strategic changes, adding new competitor, restructuring, significant rewrite

**Step 2: Verify guide created**

```bash
head -20 /Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/QUICK-ITERATIONS-GUIDE.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 6.2: Document Quick Iteration Process

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/QUICK-ITERATIONS-GUIDE.md`

**Step 1: Add step-by-step process**

Document 7 steps:
1. Identify change needed (with examples)
2. Locate all files affected (use grep)
3. Make changes to source files (DOCX + HTML, not PDFs)
4. Regenerate PDFs from sources
5. Quick consistency check
6. Document change in VERSION-HISTORY.md
7. Commit changes

**Step 2: Verify process documented**

```bash
grep "Step [1-7]" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/QUICK-ITERATIONS-GUIDE.md | wc -l
# Expected: 7 steps
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 6.3: Add Quick Iteration Templates

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/QUICK-ITERATIONS-GUIDE.md`

**Step 1: Add iteration templates**

Document 3 templates:
- Template 1: Update Single Data Point (pricing change, funding update)
- Template 2: Add Missing Citation
- Template 3: Fix Formatting Issue

Each template includes: grep command to find references, edit instructions, PDF regeneration command, verification command, commit message format

**Step 2: Verify templates added**

```bash
grep "Template [123]" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/QUICK-ITERATIONS-GUIDE.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 6.4: Add Automation Script Specifications

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/QUICK-ITERATIONS-GUIDE.md`

**Step 1: Document helper scripts for quick iterations**

Document:
- `generate-single-pdf.sh`: Regenerate one PDF without all
- `bulk-replace.py`: Replace text across all source files (with dry-run)
- `verify-consistency.py`: Check that change applied everywhere

**Step 2: Add decision guide**

Document when quick iteration becomes full iteration:
- Change affects 5+ files
- Requires strategic thinking
- Client requests major revision
- Takes >2 hours
- Requires new research

**Step 3: Verify sections added**

```bash
grep "bulk-replace" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/QUICK-ITERATIONS-GUIDE.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 6.5: Create Automation Script Stubs

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/06-AUTOMATION/scripts/generate-pdfs.sh`
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/06-AUTOMATION/scripts/bulk-replace.py`
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/06-AUTOMATION/scripts/verify-consistency.py`

**Step 1: Create generate-pdfs.sh stub**

```bash
#!/bin/bash
# generate-pdfs.sh - Generate PDFs from HTML visualizations
# Usage: ./generate-pdfs.sh [optional: specific-file.html]
# If no file specified, generates all PDFs in current directory

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

if [ -n "$1" ]; then
    # Single file mode
    INPUT="$1"
    OUTPUT="${INPUT%.html}.pdf"
    "$CHROME" --headless --disable-gpu --print-to-pdf="$OUTPUT" "file://$(pwd)/$INPUT"
else
    # All files mode
    for html in *.html; do
        OUTPUT="${html%.html}.pdf"
        "$CHROME" --headless --disable-gpu --print-to-pdf="$OUTPUT" "file://$(pwd)/$html"
    done
fi
```

**Step 2: Create bulk-replace.py stub**

Create Python script with argparse for --find, --replace, --files, --dry-run options.

**Step 3: Create verify-consistency.py stub**

Create Python script with argparse for --search, --expected, --path options.

**Step 4: Verify scripts created**

```bash
ls /Users/seancurrie/Desktop/MaiaLearningResearch/06-AUTOMATION/scripts/*.sh | wc -l
ls /Users/seancurrie/Desktop/MaiaLearningResearch/06-AUTOMATION/scripts/*.py | wc -l
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

### Task 6.6: Final Verification and Summary

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/IMPLEMENTATION-COMPLETE.md`

**Step 1: Create implementation summary**

Document what was completed:
- Phase 1: Discovery documentation (ITERATION-HISTORY.md, SKILLS-USAGE-REPORT.md, PROJECT-INVENTORY.md)
- Phase 2: Templates created (5 phase templates, 3 deliverable templates)
- Phase 3: Project restructured (7 numbered directories, VERSION-HISTORY.md)
- Phase 4: Skill enhancement guides (2 enhancement documents, SKILLS-USAGE-GUIDE.md)
- Phase 5: Master workflow (COMPETITIVE-ANALYSIS-WORKFLOW.md)
- Phase 6: Quick iterations framework (QUICK-ITERATIONS-GUIDE.md, automation scripts)

**Step 2: Document what's ready for next project**

- Template location: `templates/competitive-analysis/`
- Copy command: `cp -r templates/competitive-analysis /path/to/new-project/`
- First steps: Follow README.md, use skills at each phase

**Step 3: Verify summary created**

```bash
grep "Phase [1-6]" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/IMPLEMENTATION-COMPLETE.md
```

**Verification Requirement:** Do not mark this task complete unless the verification output matches the expected output exactly.

---

## CHANGES MADE & WHY THEY MATTER

This section documents the upgrades made to the original Sonnet-generated plan:

### 1. Removed Time Estimates
**Original:** Included weekly timelines ("Week 1-2", "Duration: 4-8 weeks")
**Changed:** Removed all time-based references
**Why:** User explicitly prohibited time estimates. Focus on what needs doing, not when.

### 2. Split Large Tasks into Atomic Units
**Original:** Task 1.2 contained 200+ lines of markdown to write as one task
**Changed:** Split into Tasks 1.2, 1.3, 1.4, 1.5 (one iteration per task)
**Why:** `executing-plans` requires 2-5 minute tasks. Large tasks cause context overflow and make review checkpoints ineffective.

### 3. Unified Skill Invocation Syntax
**Original:** Mixed `@skill-name`, `Skill: skill-name`, `/superpowers:skill-name`
**Changed:** Documented unified syntax: `Skill: name` for custom skills, `/superpowers:name` for slash commands
**Why:** Consistency prevents invocation errors and confusion.

### 4. Made All File Paths Absolute
**Original:** Mixed absolute paths (`/Users/seancurrie/...`) with relative (`03-DELIVERABLES/`)
**Changed:** All paths are absolute or clearly relative to documented project root
**Why:** Eliminates "which directory am I in?" errors during execution.

### 5. Strengthened Verification Steps
**Original:** Verifications like `wc -l file` (just counts lines)
**Changed:** Verifications check actual content (`grep "specific content" file`)
**Why:** Line counts don't verify quality. Content checks confirm the right thing was created.

### 6. Separated THIS Project vs. TEMPLATE
**Original:** Blurred distinction between cleaning up Maia Learning project and creating reusable template
**Changed:** Phase 2 explicitly creates templates in `templates/competitive-analysis/`, Phase 3 explicitly restructures THIS project
**Why:** Clarity on what applies to current project vs. what's reusable prevents confusion.

### 7. Added Explicit Skill Integration at Task Level
**Original:** Skills mentioned in phase overviews but not at task level
**Changed:** Each task that uses a skill explicitly names it with invocation syntax
**Why:** Executor shouldn't have to remember phase-level context; task should be self-contained.

### 8. Removed Incomplete "Execution Options" Section
**Original:** Ended with "Which approach would you prefer?" question
**Changed:** Removed; plan is now ready for direct execution
**Why:** Plans should be executable, not conversational.

### 9. Added This Documentation Section
**Original:** No meta-documentation of changes
**Changed:** Added "Changes Made & Why They Matter" section
**Why:** Future iterations need to understand what was changed and why to avoid regression.

---

## INSTRUCTIONS FOR SONNET 4.5 WHEN ITERATING NEXT

When executing or iterating on this plan, follow these rules:

### Execution Rules

1. **Use `superpowers:executing-plans` skill.** This plan is designed for 3-task batch execution with review checkpoints.

2. **Each task is self-contained.** Do not look ahead to future tasks for context. Complete one task, verify, move to next.

3. **Verification steps are mandatory.** Do not skip verification commands. If verification fails, fix before proceeding.

4. **File paths are absolute.** Use paths exactly as written. Do not `cd` around unless the task explicitly requires it.

5. **When creating markdown files:** Write the actual content specified, not placeholder text. The descriptions in "Step 1:" sections are specifications, not templates.

- Under no circumstances may more than 3 tasks be executed in a batch, even if tasks appear small. Stop and wait for review before continuing.

### Skill Usage Rules

6. **Before any research phase work:** Invoke `Skill: competitive-research-brightdata`

7. **Before any QA phase work:** Invoke `Skill: competitive-analysis-quality-assurance`

8. **Before claiming any task complete:** Mentally run `superpowers:verification-before-completion` checklist (evidence before assertions)

9. **If requirements seem unclear:** Invoke `Skill: superpowers:brainstorming` to clarify before proceeding

### Content Quality Rules

10. **No marketing language.** When writing template content, use factual language only. No "revolutionary", "best-in-class", etc.

11. **All claims need citation format.** When documenting data points, use format: `(Source, YYYY)`

12. **Professional tone throughout.** These are enterprise deliverables. No emojis unless user specifically requests them.

### Error Recovery Rules

13. **If a bash command fails:** Check the error message, fix the issue, retry. Do not skip to next task.

14. **If a file already exists:** Read it first, then decide whether to append, overwrite, or skip based on content.

15. **If you're unsure about a specification:** Ask the user via `AskUserQuestion` rather than guessing.

### Progress Tracking Rules

16. **Use TodoWrite for every phase.** Create todos at phase start, mark in_progress during work, mark complete after verification.

17. **Report after each batch.** After completing 3 tasks, provide summary: what was done, what was verified, any issues encountered.

18. **Do not batch multiple file operations.** Write one file, verify, then write the next. This prevents cascading errors.

### Iteration-Specific Rules (for future updates to this plan)

19. **Preserve structure.** If updating this plan, maintain the 6-phase structure, task numbering, and section organization.

20. **Document changes.** Add to "Changes Made & Why They Matter" section when making significant modifications.

21. **Test before committing.** Any changes to automation scripts should be tested on a sample file before committing.

---

**Plan Version:** 2.0-UPGRADED
**Original Author:** Claude Sonnet 4.5 (via superpowers:writing-plans)
**Upgraded By:** Claude Opus 4 (Upgrade Agent role)
**Upgrade Date:** November 24, 2025
**Compatibility:** superpowers:executing-plans, 3-task batch execution
