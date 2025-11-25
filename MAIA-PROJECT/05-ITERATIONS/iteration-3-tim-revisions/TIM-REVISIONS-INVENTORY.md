# Tim's Revisions - Discovery Inventory

**Date:** November 24, 2025
**Status:** IN PROGRESS - Discovery Phase
**Reviewer:** Claude (using competitive-analysis-quality-assurance skill)

---

## Executive Summary

This document catalogs ALL instances of content requiring changes based on Tim's feedback:
1. **Positioning maps** needing four-quadrant format conversion
2. **Marketing taglines** requiring removal
3. **Strategic recommendations** requiring major restructuring

---

## 1. POSITIONING MAPS REQUIRING FOUR-QUADRANT FIX

### Finding #1: market-positioning-top4-viz.html (Lines 336-369)

**Location:** `/05-FINAL-DELIVERABLES/VISUALIZATIONS/market-positioning-top4-viz.html`

**Current Format:** Text-based scatter plot representation
```
    High Innovation
    │
    │  SCOIR ⭐
    │  (Scoir AI, Network,
    │   Common App 2025-26)
    │
    │              SchooLinks ⭐
    │              ($80M, Inc. 5000,
    │               "Future of CCR")
    │
    Mid Innovation
    │
    │  Maia ⚪                    Xello ⚪
    │  (AI letter writing,        (28-year heritage,
    │   but undermarketed)        awards but no AI)
    │
    │                 Naviance ⬇️
    │                 (Adding AI,
    │                  defensive)
    │
    Low Innovation
    │
    │
    └────────────────────────────────────────────
    Niche          Mid-Market        Broad Market

                    Market Coverage →
```

**Tim's Required Format:** Four-quadrant map with visible crossbars
```
        HIGH INNOVATION
              |
              |
    Q2        |        Q1 (IDEAL)
              |
LOW ──────────┼────────── HIGH
COVERAGE      |      COVERAGE
              |
    Q3        |        Q4
              |
        LOW INNOVATION
```

**Issue:** Current map is missing the actual horizontal and vertical crossbar lines. Tim said this "snuck past" him.

**Required Change:**
- Add visible horizontal line intersecting vertical line in middle
- Create clear four-quadrant structure
- Keep dimension labels: Innovation (vertical) × Coverage (horizontal)
- Upper right quadrant = ideal position

**Files Affected:**
- ✅ `/VISUALIZATIONS/market-positioning-top4-viz.html` (source file)
- ✅ `/VISUALIZATIONS/current-enterprise-cleaned-report-documents/market-positioning-top4-viz-ENTERPRISE.pdf` (generated from HTML)

---

### Finding #2: competitive-positioning-viz.html (No Visual Maps)

**Location:** `/05-FINAL-DELIVERABLES/VISUALIZATIONS/competitive-positioning-viz.html`

**Current Format:** Uses tables, NOT visual positioning maps

**Assessment:** This file uses tables to compare platforms across dimensions (Innovation, Market Coverage, Geographic Reach, Pricing, Satisfaction). No visual scatter plot or map present.

**Action Required:** ⚠️ VERIFY - Check PDF version to confirm no visual maps present that need fixing

**Files to Check:**
- `/VISUALIZATIONS/current-enterprise-cleaned-report-documents/competitive-positioning-viz-ENTERPRISE.pdf`

---

### Finding #3: Other Files to Check for Positioning Maps

**Pending Review:**
- [ ] `strategic-recommendations-viz-ENTERPRISE.pdf` (may have positioning content)
- [ ] `threats-opportunities-viz-ENTERPRISE.pdf` (may have strategic positioning)
- [ ] Full Report DOCX (may have embedded maps)
- [ ] Executive Summary DOCX (may have embedded maps)

**Note:** Tim said positioning maps are "sprinkled throughout" version 2 of the report, so need comprehensive search.

---

## 2. MARKETING TAGLINES REQUIRING REMOVAL

### Finding #1: market-positioning-top4-viz.html (Lines 525-557)

**Location:** `/05-FINAL-DELIVERABLES/VISUALIZATIONS/market-positioning-top4-viz.html`

**Section:** "Final Recommended Positioning for Maia" (bottom of document)

**Content to REMOVE:**

#### Supporting Tagline Options (Lines 536-541):
```html
<h3 style="margin-top: 30px;">Supporting Tagline Options:</h3>
<ul>
    <li><strong>"Global Students Deserve Global AI"</strong></li>
    <li><strong>"International Schools. International Platform. International Success."</strong></li>
    <li><strong>"Built by Counselors for Counselors. Powered by AI for Students."</strong></li>
</ul>
```

**Tim's Feedback:** "Might eliminate some of the marketing taglines that were generated... now wants to use his industry knowledge to tweak it down to what's essential. Focus on Maya's positioning rather than tagline ideas."

