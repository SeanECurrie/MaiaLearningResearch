# Enterprise Visualization Refactor - Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transform 10 colorful visualization HTML files into enterprise-grade professional documents optimized for C-suite digital viewing with perfect pagination, clean layouts, and conservative grayscale styling.

**Architecture:** Systematic file-by-file refactor applying unified CSS styling standards and content abbreviation to eliminate table overflow, text wrapping, and pagination issues. Priority on layout correctness over aesthetics.

**Tech Stack:** HTML5, CSS3 (print media queries), Chrome headless PDF generation, Python (optional content analysis)

**Target Deliverables:** 10 professional PDF reports viewable on laptops/monitors via Google Drive

---

## Design Standards Reference

### Color Palette (Conservative Grayscale)
- Background: `#ffffff` (white)
- Primary text: `#333333` (dark gray)
- Secondary text: `#666666` (medium gray)
- Borders: `#000000` (black, 1px solid)
- Light shading: `#f5f5f5` (Maia rows, subtle backgrounds)
- Medium shading: `#e0e0e0` (HIGH priority)
- Dark shading: `#cccccc` (CRITICAL priority)

### Typography Standards
- **Narrative content:** 12pt body, 14pt headings
- **Table content:** 10pt body, 11pt headings
- **Headers:** Bold, black text, black bottom borders (no colors)

### Priority Indicators (replacing 🔴 🟡 🟢)
- **CRITICAL/URGENT:** Bold black text on `#cccccc` background
- **HIGH:** Bold black text on `#e0e0e0` background
- **MEDIUM:** Bold black text on `#f5f5f5` background

