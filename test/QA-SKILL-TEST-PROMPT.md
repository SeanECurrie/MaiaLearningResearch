# Quality Assurance Skill Test Prompt

**Purpose:** Test the competitive-analysis-quality-assurance skill on Phase 5 deliverables
**Output Location:** `/test` directory only
**Important:** Do NOT modify any existing files in `/05-FINAL-DELIVERABLES/`

---

## Prompt to Use (Copy/Paste After Restarting Claude Code)

```
I need you to activate the competitive-analysis-quality-assurance skill and conduct a comprehensive quality review of the Executive Summary we created for the Maia Learning competitive analysis project.

**Context:**
We just completed a 5-phase competitive research project analyzing 7 competitors in the College & Career Readiness (CCR) platform market. The project included:
- Phase 1: Foundation (Maia baseline profile)
- Phase 2: Data Collection (8 competitor profiles, 120,000+ words)
- Phase 3: Comparative Analysis (6 analyses, 25,000+ words)
- Phase 4: Strategic Insights (6 documents, 53,000+ words)
- Phase 5: Final Deliverables (Executive Summary, Full Report, Presentation Deck)

All research was conducted using the competitive-research-brightdata skill with enterprise consulting-grade methodology (400+ sources, systematic verification, strategic frameworks).

**Document to Review:**
`/Users/seancurrie/Desktop/MaiaLearningResearch/05-FINAL-DELIVERABLES/executive-summary.md`

**Review Scope:**
Please conduct a COMPREHENSIVE quality assurance review including:

1. **Fact-Checking:**
   - Verify all statistics (market share %, pricing, satisfaction ratings, funding amounts)
   - Validate competitor information (launch dates, features, geographic coverage)
   - Cross-reference key findings against Phase 2-4 source documents

2. **Source Validation:**
   - Check that all major claims are supported by evidence from the research
   - Verify consistency with underlying competitor profiles
   - Identify any unsupported assertions

3. **Consistency Review:**
   - Ensure terminology is consistent (competitor names, threat levels, metrics)
   - Verify data consistency (same statistics across different sections)
   - Check that strategic recommendations align with findings

4. **Quality Assessment:**
   - Evaluate against enterprise consulting standards (McKinsey/BCG/Bain quality)
   - Assess completeness (all required elements for executive summary)
   - Check professional tone and clarity for C-level audience

5. **Gap Identification:**
   - Note any missing information or areas needing clarification
   - Flag potential contradictions or unclear statements
   - Identify opportunities for strengthening claims

**Supporting Documents Available:**
You can cross-reference against all Phase 2-4 documents in:
- `/02-COMPETITOR-PROFILES/` (8 detailed profiles)
- `/03-COMPARATIVE-ANALYSES/` (feature comparison, pricing, technology, positioning, target segments, integration depth)
- `/04-STRATEGIC-INSIGHTS/` (SWOT analysis, competitive positioning map, market trends, threats-opportunities, strategic recommendations)

**Output Requirements:**
1. **Create a QA report:** `/Users/seancurrie/Desktop/MaiaLearningResearch/test/executive-summary-qa-report.md`
2. **Include sections:**
   - Executive Summary (pass/fail assessment, overall quality rating)
   - Fact-Checking Results (verified claims, questionable claims, errors found)
   - Source Validation Results (well-supported vs. under-supported claims)
   - Consistency Analysis (consistent vs. inconsistent elements)
   - Quality Assessment (completeness, accuracy, professionalism ratings)
   - Recommendations (improvements, corrections, enhancements)
   - Certification (ready for delivery yes/no, conditions if applicable)

3. **Format:**
   - Use clear sections with headers
   - Provide specific line references for issues found
   - Include severity ratings (🔴 Critical, 🟡 Medium, 🟢 Low)
   - Give overall quality score (⭐⭐⭐⭐⭐ format)

4. **Important Constraints:**
   - OUTPUT TO `/test` directory ONLY
   - DO NOT modify `/05-FINAL-DELIVERABLES/executive-summary.md`
   - DO NOT modify any Phase 2-4 documents
   - READ-ONLY review, no edits to source documents

**Expected Outcome:**
A comprehensive quality assurance report that validates the executive summary meets enterprise consulting standards and is ready for delivery to Maia Learning's C-level executives and board.

Please activate the competitive-analysis-quality-assurance skill and begin the review.
```

---

## Expected Behavior

When you paste this prompt after restarting Claude Code, you should see:

1. **Skill Activation Message:**
   ```
   <command-message>The "competitive-analysis-quality-assurance" skill is running</command-message>
   ```

2. **Skill Workflow:**
   - Phase 1: Scope the review (identify documents, clarify objectives)
   - Phase 2: Document analysis (read executive summary, map claims)
   - Phase 3: Source validation (cross-reference with Phase 2-4 documents)
   - Phase 4: Fact-checking (verify statistics, dates, claims)
   - Phase 5: Quality assessment (rate against consulting standards)
   - Phase 6: Report generation (create comprehensive QA report)

3. **Output File Created:**
   `/Users/seancurrie/Desktop/MaiaLearningResearch/test/executive-summary-qa-report.md`

4. **No Modifications:**
   - All files in `/05-FINAL-DELIVERABLES/` remain unchanged
   - All Phase 2-4 files remain unchanged
   - Only new file created in `/test` directory

---

## Alternative Test Scenarios

If you want to test different review depths after the initial test:

### Quick Scan (30 minutes)
```
Use the competitive-analysis-quality-assurance skill to do a RAPID SCAN of the executive summary at /05-FINAL-DELIVERABLES/executive-summary.md. Focus only on critical claims (market share, pricing, top 3 recommendations). Output quick-scan-report.md to /test directory.
```

### Targeted Fact-Check (1 hour)
```
Use the competitive-analysis-quality-assurance skill to fact-check all competitor statistics in the executive summary (market share %, pricing, satisfaction ratings, funding amounts). Verify against source documents. Output fact-check-report.md to /test directory.
```

### Consistency Audit (1 hour)
```
Use the competitive-analysis-quality-assurance skill to check consistency between the executive summary and the full competitive analysis report. Flag any contradictions or discrepancies. Output consistency-audit.md to /test directory.
```

---

## Troubleshooting

**If skill doesn't activate:**
1. Verify you restarted Claude Code
2. Check skill is installed: `ls ~/.claude/skills/` should show `competitive-analysis-quality-assurance.skill`
3. Try explicit invocation: "Activate the competitive-analysis-quality-assurance skill"

**If skill can't find documents:**
1. Check you're in the project directory: `/Users/seancurrie/Desktop/MaiaLearningResearch/`
2. Verify file paths are correct
3. Skill will auto-detect standard directory structure

**If output goes to wrong location:**
1. Explicitly state: "Output to /test directory ONLY"
2. Remind: "Do NOT modify existing deliverables"

---

## Success Criteria

The QA skill test is successful if:
- ✅ Skill activates (command message appears)
- ✅ Skill reads executive summary
- ✅ Skill cross-references Phase 2-4 documents
- ✅ Skill creates QA report in /test directory
- ✅ No modifications to existing files
- ✅ Report includes fact-checking, validation, consistency analysis, quality assessment
- ✅ Report provides overall quality rating and certification

---

**Created:** November 17, 2025
**Skill Version:** competitive-analysis-quality-assurance v1.0
**Test Target:** Executive Summary (6,500 words, Phase 5 deliverable)
**Expected Duration:** 1-2 hours (comprehensive review)
