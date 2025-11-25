# Maia Project Normalization & Skill Updates Implementation Plan

> **Execution Requirement:** All tasks in this plan must be executed strictly using `superpowers:executing-plans` in 3‑task batches. Verification is mandatory after each task and each batch. Do not proceed to the next task or batch until verification output matches the expected result exactly.

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task in 3-task batches with review checkpoints.

**Goal:** Normalize the MaiaLearningResearch repo into a clean "framework + project instance + archive" structure, implement concrete skill updates with version control, and establish a reliable repo→~/.claude sync mechanism.

**Architecture:** Multi-phase iterative approach with:
1. Safety rails and inventory (no destructive changes)
2. MAIA-PROJECT/ consolidation (moves only)
3. Archive creation for clutter
4. Reference/path updates across docs
5. Skill versioning in-repo with sync script
6. Concrete skill implementation updates
7. Skill testing and verification

**Tech Stack:**
- Bash (file operations, git)
- Python (install-skill.sh sync script)
- Markdown (documentation, skill definitions)
- Custom Claude Skills (competitive-analysis-quality-assurance, competitive-research-brightdata)

**Project Root:** `/Users/seancurrie/Desktop/MaiaLearningResearch`

**Target End-State:**
```
MaiaLearningResearch/
├── docs/                           # FRAMEWORK (unchanged)
├── templates/                      # FRAMEWORK (unchanged)
├── 06-AUTOMATION/                  # FRAMEWORK (unchanged)
├── skills/                         # NEW: Version-controlled skill definitions
│   └── local/
│       ├── competitive-analysis-quality-assurance/
│       └── competitive-research-brightdata/
├── scripts/                        # NEW: Utilities including install-skills.sh
├── MAIA-PROJECT/                   # Maia instance (all project-specific content)
│   ├── 00-PROJECT-OVERVIEW/
│   ├── 01-RESEARCH-INPUTS/
│   ├── 02-ANALYSIS-OUTPUTS/
│   ├── 03-DELIVERABLES/
│   ├── 04-QA-DOCUMENTATION/
│   ├── 05-ITERATIONS/
│   ├── 06-PROJECT-MANAGEMENT/
│   └── archive/
│       └── original-structure/
│           └── 05-FINAL-DELIVERABLES/
├── archive/                        # Root-level archive (clutter)
│   ├── legacy-scripts/
│   ├── temp-files/
│   ├── skill-artifacts/
│   └── regenerable/
├── README.md
└── .gitignore
```

---

## PHASE A: SAFETY RAILS & INVENTORY

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Establish safety nets and document current state before any moves.

### Task A.1: Create Safety Branch in Git

**Files:**
- Git operations only

**Step 1: Verify git status is clean**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
git status --porcelain
```

If output is non-empty, commit or stash changes first.

**Step 2: Create safety branch**

```bash
git branch pre-normalization-backup
git branch -v | grep pre-normalization-backup
```

**Verification:**

```bash
git branch | grep "pre-normalization-backup" && echo "SAFETY BRANCH CREATED"
```

**Expected Output:** Line containing `pre-normalization-backup` followed by `SAFETY BRANCH CREATED`

---

### Task A.2: Generate Complete File Inventory

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/plans/NORMALIZATION-INVENTORY.md`

**Step 1: Count files in each top-level directory**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
for dir in */; do
  count=$(find "$dir" -type f 2>/dev/null | wc -l | tr -d ' ')
  echo "- $dir: $count files"
done
```

**Step 2: Create inventory document**

Create `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/plans/NORMALIZATION-INVENTORY.md` with:
- Date and purpose header
- File counts per directory (from Step 1 output)
- List of root-level files to archive
- Total file count baseline

Include these specific counts that will be verified post-migration:
- Total files in numbered directories (00-06)
- Total files in 05-FINAL-DELIVERABLES/
- Total root-level .md, .py, .js files

**Verification:**

```bash
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/docs/plans/NORMALIZATION-INVENTORY.md && \
grep "File Counts" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/plans/NORMALIZATION-INVENTORY.md && \
echo "INVENTORY CREATED"
```

**Expected Output:** `File Counts` line followed by `INVENTORY CREATED`

---

### Task A.3: Create Target Directory Structure

**Files:**
- Create directories: `MAIA-PROJECT/`, `archive/`, `skills/local/`, `scripts/`

**Step 1: Create MAIA-PROJECT structure**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mkdir -p MAIA-PROJECT/{00-PROJECT-OVERVIEW,01-RESEARCH-INPUTS,02-ANALYSIS-OUTPUTS,03-DELIVERABLES,04-QA-DOCUMENTATION,05-ITERATIONS,06-PROJECT-MANAGEMENT}
mkdir -p MAIA-PROJECT/archive/original-structure
```

**Step 2: Create archive structure**

```bash
mkdir -p archive/{legacy-scripts,temp-files,skill-artifacts,regenerable}
```

**Step 3: Create skills and scripts structure**

```bash
mkdir -p skills/local/{competitive-analysis-quality-assurance,competitive-research-brightdata}
mkdir -p scripts
```

**Verification:**

```bash
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/03-DELIVERABLES && \
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/archive/legacy-scripts && \
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local && \
echo "ALL TARGET DIRECTORIES CREATED"
```

**Expected Output:** `ALL TARGET DIRECTORIES CREATED`

---

## PHASE B: MOVE MAIA RESEARCH DIRECTORIES

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Move all Maia-specific research/analysis directories into MAIA-PROJECT/.

### Task B.1: Move Project Overview and Company Profiles

**Files:**
- Move: `00-PROJECT-OVERVIEW/` → `MAIA-PROJECT/00-PROJECT-OVERVIEW/`
- Move: `00-PROJECT-MANAGEMENT/` → `MAIA-PROJECT/` (merge into existing)
- Move: `01-COMPANY-PROFILES/` → `MAIA-PROJECT/01-RESEARCH-INPUTS/company-profiles/`

