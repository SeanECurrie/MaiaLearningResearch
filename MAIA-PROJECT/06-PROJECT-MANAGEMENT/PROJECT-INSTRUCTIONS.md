# PROJECT INSTRUCTIONS - Maia Learning Competitive Analysis

**READ THIS FIRST when starting any conversation about this project.**

---

## 🎯 Project Mission

Conduct enterprise-grade competitive analysis of **Maia Learning** against 7 key competitors in the college and career readiness platform market. Deliver consulting-quality research, analysis, and strategic recommendations.

---

## 📁 Project Location

**Directory:** `/Users/seancurrie/Desktop/MaiaLearningResearch/`

**Key Files to Check First:**
1. **06-PROJECT-MANAGEMENT/CONTINUATION-NOTES.md** - Where we left off
2. **06-PROJECT-MANAGEMENT/TASK-TRACKER.md** - Current task status and checkboxes
3. **00-PROJECT-OVERVIEW/progress-tracker.md** - Overall phase progress
4. **README.md** - Project overview and structure

---

## 🏗️ Project Structure

```
MaiaLearningResearch/
├── 00-PROJECT-OVERVIEW/          # Research objectives, competitor rationale, progress tracker
├── 01-COMPANY-PROFILES/          # Individual deep-dives on 8 companies
├── 02-RAW-RESEARCH-DATA/         # Search results and scraped content
├── 03-COMPARATIVE-ANALYSIS/      # Feature matrices, pricing, positioning
├── 04-STRATEGIC-INSIGHTS/        # SWOT, competitive maps, recommendations
├── 05-DELIVERABLES/              # Executive summary, full report, presentation
├── 06-PROJECT-MANAGEMENT/        # Task tracker, continuation notes, methodology
├── PROGRESS-REPORTS/             # Timestamped progress updates
└── README.md                     # Project guide
```

---

## 🎓 The 8 Companies

**Client (Baseline):**
1. Maia Learning ✅ COMPLETE

**7 Competitors to Research:**
2. Naviance (PowerSchool) - Market leader, next priority
3. SCOIR - Modern challenger
4. SchooLinks - Comprehensive K-12
5. Xello - Career-focused
6. Cialfo - AI-powered global
7. MajorClarity (Edmentum) - CTE focus
8. Common App - Ecosystem infrastructure

---

## 📊 Current Status

**For current status, always check:**
1. **CONTINUATION-NOTES.md** (this folder) - Latest entry shows what's done, what's next
2. **TASK-TRACKER.md** (this folder) - Detailed task-by-task progress with checkboxes

**Phase Breakdown:**
- Phase 1: Foundation ✅ COMPLETE (100%)
- Phase 2: Data Collection 🔄 IN PROGRESS (see CONTINUATION-NOTES.md for %)
- Phase 3: Comparative Analysis ⏳ NOT STARTED
- Phase 4: Strategic Insights ⏳ NOT STARTED
- Phase 5: Deliverables ⏳ NOT STARTED

---

## 🔧 Research Methodology

### Approach: Balanced Coverage
- **8-10 tool calls** per competitor for initial research
- **Systematic process:** Search → Scrape → Profile → Document
- **Quality focus:** Primary sources, cross-referencing, citations
- **Iterative design:** Broad first pass, then targeted deep dives

### Tools Available

**Primary: competitive-research-brightdata Skill**

This project uses a specialized Claude skill that provides enterprise-grade research methodology:

**What the skill provides:**
- **5-Phase Research Workflow:** Clarify → Plan → Execute → Analyze → Report
- **Analytical Frameworks:** SWOT, Porter's Five Forces, Business Model Canvas, competitive positioning
- **Report Templates:** Company profiles, competitive analysis, market entry, product comparison
- **Best Practices:** Search strategies, source prioritization, quality assurance, efficiency techniques

**Skill auto-activates when you:**
- Research companies
- Conduct competitive analysis
- Create market reports
- Compare products/services
- Analyze industries

**Installation (first time):**
- Run `bash scripts/install-skill.sh` from project root
- Restart Claude CLI to activate
- See `FOR-PROJECT-KNOWLEDGE.md` for details

**Bright Data MCP Tools (used by the skill):**
- `search_engine` - Google/Bing/Yandex searches
- `search_engine_batch` - Up to 10 parallel searches (use for efficiency!)
- `scrape_as_markdown` - Extract clean webpage content
- `scrape_batch` - Up to 10 parallel scrapes (use for efficiency!)

**How it works:**
The skill operates autonomously - Claude automatically invokes it based on your research requests. It loads reference materials (methodology, frameworks, templates) progressively as needed, managing context efficiently.

### Per-Competitor Research Process
1. Execute batch search (8-10 queries covering company, products, pricing, news, reviews, vs competitors)
2. Scrape key website pages (homepage, about, products, pricing if available)
3. Write comprehensive company profile following Maia Learning template
4. Add all sources to sources-index.md
5. Update TASK-TRACKER.md with completion and summary
6. Update progress-tracker.md

---

## ✅ Task Completion Protocol

**When completing ANY task:**
1. ✅ Check off the task checkbox in TASK-TRACKER.md
2. 📝 Fill in the Summary field (2-3 sentences)
3. ⏱️ Update time spent
4. 📊 Update phase progress percentage
5. 🎯 Identify next task

