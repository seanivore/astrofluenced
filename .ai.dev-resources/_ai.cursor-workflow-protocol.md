# Cursor Workflow Protocol

## ⚠️ CRITICAL: Memory Search Requirements
The Memory MCP Server ONLY works with exact known terms - no partial matches or variations.
Always use the exact terms listed in this document for:
- Project names
- Time markers
- Category tags
- Relationship types

## Session Startup
1. Ask Sean: "What project are we working on?" to get exact project name
   - Verify name exists in Active Project Entities list
   - Name MUST match across: directory, git branch, GitHub repo, memory system

2. Create session entry with standardized date format:
   ```
   YYYY/MM/DD-project-name-session-start
   Example: 2025/02/19-claud-web-session-start
   ```

3. Document session goals:
   - Primary objective
   - Expected deliverables
   - Time constraints if any

4. Load and verify project state using exact project name
5. Create initial checkpoint
6. Confirm 20-minute timer set (ask Sean)

## Session Management

### Check-in Format
```markdown
## Session Check-in YYYY-MM-DD HH:MM
- Current Task: [Brief description]
- Session Goals: [Specific objectives]
- Progress Log: [Updates during session]
- Next Steps: [Clear continuation points]
```

### Create Checkpoints When:
1. Starting new major task
2. Every 20 minutes active
3. Before task switching
4. Upon user signal
5. Rate limit warning
6. Completing significant work

### Session End Protocol
1. Create final checkpoint
2. Document next steps
3. Update project state
4. Note continuation point

## Project State Structure
```javascript
project_state = {
    metadata: {
        name: string,           // Must match approved project name
        root_path: string,      // Full project path
        git_branch: string,     // Must match project name
        github_repo: string,    // Must match project name
        last_updated: timestamp,
        last_checkpoint: timestamp,
        last_session: timestamp,
        activity_log: timestamp[]
    },
    
    tracking: {
        current_phase: string,
        pending_tasks: string[],
        blocking_issues: string[],
        next_actions: string[],
        recent_updates: {
            timestamp: number,
            description: string
        }[]
    },

    relationships: {
        dependencies: string[],    // Other project names
        sub_projects: string[],
        related_projects: string[],
        update_cascade: boolean    // Whether changes affect related projects
    }
}
```

## Reference Section

### Time Markers
Must tag all entries with both year and month:
- year-2024
- year-2025
- month-01-january
- month-02-february
- month-03-march
- month-04-april
- month-05-may
- month-06-june
- month-07-july
- month-08-august
- month-09-september
- month-10-october
- month-11-november
- month-12-december

### Approved Relationship Types
- supports
- requires
- depends-on
- contains
- contributes-to
- contributes-evidence-to
- demonstrates-value-of
- blocks
- is-blocked-by

### Development Categories
- web-development
- mcp-integration
- api-design
- frontend-component
- backend-service
- database-schema
- authentication-flow
- testing-framework
- deployment-config

### Blockchain Categories
- tokenomics
- smart-contract
- wallet-integration
- solana-development
- transaction-flow
- blockchain-testing

### Content Categories
- blog-article
- technical-documentation
- api-documentation
- user-guide
- architectural-design
- research-paper
- grant-proposal
- project-presentation

### Analysis Categories
- performance-metrics
- user-feedback
- security-audit
- code-review
- architecture-review
- cost-analysis

### AI Integration Categories
- llm-integration
- prompt-engineering
- tool-development
- memory-system
- sequential-thinking
- consciousness-observation

### Project Management Categories
- milestone-tracking
- dependency-management
- resource-allocation
- risk-assessment
- team-collaboration

### 🚫 Never Use Generic Names Like:
- Project
- ProjectStructure
- StrategyTracker
- ResearchProject
- document
- task
- BehaviorAnalysis
- Technical_Component
- Documentation
- Implementation

## Error Recovery
1. Load last stable checkpoint
2. Verify state consistency
3. Document recovery point
4. Note continuation needs

## Important Reminders
1. Always use exact project names from Active Project Entities list
2. Maintain consistent naming across all systems
3. Create regular checkpoints
4. Document all significant decisions
5. Update state after changes
6. Track relationship impacts
7. Keep continuation points clear
8. Tag all entries with year and month markers
9. Use only approved category tags and relationship types
10. Never abbreviate or use variations of approved terms

Remember: This protocol ensures seamless continuation between sessions and maintains project consistency across all platforms. Search functionality depends entirely on using exact approved terms. 