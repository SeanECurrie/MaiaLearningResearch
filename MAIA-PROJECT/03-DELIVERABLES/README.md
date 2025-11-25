# 03-DELIVERABLES

## Purpose
Client-ready deliverables only. This directory contains final, QA-passed documents.

## Current Version

**Latest:** `v2.3-FINAL-2025-11-25/`

## Directory Structure

```
03-DELIVERABLES/
├── v2.3-FINAL-2025-11-25/      ← CURRENT (Enterprise styling, table borders, SWOT grid)
│   ├── PDF/                     ← 13 PDFs for distribution
│   ├── HTML/                    ← Source HTML files
│   └── DOCX/                    ← Word documents
├── archive/                     ← Previous versions (when applicable)
├── README.md                    ← This file
└── VERSION-HISTORY.md           ← Complete changelog
```

## Folder Naming Convention

**Format:** `v{major}.{minor}-FINAL-{YYYY-MM-DD}`

| Component | Meaning |
|-----------|---------|
| Major (v2) | Big changes (strategy pivot, new analysis) |
| Minor (.1) | Corrections, fixes, branding updates |
| FINAL | Client-ready status |
| Date | When finalized |

## Contents of Current Version

### PDF/ (13 files)
- `executive-summary-CORRECTED.pdf` - 15-page executive summary
- `full-report-CORRECTED.pdf` - 50+ page comprehensive report
- `Combined-Competitive-Analysis-Visualizations-ENTERPRISE.pdf` - All visualizations merged
- 10 individual visualization PDFs (`*-ENTERPRISE.pdf`)

### HTML/
- Source files for PDFs (edit these, then regenerate PDFs)
- `visualizations/` - Individual visualization HTML files

### DOCX/
- Word document versions for editing

## When to Use
- **Sharing with client:** Use PDFs from latest version folder
- **Making edits:** Edit HTML sources, regenerate PDFs
- **Comparing versions:** Check `archive/` folder

## Regenerating PDFs

After editing HTML files:
```bash
# Individual PDF
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="output.pdf" \
  "file:///path/to/source.html"

# Combined PDF (requires poppler)
pdfunite file1.pdf file2.pdf ... combined.pdf
```

## Related Directories
- `02-ANALYSIS-OUTPUTS/` - Source analysis for these deliverables
- `04-QA-DOCUMENTATION/` - QA reports for these deliverables
