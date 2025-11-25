---
name: competitive-research-brightdata
description: Enterprise-grade company research, competitive analysis, and market intelligence using Bright Data's professional web scraping and search capabilities. Use this skill when asked to research companies, conduct competitive analysis, create market reports, analyze industries, compare products/services, or gather business intelligence. Triggers include requests like "research [company]", "competitive analysis of X vs Y", "create a market report", "analyze the [industry] landscape", or "compare [products/companies]".
---

# Competitive Research with Bright Data

This skill provides enterprise consulting-grade methodologies for conducting comprehensive company research, competitive analysis, and market intelligence using Bright Data's professional search and web scraping tools.

## Skill Capabilities

This skill supports:

- **Company Research** - Deep dives into company background, business model, financials, strategy, and market position
- **Competitive Analysis** - Multi-company comparisons across products, pricing, positioning, and capabilities
- **Market Intelligence** - Industry landscape analysis, market sizing, trends, and dynamics
- **Product Comparison** - Feature-by-feature analysis of competing products or services
- **Strategic Analysis** - SWOT, Porter's Five Forces, positioning, and strategic recommendations
- **Custom Reports** - Tailored deliverables matching specific client needs and formats

## Available Tools

### Search Tools

**search_engine** - Search Google, Bing, or Yandex for company information
- Use Google for general company research and recent news
- Use Bing for cross-validation and Microsoft ecosystem content
- Use Yandex for companies with Eastern European operations
- Supports pagination with cursor for deep research

**search_engine_batch** - Run up to 10 searches simultaneously (⚠️ Recommend 3-4 per batch due to 25k token response limit)
- Use for multi-company research to gather parallel information
- Use for comprehensive single-company research across topics
- More efficient than sequential searches
- Returns JSON for Google, Markdown for Bing/Yandex
- **Best Practice:** Limit to 3-4 queries per batch to avoid token limit failures

### Scraping Tools

**scrape_as_markdown** - Extract complete content from a single webpage
- Returns clean Markdown format
- Use for company websites, press releases, reports, articles
- Handles bot detection and CAPTCHAs automatically

**scrape_batch** - Scrape up to 10 URLs simultaneously (⚠️ Recommend 2-3 per batch due to 25k token response limit)
- Use for systematic company website extraction
- Use for parallel competitor website analysis
- More efficient than sequential scraping
- **Best Practice:** Limit to 2-3 URLs per batch to avoid token limit failures (websites can be 5k-10k+ tokens each)

## Workflow

### 1. Clarify the Research Objective

**Always start by understanding the specific request.** Ask clarifying questions before diving into research:

**Questions to Ask:**
- What is the primary purpose of this research? (Investment decision, competitive positioning, market entry, product development, etc.)
- Which companies/products should be analyzed?
- What specific aspects are most important? (Pricing, features, market share, strategy, financials, etc.)
- Who is the audience for this report? (Executive team, sales, product, investors, etc.)
- What format should the deliverable take? (Full report, executive summary, comparison matrix, presentation deck, etc.)
- Are there any specific questions that must be answered?
- What is the scope? (Comprehensive deep-dive vs. quick overview)
- Any time constraints or priorities?

**Adapt the approach based on responses** - The research methodology and report format should match the stated objective.

### 2. Plan the Research Approach

Based on the clarified objective, determine:

**Information Needed:**
- Company background and overview
- Financial data (revenue, funding, growth)
- Product/service details
- Pricing and business model
- Market position and share
- Recent news and developments
- Customer sentiment
- Strategic direction

**Search Strategy:**
- Identify key search queries for each information area
- Determine if batch searching would be efficient
- Select appropriate search engine(s)

**Scraping Strategy:**
- Identify target URLs (company sites, reports, articles)
- Determine if batch scraping would be efficient
- Prioritize official company sources

**Framework Selection:**
- Choose appropriate analytical frameworks (see `references/consulting-frameworks.md`)
- Determine report structure (see `references/report-templates.md`)

### Research Question Template

Use this template to ensure comprehensive data gathering for each company. Customize based on research objectives.

**Company Fundamentals (8 questions):**
1. When was [company] founded and where is headquarters?
2. Who is [company]'s CEO and key leadership team?
3. What is [company]'s ownership structure (public/private/PE-backed)?
4. What funding has [company] raised and when?
5. How many employees does [company] have?
6. What is [company]'s primary business model?
7. What markets/regions does [company] operate in?
8. What is [company]'s mission/value proposition?

**Product & Technology (6 questions):**
9. What are [company]'s core products/services?
10. What key features differentiate [company] from competitors?
11. What technology stack does [company] use?
12. What integrations does [company] offer?
13. What is [company]'s product roadmap or recent launches?
14. What platform/deployment options does [company] offer?

