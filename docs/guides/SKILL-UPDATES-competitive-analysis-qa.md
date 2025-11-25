# Skill Enhancement Specifications: competitive-analysis-quality-assurance

**Skill Location:** `~/.claude/skills/competitive-analysis-quality-assurance/SKILL.md`
**Current Version:** November 17, 2025 (22,796 bytes)
**Enhancement Date:** November 25, 2025
**Based On:** Lessons learned from Maia Learning competitive analysis project

---

## Current Skill Analysis

### Existing Capabilities (8 Phases)

The skill currently implements an 8-phase QA workflow:

1. **Phase 1: Scope the Review** - Locate files, clarify objectives, identify priority, determine depth
2. **Phase 2: Document Analysis** - Read/map documents, extract claims for verification
3. **Phase 3: Source Validation** - Citation verification, cross-reference verification
4. **Phase 4: Fact-Checking** - Factual claims, statistical verification, comparative claims
5. **Phase 5: Consistency Analysis** - Internal consistency, timeline verification, numerical consistency
6. **Phase 6: Gap Identification** - Coverage assessment, missing information, conflicting information
7. **Phase 7: Quality Assessment** - Evaluate against standards, compare to benchmarks, identify improvements
8. **Phase 8: Generate QA Report** - Structure findings, provide evidence, deliver report

### Existing Review Types

- Quick Validation (30-60 minutes)
- Standard Review (2-4 hours)
- Comprehensive Audit (1-2 days)
- Targeted Fact-Check (variable)

### Existing Reference Files

- `references/verification-checklist.md`
- `references/quality-standards.md`
- `references/fact-checking-methodology.md`

---

## Enhancement 1: Cross-Document Consistency Check

### Current State

Phase 5 includes "Consistency Analysis" with cross-document checks, but:
- Process is manual and relies on human scanning
- No systematic extraction of key data points
- No comparison matrix generation
- Easy to miss inconsistencies in large document sets

**From Maia Project:** We found pricing, market share, and recommendation inconsistencies between Executive Summary, Full Report, and visualization PDFs that were only caught on the third review pass.

### Enhancement Specification

**Add New Sub-Phase: 5.0 - Automated Consistency Matrix**

Before manual consistency review, automatically:

1. **Extract Key Data Points** from all in-scope documents:
   - Pricing figures (all `$X.XX` patterns)
   - Market share percentages (all `X%` patterns)
   - Company metrics (funding, customers, students)
   - Investment recommendations (amounts, timelines)
   - Strategic priorities (Priority 1, Priority 2, etc.)

2. **Generate Comparison Matrix:**
   ```
   | Data Point | Exec Summary | Full Report | Viz 1 | Viz 2 | Status |
   |------------|--------------|-------------|-------|-------|--------|
   | Naviance pricing | $8-12 | $8-12 | $8-12 | — | ✅ Consistent |
   | SCOIR market share | 12% | 12% | 10% | — | ⚠️ Inconsistent |
   ```

3. **Flag Discrepancies** automatically:
   - Critical: Investment amounts, strategic recommendations
   - High: Pricing, market share, customer counts
   - Medium: Dates, feature claims

### Implementation Notes

- Add regex patterns for common data extraction
- Store extracted data in structured format (JSON)
- Generate comparison matrix as Markdown table
- Include in QA report as "Consistency Matrix" section

---

## Enhancement 2: Source Attribution Verification

### Current State

Phase 3 validates citations for:
- URL accessibility
- Content accuracy
- Date currency
- Author credibility
- Context accuracy

But does NOT enforce citation format standards.

**From Maia Project:** We had to manually add 100+ citations in "(Source, YYYY)" format during QA. Many numeric claims lacked any citation.

### Enhancement Specification

**Add New Verification Rule: Citation Format Compliance**

1. **Define Required Citation Format:**
   - Standard: `(Source, YYYY)` or `(Source, Month YYYY)`
   - Examples: `(Naviance, 2024)`, `(G2 Reviews, November 2025)`

2. **Identify Claims Requiring Citations:**
   - Pricing claims: Any `$X` figure
   - Market share: Any `X%` market/share claim
   - Customer counts: Any "X schools" or "X students"
   - Funding amounts: Any `$XM` or `$XB` funding claim
   - Satisfaction ratings: Any `X/5` or `X.X/10` rating
   - Growth rates: Any `X% growth` claim

3. **Verification Process:**
   ```
   Step 1: Regex scan for numeric claims
   Step 2: Check if claim followed by (Source, YYYY) within 50 characters
   Step 3: Flag uncited claims
   Step 4: Validate cited claims have proper format
   ```

4. **Report Output:**
   ```
   CITATION COMPLIANCE CHECK
   -------------------------
   Total numeric claims found: 47
   Claims with proper citations: 38 (81%)
   Claims missing citations: 9
   Claims with improper format: 0

   UNCITED CLAIMS:
   - Line 45: "SCOIR has 12% market share" [NEEDS CITATION]
   - Line 67: "$4.80 per student" [NEEDS CITATION]
   ```

### Implementation Notes

- Add regex patterns for numeric claim detection
- Define "citation proximity" rule (within X characters)
- Add citation format validation regex
- Include compliance percentage in QA report

---

## Enhancement 3: Marketing Language Detection

### Current State