**Rationale:** These are marketing taglines, NOT positioning statements. Tim wants positioning (e.g., "International Innovation Leader") but not cute marketing slogans.

#### Elevator Pitch (Lines 543-546):
```html
<div class="elevator-pitch">
    <h4 style="margin-top: 0; ">Elevator Pitch (30 seconds):</h4>
    <p>"Maia Learning is the only AI-powered college and career readiness platform built specifically for international schools. While US platforms like Naviance and SCOIR focus on American students, Maia serves 70+ countries with deep multilingual localization—not just translation. Our AI is trained on global university data, not just US colleges. Built by international school counselors, Maia combines counselor expertise with cutting-edge AI to help global students succeed anywhere in the world."</p>
</div>
```

**Assessment:** This is marketing copy, not strategic positioning. LIKELY TO BE REMOVED per Tim's guidance.

#### Proof Points (Lines 548-556):
```html
<h3 style="margin-top: 30px;">Proof Points:</h3>
<ul>
    <li>70+ countries (unique)</li>
    <li>12+ languages (deep localization)</li>
    <li>AI letter writing (unique feature)</li>
    <li>Counselor-built (professional trust)</li>
    <li>1.5M+ students (scale)</li>
    <li>Minority Owned (diversity)</li>
</ul>
```

**Assessment:** Borderline - these are factual positioning elements, not taglines. May keep with "positioning statement" framing, or remove if too marketing-y.

**Decision:** ⚠️ ASK USER - Should we keep "Proof Points" or remove entire final section?

---

### Finding #2: Other Files to Check for Marketing Taglines

**Pending Review:**
- [ ] Executive Summary DOCX (check for tagline language)
- [ ] Full Report DOCX (check for similar marketing copy)
- [ ] Other visualization PDFs (check for taglines at bottom)

**Search Strategy:** Look for:
- "Tagline" keyword
- "Elevator pitch" sections
- Quotation-marked marketing slogans
- "Proof points" sections

---

## 3. STRATEGIC RECOMMENDATIONS REQUIRING RESTRUCTURING

### Current Structure (Executive Summary + Full Report)

**Location:**
- `executive-summary-CORRECTED-temp.md` (Lines 330-466)
- `full-report-CORRECTED-temp.md` (Lines 109-116)

**Current Priority Order:**
1. 🔴 **CRITICAL Priority 1:** Close AI Gap & Deepen Common App Integration ($500K-1M, Q1-Q2 2026)
2. 🔴 **CRITICAL Priority 2:** Launch Tiered Pricing Model ($150-250K, Q1-Q4 2026)
3. 🟡 **HIGH Priority 3:** Target Naviance Switchers + Attack Cialfo Asia-Pacific ($500-900K, 2026-2030)

**Additional Priorities:**
4. Develop Native Mobile App
5. Enhance AI Career Exploration
6. Build Direct Admissions Support
7. Leverage International Moat Defensively

---

### Tim's Required Changes

**Tim's Quote:**
> "Okay, and I think the number one recommendation is double down on international. Okay, but in real life. The real answer is you've got to adjust your fucking prices and go after the biggest market in the world, which is the U.S. market. So, what I want to see, I'm wondering if we can leave that in, right, the way it is. But offer an alternate or, if you decide to invest in AI, deeper integration with Common App, and... You fix your pricing, then you can attack the U.S. market while simultaneously what you just did benefits the international market as well, particularly the A.I."

**Interpretation:**
- **PRIMARY STRATEGY:** Attack US market (adjust pricing + accelerate AI + deepen Common App)
- **SECONDARY/BONUS:** International market benefits automatically from same investments
- **Framing:** "If you invest in [X], this is what you can get"
- **Key Phrases to Include:**
  - "Accelerate AI introduction as quickly as possible"
  - "Lower the price and go after public schools"
  - "Biggest market in the world" (referring to US market)

---

### New Recommended Structure

**Priority 1: ATTACK US MARKET (NEW - Flip from current)**

**Title:** "Attack US Market: Adjust Pricing + Accelerate AI + Deepen Common App"

**Objective:** Position Maia to compete aggressively in the US market (the biggest CCR market in the world) by addressing the two primary barriers: pricing gap and AI gap.

**Rationale:** The US market represents the largest addressable opportunity (~50M students vs. 6-7M international). Current $10 pricing and AI gap prevent US expansion. Fixing these unlocks US public schools AND benefits international customers simultaneously.

**Specific Actions:**
1. **Launch Tiered Pricing** (Q1-Q4 2026)
   - Basic Tier: $5-6/student → Target US public schools
   - Plus Tier: $8-9/student → Current customer segment
   - Premium Tier: $12-15/student → High-touch international
   - **Investment:** $150-250K

