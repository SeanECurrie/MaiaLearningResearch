# Skill Enhancement Specifications: competitive-research-brightdata

**Skill Location:** `~/.claude/skills/competitive-research-brightdata/SKILL.md`
**Current Version:** November 16, 2025 (14,092 bytes)
**Enhancement Date:** November 25, 2025
**Based On:** Lessons learned from Maia Learning competitive analysis project

---

## Current Skill Analysis

### Existing Capabilities

The skill provides a 5-step research workflow:

1. **Clarify the Research Objective** - Ask questions to understand purpose, companies, aspects, audience, format
2. **Plan the Research Approach** - Identify information needed, search strategy, scraping strategy, framework selection
3. **Execute Research Systematically** - Phase A (initial search), Phase B (deep dive), Phase C (competitive/comparative)
4. **Analyze and Synthesize** - Apply frameworks, generate insights, quality assurance
5. **Create the Report** - Select structure, apply quality standards, format flexibility

### Existing Tools

- `search_engine` - Single searches on Google/Bing/Yandex
- `search_engine_batch` - Up to 10 searches (recommend 3-4 per batch)
- `scrape_as_markdown` - Single webpage scraping
- `scrape_batch` - Up to 10 URLs (recommend 2-3 per batch)

### Existing Reference Files

- `references/consulting-frameworks.md` - Strategic analysis frameworks
- `references/report-templates.md` - Report structures for different deliverables
- `references/research-methodology.md` - Search strategies, scraping best practices

### Key Constraints

- 25,000 token limit on MCP tool responses
- Batch size guidelines already documented (3-4 searches, 2-3 URLs)
- Failure recovery protocol included

---

## Enhancement 1: Output Format Standardization

### Current State

The skill outputs vary based on context:
- No defined schema for competitor data
- Pricing, features, positioning captured inconsistently
- Makes QA and comparison difficult
- Requires manual normalization before analysis

**From Maia Project:** Each competitor profile had slightly different structure, making cross-comparison tables tedious to create.

### Enhancement Specification

**Add Standardized Output Schema for Competitor Data**

1. **Define JSON Schema:**
   ```json
   {
     "competitor": {
       "name": "string",
       "website": "url",
       "founded": "year",
       "headquarters": "string",
       "ownership": "public | private | pe-backed",
       "parent_company": "string | null"
     },
     "financials": {
       "total_funding": {
         "amount": "number | null",
         "source": "string",
         "date": "YYYY-MM",
         "confidence": "verified | estimated | unknown"
       },
       "latest_round": {
         "series": "string",
         "amount": "number",
         "date": "YYYY-MM"
       },
       "revenue": {
         "amount": "number | null",
         "source": "string",
         "confidence": "verified | estimated | unknown"
       }
     },
     "market": {
       "customers": {
         "count": "number",
         "unit": "schools | students | users",
         "source": "string",
         "date": "YYYY-MM"
       },
       "market_share": {
         "percentage": "number | null",
         "source": "string",
         "confidence": "verified | estimated | unknown"
       },
       "geographic_presence": ["country1", "country2"]
     },
     "pricing": {
       "model": "per-student | per-school | tiered | custom",
       "low_range": "number",
       "high_range": "number",
       "source": "string",
       "confidence": "verified | estimated | unknown",
       "notes": "string"
     },
     "product": {
       "description": "string",
       "primary_focus": "string",
       "features": [
         {
           "name": "string",
           "available": "yes | no | partial",
           "notes": "string"
         }
       ],
       "integrations": ["string"],
       "technology": {
         "ai_capabilities": "string | null",
         "mobile_apps": "yes | no",
         "api_available": "yes | no"
       }
     },
     "positioning": {
       "target_segment": "enterprise | mid-market | smb",
       "value_proposition": "string",
       "differentiators": ["string"],
       "weaknesses": ["string"]
     },
     "satisfaction": {
       "rating": "number",
       "scale": "5 | 10",
       "source": "string",
       "review_count": "number",
       "confidence": "verified | inferred | unknown"
     },
     "metadata": {
       "research_date": "YYYY-MM-DD",
       "last_updated": "YYYY-MM-DD",
       "data_freshness": "current | 6-months | 1-year | older"
     }
   }
   ```

