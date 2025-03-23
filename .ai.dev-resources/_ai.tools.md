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
- ProjectState: Core project metadata and current status
  - Contains: name, paths, timestamps, status flags
  - Used for: Tracking project progress and state

- SessionCheckpoint: Captures state at specific moments
  - Contains: timestamp, trigger reason, state snapshot
  - Used for: Recovery, continuity between sessions

- ResearchSession: Tracks research-specific activities
  - Contains: focus areas, findings, token usage
  - Used for: Managing separate research threads

- ErrorState: Records error conditions and recovery
  - Contains: error details, context, recovery steps
  - Used for: Troubleshooting, preventing recurrence

- ContinuationPoint: Marks session transition points
  - Contains: next steps, required resources
  - Used for: Clean session handoffs

- ActivityLog: Tracks all project activities
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
- /Users/seanivore/Development
- /Users/seanivore/Dropbox/Workspaces
- /Users/seanivore/Desktop
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