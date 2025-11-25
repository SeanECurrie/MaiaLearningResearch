# Quick Iterations Guide

**Purpose:** How to make quick updates to competitive analysis deliverables without running the full workflow
**Scope:** Operational quick-reference for Scenario 2 (Quick Competitive Update) from the master workflow
**Reference:** For full workflow, see `docs/COMPETITIVE-ANALYSIS-WORKFLOW.md`

---

## Overview

This guide covers how to make small, targeted updates to existing competitive analysis deliverables. Use this when you need to fix a typo, update a single data point, add a missing citation, or regenerate PDFs.

---

## When to Use Quick Iterations

**Use this guide when:**
- Updating a single data point (e.g., new funding amount, pricing change)
- Fixing a typo or formatting issue
- Adding a missing citation
- Making a small content addition (single paragraph or less)
- Regenerating PDFs after source file changes
- Correcting an inconsistency across documents

---

## When NOT to Use Quick Iterations

**Use the full workflow instead when:**
- Making major strategic changes (repositioning, new recommendations)
- Adding a new competitor to the analysis
- Restructuring document organization
- Significant content rewrites (more than a few paragraphs)
- Changes that affect 5+ files
- Changes requiring new research
- Client requests a major revision

**Decision Rule:** If you're unsure, start with the quick iteration approach. If you realize the change is larger than expected, switch to the full workflow.

---

## Quick Iteration Process

Follow these 7 steps for any quick update:

### Step 1: Identify the Change Needed

**Clearly define what needs to change:**
- What is the current value/text?
- What should it be changed to?
- Why is this change needed?

**Examples:**
- "SCOIR funding needs to change from $50M to $88.3M"
- "Missing citation needed for Naviance market share claim"
- "Typo: 'reccommendations' should be 'recommendations'"

---

### Step 2: Locate All Files Affected

**Use grep to find all occurrences:**

```bash
# Find all files containing the text to change
grep -r "SCOIR.*funding" 03-DELIVERABLES/current/

# Find all files mentioning specific term
grep -r "market share" 03-DELIVERABLES/current/ --include="*.md" --include="*.html"

# Count occurrences
grep -r "term to find" 03-DELIVERABLES/current/ | wc -l
```

**Document the files found:**
- List each file path
- Note the line numbers if helpful
- Verify you've found ALL occurrences

---

### Step 3: Make Changes to Source Files

**Edit source files (DOCX + HTML), NOT PDFs:**

1. Open each affected file
2. Make the change consistently
3. Ensure citation format is "(Source, YYYY)" if adding sources
4. Save each file

**Important:** PDFs are generated FROM source files. Never edit PDFs directly.

**File priority:**
1. `.docx` files (primary source for reports)
2. `.html` files (primary source for visualizations)
3. `.md` files (if markdown sources exist)

---

### Step 4: Regenerate PDFs from Sources

**For visualization PDFs:**

```bash
# Regenerate all PDFs
./06-AUTOMATION/scripts/generate-pdfs.sh

# Or regenerate a single PDF
./06-AUTOMATION/scripts/generate-pdfs.sh specific-file.html
```

**For report PDFs:**
- Re-export from DOCX using your PDF tool
- Or use Chrome headless if HTML-based

---

### Step 5: Quick Consistency Check

**Verify the change applied everywhere:**

```bash
# Search for OLD value (should return 0 results)
grep -r "OLD_VALUE" 03-DELIVERABLES/current/

# Search for NEW value (should match expected count)
grep -r "NEW_VALUE" 03-DELIVERABLES/current/

# Use verify-consistency.py for automated check
python 06-AUTOMATION/scripts/verify-consistency.py --search "NEW_VALUE" --expected 5 --path 03-DELIVERABLES/current/
```

**If inconsistencies found:** Go back to Step 3 and fix missing occurrences.

---

### Step 6: Document Change in VERSION-HISTORY.md

**Add entry to VERSION-HISTORY.md:**