**Market Position (5 questions):**
15. What is [company]'s estimated market share?
16. How many customers does [company] serve?
17. Who are [company]'s target customer segments?
18. Who are [company]'s main competitors?
19. What is [company]'s competitive positioning/differentiation?

**Pricing & Business (4 questions):**
20. What is [company]'s pricing model and price range?
21. What contract terms does [company] typically offer?
22. What implementation/onboarding process does [company] use?
23. What customer support does [company] provide?

**Customer Sentiment (3 questions):**
24. What do G2/Capterra/TrustRadius reviews say about [company]?
25. What is [company]'s customer satisfaction rating?
26. What are common complaints or praise for [company]?

**Usage Notes:**
- Not all questions apply to every research project
- Prioritize based on clarified research objectives
- Track which questions are answered vs. gaps remaining
- Add industry-specific questions as needed

### 3. Execute Research Systematically

**Phase A: Initial Search and Discovery**

Start with broad searches to identify sources and get overview:

```
Company overview and background
Recent news and announcements
Product/service offerings
Competitive landscape
```

⚠️ **BATCH SIZE WARNING:** Start conservative to avoid token limit failures
- **First batch:** 3-4 broad searches maximum (NOT 8-10)
- **Second batch:** 3-4 targeted searches
- **Never exceed:** 5 queries per batch
- **If failure occurs:** Immediately retry with 2-3 queries (half the batch)

**Use batch searches when researching multiple topics simultaneously** - More efficient than sequential searches, but respect token limits.

**Phase B: Deep Dive Information Gathering**

Based on initial findings, conduct targeted searches and scraping:

- Search for specific data points identified as important
- Scrape key company website pages (About, Products, Newsroom, Investors)
- Scrape relevant articles, reports, and announcements
- Cross-reference facts across multiple sources

⚠️ **WEBSITE SCRAPING WARNING:** Be conservative with batch sizes
- **Homepage + About page:** 2 URLs together (likely large pages)
- **Product/pricing pages:** 2-3 URLs per batch
- **Never exceed:** 3 URLs per batch
- **If page suspected to be long:** Scrape individually
- **If failure occurs:** Retry with 1-2 URLs only

**Use batch scraping for related URLs** - Scrape competitor websites or multiple company pages together, but never exceed 3 URLs per batch.

**Phase C: Competitive/Comparative Research** (if applicable)

For competitive analysis:

- Research all competitors using parallel search batches
- Scrape all competitor websites systematically
- Gather same data points for each competitor
- Create comparison tables as research progresses

See `references/research-methodology.md` for detailed search query examples and best practices.

### 4. Analyze and Synthesize

**Apply Analytical Frameworks:**

Depending on the research objective, apply relevant frameworks from `references/consulting-frameworks.md`:

- **Strategic Analysis** - Porter's Five Forces, SWOT, Value Chain
- **Competitive Positioning** - Strategic groups, positioning matrix
- **Market Analysis** - TAM/SAM/SOM, customer segmentation
- **Financial Analysis** - Unit economics, growth metrics
- **Product Analysis** - Feature comparison, technology assessment

**Generate Insights:**
- Go beyond raw data to interpretation
- Identify patterns and implications
- Draw evidence-based conclusions
- Make strategic recommendations when requested

**Quality Assurance:**
- Verify key facts across multiple sources
- Flag conflicting information
- Note data gaps clearly
- Assess recency of information
- Prioritize primary sources

### 5. Create the Report

**Select Appropriate Report Structure:**

Choose from templates in `references/report-templates.md` based on the request:

- **Company Profile Report** - For single-company deep dives
- **Competitive Analysis Report** - For multi-company comparisons
- **Market Entry Analysis** - For new market assessment
- **Product Comparison Report** - For product/service evaluation
- **Industry Analysis Report** - For sector-level intelligence
- **Quick Comparison Matrix** - For rapid comparative analysis
- **Presentation Deck** - For client-facing presentations

**Report Quality Standards:**

- **Executive Summary** - Lead with key findings and recommendations
- **Clear Structure** - Use headings and sections from templates
- **Data Presentation** - Tables for comparisons, bullets for lists, prose for analysis
- **Source Attribution** - Cite sources for key claims
- **Professional Tone** - Enterprise consulting quality
- **Actionable Insights** - Provide clear implications and recommendations
- **Completeness** - Address all clarifying questions answered at the start

### Output Schema

Use this schema for structuring company profile outputs. Ensures consistency across all profiles.

**Company Profile Schema:**

