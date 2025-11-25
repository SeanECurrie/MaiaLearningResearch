# Archive Directory

This directory contains files archived during the November 2025 repository normalization.

## Contents

### legacy-scripts/
One-off scripts created during the Maia Learning project that are no longer needed for framework operation:
- `convert-to-docx.js` - DOCX conversion utility
- `fix-scoir-pricing.py` - Pricing correction script
- `search-scoir-pricing.py` - Pricing search utility
- `project-scripts-pre-normalization/` - Original scripts directory

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
