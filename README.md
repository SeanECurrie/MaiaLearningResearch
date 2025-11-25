# Maia Learning Competitive Analysis Research

**Client:** Maia Learning
**Start Date:** 11-16-2024
**Scope:** 7 Competitors
**Status:** See `06-PROJECT-MANAGEMENT/CONTINUATION-NOTES.md` for current status

---

## Quick Start for AI Assistants

**When starting any conversation:**
1. Check `06-PROJECT-MANAGEMENT/CONTINUATION-NOTES.md` - where we left off
2. Check `06-PROJECT-MANAGEMENT/TASK-TRACKER.md` - current task
3. Summarize status and ask user: Continue | Review | Discuss

**Full context:** See `06-PROJECT-MANAGEMENT/PROJECT-INSTRUCTIONS.md`

---

## Skills Setup (First Time Only)

This project uses the **competitive-research-brightdata** Claude skill for enterprise-grade research methodology.

### Installation

```bash
bash scripts/install-skill.sh
```

Then restart Claude CLI to activate the skill.

### What the Skill Provides

- **5-Phase Research Workflow:** Clarify → Plan → Execute → Analyze → Report
- **Analytical Frameworks:** SWOT, Porter's Five Forces, competitive positioning
- **Report Templates:** Company profiles, competitive analysis, market intelligence
- **Best Practices:** Search strategies, batch operations, quality assurance

### Auto-Activation

The skill automatically activates when Claude detects research requests such as:
- "Research [company name]"
- "Conduct competitive analysis of X vs Y"
- "Create a market report for [industry]"
- "Compare [products/services]"

See `06-PROJECT-MANAGEMENT/PROJECT-INSTRUCTIONS.md` for detailed skill documentation.

---

## Directory Structure

### 00-PROJECT-OVERVIEW/
- **research-objectives.md** - 18 key research questions
- **competitor-selection-rationale.md** - Why these 7 competitors
- **progress-tracker.md** - Phase-level status (points to TASK-TRACKER for details)

### 01-COMPANY-PROFILES/
Individual company profiles (1/8 complete)
- maia-learning.md ✅
- [7 more to come]

### 02-RAW-RESEARCH-DATA/
- search-results/
- scraped-content/

### 03-COMPARATIVE-ANALYSIS/
Feature matrices, pricing, positioning (ready for Phase 3)

### 04-STRATEGIC-INSIGHTS/
SWOT, competitive maps, recommendations (ready for Phase 4)

### 05-DELIVERABLES/
Executive summary, full report, presentation (ready for Phase 5)

### 06-PROJECT-MANAGEMENT/ ⭐ START HERE
- **FOR-PROJECT-KNOWLEDGE.md** - Copy to Project Knowledge
- **PROJECT-INSTRUCTIONS.md** - Complete AI context
- **TASK-TRACKER.md** - Detailed task list with checkboxes
- **CONTINUATION-NOTES.md** - Conversation handoff notes
- **RESEARCH-GAPS.md** - Areas needing investigation
- **METHODOLOGY-NOTES.md** - Research decisions

### PROGRESS-REPORTS/
Timestamped updates

---

## The 8 Companies

1. Maia Learning ✅ (client baseline - complete)
2. Naviance (PowerSchool) ✅ (complete)
3. SCOIR - Next
4. SchooLinks
5. Xello
6. Cialfo
7. MajorClarity (Edmentum)
8. Common App

---

## Research Methodology

- **Approach:** 8-10 tool calls per competitor
- **Process:** Search → Scrape → Profile → Document
- **Quality:** Primary sources, 2024-2025 focus, cross-verification
- **Tools:** Bright Data competitive-research skill

---

## Current Status

**For up-to-date status, see:**
- **CONTINUATION-NOTES.md** - Latest entry shows what's done, what's next, current %
- **TASK-TRACKER.md** - Detailed task-by-task progress

---

**Last Updated:** 11-15-2025