```markdown
# [Company Name] - Competitor Profile

## Executive Summary
[2-3 paragraph overview with key findings]

## Company Overview
| Attribute | Value |
|-----------|-------|
| Founded | YYYY |
| Headquarters | City, State/Country |
| CEO | Name |
| Ownership | Public/Private/PE-backed |
| Funding | $XXM (total raised) |
| Employees | X,XXX (est.) |
| Customers | X,XXX schools / X.XM students |

## Products & Services
### Core Platform
[Description of main offering]

### Key Features
- Feature 1: [description]
- Feature 2: [description]
- Feature 3: [description]

### Integrations
[List of key integrations with SIS, LMS, etc.]

## Pricing
| Tier | Price Range | Notes |
|------|-------------|-------|
| [Tier name] | $X-Y per student | [conditions] |

**Pricing Confidence:** Verified/Estimated/Unknown
**Source:** (Source, YYYY)

## Market Position
### Target Segments
[Primary customer segments]

### Geographic Focus
[Markets served]

### Competitive Positioning
[How company positions itself vs. competitors]

## SWOT Analysis
| Strengths | Weaknesses |
|-----------|------------|
| - Item 1  | - Item 1   |
| - Item 2  | - Item 2   |

| Opportunities | Threats |
|---------------|---------|
| - Item 1      | - Item 1|
| - Item 2      | - Item 2|

## Customer Sentiment
**G2 Rating:** X.X/5 (N reviews)
**Key Praise:** [summary]
**Key Complaints:** [summary]

## Sources
- [Source 1](URL) - accessed YYYY-MM-DD
- [Source 2](URL) - accessed YYYY-MM-DD
```

**Usage Notes:**
- Adapt schema sections based on available data
- Mark unknown fields as "Not available" rather than omitting
- Include confidence levels for estimated data
- Add industry-specific sections as needed

**Format Flexibility:**
- Adapt templates to specific needs
- Combine elements from multiple templates if needed
- Match the format to the stated audience and purpose

## Best Practices

### Research Excellence

1. **Triangulate Information** - Verify key facts from 2-3 independent sources
2. **Prioritize Primary Sources** - Company websites, SEC filings, official reports
3. **Check Recency** - Note publication dates, prefer recent data
4. **Flag Gaps** - Clearly state when information is unavailable
5. **Maintain Objectivity** - Seek disconfirming evidence, not just supporting
6. **Provide Context** - Explain what numbers mean in industry context

### Citation Generation

**Citation Format:**
All factual claims must include inline citations using `(Source, YYYY)` format.

**What Requires Citation:**
- Pricing data: "$X per student (Company Website, 2024)"
- Market share: "12% market share (Industry Report, 2024)"
- Customer counts: "serving 2,400 schools (Company, 2024)"
- Funding amounts: "raised $42M (Crunchbase, 2024)"
- Ratings: "4.6/5 on G2 (G2, November 2024)"
- Growth metrics: "40% YoY growth (Company Report, 2024)"

**Source Quality Hierarchy:**
1. **Primary Sources (Preferred):**
   - Company website (official pages)
   - SEC filings (for public companies)
   - Official press releases
   - Company annual reports

2. **Secondary Sources (Good):**
   - Industry analyst reports (Gartner, Forrester)
   - Reputable news outlets
   - Funding databases (Crunchbase, PitchBook)

3. **Tertiary Sources (Use with caution):**
   - Review sites (G2, Capterra) - good for sentiment
   - Wikipedia - verify against primary sources
   - Blog posts - verify claims independently

**Confidence Levels:**
- **Verified:** Multiple authoritative sources confirm
- **Estimated:** Single source or industry inference
- **Unknown:** No reliable source found (note explicitly)

**Example Citation Block:**
```
## Sources Referenced
- [Company About Page](https://company.com/about) - accessed 2024-11-25
- [Crunchbase Profile](https://crunchbase.com/company) - funding data
- [G2 Reviews](https://g2.com/products/company) - customer sentiment
- [Industry Report](https://analyst.com/report) - market analysis
```

### Output Location

**Where to Save Research Outputs:**

For projects following the standard template structure:

```
[PROJECT]/
├── 01-RESEARCH-INPUTS/
│   ├── company-profiles/
│   │   └── [company-name].md          # Company profile documents
│   ├── competitor-profiles/
│   │   └── [competitor-name]-profile.md   # Competitor profiles
│   └── raw-data/
│       └── [topic]-research-notes.md   # Raw research notes
├── 02-ANALYSIS-OUTPUTS/
│   ├── comparative-analysis/
│   │   └── [analysis-type].md         # Comparison matrices, pricing
│   └── strategic-insights/
│       └── [insight-type].md          # SWOT, recommendations
└── 03-DELIVERABLES/
    └── current/
        └── [deliverable].md           # Final client deliverables
```

**File Naming Conventions:**
- Company profiles: `[company-name].md` (lowercase, hyphens)
- Competitor profiles: `[NN]-[COMPANY]-profile.md` (numbered for ordering)
- Analysis outputs: `[analysis-type].md` (descriptive name)
- Deliverables: `[deliverable-name]-CORRECTED.md` (versioned)

