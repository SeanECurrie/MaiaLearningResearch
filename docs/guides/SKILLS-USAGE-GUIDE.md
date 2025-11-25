# Skills Usage Guide for Competitive Analysis

**Purpose:** How to use Claude skills effectively for competitive analysis projects
**Created:** November 25, 2025
**Based On:** Maia Learning competitive analysis project experience

---

## Overview

This guide documents how to use Claude Code skills effectively throughout a competitive analysis project. Skills fall into two categories:

1. **Custom Skills (Domain-Specific)** - Specialized for competitive research tasks
2. **Superpowers Skills (Process/Workflow)** - General workflow and development practices

---

## Skill Categories

### Custom Skills

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| `competitive-research-brightdata` | Enterprise-grade company research using Bright Data tools | Research phase - gathering competitor data |
| `competitive-analysis-quality-assurance` | Fact-checking, source verification, consistency review | QA phase - before client delivery |

### Superpowers Skills

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| `superpowers:brainstorming` | Refine ideas into designs through questioning | Project setup, major pivots, clarifying requirements |
| `superpowers:writing-plans` | Create detailed implementation plans | Before major implementation work |
| `superpowers:executing-plans` | Execute plans in controlled batches | Implementing multi-task plans |
| `superpowers:verification-before-completion` | Verify work before claiming done | Before any completion claim |
| `superpowers:using-git-worktrees` | Isolate work in separate worktrees | Optional: for risky changes |
| `superpowers:requesting-code-review` | Get implementation reviewed | After completing major features |

---

## When to Use Each Skill

### By Project Phase

#### Phase 1: Project Setup
**Skills:** `superpowers:brainstorming`

Use brainstorming to:
- Clarify project objectives
- Define scope boundaries
- Identify key stakeholders
- Establish success criteria
- Resolve ambiguous requirements

#### Phase 2: Research
**Skills:** `competitive-research-brightdata`

Use research skill to:
- Gather competitor data systematically
- Execute batch searches efficiently
- Scrape company websites
- Apply consulting frameworks
- Create structured profiles

#### Phase 3: Analysis
**Skills:** None required (manual analysis)

During analysis:
- Apply SWOT, Porter's Five Forces frameworks
- Create comparison matrices
- Build positioning maps
- Generate strategic recommendations
- Manual work, no specific skill needed

#### Phase 4: Deliverables
**Skills:** None required (manual creation)

During deliverable creation:
- Write executive summary
- Create full report
- Generate visualizations
- Format for client
- Manual work, no specific skill needed

#### Phase 5: QA
**Skills:** `competitive-analysis-quality-assurance`

Use QA skill to:
- Verify facts and claims
- Validate source citations
- Check cross-document consistency
- Identify gaps
- Generate QA report

#### Phase 6: Iterations
**Skills:** `superpowers:brainstorming` → `superpowers:writing-plans` → `superpowers:executing-plans`

For major iterations:
1. **Brainstorm** - Clarify feedback and requirements
2. **Write Plan** - Create detailed implementation plan
3. **Execute Plan** - Implement changes in batches
4. **QA** - Verify changes meet requirements

#### Phase 7: Verification
**Skills:** `superpowers:verification-before-completion`

Before claiming done:
- Run verification commands
- Confirm expected outputs
- Document completion evidence
- Never claim done without verification

---

## Skill Quick Reference

### competitive-research-brightdata

**Trigger Phrases:**
- "Research [company]"
- "Competitive analysis of X vs Y"
- "Create a market report"
- "Analyze the [industry] landscape"

