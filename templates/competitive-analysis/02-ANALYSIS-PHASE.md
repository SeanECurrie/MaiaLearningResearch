# Phase 2: Analysis

**Objective:** Transform raw research into strategic insights
**Skills:** Manual analysis (no specific skill required)

---

## Analysis Overview

This phase converts raw research data into structured analysis:
- Competitive matrices (feature, pricing, positioning)
- SWOT analyses (per competitor + client)
- Market positioning map (four-quadrant format)
- Strategic recommendations (5-7 priorities)

---

## Competitive Matrices

### Feature Comparison Matrix

Create `02-ANALYSIS-OUTPUTS/competitive-matrices/feature-comparison.csv`:

**Structure:**
- Rows: 50+ features across categories
- Columns: Client + 5-7 competitors
- Values: Yes/No/Partial/Unknown

**Categories to include:**
1. Core Platform Features (10-15 features)
2. College Planning Features (10-15 features)
3. Career Exploration Features (5-10 features)
4. AI/Technology Features (5-10 features)
5. Integration Capabilities (5-10 features)
6. Reporting & Analytics (5-10 features)

**Example:**
```csv
Category,Feature,Client,Competitor1,Competitor2,Competitor3
Core,Student Portal,Yes,Yes,Yes,Yes
Core,Parent Portal,Yes,Yes,Partial,No
AI,AI College Matching,Yes,Yes,Yes,No
```

---

### Pricing Comparison Matrix

Create `02-ANALYSIS-OUTPUTS/competitive-matrices/pricing-comparison.csv`:

**Structure:**
```csv
Competitor,Pricing Model,Low Range,High Range,Notes,Source,Confidence
Competitor1,Per-student,$8,$12,Enterprise only,Website 2024,Verified
Competitor2,Per-student,$4.80,$4.80,Public pricing,Website 2024,Verified
Competitor3,Per-student,$5,$7,Estimated,Industry report,Estimated
```

**Confidence Levels:**
- Verified: Confirmed on company website or official source
- Estimated: Based on industry reports or inference
- Unknown: No reliable data available

---

### Market Positioning Comparison

Create `02-ANALYSIS-OUTPUTS/competitive-matrices/positioning-comparison.csv`:

**Structure:**
```csv
Competitor,Primary Position,Target Segment,Geographic Focus,Key Differentiator
Competitor1,Market Leader,Enterprise K-12,US Domestic,Scale + Integration
Competitor2,Innovation Challenger,Mid-size schools,US Domestic,AI Features
Client,Global Specialist,International schools,70+ countries,International focus
```

---

## SWOT Analyses

### Per-Competitor SWOT

Create `02-ANALYSIS-OUTPUTS/swot-analyses/[competitor]-swot.md` for each competitor:

**Template:**
```markdown
# SWOT Analysis: [Competitor Name]

## Strengths
- [Strength 1 with evidence]
- [Strength 2 with evidence]
- [Strength 3 with evidence]

## Weaknesses
- [Weakness 1 with evidence]
- [Weakness 2 with evidence]
- [Weakness 3 with evidence]

## Opportunities
- [Market opportunity 1]
- [Market opportunity 2]
- [Market opportunity 3]

## Threats
- [Competitive threat 1]
- [Market threat 2]
- [Technology threat 3]

## Threat Level to Client: [HIGH/MEDIUM/LOW]
**Rationale:** [Why this competitor is/isn't a significant threat]
```

### Client SWOT

Create `02-ANALYSIS-OUTPUTS/swot-analyses/client-swot.md`:

Focus on:
- Strengths relative to competitors
- Weaknesses that need addressing
- Market opportunities to pursue
- Competitive threats to defend against

---

## Market Positioning Map

### Four-Quadrant Format

Create `02-ANALYSIS-OUTPUTS/market-positioning/positioning-map.md`:

**Dimensions:**
- X-axis: Market Coverage (Niche → Broad)
- Y-axis: Innovation Level (Traditional → Innovative)

**Quadrant Labels:**
- Q1 (Upper Right): IDEAL - High Innovation + Broad Coverage
- Q2 (Upper Left): Innovators - High Innovation + Niche Coverage
- Q3 (Lower Left): Specialists - Traditional + Niche Coverage
- Q4 (Lower Right): Incumbents - Traditional + Broad Coverage

**Position each competitor:**
```markdown
## Positioning Map

### Q1 - IDEAL (High Innovation + Broad Coverage)
- [Competitor X]: [Rationale for placement]

### Q2 - Innovators (High Innovation + Niche)
- [Competitor Y]: [Rationale]

### Q3 - Specialists (Traditional + Niche)
- [Client]: [Current position rationale]

### Q4 - Incumbents (Traditional + Broad)
- [Competitor Z]: [Rationale]

## Strategic Implications
- Client needs to move from Q3 → Q1
- Key investments needed: [List]
```

---

## Strategic Recommendations

### Framework for Recommendations

Create `02-ANALYSIS-OUTPUTS/strategic-recommendations/recommendations.md`:

**For each recommendation (5-7 total):**

```markdown
### Priority [N]: [Recommendation Title]

**Priority Level:** CRITICAL / HIGH / MEDIUM

**Objective:** [One sentence - what this achieves]

**Rationale:** [2-3 sentences with data supporting this recommendation]

**Implementation:**
- Action 1: [Specific action]
- Action 2: [Specific action]
- Action 3: [Specific action]

**Investment Estimate:** $[X]K - $[Y]K

**Expected Return:** [Quantified outcome]

**Source:** [Analysis reference]
```

### Investment Estimates

Create `02-ANALYSIS-OUTPUTS/strategic-recommendations/investment-estimates.md`:

**Template:**
```markdown
# Investment Summary

| Priority | Description | Investment | Timeline |
|----------|-------------|------------|----------|
| 1 | [Title] | $XK-YK | Q1-Q2 |
| 2 | [Title] | $XK-YK | Q2-Q3 |
| ... | ... | ... | ... |
| **Total** | | **$X.XM - $Y.YM** | |
```

---

## Analysis Phase Completion Checklist

Before moving to Deliverables Phase:

- [ ] Feature comparison matrix complete (50+ features)
- [ ] Pricing comparison matrix complete (all competitors)
- [ ] Positioning comparison complete
- [ ] SWOT analysis for each competitor (5-7)
- [ ] SWOT analysis for client
- [ ] Market positioning map created
- [ ] Strategic recommendations drafted (5-7)
- [ ] Investment estimates calculated
- [ ] All analysis outputs in `02-ANALYSIS-OUTPUTS/`

---

## Next Phase

Once analysis is complete, move to:
**[03-DELIVERABLES-PHASE.md](./03-DELIVERABLES-PHASE.md)**