**Step 1: Move 00-PROJECT-OVERVIEW**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mv 00-PROJECT-OVERVIEW/* MAIA-PROJECT/00-PROJECT-OVERVIEW/ 2>/dev/null || true
rmdir 00-PROJECT-OVERVIEW 2>/dev/null || true
```

**Step 2: Move 00-PROJECT-MANAGEMENT contents**

```bash
mv 00-PROJECT-MANAGEMENT/* MAIA-PROJECT/00-PROJECT-OVERVIEW/ 2>/dev/null || true
rmdir 00-PROJECT-MANAGEMENT 2>/dev/null || true
```

**Step 3: Move 01-COMPANY-PROFILES**

```bash
mkdir -p MAIA-PROJECT/01-RESEARCH-INPUTS/company-profiles
mv 01-COMPANY-PROFILES/* MAIA-PROJECT/01-RESEARCH-INPUTS/company-profiles/ 2>/dev/null || true
rmdir 01-COMPANY-PROFILES 2>/dev/null || true
```

**Verification:**

```bash
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/01-RESEARCH-INPUTS/company-profiles && \
! test -d /Users/seancurrie/Desktop/MaiaLearningResearch/01-COMPANY-PROFILES && \
echo "B.1 COMPLETE"
```

**Expected Output:** `B.1 COMPLETE`

---

### Task B.2: Move Competitor Profiles and Raw Research

**Files:**
- Move: `02-COMPETITOR-PROFILES/` → `MAIA-PROJECT/01-RESEARCH-INPUTS/competitor-profiles/`
- Move: `02-RAW-RESEARCH-DATA/` → `MAIA-PROJECT/01-RESEARCH-INPUTS/raw-data/`
- Move: `01-RESEARCH-INPUTS/` → merge into `MAIA-PROJECT/01-RESEARCH-INPUTS/`

**Step 1: Move 02-COMPETITOR-PROFILES**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mkdir -p MAIA-PROJECT/01-RESEARCH-INPUTS/competitor-profiles
mv 02-COMPETITOR-PROFILES/* MAIA-PROJECT/01-RESEARCH-INPUTS/competitor-profiles/ 2>/dev/null || true
rmdir 02-COMPETITOR-PROFILES 2>/dev/null || true
```

**Step 2: Move 02-RAW-RESEARCH-DATA**

```bash
mkdir -p MAIA-PROJECT/01-RESEARCH-INPUTS/raw-data
mv 02-RAW-RESEARCH-DATA/* MAIA-PROJECT/01-RESEARCH-INPUTS/raw-data/ 2>/dev/null || true
rmdir 02-RAW-RESEARCH-DATA 2>/dev/null || true
```

**Step 3: Merge existing 01-RESEARCH-INPUTS**

```bash
mv 01-RESEARCH-INPUTS/* MAIA-PROJECT/01-RESEARCH-INPUTS/ 2>/dev/null || true
rmdir 01-RESEARCH-INPUTS 2>/dev/null || true
```

**Verification:**

```bash
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/01-RESEARCH-INPUTS/competitor-profiles && \
! test -d /Users/seancurrie/Desktop/MaiaLearningResearch/02-COMPETITOR-PROFILES && \
echo "B.2 COMPLETE"
```

**Expected Output:** `B.2 COMPLETE`

---

### Task B.3: Move Analysis Directories

**Files:**
- Move: `02-ANALYSIS-OUTPUTS/` → merge into `MAIA-PROJECT/02-ANALYSIS-OUTPUTS/`
- Move: `03-COMPARATIVE-ANALYSIS/` → `MAIA-PROJECT/02-ANALYSIS-OUTPUTS/comparative-analysis/`
- Move: `04-STRATEGIC-INSIGHTS/` → `MAIA-PROJECT/02-ANALYSIS-OUTPUTS/strategic-insights/`

**Step 1: Merge 02-ANALYSIS-OUTPUTS**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mv 02-ANALYSIS-OUTPUTS/* MAIA-PROJECT/02-ANALYSIS-OUTPUTS/ 2>/dev/null || true
rmdir 02-ANALYSIS-OUTPUTS 2>/dev/null || true
```

**Step 2: Move 03-COMPARATIVE-ANALYSIS**

```bash
mkdir -p MAIA-PROJECT/02-ANALYSIS-OUTPUTS/comparative-analysis
mv 03-COMPARATIVE-ANALYSIS/* MAIA-PROJECT/02-ANALYSIS-OUTPUTS/comparative-analysis/ 2>/dev/null || true
rmdir 03-COMPARATIVE-ANALYSIS 2>/dev/null || true
```

**Step 3: Move 04-STRATEGIC-INSIGHTS**

```bash
mkdir -p MAIA-PROJECT/02-ANALYSIS-OUTPUTS/strategic-insights
mv 04-STRATEGIC-INSIGHTS/* MAIA-PROJECT/02-ANALYSIS-OUTPUTS/strategic-insights/ 2>/dev/null || true
rmdir 04-STRATEGIC-INSIGHTS 2>/dev/null || true
```

**Verification:**

```bash
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/02-ANALYSIS-OUTPUTS/comparative-analysis && \
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/02-ANALYSIS-OUTPUTS/strategic-insights && \
! test -d /Users/seancurrie/Desktop/MaiaLearningResearch/03-COMPARATIVE-ANALYSIS && \
echo "B.3 COMPLETE"
```

**Expected Output:** `B.3 COMPLETE`

---

## PHASE C: MOVE DELIVERABLES & LEGACY SNAPSHOT

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Move deliverables directories and preserve 05-FINAL-DELIVERABLES intact as legacy snapshot.

### Task C.1: Move Current Deliverables

**Files:**
- Move: `03-DELIVERABLES/` → `MAIA-PROJECT/03-DELIVERABLES/`

**Step 1: Move 03-DELIVERABLES with all contents**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mv 03-DELIVERABLES/* MAIA-PROJECT/03-DELIVERABLES/ 2>/dev/null || true
rmdir 03-DELIVERABLES 2>/dev/null || true
```

**Step 2: Verify current/ subdirectory moved**

```bash
ls MAIA-PROJECT/03-DELIVERABLES/current/
```

**Verification:**

```bash
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/03-DELIVERABLES/current && \
! test -d /Users/seancurrie/Desktop/MaiaLearningResearch/03-DELIVERABLES && \
echo "C.1 COMPLETE"
```

**Expected Output:** `C.1 COMPLETE`

---

### Task C.2: Move 05-FINAL-DELIVERABLES as Intact Snapshot

**Files:**
- Move: `05-FINAL-DELIVERABLES/` → `MAIA-PROJECT/archive/original-structure/05-FINAL-DELIVERABLES/`

**Step 1: Count files before move**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
find 05-FINAL-DELIVERABLES -type f | wc -l
```

Record this count for verification.

**Step 2: Move entire directory intact**

```bash
mv 05-FINAL-DELIVERABLES MAIA-PROJECT/archive/original-structure/
```

**Step 3: Count files after move**

```bash
find MAIA-PROJECT/archive/original-structure/05-FINAL-DELIVERABLES -type f | wc -l
```

**Verification:**

```bash
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/archive/original-structure/05-FINAL-DELIVERABLES && \
! test -d /Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES && \
echo "C.2 COMPLETE"
```

**Expected Output:** `C.2 COMPLETE`

---

### Task C.3: Move Empty 05-DELIVERABLES and QA/Iteration Directories

**Files:**
- Move: `05-DELIVERABLES/` → remove if empty, or move to archive
- Move: `04-QA-DOCUMENTATION/` → `MAIA-PROJECT/04-QA-DOCUMENTATION/`
- Move: `05-ITERATIONS/` → `MAIA-PROJECT/05-ITERATIONS/`

**Step 1: Handle 05-DELIVERABLES (likely empty)**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
rmdir 05-DELIVERABLES 2>/dev/null || mv 05-DELIVERABLES MAIA-PROJECT/archive/original-structure/05-DELIVERABLES-LEGACY 2>/dev/null || true
```

**Step 2: Move 04-QA-DOCUMENTATION**

```bash
mv 04-QA-DOCUMENTATION/* MAIA-PROJECT/04-QA-DOCUMENTATION/ 2>/dev/null || true
rmdir 04-QA-DOCUMENTATION 2>/dev/null || true
```

**Step 3: Move 05-ITERATIONS**

```bash
mv 05-ITERATIONS/* MAIA-PROJECT/05-ITERATIONS/ 2>/dev/null || true
rmdir 05-ITERATIONS 2>/dev/null || true
```

**Verification:**

```bash
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/04-QA-DOCUMENTATION && \
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/05-ITERATIONS && \
! test -d /Users/seancurrie/Desktop/MaiaLearningResearch/05-ITERATIONS && \
echo "C.3 COMPLETE"
```

**Expected Output:** `C.3 COMPLETE`

---

## PHASE D: MOVE PROJECT MANAGEMENT & TEST FILES

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Move remaining Maia-specific directories to MAIA-PROJECT/.

### Task D.1: Move 06-PROJECT-MANAGEMENT

**Files:**
- Move: `06-PROJECT-MANAGEMENT/` → `MAIA-PROJECT/06-PROJECT-MANAGEMENT/`

**Step 1: Move directory**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mv 06-PROJECT-MANAGEMENT/* MAIA-PROJECT/06-PROJECT-MANAGEMENT/ 2>/dev/null || true
rmdir 06-PROJECT-MANAGEMENT 2>/dev/null || true
```

**Verification:**

```bash
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/06-PROJECT-MANAGEMENT && \
! test -d /Users/seancurrie/Desktop/MaiaLearningResearch/06-PROJECT-MANAGEMENT && \
echo "D.1 COMPLETE"
```

**Expected Output:** `D.1 COMPLETE`

---

### Task D.2: Move Test Directory to QA Documentation

**Files:**
- Move: `test/` → `MAIA-PROJECT/04-QA-DOCUMENTATION/test-files/`

**Step 1: Move test directory**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mkdir -p MAIA-PROJECT/04-QA-DOCUMENTATION/test-files
mv test/* MAIA-PROJECT/04-QA-DOCUMENTATION/test-files/ 2>/dev/null || true
rmdir test 2>/dev/null || true
```

**Verification:**

```bash
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/04-QA-DOCUMENTATION/test-files && \
! test -d /Users/seancurrie/Desktop/MaiaLearningResearch/test && \
echo "D.2 COMPLETE"
```

**Expected Output:** `D.2 COMPLETE`

---

### Task D.3: Move PROGRESS-REPORTS to MAIA-PROJECT

**Files:**
- Move: `PROGRESS-REPORTS/` → `MAIA-PROJECT/06-PROJECT-MANAGEMENT/progress-reports/`

**Step 1: Move directory**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mkdir -p MAIA-PROJECT/06-PROJECT-MANAGEMENT/progress-reports
mv PROGRESS-REPORTS/* MAIA-PROJECT/06-PROJECT-MANAGEMENT/progress-reports/ 2>/dev/null || true
rmdir PROGRESS-REPORTS 2>/dev/null || true
```

**Verification:**

```bash
! test -d /Users/seancurrie/Desktop/MaiaLearningResearch/PROGRESS-REPORTS && \
echo "D.3 COMPLETE"
```

**Expected Output:** `D.3 COMPLETE`

---

## PHASE E: ARCHIVE ROOT-LEVEL CLUTTER

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Move root-level scripts, temp files, and skill artifacts to archive/.

### Task E.1: Archive Legacy Scripts

**Files:**
- Move: `convert-to-docx.js`, `fix-scoir-pricing.py`, `search-scoir-pricing.py` → `archive/legacy-scripts/`
- Move: `scripts/` directory (pre-normalization snapshot) → `archive/legacy-scripts/project-scripts-pre-normalization/` (then recreate clean scripts/ at root)

**Step 1: Move root-level scripts**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mv convert-to-docx.js archive/legacy-scripts/ 2>/dev/null || true
mv fix-scoir-pricing.py archive/legacy-scripts/ 2>/dev/null || true
mv search-scoir-pricing.py archive/legacy-scripts/ 2>/dev/null || true
```

**Step 2: Move scripts directory**

```bash
# Preserve pre-normalization project scripts as a snapshot
mv scripts archive/legacy-scripts/project-scripts-pre-normalization 2>/dev/null || true

# Recreate a clean root scripts/ directory for framework utilities created later in this plan
mkdir -p scripts
```

**Verification:**

```bash
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/archive/legacy-scripts/convert-to-docx.js && \
! test -f /Users/seancurrie/Desktop/MaiaLearningResearch/convert-to-docx.js && \
echo "E.1 COMPLETE"
```

**Expected Output:** `E.1 COMPLETE`

---

### Task E.2: Archive Temp Files

**Files:**
- Move: `temp-*.md` files → `archive/temp-files/`
- Move: `temp-market-positioning-unpacked/` → `archive/temp-files/`
- Move: `EXECUTION-RESULTS.txt` → `archive/temp-files/`

**Step 1: Move temp markdown files**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mv temp-feature-matrix.md archive/temp-files/ 2>/dev/null || true
mv temp-market-positioning.md archive/temp-files/ 2>/dev/null || true
mv temp-pricing-analysis.md archive/temp-files/ 2>/dev/null || true
mv temp-target-segments.md archive/temp-files/ 2>/dev/null || true
mv temp-tech-stack.md archive/temp-files/ 2>/dev/null || true
```

**Step 2: Move temp directories and other files**

```bash
mv temp-market-positioning-unpacked archive/temp-files/ 2>/dev/null || true
mv EXECUTION-RESULTS.txt archive/temp-files/ 2>/dev/null || true
```

**Verification:**

```bash
! test -f /Users/seancurrie/Desktop/MaiaLearningResearch/temp-feature-matrix.md && \
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/archive/temp-files/temp-feature-matrix.md && \
echo "E.2 COMPLETE"
```

**Expected Output:** `E.2 COMPLETE`

---

### Task E.3: Archive Skill Artifacts and Regenerable Items

**Files:**
- Move: `temp_skill_extract/` → `archive/skill-artifacts/`
- Move: `competitive-analysis-quality-assurance/` → `archive/skill-artifacts/`
- Move: `competitive-research-brightdata.skill` → `archive/skill-artifacts/`
- Move: `node_modules/`, `package.json`, `package-lock.json` → `archive/regenerable/`

**Step 1: Move skill artifacts**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mv temp_skill_extract archive/skill-artifacts/ 2>/dev/null || true
mv competitive-analysis-quality-assurance archive/skill-artifacts/ 2>/dev/null || true
mv competitive-research-brightdata.skill archive/skill-artifacts/ 2>/dev/null || true
```

**Step 2: Move regenerable Node artifacts**

```bash
mv node_modules archive/regenerable/ 2>/dev/null || true
mv package.json archive/regenerable/ 2>/dev/null || true
mv package-lock.json archive/regenerable/ 2>/dev/null || true
```

**Verification:**

```bash
! test -d /Users/seancurrie/Desktop/MaiaLearningResearch/node_modules && \
test -d /Users/seancurrie/Desktop/MaiaLearningResearch/archive/regenerable/node_modules && \
echo "E.3 COMPLETE"
```

**Expected Output:** `E.3 COMPLETE`

---

## PHASE F: ARCHIVE REMAINING ROOT FILES

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Archive remaining Maia-specific markdown files from root.

### Task F.1: Archive Root Markdown Files

**Files:**
- Move: `DOCUMENTATION-CLEANUP-SUMMARY.md` → `archive/`
- Move: `RESEARCH-QA-SKILL-SUMMARY.md` → `archive/`
- Keep: `README.md`, `CLAUDE.md` at root (framework-level)

**Step 1: Move Maia-specific markdown files**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
mv DOCUMENTATION-CLEANUP-SUMMARY.md archive/ 2>/dev/null || true
mv RESEARCH-QA-SKILL-SUMMARY.md archive/ 2>/dev/null || true
```

**Verification:**

```bash
! test -f /Users/seancurrie/Desktop/MaiaLearningResearch/DOCUMENTATION-CLEANUP-SUMMARY.md && \
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/archive/DOCUMENTATION-CLEANUP-SUMMARY.md && \
echo "F.1 COMPLETE"
```

**Expected Output:** `F.1 COMPLETE`

---

### Task F.2: Create Archive README

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/archive/README.md`

**Step 1: Write archive README**

Create `/Users/seancurrie/Desktop/MaiaLearningResearch/archive/README.md` with:

```markdown
# Archive Directory

This directory contains files archived during the November 2025 repository normalization.

## Contents

### legacy-scripts/
One-off scripts created during the Maia Learning project that are no longer needed for framework operation:
- `convert-to-docx.js` - DOCX conversion utility
- `fix-scoir-pricing.py` - Pricing correction script
- `search-scoir-pricing.py` - Pricing search utility
- `project-scripts/` - Original scripts directory

### temp-files/
Temporary working files from analysis phases:
- `temp-*.md` - Working markdown files
- `temp-market-positioning-unpacked/` - Extracted files
- `EXECUTION-RESULTS.txt` - Execution logs

### skill-artifacts/
Skill development artifacts (skill definitions now live in `skills/local/`):
- `temp_skill_extract/` - Extracted skill documentation
- `competitive-analysis-quality-assurance/` - Old skill registration files
- `competitive-research-brightdata.skill` - Original skill file

### regenerable/
Node.js artifacts that can be regenerated with `npm install`:
- `node_modules/`
- `package.json`
- `package-lock.json`

## When to Access

These files are preserved for forensic and reference purposes. They are not needed for:
- Running the competitive analysis framework
- Starting new projects
- Updating skills

Access only when investigating historical decisions or recovering specific utilities.

---

**Archived:** November 25, 2025
**Reason:** Repository normalization to separate framework from project instance
```

**Verification:**

```bash
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/archive/README.md && \
grep "legacy-scripts" /Users/seancurrie/Desktop/MaiaLearningResearch/archive/README.md && \
echo "F.2 COMPLETE"
```

**Expected Output:** `legacy-scripts` line followed by `F.2 COMPLETE`

---

### Task F.3: Create MAIA-PROJECT README

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/README.md`

**Step 1: Write MAIA-PROJECT README**

Create `/Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/README.md` with:

```markdown
# Maia Learning Competitive Analysis Project

This directory contains all project-specific assets for the Maia Learning competitive analysis conducted September-November 2025.

## Project Status

**Version:** 2.0 (US-Primary Strategy Edition)
**Quality Score:** 9.5/10
**Status:** Client-Ready

## Directory Structure

```
MAIA-PROJECT/
├── 00-PROJECT-OVERVIEW/      # Project scope, objectives, stakeholders
├── 01-RESEARCH-INPUTS/       # All research data
│   ├── company-profiles/     # Maia Learning profile
│   ├── competitor-profiles/  # 7 competitor deep-dives
│   └── raw-data/             # Search results, scraped content
├── 02-ANALYSIS-OUTPUTS/      # Analysis working files
│   ├── comparative-analysis/ # Feature matrices, pricing, positioning
│   └── strategic-insights/   # SWOT, recommendations
├── 03-DELIVERABLES/          # Client-ready deliverables
│   └── current/              # V2.0 canonical files (DOCX/HTML/PDF)
├── 04-QA-DOCUMENTATION/      # QA reports, change logs
│   └── test-files/           # QA test corpus
├── 05-ITERATIONS/            # Iteration documentation
├── 06-PROJECT-MANAGEMENT/    # Project tracking, methodology
└── archive/
    └── original-structure/
        └── 05-FINAL-DELIVERABLES/  # Preserved legacy structure
```

## Canonical Deliverables

The canonical V2.0 deliverables are located at:

```
MAIA-PROJECT/03-DELIVERABLES/current/
├── DOCX/
│   ├── executive-summary-CORRECTED.docx
│   └── full-report-CORRECTED.docx
├── HTML/
│   ├── executive-summary-CORRECTED.html
│   ├── full-report-CORRECTED.html
│   └── visualizations/
└── PDF/
    ├── executive-summary-CORRECTED.pdf
    ├── full-report-CORRECTED.pdf
    └── visualizations/ (10 ENTERPRISE PDFs)
```

## Using This as a Reference

This project instance demonstrates the competitive analysis framework in action. To start a new project:

1. Copy `templates/competitive-analysis/` to a new location
2. Follow `docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`
3. Reference this MAIA-PROJECT for examples of completed deliverables

## Version History

- **V2.0** (Nov 24, 2025): US-Primary strategy, four-quadrant positioning maps, taglines removed
- **V1.0** (Nov 2025): QA corrections, 100+ citations added, pricing fixes
- **V0.9** (Sep-Oct 2025): Initial deliverables

---

**Project Owner:** Sean Currie
**Analysis Period:** September-November 2025
**Framework Version:** 1.0
```

**Verification:**

```bash
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/README.md && \
grep "Canonical Deliverables" /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/README.md && \
echo "F.3 COMPLETE"
```

**Expected Output:** `Canonical Deliverables` line followed by `F.3 COMPLETE`

---

## PHASE G: UPDATE PATH REFERENCES

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Update documentation references that point to old paths.

### Task G.1: Update docs/COMPETITIVE-ANALYSIS-WORKFLOW.md References

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/QUICK-ITERATIONS-GUIDE.md`
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/guides/SKILLS-USAGE-GUIDE.md`

**Step 1: Read current file and identify path references**

Read the file and look for references to:
- `03-DELIVERABLES/current/`
- `05-FINAL-DELIVERABLES/`
- Old numbered directories

**Step 2: Update references**

Update any hardcoded commands/paths that assume the repo-root deliverables path (e.g., 03-DELIVERABLES/current/) so they either (a) use a placeholder like [PROJECT]/03-DELIVERABLES/current/ OR (b) mention both patterns: 03-DELIVERABLES/current/ (new projects) and MAIA-PROJECT/03-DELIVERABLES/current/ (this repo’s example instance).

For framework documentation, prefer generic references like:
- `[PROJECT]/03-DELIVERABLES/current/` rather than `MAIA-PROJECT/03-DELIVERABLES/current/`

Add a note near the top:

```markdown
> **Note:** For the Maia Learning project instance, all project-specific files are located under `MAIA-PROJECT/`. For new projects, follow the directory structure in `templates/competitive-analysis/`.
```

**Verification:**

```bash
grep -c "MAIA-PROJECT\|templates/competitive-analysis" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/COMPETITIVE-ANALYSIS-WORKFLOW.md
```

**Expected Output:** At least `1` (confirming reference added)

---

### Task G.2: Update templates/competitive-analysis/README.md References

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/README.md`

**Step 1: Add reference to Maia example project**

Add a section near the end:

```markdown
---

## Example Project

For a complete example of this framework in action, see the Maia Learning project:

- **Location:** `MAIA-PROJECT/` in the repository root
- **Deliverables:** `MAIA-PROJECT/03-DELIVERABLES/current/`
- **Documentation:** `MAIA-PROJECT/README.md`

This project demonstrates V2.0 quality deliverables (9.5/10) achieved through the full workflow.
```

**Verification:**

```bash
grep "Example Project" /Users/seancurrie/Desktop/MaiaLearningResearch/templates/competitive-analysis/README.md && \
echo "G.2 COMPLETE"
```

**Expected Output:** `Example Project` line followed by `G.2 COMPLETE`

---

### Task G.3: Update docs/PROJECT-INVENTORY.md with New Structure

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/PROJECT-INVENTORY.md`

**Step 1: Add deprecation notice and new structure reference**

Add at the top of the file:

```markdown
> **NOTICE:** This inventory reflects the pre-normalization structure. As of November 25, 2025, the repository has been reorganized:
> - All Maia-specific files are now under `MAIA-PROJECT/`
> - Legacy files are in `archive/`
> - See `MAIA-PROJECT/README.md` for current deliverables location
```

**Step 2: Add new structure section at end**

Add:

```markdown
---

## Post-Normalization Structure (November 25, 2025)

```
MaiaLearningResearch/
├── docs/                    # Framework documentation
├── templates/               # Reusable templates
├── 06-AUTOMATION/           # Framework automation scripts
├── skills/local/            # Version-controlled skill definitions
├── scripts/                 # Utility scripts
├── MAIA-PROJECT/            # Maia Learning project instance
└── archive/                 # Archived files
```

For current file locations, see `MAIA-PROJECT/README.md`.
```

**Verification:**

```bash
grep "Post-Normalization Structure" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/PROJECT-INVENTORY.md && \
echo "G.3 COMPLETE"
```

**Expected Output:** `Post-Normalization Structure` line followed by `G.3 COMPLETE`

---

## PHASE H: SKILL VERSION CONTROL SETUP

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Copy current skill definitions to repo and create install script.

### Task H.1: Copy QA Skill to Repo

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md`

**Step 1: Copy current skill definition**

```bash
cp ~/.claude/skills/competitive-analysis-quality-assurance/SKILL.md \
   /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md
```

**Verification:**

```bash
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md && \
head -5 /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md | grep "competitive-analysis-quality-assurance" && \
echo "H.1 COMPLETE"
```

**Expected Output:** Line containing `competitive-analysis-quality-assurance` followed by `H.1 COMPLETE`

---

### Task H.2: Copy Research Skill to Repo

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md`

**Step 1: Copy current skill definition**

```bash
cp ~/.claude/skills/competitive-research-brightdata/SKILL.md \
   /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md
```

**Verification:**

```bash
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md && \
head -5 /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md | grep "competitive-research-brightdata" && \
echo "H.2 COMPLETE"
```

**Expected Output:** Line containing `competitive-research-brightdata` followed by `H.2 COMPLETE`

---

### Task H.3: Create Install Script

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/scripts/install-skills.sh`

**Step 1: Write install script**

Create `/Users/seancurrie/Desktop/MaiaLearningResearch/scripts/install-skills.sh` with:

```bash
# Ensure scripts/ exists (it may have been archived and recreated earlier)
mkdir -p /Users/seancurrie/Desktop/MaiaLearningResearch/scripts

```bash
#!/bin/bash
# install-skills.sh - Sync skill definitions from repo to ~/.claude/skills/
#
# Usage: ./install-skills.sh [--dry-run] [--backup]
#
# Options:
#   --dry-run   Show what would be done without making changes
#   --backup    Create timestamped backups before overwriting
#
# This script copies skill definitions from skills/local/ to ~/.claude/skills/
# The repo is the source of truth; this script pushes changes to the active location.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SKILLS_SOURCE="$REPO_ROOT/skills/local"
SKILLS_TARGET="$HOME/.claude/skills"

DRY_RUN=false
BACKUP=false

# Parse arguments
for arg in "$@"; do
    case $arg in
        --dry-run)
            DRY_RUN=true
            ;;
        --backup)
            BACKUP=true
            ;;
        *)
            echo "Unknown option: $arg"
            echo "Usage: ./install-skills.sh [--dry-run] [--backup]"
            exit 1
            ;;
    esac
done

echo "=== Skill Installation Script ==="
echo "Source: $SKILLS_SOURCE"
echo "Target: $SKILLS_TARGET"
echo "Dry run: $DRY_RUN"
echo "Backup: $BACKUP"
echo ""

# Check source exists
if [ ! -d "$SKILLS_SOURCE" ]; then
    echo "ERROR: Source directory not found: $SKILLS_SOURCE"
    exit 1
fi

# Create target if needed
if [ ! -d "$SKILLS_TARGET" ]; then
    if [ "$DRY_RUN" = true ]; then
        echo "[DRY RUN] Would create: $SKILLS_TARGET"
    else
        mkdir -p "$SKILLS_TARGET"
        echo "Created: $SKILLS_TARGET"
    fi
fi

# Process each skill
for skill_dir in "$SKILLS_SOURCE"/*/; do
    skill_name=$(basename "$skill_dir")
    source_file="$skill_dir/SKILL.md"
    target_dir="$SKILLS_TARGET/$skill_name"
    target_file="$target_dir/SKILL.md"

    if [ ! -f "$source_file" ]; then
        echo "SKIP: No SKILL.md found in $skill_dir"
        continue
    fi

    echo "Processing: $skill_name"

    # Backup if requested and target exists
    if [ "$BACKUP" = true ] && [ -f "$target_file" ]; then
        backup_file="${target_file}.backup.$(date +%Y%m%d-%H%M%S)"
        if [ "$DRY_RUN" = true ]; then
            echo "  [DRY RUN] Would backup: $target_file -> $backup_file"
        else
            cp "$target_file" "$backup_file"
            echo "  Backed up: $backup_file"
        fi
    fi

    # Create target directory if needed
    if [ ! -d "$target_dir" ]; then
        if [ "$DRY_RUN" = true ]; then
            echo "  [DRY RUN] Would create directory: $target_dir"
        else
            mkdir -p "$target_dir"
            echo "  Created directory: $target_dir"
        fi
    fi

    # Copy skill file
    if [ "$DRY_RUN" = true ]; then
        echo "  [DRY RUN] Would copy: $source_file -> $target_file"
    else
        cp "$source_file" "$target_file"
        echo "  Installed: $target_file"
    fi