**Key Capabilities:**
- Batch search (3-4 queries max per batch)
- Batch scrape (2-3 URLs max per batch)
- Framework application (SWOT, Porter's, etc.)
- Report generation

**Critical Constraints:**
- 25,000 token limit on MCP responses
- Always start conservative with batch sizes
- Use failure recovery protocol if exceeded

---

### competitive-analysis-quality-assurance

**Trigger Phrases:**
- "Review this competitive analysis"
- "Fact-check these findings"
- "Verify the sources"
- "Quality check this report"

**Review Types:**
- Quick Validation (30-60 min)
- Standard Review (2-4 hours)
- Comprehensive Audit (1-2 days)
- Targeted Fact-Check (variable)

**Output Symbols:**
- ✅ Verified
- ⚠️ Partially Verified
- ❌ Not Verified
- 🔗 Broken Link
- 📅 Outdated

---

### superpowers:brainstorming

**When to Use:**
- Starting a new project
- Receiving ambiguous requirements
- Making strategic pivots
- Before major implementation

**Process:**
1. Present initial understanding
2. Ask clarifying questions
3. Explore alternatives
4. Validate assumptions
5. Document decisions

---

### superpowers:writing-plans

**When to Use:**
- Before implementing complex changes
- After brainstorming completes
- For multi-day implementation work

**Plan Structure:**
- Clear objectives
- Atomic tasks (can be completed independently)
- Verification commands for each task
- Batch groupings

---

### superpowers:executing-plans

**When to Use:**
- After plan is approved
- For systematic implementation
- When verification gates needed

**Process:**
1. Load plan file
2. Execute in 3-task batches
3. Verify each task
4. Report after each batch
5. Stop on verification failure

---

### superpowers:verification-before-completion

**When to Use:**
- Before claiming any task complete
- Before committing/pushing code
- Before client delivery

**Rule:**
- Never claim "done" without running verification
- Evidence before assertions
- If verification fails, task is not complete

---

## Skill Invocation Syntax

### Unified Invocation Patterns

**Custom Skills (via Skill tool):**
```
Skill: competitive-research-brightdata
Skill: competitive-analysis-quality-assurance
```

**Superpowers via Slash Command:**
```
/superpowers:brainstorm
/superpowers:write-plan
/superpowers:execute-plan
```

**Superpowers via Skill Tool:**
```
Skill: superpowers:brainstorming
Skill: superpowers:writing-plans
Skill: superpowers:executing-plans
Skill: superpowers:verification-before-completion
```

### Syntax Notes

- Slash commands use hyphens: `/superpowers:write-plan`
- Skill tool uses full names: `Skill: superpowers:writing-plans`
- Custom skills don't have slash command equivalents
- Both invocation methods load the same skill content

---

## Common Mistakes to Avoid

### Mistake 1: Skipping Brainstorming

**Problem:** Jumping straight into implementation without clarifying requirements.

**Consequence:** Rework when requirements were misunderstood. In Maia project, V1.0 was international-focused but client wanted US-primary - this could have been caught with brainstorming.

**Solution:** Always use `superpowers:brainstorming` when:
- Requirements are ambiguous
- Multiple approaches are possible
- Strategic direction is unclear

---

### Mistake 2: Not Using QA Skill

**Problem:** Skipping formal QA review before client delivery.

**Consequence:** Inconsistencies, missing citations, and factual errors reach the client. In Maia project, QA found 100+ missing citations and cross-document inconsistencies.

**Solution:** Always use `competitive-analysis-quality-assurance` when:
- Preparing deliverables for client
- After major revisions
- Before any "final" claim

---

### Mistake 3: Skipping Verification

**Problem:** Claiming tasks complete without running verification commands.

**Consequence:** "Done" claims that aren't actually done. Changes not made, files not created, tests not passing.

**Solution:** Always use `superpowers:verification-before-completion` when:
- About to claim any task complete
- Before committing code
- Before marking plan tasks done
- Before client delivery

**Rule:** If you haven't run verification, it's not done.

---

## Advanced Skill Workflows

### Major Iteration Workflow (V2.0-style changes)

Use this workflow for significant changes like strategic pivots, major revisions, or client feedback implementation:

```
┌─────────────────────────────────────────────────────────────────┐
│ MAJOR ITERATION WORKFLOW                                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. superpowers:brainstorming                                   │
│     └── Clarify feedback, resolve ambiguities                   │
│                                                                 │
│  2. superpowers:writing-plans                                   │
│     └── Create detailed implementation plan with tasks          │
│                                                                 │
│  3. superpowers:using-git-worktrees (optional)                  │
│     └── Isolate work if changes are risky                       │
│                                                                 │
│  4. superpowers:executing-plans                                 │
│     └── Implement changes in 3-task batches                     │
│                                                                 │
│  5. competitive-analysis-quality-assurance                      │
│     └── Verify all changes, check consistency                   │
│                                                                 │
│  6. superpowers:verification-before-completion                  │
│     └── Final check before claiming done                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**When to Use:**
- Receiving client feedback requiring strategic changes
- Making changes affecting multiple documents
- Implementing changes that took >2 hours to plan
- Any change that modifies >3 files

**Example:** Maia V2.0 revisions used this workflow to flip from international-primary to US-primary strategy across executive summary, full report, and 3 visualization PDFs.

---

### Quick Update Workflow (Minor corrections)

Use this abbreviated workflow for small fixes, typo corrections, or single-document updates:

```
┌─────────────────────────────────────────────────────────────────┐
│ QUICK UPDATE WORKFLOW                                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Make changes directly                                       │
│     └── Edit the file(s) as needed                              │
│                                                                 │
│  2. competitive-analysis-quality-assurance (quick check)        │
│     └── Spot-check changes, verify no new inconsistencies       │
│                                                                 │
│  3. superpowers:verification-before-completion                  │
│     └── Confirm changes are complete                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**When to Use:**
- Fixing typos or formatting issues
- Updating a single data point
- Adding a missing citation
- Correcting a single inconsistency

**Not For:** Multi-document changes, strategic pivots, or anything affecting >3 files.

---

### Research-to-Delivery Workflow (Full project)

Use this workflow for a complete competitive analysis project from start to finish:

```
┌─────────────────────────────────────────────────────────────────┐
│ FULL PROJECT WORKFLOW                                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PHASE 1: SETUP                                                 │
│  └── superpowers:brainstorming → clarify scope & requirements   │
│                                                                 │
│  PHASE 2: RESEARCH                                              │
│  └── competitive-research-brightdata → gather competitor data   │
│                                                                 │
│  PHASE 3: ANALYSIS                                              │
│  └── Manual → apply frameworks, create matrices                 │
│                                                                 │
│  PHASE 4: DELIVERABLES                                          │
│  └── Manual → write reports, create visualizations              │
│                                                                 │
│  PHASE 5: QA                                                    │
│  └── competitive-analysis-quality-assurance → verify all        │
│                                                                 │
│  PHASE 6: ITERATION (repeat as needed)                          │
│  └── Major Iteration Workflow or Quick Update Workflow          │
│                                                                 │
│  PHASE 7: FINAL DELIVERY                                        │
│  └── superpowers:verification-before-completion → confirm done  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Workflow Decision Guide

**Deciding which workflow to use:**

| Situation | Workflow | Skills Used |
|-----------|----------|-------------|
| New project | Full Project | All |
| Client says "change everything" | Major Iteration | brainstorm → write-plan → execute → QA → verify |
| Client says "fix this one thing" | Quick Update | direct edit → QA quick-check → verify |
| Client says "add more detail here" | Quick Update | direct edit → QA quick-check → verify |
| "I'm not sure what they want" | Start with brainstorming | brainstorming first, then decide |

---

**Document Updated:** November 25, 2025