2. **Usage in Workflow:**
   - After Phase B (Deep Dive), populate schema
   - Missing fields marked as `null` with `confidence: "unknown"`
   - Schema enables automatic comparison matrix generation

3. **Benefits:**
   - Consistent data structure across competitors
   - Enables automated comparison tables
   - Simplifies QA (check for nulls, confidence levels)
   - Integrates with QA skill for validation

### Implementation Notes

- Add schema definition to `references/data-schema.md`
- Update Phase 4 (Analyze) to include schema population step
- Allow partial schema (not all fields required)
- Export as JSON or Markdown table

---

## Enhancement 2: Research Question Templates

### Current State

Step 1 ("Clarify the Research Objective") asks questions ad-hoc:
- No standard question set
- Coverage varies by researcher
- Easy to miss important dimensions

**From Maia Project:** We discovered late that we hadn't gathered customer satisfaction data for 3 competitors, requiring additional research passes.

### Enhancement Specification

**Add Standard Research Question Templates**

1. **Company Overview Questions (5):**
   ```
   1. When was [Company] founded and where is it headquartered?
   2. Who owns [Company]? (Public, private, PE-backed, acquired?)
   3. Who is the CEO/leadership team?
   4. What is [Company]'s total funding and latest funding round?
   5. What is [Company]'s estimated revenue or financial status?
   ```

2. **Product/Service Questions (5):**
   ```
   6. What are [Company]'s core products/services?
   7. What key features does [Company] offer?
   8. What integrations does [Company] support?
   9. Does [Company] have AI/ML capabilities? What kind?
   10. Does [Company] have mobile apps? API access?
   ```

3. **Pricing Questions (4):**
   ```
   11. What is [Company]'s pricing model? (per-user, per-school, tiered?)
   12. What is [Company]'s price range? (low/high estimates)
   13. Are there published pricing tiers or is it custom-quoted?
   14. How does pricing compare to market average?
   ```

4. **Market Position Questions (4):**
   ```
   15. How many customers/users does [Company] have?
   16. What is [Company]'s estimated market share?
   17. What geographic regions does [Company] serve?
   18. Who are [Company]'s primary target customers?
   ```

5. **Customer Satisfaction Questions (3):**
   ```
   19. What is [Company]'s rating on G2/Capterra/TrustRadius?
   20. What do customers praise about [Company]?
   21. What are common complaints about [Company]?
   ```

6. **Strategic Questions (3):**
   ```
   22. What is [Company]'s stated strategy/vision?
   23. What recent news/developments are significant?
   24. What are [Company]'s key strengths and weaknesses?
   ```

2. **Usage:**
   - Present checklist at start of research
   - Mark questions as user requires (not all needed for every project)
   - Track which questions have been answered
   - Flag gaps at end of research

### Implementation Notes

- Add to `references/research-questions.md`
- Create question tracker template
- Allow custom questions to be added
- Integrate with schema (questions map to schema fields)

---

## Enhancement 3: Data Validation Rules

### Current State

No validation of gathered data:
- Missing fields not flagged
- Confidence levels not required
- Easy to deliver incomplete research

**From Maia Project:** We delivered initial research with missing satisfaction ratings for 3 competitors, discovered only during QA.

### Enhancement Specification

**Add Data Validation Step Before Report Generation**

1. **Required Field Validation:**
   ```
   MINIMUM REQUIRED FIELDS (for each competitor):
   - name ✓
   - founded ✓
   - website ✓
   - pricing.model OR pricing.notes ✓
   - customers.count OR customers.notes ✓
   - at least 5 features ✓
   - positioning.target_segment ✓
   ```

2. **Confidence Level Requirements:**
   ```
   CONFIDENCE REQUIREMENTS:
   - pricing: Must have source and date
   - market_share: Must have source OR be marked "estimated"
   - satisfaction: Must have source OR be marked "inferred"
   - funding: Must have source for "verified" confidence
   ```

