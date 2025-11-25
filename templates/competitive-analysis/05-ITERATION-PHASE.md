# Phase 5: Iterations

**Objective:** Handle client feedback and revisions systematically
**Skills:**
- `superpowers:brainstorming` (clarify requirements)
- `superpowers:writing-plans` (plan implementation)
- `superpowers:executing-plans` (systematic execution)
- `competitive-analysis-quality-assurance` (verify changes)
- `superpowers:verification-before-completion` (final check)

---

## Iteration Workflow

```
Client Feedback Received
    ↓
superpowers:brainstorming (clarify requirements)
    ↓
superpowers:writing-plans (create implementation plan)
    ↓
superpowers:executing-plans (implement changes)
    ↓
competitive-analysis-quality-assurance (verify consistency)
    ↓
superpowers:verification-before-completion (final check)
    ↓
Version Bump (V1.0 → V2.0)
```

---

## Step 1: Receive and Clarify Feedback

### Using superpowers:brainstorming

When client feedback is received:

```
/superpowers:brainstorm

Present:
- Client's feedback (rough notes or recording)
- Current deliverables state
- Questions about unclear requirements
```

**Skill will:**
- Ask 5-8 clarifying questions
- Document answers
- Produce clear implementation requirements

**Output:** Clear change specifications with no ambiguity

---

## Step 2: Plan Implementation

### Using superpowers:writing-plans

Once requirements are clear:

```
/superpowers:write-plan

Provide:
- Clear requirements from brainstorming
- Current deliverables state
- Files that need to change
```

**Skill will create:**
- Multi-phase implementation plan
- Bite-sized tasks (2-5 minutes each)
- Verification steps for each task
- Plan file saved to `docs/plans/[date]-[iteration-name].md`

---

## Step 3: Execute Changes

### Using superpowers:executing-plans

Execute the plan systematically:

```
/superpowers:execute-plan docs/plans/[plan-file].md
```

**Process:**
- Execute tasks in 3-task batches
- Verify each task before marking complete
- Report after each batch for review
- Continue with next batch after feedback

---

## Step 4: Verify Changes

### Using competitive-analysis-quality-assurance

After all changes implemented:

```
Skill: competitive-analysis-quality-assurance

Provide:
- Updated deliverable files
- List of changes made
- Original requirements
```

**Verify:**
- All requested changes implemented
- No new inconsistencies introduced
- Quality maintained at 9.5/10
- Cross-document consistency preserved

### Using superpowers:verification-before-completion

Before marking iteration complete:

**Checklist:**
- [ ] All planned tasks completed
- [ ] All changes verified
- [ ] PDFs regenerated from updated sources
- [ ] No regressions introduced
- [ ] Documentation updated

---

## Step 5: Version Management

### Update VERSION-HISTORY.md

Add new version entry:

```markdown
## V2.0 ([Date]) - [Iteration Name]

**Changes:**
- [Change 1 description]
- [Change 2 description]
- [Change 3 description]

**Files Changed:**
- [file1.docx]
- [file2.html]
- [file3.pdf]

**Quality Score:** 9.5/10
**Consistency:** 100%
```

### Backup Previous Version

```bash
# Before making changes
cp -r 03-DELIVERABLES/current/ 03-DELIVERABLES/v1.0/
```

---

## Quick Iteration vs Full Iteration

### Use Quick Iteration For:
- Single data point update (pricing change)
- Typo fix
- Missing citation addition
- Small content addition (1-2 paragraphs)
- PDF regeneration after HTML fix

**Quick Process:**
1. Locate all affected files
2. Make changes directly
3. Run QA skill for consistency
4. Verify and commit

### Use Full Iteration For:
- Strategic direction changes
- Adding new competitor
- Restructuring recommendations
- Significant content rewrite
- Multiple interconnected changes

**Full Process:**
1. Brainstorm to clarify
2. Write plan
3. Execute plan
4. Verify with QA
5. Final verification

---

## Iteration Documentation

### Create Iteration Folder

```bash
mkdir -p 05-ITERATIONS/iteration-[N]-[name]/
```

### Required Documentation:

1. **NOTES.md** - Summary of iteration
2. **requirements.md** - Clear requirements from brainstorming
3. **plan.md** - Implementation plan (or link to docs/plans/)
4. **changes.md** - List of changes made
5. **lessons-learned.md** - What went well, what to improve

---

## Common Iteration Scenarios

### Scenario 1: Strategic Pivot

**Example:** Client wants to change from international-primary to US-primary strategy

**Process:**
1. Brainstorm: Clarify exactly what "US-primary" means
2. Plan: Create multi-phase implementation plan
3. Execute: Update all strategic recommendations, positioning, investments
4. Verify: Ensure 100% consistency across all documents
5. Version: Bump to V2.0

### Scenario 2: Data Update

**Example:** Competitor announced new funding round

**Process:**
1. Locate all funding references (grep)
2. Update funding data with new citation
3. Check for implications (threat assessment, etc.)
4. Regenerate affected PDFs
5. Version: Bump to V1.1

### Scenario 3: Feedback on Presentation

**Example:** Client wants four-quadrant map instead of scatter plot

**Process:**
1. Brainstorm: Clarify exact format requirements
2. Plan: Design new visualization approach
3. Execute: Create new HTML/CSS chart
4. Verify: Ensure all positioning logic preserved
5. Version: Bump to V1.2

---

## Iteration Phase Completion Checklist

For each iteration:

- [ ] Client feedback received and documented
- [ ] Requirements clarified (brainstorming complete)
- [ ] Implementation plan created
- [ ] All changes implemented
- [ ] QA verification passed
- [ ] Final verification passed
- [ ] VERSION-HISTORY.md updated
- [ ] Previous version backed up
- [ ] Iteration documentation complete

---

## End of Template

When all iterations are complete and client approves:
- Deliverables are client-ready
- Archive project documentation
- Document lessons learned for next project
