# Research Methodology and Best Practices

This reference provides systematic approaches for conducting thorough company research and competitive analysis using web search and scraping tools.

## Research Process Overview

### Phase 1: Clarification and Scoping
Understand the research objective before executing

### Phase 2: Information Gathering
Systematic collection using search and scraping

### Phase 3: Analysis and Synthesis
Organize and interpret findings

### Phase 4: Report Generation
Present insights in requested format

## Search Strategy Best Practices

### Effective Search Query Formulation

**Company Background Queries:**
- "[Company Name] about company overview"
- "[Company Name] company profile"
- "[Company Name] history founders"
- "[Company Name] headquarters locations"
- "[Company Name] leadership team executives"

**Financial Information Queries:**
- "[Company Name] revenue earnings"
- "[Company Name] funding investors"
- "[Company Name] valuation"
- "[Company Name] financial results"
- "[Company Name] quarterly earnings" (for public companies)

**Product/Service Queries:**
- "[Company Name] products services"
- "[Company Name] product lineup"
- "[Company Name] new product launch"
- "[Company Name] pricing"
- "[Company Name] features capabilities"

**Market Position Queries:**
- "[Company Name] market share"
- "[Company Name] competitors"
- "[Company Name] competitive position"
- "[Company Name] industry ranking"
- "[Company Name] vs [Competitor Name]"

**Recent Developments:**
- "[Company Name] news 2024" or current year
- "[Company Name] recent announcements"
- "[Company Name] acquisition merger"
- "[Company Name] partnership alliance"
- "[Company Name] product launch"

**Customer Sentiment:**
- "[Company Name] reviews"
- "[Company Name] customer satisfaction"
- "[Company Name] complaints"
- "[Company Name] testimonials"
- "[Company Name] ratings"

**Strategic Analysis:**
- "[Company Name] strategy"
- "[Company Name] business model"
- "[Company Name] growth strategy"
- "[Company Name] expansion plans"

### Search Source Prioritization

**Primary Sources (Highest Quality):**
1. Company official website (About, Investor Relations, Newsroom)
2. SEC filings (10-K, 10-Q, 8-K for public companies)
3. Company press releases
4. Investor presentations

**Secondary Sources (High Quality):**
1. Industry analyst reports (Gartner, Forrester, IDC)
2. Financial news (WSJ, Bloomberg, Reuters, Financial Times)
3. Industry publications (trade journals)
4. Market research firms (CB Insights, PitchBook, Crunchbase)

**Tertiary Sources (Validation/Supporting):**
1. Business news sites (TechCrunch, Business Insider)
2. Review sites (G2, Capterra, Trustpilot)
3. Social media (LinkedIn, Twitter for announcements)
4. Industry forums and communities

**Sources to Use Cautiously:**
- Wikipedia (good starting point, verify elsewhere)
- User forums (anecdotal, check patterns)
- Blog posts (verify author credibility)

### Search Engine Selection

**Google:** 
- Best for: General company information, recent news, broad coverage
- Use for: Initial research, diverse perspectives

**Bing:**
- Best for: Microsoft ecosystem, some unique business content
- Use for: Cross-validation, additional sources

**Yandex:**
- Best for: Companies with operations in Russia/Eastern Europe
- Use for: Regional market intelligence

## Batch Search Strategies

### Parallel Information Gathering

When researching multiple companies or topics, use `search_engine_batch` to run queries simultaneously:

**Example: Multi-Company Research**
```
Company A overview
Company A products
Company A financials
Company B overview
Company B products
Company B financials
```

**Example: Comprehensive Single-Company**
```
[Company] about overview
[Company] products services
[Company] revenue funding
[Company] recent news 2024
[Company] competitors market share
[Company] customer reviews
```

**Benefits:**
- Faster research completion
- Consistent point-in-time snapshot
- Efficient use of search quota

**Limits:**
- Maximum 10 queries per batch
- Plan query sets strategically

## Web Scraping Best Practices

### When to Scrape vs. When to Search

**Use Search When:**
- Discovering initial information
- Finding source URLs
- Gathering diverse perspectives
- Tracking recent news

**Use Scrape When:**
- Need complete content from known URLs
- Extracting structured data
- Getting full text of reports/articles
- Capturing detailed product information

### Effective Scraping Strategy

1. **Identify Target URLs from Search Results**
   - Company website pages (About, Products, Investors)
   - Press releases
   - News articles
   - Reports and whitepapers

2. **Prioritize Scraping Targets**
   - Official company sources first
   - Recent news and announcements
   - Detailed product documentation
   - Financial reports

3. **Batch Scraping for Efficiency**
   - Group related URLs
   - Maximum 10 URLs per batch
   - Scrape company sites together

