# Phase 1: Research

**Objective:** Gather comprehensive competitive intelligence
**Skill:** `Skill: competitive-research-brightdata`

---

## Pre-Research Checklist

Before starting research:

- [ ] Identify 5-7 primary competitors
- [ ] Identify 3-5 secondary competitors (for comparison/context)
- [ ] Define research questions (see template below)
- [ ] Set up research tracking spreadsheet
- [ ] Create sources.md file for citations

---

## Research Questions Template

Copy these questions for each competitor:

### Company Overview:
1. What is the company's official name and website?
2. When was the company founded?
3. Who are the founders/key executives?
4. What is their mission statement/positioning?

### Pricing:
5. What is the per-student cost? (verify or estimate)
6. What pricing model do they use? (per-student, per-school, tiered)
7. Are there setup fees or contracts?
8. What discounts are available? (volume, multi-year, etc.)

### Features:
9. What are the top 10 core features?
10. What AI capabilities do they have?
11. What integrations do they offer?
12. What makes them unique/differentiated?

### Market Position:
13. What is their estimated market share?
14. How many students/schools do they serve?
15. What geographic markets do they serve?
16. What customer segments do they target?

### Funding & Growth:
17. What is their latest funding round? (amount, date, investors)
18. What is their estimated revenue?
19. What is their growth rate? (if known)
20. Are they profitable or burning cash?

### Customer Satisfaction:
21. What are their public review ratings? (G2, Capterra, etc.)
22. What do customers praise?
23. What do customers complain about?
24. What is their NPS score? (if available)

---

## Using competitive-research-brightdata

### Step 1: Prepare competitor list

Create `01-RESEARCH-INPUTS/competitor-list.md`:

```markdown
# Competitor List

## Primary Competitors:
1. [Competitor 1] - [Website]
2. [Competitor 2] - [Website]
3. [Competitor 3] - [Website]
4. [Competitor 4] - [Website]
5. [Competitor 5] - [Website]

## Secondary Competitors:
1. [Competitor 6] - [Website]
2. [Competitor 7] - [Website]
```

### Step 2: Invoke skill

```
Skill: competitive-research-brightdata

Provide:
- Competitor names
- Research questions (from template above)
- Output format preference (JSON/CSV/Markdown)
```

### Step 3: Organize research outputs

```bash
# Create directory structure
mkdir -p 01-RESEARCH-INPUTS/competitor-data/
mkdir -p 01-RESEARCH-INPUTS/market-research/
mkdir -p 01-RESEARCH-INPUTS/pricing-data/
mkdir -p 01-RESEARCH-INPUTS/feature-data/

# Move skill outputs to appropriate directories
```

---

## Manual Research Tasks

**Not everything can be automated. Manually research:**

### 1. Review Sites:
- G2.com (search for each competitor)
- Capterra.com (category: CCR platforms)
- TrustRadius (education software)
- ProductHunt (for new/innovative platforms)

**Record:**
- Rating (X.X/5)
- Number of reviews
- Recent review themes
- Source URL + date accessed

### 2. Funding Databases:
- Crunchbase (company profiles, funding rounds)
- PitchBook (private company data)
- CB Insights (market intelligence)

**Record:**
- Latest funding round (amount, date, investors)
- Total funding raised
- Valuation (if public)
- Source URL + date accessed

### 3. Company Websites:
- Read "About Us" pages
- Review pricing pages (screenshot if available)
- Explore feature lists
- Read case studies/testimonials
- Download any public materials (whitepapers, brochures)

**Record:**
- Official positioning statement
- Pricing (screenshot + transcribe)
- Feature lists
- Source: [Company Name] website, accessed [Date]

### 4. Industry Reports:
- Search for "[industry] market report"
- Search for "EdTech market sizing"
- Look for analyst reports (Gartner, Forrester if available)

**Record:**
- Market size estimates
- Growth projections
- Trends identified
- Source: [Report Name], [Publisher], [Date]

---

## Sources.md Template

Create `01-RESEARCH-INPUTS/sources.md`:

```markdown
# Research Sources

**Project:** [Company Name] Competitive Analysis
**Research Period:** [Start Date] - [End Date]

---

## Competitor-Specific Sources

### [Competitor 1]

1. **Company Website**
   - URL: https://...
   - Date Accessed: YYYY-MM-DD
   - Data Gathered: Pricing, features, positioning

2. **G2 Reviews**
   - URL: https://g2.com/products/[competitor]
   - Date Accessed: YYYY-MM-DD
   - Rating: X.X/5 (N reviews)

3. **Crunchbase**
   - URL: https://crunchbase.com/organization/[competitor]
   - Date Accessed: YYYY-MM-DD
   - Funding: $XM (Series A, Date)

---

## Citation Format

Use this format in deliverables:
- `(Company Name, YYYY)` - for company-reported data
- `(G2, YYYY)` - for review ratings
- `(Crunchbase, YYYY)` - for funding data
- `(Industry Report Name, YYYY)` - for market data
```

---

## Research Tracking Spreadsheet

Create `01-RESEARCH-INPUTS/research-tracker.csv`:

```csv
Competitor,Pricing Verified,Features Listed,Reviews Found,Funding Found,Website Scraped,Completeness %
Competitor 1,Yes,Yes,Yes,Yes,Yes,100%
Competitor 2,Estimated,Yes,Yes,No,Yes,80%
```

---

## Common Research Challenges

### Challenge 1: Pricing Not Public

**Solution:**
- Mark as "(est.)" or "not publicly disclosed"
- Use ranges from industry reports
- Check for old pricing pages (Wayback Machine)
- Note in disclaimer: "Estimated from industry sources"

### Challenge 2: Conflicting Data

**Solution:**
- Document all sources
- Use most recent data
- Note discrepancy in footnote
- Prefer official company sources over third-party

### Challenge 3: Incomplete Feature Data

**Solution:**
- Use "Features advertised on website"
- Note: "Full feature list may not be public"
- Compare only advertised features
- Mark unknown features as "Unknown/Not Advertised"

---

## Research Phase Completion Checklist

Before moving to Analysis Phase:

- [ ] All competitors researched (5-7 primary)
- [ ] Research questions answered (20 per competitor)
- [ ] All sources documented in sources.md
- [ ] Research tracker shows 80%+ completeness
- [ ] Data organized in directory structure
- [ ] Gaps identified and documented (some data unavailable is OK)

---

## Next Phase

Once research is complete, move to:
**[02-ANALYSIS-PHASE.md](./02-ANALYSIS-PHASE.md)**
