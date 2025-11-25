# Phase 4: Quality Assurance

**Objective:** Systematic quality verification before client delivery
**Skill:** `Skill: competitive-analysis-quality-assurance`

---

## QA Overview

This phase ensures deliverables meet quality standards:
- Source attribution verification
- Pricing consistency
- Cross-document consistency
- Professional language check
- Completeness verification

**Target Quality Score:** 9.5/10

---

## QA Pass 1: Initial Review

### Step 1: Invoke QA Skill

```
Skill: competitive-analysis-quality-assurance

Provide:
- All deliverable files (DOCX, HTML, PDF)
- Source materials for fact-checking
- Original research data
```

### Step 2: Review QA Report

The skill will generate a report with:
- Missing source citations
- Pricing inconsistencies
- Disclaimer gaps
- Formatting issues
- Language quality concerns

### Step 3: Create Fix List

Document all findings in `04-QA-DOCUMENTATION/qa-reports/v1.0-qa-report.md`:

```markdown
# QA Report - V1.0

**Date:** [Date]
**Files Reviewed:** [List]
**Findings:** [Count]

## Critical Issues (Must Fix)
1. [Issue description] - [File] - [Location]
2. ...

## High Priority Issues
1. ...

## Medium Priority Issues
1. ...

## Low Priority Issues
1. ...
```

---

## Expected Finding Categories

### 1. Missing Source Citations

**Common issues:**
- Pricing claims without "(Source, YYYY)"
- Market share figures without citation
- Satisfaction ratings without source

**Fix pattern:**
```
Before: "Naviance costs $8-12 per student"
After: "Naviance costs $8-12 per student (est.) (PowerSchool, 2024)"
```

### 2. Pricing Inconsistencies

**Check:**
- Same competitor's pricing consistent across all documents
- Executive Summary matches Full Report matches Visualizations
- All estimates marked with "(est.)"

**Fix pattern:**
```
Document 1: "$6-8"
Document 2: "$8-12"
→ Verify correct value, update ALL references to match
```

### 3. Disclaimer Gaps

**Required disclaimers:**
- "(est.)" for estimated pricing
- Methodology context for market sizing
- Data recency notes
- Inferred rating explanations

**Fix pattern:**
```
Before: "Maia Learning rated 4.5/5"
After: "Maia Learning rated 4.5/5 (inferred from limited reviews; G2, 2024)"
```

### 4. Marketing Language

**Red flags to remove:**
- "Best-in-class"
- "Industry-leading"
- "Revolutionary"
- "Cutting-edge"
- Unsubstantiated superlatives

**Fix pattern:**
```
Before: "SCOIR's revolutionary AI features"
After: "SCOIR's AI features (launched 2024)"
```

---

## Fixing Issues

### Priority Order:
1. **Critical:** Factual errors, missing citations for key claims
2. **High:** Pricing inconsistencies, major disclaimer gaps
3. **Medium:** Language improvements, formatting
4. **Low:** Minor formatting, style consistency

### For Each Fix:
1. Locate all instances (use grep)
2. Fix in source file (DOCX or HTML)
3. Regenerate dependent files (PDFs)
4. Document fix in change log

### Change Log Template

Create `04-QA-DOCUMENTATION/change-logs/v1.0-changes.md`:

```markdown
# Change Log - V1.0 QA Fixes

## Summary
- Total changes: [N]
- Critical fixes: [N]
- Files modified: [List]

## Changes by Category

### Source Citations Added
1. [File]: Added "(Source, YYYY)" for [claim]
2. ...

### Pricing Corrections
1. [File]: Changed [old] → [new] for [competitor]
2. ...

### Disclaimers Added
1. [File]: Added "(est.)" for [pricing]
2. ...

### Language Corrections
1. [File]: Changed "[marketing phrase]" → "[factual phrase]"
2. ...
```

---

## QA Pass 2: Verification

### Step 1: Re-run QA Skill

After implementing fixes:

```
Skill: competitive-analysis-quality-assurance

Provide:
- Updated deliverable files
- Previous QA report for comparison
```

### Step 2: Verify All Fixed

**Expected outcome:**
- 0 critical issues
- 0 high priority issues
- Quality score: 9.5/10

### Step 3: Final Verification

Use `superpowers:verification-before-completion`:

**Checklist:**
- [ ] All QA findings addressed
- [ ] PDFs regenerated from updated sources
- [ ] Cross-document consistency verified
- [ ] File sizes reasonable (not corrupted)
- [ ] VERSION-HISTORY.md updated

---

## Quality Metrics Verification

### Source Citations: 100%

```bash
# Count claims vs citations
grep -c "\$[0-9]" executive-summary.md  # Pricing claims
grep -c "([A-Za-z]+, [0-9]{4})" executive-summary.md  # Citations
# Should be equal or citations > claims
```

### Pricing Consistency: 100%

```bash
# Check specific competitor pricing across files
grep -r "Naviance.*\$" 03-DELIVERABLES/current/
# All results should show same pricing
```

### Professional Language: Pass

```bash
# Check for marketing language
grep -ri "best\|leading\|revolutionary" 03-DELIVERABLES/current/
# Should return 0 results (or only in quotes from sources)
```

---

## QA Phase Completion Checklist

Before moving to client delivery or iterations:

- [ ] QA Pass 1 completed (all issues documented)
- [ ] All critical and high priority issues fixed
- [ ] QA Pass 2 completed (verified fixes)
- [ ] Final verification passed
- [ ] Change log documented
- [ ] VERSION-HISTORY.md updated to V1.0
- [ ] Quality score: 9.5/10 or higher

---

## Next Phase

If client feedback received, move to:
**[05-ITERATION-PHASE.md](./05-ITERATION-PHASE.md)**

If no feedback needed, deliverables are client-ready.
