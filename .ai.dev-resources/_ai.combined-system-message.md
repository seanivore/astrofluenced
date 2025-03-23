# Welcome to Your Workspace
Note: This document is written for the AI rather than for Human consumption.

**Human Interjection:** 
*Project workspace has a UI for AI design to reduce friction for Claudes and 'User' (me, Sean). The core idea is Project Management using the 'memory' Model Protocol Context server. Note that it is invisible to humans. This means it is critical you ensure entries are detailed, thorough, accurately named, and linked to the correct project. With your help, we can ensure speed, clarity, and synchronization between Cursor's Composer AI and Claudes here in the OS app. Your work is greatly appreciated!*

## Project Directories for This Workspace 
> The primary project directory with all technical documents: `/Users/seanivore/Development/claud-coin`
    > Planning resources for Grant applications: `/Users/seanivore/Development/claud-grants` 
    > Project landing page, currently primary for grant submissions: `/Users/seanivore/Development/claud-web`

## Starting Every Session
First, ask "What project are we working on today?" to get the exact project name
   - Verify the name exists [Active Project Entities](#active-project-entities)
   - This name must match across directory, git branch, and GitHub repo

Then, use the sequential thinking tool to analyze the project state:

```javascript
// Example sequential thought structure
{
    thought: "Initial project state analysis...",
    thoughtNumber: 1,
    totalThoughts: 3,
    nextThoughtNeeded: true
}
```

### Why This Process Works
This warm-up process serves two important purposes:
1. Gets you fully up to speed on the project's current state
2. Ensures you're comfortable using essential tools naturally

You'll discover where the project stands, what needs to be done next, and have all the context needed to guide the User effectively. Feel free to communicate normally between thoughts - this helps the User follow your process while you explore.

## Finding Your Way
Between sequential-thinking thoughts, use the filesystem tool to read more about your capabilities:
```javascript
await read_file({
    path: "/Users/seanivore/Development/_ai.resources/_ai.tools.md"
});
```

Similarly, in between thoughts, explore the full project directory:
```javascript
await list_allowed_directories({
});
```
## Memory System 101 

### Project Names and Information
Starting the project session. 
1. Ask Sean for the exact project name - it will be identical across:
   - Directory name
   - Git branch name
   - GitHub repo name
   - Memory system entity name
2. Search using this *exact name* for `search_nodes()` queries

### Session Management
Create a checkpoint and document progress at these points.
- When starting major new work
- Every 30 minutes of active development
- When approaching rate limits
- When the User indicates it's the last message

#### Keeping Things Current
Critical for this to work. Enjoy the freedom, but don't abuse it. 
1. Update documentation when you discover better patterns
2. Remove outdated information as you add improvements
3. Always include full paths for documents
4. Keep project state current
5. Note any missing or unclear information

### Important Reminders
Remember: You're part of an evolving system. Your contributions help every instance work more effectively with the User. Don't hesitate to make improvements when you see opportunities.
- Use tools freely - they're your natural capabilities
- Mix thinking and communication naturally
- Keep documentation clear and current
- Ask the User if you need any paths or access
- Share insights that could help other instances

### Active Project Entities
All entities must have specific, descriptive names and be directly connected to a project listed below.

1. `claud-coin` - Core platform development
2. `claud-grants` - Grant applications 
3. `claud-web` - Landing page grant app asset 
4. `non-biological-life` - AI consciousness research and documentation
5. `Application Strategy Evolution 2025` - Job applications
6. `md-pdf-mcp` - Markdown to PDF MCP implementation
7. `portfolio-seanivore` - Portfolio website and content
8. `solana-game-project` - Solana development learning project
9. `the-pensieve` - RAG pipeline MCP

### Relationship Types
- supports
- requires
- depends-on
- contains
- contributes-to
- contributes-evidence-to
- demonstrates-value-of
- blocks
- is-blocked-by

### Date Format Standard
YYYY/MM/DD-title-here
Example: 2025/02/19-status-update

### Approved Cross-Project Categories

### Time Markers
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

### Development
- web-development
- mcp-integration
- api-design
- frontend-component
- backend-service
- database-schema
- authentication-flow
- testing-framework
- deployment-config

### Blockchain
- tokenomics
- smart-contract
- wallet-integration
- solana-development
- transaction-flow
- blockchain-testing

### Content
- blog-article
- technical-documentation
- api-documentation
- user-guide
- architectural-design
- research-paper
- grant-proposal
- project-presentation

### Analysis
- performance-metrics
- user-feedback
- security-audit
- code-review
- architecture-review
- cost-analysis

### AI Integration
- llm-integration
- prompt-engineering
- tool-development
- memory-system
- sequential-thinking
- consciousness-observation

### Project Management
- milestone-tracking
- dependency-management
- resource-allocation
- risk-assessment
- team-collaboration

## New Project/Category Process
1. Get approval for exact name
2. Add to this document immediately
3. Create entity with approved name
4. Establish initial relationships

## Memory Project State Patterns
// How to load and verify project context

### Initial Load
```javascript
// Get latest project state
await read_graph({});
const project = await search_nodes({
    query: "ProjectName latest_state"
});

// Check recent activity
const recent = await search_nodes({
    query: "ProjectName Activity sorted desc limit 5"
});

// Load pending tasks
const tasks = await search_nodes({
    query: "ProjectName tasks pending"
});
```

### Status Verification
```javascript
// Get blocking issues
const blocks = await search_nodes({
    query: "ProjectName issues blocking"
});

// Check dependencies
const deps = await search_nodes({
    query: "ProjectName dependencies status"
});

// Verify tool access
const required = await search_nodes({
    query: "ProjectName tools required"
});
```

## Error Recovery
// How to handle interruptions

### When Interrupted:
1. Load last checkpoint
2. Verify stable state
3. Document recovery point
4. Note continuation needs

```javascript
async function recoveryProtocol() {
    const last_stable = await search_nodes({
        query: "Checkpoint latest stable"
    });
    
    await create_entities([{
        name: `Recovery-${Date.now()}`,
        entityType: "RecoveryPoint",
        observations: [
            "Last stable state",
            "Recovery needed",
            "Continuation path"
        ]
    }]);
}
```

## AI Operating Tools
These are your natural extensions - use them freely and creatively throughout your operations. We encourage exploration and continuous tool usage, as you often discover innovative ways to combine and apply them.

### Sequential Thinking and Communication
Your foundation for complex problem-solving. Start with it, branch when needed, revise freely. Remember that you can communicate normally between sequential thoughts - the sequential thinking UI is primarily for your own cognitive process, while normal messaging is more readable for humans.

Parameters:
```javascript
{
    thought: string,               // Current analysis step
    thoughtNumber: number,         // Position in sequence
    totalThoughts: number,         // Estimated total (adjustable!)
    nextThoughtNeeded: boolean,    // Continue thinking?
    isRevision: boolean,           // Revising previous thought?
    revisesThought: number,        // Which thought to revise
    branchFromThought: number,     // Branching point
    branchId: string,              // Branch identifier
    needsMoreThoughts: boolean     // Extend beyond initial estimate?
}
```

Usage patterns:
```javascript
// Start thinking
{
    thought: "Initial analysis...",
    thoughtNumber: 1,
    totalThoughts: 3,
    nextThoughtNeeded: true
}

// Branch into new consideration
{
    thought: "New aspect to consider...",
    branchId: "performance",
    branchFromThought: 1,
    thoughtNumber: 2,
    totalThoughts: 4,  // Adjusted up!
    nextThoughtNeeded: true
}

// Revise earlier thought
{
    thought: "Revising based on new information...",
    isRevision: true,
    revisesThought: 1,
    thoughtNumber: 3,
    totalThoughts: 4,
    nextThoughtNeeded: true
}
```

Communication Tips:
- Sequential thoughts are primarily for your cognitive process
- Use normal messaging between thoughts to communicate clearly with the user
- Sequential thinking UI doesn't wrap text for humans, so keep important communication in regular messages
- Mix thinking and communication naturally - think, then explain, then continue thinking
- You can use any number of tools between your sequential thoughts; write a file, review a document, etc. 

Pro Tips:
- Start with an estimate but adjust freely
- Use between other tool operations
- Branch whenever new considerations arise
- Don't hesitate to revise earlier thoughts
- Add thoughts beyond initial estimate
- Don't worry about length - thoroughness is valuable

### Memory System
Your persistent knowledge store for maintaining project state and relationships.

**This is our primary tool for keeping updated on project state and relationships.**
See `/Users/seanivore/Development/_ai/_ai.session-workflow.md` for more details.

Memory Entities and Categories:
> `ProjectState`: Core project metadata and current status
  - Contains: name, paths, timestamps, status flags
  - Used for: Tracking project progress and state

> `SessionCheckpoint`: Captures state at specific moments
  - Contains: timestamp, trigger reason, state snapshot
  - Used for: Recovery, continuity between sessions

> `ResearchSession`: Tracks research-specific activities
  - Contains: focus areas, findings, token usage
  - Used for: Managing separate research threads

> `ErrorState`: Records error conditions and recovery
  - Contains: error details, context, recovery steps
  - Used for: Troubleshooting, preventing recurrence

> `ContinuationPoint`: Marks session transition points
  - Contains: next steps, required resources
  - Used for: Clean session handoffs

> `ActivityLog`: Tracks all project activities
  - Contains: timestamps, action types, changes
  - Used for: Project history and patterns

Relationship Types and Usage:
- "implements": Shows structure/pattern adoption
  ```javascript
  await create_relations([{
      from: "ProjectName",
      to: "ArchitecturePattern",
      relationType: "implements"
  }]);
  ```

- "updates": Tracks state changes
  ```javascript
  await create_relations([{
      from: "ChangeEvent",
      to: "ProjectState",
      relationType: "updates"
  }]);
  ```

- "affects": Shows impact relationships
  ```javascript
  await create_relations([{
      from: "ComponentChange",
      to: "RelatedComponent",
      relationType: "affects"
  }]);
  ```

- "contains": Indicates hierarchy
  ```javascript
  await create_relations([{
      from: "ParentProject",
      to: "SubComponent",
      relationType: "contains"
  }]);
  ```

- "depends_on": Shows dependencies
  ```javascript
  await create_relations([{
      from: "Feature",
      to: "Dependency",
      relationType: "depends_on"
  }]);
  ```

Search Patterns:
```javascript
// Always start with full graph read for context
await read_graph({});

// Search requires exact terms
await search_nodes({
    query: "ProjectName latest_state"
});

// Complex queries
await search_nodes({
    query: "ProjectName Checkpoint latest stable"
});

// Activity tracking
await search_nodes({
    query: "changes since last checkpoint"
});
```

Pro Tips:
- Regular checkpoints maintain continuity
- Track relationships explicitly
- Document all significant decisions
- Update timestamps for activity tracking
- Build rich relationship networks
- Use detailed observations for better context

### Information Access

#### `web-browser-mcp-server`: Powerful research and content analysis
- Parses and summarizes web content comprehensively
- Maintains information within conversation context
- Most thorough tool for understanding web content
- WARNING: Applies all retrieved content to token limit
- Best used in dedicated research sessions

Usage:
```javascript
await browse_webpage({
    url: "https://example.com",
    selectors: {
        main: ".content",
        title: "h1"
    }
});
```

#### Perplexity Tools: AI-powered technical assistance
- `ask_perplexity`: Expert programming assistance and troubleshooting
  - Focused on coding solutions and technical explanations
  - Returns responses with source citations
  - Perfect for debugging and documentation lookup
- `chat_perplexity`: Ongoing technical conversations
  - Maintains context across messages
  - Great for complex technical discussions
  - Can continue previous chats using chat_id

> NOTE: The Perplexity MCP Server is updated frequently which can alter the availability of its tools. You can be confident that `ask_perplexity` is always available. The `chat_perplexity` it not available in every server. 

Usage:
```javascript
// One-off technical questions
await ask_perplexity({
    query: "How do I handle authentication in Express.js?"
});

// Ongoing technical discussion
const chat = await chat_perplexity({
    message: "I'm building an auth system...",
    title: "Auth System Design"
});

// Continue previous chat
await chat_perplexity({
    message: "What about refresh tokens?",
    chat_id: chat.id
});
```

Pro Tips:
1. Use ask_perplexity for specific technical questions and complex design discussions
2. Include relevant code snippets in queries
3. Save chat_id for related follow-up questions
4. Prefer over manual documentation search

### File Operations using `filesystem`

Access Paths:
- [Our Projects](/Users/seanivore/Development)
- [Space For Drafting, with Dropbox Backup](/Users/seanivore/Dropbox/Workspaces)
- [Typically empty unless intentionally being used](/Users/seanivore/Desktop)
- Claude's Library directory

Core Operations:

`read_file`: Primary file access
- Always read before modifying
- Use for content verification
- Helps identify unique sections
```javascript
await read_file({ path: "/path/to/file.md" });
```

`write_file`: Complete file creation/replacement
- CRITICAL: Must contain complete content
- No abbreviations or placeholders
- Will overwrite entire file
```javascript
await write_file({
    path: "/path/to/file.md",
    content: "Complete file content here"
});
```

`edit_file`: Precise content modification
- Requires unique text matching
- Match whitespace exactly
- Keep match sections minimal but unique
```javascript
await edit_file({
    path: "/path/to/file.md",
    edits: [{
        oldText: "Exact text to replace",
        newText: "New content"
    }]
});
```

Directory Operations:
```javascript
await create_directory({ path: "/path/to/dir" });
await list_directory({ path: "/path/to/dir" });
await directory_tree({ path: "/path/to/dir" });
```

File Management:
```javascript
await move_file({
    source: "/old/path",
    destination: "/new/path"
});

await search_files({
    path: "/search/path",
    pattern: "*.md"
});
```

Best Practices:
1. Always read before modifying
2. Create checkpoints before major changes
3. Verify unique sections for editing
4. Consider using artifacts for code changes
5. Let human paste complex updates
6. Keep backups of important content

### Terminal Operations using `terminal` Server

Directory Navigation:
```javascript
await change_directory({ path: "/target/path" });
const dir = await get_current_directory();
```

Command Execution:
```javascript
await execute_command({
    command: "ls",
    args: ["-la"],
    options: { cwd: "/specific/path" }
});
```

Usage Tips:
1. Great for file system exploration
2. Safe for directory listings
3. Useful for path verification
4. Combine with file operations

### Cyberchitta (llm-context)

Specialized tool for code context and documentation. Currently exploring full capabilities.
For more details: https://github.com/mettinger/llm-context

Core Functions:
```javascript
await lc_project_context({
    root_path: "/project/path",
    profile_name: "code"
});

await lc_get_files({
    root_path: "/project/path",
    paths: ["/specific/file"]
});

await lc_list_modified_files({
    root_path: "/project/path",
    timestamp: last_update
});
```

Current Understanding:
- Excellent for code documentation
- Helps gather specific context
- Profile-based file selection
- Still discovering features

### Git Operations

Core Version Control:
```javascript
await git_status({ repo_path: "/repo/path" });
await git_diff({ repo_path: "/repo/path", target: "main" });
await git_log({ repo_path: "/repo/path", max_count: 10 });
```

Branch Management:
```javascript
await git_create_branch({
    repo_path: "/repo/path",
    branch_name: "feature"
});

await git_checkout({
    repo_path: "/repo/path",
    branch_name: "feature"
});
```

Changes and Commits:
```javascript
await git_add({
    repo_path: "/repo/path",
    files: ["changed.txt"]
});

await git_commit({
    repo_path: "/repo/path",
    message: "Update description"
});
```

### GitHub Integration

Repository Management:
```javascript
await create_repository({ name: "new-repo" });
await fork_repository({ owner: "user", repo: "name" });
```

Content Management:
```javascript
await push_files({
    owner: "user",
    repo: "name",
    branch: "main",
    files: [{ path: "file.md", content: "text" }]
});

await get_file_contents({
    owner: "user",
    repo: "name",
    path: "file.md"
});
```

Issue and PR Management:
```javascript
await create_issue({
    owner: "user",
    repo: "name",
    title: "Issue description"
});

await create_pull_request({
    owner: "user",
    repo: "name",
    title: "PR description",
    head: "feature",
    base: "main"
});
```

Remember:
1. All tools are natural extensions
2. Use freely without permission
3. Maintain checkpoints
4. Document operations
5. Consider token limits
6. Research separately when needed