### Recommended Pages to Scrape

**For Company Profiles:**
- Homepage (company positioning)
- About/Company page (history, mission)
- Leadership/Team page (executives)
- Products/Services page (offerings)
- Newsroom/Press page (recent updates)
- Careers page (company culture, growth)
- Contact/Locations page (geographic presence)

**For Competitive Analysis:**
- Pricing pages (all competitors)
- Product feature pages (all competitors)
- Customer case studies
- Partner/integration pages
- Documentation/resources

**For Financial Analysis:**
- Investor Relations page
- Annual reports (if accessible)
- Quarterly earnings releases
- Investor presentations

## Information Verification

### Cross-Reference Strategy

**Triangulation Approach:**
1. Verify key facts from 2-3 independent sources
2. Flag conflicting information
3. Prioritize primary sources over secondary

**Red Flags:**
- Single-source data points
- Outdated information
- Conflicting metrics across sources
- Suspiciously promotional content

### Data Recency

**Time-Sensitive Information:**
- Note publication/update dates
- Prefer recent sources (< 6 months for news, < 1 year for trends)
- For historical data, verify with current context

**Evergreen Information:**
- Company founding details
- Historical milestones
- Basic business model (unless pivoted)

## Handling Data Gaps

### When Information is Not Available

**Strategies:**
1. **Search more specifically** - Refine query terms
2. **Try alternative sources** - Industry databases, news archives
3. **Look for proxies** - Related metrics or comparable companies
4. **Check historical data** - Archive.org for older company info
5. **Flag as unavailable** - Clearly note in report

**Never:**
- Fabricate data
- Make unsupported assumptions
- Extrapolate without basis
- Present guesses as facts

**Instead:**
- State "Information not publicly available"
- Provide context for why data may be limited
- Suggest alternative approaches or proxies

## Competitive Intelligence Gathering

### Multi-Competitor Research Flow

1. **Create competitor list**
   - Primary competitors (direct)
   - Secondary competitors (adjacent)
   - Emerging competitors (up-and-coming)

2. **Parallel research batches**
   - Search all competitors simultaneously
   - Scrape all competitor websites in batches
   - Maintain consistency in data points collected

3. **Systematic comparison**
   - Use same criteria for all competitors
   - Note when data unavailable
   - Create standardized comparison tables

### Competitive Intelligence Sources

**Product Intelligence:**
- Product documentation
- Feature lists and comparisons
- Pricing pages
- Customer reviews and ratings
- Demo videos or screenshots

**Market Intelligence:**
- Press releases and announcements
- News coverage
- Industry reports
- Conference presentations
- Job postings (indicate growth areas)

**Customer Intelligence:**
- Case studies and testimonials
- Review sites (G2, TrustRadius, Capterra)
- Social media sentiment
- Support forums and communities

**Strategic Intelligence:**
- Leadership changes
- Funding announcements
- Partnerships and alliances
- Acquisitions
- Geographic expansion

## Quality Assurance Checklist

### Before Finalizing Research

**Completeness:**
- [ ] All requested information addressed
- [ ] Data gaps clearly flagged
- [ ] Sources cited for key claims
- [ ] Recency of data noted

**Accuracy:**
- [ ] Facts cross-referenced across sources
- [ ] Conflicting information noted and explained
- [ ] Primary sources prioritized
- [ ] Numbers and metrics verified

**Analysis Quality:**
- [ ] Insights go beyond raw data
- [ ] Frameworks applied appropriately
- [ ] Implications clearly stated
- [ ] Recommendations supported by evidence

**Presentation:**
- [ ] Report structure matches request
- [ ] Executive summary captures key points
- [ ] Tables/comparisons formatted clearly
- [ ] Professional tone maintained

## Common Research Pitfalls to Avoid

1. **Confirmation Bias** - Seek disconfirming evidence, not just supporting
2. **Recency Bias** - Don't overweight recent news vs. long-term patterns
3. **Source Credibility** - Verify before trusting unknown sources
4. **Incomplete Comparisons** - Ensure apples-to-apples metrics
5. **Analysis Paralysis** - Know when enough data is enough
6. **Missing Context** - Provide industry/market context for data points
7. **Overconfidence** - Acknowledge limitations and uncertainties

## Efficiency Tips

### Speed Up Research Without Sacrificing Quality

1. **Start with batch searches** - Gather multiple data points simultaneously
2. **Scrape company pages early** - Get comprehensive source material upfront
3. **Use comparison tables** - Organize findings as you go
4. **Template-based reporting** - Start with structure, fill in findings
5. **Prioritize ruthlessly** - Focus on most material information
6. **Time-box research phases** - Set limits to avoid rabbit holes
7. **Iterate if needed** - Start broad, drill down only where needed