done

echo ""
echo "=== Installation Complete ==="

# Verification
echo ""
echo "Verification:"
for skill_dir in "$SKILLS_SOURCE"/*/; do
    skill_name=$(basename "$skill_dir")
    target_file="$SKILLS_TARGET/$skill_name/SKILL.md"
    if [ -f "$target_file" ]; then
        echo "  ✓ $skill_name installed"
    else
        echo "  ✗ $skill_name NOT installed"
    fi
done
```

**Step 2: Make executable**

```bash
chmod +x /Users/seancurrie/Desktop/MaiaLearningResearch/scripts/install-skills.sh
```

**Verification:**

```bash
test -x /Users/seancurrie/Desktop/MaiaLearningResearch/scripts/install-skills.sh && \
grep "Skill Installation Script" /Users/seancurrie/Desktop/MaiaLearningResearch/scripts/install-skills.sh && \
echo "H.3 COMPLETE"
```

**Expected Output:** `Skill Installation Script` line followed by `H.3 COMPLETE`

---

## PHASE I: UPDATE QA SKILL WITH ENHANCEMENTS

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Implement concrete enhancements to the QA skill definition.

### Task I.1: Add Source Attribution Verification to QA Skill

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md`

**Step 1: Add new section after "Phase 5: Consistency Analysis"**

Insert the following section:

```markdown
### Phase 5.5: Source Attribution Verification

**Objective:** Verify that all numeric claims and key facts have proper citations.

**Citation Format Requirements:**

All claims of the following types MUST have inline citations in the format `(Source, YYYY)`:

1. **Pricing Claims:** Any `$X` or `$X-Y` figure
   - Example: "Naviance pricing ranges from $8-12 per student (PowerSchool, 2024)"

2. **Market Share:** Any `X%` market or share claim
   - Example: "SCOIR holds approximately 12% market share (EdTech Analysis, 2024)"

3. **Customer Counts:** Any "X schools" or "X students" claim
   - Example: "serving over 2,400 schools (SCOIR, 2024)"

4. **Funding Amounts:** Any `$XM` or `$XB` funding claim
   - Example: "raised $42M in Series C (Crunchbase, 2023)"

5. **Satisfaction Ratings:** Any `X/5` or `X.X/10` rating
   - Example: "rated 4.6/5 on G2 (G2, November 2024)"

6. **Growth Rates:** Any `X% growth` claim
   - Example: "40% year-over-year growth (Company Report, 2024)"

**Verification Process:**

1. Scan document for numeric patterns (regex: `\$[\d,]+`, `\d+%`, `\d+/\d+`, etc.)
2. For each match, check if `(Source, YYYY)` appears within 100 characters
3. Flag uncited claims for review
4. Generate compliance report

**Citation Compliance Report Format:**

```
## Citation Compliance Check

**Document:** [filename]
**Date:** [review date]

### Summary
- Total numeric claims found: X
- Claims with proper citations: Y (Z%)
- Claims missing citations: N

### Uncited Claims Requiring Attention

| Line | Claim | Type | Recommendation |
|------|-------|------|----------------|
| 45 | "$4.80 per student" | Pricing | Add source citation |
| 112 | "12% market share" | Market Share | Add source citation |

### Properly Cited Examples
[List 2-3 good examples as reference]
```

**Integration with Workflow:**
- Run citation check BEFORE comprehensive fact-checking
- Use findings to prioritize which claims need source verification
- Include citation compliance score in final QA report
```

**Verification:**

```bash
grep "Source Attribution Verification" /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md && \
grep "Citation Compliance Report" /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md && \
echo "I.1 COMPLETE"
```

**Expected Output:** Two grep matches followed by `I.1 COMPLETE`

---

### Task I.2: Add Marketing Language Detection to QA Skill

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md`

**Step 1: Add new section after "Phase 5.5: Source Attribution Verification"**

Insert the following section:

```markdown
### Phase 5.6: Marketing Language Detection

**Objective:** Identify and flag subjective or marketing language that reduces analytical credibility.

**Red Flag Word Categories:**

**Category 1: Superlatives (Remove or Cite)**
- best, leading, top, premier, #1, first
- revolutionary, game-changing, breakthrough
- only, unique, exclusive (unless verifiable)
- most, fastest, largest (without data)

**Category 2: Subjective Intensifiers (Soften or Remove)**
- clearly, obviously, certainly, definitely
- significantly, dramatically, massively
- amazing, incredible, exceptional, outstanding
- absolutely, totally, completely

**Category 3: Marketing Phrases (Replace with Factual)**
- "industry leader" → "among the larger players" or cite market share
- "best-in-class" → describe specific capability
- "world-class" → cite recognition or award
- "trusted by" → cite customer count with source
- "preferred by" → cite survey or market data

**Detection Process:**

1. Case-insensitive scan for red flag words/phrases
2. Extract context (full sentence containing the word)
3. Classify finding: MUST REMOVE | NEEDS CITATION | SOFTEN
4. Generate replacement suggestions

**Marketing Language Report Format:**

```
## Marketing Language Scan

**Document:** [filename]
**Red Flags Found:** X

### Must Remove
| Line | Original | Issue | Suggested Replacement |
|------|----------|-------|----------------------|
| 23 | "revolutionary AI capabilities" | Superlative | "advanced AI capabilities" |
| 89 | "best-in-class support" | Marketing phrase | "highly-rated support (G2, 4.5/5)" |

### Needs Citation
| Line | Claim | Required Evidence |
|------|-------|-------------------|
| 45 | "industry leader" | Market share data or analyst ranking |

### Soften Language
| Line | Original | Suggested |
|------|----------|-----------|
| 112 | "clearly dominates" | "leads in" |
| 156 | "dramatically improved" | "improved by X%" |
```

**Quality Standard:**
- Enterprise deliverables should have ZERO uncited superlatives
- All comparative claims should have supporting data
- Tone should be analytical, not promotional

**Integration with Workflow:**
- Run marketing scan during document analysis phase
- Address findings before fact-checking (saves time on claims that will be removed)
- Include marketing language score in final QA report
```

**Verification:**

```bash
grep "Marketing Language Detection" /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md && \
grep "Red Flag Word Categories" /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md && \
echo "I.2 COMPLETE"
```

**Expected Output:** Two grep matches followed by `I.2 COMPLETE`

---

### Task I.3: Add Path Discovery and Cross-Document Consistency to QA Skill

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md`

**Step 1: Update "Typical Project Structure" section**

Replace the existing "Typical Project Structure" section with:

```markdown
## Typical Project Structure

When working with competitive research projects, documents are typically organized in one of these patterns:

**Pattern 1: Normalized Structure (Preferred)**
```
ProjectName/
├── MAIA-PROJECT/                    # Or [CLIENT]-PROJECT/
│   ├── 03-DELIVERABLES/
│   │   └── current/                 # ← CANONICAL deliverables location
│   │       ├── DOCX/
│   │       ├── HTML/
│   │       └── PDF/
│   └── 04-QA-DOCUMENTATION/
│       └── test-files/              # ← Test corpus for QA
└── templates/
    └── competitive-analysis/        # Framework templates
```

**Pattern 2: Legacy/Flat Structure**
```
ProjectName/
├── 03-DELIVERABLES/
│   └── current/                     # ← Check here if no PROJECT/ folder
├── 05-FINAL-DELIVERABLES/           # ← Legacy location
│   └── VISUALIZATIONS/
│       └── current-enterprise-cleaned-report-documents/
└── test/                            # ← Legacy test location
```

**Path Discovery Protocol:**

When asked to review documents, check paths in this order:

1. **Check for normalized structure first:**
   - Look for `*-PROJECT/03-DELIVERABLES/current/`
   - If found, use this as canonical location

2. **Fall back to flat structure:**
   - Check `03-DELIVERABLES/current/`
   - Check `05-FINAL-DELIVERABLES/VISUALIZATIONS/current-enterprise-cleaned-report-documents/`

3. **Locate test corpus:**
   - Check `*-PROJECT/04-QA-DOCUMENTATION/test-files/`
   - Fall back to `test/`

This ensures backward compatibility while preferring the normalized structure.
```

**Step 2: Add Cross-Document Consistency Check section**

Add after Phase 5.6:

```markdown
### Phase 5.7: Cross-Document Consistency Check

**Objective:** Verify that key data points are identical across all deliverable documents.

**Critical Data Points to Verify:**

1. **Pricing Figures**
   - All competitor pricing must match across exec summary, full report, and pricing visualization
   - Format should be consistent (e.g., "$8-12 (est.)" everywhere, not "$8-12" in some places)

2. **Strategic Recommendations**
   - Priority numbers and titles must match
   - Investment amounts must be identical
   - Order of priorities must be consistent

3. **Market Share / Customer Counts**
   - Percentages must match across documents
   - Customer counts must be identical

4. **Competitor Names and Descriptions**
   - Spelling must be consistent
   - Brief descriptions should align

**Consistency Check Process:**

1. Extract key data points from each document:
   - Executive Summary
   - Full Report
   - Key visualization HTML files (pricing, positioning, recommendations)

2. Build comparison matrix:

```
| Data Point | Exec Summary | Full Report | Pricing Viz | Positioning Viz | Status |
|------------|--------------|-------------|-------------|-----------------|--------|
| Naviance pricing | $8-12 (est.) | $8-12 (est.) | $8-12 (est.) | — | ✅ |
| Priority 1 title | Attack US Market | Attack US Market | Attack US Market | — | ✅ |
| SCOIR market share | 12% | 12% | — | 10% | ⚠️ |
```

3. Flag discrepancies by severity:
   - **CRITICAL:** Investment amounts, strategic recommendations differ
   - **HIGH:** Pricing, market share, customer counts differ
   - **MEDIUM:** Descriptions, feature claims differ

**Consistency Report Format:**

```
## Cross-Document Consistency Check

**Documents Analyzed:** X
**Discrepancies Found:** Y

### Critical Discrepancies
[List any investment/recommendation mismatches]

### High Priority Discrepancies
| Data Point | Location 1 | Value 1 | Location 2 | Value 2 | Resolution |
|------------|------------|---------|------------|---------|------------|
| Naviance pricing | exec-summary.docx:L45 | $6-8 | full-report.docx:L234 | $8-12 (est.) | Update exec summary |

### Consistency Matrix
[Full comparison table]
```

**Integration with Workflow:**
- Run consistency check AFTER individual document reviews
- This is a "final gate" before declaring deliverables client-ready
- Any CRITICAL discrepancies must be resolved before delivery
```

**Verification:**

```bash
grep "Path Discovery Protocol" /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md && \
grep "Cross-Document Consistency Check" /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-analysis-quality-assurance/SKILL.md && \
echo "I.3 COMPLETE"
```

**Expected Output:** Two grep matches followed by `I.3 COMPLETE`

---

## PHASE J: UPDATE RESEARCH SKILL WITH ENHANCEMENTS

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Implement concrete enhancements to the research skill definition.

### Task J.1: Add Research Question Template to Research Skill

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md`

**Step 1: Add new section after "### 1. Clarify the Research Objective"**

Insert the following section:

```markdown
### Standard Research Question Template

Use this 24-question checklist to ensure comprehensive competitor coverage. Mark questions as required based on project scope.

**Company Overview (5 questions)**

| # | Question | Required | Answered |
|---|----------|----------|----------|
| 1 | When was [Company] founded and where is it headquartered? | ☐ | ☐ |
| 2 | Who owns [Company]? (Public, private, PE-backed, acquired?) | ☐ | ☐ |
| 3 | Who is the CEO/leadership team? | ☐ | ☐ |
| 4 | What is [Company]'s total funding and latest funding round? | ☐ | ☐ |
| 5 | What is [Company]'s estimated revenue or financial status? | ☐ | ☐ |

**Product/Service (5 questions)**

| # | Question | Required | Answered |
|---|----------|----------|----------|
| 6 | What are [Company]'s core products/services? | ☐ | ☐ |
| 7 | What key features does [Company] offer? | ☐ | ☐ |
| 8 | What integrations does [Company] support? | ☐ | ☐ |
| 9 | Does [Company] have AI/ML capabilities? What kind? | ☐ | ☐ |
| 10 | Does [Company] have mobile apps? API access? | ☐ | ☐ |

**Pricing (4 questions)**

| # | Question | Required | Answered |
|---|----------|----------|----------|
| 11 | What is [Company]'s pricing model? (per-user, per-school, tiered?) | ☐ | ☐ |
| 12 | What is [Company]'s price range? (low/high estimates) | ☐ | ☐ |
| 13 | Are there published pricing tiers or is it custom-quoted? | ☐ | ☐ |
| 14 | How does pricing compare to market average? | ☐ | ☐ |

**Market Position (4 questions)**

| # | Question | Required | Answered |
|---|----------|----------|----------|
| 15 | How many customers/users does [Company] have? | ☐ | ☐ |
| 16 | What is [Company]'s estimated market share? | ☐ | ☐ |
| 17 | What geographic regions does [Company] serve? | ☐ | ☐ |
| 18 | Who are [Company]'s primary target customers? | ☐ | ☐ |

**Customer Satisfaction (3 questions)**

| # | Question | Required | Answered |
|---|----------|----------|----------|
| 19 | What is [Company]'s rating on G2/Capterra/TrustRadius? | ☐ | ☐ |
| 20 | What do customers praise about [Company]? | ☐ | ☐ |
| 21 | What are common complaints about [Company]? | ☐ | ☐ |

**Strategic (3 questions)**

| # | Question | Required | Answered |
|---|----------|----------|----------|
| 22 | What is [Company]'s stated strategy/vision? | ☐ | ☐ |
| 23 | What recent news/developments are significant? | ☐ | ☐ |
| 24 | What are [Company]'s key strengths and weaknesses? | ☐ | ☐ |

**Usage Instructions:**
1. At project start, mark which questions are "Required" based on scope
2. Track "Answered" status during research
3. Flag any Required questions not answered before report generation
4. Minimum coverage: 80% of Required questions must be answered
```

**Verification:**

```bash
grep "Standard Research Question Template" /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md && \
grep "24-question checklist" /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md && \
echo "J.1 COMPLETE"
```

**Expected Output:** Two grep matches followed by `J.1 COMPLETE`

---

### Task J.2: Add Output Schema to Research Skill

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md`

**Step 1: Add new section after "### 4. Analyze and Synthesize"**

Insert the following section:

```markdown
### Output Format Standardization

**Competitor Data Schema:**

After completing research for each competitor, structure data in this standard format for consistency and automated comparison:

```json
{
  "competitor": {
    "name": "SCOIR",
    "website": "https://www.scoir.com",
    "founded": 2014,
    "headquarters": "Pittsburgh, PA",
    "ownership": "private",
    "parent_company": null
  },
  "financials": {
    "total_funding": {
      "amount": 42000000,
      "currency": "USD",
      "source": "Crunchbase",
      "date": "2023-06",
      "confidence": "verified"
    },
    "latest_round": {
      "series": "Series C",
      "amount": 25000000,
      "date": "2023-06"
    },
    "revenue": {
      "amount": null,
      "source": null,
      "confidence": "unknown"
    }
  },
  "market": {
    "customers": {
      "count": 2400,
      "unit": "schools",
      "source": "SCOIR website",
      "date": "2024-11"
    },
    "market_share": {
      "percentage": 12,
      "source": "EdTech Analysis",
      "confidence": "estimated"
    },
    "geographic_presence": ["USA", "Canada"]
  },
  "pricing": {
    "model": "per-student",
    "low_range": 4.80,
    "high_range": 4.80,
    "currency": "USD",
    "source": "SCOIR pricing page",
    "confidence": "verified",
    "notes": "Flat per-student pricing, no tiers"
  },
  "product": {
    "description": "College admissions management platform",
    "primary_focus": "College matching and application management",
    "key_features": [
      "AI-powered college matching",
      "Document management",
      "Direct admissions partnerships",
      "Student-counselor collaboration"
    ],
    "integrations": ["Naviance", "PowerSchool", "Canvas"],
    "ai_capabilities": "College matching algorithm, personalized recommendations",
    "mobile_app": true,
    "api_available": true
  },
  "positioning": {
    "target_segment": "mid-market",
    "target_customers": ["Public schools", "Independent schools"],
    "value_proposition": "AI-forward college guidance platform",
    "differentiators": [
      "Direct admissions partnerships",
      "Modern user experience",
      "Transparent pricing"
    ],
    "weaknesses": [
      "Smaller market share than Naviance",
      "Limited international presence"
    ]
  },
  "satisfaction": {
    "rating": 4.6,
    "scale": 5,
    "source": "G2",
    "review_count": 89,
    "date": "2024-11",
    "confidence": "verified"
  },
  "metadata": {
    "research_date": "2024-11-15",
    "researcher": "Claude",
    "data_freshness": "current",
    "completeness_score": 92
  }
}
```

**Schema Field Requirements:**

| Field | Required | Notes |
|-------|----------|-------|
| competitor.name | Yes | Exact company name |
| competitor.website | Yes | Primary domain |
| pricing.model | Yes | At minimum, describe the model |
| pricing.confidence | Yes | "verified", "estimated", or "unknown" |
| market.customers | Recommended | If unavailable, note in metadata |
| satisfaction.rating | Recommended | From G2, Capterra, or TrustRadius |
| metadata.research_date | Yes | Date research was conducted |
| metadata.completeness_score | Yes | Percentage of questions answered |

**Confidence Levels:**
- `verified`: Data from official source (company website, SEC filing, official announcement)
- `estimated`: Data inferred or from secondary source (analyst report, news article)
- `unknown`: Data not found or conflicting sources

**Usage:**
1. Populate schema during Phase B (Deep Dive)
2. Use schema to generate comparison matrices automatically
3. Export as JSON file alongside markdown profile
4. QA skill can validate schema completeness
```

**Verification:**

```bash
grep "Competitor Data Schema" /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md && \
grep "completeness_score" /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md && \
echo "J.2 COMPLETE"
```

**Expected Output:** Two grep matches followed by `J.2 COMPLETE`

---

### Task J.3: Add Citation Generation and Output Location to Research Skill

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md`

**Step 1: Add Citation Generation section**

Insert after the Output Schema section:

```markdown
### Citation Auto-Generation

**Capture During Research:**

When scraping or searching, automatically capture citation metadata:

```json
{
  "source_name": "SCOIR",
  "source_type": "company_website",
  "url": "https://www.scoir.com/about",
  "page_title": "About SCOIR",
  "access_date": "2024-11-15",
  "publication_date": null,
  "author": null
}
```

**Citation Formats:**

**Short Format (for inline use):**
```
(Source, YYYY)
```
Examples:
- `(SCOIR, 2024)`
- `(G2 Reviews, November 2024)`
- `(Crunchbase, 2023)`

**Full Format (for references section):**
```
Source Name. "Page Title." URL. Accessed YYYY-MM-DD.
```
Examples:
- `SCOIR. "About Us." https://www.scoir.com/about. Accessed 2024-11-15.`
- `G2. "SCOIR Reviews." https://g2.com/products/scoir. Accessed 2024-11-15.`

**Citation Registry:**

Maintain a running list of all sources used:

```markdown
## Sources Used

| # | Source | Type | URL | Access Date | Used For |
|---|--------|------|-----|-------------|----------|
| 1 | SCOIR | Company website | https://scoir.com/about | 2024-11-15 | Company overview |
| 2 | G2 | Review site | https://g2.com/products/scoir | 2024-11-15 | Satisfaction rating |
| 3 | Crunchbase | Database | https://crunchbase.com/scoir | 2024-11-15 | Funding data |
```

**Integration:**
- Build citation registry during research
- Export as `sources.md` alongside competitor profiles
- QA skill can verify citations against this registry
```

**Step 2: Add Output Location Defaults section**

Insert after Citation Generation:

```markdown
### Output Location Defaults

**Path Discovery Protocol:**

When saving research outputs, check locations in this order:

1. **Normalized structure (preferred):**
   ```
   [PROJECT]-PROJECT/01-RESEARCH-INPUTS/competitor-data/
   ```
   Example: `MAIA-PROJECT/01-RESEARCH-INPUTS/competitor-data/`

2. **Flat structure (fallback):**
   ```
   01-RESEARCH-INPUTS/competitor-data/
   ```

3. **Legacy structure (last resort):**
   ```
   02-COMPETITOR-PROFILES/
   ```

**Output File Naming:**

| File Type | Naming Convention | Example |
|-----------|-------------------|---------|
| Competitor profile | `[company]-profile.md` | `scoir-profile.md` |
| Competitor data (JSON) | `[company]-data.json` | `scoir-data.json` |
| Source registry | `sources.md` | `sources.md` |
| Research tracker | `research-tracker.md` | `research-tracker.md` |

**Directory Structure After Research:**

```
01-RESEARCH-INPUTS/
├── competitor-data/
│   ├── naviance-profile.md
│   ├── naviance-data.json
│   ├── scoir-profile.md
│   ├── scoir-data.json
│   └── ... (other competitors)
├── sources.md
└── research-tracker.md
```

This structure integrates with the QA skill's path discovery protocol.
```

**Verification:**

```bash
grep "Citation Auto-Generation" /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md && \
grep "Output Location Defaults" /Users/seancurrie/Desktop/MaiaLearningResearch/skills/local/competitive-research-brightdata/SKILL.md && \
echo "J.3 COMPLETE"
```

**Expected Output:** Two grep matches followed by `J.3 COMPLETE`

---

## PHASE K: SKILL INSTALLATION, TESTING & FINAL VERIFICATION

**Batching Reminder:** Execute the tasks in this phase in strict 3‑task batches. Stop immediately if any verification fails and request clarification.

**Objective:** Install updated skills, run tests, and complete documentation.

### Task K.1: Install Updated Skills to ~/.claude/skills/

**Files:**
- Sync: `skills/local/` → `~/.claude/skills/`

**Step 1: Run install script with backup**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
./scripts/install-skills.sh --backup
```

**Step 2: Verify installation**

```bash
grep "Source Attribution Verification" ~/.claude/skills/competitive-analysis-quality-assurance/SKILL.md && \
grep "Standard Research Question Template" ~/.claude/skills/competitive-research-brightdata/SKILL.md && \
echo "SKILLS INSTALLED SUCCESSFULLY"
```

**Verification:**

```bash
test -f ~/.claude/skills/competitive-analysis-quality-assurance/SKILL.md && \
test -f ~/.claude/skills/competitive-research-brightdata/SKILL.md && \
echo "K.1 COMPLETE"
```

**Expected Output:** `K.1 COMPLETE`

---

### Task K.2: Test QA Skill Against Test Corpus

**Files:**
- Test using: `MAIA-PROJECT/04-QA-DOCUMENTATION/test-files/`

**Step 1: Verify test files exist**

```bash
ls /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/04-QA-DOCUMENTATION/test-files/
```

**Step 2: Run skill test (manual invocation)**

After this task completes, invoke the QA skill manually with:

```
Skill: competitive-analysis-quality-assurance

Please run a quick validation on the test files in MAIA-PROJECT/04-QA-DOCUMENTATION/test-files/. Specifically:
1. Verify the new Source Attribution Verification section appears in your workflow
2. Verify the Marketing Language Detection section appears
3. Verify the Cross-Document Consistency Check section appears
4. Verify the Path Discovery Protocol correctly identifies the MAIA-PROJECT structure

Report which new sections you can see in your skill definition.
```

**Step 3: Document test results**

Create a brief note in the test-files directory documenting that the skill was tested:

Create `/Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/04-QA-DOCUMENTATION/test-files/SKILL-TEST-LOG.md`:

```markdown
# Skill Test Log

## QA Skill Test - November 25, 2025

**Skill Version:** Post-enhancement (includes Phase 5.5, 5.6, 5.7)

**New Sections Tested:**
- [ ] Source Attribution Verification (Phase 5.5)
- [ ] Marketing Language Detection (Phase 5.6)
- [ ] Cross-Document Consistency Check (Phase 5.7)
- [ ] Path Discovery Protocol (updated)

**Test Status:** Pending manual verification

**Notes:**
- Test corpus files: executive-summary-qa-report.md, maia-learning-profile-qa-report.md, etc.
- After running skill, mark checkboxes and add notes below.

---

**Tester:** [Name]
**Date:** [Date]
**Result:** [PASS/FAIL]
**Notes:** [Any issues or observations]
```

**Verification:**

```bash
test -f /Users/seancurrie/Desktop/MaiaLearningResearch/MAIA-PROJECT/04-QA-DOCUMENTATION/test-files/SKILL-TEST-LOG.md && \
echo "K.2 COMPLETE"
```

**Expected Output:** `K.2 COMPLETE`

---

### Task K.3: Update Root README and IMPLEMENTATION-COMPLETE

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/README.md`
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/docs/IMPLEMENTATION-COMPLETE.md`

**Step 1: Update root README.md**

Update to reflect new structure:

```markdown
# Competitive Analysis Framework

A comprehensive framework for conducting enterprise-grade competitive analysis, including templates, workflows, automation scripts, and custom Claude skills.

## Repository Structure

```
MaiaLearningResearch/
├── docs/                    # Framework documentation
│   ├── COMPETITIVE-ANALYSIS-WORKFLOW.md
│   ├── guides/
│   └── plans/
├── templates/               # Reusable templates
│   └── competitive-analysis/
├── 06-AUTOMATION/           # Automation scripts
│   ├── scripts/
│   └── templates/
├── skills/                  # Version-controlled skill definitions
│   └── local/
├── scripts/                 # Utility scripts
│   └── install-skills.sh
├── MAIA-PROJECT/            # Example: Maia Learning project instance
└── archive/                 # Archived files
```

## Quick Start

### Starting a New Competitive Analysis

1. Copy the template:
   ```bash
   cp -r templates/competitive-analysis /path/to/new-project/
   ```

2. Follow the workflow:
   - Read `docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`
   - Use skills as documented in `docs/guides/SKILLS-USAGE-GUIDE.md`

3. Reference the example:
   - See `MAIA-PROJECT/` for a completed project instance

### Installing Skills

To sync skill definitions to your Claude environment:

```bash
./scripts/install-skills.sh --backup
```

## Custom Skills

This framework includes two custom Claude skills:

- **competitive-research-brightdata**: Enterprise-grade competitive research using Bright Data
- **competitive-analysis-quality-assurance**: Systematic QA for competitive analysis deliverables

Skill definitions are version-controlled in `skills/local/` and can be synced to `~/.claude/skills/` using the install script.

## Framework Version

- **Version:** 2.0
- **Quality Standard:** 9.5/10 (enterprise-grade)
- **Last Updated:** November 25, 2025

---

See `docs/IMPLEMENTATION-COMPLETE.md` for full implementation history.
```

**Step 2: Update IMPLEMENTATION-COMPLETE.md**

Add new section at the end:

```markdown
---

## Phase 7: Repository Normalization & Skill Updates (November 25, 2025)

### 7.1 Repository Restructuring

**Completed:**
- Created `MAIA-PROJECT/` to consolidate all project-specific files
- Moved all Maia research/analysis directories into `MAIA-PROJECT/`
- Preserved `05-FINAL-DELIVERABLES/` intact in `MAIA-PROJECT/archive/original-structure/`
- Created `archive/` for root-level clutter (legacy scripts, temp files, node artifacts)
- Framework layer (docs/, templates/, 06-AUTOMATION/) unchanged at root

**New Structure:**
- `MAIA-PROJECT/` - Complete Maia Learning project instance
- `archive/` - Archived files not needed for framework operation
- `skills/local/` - Version-controlled skill definitions
- `scripts/` - Utility scripts including skill installer

### 7.2 Skill Version Control

**Completed:**
- Copied skill definitions from `~/.claude/skills/` to `skills/local/`
- Created `scripts/install-skills.sh` for repo→~/.claude sync
- Install script includes `--backup` and `--dry-run` options

### 7.3 Skill Enhancements

**competitive-analysis-quality-assurance:**
- Added Phase 5.5: Source Attribution Verification
- Added Phase 5.6: Marketing Language Detection
- Added Phase 5.7: Cross-Document Consistency Check
- Updated Path Discovery Protocol for normalized structure

**competitive-research-brightdata:**
- Added Standard Research Question Template (24 questions)
- Added Competitor Data Schema (JSON format)
- Added Citation Auto-Generation
- Added Output Location Defaults

### 7.4 Documentation Updates

- Updated root README.md with new structure
- Updated docs/PROJECT-INVENTORY.md with deprecation notice
- Updated templates/competitive-analysis/README.md with example reference
- Created MAIA-PROJECT/README.md
- Created archive/README.md

### Verification

- [x] Safety branch created: `pre-normalization-backup`
- [x] All Maia files moved to MAIA-PROJECT/
- [x] Framework layer unchanged at root
- [x] Skills copied to skills/local/
- [x] Install script functional
- [x] Skill enhancements added
- [ ] Skill tests passed (manual verification required)

---

**Implementation Completed:** November 25, 2025
**Framework Version:** 2.0
**Plan Reference:** `docs/plans/2025-11-25-maia-project-normalization-and-skill-updates.md`
```

**Verification:**

```bash
grep "Repository Normalization" /Users/seancurrie/Desktop/MaiaLearningResearch/docs/IMPLEMENTATION-COMPLETE.md && \
grep "MAIA-PROJECT" /Users/seancurrie/Desktop/MaiaLearningResearch/README.md && \
echo "K.3 COMPLETE"
```

**Expected Output:** Two grep matches followed by `K.3 COMPLETE`

---

## CHANGES MADE & WHY THEY MATTER

This section documents key design decisions in this plan:

### 1. Moves Only, No Deletes on First Pass
**Rationale:** Preserves ability to recover from mistakes. Even regenerable items (node_modules) are archived first.

### 2. 05-FINAL-DELIVERABLES Preserved Intact
**Rationale:** Contains forensic value (how files evolved). Decomposing it risks losing context. Can be cleaned up in future phase if needed.

### 3. Skills Version-Controlled in Repo
**Rationale:** Repo becomes source of truth. Changes are tracked in git. Install script pushes to ~/.claude/skills/ as needed.

### 4. Path Discovery Protocol Added to Skills
**Rationale:** Skills need to work with both old and new structures during transition and for future projects with different layouts.

### 5. Concrete Skill Enhancements
**Rationale:** Previous plan only created spec docs. This plan implements actual changes to skill definitions that will affect skill behavior.

### 6. Test Corpus Preserved and Located
**Rationale:** QA skill needs test files to verify enhancements work. Moving test/ to MAIA-PROJECT keeps it accessible while cleaning root.

---

## INSTRUCTIONS FOR EXECUTING THIS PLAN

### Execution Rules

1. **Use `superpowers:executing-plans` skill.** This plan is designed for 3-task batch execution.

2. **Each task is self-contained.** Complete one task, verify, move to next.

3. **Verification steps are mandatory.** If verification fails, fix before proceeding.

4. **File paths are absolute.** Use paths exactly as written.

5. **Under no circumstances may more than 3 tasks be executed in a batch.** Stop and wait for review.

### Skill Usage During Execution

- Before any file move: Verify source exists with `test -d` or `test -f`
- After any file move: Verify destination exists AND source removed
- For skill edits: Read file first, then make targeted additions

### Error Recovery

- If a mv command fails: Check if source exists, check if destination parent exists
- If a verification fails: Do not proceed; investigate and fix
- If unsure: Ask user via `AskUserQuestion`

---

**Plan Version:** 1.0
**Author:** Claude Opus 4.5 (via superpowers:writing-plans)
**Date:** November 25, 2025
**Compatibility:** superpowers:executing-plans, 3-task batch execution
**Phases:** A through K (33 tasks total)
