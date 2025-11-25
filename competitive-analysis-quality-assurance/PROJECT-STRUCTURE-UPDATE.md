# Project Structure Efficiency Update

**Date:** November 17, 2025  
**Change:** Added project structure awareness to research-quality-assurance skill

---

## What Changed

**Added a "Typical Project Structure" section** to the skill that documents common research project organization:

```
ProjectName/
├── 00-PROJECT-OVERVIEW/          # Research objectives, progress tracker
├── 01-COMPANY-PROFILES/          # Client/baseline company profile
├── 02-COMPETITOR-PROFILES/       # Individual competitor deep-dives
├── 02-RAW-RESEARCH-DATA/        # Search results, scraped content
├── 03-COMPARATIVE-ANALYSIS/     # Feature matrices, pricing, positioning
├── 04-STRATEGIC-INSIGHTS/       # SWOT, competitive maps, recommendations
├── 05-DELIVERABLES/             # Executive summaries, reports, presentations
└── 06-PROJECT-MANAGEMENT/       # Task trackers, methodology notes
```

**Added guidance to Phase 1 (Scope the Review):**
- Check filesystem for common project structure first
- Identify available documents before asking clarifying questions
- This allows more specific and efficient QA scoping

---

## Why This Helps

**Before:**
You'd need to tell the skill exactly which files to review:
```
"Review the file at /Users/.../MaiaLearningResearch/02-COMPETITOR-PROFILES/01-NAVIANCE-profile.md"
```

**After:**
The skill knows where to look:
```
"Review the Naviance competitor profile"
```

The skill will automatically check `02-COMPETITOR-PROFILES/` for Naviance-related files.

---

## Benefits

✅ **Less Searching** - Skill knows where different document types live  
✅ **Faster QA** - No need to provide full file paths  
✅ **Smarter Questions** - Skill can ask "Should I review all 7 competitor profiles?" instead of "What files?"  
✅ **Better Context** - Understanding project structure helps prioritize what to review  

---

## Example Usage

**You:**
"Do a standard review of all competitor profiles"

**Skill (internally):**
1. Checks filesystem for `02-COMPETITOR-PROFILES/` directory
2. Lists all files in that directory
3. Identifies 7 competitor profile files
4. Asks: "I found 7 competitor profiles. Should I review all of them or specific ones?"

**More Efficient Than:**
You having to list all 7 file paths manually!

---

## Notes

- This makes the skill "project structure aware" without being project-specific
- Works for any research project using this common directory structure
- Still flexible - you can provide exact paths if needed
- Skill will adapt if your structure is different

---

**Updated skill file:** [research-quality-assurance.skill](computer:///mnt/user-data/outputs/research-quality-assurance.skill)