```markdown
## V2.1 (Date) - Quick Update

**Change:** Updated SCOIR funding from $50M to $88.3M (Series B, October 2024)

**Files Changed:**
- executive-summary.docx
- full-report.docx
- competitive-positioning-viz.html

**Source:** (Crunchbase, 2024)
```

---

### Step 7: Commit Changes

**If using git:**

```bash
# Stage all changed files
git add 03-DELIVERABLES/current/
git add 03-DELIVERABLES/VERSION-HISTORY.md

# Commit with descriptive message
git commit -m "Update SCOIR funding to $88.3M (Series B Oct 2024)

- Updated executive summary
- Updated full report
- Regenerated positioning visualization PDF

Source: Crunchbase, 2024"
```

---

## Quick Iteration Templates

Use these templates for common update scenarios:

---

### Template 1: Update Single Data Point

**Use for:** Pricing changes, funding updates, customer count changes, market share updates

**Grep Command:**
```bash
# Find all references to the data point
grep -rn "CURRENT_VALUE" 03-DELIVERABLES/current/
```

**Edit Instructions:**
1. Open each file listed
2. Find and replace: `CURRENT_VALUE` → `NEW_VALUE (Source, YYYY)`
3. Ensure the source citation is added/updated
4. Save file

**PDF Regeneration:**
```bash
./06-AUTOMATION/scripts/generate-pdfs.sh
```

**Verification:**
```bash
# Old value should return 0 results
grep -r "CURRENT_VALUE" 03-DELIVERABLES/current/ | wc -l
# Expected: 0

# New value should return expected count
grep -r "NEW_VALUE" 03-DELIVERABLES/current/ | wc -l
# Expected: [number of occurrences]
```

**Commit Message Format:**
```
Update [DATA_POINT] from [OLD] to [NEW]

Files: [list files]
Source: (Source, YYYY)
```

---

### Template 2: Add Missing Citation

**Use for:** Adding "(Source, YYYY)" citations to unsourced claims

**Grep Command:**
```bash
# Find the uncited claim
grep -rn "CLAIM_TEXT" 03-DELIVERABLES/current/
```

**Edit Instructions:**
1. Open each file containing the claim
2. Add citation directly after the claim: `CLAIM_TEXT (Source, YYYY)`
3. If claim needs adjustment, update claim text as well
4. Save file

**PDF Regeneration:**
```bash
./06-AUTOMATION/scripts/generate-pdfs.sh
```

**Verification:**
```bash
# Claim with citation should now exist
grep -r "CLAIM_TEXT.*(.*," 03-DELIVERABLES/current/
# Should show claim followed by citation
```

**Commit Message Format:**
```
Add citation for [CLAIM_DESCRIPTION]

Added: (Source, YYYY) to [brief description]
Files: [list files]
```

---

### Template 3: Fix Formatting Issue

**Use for:** Typos, formatting inconsistencies, style fixes

**Grep Command:**
```bash
# Find all instances of the formatting issue
grep -rn "WRONG_TEXT" 03-DELIVERABLES/current/
```

**Edit Instructions:**
1. Open each affected file
2. Find and replace: `WRONG_TEXT` → `CORRECT_TEXT`
3. Check surrounding context for related issues
4. Save file

**PDF Regeneration:**
```bash
# Only needed if HTML files were changed
./06-AUTOMATION/scripts/generate-pdfs.sh
```

**Verification:**
```bash
# Wrong text should return 0 results
grep -r "WRONG_TEXT" 03-DELIVERABLES/current/ | wc -l
# Expected: 0

# Correct text should exist
grep -r "CORRECT_TEXT" 03-DELIVERABLES/current/ | wc -l
# Expected: [number of corrections]
```

**Commit Message Format:**
```
Fix: [DESCRIPTION OF FIX]

Corrected: [WRONG] → [CORRECT]
Files: [list files]
```

---

## Automation Scripts

The following scripts in `06-AUTOMATION/scripts/` support quick iterations:

---

### generate-pdfs.sh

**Purpose:** Convert HTML visualizations to PDF using Chrome headless

