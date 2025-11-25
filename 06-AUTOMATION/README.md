# 06-AUTOMATION

## Purpose
Scripts, templates, and automation tools for the competitive analysis workflow.

## Contents
- `scripts/` - Automation scripts (PDF generation, file conversion, etc.)
- `templates/` - Reusable templates (CSS, HTML base files)
  - `enterprise-styles.css` - Enterprise styling for visualizations

## Key Tools

### PDF Generation (Chrome Headless)
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu \
  --print-to-pdf="output.pdf" \
  "file://$(pwd)/input.html"
```

### Enterprise Styling
- Use `enterprise-styles.css` for consistent enterprise look
- Conservative grayscale palette for C-suite distribution
- Print-friendly CSS for PDF generation

## When to Use
- When generating PDFs from HTML
- When applying consistent styling across visualizations
- When automating repetitive tasks
- When setting up new projects

## Related Directories
- `03-DELIVERABLES/current/HTML/` - HTML files using these templates
- `templates/competitive-analysis/automation-scripts/` - Template scripts for new projects