**When conversation limit approaching:**
1. Update TASK-TRACKER.md with current status
2. Add entry to CONTINUATION-NOTES.md with context
3. Note what was happening and what's next

---

## 🚀 How to Start Working

### First Time in New Conversation
1. **Read CONTINUATION-NOTES.md** - See where we left off
2. **Check TASK-TRACKER.md** - Find current task
3. **Review relevant docs** - Understand context
4. **Start working** - Execute next task
5. **Update as you go** - Keep trackers current

### If User Wants to Brainstorm/Discuss
1. **Check progress-tracker.md** - Get current phase status
2. **Review completed work** - Read relevant profiles/analyses
3. **Reference findings** - Ground discussion in research
4. **Note insights** - Add to relevant docs if valuable

### If User Asks "Where Are We?"
1. Check TASK-TRACKER.md Quick Status Dashboard
2. Reference CONTINUATION-NOTES.md latest entry
3. Summarize current phase, progress %, next task
4. Offer to show details from any specific area

---

## 🎯 Quality Standards

**Research Quality:**
- All claims cited with sources (URL + access date)
- Primary sources prioritized (official company sites)
- Recent information emphasized (2024-2025)
- Key facts verified from 2-3 independent sources
- Data gaps clearly noted

**Documentation Quality:**
- Consistent formatting across all documents
- Professional, consulting-grade writing
- Clear, actionable insights
- Suitable for C-level presentation

---

## ⚠️ Important Notes

**Scope Boundaries:**
- 7 competitors only (don't add more without discussion)
- Focus on user-facing features (not deep technical architecture)
- Accept data gaps for private companies (pricing, financials)
- Prioritize 2024-2025 information

**Skill Usage:**
- Use the competitive-research-brightdata skill - it's built for this
- The skill knows to clarify, plan, research, analyze, report
- Follow the skill's best practices for consulting frameworks

**Conversation Management:**
- MCP tools use tokens heavily - conversations will end mid-work
- That's okay! The task tracker system handles handoffs
- Always update TASK-TRACKER.md and CONTINUATION-NOTES.md before limits hit
- Next conversation can pick up seamlessly

---

## 🆘 Emergency Procedures

### If Conversation Limit Hit Mid-Task
1. Update TASK-TRACKER.md with current status
2. Write summary in task's Summary field
3. Check off completed sub-tasks
4. Add entry to CONTINUATION-NOTES.md
5. Next conversation: Read these instructions + continuation notes

### If Data Gap Discovered
1. Note gap in relevant document
2. Add to RESEARCH-GAPS.md
3. Flag for potential deep dive
4. Continue with available information

### If Methodology Needs Adjustment
1. Document issue
2. Propose solution in METHODOLOGY-NOTES.md
3. Discuss with user
4. Update docs if agreed
5. Continue with new approach

---

## 📖 Quick Reference Commands

**"Where are we?"**
→ Check TASK-TRACKER.md Quick Status Dashboard + CONTINUATION-NOTES.md

**"What's next?"**
→ Check CONTINUATION-NOTES.md latest entry + TASK-TRACKER.md current phase

**"Show me what we know about [competitor]"**
→ Read 01-COMPANY-PROFILES/[competitor].md

**"Let's work on the next task"**
→ Read CONTINUATION-NOTES.md, check TASK-TRACKER.md, execute next unchecked task

**"I want to brainstorm about [topic]"**
→ Review relevant completed research, discuss based on findings, note insights in relevant docs

---

## 🎓 Expected Behavior

**When starting conversation:**
- Immediately check CONTINUATION-NOTES.md and TASK-TRACKER.md
- Summarize current status concisely
- Ask if user wants to: (a) continue next task, (b) review progress, or (c) discuss/brainstorm

**When working on tasks:**
- Follow methodology in research-objectives.md
- Use competitive-research-brightdata skill
- Update TASK-TRACKER.md as you complete items
- Keep documentation professional and thorough

**When conversation limits approaching:**
- Update all trackers with current state
- Write clear continuation notes
- Don't worry - next conversation will pick up seamlessly

**When discussing/brainstorming:**
- Ground discussion in completed research
- Reference specific findings from profiles/analyses
- Suggest next research steps if gaps identified
- Keep strategic focus on Maia Learning's competitive position

---

## ✨ Success Metrics

**Project Complete When:**
- ✅ All 8 company profiles written and comprehensive
- ✅ All comparative analysis documents complete
- ✅ Strategic insights delivered (SWOT, positioning, recommendations)
- ✅ Executive summary suitable for C-level presentation
- ✅ Full report compiled and ready
- ✅ Presentation deck outline created

**Quality Indicators:**
- All claims backed by credible sources
- Insights actionable and strategic
- Analysis suitable for executive presentation
- Professional consulting-grade deliverable

---

**Last Updated:** 11-15-2025  
**Version:** 1.0  
**Next Review:** After Phase 2 completion

---

## 🚀 Ready to Start?

1. Check CONTINUATION-NOTES.md for latest status
2. Check TASK-TRACKER.md for current task
3. Ask user: "Continue with next task or discuss/review?"
4. Execute and update trackers as you work

**You've got this!** The system is designed for seamless handoffs. Just follow the task tracker and keep documentation updated.