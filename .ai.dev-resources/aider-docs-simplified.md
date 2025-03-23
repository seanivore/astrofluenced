Aider Core Reference Guide

Key Capabilities & Best Practices
Aider is an AI pair programming tool designed to work incrementally and intelligently with your codebase:

1. Incremental Changes
- Work in small, focused steps rather than large rewrites
- Each change should be a single logical unit (e.g., "add input validation" or "refactor this function")
- Complex changes should be broken down into smaller tasks
- Use architect mode for planning larger changes

2. Contextual Understanding
- Maintains a map of your entire repository for context
- Automatically understands dependencies and relationships
- Can see related code even if files aren't directly added
- Uses this context to make informed changes

3. Smart File Management
- Only add files that need editing to reduce noise
- Repository map provides broader context automatically
- Can work with multiple files for coordinated changes
- Supports read-only files for reference documentation

4. Flexible Integration Methods
- Traditional chat interface for direct interaction
- Watch mode for adding AI comments in your editor
- Git integration for tracking and managing changes
- Automatic linting and testing of changes

5. Working with Models
- Different models have different strengths
- Architect mode splits planning and implementation
- Stronger models (GPT-4o, Claude) handle complex edits better
- Weaker models work best with smaller, focused changes

6. Safety Features
- All changes are git-tracked
- Easy to undo changes with /undo
- Review changes before they're applied
- Automatic linting and testing

Chat Modes
Aider has four different chat modes:
- code - Makes direct changes to your code based on requests
- architect - First proposes a solution, then asks if you want to implement the changes
- ask - Answers questions about your code without making edits
- help - Answers questions about using aider and its features

Architect Mode
When using architect mode, aider uses two models:
1. Main model: Reviews your request and proposes a solution
2. Editor model: Implements the approved changes using specific code editing instructions

Architect mode often produces better results than code mode but uses two LLM requests, making it slower but more reliable. It's especially useful with:
- OpenAI's o1 models (strong reasoning, weaker editing)
- Complex changes that benefit from planning
- When you want to review proposed changes before implementation

Core Features
1. File Management
- Add only files that need editing to the chat
- Aider automatically includes context from related files
- Use /drop to remove unneeded files
- Use /clear to clear chat history

2. Git Integration
- Automatic commits of changes with descriptive messages
- Easy undo of AI changes with /undo
- Repository map provides context from entire codebase
- Tracks edit history and attribution

3. Testing & Linting
- Automatic linting after changes
- Test command integration
- Error fixing based on test output
- Support for compiled languages

Essential Commands
Chat & Editing:
/add <file> - Add files to edit
/architect - Enter architect mode
/ask - Ask questions without editing
/chat-mode <mode> - Switch chat modes
/clear - Clear chat history
/code - Request code changes
/copy - Copy last assistant message to clipboard
/copy-context - Copy chat context as markdown
/diff - Show recent changes
/drop - Remove files from chat
/editor - Open editor to write prompt
/help - Get help
/lint - Lint and fix files
/ls - List files and show which are in chat
/map - Show repository map
/map-refresh - Force refresh of repository map
/model - Switch models
/models - Search available models
/multiline-mode - Toggle multiline input mode
/paste - Paste image/text from clipboard
/read - Add read-only files
/read-only - Add files as read-only or convert existing
/reset - Drop all files and clear history
/run - Execute shell commands (alias: !)
/save - Save commands to reconstruct session
/settings - Show current settings
/test - Run tests and show output
/tokens - Show token usage
/undo - Undo last git commit
/voice - Record and transcribe voice input
/web - Add webpage content to chat

Key Command-Line Flags

Model Selection & Configuration:
--model MODEL - Specify model to use
--opus - Use Claude 3 Opus
--sonnet - Use Claude 3.5 Sonnet
--haiku - Use Claude 3.5 Haiku
--4 - Use GPT-4
--4o - Use GPT-4o
--mini - Use GPT-4o Mini
--4-turbo - Use GPT-4 Turbo
--35turbo - Use GPT-3.5 Turbo
--deepseek - Use DeepSeek Coder
--o1-mini - Use O1 Mini
--o1-preview - Use O1 Preview

Mode & Behavior:
--architect - Use architect mode
--edit-format FORMAT - Specify edit format
--editor-model MODEL - Specify model for edits
--editor-edit-format FORMAT - Specify edit format for editor
--map-tokens VALUE - Control repo map size
--cache-prompts - Enable prompt caching
--cache-keepalive-pings N - Keep cache warm
--max-chat-history-tokens N - Limit chat history

Git & Code Management:
--auto-commits - Toggle auto-committing changes
--dirty-commits - Allow commits when repo is dirty
--attribute-author - Git author attribution
--attribute-committer - Git committer attribution
--commit - Commit changes and exit
--commit-prompt TEXT - Custom commit message prompt
--lint - Enable linting
--lint-cmd CMD - Custom lint command
--test-cmd CMD - Specify test command
--auto-test - Run tests after changes
--watch-files - Watch for AI comments

Input/Output Settings:
--dark-mode/--light-mode - Set color theme
--pretty - Enable pretty output
--stream - Enable streaming responses
--show-diffs - Show diffs when committing
--user-input-color COLOR - Set input color
--assistant-output-color COLOR - Set output color
--code-theme THEME - Set code highlighting theme
--multiline - Enable multiline input mode
--detect-urls - Auto-detect URLs to add
--chat-language LANG - Set chat language

File & Context Management:
--file FILE - Specify files to edit
--read FILE - Specify read-only files
--encoding ENC - Set file encoding
--map-refresh MODE - Control map updates
--restore-chat-history - Load previous chat

Voice Settings:
--voice-format FORMAT - Set voice recording format
--voice-language LANG - Set voice recognition language
--voice-input-device DEV - Specify input device

Common Workflows

1. Basic Code Editing
- Add files with /add or specify them on command line
- Make requests in natural language
- Review changes in diffs
- Changes are automatically committed

2. Complex Changes with Architect Mode
- Switch to architect mode with /architect
- Discuss the approach first
- Review proposed changes
- Approve implementation
- Test and refine as needed

3. Using AI Comments in Files
Run aider with --watch-files to enable:
# Make a change AI!
# What does this do? AI?

4. Working with Multiple Files
- Add only necessary files
- Use /drop to remove files when done
- Use /read for reference-only files
- Let repository map provide context

5. Testing & Debugging
- Use /run to execute commands
- Use /test to run test suite
- Share error messages in chat
- Let aider propose fixes

Best Practices
1. File Management
- Only add files that need editing
- Use /drop to manage context size
- Use /clear to reset when stuck
- Let repo map provide broader context

2. Making Changes
- Break complex changes into steps
- Use architect mode for planning
- Review diffs before continuing
- Test changes incrementally

3. Context Management
- Monitor token usage with /tokens
- Clear chat history when switching tasks
- Use read-only files for documentation
- Keep chat focused on current task 