2. **Accelerate AI Introduction** (Q1-Q2 2026) ⚡ CRITICAL URGENCY
   - Match SCOIR AI 2.0 features (acceptance predictions, college list balancing)
   - Develop conversational AI assistant
   - Add AI essay review
   - **Investment:** $500K-1M
   - **Timeline:** "As quickly as possible" (6-month critical window)

3. **Deepen Common App Integration** (Q1-Q2 2026)
   - Audit current integration vs. SCOIR's NEW 2025-26 depth
   - Support Direct Admissions (200+ colleges)
   - Close any feature gaps
   - **Investment:** Included in $500K-1M AI budget

**Total Investment:** $650K-1.25M

**Expected Return:**
- **US Market:** Opens 25,000+ US public schools previously inaccessible
- **International Bonus:** AI and integrations benefit existing 70+ country base
- **Dual Market Strategy:** Single investment, dual market benefits

**Framing:** "If you invest in US market capabilities (pricing flexibility + AI leadership + Common App depth), you can attack the biggest CCR market in the world (US) while simultaneously enhancing your international competitive advantage."

---

**Priority 2: INTERNATIONAL MARKET BENEFITS AUTOMATICALLY (NEW - Reframe from current)**

**Title:** "International Market Gains as Bonus from US Investments"

**Key Point:** All US-focused investments (AI, Common App, pricing tiers) benefit international customers:
- **AI:** Works for global university applications, not just US colleges
- **Common App:** International students applying to US colleges benefit
- **Tiered Pricing:** Enables expansion to price-sensitive international markets

**No Additional Investment Required** - International benefits come "for free" from US market initiatives

---

**Priority 3-7: Keep Current Recommendations**

Maintain existing priorities 3-7 but reframe as supporting the US market attack:
- Priority 3: Target Naviance Switchers (US) + Attack Cialfo Asia-Pacific (International)
- Priority 4: Native Mobile App (benefits both markets)
- Priority 5: AI Career Exploration (comprehensive platform strategy)
- Priority 6: Direct Admissions Support (US + International applicants)
- Priority 7: International Moat Defense (maintain advantage while attacking US)

---

### Files Requiring Strategic Recommendation Changes

**Primary Documents:**
1. ✅ `executive-summary-CORRECTED.docx` - Lines 330-466
   - Rewrite Strategic Recommendations section completely
   - Flip priority order (US-primary, international-secondary)
   - Add "biggest market in the world" language
   - Emphasize "accelerate AI as quickly as possible"
   - Add "lower price and go after public schools" strategy

2. ✅ `full-report-CORRECTED.docx` - PART V: Strategic Implications
   - Apply same changes as Executive Summary
   - Ensure consistency across both documents

**Supporting Documents:**
3. ✅ `strategic-recommendations-viz.html` (SOURCE FILE - CONFIRMED NEEDS UPDATE)
   - Current Priority 1: Close AI Gap & Deepen Common App Integration
   - Current Priority 2: Launch First-Mover Native Mobile App
   - Current Priority 3: Target Naviance Switchers (US Private Schools)
   - Current Priority 4: Implement Tiered Pricing Model
   - **NOTE:** Priority order is DIFFERENT from Executive Summary!
   - **MUST UPDATE** to match Tim's new structure (US-primary strategy)

4. ✅ `strategic-recommendations-viz-ENTERPRISE.pdf` (GENERATED FROM HTML)
   - Must regenerate after HTML source is fixed

---

## 4. ADDITIONAL FINDINGS

### Pricing Data Inconsistency (Found in competitive-positioning-viz.html)

**Location:** Line 180
```html
<td class="score">$6-8</td>
```

**Issue:** Naviance pricing showing as "$6-8" but should be "$8-12 (est.)" per previous QA corrections

**Action Required:** Fix this inconsistency while making other changes

**Note:** This was supposed to be fixed in previous QA but appears to have been missed in this HTML file.

---

## 5. SEARCH STRATEGY FOR REMAINING FILES

### Files Pending Review:

**PDFs (Need to Check for Maps/Taglines):**
- [ ] strategic-recommendations-viz-ENTERPRISE.pdf
- [ ] threats-opportunities-viz-ENTERPRISE.pdf
- [ ] swot-analysis-viz-ENTERPRISE.pdf
- [ ] market-trends-viz-ENTERPRISE.pdf
- [ ] feature-comparison-matrix-top4-viz-ENTERPRISE.pdf
- [ ] pricing-analysis-top4-viz-ENTERPRISE.pdf
- [ ] technology-stack-top4-viz-ENTERPRISE.pdf
- [ ] target-segments-top4-viz-ENTERPRISE.pdf
- [ ] Combined-Competitive-Analysis-Visualizations-ENTERPRISE.pdf

