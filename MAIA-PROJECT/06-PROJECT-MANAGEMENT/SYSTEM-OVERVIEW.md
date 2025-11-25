# Project Management System - How It All Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    NEW CONVERSATION STARTS                       │
│                                                                   │
│  User adds Project Knowledge with FOR-PROJECT-KNOWLEDGE.md       │
│                            ▼                                      │
│              Claude reads Project Knowledge                       │
│                            ▼                                      │
│              Checks CONTINUATION-NOTES.md                         │
│                  (Where did we leave off?)                        │
│                            ▼                                      │
│               Checks TASK-TRACKER.md                              │
│              (What task are we working on?)                       │
│                            ▼                                      │
│     Reads PROJECT-INSTRUCTIONS.md if needed for details           │
│                            ▼                                      │
│            Summarizes status to user concisely                    │
│                            ▼                                      │
│     Asks: Continue task | Review progress | Discuss/brainstorm   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    WORKING ON TASKS                              │
│                                                                   │
│  1. Execute current task from TASK-TRACKER.md                    │
│  2. Use competitive-research-brightdata skill + tools             │
│  3. Follow methodology in PROJECT-INSTRUCTIONS.md                │
│  4. As subtasks complete, check them off in TASK-TRACKER.md     │
│  5. Update phase progress percentages                            │
│  6. Write task summaries (2-3 sentences)                         │
│  7. Update progress-tracker.md in 00-PROJECT-OVERVIEW/          │
│  8. Add sources to sources-index.md as you research              │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│               CONVERSATION LIMIT APPROACHING                     │
│                                                                   │
│  1. Update TASK-TRACKER.md                                        │
│     - Check off completed items                                  │
│     - Write summary for partially complete tasks                 │
│     - Update time spent                                          │
│                            ▼                                      │
│  2. Add entry to CONTINUATION-NOTES.md                           │
│     - What was happening                                         │
│     - What's next                                                │
│     - Any important context                                      │
│                            ▼                                      │
│  3. Optionally create progress report in PROGRESS-REPORTS/      │
│                            ▼                                      │
│            CONVERSATION ENDS - NO PROBLEM!                        │
│                                                                   │
│       Next conversation will pick up seamlessly                   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                 DISCUSSION/BRAINSTORMING MODE                    │
│                                                                   │
│  1. Check progress-tracker.md for current status                 │
│  2. Read relevant completed profiles/analyses                    │
│  3. Ground discussion in actual research findings                │
│  4. Reference specific data and sources                          │
│  5. If valuable insights emerge, add to relevant docs            │
│  6. If gaps identified, add to RESEARCH-GAPS.md                  │
│  7. Suggest potential next research steps                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## File Relationships

```
PROJECT-INSTRUCTIONS.md (Master context document)
    ↓
    References all other files
    ↓
CONTINUATION-NOTES.md ←→ TASK-TRACKER.md
    ↓                           ↓
Quick handoff notes      Detailed task list
    ↓                           ↓
Latest entry             Current checkboxes
    ↓                           ↓
Where we left off        What to work on next

RESEARCH-GAPS.md ←→ METHODOLOGY-NOTES.md
    ↓                      ↓
Track data gaps      Research decisions
    ↓                      ↓
Flag deep dives      Document adjustments
```

---

## Document Hierarchy by Use Case

### "I'm a new conversation, what do I do?"
1. FOR-PROJECT-KNOWLEDGE.md (in Project Knowledge)
2. CONTINUATION-NOTES.md (latest entry)
3. TASK-TRACKER.md (find current task)
4. PROJECT-INSTRUCTIONS.md (full context if needed)

### "I'm working on research tasks"
1. TASK-TRACKER.md (what to do)
2. PROJECT-INSTRUCTIONS.md (how to do it)
3. METHODOLOGY-NOTES.md (research approach)
4. Company profile template (in Maia Learning profile)

### "Conversation limit is approaching"
1. TASK-TRACKER.md (update checkboxes & summaries)
2. CONTINUATION-NOTES.md (add handoff entry)
3. progress-tracker.md (update phase %)
4. Optional: Create progress report

### "User wants to discuss/brainstorm"
1. progress-tracker.md (current status)
2. Relevant company profiles (read completed work)
3. RESEARCH-GAPS.md (note any gaps identified)
4. Relevant analysis docs (if discussing specific topics)

---

## The Beautiful Loop

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│  Conversation 1: Work → Update trackers → Limit hits         │
│        ↓                                                      │
│  Trackers saved → Handoff notes written                      │
│        ↓                                                      │
│  Conversation 2: Read trackers → Pick up exactly where left  │
│        ↓                                                      │
│  Work → Update trackers → Limit hits                         │
│        ↓                                                      │
│  Trackers saved → Handoff notes written                      │
│        ↓                                                      │
│  Conversation 3: Read trackers → Continue seamlessly         │
│        ↓                                                      │
│  [Repeat indefinitely until project complete]                │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**The Key Insight:**
By maintaining state in markdown files with clear protocols, we make conversation handoffs completely seamless. Each new conversation can pick up EXACTLY where the last one left off, with full context, no loss of progress, and clear next steps.

---

## Success Metrics

**System is working when:**
- ✅ New conversations start with clear understanding of status
- ✅ No work is lost when conversation limits hit
- ✅ Tasks are tracked and checkable
- ✅ Progress is visible at multiple levels (task, phase, project)
- ✅ Handoffs are seamless and require no user explanation
- ✅ User can brainstorm/discuss at any time with full context
- ✅ Research maintains consistent quality across conversations

**You know it's working when:**
The user never has to explain where you are in the project - you just know.