3. **Completeness Score:**
   ```
   COMPLETENESS REPORT
   -------------------
   Competitor: SCOIR

   Required Fields: 8/8 (100%)
   Optional Fields: 12/15 (80%)
   Fields with Sources: 14/20 (70%)
   Confidence Levels: All assigned ✓

   Overall Completeness: 85%
   Recommendation: Ready for report generation

   GAPS TO ADDRESS:
   - satisfaction.rating: Missing (mark as "no public reviews" or research further)
   - revenue: Missing (mark as "private company" or estimate)
   ```

4. **Validation Rules:**
   - Block report generation if completeness < 70%
   - Warn if any "required" fields missing
   - Require confidence level for all numeric data
   - Require source for all "verified" confidence claims

### Implementation Notes

- Add validation step between Phase 4 (Analyze) and Phase 5 (Report)
- Generate completeness report as Markdown
- Allow override with acknowledgment of gaps
- Track validation results for QA integration

---

## Enhancement 4: Citation Formatting

### Current State

Citations created manually:
- No auto-generation from research
- Format inconsistent
- Source URLs not always captured
- Access dates not tracked

**From Maia Project:** We spent hours manually formatting citations as "(Source, YYYY)" during QA, and some source URLs were lost.

### Enhancement Specification

**Add Auto-Citation Generation**

1. **Capture During Research:**
   ```
   When scraping/searching, automatically capture:
   - Source URL
   - Page title
   - Access date
   - Publication date (if available)
   - Author/organization (if available)
   ```

2. **Citation Format Options:**
   ```
   SHORT FORMAT (for inline):
   (Source, YYYY)
   Example: (G2, 2024), (Crunchbase, November 2025)

   FULL FORMAT (for references section):
   Source Name. "Page Title." URL. Accessed YYYY-MM-DD.
   Example: G2. "SCOIR Reviews." https://g2.com/products/scoir. Accessed 2025-11-15.
   ```

3. **Auto-Generation:**
   ```
   When data is gathered, auto-generate citation:

   INPUT: Scraping https://www.scoir.com/about
   OUTPUT:
   - source_name: "SCOIR"
   - source_url: "https://www.scoir.com/about"
   - access_date: "2025-11-25"
   - short_citation: "(SCOIR, 2025)"
   - full_citation: "SCOIR. 'About Us.' https://www.scoir.com/about. Accessed 2025-11-25."
   ```

4. **Citation Index:**
   ```
   Generate citation index at end of research:

   SOURCES USED
   ------------
   [1] SCOIR. "About Us." https://www.scoir.com/about. Accessed 2025-11-25.
   [2] G2. "SCOIR Reviews." https://g2.com/products/scoir. Accessed 2025-11-25.
   [3] Crunchbase. "SCOIR Profile." https://crunchbase.com/scoir. Accessed 2025-11-25.

   In-text: Use [1], [2], [3] or (SCOIR, 2025), (G2, 2025) as preferred.
   ```

### Implementation Notes

- Capture metadata during scrape_as_markdown calls
- Store in citation registry (JSON array)
- Generate formatted citations on demand
- Export as numbered list or inline format
- Include in schema as `sources[]` array

---

## Summary: Enhancement Priority

| Enhancement | Priority | Complexity | Impact |
|-------------|----------|------------|--------|
| Enhancement 1: Output Format Standardization | HIGH | Medium | Enables consistent data and automated comparisons |
| Enhancement 2: Research Question Templates | HIGH | Low | Ensures comprehensive coverage |
| Enhancement 3: Data Validation Rules | MEDIUM | Medium | Prevents incomplete deliverables |
| Enhancement 4: Citation Formatting | MEDIUM | Low | Saves time, ensures compliance |

---

## Implementation Recommendations

1. **Phase 1:** Implement Enhancement 2 (low complexity, immediate value)
2. **Phase 2:** Implement Enhancement 4 (low complexity, time-saving)
3. **Phase 3:** Implement Enhancement 1 (medium complexity, enables automation)
4. **Phase 4:** Implement Enhancement 3 (medium complexity, quality gate)

**Testing Approach:**
- Use Maia Learning competitor set as test cases
- Validate schema against existing profiles
- Verify question templates cover all gathered data
- Test citation generation against actual source URLs

---

**Document Created:** November 25, 2025
**Based On:** Review of `~/.claude/skills/competitive-research-brightdata/SKILL.md` and Maia Learning project experience