**When Asked to Research:**
1. Clarify where user wants output saved
2. If no preference, use standard structure above
3. Create directories if they don't exist
4. Save intermediate research to raw-data/
5. Save polished outputs to appropriate location

### Efficiency

1. **Batch Operations** - Use batch search and scrape tools when researching multiple items (see critical sizing guidelines below)
2. **Start Broad** - Get overview first, then drill down into specifics
3. **Organize As You Go** - Build comparison tables during research, not after
4. **Time-Box Research** - Know when enough data is enough
5. **Template-Based** - Start with report structure, fill in findings

### Batch Size Guidelines (Critical!)

⚠️ **IMPORTANT: MCP tool responses are capped at 25,000 tokens. Exceeding this causes failures.**

**Search Engine Batching:**
- **Recommended:** 3-4 queries per batch
- **Maximum:** 5 queries per batch (to stay under 25k token limit)
- **Rationale:** Google search results average 2,000-5,000 tokens each (especially with AI overviews, featured snippets, related searches)
- **Strategy:** If batch fails, immediately retry with half the batch size
- **Single queries:** Use individual `search_engine` for 1-2 queries only

**Website Scraping Batching:**
- **Recommended:** 2-3 URLs per batch
- **Maximum:** 3 URLs per batch (websites can be lengthy when converted to markdown)
- **Rationale:** Website scrapes average 5,000-10,000+ tokens each in markdown format
- **Strategy:** Scrape homepages and large content pages individually if suspected to be verbose
- **Single URLs:** Use individual `scrape_as_markdown` for 1-2 URLs only

**Why These Limits Exist:**
- Google search results with AI overviews can be 4,000-5,000 tokens per query
- Website content converted to markdown can easily exceed 8,000-10,000 tokens
- 10 searches × 3,000 tokens = 30,000 tokens (exceeds limit)
- 5 website scrapes × 6,000 tokens = 30,000 tokens (exceeds limit)
- Better to do multiple small batches than fail and retry

**Conservative Batching Example (Comprehensive Company Research):**
```
Batch 1 (4 searches): Company overview, products, pricing, recent news
Batch 2 (4 searches): Customer reviews, competitors, market share, integrations
Scrape Batch 1 (2 URLs): Homepage, about page
Scrape Batch 2 (3 URLs): Products page, pricing page, features page
```

**Failure Recovery Protocol:**

If you encounter "exceeds maximum allowed tokens (25000)" error:
1. **Immediately retry with exactly half the batch size**
2. **Do not attempt to optimize** - simply cut the batch in half
3. **Log the failure** - note which queries/URLs caused issues for future reference
4. **Continue systematically** - complete smaller batches sequentially

**When to Use Maximum Batch Sizes:**
- Only for known-concise queries (e.g., "company founding date", "CEO name")
- Only for known-small websites (e.g., simple about pages, contact pages)
- When you have high confidence results will be brief

### Professional Quality

1. **Clear Methodology** - Explain how research was conducted
2. **Evidence-Based** - Support claims with data and sources
3. **Balanced Analysis** - Present strengths and weaknesses fairly
4. **Strategic Framing** - Connect findings to business implications
5. **Executive-Ready** - Make reports actionable for decision-makers

## Common Use Cases

### Single Company Deep Dive
1. Clarify: What aspects to focus on, audience, format
2. Research: Batch search across company topics, scrape company website
3. Analyze: Apply SWOT or relevant framework
4. Report: Use Company Profile Report template

### Head-to-Head Competitive Analysis
1. Clarify: Which companies, key comparison dimensions, decision being made
2. Research: Parallel batch searches for all companies, scrape all company sites
3. Analyze: Create comparison matrices, positioning map
4. Report: Use Competitive Analysis Report template

### Market Landscape Analysis
1. Clarify: Market definition, level of detail needed, strategic questions
2. Research: Industry trends, major players, market dynamics
3. Analyze: Porter's Five Forces, strategic group mapping
4. Report: Use Industry Analysis Report or Market Entry Analysis template

### Product/Service Comparison
1. Clarify: Products being compared, evaluation criteria, use cases
2. Research: Product pages, documentation, reviews for all products
3. Analyze: Feature matrices, use case fit analysis
4. Report: Use Product Comparison Report template

## References

- **consulting-frameworks.md** - Strategic analysis frameworks (Porter's Five Forces, SWOT, Business Model Canvas, competitive positioning, market sizing, financial analysis)
- **report-templates.md** - Proven report structures for different deliverable types (company profiles, competitive analysis, market entry, product comparison, quick matrices)
- **research-methodology.md** - Detailed search strategies, query examples, scraping best practices, source prioritization, and quality assurance processes

Load these references as needed based on the specific research objective and analytical requirements.