**Usage:**
```bash
# Regenerate all PDFs in VISUALIZATIONS directory
./06-AUTOMATION/scripts/generate-pdfs.sh

# Regenerate a specific PDF
./06-AUTOMATION/scripts/generate-pdfs.sh path/to/file.html
```

**What it does:**
1. Finds all `.html` files in target directory
2. Uses Chrome headless to render each file
3. Outputs PDF with same name to same directory
4. Reports success/failure for each file

**Requirements:**
- Google Chrome installed
- Write access to output directory

---

### bulk-replace.py

**Purpose:** Find and replace text across multiple files safely

**Usage:**
```bash
# Preview changes (ALWAYS run first)
python 06-AUTOMATION/scripts/bulk-replace.py --old "OLD_TEXT" --new "NEW_TEXT" --path 03-DELIVERABLES/current/ --dry-run

# Apply changes after reviewing preview
python 06-AUTOMATION/scripts/bulk-replace.py --old "OLD_TEXT" --new "NEW_TEXT" --path 03-DELIVERABLES/current/
```

**Options:**
- `--old`: Text to find (required)
- `--new`: Replacement text (required)
- `--path`: Directory to search (required)
- `--dry-run`: Preview changes without modifying files (recommended first)
- `--include`: File patterns to include (e.g., `"*.md,*.html"`)
- `--exclude`: File patterns to exclude (e.g., `"*.pdf"`)

**Safety Features:**
- `--dry-run` mode shows exactly what would change
- Reports file count and occurrence count before applying
- Creates backup of modified files (optional)
- Never modifies binary files (PDF, DOCX, images)

**Important:** Always run with `--dry-run` first to preview changes.

---

### verify-consistency.py

**Purpose:** Check that a value appears consistently across documents (report only, no modifications)

**Usage:**
```bash
# Check that "SCOIR" appears exactly 15 times
python 06-AUTOMATION/scripts/verify-consistency.py --search "SCOIR" --expected 15 --path 03-DELIVERABLES/current/

# Check that old value no longer exists
python 06-AUTOMATION/scripts/verify-consistency.py --search "OLD_VALUE" --expected 0 --path 03-DELIVERABLES/current/

# List all occurrences without count expectation
python 06-AUTOMATION/scripts/verify-consistency.py --search "funding" --path 03-DELIVERABLES/current/ --list
```

**Options:**
- `--search`: Text or pattern to search for (required)
- `--path`: Directory to search (required)
- `--expected`: Expected occurrence count (optional)
- `--list`: List all occurrences with file and line number
- `--include`: File patterns to include
- `--exclude`: File patterns to exclude

**Output:**
- Reports actual count vs expected count
- Lists files containing the search term
- Exits with error code if count doesn't match expected

**Note:** This script only reports findings. It never modifies files.

---

## Decision Guide

Use this decision tree to choose the right approach:

```
START: What kind of change do you need to make?
│
├─► Single data point update (pricing, funding, count)
│   └─► Use Template 1 + bulk-replace.py --dry-run
│
├─► Add missing citation to existing claim
│   └─► Use Template 2 (manual edit, usually 1-3 files)
│
├─► Fix typo or formatting issue
│   └─► Use Template 3 + bulk-replace.py --dry-run
│
├─► Regenerate PDFs after editing HTML sources
│   └─► Run generate-pdfs.sh directly
│
├─► Verify a change was applied consistently
│   └─► Run verify-consistency.py
│
└─► Multiple changes or strategic revision
    └─► Use full workflow (docs/COMPETITIVE-ANALYSIS-WORKFLOW.md)
```

**Quick Decision Rules:**

| If... | Then... |
|-------|---------|
| Change affects 1-3 files | Use this guide |
| Change affects 4+ files | Consider full workflow |
| Change is just text replacement | Use bulk-replace.py |
| Change requires judgment per file | Edit manually |
| Unsure if change applied everywhere | Run verify-consistency.py |
| Need to update PDFs | Run generate-pdfs.sh |

---