Phase 6 mentions "Vague or Subjective Claim" in Common Issues, but:
- No systematic detection of marketing language
- No red flag word list
- Relies on manual identification

**From Maia Project:** We had to remove marketing taglines and subjective language ("game-changing", "revolutionary") that crept into analysis during V1.0 → V2.0 transition.

### Enhancement Specification

**Add New Sub-Phase: 4.5 - Marketing Language Scan**

1. **Define Red Flag Word List:**
   ```
   SUPERLATIVES (remove or cite):
   - best, leading, top, premier, #1, first
   - revolutionary, game-changing, breakthrough
   - only, unique, exclusive (unless verifiable)

   SUBJECTIVE (soften or remove):
   - clearly, obviously, certainly
   - significantly, dramatically, massively
   - amazing, incredible, exceptional

   MARKETING PHRASES (remove):
   - "industry leader", "market leader" (unless cited)
   - "best-in-class", "world-class" (unless criteria defined)
   - "trusted by", "preferred by" (unless sourced)
   ```

2. **Scan Process:**
   ```
   Step 1: Case-insensitive scan for red flag words
   Step 2: Extract context (sentence containing word)
   Step 3: Classify: Must Remove | Needs Citation | Soften Language
   Step 4: Generate replacement suggestions
   ```

3. **Report Output:**
   ```
   MARKETING LANGUAGE SCAN
   -----------------------
   Red flags found: 7

   MUST REMOVE:
   - Line 23: "revolutionary AI capabilities" → "advanced AI capabilities"
   - Line 89: "best-in-class support" → "highly-rated support (G2, 2024)"

   NEEDS CITATION:
   - Line 45: "industry leader" → add source or remove

   SOFTEN:
   - Line 112: "clearly dominates" → "leads in"
   ```

### Implementation Notes

- Create configurable red flag word list
- Add context extraction (full sentence)
- Generate replacement suggestions
- Allow custom word lists per project

---

## Enhancement 4: Version Comparison

### Current State

The skill has no version comparison capability:
- Cannot compare V1.0 vs V2.0 changes
- No tracking of what changed between iterations
- No way to verify all requested changes were made

**From Maia Project:** During V2.0 revisions, we created manual change inventories. Automated comparison would have saved hours and ensured completeness.

### Enhancement Specification

**Add New Review Type: Version Comparison Review**

1. **Input Requirements:**
   - Path to V1 document
   - Path to V2 document
   - Optional: Change request document listing expected changes

2. **Comparison Process:**
   ```
   Step 1: Calculate file sizes and word counts
   Step 2: Identify structural changes (sections added/removed)
   Step 3: Identify data changes (numbers, percentages that changed)
   Step 4: If change request provided, verify each requested change made
   ```

3. **Metrics Generated:**
   ```
   VERSION COMPARISON: V1.0 → V2.0
   -------------------------------
   File size: 45KB → 52KB (+15%)
   Word count: 8,500 → 9,200 (+8%)

   STRUCTURAL CHANGES:
   + Added: "US Market Strategy" section
   + Added: "Implementation Timeline" section
   - Removed: "International Expansion" as Priority 1
   ~ Modified: 12 sections with content changes

   DATA CHANGES:
   - Priority 1 investment: $450K-750K → $650K-1.25M
   - Strategic focus: "International" → "US-Primary"
   - Positioning map: Scatter plot → Four-quadrant

   CHANGE REQUEST VERIFICATION:
   ✅ "Flip recommendations to US-primary" - DONE
   ✅ "Convert positioning maps to four-quadrant" - DONE
   ✅ "Remove marketing taglines" - DONE (7 instances removed)
   ⚠️ "Add implementation timeline" - PARTIAL (added but missing Q4)
   ```

4. **Report Output:**
   - Summary of changes (overview)
   - Detailed change list (line-by-line if requested)
   - Change request verification (if provided)
   - Recommendations for V3 if issues found

### Implementation Notes

- Use diff algorithms for structural comparison
- Track numeric changes specifically
- Support optional change request verification
- Generate human-readable change summary

---

## Summary: Enhancement Priority

| Enhancement | Priority | Complexity | Impact |
|-------------|----------|------------|--------|
| Enhancement 1: Cross-Document Consistency | HIGH | Medium | Prevents inconsistencies in multi-document deliverables |
| Enhancement 2: Source Attribution Verification | HIGH | Low | Ensures citation completeness and format compliance |
| Enhancement 3: Marketing Language Detection | MEDIUM | Low | Maintains professional, objective tone |
| Enhancement 4: Version Comparison | MEDIUM | High | Streamlines iteration tracking and verification |

---

## Implementation Recommendations

1. **Phase 1:** Implement Enhancements 2 and 3 (low complexity, high value)
2. **Phase 2:** Implement Enhancement 1 (medium complexity, prevents critical errors)
3. **Phase 3:** Implement Enhancement 4 (high complexity, valuable for iteration-heavy projects)

**Testing Approach:**
- Use Maia Learning project files as test cases
- Verify each enhancement against known issues from V1.0 → V2.0 transition
- Document false positive/negative rates

---

**Document Created:** November 25, 2025
**Based On:** Review of `~/.claude/skills/competitive-analysis-quality-assurance/SKILL.md` and Maia Learning project experience