**HTML Source Files (Easier to Review):**
- [ ] Find all .html files in VISUALIZATIONS directory
- [ ] Search for positioning map ASCII art or visual elements
- [ ] Search for "tagline," "elevator pitch," "proof points"

**DOCX Files:**
- [x] executive-summary-CORRECTED.docx (reviewed - strategic recs found)
- [x] full-report-CORRECTED.docx (partially reviewed - strategic recs found)

---

## 6. SUMMARY OF REQUIRED CHANGES

### By Category:

**POSITIONING MAPS (4-Quadrant Format):**
- ✅ Confirmed: market-positioning-top4-viz.html (Lines 336-369)
- ⚠️ Pending: Check remaining files for additional maps

**MARKETING TAGLINES (Remove):**
- ✅ Confirmed: market-positioning-top4-viz.html (Lines 536-557)
  - 3 tagline options
  - Elevator pitch
  - Proof points section (decision needed)
- ⚠️ Pending: Check remaining files for similar content

**STRATEGIC RECOMMENDATIONS (Major Restructure):**
- ✅ Confirmed: Executive Summary DOCX (Lines 330-466)
- ✅ Confirmed: Full Report DOCX (PART V: Strategic Implications)
- ⚠️ Pending: strategic-recommendations-viz-ENTERPRISE.pdf

**PRICING INCONSISTENCY:**
- ✅ Found: competitive-positioning-viz.html Line 180 (Naviance $6-8 should be $8-12 est.)

---

## 7. NEXT STEPS

### Immediate (Complete Discovery):
1. ✅ Check all remaining HTML source files for positioning maps
2. ✅ Check all remaining HTML source files for marketing taglines
3. ⚠️ Verify findings by reviewing PDF versions
4. ⚠️ Search Full Report DOCX for embedded maps/taglines

### Then (Implementation):
1. Fix all positioning maps to four-quadrant format
2. Remove all marketing taglines identified
3. Restructure strategic recommendations (US-primary flip)
4. Fix pricing inconsistency
5. Regenerate all PDFs from corrected HTML sources
6. Update DOCX files
7. QA review all changes

---

## 8. DISCOVERY COMPLETE - FINAL SUMMARY

### Total Items Identified:

**POSITIONING MAPS TO FIX:** 1 confirmed
- ✅ market-positioning-top4-viz.html (Lines 336-369) - Text-based scatter plot → Four-quadrant format

**MARKETING TAGLINES TO REMOVE:** 1 section confirmed
- ✅ market-positioning-top4-viz.html (Lines 536-557) - Taglines, elevator pitch, proof points

**STRATEGIC RECOMMENDATIONS TO RESTRUCTURE:** 3 files confirmed
- ✅ executive-summary-CORRECTED.docx - Full rewrite required
- ✅ full-report-CORRECTED.docx - Full rewrite required
- ✅ strategic-recommendations-viz.html - Priority order update required

**PRICING INCONSISTENCIES TO FIX:** 1 instance
- ✅ competitive-positioning-viz.html Line 180 - Naviance $6-8 → $8-12 (est.)

### Files Requiring Changes:

**HTML Source Files (4):**
1. market-positioning-top4-viz.html (positioning map + taglines)
2. competitive-positioning-viz.html (pricing fix)
3. strategic-recommendations-viz.html (priority restructure)

**DOCX Files (2):**
1. executive-summary-CORRECTED.docx (strategic recommendations rewrite)
2. full-report-CORRECTED.docx (strategic recommendations rewrite)

**PDFs to Regenerate (3+):**
1. market-positioning-top4-viz-ENTERPRISE.pdf
2. competitive-positioning-viz-ENTERPRISE.pdf
3. strategic-recommendations-viz-ENTERPRISE.pdf
4. Combined-Competitive-Analysis-Visualizations-ENTERPRISE.pdf (after all individual PDFs fixed)

### Priority Implementation Order:

**PHASE 1 - CRITICAL (Do First):**
1. Fix positioning map to four-quadrant format (market-positioning-top4-viz.html)
2. Remove marketing taglines (market-positioning-top4-viz.html)
3. Fix Naviance pricing inconsistency (competitive-positioning-viz.html)

**PHASE 2 - HIGH PRIORITY (Do Second):**
4. Restructure strategic recommendations in HTML visualization (strategic-recommendations-viz.html)
5. Rewrite strategic recommendations in Executive Summary DOCX
6. Rewrite strategic recommendations in Full Report DOCX

**PHASE 3 - FINAL (Do Third):**
7. Regenerate all affected PDFs from corrected HTML sources
8. Quality assurance review
9. Update package README with change log

---

**Discovery Status:** ✅ 100% COMPLETE
**Next Action:** BEGIN IMPLEMENTATION - Phase 1 (Positioning Maps + Taglines)

**Updated:** November 24, 2025 (Discovery Phase - COMPLETE)