### Table Structure
- Minimal black borders (1px solid #000000)
- Dark gray headers (#333333 background, white text)
- White cell backgrounds
- Maia Learning rows: Light gray (#f5f5f5) background

### Page Layout (PDF Generation)
- Optimize for digital screen viewing (not print)
- Intelligent page breaks (keep headers with content)
- No table row orphans
- Adequate whitespace at bottom of pages

---

## Phase 1: Create Shared CSS Standards File

### Task 1.1: Create enterprise-styles.css template

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/enterprise-styles.css`

**Step 1: Create base CSS file with print-optimized styles**

```css
/* Enterprise Professional Styling Standards */
/* Maia Learning Competitive Analysis - November 2025 */

/* ===== BASE STYLES ===== */
body {
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px;
    background: #ffffff;
    color: #333333;
    line-height: 1.6;
    font-size: 12pt;
}

/* ===== TYPOGRAPHY HIERARCHY ===== */
h1 {
    font-size: 24pt;
    font-weight: 700;
    color: #000000;
    border-bottom: 2px solid #000000;
    padding-bottom: 10px;
    margin: 0 0 20px 0;
    page-break-after: avoid;
}

h2 {
    font-size: 18pt;
    font-weight: 600;
    color: #333333;
    border-bottom: 1px solid #000000;
    padding-bottom: 8px;
    margin: 30px 0 15px 0;
    page-break-after: avoid;
}

h3 {
    font-size: 14pt;
    font-weight: 600;
    color: #333333;
    margin: 20px 0 10px 0;
    page-break-after: avoid;
}

h4 {
    font-size: 12pt;
    font-weight: 600;
    color: #333333;
    margin: 15px 0 8px 0;
}

p {
    margin: 10px 0;
    color: #333333;
}

/* ===== TABLES ===== */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 10pt;
    page-break-inside: auto;
    border: 1px solid #000000;
}

thead {
    display: table-header-group; /* Repeat on each page */
}

th {
    background: #333333;
    color: #ffffff;
    padding: 10px 8px;
    text-align: left;
    font-weight: 600;
    font-size: 11pt;
    border: 1px solid #000000;
    page-break-inside: avoid;
    page-break-after: avoid;
}

td {
    padding: 8px 8px;
    border: 1px solid #000000;
    background: #ffffff;
    vertical-align: top;
    page-break-inside: avoid;
    hyphens: none;
}

tr {
    page-break-inside: avoid;
    page-break-after: auto;
}

tbody tr:nth-child(even) {
    /* Optional: very subtle zebra striping */
    background: #fafafa;
}

/* Maia Learning rows - subtle highlight */
tr.maia-row td,
td.maia-cell {
    background: #f5f5f5;
    font-weight: 500;
}

/* ===== SECTIONS & BOXES ===== */
.section {
    background: #ffffff;
    padding: 25px;
    margin-bottom: 30px;
    border: 1px solid #cccccc;
    page-break-inside: avoid;
}

.overview,
.summary-box,
.executive-summary {
    background: #f5f5f5;
    border-left: 3px solid #000000;
    padding: 20px;
    margin: 20px 0;
    page-break-inside: avoid;
}

/* ===== PRIORITY BADGES ===== */
.badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 3px;
    font-size: 9pt;
    font-weight: 600;
    text-transform: uppercase;
    border: 1px solid #000000;
}

.badge-critical,
.priority-critical,
.threat-very-high {
    background: #cccccc;
    color: #000000;
}

.badge-high,
.priority-high,
.threat-medium-high {
    background: #e0e0e0;
    color: #000000;
}

.badge-medium,
.priority-medium,
.threat-medium {
    background: #f5f5f5;
    color: #000000;
}

/* ===== LISTS ===== */
ul, ol {
    margin: 15px 0;
    padding-left: 25px;
}

li {
    margin: 8px 0;
    color: #333333;
}

/* ===== PAGE BREAKS ===== */
.page-break {
    page-break-after: always;
}

.no-break {
    page-break-inside: avoid;
}

/* ===== PRINT MEDIA QUERIES ===== */
@media print {
    body {
        margin: 0;
        padding: 20px;
    }

    .section {
        page-break-inside: avoid;
    }

    h1, h2, h3, h4 {
        page-break-after: avoid;
    }

    table {
        page-break-inside: auto;
    }

    tr {
        page-break-inside: avoid;
    }

    thead {
        display: table-header-group;
    }
}

/* ===== PDF GENERATION OPTIMIZATIONS ===== */
@page {
    size: letter portrait;
    margin: 0.75in;
}
```

**Step 2: Verify file created**

```bash
ls -lh /Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/enterprise-styles.css
```

Expected: File exists, ~4-5KB

**Step 3: Commit CSS standards file**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch
git add 05-FINAL-DELIVERABLES/VISUALIZATIONS/enterprise-styles.css
git commit -m "feat: add enterprise CSS styling standards for visualizations

- Conservative grayscale palette
- Print-optimized page breaks
- 12pt narrative, 10pt tables
- Minimal black borders
- Priority badges with gray shading"
```

---

## Phase 2: Refactor Individual Visualization Files

### Task 2.1: Refactor swot-analysis-viz.html (386 lines - SIMPLEST)

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/swot-analysis-viz.html`

**Step 1: Backup original file**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS
cp swot-analysis-viz.html swot-analysis-viz.html.backup-colorful
```

**Step 2: Replace <style> section with enterprise standards**

Replace lines 7-161 (entire style block) with:

```html
<link rel="stylesheet" href="enterprise-styles.css">
<style>
    /* File-specific overrides only */
    .competitor-section {
        margin-bottom: 50px;
        page-break-after: always;
    }

    .competitor-header {
        background: #333333;
        color: #ffffff;
        padding: 15px 20px;
        margin-bottom: 20px;
        border: 1px solid #000000;
    }

    .competitor-title {
        font-size: 16pt;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .competitor-subtitle {
        font-size: 11pt;
        opacity: 0.9;
    }

    th.strengths,
    th.weaknesses,
    th.opportunities,
    th.threats {
        background: #333333;
        color: #ffffff;
    }
</style>
```

**Step 3: Remove emoji threat badges**

Find and replace:
- `🔴 Very High` → `VERY HIGH`
- `🟡 Medium-High` → `MEDIUM-HIGH`
- `🟡 Medium` → `MEDIUM`

Update threat badge classes:
```html
<!-- Before -->
<span class="threat-badge threat-very-high">🔴 Very High</span>

<!-- After -->
<span class="badge badge-critical">VERY HIGH</span>
```

**Step 4: Test PDF generation**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --print-to-pdf="/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/swot-analysis-viz-ENTERPRISE.pdf" \
  "file:///Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/swot-analysis-viz.html"
```

**Step 5: Verify PDF quality**

Open PDF and check:
- [ ] No colorful backgrounds (grayscale only)
- [ ] Tables fit on pages (no overflow)
- [ ] Text doesn't wrap awkwardly
- [ ] Page breaks occur between competitor sections
- [ ] Headers repeat on multi-page tables
- [ ] No emojis visible

**Step 6: Commit if verification passes**

```bash
git add swot-analysis-viz.html swot-analysis-viz-ENTERPRISE.pdf
git commit -m "refactor: convert SWOT analysis to enterprise grayscale

- Remove gradient backgrounds and colorful sections
- Replace emoji badges with gray-shaded text
- Optimize table pagination
- Generate clean PDF for C-suite review"
```

---

### Task 2.2: Refactor market-trends-viz.html (312 lines)

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/market-trends-viz.html`

**Step 1: Backup original**

```bash
cp market-trends-viz.html market-trends-viz.html.backup-colorful
```

**Step 2: Replace style section**

Replace lines 7-144 with:

```html
<link rel="stylesheet" href="enterprise-styles.css">
<style>
    /* Market trends specific styles */
    .overview {
        background: #f5f5f5;
        padding: 20px;
        border-left: 3px solid #000000;
        margin-bottom: 30px;
    }

    .stats {
        display: flex;
        gap: 30px;
        margin-top: 15px;
    }

    .stat {
        flex: 1;
    }

    .stat-value {
        font-size: 20pt;
        font-weight: 700;
        color: #000000;
    }

    .stat-label {
        font-size: 10pt;
        color: #666666;
        margin-top: 5px;
    }

    .trend-number {
        font-weight: 700;
        font-size: 12pt;
        color: #000000;
    }

    .maia-position {
        font-weight: 600;
        color: #000000;
        margin-top: 8px;
    }
</style>
```

**Step 3: Remove emojis and colored sections**

Find and replace:
- `<h2>🔴 Tier 1:` → `<h2>TIER 1 (CRITICAL):`
- `<h2>🟡 Tier 2:` → `<h2>TIER 2 (HIGH PRIORITY):`
- `<h2>🟢 Tier 3:` → `<h2>TIER 3 (EMERGING):`
- `<span class="badge badge-critical">🔴 CRITICAL</span>` → `<span class="badge badge-critical">CRITICAL</span>`
- `<span class="badge badge-high">🟡 HIGH</span>` → `<span class="badge badge-high">HIGH</span>`
- `<span class="badge badge-medium">🟢 MEDIUM</span>` → `<span class="badge badge-medium">MEDIUM</span>`

Remove colored row backgrounds:
```html
<!-- Before -->
<tr class="priority-critical">

<!-- After -->
<tr>
```

**Step 4: Abbreviate verbose content in table cells**

Review "Impact on Market" column - shorten text to prevent wrapping:

Example abbreviations:
- "Platforms with advanced AI (SCOIR AI 2.0, SchooLinks Agentic Layer) gaining competitive advantage. AI transitioning from 'nice-to-have' to table stakes."
→ "Advanced AI (SCOIR 2.0, SchooLinks) now competitive requirement. Transitioning to table stakes."

- "200+ colleges offering admission without application. Shift from 'help students apply' → 'help students choose wisely'"
→ "200+ colleges offer direct admission. Shift from application help to choice guidance."

**Step 5: Generate and verify PDF**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --print-to-pdf="/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/market-trends-viz-ENTERPRISE.pdf" \
  "file:///Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/market-trends-viz.html"
```

Verify:
- [ ] No emojis
- [ ] Grayscale only
- [ ] Table text doesn't wrap awkwardly
- [ ] All 10 trends visible and readable

**Step 6: Commit**

```bash
git add market-trends-viz.html market-trends-viz-ENTERPRISE.pdf
git commit -m "refactor: convert market trends to enterprise grayscale

- Remove emoji tier indicators
- Abbreviate verbose table content
- Clean pagination and layout"
```

---

### Task 2.3: Refactor competitive-positioning-viz.html (315 lines)

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/competitive-positioning-viz.html`

**Step 1: Backup original**

```bash
cp competitive-positioning-viz.html competitive-positioning-viz.html.backup-colorful
```

**Step 2: Replace style section with enterprise standards**

Replace colorful styles (lines 7-120) with:

```html
<link rel="stylesheet" href="enterprise-styles.css">
<style>
    /* Competitive positioning specific */
    .map-section {
        margin: 30px 0;
        page-break-inside: avoid;
    }

    .map-container {
        background: #ffffff;
        border: 2px solid #000000;
        padding: 30px;
        margin: 20px 0;
        font-family: 'Courier New', monospace;
        font-size: 9pt;
        overflow-x: auto;
    }

    .platform-name {
        font-weight: 600;
        color: #000000;
    }

    .insights {
        background: #f5f5f5;
        border-left: 3px solid #000000;
        padding: 20px;
        margin: 20px 0;
    }
</style>
```

**Step 3: Remove star emojis from platform names**

Find and replace:
- `⭐ Maia Learning` → `Maia Learning` (keep bold or highlight via CSS)
- `⭐` from ASCII maps → Remove

For Maia rows, add class:
```html
<td class="platform-name maia-cell">Maia Learning</td>
```

**Step 4: Remove emoji priority indicators**

Replace:
- `🔴 URGENT (Q1 2026):` → `URGENT (Q1 2026):`
- `🟡 HIGH PRIORITY (Q2-Q3 2026):` → `HIGH PRIORITY (Q2-Q3 2026):`
- `🟢 MEDIUM PRIORITY (Q4 2026-2027):` → `MEDIUM PRIORITY (Q4 2026-2027):`

**Step 5: Clean ASCII positioning maps**

Remove emoji stars from ASCII art maps (around line 640):
```
Before:
│  SCOIR ⭐

After:
│  SCOIR
```

Update legend:
```
Before:
<strong>Legend:</strong> ⭐ = Positioning leaders | ⚪ = Established | ⬇️ = Declining

After:
<strong>Legend:</strong> Bold = Leaders | Regular = Established | Italic = Declining
```

**Step 6: Generate and verify PDF**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --print-to-pdf="/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/competitive-positioning-viz-ENTERPRISE.pdf" \
  "file:///Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/competitive-positioning-viz.html"
```

Verify:
- [ ] ASCII maps render correctly
- [ ] Maia rows have subtle gray background
- [ ] No emojis
- [ ] All 3 positioning maps fit on pages

**Step 7: Commit**

```bash
git add competitive-positioning-viz.html competitive-positioning-viz-ENTERPRISE.pdf
git commit -m "refactor: convert competitive positioning to enterprise format

- Remove star emojis from platform names
- Clean ASCII positioning maps
- Grayscale styling throughout"
```

---

### Task 2.4: Refactor strategic-recommendations-viz.html (354 lines)

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/strategic-recommendations-viz.html`

**Step 1: Backup and replace styles**

```bash
cp strategic-recommendations-viz.html strategic-recommendations-viz.html.backup-colorful
```

Replace style section with:

```html
<link rel="stylesheet" href="enterprise-styles.css">
<style>
    .recommendation {
        background: #ffffff;
        border: 1px solid #000000;
        padding: 20px;
        margin-bottom: 25px;
        page-break-inside: avoid;
    }

    .rec-header {
        border-bottom: 2px solid #000000;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    .rec-number {
        font-size: 18pt;
        font-weight: 700;
        color: #000000;
    }

    .rec-title {
        font-size: 14pt;
        font-weight: 600;
        color: #000000;
    }

    .tier-badge {
        display: inline-block;
        padding: 4px 10px;
        border: 1px solid #000000;
        border-radius: 3px;
        font-size: 9pt;
        font-weight: 600;
        margin-left: 10px;
    }

    .tier-1 {
        background: #cccccc;
    }

    .tier-2 {
        background: #e0e0e0;
    }

    .tier-3 {
        background: #f5f5f5;
    }
</style>
```

**Step 2: Remove colored boxes and badges**

Replace tier badge colors with grayscale classes as defined above.

Remove gradient/colored backgrounds from recommendation boxes.

**Step 3: Generate and verify PDF**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --print-to-pdf="/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/strategic-recommendations-viz-ENTERPRISE.pdf" \
  "file:///Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/strategic-recommendations-viz.html"
```

Verify:
- [ ] 7 recommendations all visible
- [ ] Tier badges show gray shading
- [ ] No page breaks within recommendations

**Step 4: Commit**

```bash
git add strategic-recommendations-viz.html strategic-recommendations-viz-ENTERPRISE.pdf
git commit -m "refactor: convert strategic recommendations to enterprise format

- Grayscale tier badges
- Remove colorful boxes
- Optimize pagination"
```

---

### Task 2.5: Refactor threats-opportunities-viz.html (641 lines)

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/threats-opportunities-viz.html`

**Step 1: Backup and replace styles**

```bash
cp threats-opportunities-viz.html threats-opportunities-viz.html.backup-colorful
```

**Step 2: Replace style section**

Use enterprise-styles.css as base, add file-specific styles for threat/opportunity cards.

**Step 3: Remove emojis from threat/opportunity headers**

Find and replace:
- `🔴` → Remove (use gray background instead)
- `🟡` → Remove
- `🟢` → Remove

**Step 4: Abbreviate long threat/opportunity descriptions**

Review each threat/opportunity card and shorten verbose text by ~20-30% to prevent wrapping.

**Step 5: Generate and verify PDF**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --print-to-pdf="/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/threats-opportunities-viz-ENTERPRISE.pdf" \
  "file:///Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/threats-opportunities-viz.html"
```

**Step 6: Commit**

```bash
git add threats-opportunities-viz.html threats-opportunities-viz-ENTERPRISE.pdf
git commit -m "refactor: convert threats-opportunities to enterprise format

- Remove emoji severity indicators
- Abbreviate verbose descriptions
- Grayscale priority shading"
```

---

### Task 2.6: Refactor pricing-analysis-top4-viz.html (567 lines)

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/pricing-analysis-top4-viz.html`

**Step 1: Backup and replace styles**

```bash
cp pricing-analysis-top4-viz.html pricing-analysis-top4-viz.html.backup-colorful
```

**Step 2: Replace gradient headers with grayscale**

Remove:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
```

Replace with:
```css
background: #333333;
color: #ffffff;
border: 1px solid #000000;
```

**Step 3: Convert star ratings to text**

Find and replace:
- `⭐⭐⭐⭐⭐ High` → `HIGH (5/5)`
- `⭐⭐⭐ Moderate` → `MODERATE (3/5)`
- `⭐⭐ Low` → `LOW (2/5)`
- `⭐ Very Low` → `VERY LOW (1/5)`

**Step 4: Remove colored callout boxes**

Replace:
```html
<!-- Before -->
<div class="critical-issue">

<!-- After -->
<div class="section" style="border-left: 3px solid #000000; background: #f5f5f5;">
```

**Step 5: Abbreviate pricing table content**

Review pricing comparison tables - shorten verbose cell content by 20-30%.

**Step 6: Generate and verify PDF**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --print-to-pdf="/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/pricing-analysis-top4-viz-ENTERPRISE.pdf" \
  "file:///Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/pricing-analysis-top4-viz.html"
```

Verify:
- [ ] Pricing tables fit on pages
- [ ] Star ratings converted to text
- [ ] No gradient backgrounds

**Step 7: Commit**

```bash
git add pricing-analysis-top4-viz.html pricing-analysis-top4-viz-ENTERPRISE.pdf
git commit -m "refactor: convert pricing analysis to enterprise format

- Remove gradient headers
- Convert star ratings to text
- Abbreviate table content"
```

---

### Task 2.7: Refactor target-segments-top4-viz.html (548 lines)

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/target-segments-top4-viz.html`

**Step 1: Backup and replace styles**

```bash
cp target-segments-top4-viz.html target-segments-top4-viz.html.backup-colorful
```

**Step 2: Apply enterprise CSS standards**

Link to enterprise-styles.css and remove colorful section backgrounds.

**Step 3: Abbreviate segment descriptions**

Shorten verbose geographic and segment descriptions to prevent table overflow.

**Step 4: Generate and verify PDF**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --print-to-pdf="/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/target-segments-top4-viz-ENTERPRISE.pdf" \
  "file:///Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/target-segments-top4-viz.html"
```

**Step 5: Commit**

```bash
git add target-segments-top4-viz.html target-segments-top4-viz-ENTERPRISE.pdf
git commit -m "refactor: convert target segments to enterprise format

- Grayscale styling
- Abbreviated segment descriptions"
```

---

### Task 2.8: Refactor market-positioning-top4-viz.html (863 lines)

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/market-positioning-top4-viz.html`

**Step 1: Backup and replace styles**

```bash
cp market-positioning-top4-viz.html market-positioning-top4-viz.html.backup-colorful
```

**Step 2: Remove gradient backgrounds from headers**

**Step 3: Clean messaging comparison tables**

Abbreviate verbose messaging comparisons to fit in table cells without wrapping.

**Step 4: Remove emojis from positioning analysis**

**Step 5: Generate and verify PDF**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --print-to-pdf="/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/market-positioning-top4-viz-ENTERPRISE.pdf" \
  "file:///Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/market-positioning-top4-viz.html"
```

**Step 6: Commit**

```bash
git add market-positioning-top4-viz.html market-positioning-top4-viz-ENTERPRISE.pdf
git commit -m "refactor: convert market positioning to enterprise format

- Remove gradients
- Abbreviate messaging tables
- Grayscale throughout"
```

---

### Task 2.9: Refactor technology-stack-top4-viz.html (1148 lines - COMPLEX)

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/technology-stack-top4-viz.html`

**Step 1: Backup original**

```bash
cp technology-stack-top4-viz.html technology-stack-top4-viz.html.backup-colorful
```

**Step 2: Replace style section**

This is a large file. Apply enterprise-styles.css and carefully review all section backgrounds.

**Step 3: Abbreviate technical descriptions**

Review AI/ML, integration, and security tables - shorten technical jargon where verbose.

**Step 4: Consider splitting very long tables**

If any single table exceeds 30-40 rows, consider splitting into sub-sections with repeated headers.

**Step 5: Generate and verify PDF**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --print-to-pdf="/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/technology-stack-top4-viz-ENTERPRISE.pdf" \
  "file:///Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/technology-stack-top4-viz.html"
```

Verify carefully:
- [ ] All tables fit on pages
- [ ] No text overflow
- [ ] Technical terms don't wrap awkwardly
- [ ] Page breaks occur logically

**Step 6: Commit**

```bash
git add technology-stack-top4-viz.html technology-stack-top4-viz-ENTERPRISE.pdf
git commit -m "refactor: convert technology stack to enterprise format

- Grayscale styling for large document
- Abbreviate technical descriptions
- Optimize table pagination
- Split oversized tables if needed"
```

---

### Task 2.10: Refactor feature-comparison-matrix-top4-viz.html (1785 lines - LARGEST & MOST COMPLEX)

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/feature-comparison-matrix-top4-viz.html`

**Step 1: Backup original**

```bash
cp feature-comparison-matrix-top4-viz.html feature-comparison-matrix-top4-viz.html.backup-colorful
```

**Step 2: Replace gradient header styles**

Remove purple gradient:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Replace with:
```css
background: #333333;
color: #ffffff;
border: 1px solid #000000;
```

**Step 3: Convert emoji gap indicators**

Find and replace:
- `🔴 CRITICAL GAPS` → `CRITICAL GAPS`
- `🟡 MODERATE GAPS` → `MODERATE GAPS`
- `🟢 MAIA'S UNIQUE STRENGTHS` → `MAIA'S UNIQUE STRENGTHS`

**Step 4: Review 50+ feature rows for text wrapping**

This is the MOST CRITICAL step. Go through each feature row and:
- Abbreviate feature names if over 30 characters
- Shorten descriptions to 10-15 words max
- Use bullet points or abbreviations

Example:
```html
<!-- Before -->
<td>Direct admissions workflow support with application-free college matching and guided decision tools</td>

<!-- After -->
<td>Direct admissions workflow, app-free matching, decision tools</td>
```

**Step 5: Consider landscape orientation for this file**

Add to print styles:
```css
@page {
    size: letter landscape;
    margin: 0.5in;
}
```

Test if landscape improves table readability for 5-column comparison.

**Step 6: Split into multiple category tables if needed**

If single 50-feature table causes overflow, split into:
- College Planning Features (15 features)
- Career Exploration Features (12 features)
- Administrative Features (10 features)
- AI & Technology Features (8 features)
- Integration Features (5 features)

Each sub-table gets its own section with header.

**Step 7: Generate and verify PDF**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --print-to-pdf="/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/feature-comparison-matrix-top4-viz-ENTERPRISE.pdf" \
  "file:///Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/feature-comparison-matrix-top4-viz.html"
```

**CRITICAL VERIFICATION:**
- [ ] All 50+ features visible
- [ ] No table overflow horizontally
- [ ] Text fits in cells without awkward wrapping
- [ ] Page breaks occur between logical feature categories
- [ ] Headers repeat on multi-page tables
- [ ] Maia column has subtle gray background
- [ ] No gradient backgrounds anywhere

**Step 8: Commit**

```bash
git add feature-comparison-matrix-top4-viz.html feature-comparison-matrix-top4-viz-ENTERPRISE.pdf
git commit -m "refactor: convert feature matrix to enterprise format (LARGEST FILE)

- Remove gradient backgrounds
- Abbreviate 50+ feature descriptions
- Optimize 5-column table layout
- Consider landscape orientation
- Split into category sub-tables if needed
- Critical pagination fixes"
```

---

## Phase 3: Final Quality Assurance

### Task 3.1: Batch regenerate all 10 enterprise PDFs

**Files:**
- Generate: All 10 `-ENTERPRISE.pdf` files

**Step 1: Create batch PDF generation script**

Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/generate-enterprise-pdfs.sh`

```bash
#!/bin/bash
# Batch generate enterprise PDFs from refactored HTML files

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
VIZ_DIR="/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS"

FILES=(
    "swot-analysis-viz"
    "competitive-positioning-viz"
    "market-trends-viz"
    "strategic-recommendations-viz"
    "threats-opportunities-viz"
    "pricing-analysis-top4-viz"
    "target-segments-top4-viz"
    "market-positioning-top4-viz"
    "technology-stack-top4-viz"
    "feature-comparison-matrix-top4-viz"
)

echo "Generating enterprise PDFs..."

for file in "${FILES[@]}"; do
    echo "Processing: ${file}.html"
    "$CHROME" \
        --headless \
        --disable-gpu \
        --print-to-pdf="${VIZ_DIR}/${file}-ENTERPRISE.pdf" \
        "file://${VIZ_DIR}/${file}.html"
    echo "✓ Generated: ${file}-ENTERPRISE.pdf"
done

echo ""
echo "Complete! Generated 10 enterprise PDFs."
ls -lh *-ENTERPRISE.pdf
```

**Step 2: Make script executable and run**

```bash
chmod +x generate-enterprise-pdfs.sh
./generate-enterprise-pdfs.sh
```

**Step 3: Verify all 10 PDFs generated**

```bash
ls -lh *-ENTERPRISE.pdf | wc -l
```

Expected: 10

**Step 4: Commit batch script**

```bash
git add generate-enterprise-pdfs.sh
git commit -m "feat: add batch PDF generation script for enterprise visualizations"
```

---

### Task 3.2: Create QA checklist and verify each PDF

**Step 1: Create QA checklist document**

Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/ENTERPRISE-QA-CHECKLIST.md`

```markdown
# Enterprise Visualization QA Checklist

**Date:** 2025-11-21
**Reviewer:** [Your Name]
**Purpose:** Verify all 10 enterprise PDFs meet C-suite quality standards

---

## Universal Checks (All 10 PDFs)

### Visual Styling
- [ ] No colorful gradient backgrounds (grayscale only)
- [ ] No emojis (🔴 🟡 🟢 ⭐) visible
- [ ] Priority badges use gray shading (not colors)
- [ ] Tables use minimal black borders
- [ ] Maia Learning rows have subtle gray background (#f5f5f5)
- [ ] Headers are black text on white or dark gray backgrounds

### Layout & Pagination
- [ ] Tables fit on pages (no horizontal overflow)
- [ ] Text wraps naturally (no awkward single-word lines)
- [ ] No orphaned table rows at page breaks
- [ ] Headers repeat on multi-page tables
- [ ] Adequate whitespace at bottom of pages
- [ ] Page breaks occur at logical section boundaries

### Typography & Readability
- [ ] Body text 12pt (narrative) or 10pt (tables)
- [ ] Headers 14-24pt, bold, readable
- [ ] Text contrast sufficient (dark text on white)
- [ ] No text cutoff or truncation
- [ ] Lists and bullets render correctly

---

## File-Specific Checks

### 1. swot-analysis-viz-ENTERPRISE.pdf (386 lines source)
- [ ] 4 competitor SWOT analyses visible
- [ ] Page break after each competitor
- [ ] Threat level badges use gray shading
- [ ] SWOT tables (Strengths/Weaknesses/Opportunities/Threats) fit on pages

### 2. competitive-positioning-viz-ENTERPRISE.pdf (315 lines)
- [ ] 3 positioning maps render correctly
- [ ] ASCII art maps display properly
- [ ] Maia platform highlighted subtly
- [ ] No emoji stars in maps

### 3. market-trends-viz-ENTERPRISE.pdf (312 lines)
- [ ] All 10 trends visible
- [ ] Tier sections (1/2/3) clearly delineated
- [ ] Priority badges grayscale
- [ ] Impact/Position columns readable

### 4. strategic-recommendations-viz-ENTERPRISE.pdf (354 lines)
- [ ] 7 recommendations all present
- [ ] Tier badges (1/2/3) use gray shading
- [ ] No page breaks within single recommendation
- [ ] Investment figures and timelines clear

### 5. threats-opportunities-viz-ENTERPRISE.pdf (641 lines)
- [ ] 8 threats visible
- [ ] 10 opportunities visible
- [ ] Severity indicators grayscale
- [ ] Descriptions abbreviated appropriately

### 6. pricing-analysis-top4-viz-ENTERPRISE.pdf (567 lines)
- [ ] Pricing comparison table fits
- [ ] Star ratings converted to text (HIGH, MODERATE, LOW)
- [ ] No gradient headers
- [ ] Critical issue callouts use gray borders

### 7. target-segments-top4-viz-ENTERPRISE.pdf (548 lines)
- [ ] Geographic segment tables fit
- [ ] School type comparisons readable
- [ ] Segment descriptions abbreviated

### 8. market-positioning-top4-viz-ENTERPRISE.pdf (863 lines)
- [ ] Messaging comparison tables fit
- [ ] Positioning quadrants clear
- [ ] No emoji indicators
- [ ] Strategic implications readable

### 9. technology-stack-top4-viz-ENTERPRISE.pdf (1148 lines - COMPLEX)
- [ ] AI/ML comparison table fits
- [ ] Integration tables readable
- [ ] Security/compliance sections clear
- [ ] Technical descriptions abbreviated
- [ ] Long tables split appropriately

### 10. feature-comparison-matrix-top4-viz-ENTERPRISE.pdf (1785 lines - LARGEST)
- [ ] All 50+ features visible
- [ ] 5-column comparison table fits (consider landscape?)
- [ ] Feature descriptions abbreviated
- [ ] Category sections clearly separated
- [ ] Gap analysis sections readable
- [ ] Final threat assessment table fits

---

## Overall Quality Assessment

**Pass Criteria:** All checkboxes above marked ✓

**Issues Found:** [Document any problems here]

**Action Items:** [List fixes needed]

**Final Verdict:** [ ] APPROVED FOR C-SUITE DISTRIBUTION / [ ] NEEDS REVISION

---

**Completed By:** ___________________
**Date:** ___________________
```

**Step 2: Manually review all 10 PDFs**

Open each PDF and systematically check all boxes above.

**Step 3: Document any issues found**

If any PDF fails checks, document specific issues in QA checklist.

**Step 4: Commit QA checklist**

```bash
git add ENTERPRISE-QA-CHECKLIST.md
git commit -m "docs: add QA checklist for enterprise visualization PDFs"
```

---

### Task 3.3: Fix any issues identified during QA

**Step 1: Review QA checklist issues**

Read documented issues from Task 3.2.

**Step 2: Prioritize fixes**

Critical issues (blocking C-suite distribution):
- Table overflow
- Text truncation
- Missing content

Nice-to-have fixes:
- Minor styling inconsistencies
- Slight layout improvements

**Step 3: Fix each issue and regenerate PDF**

For each issue:
1. Edit HTML file
2. Regenerate PDF
3. Re-verify against QA checklist
4. Commit fix

Example:
```bash
# Fix swot-analysis table overflow
# Edit swot-analysis-viz.html (abbreviate text)
# Regenerate PDF
./generate-enterprise-pdfs.sh
# Verify fix
# Commit
git add swot-analysis-viz.html swot-analysis-viz-ENTERPRISE.pdf
git commit -m "fix: abbreviate SWOT table content to prevent overflow"
```

**Step 4: Repeat until all QA checks pass**

---

### Task 3.4: Replace original colorful PDFs with enterprise versions

**Files:**
- Delete: Original colorful PDFs (10 files)
- Rename: `-ENTERPRISE.pdf` → `.pdf` (production versions)

**Step 1: Backup original colorful PDFs**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS

mkdir -p ../ARCHIVE/COLORFUL-ORIGINALS
mv *-viz.pdf ../ARCHIVE/COLORFUL-ORIGINALS/
```

**Step 2: Rename enterprise PDFs to production names**

```bash
for file in *-ENTERPRISE.pdf; do
    mv "$file" "${file/-ENTERPRISE/}"
done
```

Verify:
```bash
ls -lh *.pdf
```

Expected: 10 PDF files without "-ENTERPRISE" suffix

**Step 3: Update README to document change**

Add to `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/README.md`:

```markdown
## Enterprise Refactor (November 21, 2025)

**Changes:**
- Converted all visualizations to conservative grayscale styling
- Removed colorful backgrounds, gradients, and emojis
- Optimized for C-suite digital viewing on laptops/monitors
- Fixed table pagination and text overflow issues
- Applied enterprise consulting-grade aesthetics

**Backup:** Original colorful versions archived in `../ARCHIVE/COLORFUL-ORIGINALS/`
```

**Step 4: Commit production PDFs**

```bash
git add *.pdf ../ARCHIVE/COLORFUL-ORIGINALS/*.pdf
git commit -m "feat: replace colorful PDFs with enterprise grayscale versions

- All 10 visualizations now use conservative styling
- Removed emojis, gradients, colored backgrounds
- Optimized pagination and layout for digital viewing
- Original colorful versions archived
- Ready for C-suite distribution via Google Drive"
```

---

## Phase 4: Documentation & Cleanup

### Task 4.1: Create migration summary document

**Files:**
- Create: `/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS/ENTERPRISE-MIGRATION-SUMMARY.md`

```markdown
# Enterprise Visualization Migration Summary

**Date:** November 21, 2025
**Project:** Maia Learning Competitive Analysis
**Scope:** 10 visualization HTML/PDF files refactored to enterprise standards

---

## Executive Summary

Successfully converted all 10 competitive analysis visualization files from colorful consumer-style aesthetics to conservative enterprise-grade professional styling optimized for C-suite digital viewing.

**Result:** Clean, readable, professional PDFs suitable for board meetings and strategic planning sessions.

---

## Changes Applied

### Visual Styling
- **Before:** Colorful gradients (purple, pink, blue), emoji indicators (🔴 🟡 🟢 ⭐), bright colored section backgrounds
- **After:** Conservative grayscale palette, text-based priority indicators, minimal black borders, subtle gray shading

### Layout & Pagination
- **Before:** Tables overflowing pages, awkward text wrapping, inconsistent page breaks
- **After:** Intelligent page breaks, abbreviated content, optimized table layouts, headers repeat on multi-page tables

### Typography
- **Before:** Mixed sizing, colorful headers
- **After:** Standardized 12pt narrative/10pt tables, black headers with minimal borders

---

## Files Modified

| File | Original Lines | Changes | Status |
|------|---------------|---------|--------|
| swot-analysis-viz.html | 386 | ✓ Grayscale, emoji removal, tier badges | Complete |
| competitive-positioning-viz.html | 315 | ✓ ASCII map cleanup, star removal | Complete |
| market-trends-viz.html | 312 | ✓ Trend tier indicators, content abbreviation | Complete |
| strategic-recommendations-viz.html | 354 | ✓ Tier badge grayscale | Complete |
| threats-opportunities-viz.html | 641 | ✓ Severity indicators, content abbreviation | Complete |
| pricing-analysis-top4-viz.html | 567 | ✓ Star rating conversion, gradient removal | Complete |
| target-segments-top4-viz.html | 548 | ✓ Segment table optimization | Complete |
| market-positioning-top4-viz.html | 863 | ✓ Messaging table abbreviation | Complete |
| technology-stack-top4-viz.html | 1148 | ✓ Technical content abbreviation, table splits | Complete |
| feature-comparison-matrix-top4-viz.html | 1785 | ✓ 50+ feature abbreviation, landscape layout | Complete |

**Total:** 6,919 lines of HTML refactored

---

## Quality Assurance

**QA Process:**
- Created 10-point checklist for each PDF
- Verified no table overflow, text wrapping issues
- Confirmed grayscale styling throughout
- Tested digital viewing on laptop screens

**Result:** ✅ All 10 PDFs approved for C-suite distribution

---

## Technical Details

### CSS Standards
- Created `enterprise-styles.css` (shared base)
- Grayscale palette: #ffffff, #333333, #666666, #000000, #f5f5f5
- Print-optimized `@page` rules for PDF generation
- Intelligent `page-break-inside: avoid` rules

### Content Abbreviation
- Reduced verbose table cells by 20-30%
- Prioritized titles over descriptions
- Converted visual indicators (emojis, stars) to text

### PDF Generation
- Chrome headless `--print-to-pdf` command
- Batch generation script created
- Letter portrait orientation (landscape for wide tables)

---

## Distribution Ready

**Target Audience:** C-suite executives, board members, strategic planning teams

**Delivery Method:** Google Drive shared folder (digital viewing on laptops/monitors)

**File Format:** PDF (generated from HTML, print-optimized)

**Quality Level:** ⭐⭐⭐⭐⭐ Enterprise consulting-grade (McKinsey/BCG/Bain standards)

---

## Archive

**Original Colorful Versions:** Backed up to `../ARCHIVE/COLORFUL-ORIGINALS/`

**Restore Command (if needed):**
```bash
cp ../ARCHIVE/COLORFUL-ORIGINALS/*.pdf .
```

---

**Migration Completed By:** [Your Name]
**Date:** November 21, 2025
**Status:** ✅ COMPLETE - Ready for C-suite distribution
```

**Step 1: Save migration summary**

(File created above)

**Step 2: Commit documentation**

```bash
git add ENTERPRISE-MIGRATION-SUMMARY.md
git commit -m "docs: add enterprise migration summary

- Documents complete refactor of 10 visualization files
- 6,919 lines of HTML converted to grayscale
- QA verified, ready for C-suite distribution"
```

---

### Task 4.2: Update main project README

**Files:**
- Modify: `/Users/seancurrie/Desktop/MaiaLearningResearch/README.md`

**Step 1: Add enterprise refactor notice**

Add after line 120 (Current Status section):

```markdown
### Recent Updates

**November 21, 2025 - Enterprise Visualization Refactor**
- All 10 visualization PDFs converted to enterprise-grade professional styling
- Removed colorful gradients, emojis, and consumer aesthetics
- Optimized for C-suite digital viewing (laptops/monitors via Google Drive)
- Fixed table pagination and text overflow issues
- See `05-FINAL-DELIVERABLES/VISUALIZATIONS/ENTERPRISE-MIGRATION-SUMMARY.md`
```

**Step 2: Commit README update**

```bash
git add README.md
git commit -m "docs: update README with enterprise visualization refactor notice"
```

---

### Task 4.3: Create final summary for user

**Step 1: Generate file size comparison**

```bash
cd /Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/VISUALIZATIONS

echo "Original Colorful PDFs:"
ls -lh ../ARCHIVE/COLORFUL-ORIGINALS/*.pdf | awk '{print $9, $5}'

echo ""
echo "Enterprise Grayscale PDFs:"
ls -lh *.pdf | awk '{print $9, $5}'
```

**Step 2: Create completion summary**

Print to console:

```
========================================
ENTERPRISE VISUALIZATION REFACTOR COMPLETE
========================================

Files Processed: 10 HTML + 10 PDF files
Total Lines Refactored: 6,919 lines
Time Estimate: 4-6 hours

Changes Applied:
✓ Grayscale color palette (no gradients, emojis, or bright colors)
✓ Fixed table pagination (no overflow)
✓ Abbreviated verbose content (improved readability)
✓ Optimized for digital viewing (C-suite laptops/monitors)
✓ Enterprise consulting-grade aesthetics

Quality Assurance:
✓ All 10 PDFs verified against QA checklist
✓ No table overflow or text wrapping issues
✓ Headers repeat on multi-page tables
✓ Maia Learning rows subtly highlighted

Distribution Ready:
✓ Professional PDFs suitable for board meetings
✓ Optimized for Google Drive sharing
✓ C-suite approved quality level

Archive:
✓ Original colorful versions backed up to ../ARCHIVE/COLORFUL-ORIGINALS/

Next Steps:
1. Review all 10 PDFs in 05-FINAL-DELIVERABLES/VISUALIZATIONS/
2. Upload to Google Drive for C-suite distribution
3. Share link with executives

========================================
```

---

## Execution Guidance

### Estimated Timeline
- **Phase 1** (CSS Standards): 30 minutes
- **Phase 2** (10 File Refactors): 4-5 hours (30-45 min per file)
- **Phase 3** (QA & Fixes): 1-2 hours
- **Phase 4** (Documentation): 30 minutes

**Total:** 6-8 hours

### Critical Success Factors
1. **Test PDFs after EACH file refactor** (don't batch all 10 then test)
2. **Abbreviate content aggressively** (C-suite prefers concise)
3. **Prioritize layout over aesthetics** (fitting on page > visual appeal)
4. **Use QA checklist rigorously** (systematic verification prevents rework)

### Common Pitfalls to Avoid
- Skipping PDF generation until all files done (test incrementally!)
- Insufficient content abbreviation (tables still overflow)
- Forgetting page-break CSS (orphaned rows)
- Not testing on laptop screen (digital viewing target)

---

## Plan Complete

**Plan saved to:** `docs/plans/2025-11-21-enterprise-visualization-refactor.md`

**Two execution options:**

**1. Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration with quality gates

**2. Parallel Session (separate)** - Open new session with executing-plans skill, batch execution with checkpoints

**Which approach would you prefer?**
