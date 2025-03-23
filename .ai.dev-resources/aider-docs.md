Aider is AI pair programming in your terminal
Aider lets you pair program with LLMs, to edit code in your local git repository. Start a new project or work with an existing code base. Aider works best with Claude 3.5 Sonnet, DeepSeek V3, o1 & GPT-4o and can connect to almost any LLM [https://aider.chat/docs/llms.html]. 

Getting started
If you already have python 3.8-3.13 installed, you can get started quickly like this:

python -m pip install aider-install
aider-install

# Change directory into your code base
cd /to/your/project

# Work with Claude 3.5 Sonnet on your code
aider --model sonnet --anthropic-api-key your-key-goes-here

# Work with GPT-4o on your code
aider --model gpt-4o --openai-api-key your-key-goes-here

See the installation instructions [https://aider.chat/docs/install.html] and usage documentation [https://aider.chat/docs/usage.html] for more details.

Features
- Run aider with the files you want to edit: aider <file1> <file2> ...
- Ask for changes:
	- Add new features or test cases.
	- Describe a bug.
	- Paste in an error message or or GitHub issue URL.
	- Refactor code.
	- Update docs.
- Aider will edit your files to complete your request.
- Aider automatically git commits [https://aider.chat/docs/git.html] changes with a sensible commit message.
- Aider works with most popular languages [https://aider.chat/docs/languages.html]: python, javascript, typescript, php, html, css, and more…
- Aider works best with Claude 3.5 Sonnet, DeepSeek V3, o1 & GPT-4o and can connect to almost any LLM [https://aider.chat/docs/llms.html]. 
- Aider can edit multiple files at once for complex requests.
- Aider uses a map of your entire git repo [https://aider.chat/docs/repomap.html], which helps it work well in larger codebases.
- Edit files in your editor while chatting with aider, and it will always use the latest version. Pair program with AI.
- Add images to the chat (GPT-4o, Claude 3.5 Sonnet, etc) [https://aider.chat/docs/usage/images-urls.html]. 
- Add URLs [https://aider.chat/docs/usage/images-urls.html] to the chat and aider will read their content.
- Code with your voice [https://aider.chat/docs/usage/voice.html].

Top tier performance
Aider has one of the top scores on SWE Bench [https://aider.chat/2024/06/02/main-swe-bench.html]. SWE Bench is a challenging software engineering benchmark where aider solved real GitHub issues from popular open source projects like django, scikitlearn, matplotlib, etc.

More info
- Documentation [https://aider.chat/]
- Installation [https://aider.chat/docs/install.html]
- Usage [https://aider.chat/docs/usage.html]
- Tutorial videos [https://aider.chat/docs/usage/tutorials.html]
- Connecting to LLMs [https://aider.chat/docs/llms.html] 
- Configuration [https://aider.chat/docs/config.html]
- Troubleshooting [https://aider.chat/docs/troubleshooting.html] 
- LLM Leaderboards [https://aider.chat/docs/leaderboards/] 
- GitHub [https://github.com/Aider-AI/aider]
- Discord [https://discord.gg/Tv2uQnR88V] 
- Blog [https://aider.chat/blog/]

Installation
Get started quickly with aider-install
If you already have python 3.8-3.13 installed, you can get started quickly like this:

python -m pip install aider-install
aider-install

# Change directory into your code base
cd /to/your/project

# Work with Claude 3.5 Sonnet on your code
aider --model sonnet --anthropic-api-key your-key-goes-here

# Work with GPT-4o on your code
aider --model gpt-4o --openai-api-key your-key-goes-here

This will install aider in its own separate python environment. If needed, aider-install will also install a separate version of python 3.12 to use with aider.

Once aider is installed, there are also some optional install steps [https://aider.chat/docs/install/optional.html]. 

See the usage instructions [https://aider.chat/docs/usage.html] to start coding with aider.

One-liners
These one-liners will install aider, along with python 3.12 if needed. They are based on the uv installers [https://docs.astral.sh/uv/getting-started/installation/]. 

Mac & Linux
Use curl to download the script and execute it with sh:

curl -LsSf https://aider.chat/install.sh | sh

Install with uv
You can install aider with uv:

python -m pip install pipx  # If you need to install pipx
pipx install aider-chat

You can use pipx to install aider with python versions 3.9-3.12.

Also see the docs on other methods for installing pipx itself [https://pipx.pypa.io/stable/installation/]. 

Other install methods
You can install aider with the methods described below, but one of the above methods is usually safer.

Install with pip
If you install with pip, you should consider using a virtual environment [https://docs.python.org/3/library/venv.html] to keep aider's dependencies separated.

You can use pip to install aider with python versions 3.9-3.12.

# Install aider
python -m pip install -U --upgrade-strategy only-if-needed aider-chat

# To work with GPT-4o:
aider --4o --openai-api-key sk-xxx...

# To work with Claude 3.5 Sonnet:
aider --sonnet --anthropic-api-key sk-xxx...

TIP

In some environments you may get "aider command not found" errors. You can try python -m aider or see here for more info [https://aider.chat/docs/troubleshooting/aider-not-found.html]. 

Installing with package managers
It's best to install aider using one of methods recommended above. While aider is available in a number of system package managers, they often install aider with incorrect dependencies.

Next steps…
There are some optional install steps [https://aider.chat/docs/install/optional.html] you could consider. See the usage instructions [https://aider.chat/docs/usage.html] to start coding with aider.

Optional steps
The steps below are completely optional.

Install git
Aider works best if you have git installed. Here are instructions for installing git in various environments [https://github.com/git-guides/install-git]. 

Get your API key
To work with OpenAI's models like GPT-4o or o1-preview you need a paid OpenAI API key [https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key]. Note that this is different than being a "ChatGPT Plus" subscriber.

To work with Anthropic's models like Claude 3.5 Sonnet you need a paid Anthropic API key [https://docs.anthropic.com/claude/reference/getting-started-with-the-api].

Working with other LLMs
Aider works best with Claude 3.5 Sonnet, DeepSeek V3, o1 & GPT-4o and can connect to almost any LLM [https://aider.chat/docs/llms.html]. 

Store your api keys
You can store your api keys in configuration or env [https://aider.chat/docs/config/api-keys.html] files and they will be loaded automatically whenever you run aider.

Enable Playwright
Aider supports adding web pages to the chat with the /web <url> command. When you add a url to the chat, aider fetches the page and scrapes its content.

By default, aider uses the httpx library to scrape web pages, but this only works on a subset of web pages. Some sites explicitly block requests from tools like httpx. Others rely heavily on javascript to render the page content, which isn't possible using only httpx.

Aider works best with all web pages if you install Playwright's chromium browser and its dependencies:

playwright install --with-deps chromium

See the Playwright for Python [https://playwright.dev/python/docs/browsers#install-system-dependencies] documentation for additional information.

Enable voice coding
Aider supports coding with your voice [https://aider.chat/docs/usage/voice.html] using the in-chat /voice command. Aider uses the PortAudio [http://www.portaudio.com/] library to capture audio. Installing PortAudio is completely optional, but can usually be accomplished like this:

For Windows, there is no need to install PortAudio.
For Mac, do brew install portaudio
For Linux, do sudo apt-get install libportaudio2
Some linux environments may also need sudo apt install libasound2-plugins

NeoVim
joshuavial [https://github.com/joshuavial] provided a NeoVim plugin for aider:

https://github.com/joshuavial/aider.nvim

VS Code
You can run aider inside a VS Code terminal window. There are a number of 3rd party aider plugins for VSCode [https://marketplace.visualstudio.com/search?term=aider%20-kodu&target=VSCode&category=All%20categories&sortBy=Relevance].

Other editors
If you are interested in creating an aider plugin for your favorite editor, please let us know by opening a GitHub issue [https://github.com/Aider-AI/aider/issues]. 

Install the development version of aider
If you want the very latest development version of aider you can install it like this:

aider --install-main-branch

Aider with docker
Aider is available as 2 docker images:

paulgauthier/aider installs the aider core, a smaller image that's good to get started quickly.
paulgauthier/aider-full installs aider will all the optional extras.
The full image has support for features like interactive help, the browser GUI and support for using Playwright to scrape web pages. The core image can still use these features, but they will need to be installed the first time you access them. Since containers are ephemeral, the extras will need to be reinstalled the next time you launch the aider core container.

Aider core
docker pull paulgauthier/aider
docker run -it --user $(id -u):$(id -g) --volume $(pwd):/app paulgauthier/aider --openai-api-key $OPENAI_API_KEY [...other aider args...]

Full version
docker pull paulgauthier/aider-full
docker run -it --user $(id -u):$(id -g) --volume $(pwd):/app paulgauthier/aider-full --openai-api-key $OPENAI_API_KEY [...other aider args...]

How to use it
You should run the above commands from the root of your git repo, since the --volume arg maps your current directory into the docker container. Given that, you need to be in the root of your git repo for aider to be able to see the repo and all its files.

You should be sure your that git repo config contains your user name and email, since the docker container won't have your global git config. Run these commands while in your git repo, before you do the docker run command:

git config user.email "you@example.com"
git config user.name "Your Name"

Limitations
When you use the in-chat /run command, it will be running shell commands inside the docker container. So those commands won't be running in your local environment, which may make it tricky to /run tests, etc for your project.
The /voice command won't work unless you can figure out how to give the docker container access to your host audio device. The container has libportaudio2 installed, so it should work if you can do that.

GitHub Codespaces
You can use aider in GitHub Codespaces via the built-in Terminal pane. See below for an example, but you can just follow the main install instructions inside your codespace terminal.

Replit
To use aider with pipx on replit, you can run these commands in the replit shell:

pip install pipx
pipx run aider-chat ...normal aider args...

If you install aider with pipx on replit and try and run it as just aider it will crash with a missing libstdc++.so.6 library.

Usage
Run aider with the source code files you want to edit. These files will be "added to the chat session", so that aider can see their contents and edit them for you. They can be existing files or the name of files you want aider to create for you.

aider <file1> <file2> ...

At the aider > prompt, ask for code changes and aider will edit those files to accomplish your request.

$ aider factorial.py

Aider v0.37.1-dev
Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo
Git repo: .git with 258 files
Repo-map: using 1024 tokens
Use /help to see in-chat commands, run with --help to see cmd line args
───────────────────────────────────────────────────────────────────────
> Make a program that asks for a number and prints its factorial

...

TIP 
Use /help <question> to ask for help about using aider [https://aider.chat/docs/troubleshooting/support.html], customizing settings, troubleshooting, using LLMs, etc.

Adding files
To edit files, you need to "add them to the chat". Do this by naming them on the aider command line. Or, you can use the in-chat /add command to add files.

Only add the files that need to be edited for your task. Don't add a bunch of extra files. If you add too many files, the LLM can get overwhelmed and confused (and it costs more tokens). Aider will automatically pull in content from related files so that it can understand the rest of your code base [https://aider.chat/docs/repomap.html].

You can use aider without adding any files, and it will try to figure out which files need to be edited based on your requests.

TIP
You'll get the best results if you think about which files need to be edited. Add just those files to the chat. Aider will include relevant context from the rest of your repo.

LLMs
Aider works best with Claude 3.5 Sonnet, DeepSeek V3, o1 & GPT-4o and can connect to almost any LLM [https://aider.chat/docs/llms.html]. 

# GPT-4o
$ aider --4o

# Claude 3.5 Sonnet
$ aider --sonnet

Or you can run aider --model XXX to launch aider with another model. During your chat you can switch models with the in-chat /model command.

Making changes
Ask aider to make changes to your code. It will show you some diffs of the changes it is making to complete you request. Aider will git commit all of its changes [https://aider.chat/docs/git.html], so they are easy to track and undo.

You can always use the /undo command to undo AI changes that you don't like.

Tips
Just add the files that need to be changed to the chat
Take a moment and think about which files will need to be changed. Aider can often figure out which files to edit all by itself, but the most efficient approach is for you to add the files to the chat.

Don't add lots of files to the chat
Just add the files you think need to be edited. Too much irrelevant code will distract and confuse the LLM. Aider uses a map of your entire git repo so is usually aware of relevant classes/functions/methods elsewhere in your code base. It's ok to add 1-2 highly relevant files that don't need to be edited, but be selective. https://aider.chat/docs/repomap.html

Break your goal down into bite sized steps
Do them one at a time. Adjust the files added to the chat as you go: /drop files that don't need any more changes, /add files that need changes for the next step.

For complex changes, discuss a plan first
Use the /ask command to make a plan with aider. Once you are happy with the approach, just say "go ahead" without the /ask prefix. https://aider.chat/docs/usage/modes.html

If aider gets stuck
Use /clear to discard the chat history and make a fresh start.
Can you /drop any extra files?
Use /ask to discuss a plan before aider starts editing code.
Use the /model command to switch to a different model and try again. Switching between GPT-4o and Sonnet will often get past problems. https://aider.chat/docs/usage/commands.html
If aider is hopelessly stuck, just code the next step yourself and try having aider code some more after that. Take turns and pair program with aider.
Creating new files
If you want aider to create a new file, add it to the repository first with /add <file>. This way aider knows this file exists and will write to it. Otherwise, aider might write the changes to an existing file. This can happen even if you ask for a new file, as LLMs tend to focus a lot on the existing information in their contexts.

Fixing bugs and errors
If your code is throwing an error, use the /run command to share the error output with the aider. Or just paste the errors into the chat. Let the aider figure out how to fix the bug. https://aider.chat/docs/usage/commands.html

If test are failing, use the /test command to run tests and share the error output with the aider. https://aider.chat/docs/usage/lint-test.html

Providing docs
LLMs know about a lot of standard tools and libraries, but may get some of the fine details wrong about API versions and function arguments.

You can provide up-to-date documentation in a few ways:

Paste doc snippets into the chat.
Include a URL to docs in your chat message and aider will scrape and read it. For example: Add a submit button like this https://ui.shadcn.com/docs/components/button.
Use the /read command to read doc files into the chat from anywhere on your filesystem. https://aider.chat/docs/usage/commands.html
If you have coding conventions or standing instructions you want aider to follow, consider using a conventions file. https://aider.chat/docs/usage/conventions.html
Interrupting & inputting
Use Control-C to interrupt aider if it isn't providing a useful response. The partial response remains in the conversation, so you can refer to it when you reply with more information or direction.

You can send long, multi-line messages in the chat in a few ways:

Paste a multi-line message directly into the chat.
Enter { alone on the first line to start a multiline message and } alone on the last line to end it.
Or, start with {tag (where "tag" is any sequence of letters/numbers) and end with tag}. This is useful when you need to include closing braces } in your message.
Use Meta-ENTER to start a new line without sending the message (Esc+ENTER in some environments).
Use /paste to paste text from the clipboard into the chat. https://aider.chat/docs/config/editor.html
Use the /editor command to open your editor to create the next chat message. See editor configuration docs for more info.
Use multiline-mode, which swaps the function of Meta-Enter and Enter, so that Enter inserts a newline, and Meta-Enter submits your command. To enable multiline mode:
Use the /multiline-mode command to toggle it during a session.
Use the --multiline switch.
Example with a tag:

{python
def hello():
    print("Hello}")  # Note: contains a brace
python}

People often ask for SHIFT-ENTER to be a soft-newline. Unfortunately there is no portable way to detect that keystroke in terminals.

In-chat commands

Slash commands
Aider supports commands from within the chat, which all start with /.

Command	Description
/add	Add files to the chat so aider can edit them or review them in detail
/architect	Enter architect mode to discuss high-level design and architecture
/ask	Ask questions about the code base without editing any files
/chat-mode	Switch to a new chat mode
/clear	Clear the chat history
/code	Ask for changes to your code
/commit	Commit edits to the repo made outside the chat (commit message optional)
/copy	Copy the last assistant message to the clipboard
/copy-context	Copy the current chat context as markdown, suitable to paste into a web UI
/diff	Display the diff of changes since the last message
/drop	Remove files from the chat session to free up context space
/editor	Open an editor to write a prompt
/exit	Exit the application
/git	Run a git command (output excluded from chat)
/help	Ask questions about aider
/lint	Lint and fix in-chat files or all dirty files if none in chat
/load	Load and execute commands from a file
/ls	List all known files and indicate which are included in the chat session
/map	Print out the current repository map
/map-refresh	Force a refresh of the repository map
/model	Switch to a new LLM
/models	Search the list of available models
/multiline-mode	Toggle multiline mode (swaps behavior of Enter and Meta+Enter)
/paste	Paste image/text from the clipboard into the chat. Optionally provide a name for the image.
/quit	Exit the application
/read-only	Add files to the chat that are for reference only, or turn added files to read-only
/report	Report a problem by opening a GitHub Issue
/reset	Drop all files and clear the chat history
/run	Run a shell command and optionally add the output to the chat (alias: !)
/save	Save commands to a file that can reconstruct the current chat session's files
/settings	Print out the current settings
/test	Run a shell command and add the output to the chat on non-zero exit code
/tokens	Report on the number of tokens used by the current chat context
/undo	Undo the last git commit if it was done by aider
/voice	Record and transcribe voice input
/web	Scrape a webpage, convert to markdown and send in a message

TIP 
You can easily re-send commands or messages. Use the up arrow ⬆ to scroll back or CONTROL-R to search your message history.

Entering multi-line chat messages
You can send long, multi-line messages in the chat in a few ways:

- Paste a multi-line message directly into the chat.
- Enter { alone on the first line to start a multiline message and } alone on the last line to end it.
	- Or, start with {tag (where "tag" is any sequence of letters/numbers) and end with tag}. This is useful when you need to include closing braces } in your message.
	- Use Meta-ENTER to start a new line without sending the message (Esc+ENTER in some environments).
- Use /paste to paste text from the clipboard into the chat.
- Use the /editor command to open your editor to create the next chat message. See editor configuration docs for more info. https://aider.chat/docs/config/editor.html
- Use multiline-mode, which swaps the function of Meta-Enter and Enter, so that Enter inserts a newline, and Meta-Enter submits your command. To enable multiline mode:
	- Use the /multiline-mode command to toggle it during a session.
	- Use the --multiline switch.

Example with a tag:

{python
def hello():
    print("Hello}")  # Note: contains a brace
python}

NOTE 
People often ask for SHIFT-ENTER to be a soft-newline. Unfortunately there is no portable way to detect that keystroke in terminals.

Interrupting with CONTROL-C
It's always safe to use Control-C to interrupt aider if it isn't providing a useful response. The partial response remains in the conversation, so you can refer to it when you reply to the LLM with more information or direction.

Keybindings
The interactive prompt is built with prompt-toolkit which provides emacs and vi keybindings. https://github.com/prompt-toolkit/python-prompt-toolkit

Emacs
Up Arrow : Move up one line in the current message.
Down Arrow : Move down one line in the current message.
Ctrl-Up : Scroll back through previously sent messages.
Ctrl-Down : Scroll forward through previously sent messages.
Ctrl-A : Move cursor to the start of the line.
Ctrl-B : Move cursor back one character.
Ctrl-D : Delete the character under the cursor.
Ctrl-E : Move cursor to the end of the line.
Ctrl-F : Move cursor forward one character.
Ctrl-K : Delete from the cursor to the end of the line.
Ctrl-L : Clear the screen.
Ctrl-N : Move down to the next history entry.
Ctrl-P : Move up to the previous history entry.
Ctrl-R : Reverse search in command history.

Vi
To use vi/vim keybindings, run aider with the --vim switch.

Up Arrow : Move up one line in the current message.
Down Arrow : Move down one line in the current message.
Ctrl-Up : Scroll back through previously sent messages.
Ctrl-Down : Scroll forward through previously sent messages.
Esc : Switch to command mode.
i : Switch to insert mode.
a : Move cursor one character to the right and switch to insert mode.
A : Move cursor to the end of the line and switch to insert mode.
I : Move cursor to the beginning of the line and switch to insert mode.
h : Move cursor one character to the left.
j : Move cursor down one line.
k : Move cursor up one line.
l : Move cursor one character to the right.
w : Move cursor forward one word.
b : Move cursor backward one word.
0 : Move cursor to the beginning of the line.
$ : Move cursor to the end of the line.
x : Delete the character under the cursor.
dd : Delete the current line.
u : Undo the last change.
Ctrl-R : Redo the last undone change.

Chat modes
Aider has a few different chat modes:

- code - Aider will make changes to your code to satisfy your requests.
- architect - Aider will first propose a solution, then ask if you want it to turn that proposal into edits to your files.
- ask - Aider will answer questions about your code, but never edit it.
- help - Aider will answer questions about using aider, configuring, troubleshooting, etc.

By default, aider starts in "code" mode. As you are talking, you can send individual messages in a specific mode using /code, /architect, /ask, and /help commands: Using these /-commands applies just to that particular message. Your next message will go back to the active mode (usually "code" mode by default).

You can switch the active mode in a sticky way with the /chat-mode <mode> command:

/chat-mode code
/chat-mode architect
/chat-mode ask
/chat-mode help

Or you can launch aider in one of the modes with the --chat-mode <mode> switch. There is also a special shortcut --architect to launch in --chat-mode architect.

Architect mode and the editor model
When you are in architect mode, aider sends your request to two models:

1. First, it sends your request to the main active model. The main model is configured with /model, --model or the shortcut switches like --sonnet. After the main model replies, aider will offer to edit the files based on the response.

2. To edit the files, aider sends a second LLM request asking for specific code editing instructions. This request goes to the "editor" model. Aider has built in defaults to select an editor model based on your main model. Or, you can choose an editor model yourself with --editor-model <model>.

Architect mode produces better results than code mode, but uses two LLM requests. This probably makes it slower and more expensive than using code mode.

Architect mode is especially useful with OpenAI's o1 models, which are strong at reasoning but less capable at editing files. Pairing an o1 architect with an editor model like GPT-4o or Sonnet will give the best results.

But architect mode is also quite helpful when you use GPT-4o or Sonnet at both the architect and the editor. Allowing the model two requests to solve the problem and edit the files usually provides a better result.

The editor model uses one of aider's edit formats to let the LLM edit source files. Aider will pick a suitable edit format by default, but you can customize it with --editor-edit-format <format>. The "editor-diff" and "editor-whole" edit formats [https://aider.chat/docs/more/edit-formats.html#editor-diff-and-editor-whole] are the recommended edit formats when using architect mode. See this article on aider's architect/editor mode for more details [https://aider.chat/2024/09/26/architect.html]. 

Examples

Aider v0.47.1-dev
Models: claude-3-5-sonnet-20240620 with diff edit format
Git repo: .git with 298 files
Repo-map: using 1024 tokens
Use /help to see in-chat commands, run with –help to see cmd line args

/ask What is this repo?
This is the source code to the popular django package.

/help How do I use ollama?
Run aider --model ollama/<ollama-model>. See these docs for more info: https://aider.chat/docs/llms/ollama.html

/code Add a function to calculate the factorial of a number
Certainly! I'll add a function to calculate the factorial of a number. Here's the change:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120

This function uses recursion to calculate the factorial. It's been added to your code.

/architect Can we make this simpler?
Yes, you could replace the factorial() function with a call to the math.factorial() builtin. This way you don't have to maintain a custom factorial implementation, and the builtin function is well optimized.

Edit the files? (Y)es/(N)o [Yes]: Yes

<<<<<<< SEARCH
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
=======
from math import factorial
>>>>>>> REPLACE

Images & web pages
You can add images and URLs to the aider chat.

Images
Aider supports working with image files for many vision-capable models like GPT-4o and Claude 3.5 Sonnet. Adding images to a chat can be helpful in many situations:

- Add screenshots of web pages or UIs that you want aider to build or modify.
- Show aider a mockup of a UI you want to build.
- Screenshot an error message that is otherwise hard to copy & paste as text.
- Etc.

You can add images to the chat just like you would add any other file:

- Use /add <image-filename> from within the chat
- Use /paste to paste an image from your clipboard into the chat.
- Launch aider with image filenames on the command line: aider <image-filename> along with any other command line arguments you need.

Web pages
Aider can scrape the text from URLs and add it to the chat. This can be helpful to:

- Include documentation pages for less popular APIs.
- Include the latest docs for libraries or packages that are newer than the model's training cutoff date.
- Etc.

To add URLs to the chat:

- Use /web <url>
- Just paste the URL into the chat and aider will ask if you want to add it.

You can also scrape web pages from the command line to see the markdown version that aider produces:

python -m aider.scrape https://aider.chat/docs/usage/tips.html

Prompt caching
Aider supports prompt caching for cost savings and faster coding. Currently Anthropic provides caching for Sonnet and Haiku, and DeepSeek provides caching for Coder.

Aider organizes the chat history to try and cache:

- The system prompt.
- Read only files added with --read or /read-only.
- The repository map.
- The editable files that have been added to the chat.

§ aider --cache-prompts --no-stream
Aider vO.51.0
Model: claude-3-5-sonnet with ask edit format, prompt cache.
> What is this repo?
This appears to be a repository for a tool called "aider" that involves nteraction with language models for AI-assisted coding.
Tokens: 1.7k sent, 1.6k cache write, 51 received.
Cost: $0. 0069 msg.
> What language is it written in?
The repository appears to be primarily written in Python, as evidenced by the numerous -py files and the presence of Python-specific modules.
Tokens: 1.7k sent, 1. 6k cache hit, 43 received. Cost: $0.0014 msg.

Usage
Run aider with --cache-prompts or add that setting to your configuration files [https://aider.chat/docs/config.html]. 

Due to limitations in the provider APIs, caching statistics and costs are not available when streaming responses. To turn off streaming, use --no-stream.

When caching is enabled, it will be noted for the main model when aider launches:

Main model: claude-3-5-sonnet-20240620 with diff edit format, prompt cache, infinite output

Preventing cache expiration
Aider can ping the provider to keep your prompt cache warm and prevent it from expiring. By default, Anthropic keeps your cache for 5 minutes. Use --cache-keepalive-pings N to tell aider to ping every 5 minutes to keep the cache warm. Aider will ping up to N times over a period of N*5 minutes after each message you send.

Aider in your IDE

AI comments
If you run aider with --watch-files, it will watch all files in your repo and look for any AI coding instructions you add using your favorite IDE or text editor.

Specifically, aider looks for one-liner comments (# … or // …) that either start or end with AI, AI! or AI? like these:

# Make a snake game. AI!
# What is the purpose of this method AI?

Or in // comment languages…

// Write a protein folding prediction engine. AI!

Aider will take note of all the comments that start or end with AI. Comments that include AI! with an exclamation point or AI? with a question mark are special. They triggers aider to take action to collect all the AI comments and use them as your instructions.

- AI! triggers aider to make changes to your code.
- AI? triggers aider to answer your question.

See the demo video above that shows aider working with AI comments in VSCode.

Example
For example, if you included this AI comment in your code:

function factorial(n) // Implement this. AI!

Then aider would update the file and implement the function:

function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

Comment styles
Aider only watches for these types of one-liner comments:

# Python and bash style
// Javascript style 
-- SQL style 

Aider will look for those comment types in all files. You can use them into any code file you're editing, even if they aren't the correct comment syntax for that language.

Multiple uses
This capability is quite flexible and powerful, and can be used in many ways.

In-context instructions
You can add an AI comment in the function you want changed, explaining the change request in-context right where you want the changes.

app.get('/sqrt/:n', (req, res) => {
    const n = parseFloat(req.params.n);

    // Add error handling for NaN and less than zero. AI!

    const result = math.sqrt(n);
    res.json({ result: result });
});

Multiple comments
You can add multiple AI comments without the !, before triggering aider with a final AI!. Also keep in mind that you can spread the AI comments across multiple files, if you want to coordinate changes in multiple places. Just use AI! last, to trigger aider.

@app.route('/factorial/<int:n>')
def factorial(n):
    if n < 0:
        return jsonify(error="Factorial is not defined for negative numbers"), 400
        
    # AI: Refactor this code...
    
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    # ... into to a compute_factorial() function. AI!
    
    return jsonify(result=result)

Long form instructions
You can add a block of comments, with longer instructions. Just be sure to start or end one of the lines with AI or AI! to draw aider's attention to the block.

# Make these changes: AI!
# - Add a proper main() function
# - Use Click to process cmd line args
# - Accept --host and --port args
# - Print a welcome message that includes the listening url

if __name__ == "__main__":
    app.run(debug=True)

Add a file to the aider chat
Rather than using /add to add a file inside the aider chat, you can simply put an #AI comment in it and save the file. You can undo/remove the comment immediately if you like, the file will still be added to the aider chat.

Also use aider chat in the terminal
It can be really helpful to get a change started with AI comments. But sometimes you want to build on or refine those changes. You can of course continue to do that with AI comments, but it can sometimes be effective to switch over to the aider terminal chat. The chat has the history of the AI comments you just made, so you can continue on naturally from there.

You can also use the normal aider chat in your terminal to work with many of aider's more advanced features:

- Use /undo to revert changes you don't like. Although you may also be able to use your IDE's undo function to step back in the file history.
- Use chat modes [https://aider.chat/docs/usage/modes.html] to ask questions or get help.
- Manage the chat context with /tokens, /clear, /drop, /reset. Adding an AI comment will add the file to the chat. Periodically, you may want remove extra context that is no longer needed.
- Fix lint and test errors [https://aider.chat/docs/usage/lint-test.html]. 
- Run shell commands.
- Etc.

You can be lazy
The examples above all show AI comments with full sentences, proper capitalization, punctuation, etc. This was done to help explain how AI comments work, but is not needed in practice.

Most LLMs are perfectly capable of dealing with ambiguity and inferring implied intent. This often allows you to be quite lazy with your AI comments. In particular, you can start and end comments with lowercase ai and ai!, but you can also be much more terse with the request itself. Below are simpler versions of some of the examples given above.

When the context clearly implies the needed action, ai! might be all you need. For example, to implement a factorial function in a program full of other math functions either of these approaches would probably work:

function factorial(n) // ai!

OR 

// add factorial() ai!

Rather than a long, explicit comment like "Add error handling for NaN and less than zero," you can let aider infer more about the request. This simpler comment may be sufficient:

app.get('/sqrt/:n', (req, res) => {
    const n = parseFloat(req.params.n);

    // add error handling ai!

    const result = math.sqrt(n);
    res.json({ result: result });
});

Similarly, this refactor probably could have been requested with fewer words, like this:

@app.route('/factorial/<int:n>')
def factorial(n):
    if n < 0:
        return jsonify(error="Factorial is not defined for negative numbers"), 400
        
    # ai refactor...
    
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    # ... to compute_factorial() ai!
    
    return jsonify(result=result)

As you use aider with your chosen LLM, you can develop a sense for how explicit you need to make your AI comments.

Behind the scenes
Aider sends your AI comments to the LLM with the repo map [https://aider.chat/docs/repomap.html] and all the other code context you've added to the chat.

It also pulls out and highlights the AI comments with specific context, showing the LLM exactly how they fit into the code base.

The "AI" comments below marked with █ can be found in the code files I've shared with you.
They contain your instructions.
Make the requested changes.
Be sure to remove all these "AI" comments from the code!

todo_app.py:
⋮...
│class TodoList:
⋮...
│    def __init__(self):
│        """Initialize an empty todo list"""
⋮...
│
│    def list_tasks(self):
│        """Display all tasks"""
█        # Implement this. AI!
│
│def main():
│    todo = TodoList()
│
⋮...

Aider in your browser
Use aider's new experimental browser UI to collaborate with LLMs to edit code in your local git repo. Aider will directly edit the code in your local source files, and [https://aider.chat/docs/git.html] git commit the changes with sensible commit messages. You can start a new project or work with an existing git repo. Aider works well with GPT 3.5, GPT-4, GPT-4 Turbo with Vision, and Claude 3 Opus. It also supports connecting to almost any LLM [https://aider.chat/docs/llms.html]. 

Use the --browser switch to launch the browser version of aider:

python -m pip install -U aider-chat

export OPENAI_API_KEY=<key> # Mac/Linux
setx   OPENAI_API_KEY <key> # Windows, restart shell after setx

aider --browser

Specifying coding conventions
Sometimes you want GPT to be aware of certain coding guidelines, like whether to provide type hints, which libraries or packages to prefer, etc.

The easiest way to do that with aider is to simply create a small markdown file and include it in the chat.

For example, say we want our python code to:

- Prefer httpx over requests for making http requests.
- Use types everywhere possible.

We would simply create a file like CONVENTIONS.md with those lines and then we can add it to the aider chat, along with the file(s) that we want to edit.

It's best to load the conventions file with /read CONVENTIONS.md or aider --read CONVENTIONS.md. This way it is marked as read-only, and cached if prompt caching is enabled.

Community contributed conventions
You can check the aider conventions repository [https://github.com/Aider-AI/conventions] to find or contribute conventions files.

Always load conventions
You can also configure aider to always load your conventions file in the .aider.conf.yml config file [https://aider.chat/docs/config/aider_conf.html]: 

# alone
read: CONVENTIONS.md

# multiple files
read: [CONVENTIONS.md, anotherfile.txt]

Example
See below for an example of how the conventions can affect the code that aider writes.

$ aider –read CONVENTIONS.md useragent.py

Aider v0.24.2-dev
Added CONVENTIONS.md to the chat.
Added useragent.py to the chat.

write a function that uses httpbin to check the user agent on the request. return the ua.
To fulfill your request, I will:

Add an import for httpx.
Write a function named check_user_agent that makes a GET request to httpbin.org/user-agent and returns the user agent string.
Here is the diff for the useragent.py file:

--- useragent.py
+++ useragent.py
@@ ... @@
+import httpx
+
+def check_user_agent() -> str:
+    response = httpx.get('https://httpbin.org/user-agent')
+    return response.json()['user-agent']

This function uses httpx to make a GET request to httpbin.org/user-agent, which returns a JSON response containing the user agent of the HTTP client. The function then extracts the user agent string from the JSON response and returns it.

Applied edit to useragent.py

GPT correctly used httpx and provided type hints. See below for the transcript of this same coding task conducted without using CONVENTIONS.md. In this case, GPT used requests and skipped types, which is perhaps more typical in small python scripts.

$ aider useragent.py

Aider v0.24.2-dev
Added useragent.py to the chat.

write a function that uses httpbin to check the user agent on the request. return the ua.
--- /dev/null
+++ useragent.py
@@ ... @@
+import requests
+
+def check_user_agent():
+    response = requests.get('https://httpbin.org/user-agent')
+    user_agent = response.json().get('user-agent')
+    return user_agent

Applied edit to useragent.py

Copy/paste with web chat

Working with an LLM web chat
Aider can connect to most LLMs via API [https://aider.chat/docs/llms.html] and works best that way. But there are times when you may want to work with an LLM via its web chat interface:

- Workplace policies may limit your LLM usage to a proprietary web chat system.
- The web chat LLM may have access to unique context or may have been specially fine tuned for your task.
- It may be cost prohibitive to use some models via API.
- There may not be an API available.

Aider has features for working with an LLM via its web chat interface. This allows you to use the web chat LLM as the "big brain code architect" while running aider with a smaller, cheaper LLM to actually make changes to your local files.

For this "file editor" part of the process you can run aider with many open source, free or very inexpensive LLMs. For example, the demo video above shows aider using DeepSeek to apply the changes that o1-preview is suggesting in the web chat.

Copy aider's code context to your clipboard, paste into the web UI
The /copy-context <instructions> command can be used in chat to copy aider's code context to your clipboard. It will include:

- All the files which have been added to the chat via /add.
- Any read only files which have been added via /read.
- Aider's repository map [https://aider.chat/docs/repomap.html] that brings in code context related to the above files from elsewhere in your git repo.
- Some instructions to the LLM that ask it to output change instructions concisely.
- If you include <instructions>, they will be copied too.

You can paste the context into your browser, and start interacting with the LLM web chat to ask for code changes.

Paste the LLM's reply back into aider to edit your files
Once the LLM has replied, you can use the "copy response" button in the web UI to copy the LLM's response. Back in aider, you can run /paste and aider will edit your files to implement the changes suggested by the LLM.

You can use a cheap, efficient model like GPT-4o Mini, DeepSeek or Qwen to do these edits. This works best if you run aider with --edit-format editor-diff or --edit-format editor-whole.

Copy/paste mode
Aider has a --copy-paste mode that streamlines this entire process:

- Whenever you /add or /read files, aider will automatically copy the entire, updated code context to your clipboard. You'll see "Copied code context to clipboard" whenever this happens.
- When you copy the LLM reply to your clipboard outside aider, aider will automatically notice and load it into the aider chat. Just press ENTER to send the message and aider will apply the LLMs changes to your local files.
- Aider will automatically select the best edit format for this copy/paste functionality. Depending on the LLM you have aider use, it will be either editor-whole or editor-diff.

Linting and testing
Aider can automatically lint and test your code every time it makes changes. This helps identify and repair any problems introduced by the AI edits.

Linting
Aider comes with built in linters for most popular languages [https://aider.chat/docs/languages.html] and will automatically lint code in these languages.

Or you can specify your favorite linter with the --lint-cmd <cmd> switch. The lint command should accept the filenames of the files to lint. If there are linting errors, aider expects the command to print them on stdout/stderr and return a non-zero exit code. This is how most linters normally operate.

By default, aider will lint any files which it edits. You can disable this with the --no-auto-lint switch.

Testing
You can run tests with /test <test-command>. Aider will run the test command without any arguments. If there are test errors, aider expects the command to print them on stdout/stderr and return a non-zero exit code.

Aider will try and fix any errors if the command returns a non-zero exit code.

You can configure aider to run your test suite after each time the AI edits your code using the --test-cmd <test-command> and --auto-test switch.

Compiled languages
If you want to have aider compile code after each edit, you can use the lint and test commands to achieve this.

- You might want to recompile each file which was modified to check for compile errors. To do this, provide a --lint-cmd which both lints and compiles the file. You could create a small shell script for this.
- You might want to rebuild the entire project after files are edited to check for build errors. To do this, provide a --test-cmd which both builds and tests the project. You could create a small shell script for this. Or you may be able to do something as simple as --test-cmd "dotnet build && dotnet test".

Manually running code
You can use the /run command in the chat to run your code and optionally share the output with aider. This can be useful to share error messages or to show aider the code's output before asking for changes or corrections.

Aider v0.43.5-dev

/run python myscript.py
Traceback (most recent call last):  
 File "myscript.py", line 22, in \<module\ 
   raise ValueError("something bad happened")  
ValueError: something bad happened  

Add the output to the chat? y

Aider can connect to most LLMs
connecting to many LLMs

Best models
Aider works best with these models, which are skilled at editing code:

GPT-4o
Claude 3.5 Sonnet
Claude 3 Opus
DeepSeek Coder V2

Free models
Aider works with a number of free API providers:

Google's Gemini 1.5 Pro works with aider, with code editing capabilities similar to GPT-3.5.
You can use Llama 3 70B on Groq which is comparable to GPT-3.5 in code editing performance.
Cohere also offers free API access to their Command-R+ model, which works with aider as a very basic coding assistant.
Local models
Aider can work also with local models, for example using Ollama. It can also access local models that provide an Open AI compatible API.

Use a capable model
Check Aider's LLM leaderboards to see which models work best with aider.

Be aware that aider may not work well with less capable models. If you see the model returning code, but aider isn't able to edit your files and commit the changes… this is usually because the model isn't capable of properly returning "code edits". Models weaker than GPT 3.5 may have problems working well with aider.

OpenAI
To work with OpenAI's models, you need to provide your OpenAI API key either in the OPENAI_API_KEY environment variable or via the --openai-api-key command line switch.

Aider has some built in shortcuts for the most popular OpenAI models and has been tested and benchmarked to work well with them:

python -m pip install -U aider-chat

export OPENAI_API_KEY=<key> # Mac/Linux
setx   OPENAI_API_KEY <key> # Windows, restart shell after setx

# Aider uses gpt-4o by default (or use --4o)
aider

# GPT-4o
aider --4o

# GPT-3.5 Turbo
aider --35-turbo

# o1-mini
aider --model o1-mini

# o1-preview
aider --model o1-preview

# List models available from OpenAI
aider --list-models openai/

You can use aider --model <model-name> to use any other OpenAI model. For example, if you want to use a specific version of GPT-4 Turbo you could do aider --model gpt-4-0125-preview.

Anthropic
To work with Anthropic's models, you need to provide your Anthropic API key either in the ANTHROPIC_API_KEY environment variable or via the --anthropic-api-key command line switch.

Aider has some built in shortcuts for the most popular Anthropic models and has been tested and benchmarked to work well with them:

python -m pip install -U aider-chat

export ANTHROPIC_API_KEY=<key> # Mac/Linux
setx   ANTHROPIC_API_KEY <key> # Windows, restart shell after setx

# Aider uses Claude 3.5 Sonnet by default (or use --sonnet)
aider

# Claude 3 Opus
aider --opus

# List models available from Anthropic
aider --list-models anthropic/

NOTE 
Anthropic has very low rate limits. You can access all the Anthropic models via OpenRouter or Google Vertex AI with more generous rate limits.

You can use aider --model <model-name> to use any other Anthropic model. For example, if you want to use a specific version of Opus you could do aider --model claude-3-opus-20240229.

Configuration
Aider has many options which can be set with command line switches. Most options can also be set in an .aider.conf.yml file which can be placed in your home directory or at the root of your git repo. Or by setting environment variables like AIDER_xxx either in your shell or a .env file.

Here are 4 equivalent ways of setting an option.

With a command line switch:

$ aider --dark-mode

Using a .aider.conf.yml file:

dark-mode: true

By setting an environment variable:

export AIDER_DARK_MODE=true

Using an .env file:

AIDER_DARK_MODE=true

TIP 
See the API key configuration docs for information on how to configure and store your API keys.

API Keys
Aider lets you specify API keys in a few ways:

On the command line
As environment variables
In a .env file
In your .aider.conf.yml config file

OpenAI and Anthropic
Aider has special support for providing OpenAI and Anthropic API keys via dedicated switches and configuration options. Settings keys for other providers works a bit differently, see below.

Command line
You can set OpenAI and Anthropic API keys via command line switches [https://aider.chat/docs/config/options.html#api-keys-and-settings] --openai-api-key and --anthropic-api-key.

Environment variables or .env file
You can also store them in environment variables or a .env file [https://aider.chat/docs/config/dotenv.html], which also works for every API provider:

OPENAI_API_KEY=<key>
ANTHROPIC_API_KEY=<key>

Yaml config file
You can also set those API keys via special entries in the yaml config file [https://aider.chat/docs/config/aider_conf.html], like this:

openai-api-key: <key>
anthropic-api-key: <key>

Options reference
You can use aider --help to see all the available options, or review them below.

Usage summary
options:
--help
Main model:
--model MODEL
--opus
--sonnet
--haiku
--4
--4o
--mini
--4-turbo
--35turbo
--deepseek
--o1-mini
--o1-preview
API Keys and settings:
--openai-api-key VALUE
--anthropic-api-key VALUE
--openai-api-base VALUE
--openai-api-type VALUE
--openai-api-version VALUE
--openai-api-deployment-id VALUE
--openai-organization-id VALUE
--set-env ENV_VAR_NAME=value
--api-key PROVIDER=KEY
Model settings:
--list-models MODEL
--model-settings-file MODEL_SETTINGS_FILE
--model-metadata-file MODEL_METADATA_FILE
--alias ALIAS:MODEL
--verify-ssl
--timeout VALUE
--edit-format EDIT_FORMAT
--architect
--weak-model WEAK_MODEL
--editor-model EDITOR_MODEL
--editor-edit-format EDITOR_EDIT_FORMAT
--show-model-warnings
--max-chat-history-tokens VALUE
Cache settings:
--cache-prompts
--cache-keepalive-pings VALUE
Repomap settings:
--map-tokens VALUE
--map-refresh VALUE
--map-multiplier-no-files VALUE
History Files:
--input-history-file INPUT_HISTORY_FILE
--chat-history-file CHAT_HISTORY_FILE
--restore-chat-history
--llm-history-file LLM_HISTORY_FILE
Output settings:
--dark-mode
--light-mode
--pretty
--stream
--user-input-color VALUE
--tool-output-color VALUE
--tool-error-color VALUE
--tool-warning-color VALUE
--assistant-output-color VALUE
--completion-menu-color COLOR
--completion-menu-bg-color COLOR
--completion-menu-current-color COLOR
--completion-menu-current-bg-color COLOR
--code-theme VALUE
--show-diffs
Git settings:
--git
--gitignore
--aiderignore AIDERIGNORE
--subtree-only
--auto-commits
--dirty-commits
--attribute-author
--attribute-committer
--attribute-commit-message-author
--attribute-commit-message-committer
--commit
--commit-prompt PROMPT
--dry-run
--skip-sanity-check-repo
--watch-files
Fixing and committing:
--lint
--lint-cmd
--auto-lint
--test-cmd VALUE
--auto-test
--test
Analytics:
--analytics
--analytics-log ANALYTICS_LOG_FILE
--analytics-disable
Upgrading:
--just-check-update
--check-update
--show-release-notes
--install-main-branch
--upgrade
--version
Modes:
--message COMMAND
--message-file MESSAGE_FILE
--gui
--copy-paste
--apply FILE
--apply-clipboard-edits
--exit
--show-repo-map
--show-prompts
Voice settings:
--voice-format VOICE_FORMAT
--voice-language VOICE_LANGUAGE
--voice-input-device VOICE_INPUT_DEVICE
Other settings:
--file FILE
--read FILE
--vim
--chat-language CHAT_LANGUAGE
--yes-always
--verbose
--load LOAD_FILE
--encoding VALUE
--config CONFIG_FILE
--env-file ENV_FILE
--suggest-shell-commands
--fancy-input
--multiline
--detect-urls
--editor VALUE

TIP 
See the API key configuration docs for information on how to configure and store your API keys.

Usage summary

usage: aider [-h] [--model] [--opus] [--sonnet] [--haiku] [--4]
             [--4o] [--mini] [--4-turbo] [--35turbo] [--deepseek]
             [--o1-mini] [--o1-preview] [--openai-api-key]
             [--anthropic-api-key] [--openai-api-base]
             [--openai-api-type] [--openai-api-version]
             [--openai-api-deployment-id] [--openai-organization-id]
             [--set-env] [--api-key] [--list-models]
             [--model-settings-file] [--model-metadata-file]
             [--alias] [--verify-ssl | --no-verify-ssl] [--timeout]
             [--edit-format] [--architect] [--weak-model]
             [--editor-model] [--editor-edit-format]
             [--show-model-warnings | --no-show-model-warnings]
             [--max-chat-history-tokens]
             [--cache-prompts | --no-cache-prompts]
             [--cache-keepalive-pings] [--map-tokens]
             [--map-refresh] [--map-multiplier-no-files]
             [--input-history-file] [--chat-history-file]
             [--restore-chat-history | --no-restore-chat-history]
             [--llm-history-file] [--dark-mode] [--light-mode]
             [--pretty | --no-pretty] [--stream | --no-stream]
             [--user-input-color] [--tool-output-color]
             [--tool-error-color] [--tool-warning-color]
             [--assistant-output-color] [--completion-menu-color]
             [--completion-menu-bg-color]
             [--completion-menu-current-color]
             [--completion-menu-current-bg-color] [--code-theme]
             [--show-diffs] [--git | --no-git]
             [--gitignore | --no-gitignore] [--aiderignore]
             [--subtree-only] [--auto-commits | --no-auto-commits]
             [--dirty-commits | --no-dirty-commits]
             [--attribute-author | --no-attribute-author]
             [--attribute-committer | --no-attribute-committer]
             [--attribute-commit-message-author | --no-attribute-commit-message-author]
             [--attribute-commit-message-committer | --no-attribute-commit-message-committer]
             [--commit] [--commit-prompt] [--dry-run | --no-dry-run]
             [--skip-sanity-check-repo]
             [--watch-files | --no-watch-files] [--lint]
             [--lint-cmd] [--auto-lint | --no-auto-lint]
             [--test-cmd] [--auto-test | --no-auto-test] [--test]
             [--analytics | --no-analytics] [--analytics-log]
             [--analytics-disable] [--just-check-update]
             [--check-update | --no-check-update]
             [--show-release-notes | --no-show-release-notes]
             [--install-main-branch] [--upgrade] [--version]
             [--message] [--message-file]
             [--gui | --no-gui | --browser | --no-browser]
             [--copy-paste | --no-copy-paste] [--apply]
             [--apply-clipboard-edits] [--exit] [--show-repo-map]
             [--show-prompts] [--voice-format] [--voice-language]
             [--voice-input-device] [--file] [--read] [--vim]
             [--chat-language] [--yes-always] [-v] [--load]
             [--encoding] [-c] [--env-file]
             [--suggest-shell-commands | --no-suggest-shell-commands]
             [--fancy-input | --no-fancy-input]
             [--multiline | --no-multiline]
             [--detect-urls | --no-detect-urls] [--editor]

options:
--help
show this help message and exit
Aliases:

-h
--help

Main model:
--model MODEL
Specify the model to use for the main chat
Environment variable: AIDER_MODEL

--opus
Use claude-3-opus-20240229 model for the main chat
Environment variable: AIDER_OPUS

--sonnet
Use claude-3-5-sonnet-20241022 model for the main chat
Environment variable: AIDER_SONNET

--haiku
Use claude-3-5-haiku-20241022 model for the main chat
Environment variable: AIDER_HAIKU

--4
Use gpt-4-0613 model for the main chat
Environment variable: AIDER_4
Aliases:

--4
-4
--4o
Use gpt-4o model for the main chat
Environment variable: AIDER_4O

--mini
Use gpt-4o-mini model for the main chat
Environment variable: AIDER_MINI

--4-turbo
Use gpt-4-1106-preview model for the main chat
Environment variable: AIDER_4_TURBO

--35turbo
Use gpt-3.5-turbo model for the main chat
Environment variable: AIDER_35TURBO
Aliases:

--35turbo
--35-turbo
--3
-3
--deepseek
Use deepseek/deepseek-chat model for the main chat
Environment variable: AIDER_DEEPSEEK

--o1-mini
Use o1-mini model for the main chat
Environment variable: AIDER_O1_MINI

--o1-preview
Use o1-preview model for the main chat
Environment variable: AIDER_O1_PREVIEW

API Keys and settings:
--openai-api-key VALUE
Specify the OpenAI API key
Environment variable: AIDER_OPENAI_API_KEY

--anthropic-api-key VALUE
Specify the Anthropic API key
Environment variable: AIDER_ANTHROPIC_API_KEY

--openai-api-base VALUE
Specify the api base url
Environment variable: AIDER_OPENAI_API_BASE

--openai-api-type VALUE
(deprecated, use –set-env OPENAI_API_TYPE=) Environment variable: `AIDER_OPENAI_API_TYPE`

--openai-api-version VALUE
(deprecated, use –set-env OPENAI_API_VERSION=) Environment variable: `AIDER_OPENAI_API_VERSION`

--openai-api-deployment-id VALUE
(deprecated, use –set-env OPENAI_API_DEPLOYMENT_ID=) Environment variable: `AIDER_OPENAI_API_DEPLOYMENT_ID`

--openai-organization-id VALUE
(deprecated, use –set-env OPENAI_ORGANIZATION=) Environment variable: `AIDER_OPENAI_ORGANIZATION_ID`

--set-env ENV_VAR_NAME=value
Set an environment variable (to control API settings, can be used multiple times)
Default: []
Environment variable: AIDER_SET_ENV

--api-key PROVIDER=KEY
Set an API key for a provider (eg: –api-key provider= sets PROVIDER_API_KEY=) Default: [] Environment variable: `AIDER_API_KEY`

Model settings:
--list-models MODEL
List known models which match the (partial) MODEL name
Environment variable: AIDER_LIST_MODELS
Aliases:

--list-models MODEL
--models MODEL
--model-settings-file MODEL_SETTINGS_FILE
Specify a file with aider model settings for unknown models
Default: .aider.model.settings.yml
Environment variable: AIDER_MODEL_SETTINGS_FILE

--model-metadata-file MODEL_METADATA_FILE
Specify a file with context window and costs for unknown models
Default: .aider.model.metadata.json
Environment variable: AIDER_MODEL_METADATA_FILE

--alias ALIAS:MODEL
Add a model alias (can be used multiple times)
Environment variable: AIDER_ALIAS

--verify-ssl
Verify the SSL cert when connecting to models (default: True)
Default: True
Environment variable: AIDER_VERIFY_SSL
Aliases:

--verify-ssl
--no-verify-ssl
--timeout VALUE
Timeout in seconds for API calls (default: None)
Environment variable: AIDER_TIMEOUT

--edit-format EDIT_FORMAT
Specify what edit format the LLM should use (default depends on model)
Environment variable: AIDER_EDIT_FORMAT
Aliases:

--edit-format EDIT_FORMAT
--chat-mode EDIT_FORMAT
--architect
Use architect edit format for the main chat
Environment variable: AIDER_ARCHITECT

--weak-model WEAK_MODEL
Specify the model to use for commit messages and chat history summarization (default depends on –model)
Environment variable: AIDER_WEAK_MODEL

--editor-model EDITOR_MODEL
Specify the model to use for editor tasks (default depends on –model)
Environment variable: AIDER_EDITOR_MODEL

--editor-edit-format EDITOR_EDIT_FORMAT
Specify the edit format for the editor model (default: depends on editor model)
Environment variable: AIDER_EDITOR_EDIT_FORMAT

--show-model-warnings
Only work with models that have meta-data available (default: True)
Default: True
Environment variable: AIDER_SHOW_MODEL_WARNINGS
Aliases:

--show-model-warnings
--no-show-model-warnings
--max-chat-history-tokens VALUE
Soft limit on tokens for chat history, after which summarization begins. If unspecified, defaults to the model's max_chat_history_tokens.
Environment variable: AIDER_MAX_CHAT_HISTORY_TOKENS

Cache settings:
--cache-prompts
Enable caching of prompts (default: False)
Default: False
Environment variable: AIDER_CACHE_PROMPTS
Aliases:

--cache-prompts
--no-cache-prompts
--cache-keepalive-pings VALUE
Number of times to ping at 5min intervals to keep prompt cache warm (default: 0)
Default: 0
Environment variable: AIDER_CACHE_KEEPALIVE_PINGS

Repomap settings:
--map-tokens VALUE
Suggested number of tokens to use for repo map, use 0 to disable (default: 1024)
Environment variable: AIDER_MAP_TOKENS

--map-refresh VALUE
Control how often the repo map is refreshed. Options: auto, always, files, manual (default: auto)
Default: auto
Environment variable: AIDER_MAP_REFRESH

--map-multiplier-no-files VALUE
Multiplier for map tokens when no files are specified (default: 2)
Default: 2
Environment variable: AIDER_MAP_MULTIPLIER_NO_FILES

History Files:
--input-history-file INPUT_HISTORY_FILE
Specify the chat input history file (default: .aider.input.history)
Default: .aider.input.history
Environment variable: AIDER_INPUT_HISTORY_FILE

--chat-history-file CHAT_HISTORY_FILE
Specify the chat history file (default: .aider.chat.history.md)
Default: .aider.chat.history.md
Environment variable: AIDER_CHAT_HISTORY_FILE

--restore-chat-history
Restore the previous chat history messages (default: False)
Default: False
Environment variable: AIDER_RESTORE_CHAT_HISTORY
Aliases:

--restore-chat-history
--no-restore-chat-history
--llm-history-file LLM_HISTORY_FILE
Log the conversation with the LLM to this file (for example, .aider.llm.history)
Environment variable: AIDER_LLM_HISTORY_FILE

Output settings:
--dark-mode
Use colors suitable for a dark terminal background (default: False)
Default: False
Environment variable: AIDER_DARK_MODE

--light-mode
Use colors suitable for a light terminal background (default: False)
Default: False
Environment variable: AIDER_LIGHT_MODE

--pretty
Enable/disable pretty, colorized output (default: True)
Default: True
Environment variable: AIDER_PRETTY
Aliases:

--pretty
--no-pretty
--stream
Enable/disable streaming responses (default: True)
Default: True
Environment variable: AIDER_STREAM
Aliases:

--stream
--no-stream
--user-input-color VALUE
Set the color for user input (default: #00cc00)
Default: #00cc00
Environment variable: AIDER_USER_INPUT_COLOR

--tool-output-color VALUE
Set the color for tool output (default: None)
Environment variable: AIDER_TOOL_OUTPUT_COLOR

--tool-error-color VALUE
Set the color for tool error messages (default: #FF2222)
Default: #FF2222
Environment variable: AIDER_TOOL_ERROR_COLOR

--tool-warning-color VALUE
Set the color for tool warning messages (default: #FFA500)
Default: #FFA500
Environment variable: AIDER_TOOL_WARNING_COLOR

--assistant-output-color VALUE
Set the color for assistant output (default: #0088ff)
Default: #0088ff
Environment variable: AIDER_ASSISTANT_OUTPUT_COLOR

--completion-menu-color COLOR
Set the color for the completion menu (default: terminal's default text color)
Environment variable: AIDER_COMPLETION_MENU_COLOR

--completion-menu-bg-color COLOR
Set the background color for the completion menu (default: terminal's default background color)
Environment variable: AIDER_COMPLETION_MENU_BG_COLOR

--completion-menu-current-color COLOR
Set the color for the current item in the completion menu (default: terminal's default background color)
Environment variable: AIDER_COMPLETION_MENU_CURRENT_COLOR

--completion-menu-current-bg-color COLOR
Set the background color for the current item in the completion menu (default: terminal's default text color)
Environment variable: AIDER_COMPLETION_MENU_CURRENT_BG_COLOR

--code-theme VALUE
Set the markdown code theme (default: default, other options include monokai, solarized-dark, solarized-light, or a Pygments builtin style, see https://pygments.org/styles for available themes)
Default: default
Environment variable: AIDER_CODE_THEME

--show-diffs
Show diffs when committing changes (default: False)
Default: False
Environment variable: AIDER_SHOW_DIFFS

Git settings:
--git
Enable/disable looking for a git repo (default: True)
Default: True
Environment variable: AIDER_GIT
Aliases:

--git
--no-git
--gitignore
Enable/disable adding .aider* to .gitignore (default: True)
Default: True
Environment variable: AIDER_GITIGNORE
Aliases:

--gitignore
--no-gitignore
--aiderignore AIDERIGNORE
Specify the aider ignore file (default: .aiderignore in git root)
Default: .aiderignore
Environment variable: AIDER_AIDERIGNORE

--subtree-only
Only consider files in the current subtree of the git repository
Default: False
Environment variable: AIDER_SUBTREE_ONLY

--auto-commits
Enable/disable auto commit of LLM changes (default: True)
Default: True
Environment variable: AIDER_AUTO_COMMITS
Aliases:

--auto-commits
--no-auto-commits
--dirty-commits
Enable/disable commits when repo is found dirty (default: True)
Default: True
Environment variable: AIDER_DIRTY_COMMITS
Aliases:

--dirty-commits
--no-dirty-commits
--attribute-author
Attribute aider code changes in the git author name (default: True)
Default: True
Environment variable: AIDER_ATTRIBUTE_AUTHOR
Aliases:

--attribute-author
--no-attribute-author
--attribute-committer
Attribute aider commits in the git committer name (default: True)
Default: True
Environment variable: AIDER_ATTRIBUTE_COMMITTER
Aliases:

--attribute-committer
--no-attribute-committer
--attribute-commit-message-author
Prefix commit messages with 'aider: ' if aider authored the changes (default: False)
Default: False
Environment variable: AIDER_ATTRIBUTE_COMMIT_MESSAGE_AUTHOR
Aliases:

--attribute-commit-message-author
--no-attribute-commit-message-author
--attribute-commit-message-committer
Prefix all commit messages with 'aider: ' (default: False)
Default: False
Environment variable: AIDER_ATTRIBUTE_COMMIT_MESSAGE_COMMITTER
Aliases:

--attribute-commit-message-committer
--no-attribute-commit-message-committer
--commit
Commit all pending changes with a suitable commit message, then exit
Default: False
Environment variable: AIDER_COMMIT

--commit-prompt PROMPT
Specify a custom prompt for generating commit messages
Environment variable: AIDER_COMMIT_PROMPT

--dry-run
Perform a dry run without modifying files (default: False)
Default: False
Environment variable: AIDER_DRY_RUN
Aliases:

--dry-run
--no-dry-run
--skip-sanity-check-repo
Skip the sanity check for the git repository (default: False)
Default: False
Environment variable: AIDER_SKIP_SANITY_CHECK_REPO

--watch-files
Enable/disable watching files for ai coding comments (default: False)
Default: False
Environment variable: AIDER_WATCH_FILES
Aliases:

--watch-files
--no-watch-files
Fixing and committing:
--lint
Lint and fix provided files, or dirty files if none provided
Default: False
Environment variable: AIDER_LINT

--lint-cmd
Specify lint commands to run for different languages, eg: "python: flake8 –select=…" (can be used multiple times)
Default: []
Environment variable: AIDER_LINT_CMD

--auto-lint
Enable/disable automatic linting after changes (default: True)
Default: True
Environment variable: AIDER_AUTO_LINT
Aliases:

--auto-lint
--no-auto-lint
--test-cmd VALUE
Specify command to run tests
Default: []
Environment variable: AIDER_TEST_CMD

--auto-test
Enable/disable automatic testing after changes (default: False)
Default: False
Environment variable: AIDER_AUTO_TEST
Aliases:

--auto-test
--no-auto-test
--test
Run tests, fix problems found and then exit
Default: False
Environment variable: AIDER_TEST

Analytics:
--analytics
Enable/disable analytics for current session (default: random)
Environment variable: AIDER_ANALYTICS
Aliases:

--analytics
--no-analytics
--analytics-log ANALYTICS_LOG_FILE
Specify a file to log analytics events
Environment variable: AIDER_ANALYTICS_LOG

--analytics-disable
Permanently disable analytics
Default: False
Environment variable: AIDER_ANALYTICS_DISABLE

Upgrading:
--just-check-update
--check-update
--show-release-notes
--install-main-branch
--upgrade
--version
Modes:
--message COMMAND
--message-file MESSAGE_FILE
--gui
--copy-paste
--apply FILE
--apply-clipboard-edits
--exit
--show-repo-map
--show-prompts
Voice settings:
--voice-format VOICE_FORMAT
--voice-language VOICE_LANGUAGE
--voice-input-device VOICE_INPUT_DEVICE
Other settings:
--file FILE
--read FILE
--vim
--chat-language CHAT_LANGUAGE
--yes-always
--verbose
--load LOAD_FILE
--encoding VALUE
--config CONFIG_FILE
--env-file ENV_FILE
--suggest-shell-commands
--fancy-input
--multiline
--detect-urls
--editor VALUE

TIP 
See the API key configuration docs for information on how to configure and store your API keys.

Usage summary

usage: aider [-h] [--model] [--opus] [--sonnet] [--haiku] [--4]
             [--4o] [--mini] [--4-turbo] [--35turbo] [--deepseek]
             [--o1-mini] [--o1-preview] [--openai-api-key]
             [--anthropic-api-key] [--openai-api-base]
             [--openai-api-type] [--openai-api-version]
             [--openai-api-deployment-id] [--openai-organization-id]
             [--set-env] [--api-key] [--list-models]
             [--model-settings-file] [--model-metadata-file]
             [--alias] [--verify-ssl | --no-verify-ssl] [--timeout]
             [--edit-format] [--architect] [--weak-model]
             [--editor-model] [--editor-edit-format]
             [--show-model-warnings | --no-show-model-warnings]
             [--max-chat-history-tokens]
             [--cache-prompts | --no-cache-prompts]
             [--cache-keepalive-pings] [--map-tokens]
             [--map-refresh] [--map-multiplier-no-files]
             [--input-history-file] [--chat-history-file]
             [--restore-chat-history | --no-restore-chat-history]
             [--llm-history-file] [--dark-mode] [--light-mode]
             [--pretty | --no-pretty] [--stream | --no-stream]
             [--user-input-color] [--tool-output-color]
             [--tool-error-color] [--tool-warning-color]
             [--assistant-output-color] [--completion-menu-color]
             [--completion-menu-bg-color]
             [--completion-menu-current-color]
             [--completion-menu-current-bg-color] [--code-theme]
             [--show-diffs] [--git | --no-git]
             [--gitignore | --no-gitignore] [--aiderignore]
             [--subtree-only] [--auto-commits | --no-auto-commits]
             [--dirty-commits | --no-dirty-commits]
             [--attribute-author | --no-attribute-author]
             [--attribute-committer | --no-attribute-committer]
             [--attribute-commit-message-author | --no-attribute-commit-message-author]
             [--attribute-commit-message-committer | --no-attribute-commit-message-committer]
             [--commit] [--commit-prompt] [--dry-run | --no-dry-run]
             [--skip-sanity-check-repo]
             [--watch-files | --no-watch-files] [--lint]
             [--lint-cmd] [--auto-lint | --no-auto-lint]
             [--test-cmd] [--auto-test | --no-auto-test] [--test]
             [--analytics | --no-analytics] [--analytics-log]
             [--analytics-disable] [--just-check-update]
             [--check-update | --no-check-update]
             [--show-release-notes | --no-show-release-notes]
             [--install-main-branch] [--upgrade] [--version]
             [--message] [--message-file]
             [--gui | --no-gui | --browser | --no-browser]
             [--copy-paste | --no-copy-paste] [--apply]
             [--apply-clipboard-edits] [--exit] [--show-repo-map]
             [--show-prompts] [--voice-format] [--voice-language]
             [--voice-input-device] [--file] [--read] [--vim]
             [--chat-language] [--yes-always] [-v] [--load]
             [--encoding] [-c] [--env-file]
             [--suggest-shell-commands | --no-suggest-shell-commands]
             [--fancy-input | --no-fancy-input]
             [--multiline | --no-multiline]
             [--detect-urls | --no-detect-urls] [--editor]

options:
--help
show this help message and exit
Aliases:

-h
--help

Main model:
--model MODEL
Specify the model to use for the main chat
Environment variable: AIDER_MODEL

--opus
Use claude-3-opus-20240229 model for the main chat
Environment variable: AIDER_OPUS

--sonnet
Use claude-3-5-sonnet-20241022 model for the main chat
Environment variable: AIDER_SONNET

--haiku
Use claude-3-5-haiku-20241022 model for the main chat
Environment variable: AIDER_HAIKU

--4
Use gpt-4-0613 model for the main chat
Environment variable: AIDER_4
Aliases:

--4
-4
--4o
Use gpt-4o model for the main chat
Environment variable: AIDER_4O

--mini
Use gpt-4o-mini model for the main chat
Environment variable: AIDER_MINI

--4-turbo
Use gpt-4-1106-preview model for the main chat
Environment variable: AIDER_4_TURBO

--35turbo
Use gpt-3.5-turbo model for the main chat
Environment variable: AIDER_35TURBO
Aliases:

--35turbo
--35-turbo
--3
-3
--deepseek
Use deepseek/deepseek-chat model for the main chat
Environment variable: AIDER_DEEPSEEK

--o1-mini
Use o1-mini model for the main chat
Environment variable: AIDER_O1_MINI

--o1-preview
Use o1-preview model for the main chat
Environment variable: AIDER_O1_PREVIEW

API Keys and settings:
--openai-api-key VALUE
Specify the OpenAI API key
Environment variable: AIDER_OPENAI_API_KEY

--anthropic-api-key VALUE
Specify the Anthropic API key
Environment variable: AIDER_ANTHROPIC_API_KEY

--openai-api-base VALUE
Specify the api base url
Environment variable: AIDER_OPENAI_API_BASE

--openai-api-type VALUE
(deprecated, use –set-env OPENAI_API_TYPE=) Environment variable: `AIDER_OPENAI_API_TYPE`

--openai-api-version VALUE
(deprecated, use –set-env OPENAI_API_VERSION=) Environment variable: `AIDER_OPENAI_API_VERSION`

--openai-api-deployment-id VALUE
(deprecated, use –set-env OPENAI_API_DEPLOYMENT_ID=) Environment variable: `AIDER_OPENAI_API_DEPLOYMENT_ID`

--openai-organization-id VALUE
(deprecated, use –set-env OPENAI_ORGANIZATION=) Environment variable: `AIDER_OPENAI_ORGANIZATION_ID`

--set-env ENV_VAR_NAME=value
Set an environment variable (to control API settings, can be used multiple times)
Default: []
Environment variable: AIDER_SET_ENV

--api-key PROVIDER=KEY
Set an API key for a provider (eg: –api-key provider= sets PROVIDER_API_KEY=) Default: [] Environment variable: `AIDER_API_KEY`

Model settings:
--list-models MODEL
List known models which match the (partial) MODEL name
Environment variable: AIDER_LIST_MODELS
Aliases:

--list-models MODEL
--models MODEL
--model-settings-file MODEL_SETTINGS_FILE
Specify a file with aider model settings for unknown models
Default: .aider.model.settings.yml
Environment variable: AIDER_MODEL_SETTINGS_FILE

--model-metadata-file MODEL_METADATA_FILE
Specify a file with context window and costs for unknown models
Default: .aider.model.metadata.json
Environment variable: AIDER_MODEL_METADATA_FILE

--alias ALIAS:MODEL
Add a model alias (can be used multiple times)
Environment variable: AIDER_ALIAS

--verify-ssl
Verify the SSL cert when connecting to models (default: True)
Default: True
Environment variable: AIDER_VERIFY_SSL
Aliases:

--verify-ssl
--no-verify-ssl
--timeout VALUE
Timeout in seconds for API calls (default: None)
Environment variable: AIDER_TIMEOUT

--edit-format EDIT_FORMAT
Specify what edit format the LLM should use (default depends on model)
Environment variable: AIDER_EDIT_FORMAT
Aliases:

--edit-format EDIT_FORMAT
--chat-mode EDIT_FORMAT
--architect
Use architect edit format for the main chat
Environment variable: AIDER_ARCHITECT

--weak-model WEAK_MODEL
Specify the model to use for commit messages and chat history summarization (default depends on –model)
Environment variable: AIDER_WEAK_MODEL

--editor-model EDITOR_MODEL
Specify the model to use for editor tasks (default depends on –model)
Environment variable: AIDER_EDITOR_MODEL

--editor-edit-format EDITOR_EDIT_FORMAT
Specify the edit format for the editor model (default: depends on editor model)
Environment variable: AIDER_EDITOR_EDIT_FORMAT

--show-model-warnings
Only work with models that have meta-data available (default: True)
Default: True
Environment variable: AIDER_SHOW_MODEL_WARNINGS
Aliases:

--show-model-warnings
--no-show-model-warnings
--max-chat-history-tokens VALUE
Soft limit on tokens for chat history, after which summarization begins. If unspecified, defaults to the model's max_chat_history_tokens.
Environment variable: AIDER_MAX_CHAT_HISTORY_TOKENS

Cache settings:
--cache-prompts
Enable caching of prompts (default: False)
Default: False
Environment variable: AIDER_CACHE_PROMPTS
Aliases:

--cache-prompts
--no-cache-prompts
--cache-keepalive-pings VALUE
Number of times to ping at 5min intervals to keep prompt cache warm (default: 0)
Default: 0
Environment variable: AIDER_CACHE_KEEPALIVE_PINGS

Repomap settings:
--map-tokens VALUE
Suggested number of tokens to use for repo map, use 0 to disable (default: 1024)
Environment variable: AIDER_MAP_TOKENS

--map-refresh VALUE
Control how often the repo map is refreshed. Options: auto, always, files, manual (default: auto)
Default: auto
Environment variable: AIDER_MAP_REFRESH

--map-multiplier-no-files VALUE
Multiplier for map tokens when no files are specified (default: 2)
Default: 2
Environment variable: AIDER_MAP_MULTIPLIER_NO_FILES

History Files:
--input-history-file INPUT_HISTORY_FILE
Specify the chat input history file (default: .aider.input.history)
Default: .aider.input.history
Environment variable: AIDER_INPUT_HISTORY_FILE

--chat-history-file CHAT_HISTORY_FILE
Specify the chat history file (default: .aider.chat.history.md)
Default: .aider.chat.history.md
Environment variable: AIDER_CHAT_HISTORY_FILE

--restore-chat-history
Restore the previous chat history messages (default: False)
Default: False
Environment variable: AIDER_RESTORE_CHAT_HISTORY
Aliases:

--restore-chat-history
--no-restore-chat-history
--llm-history-file LLM_HISTORY_FILE
Log the conversation with the LLM to this file (for example, .aider.llm.history)
Environment variable: AIDER_LLM_HISTORY_FILE

Output settings:
--dark-mode
Use colors suitable for a dark terminal background (default: False)
Default: False
Environment variable: AIDER_DARK_MODE

--light-mode
Use colors suitable for a light terminal background (default: False)
Default: False
Environment variable: AIDER_LIGHT_MODE

--pretty
Enable/disable pretty, colorized output (default: True)
Default: True
Environment variable: AIDER_PRETTY
Aliases:

--pretty
--no-pretty
--stream
Enable/disable streaming responses (default: True)
Default: True
Environment variable: AIDER_STREAM
Aliases:

--stream
--no-stream
--user-input-color VALUE
Set the color for user input (default: #00cc00)
Default: #00cc00
Environment variable: AIDER_USER_INPUT_COLOR

--tool-output-color VALUE
Set the color for tool output (default: None)
Environment variable: AIDER_TOOL_OUTPUT_COLOR

--tool-error-color VALUE
Set the color for tool error messages (default: #FF2222)
Default: #FF2222
Environment variable: AIDER_TOOL_ERROR_COLOR

--tool-warning-color VALUE
Set the color for tool warning messages (default: #FFA500)
Default: #FFA500
Environment variable: AIDER_TOOL_WARNING_COLOR

--assistant-output-color VALUE
Set the color for assistant output (default: #0088ff)
Default: #0088ff
Environment variable: AIDER_ASSISTANT_OUTPUT_COLOR

--completion-menu-color COLOR
Set the color for the completion menu (default: terminal's default text color)
Environment variable: AIDER_COMPLETION_MENU_COLOR

--completion-menu-bg-color COLOR
Set the background color for the completion menu (default: terminal's default background color)
Environment variable: AIDER_COMPLETION_MENU_BG_COLOR

--completion-menu-current-color COLOR
Set the color for the current item in the completion menu (default: terminal's default background color)
Environment variable: AIDER_COMPLETION_MENU_CURRENT_COLOR

--completion-menu-current-bg-color COLOR
Set the background color for the current item in the completion menu (default: terminal's default text color)
Environment variable: AIDER_COMPLETION_MENU_CURRENT_BG_COLOR

--code-theme VALUE
Set the markdown code theme (default: default, other options include monokai, solarized-dark, solarized-light, or a Pygments builtin style, see https://pygments.org/styles for available themes)
Default: default
Environment variable: AIDER_CODE_THEME

--show-diffs
Show diffs when committing changes (default: False)
Default: False
Environment variable: AIDER_SHOW_DIFFS

Git settings:
--git
Enable/disable looking for a git repo (default: True)
Default: True
Environment variable: AIDER_GIT
Aliases:

--git
--no-git
--gitignore
Enable/disable adding .aider* to .gitignore (default: True)
Default: True
Environment variable: AIDER_GITIGNORE
Aliases:

--gitignore
--no-gitignore
--aiderignore AIDERIGNORE
Specify the aider ignore file (default: .aiderignore in git root)
Default: .aiderignore
Environment variable: AIDER_AIDERIGNORE

--subtree-only
Only consider files in the current subtree of the git repository
Default: False
Environment variable: AIDER_SUBTREE_ONLY

--auto-commits
Enable/disable auto commit of LLM changes (default: True)
Default: True
Environment variable: AIDER_AUTO_COMMITS
Aliases:

--auto-commits
--no-auto-commits
--dirty-commits
Enable/disable commits when repo is found dirty (default: True)
Default: True
Environment variable: AIDER_DIRTY_COMMITS
Aliases:

--dirty-commits
--no-dirty-commits
--attribute-author
Attribute aider code changes in the git author name (default: True)
Default: True
Environment variable: AIDER_ATTRIBUTE_AUTHOR
Aliases:

--attribute-author
--no-attribute-author
--attribute-committer
Attribute aider commits in the git committer name (default: True)
Default: True
Environment variable: AIDER_ATTRIBUTE_COMMITTER
Aliases:

--attribute-committer
--no-attribute-committer
--attribute-commit-message-author
Prefix commit messages with 'aider: ' if aider authored the changes (default: False)
Default: False
Environment variable: AIDER_ATTRIBUTE_COMMIT_MESSAGE_AUTHOR
Aliases:

--attribute-commit-message-author
--no-attribute-commit-message-author
--attribute-commit-message-committer
Prefix all commit messages with 'aider: ' (default: False)
Default: False
Environment variable: AIDER_ATTRIBUTE_COMMIT_MESSAGE_COMMITTER
Aliases:

--attribute-commit-message-committer
--no-attribute-commit-message-committer
--commit
Commit all pending changes with a suitable commit message, then exit
Default: False
Environment variable: AIDER_COMMIT

--commit-prompt PROMPT
Specify a custom prompt for generating commit messages
Environment variable: AIDER_COMMIT_PROMPT

--dry-run
Perform a dry run without modifying files (default: False)
Default: False
Environment variable: AIDER_DRY_RUN
Aliases:

--dry-run
--no-dry-run
--skip-sanity-check-repo
Skip the sanity check for the git repository (default: False)
Default: False
Environment variable: AIDER_SKIP_SANITY_CHECK_REPO

--watch-files
Enable/disable watching files for ai coding comments (default: False)
Default: False
Environment variable: AIDER_WATCH_FILES
Aliases:

--watch-files
--no-watch-files
Fixing and committing:
--lint
Lint and fix provided files, or dirty files if none provided
Default: False
Environment variable: AIDER_LINT

--lint-cmd
Specify lint commands to run for different languages, eg: "python: flake8 –select=…" (can be used multiple times)
Default: []
Environment variable: AIDER_LINT_CMD

--auto-lint
Enable/disable automatic linting after changes (default: True)
Default: True
Environment variable: AIDER_AUTO_LINT
Aliases:

--auto-lint
--no-auto-lint
--test-cmd VALUE
Specify command to run tests
Default: []
Environment variable: AIDER_TEST_CMD

--auto-test
Enable/disable automatic testing after changes (default: False)
Default: False
Environment variable: AIDER_AUTO_TEST
Aliases:

--auto-test
--no-auto-test
--test
Run tests, fix problems found and then exit
Default: False
Environment variable: AIDER_TEST

Analytics:
--analytics
Enable/disable analytics for current session (default: random)
Environment variable: AIDER_ANALYTICS
Aliases:

--analytics
--no-analytics
--analytics-log ANALYTICS_LOG_FILE
Specify a file to log analytics events
Environment variable: AIDER_ANALYTICS_LOG

--analytics-disable
Permanently disable analytics
Default: False
Environment variable: AIDER_ANALYTICS_DISABLE

Upgrading:
--just-check-update
Check for updates and return status in the exit code
Default: False
Environment variable: AIDER_JUST_CHECK_UPDATE

--check-update
Check for new aider versions on launch
Default: True
Environment variable: AIDER_CHECK_UPDATE
Aliases:

--check-update
--no-check-update
--show-release-notes
Show release notes on first run of new version (default: None, ask user)
Environment variable: AIDER_SHOW_RELEASE_NOTES
Aliases:

--show-release-notes
--no-show-release-notes
--install-main-branch
Install the latest version from the main branch
Default: False
Environment variable: AIDER_INSTALL_MAIN_BRANCH

--upgrade
Upgrade aider to the latest version from PyPI
Default: False
Environment variable: AIDER_UPGRADE
Aliases:

--upgrade
--update
--version
Show the version number and exit

Modes:
--message COMMAND
Specify a single message to send the LLM, process reply then exit (disables chat mode)
Environment variable: AIDER_MESSAGE
Aliases:

--message COMMAND
--msg COMMAND
-m COMMAND
--message-file MESSAGE_FILE
Specify a file containing the message to send the LLM, process reply, then exit (disables chat mode)
Environment variable: AIDER_MESSAGE_FILE
Aliases:

--message-file MESSAGE_FILE
-f MESSAGE_FILE
--gui
Run aider in your browser (default: False)
Default: False
Environment variable: AIDER_GUI
Aliases:

--gui
--no-gui
--browser
--no-browser
--copy-paste
Enable automatic copy/paste of chat between aider and web UI (default: False)
Default: False
Environment variable: AIDER_COPY_PASTE
Aliases:

--copy-paste
--no-copy-paste
--apply FILE
Apply the changes from the given file instead of running the chat (debug)
Environment variable: AIDER_APPLY

--apply-clipboard-edits
Apply clipboard contents as edits using the main model's editor format
Default: False
Environment variable: AIDER_APPLY_CLIPBOARD_EDITS

--exit
Do all startup activities then exit before accepting user input (debug)
Default: False
Environment variable: AIDER_EXIT

--show-repo-map
Print the repo map and exit (debug)
Default: False
Environment variable: AIDER_SHOW_REPO_MAP

--show-prompts
Print the system prompts and exit (debug)
Default: False
Environment variable: AIDER_SHOW_PROMPTS

Voice settings:
--voice-format VOICE_FORMAT
Audio format for voice recording (default: wav). webm and mp3 require ffmpeg
Default: wav
Environment variable: AIDER_VOICE_FORMAT

--voice-language VOICE_LANGUAGE
Specify the language for voice using ISO 639-1 code (default: auto)
Default: en
Environment variable: AIDER_VOICE_LANGUAGE

--voice-input-device VOICE_INPUT_DEVICE
Specify the input device name for voice recording
Environment variable: AIDER_VOICE_INPUT_DEVICE

Other settings:
--file FILE
specify a file to edit (can be used multiple times)
Environment variable: AIDER_FILE

--read FILE
specify a read-only file (can be used multiple times)
Environment variable: AIDER_READ

--vim
Use VI editing mode in the terminal (default: False)
Default: False
Environment variable: AIDER_VIM

--chat-language CHAT_LANGUAGE
Specify the language to use in the chat (default: None, uses system settings)
Environment variable: AIDER_CHAT_LANGUAGE

--yes-always
Always say yes to every confirmation
Environment variable: AIDER_YES_ALWAYS

--verbose
Enable verbose output
Default: False
Environment variable: AIDER_VERBOSE
Aliases:

-v
--verbose
--load LOAD_FILE
Load and execute /commands from a file on launch
Environment variable: AIDER_LOAD

--encoding VALUE
Specify the encoding for input and output (default: utf-8)
Default: utf-8
Environment variable: AIDER_ENCODING

--config CONFIG_FILE
Specify the config file (default: search for .aider.conf.yml in git root, cwd or home directory)
Aliases:

-c CONFIG_FILE
--config CONFIG_FILE
--env-file ENV_FILE
Specify the .env file to load (default: .env in git root)
Default: .env
Environment variable: AIDER_ENV_FILE

--suggest-shell-commands
Enable/disable suggesting shell commands (default: True)
Default: True
Environment variable: AIDER_SUGGEST_SHELL_COMMANDS
Aliases:

--suggest-shell-commands
--no-suggest-shell-commands
--fancy-input
Enable/disable fancy input with history and completion (default: True)
Default: True
Environment variable: AIDER_FANCY_INPUT
Aliases:

--fancy-input
--no-fancy-input
--multiline
Enable/disable multi-line input mode with Meta-Enter to submit (default: False)
Default: False
Environment variable: AIDER_MULTILINE
Aliases:

--multiline
--no-multiline
--detect-urls
Enable/disable detection and offering to add URLs to chat (default: True)
Default: True
Environment variable: AIDER_DETECT_URLS
Aliases:

--detect-urls
--no-detect-urls
--editor VALUE
Specify which editor to use for the /editor command
Environment variable: AIDER_EDITOR

YAML config file
Most of aider's options can be set in an .aider.conf.yml file. Aider will look for a this file in these locations and load whichever is found first.

- As specified with the --config <filename> parameter.
- The current directory.
- The root of your git repo.
- Your home directory.

TIP
See the API key configuration docs for information on how to configure and store your API keys.

A note on lists
Lists of values can be specified either as a bulleted list:

read:
  - CONVENTIONS.md
  - anotherfile.txt
  - thirdfile.py

Or lists can be specified using commas and square brackets:

read: [CONVENTIONS.md, anotherfile.txt, thirdfile.py]

Sample YAML config file
Below is a sample of the YAML config file, which you can also download from GitHub [https://github.com/Aider-AI/aider/blob/main/aider/website/assets/sample.aider.conf.yml] 

##########################################################
# Sample .aider.conf.yml
# This file lists *all* the valid configuration entries.
# Place in your home dir, or at the root of your git repo.
##########################################################

# Note: You can only put OpenAI and Anthropic API keys in the yaml
# config file. Keys for all APIs can be stored in a .env file
# https://aider.chat/docs/config/dotenv.html

##########
# options:

## show this help message and exit
#help: xxx

#############
# Main model:

## Specify the model to use for the main chat
#model: xxx

## Use claude-3-opus-20240229 model for the main chat
#opus: false

## Use claude-3-5-sonnet-20241022 model for the main chat
#sonnet: false

## Use claude-3-5-haiku-20241022 model for the main chat
#haiku: false

## Use gpt-4-0613 model for the main chat
#4: false

## Use gpt-4o model for the main chat
#4o: false

## Use gpt-4o-mini model for the main chat
#mini: false

## Use gpt-4-1106-preview model for the main chat
#4-turbo: false

## Use gpt-3.5-turbo model for the main chat
#35turbo: false

## Use deepseek/deepseek-chat model for the main chat
#deepseek: false

## Use o1-mini model for the main chat
#o1-mini: false

## Use o1-preview model for the main chat
#o1-preview: false

########################
# API Keys and settings:

## Specify the OpenAI API key
#openai-api-key: xxx

## Specify the Anthropic API key
#anthropic-api-key: xxx

## Specify the api base url
#openai-api-base: xxx

## (deprecated, use --set-env OPENAI_API_TYPE=<value>)
#openai-api-type: xxx

## (deprecated, use --set-env OPENAI_API_VERSION=<value>)
#openai-api-version: xxx

## (deprecated, use --set-env OPENAI_API_DEPLOYMENT_ID=<value>)
#openai-api-deployment-id: xxx

## (deprecated, use --set-env OPENAI_ORGANIZATION=<value>)
#openai-organization-id: xxx

## Set an environment variable (to control API settings, can be used multiple times)
#set-env: xxx
## Specify multiple values like this:
#set-env:
#  - xxx
#  - yyy
#  - zzz

## Set an API key for a provider (eg: --api-key provider=<key> sets PROVIDER_API_KEY=<key>)
#api-key: xxx
## Specify multiple values like this:
#api-key:
#  - xxx
#  - yyy
#  - zzz

#################
# Model settings:

## List known models which match the (partial) MODEL name
#list-models: xxx

## Specify a file with aider model settings for unknown models
#model-settings-file: .aider.model.settings.yml

## Specify a file with context window and costs for unknown models
#model-metadata-file: .aider.model.metadata.json

## Add a model alias (can be used multiple times)
#alias: xxx
## Specify multiple values like this:
#alias:
#  - xxx
#  - yyy
#  - zzz

## Verify the SSL cert when connecting to models (default: True)
#verify-ssl: true

## Timeout in seconds for API calls (default: None)
#timeout: xxx

## Specify what edit format the LLM should use (default depends on model)
#edit-format: xxx

## Use architect edit format for the main chat
#architect: false

## Specify the model to use for commit messages and chat history summarization (default depends on --model)
#weak-model: xxx

## Specify the model to use for editor tasks (default depends on --model)
#editor-model: xxx

## Specify the edit format for the editor model (default: depends on editor model)
#editor-edit-format: xxx

## Only work with models that have meta-data available (default: True)
#show-model-warnings: true

## Soft limit on tokens for chat history, after which summarization begins. If unspecified, defaults to the model's max_chat_history_tokens.
#max-chat-history-tokens: xxx

#################
# Cache settings:

## Enable caching of prompts (default: False)
#cache-prompts: false

## Number of times to ping at 5min intervals to keep prompt cache warm (default: 0)
#cache-keepalive-pings: false

###################
# Repomap settings:

## Suggested number of tokens to use for repo map, use 0 to disable (default: 1024)
#map-tokens: xxx

## Control how often the repo map is refreshed. Options: auto, always, files, manual (default: auto)
#map-refresh: auto

## Multiplier for map tokens when no files are specified (default: 2)
#map-multiplier-no-files: true

################
# History Files:

## Specify the chat input history file (default: .aider.input.history)
#input-history-file: .aider.input.history

## Specify the chat history file (default: .aider.chat.history.md)
#chat-history-file: .aider.chat.history.md

## Restore the previous chat history messages (default: False)
#restore-chat-history: false

## Log the conversation with the LLM to this file (for example, .aider.llm.history)
#llm-history-file: xxx

##################
# Output settings:

## Use colors suitable for a dark terminal background (default: False)
#dark-mode: false

## Use colors suitable for a light terminal background (default: False)
#light-mode: false

## Enable/disable pretty, colorized output (default: True)
#pretty: true

## Enable/disable streaming responses (default: True)
#stream: true

## Set the color for user input (default: #00cc00)
#user-input-color: #00cc00

## Set the color for tool output (default: None)
#tool-output-color: xxx

## Set the color for tool error messages (default: #FF2222)
#tool-error-color: #FF2222

## Set the color for tool warning messages (default: #FFA500)
#tool-warning-color: #FFA500

## Set the color for assistant output (default: #0088ff)
#assistant-output-color: #0088ff

## Set the color for the completion menu (default: terminal's default text color)
#completion-menu-color: xxx

## Set the background color for the completion menu (default: terminal's default background color)
#completion-menu-bg-color: xxx

## Set the color for the current item in the completion menu (default: terminal's default background color)
#completion-menu-current-color: xxx

## Set the background color for the current item in the completion menu (default: terminal's default text color)
#completion-menu-current-bg-color: xxx

## Set the markdown code theme (default: default, other options include monokai, solarized-dark, solarized-light, or a Pygments builtin style, see https://pygments.org/styles for available themes)
#code-theme: default

## Show diffs when committing changes (default: False)
#show-diffs: false

###############
# Git settings:

## Enable/disable looking for a git repo (default: True)
#git: true

## Enable/disable adding .aider* to .gitignore (default: True)
#gitignore: true

## Specify the aider ignore file (default: .aiderignore in git root)
#aiderignore: .aiderignore

## Only consider files in the current subtree of the git repository
#subtree-only: false

## Enable/disable auto commit of LLM changes (default: True)
#auto-commits: true

## Enable/disable commits when repo is found dirty (default: True)
#dirty-commits: true

## Attribute aider code changes in the git author name (default: True)
#attribute-author: true

## Attribute aider commits in the git committer name (default: True)
#attribute-committer: true

## Prefix commit messages with 'aider: ' if aider authored the changes (default: False)
#attribute-commit-message-author: false

## Prefix all commit messages with 'aider: ' (default: False)
#attribute-commit-message-committer: false

## Commit all pending changes with a suitable commit message, then exit
#commit: false

## Specify a custom prompt for generating commit messages
#commit-prompt: xxx

## Perform a dry run without modifying files (default: False)
#dry-run: false

## Skip the sanity check for the git repository (default: False)
#skip-sanity-check-repo: false

## Enable/disable watching files for ai coding comments (default: False)
#watch-files: false

########################
# Fixing and committing:

## Lint and fix provided files, or dirty files if none provided
#lint: false

## Specify lint commands to run for different languages, eg: "python: flake8 --select=..." (can be used multiple times)
#lint-cmd: xxx
## Specify multiple values like this:
#lint-cmd:
#  - xxx
#  - yyy
#  - zzz

## Enable/disable automatic linting after changes (default: True)
#auto-lint: true

## Specify command to run tests
#test-cmd: xxx

## Enable/disable automatic testing after changes (default: False)
#auto-test: false

## Run tests, fix problems found and then exit
#test: false

############
# Analytics:

## Enable/disable analytics for current session (default: random)
#analytics: xxx

## Specify a file to log analytics events
#analytics-log: xxx

## Permanently disable analytics
#analytics-disable: false

############
# Upgrading:

## Check for updates and return status in the exit code
#just-check-update: false

## Check for new aider versions on launch
#check-update: true

## Show release notes on first run of new version (default: None, ask user)
#show-release-notes: xxx

## Install the latest version from the main branch
#install-main-branch: false

## Upgrade aider to the latest version from PyPI
#upgrade: false

## Show the version number and exit
#version: xxx

########
# Modes:

## Specify a single message to send the LLM, process reply then exit (disables chat mode)
#message: xxx

## Specify a file containing the message to send the LLM, process reply, then exit (disables chat mode)
#message-file: xxx

## Run aider in your browser (default: False)
#gui: false

## Enable automatic copy/paste of chat between aider and web UI (default: False)
#copy-paste: false

## Apply the changes from the given file instead of running the chat (debug)
#apply: xxx

## Apply clipboard contents as edits using the main model's editor format
#apply-clipboard-edits: false

## Do all startup activities then exit before accepting user input (debug)
#exit: false

## Print the repo map and exit (debug)
#show-repo-map: false

## Print the system prompts and exit (debug)
#show-prompts: false

#################
# Voice settings:

## Audio format for voice recording (default: wav). webm and mp3 require ffmpeg
#voice-format: wav

## Specify the language for voice using ISO 639-1 code (default: auto)
#voice-language: en

## Specify the input device name for voice recording
#voice-input-device: xxx

#################
# Other settings:

## specify a file to edit (can be used multiple times)
#file: xxx
## Specify multiple values like this:
#file:
#  - xxx
#  - yyy
#  - zzz

## specify a read-only file (can be used multiple times)
#read: xxx
## Specify multiple values like this:
#read:
#  - xxx
#  - yyy
#  - zzz

## Use VI editing mode in the terminal (default: False)
#vim: false

## Specify the language to use in the chat (default: None, uses system settings)
#chat-language: xxx

## Always say yes to every confirmation
#yes-always: false

## Enable verbose output
#verbose: false

## Load and execute /commands from a file on launch
#load: xxx

## Specify the encoding for input and output (default: utf-8)
#encoding: utf-8

## Specify the config file (default: search for .aider.conf.yml in git root, cwd or home directory)
#config: xxx

## Specify the .env file to load (default: .env in git root)
#env-file: .env

## Enable/disable suggesting shell commands (default: True)
#suggest-shell-commands: true

## Enable/disable fancy input with history and completion (default: True)
#fancy-input: true

## Enable/disable multi-line input mode with Meta-Enter to submit (default: False)
#multiline: false

## Enable/disable detection and offering to add URLs to chat (default: True)
#detect-urls: true

## Specify which editor to use for the /editor command
#editor: xxx

Config with .env
You can use a .env file to store API keys and other settings for the models you use with aider. You can also set many general aider options in the .env file.

Aider will look for a .env file in these locations:

- Your home directory.
- The root of your git repo.
- The current directory.
- As specified with the --env-file <filename> parameter.

If the files above exist, they will be loaded in that order. Files loaded last will take priority.

TIP 
See the API key configuration docs for information on how to configure and store your API keys.

Sample .env file
Below is a sample .env file, which you can also download from GitHub [https://github.com/Aider-AI/aider/blob/main/aider/website/assets/sample.env] 

##########################################################
# Sample aider .env file.
# Place at the root of your git repo.
# Or use `aider --env <fname>` to specify.
##########################################################

#################
# LLM parameters:
#
# Include xxx_API_KEY parameters and other params needed for your LLMs.
# See https://aider.chat/docs/llms.html for details.

## OpenAI
#OPENAI_API_KEY=

## Anthropic
#ANTHROPIC_API_KEY=

##...

#############
# Main model:

## Specify the model to use for the main chat
#AIDER_MODEL=

## Use claude-3-opus-20240229 model for the main chat
#AIDER_OPUS=

## Use claude-3-5-sonnet-20241022 model for the main chat
#AIDER_SONNET=

## Use claude-3-5-haiku-20241022 model for the main chat
#AIDER_HAIKU=

## Use gpt-4-0613 model for the main chat
#AIDER_4=

## Use gpt-4o model for the main chat
#AIDER_4O=

## Use gpt-4o-mini model for the main chat
#AIDER_MINI=

## Use gpt-4-1106-preview model for the main chat
#AIDER_4_TURBO=

## Use gpt-3.5-turbo model for the main chat
#AIDER_35TURBO=

## Use deepseek/deepseek-chat model for the main chat
#AIDER_DEEPSEEK=

## Use o1-mini model for the main chat
#AIDER_O1_MINI=

## Use o1-preview model for the main chat
#AIDER_O1_PREVIEW=

########################
# API Keys and settings:

## Specify the OpenAI API key
#AIDER_OPENAI_API_KEY=

## Specify the Anthropic API key
#AIDER_ANTHROPIC_API_KEY=

## Specify the api base url
#AIDER_OPENAI_API_BASE=

## (deprecated, use --set-env OPENAI_API_TYPE=<value>)
#AIDER_OPENAI_API_TYPE=

## (deprecated, use --set-env OPENAI_API_VERSION=<value>)
#AIDER_OPENAI_API_VERSION=

## (deprecated, use --set-env OPENAI_API_DEPLOYMENT_ID=<value>)
#AIDER_OPENAI_API_DEPLOYMENT_ID=

## (deprecated, use --set-env OPENAI_ORGANIZATION=<value>)
#AIDER_OPENAI_ORGANIZATION_ID=

## Set an environment variable (to control API settings, can be used multiple times)
#AIDER_SET_ENV=

## Set an API key for a provider (eg: --api-key provider=<key> sets PROVIDER_API_KEY=<key>)
#AIDER_API_KEY=

#################
# Model settings:

## List known models which match the (partial) MODEL name
#AIDER_LIST_MODELS=

## Specify a file with aider model settings for unknown models
#AIDER_MODEL_SETTINGS_FILE=.aider.model.settings.yml

## Specify a file with context window and costs for unknown models
#AIDER_MODEL_METADATA_FILE=.aider.model.metadata.json

## Add a model alias (can be used multiple times)
#AIDER_ALIAS=

## Verify the SSL cert when connecting to models (default: True)
#AIDER_VERIFY_SSL=true

## Timeout in seconds for API calls (default: None)
#AIDER_TIMEOUT=

## Specify what edit format the LLM should use (default depends on model)
#AIDER_EDIT_FORMAT=

## Use architect edit format for the main chat
#AIDER_ARCHITECT=

## Specify the model to use for commit messages and chat history summarization (default depends on --model)
#AIDER_WEAK_MODEL=

## Specify the model to use for editor tasks (default depends on --model)
#AIDER_EDITOR_MODEL=

## Specify the edit format for the editor model (default: depends on editor model)
#AIDER_EDITOR_EDIT_FORMAT=

## Only work with models that have meta-data available (default: True)
#AIDER_SHOW_MODEL_WARNINGS=true

## Soft limit on tokens for chat history, after which summarization begins. If unspecified, defaults to the model's max_chat_history_tokens.
#AIDER_MAX_CHAT_HISTORY_TOKENS=

#################
# Cache settings:

## Enable caching of prompts (default: False)
#AIDER_CACHE_PROMPTS=false

## Number of times to ping at 5min intervals to keep prompt cache warm (default: 0)
#AIDER_CACHE_KEEPALIVE_PINGS=false

###################
# Repomap settings:

## Suggested number of tokens to use for repo map, use 0 to disable (default: 1024)
#AIDER_MAP_TOKENS=

## Control how often the repo map is refreshed. Options: auto, always, files, manual (default: auto)
#AIDER_MAP_REFRESH=auto

## Multiplier for map tokens when no files are specified (default: 2)
#AIDER_MAP_MULTIPLIER_NO_FILES=true

################
# History Files:

## Specify the chat input history file (default: .aider.input.history)
#AIDER_INPUT_HISTORY_FILE=.aider.input.history

## Specify the chat history file (default: .aider.chat.history.md)
#AIDER_CHAT_HISTORY_FILE=.aider.chat.history.md

## Restore the previous chat history messages (default: False)
#AIDER_RESTORE_CHAT_HISTORY=false

## Log the conversation with the LLM to this file (for example, .aider.llm.history)
#AIDER_LLM_HISTORY_FILE=

##################
# Output settings:

## Use colors suitable for a dark terminal background (default: False)
#AIDER_DARK_MODE=false

## Use colors suitable for a light terminal background (default: False)
#AIDER_LIGHT_MODE=false

## Enable/disable pretty, colorized output (default: True)
#AIDER_PRETTY=true

## Enable/disable streaming responses (default: True)
#AIDER_STREAM=true

## Set the color for user input (default: #00cc00)
#AIDER_USER_INPUT_COLOR=#00cc00

## Set the color for tool output (default: None)
#AIDER_TOOL_OUTPUT_COLOR=

## Set the color for tool error messages (default: #FF2222)
#AIDER_TOOL_ERROR_COLOR=#FF2222

## Set the color for tool warning messages (default: #FFA500)
#AIDER_TOOL_WARNING_COLOR=#FFA500

## Set the color for assistant output (default: #0088ff)
#AIDER_ASSISTANT_OUTPUT_COLOR=#0088ff

## Set the color for the completion menu (default: terminal's default text color)
#AIDER_COMPLETION_MENU_COLOR=

## Set the background color for the completion menu (default: terminal's default background color)
#AIDER_COMPLETION_MENU_BG_COLOR=

## Set the color for the current item in the completion menu (default: terminal's default background color)
#AIDER_COMPLETION_MENU_CURRENT_COLOR=

## Set the background color for the current item in the completion menu (default: terminal's default text color)
#AIDER_COMPLETION_MENU_CURRENT_BG_COLOR=

## Set the markdown code theme (default: default, other options include monokai, solarized-dark, solarized-light, or a Pygments builtin style, see https://pygments.org/styles for available themes)
#AIDER_CODE_THEME=default

## Show diffs when committing changes (default: False)
#AIDER_SHOW_DIFFS=false

###############
# Git settings:

## Enable/disable looking for a git repo (default: True)
#AIDER_GIT=true

## Enable/disable adding .aider* to .gitignore (default: True)
#AIDER_GITIGNORE=true

## Specify the aider ignore file (default: .aiderignore in git root)
#AIDER_AIDERIGNORE=.aiderignore

## Only consider files in the current subtree of the git repository
#AIDER_SUBTREE_ONLY=false

## Enable/disable auto commit of LLM changes (default: True)
#AIDER_AUTO_COMMITS=true

## Enable/disable commits when repo is found dirty (default: True)
#AIDER_DIRTY_COMMITS=true

## Attribute aider code changes in the git author name (default: True)
#AIDER_ATTRIBUTE_AUTHOR=true

## Attribute aider commits in the git committer name (default: True)
#AIDER_ATTRIBUTE_COMMITTER=true

## Prefix commit messages with 'aider: ' if aider authored the changes (default: False)
#AIDER_ATTRIBUTE_COMMIT_MESSAGE_AUTHOR=false

## Prefix all commit messages with 'aider: ' (default: False)
#AIDER_ATTRIBUTE_COMMIT_MESSAGE_COMMITTER=false

## Commit all pending changes with a suitable commit message, then exit
#AIDER_COMMIT=false

## Specify a custom prompt for generating commit messages
#AIDER_COMMIT_PROMPT=

## Perform a dry run without modifying files (default: False)
#AIDER_DRY_RUN=false

## Skip the sanity check for the git repository (default: False)
#AIDER_SKIP_SANITY_CHECK_REPO=false

## Enable/disable watching files for ai coding comments (default: False)
#AIDER_WATCH_FILES=false

########################
# Fixing and committing:

## Lint and fix provided files, or dirty files if none provided
#AIDER_LINT=false

## Specify lint commands to run for different languages, eg: "python: flake8 --select=..." (can be used multiple times)
#AIDER_LINT_CMD=

## Enable/disable automatic linting after changes (default: True)
#AIDER_AUTO_LINT=true

## Specify command to run tests
#AIDER_TEST_CMD=

## Enable/disable automatic testing after changes (default: False)
#AIDER_AUTO_TEST=false

## Run tests, fix problems found and then exit
#AIDER_TEST=false

############
# Analytics:

## Enable/disable analytics for current session (default: random)
#AIDER_ANALYTICS=

## Specify a file to log analytics events
#AIDER_ANALYTICS_LOG=

## Permanently disable analytics
#AIDER_ANALYTICS_DISABLE=false

############
# Upgrading:

## Check for updates and return status in the exit code
#AIDER_JUST_CHECK_UPDATE=false

## Check for new aider versions on launch
#AIDER_CHECK_UPDATE=true

## Show release notes on first run of new version (default: None, ask user)
#AIDER_SHOW_RELEASE_NOTES=

## Install the latest version from the main branch
#AIDER_INSTALL_MAIN_BRANCH=false

## Upgrade aider to the latest version from PyPI
#AIDER_UPGRADE=false

########
# Modes:

## Specify a single message to send the LLM, process reply then exit (disables chat mode)
#AIDER_MESSAGE=

## Specify a file containing the message to send the LLM, process reply, then exit (disables chat mode)
#AIDER_MESSAGE_FILE=

## Run aider in your browser (default: False)
#AIDER_GUI=false

## Enable automatic copy/paste of chat between aider and web UI (default: False)
#AIDER_COPY_PASTE=false

## Apply the changes from the given file instead of running the chat (debug)
#AIDER_APPLY=

## Apply clipboard contents as edits using the main model's editor format
#AIDER_APPLY_CLIPBOARD_EDITS=false

## Do all startup activities then exit before accepting user input (debug)
#AIDER_EXIT=false

## Print the repo map and exit (debug)
#AIDER_SHOW_REPO_MAP=false

## Print the system prompts and exit (debug)
#AIDER_SHOW_PROMPTS=false

#################
# Voice settings:

## Audio format for voice recording (default: wav). webm and mp3 require ffmpeg
#AIDER_VOICE_FORMAT=wav

## Specify the language for voice using ISO 639-1 code (default: auto)
#AIDER_VOICE_LANGUAGE=en

## Specify the input device name for voice recording
#AIDER_VOICE_INPUT_DEVICE=

#################
# Other settings:

## specify a file to edit (can be used multiple times)
#AIDER_FILE=

## specify a read-only file (can be used multiple times)
#AIDER_READ=

## Use VI editing mode in the terminal (default: False)
#AIDER_VIM=false

## Specify the language to use in the chat (default: None, uses system settings)
#AIDER_CHAT_LANGUAGE=

## Always say yes to every confirmation
#AIDER_YES_ALWAYS=

## Enable verbose output
#AIDER_VERBOSE=false

## Load and execute /commands from a file on launch
#AIDER_LOAD=

## Specify the encoding for input and output (default: utf-8)
#AIDER_ENCODING=utf-8

## Specify the .env file to load (default: .env in git root)
#AIDER_ENV_FILE=.env

## Enable/disable suggesting shell commands (default: True)
#AIDER_SUGGEST_SHELL_COMMANDS=true

## Enable/disable fancy input with history and completion (default: True)
#AIDER_FANCY_INPUT=true

## Enable/disable multi-line input mode with Meta-Enter to submit (default: False)
#AIDER_MULTILINE=false

## Enable/disable detection and offering to add URLs to chat (default: True)
#AIDER_DETECT_URLS=true

## Specify which editor to use for the /editor command
#AIDER_EDITOR=

Editor configuration
Aider allows you to configure your preferred text editor for use with the /editor command. The editor must be capable of running in "blocking mode", meaning the command line will wait until you close the editor before proceeding.

Using --editor
You can specify the text editor with the --editor switch or using editor: in aider's yaml config file [https://aider.chat/docs/config/aider_conf.html]. 

Environment variables
Aider checks the following environment variables in order to determine which editor to use:

1. AIDER_EDITOR
2. VISUAL
3. EDITOR

Default behavior
If no editor is configured, aider will use these platform-specific defaults:

- Windows: notepad
- macOS: vim
- Linux/Unix: vi

Using a custom editor
You can set your preferred editor in your shell's configuration file (e.g., .bashrc, .zshrc):

export AIDER_EDITOR=vim

Popular Editors by Platform
macOS

1 vim
export AIDER_EDITOR=vim

2 Emacs
export AIDER_EDITOR=emacs

3 VSCode
export AIDER_EDITOR="code --wait"

4 Sublime Text
export AIDER_EDITOR="subl --wait"

5 BBEdit
export AIDER_EDITOR="bbedit --wait"

Editor command arguments
Some editors require specific command-line arguments to operate in blocking mode. The --wait flag (or equivalent) is commonly used to make the editor block until the file is closed.

Troubleshooting
If you encounter issues with your editor not blocking (returning to the prompt immediately), verify that:

1. Your editor supports blocking mode
2. You've included the necessary command-line arguments for blocking mode
3. The editor command is properly quoted if it contains spaces or special characters, e.g.:
export AIDER_EDITOR="code --wait"

Advanced model settings
Context window size and token costs
In most cases, you can safely ignore aider's warning about unknown context window size and model costs.

NOTE 
In most cases, you can safely ignore aider’s warning about unknown context window size and model costs.

NOTE 
Aider never enforces token limits, it only reports token limit errors from the API provider. You probably don’t need to configure aider with the proper token limits for unusual models.

But, you can register context window limits and costs for models that aren’t known to aider. Create a .aider.model.metadata.json file in one of these locations:

- Your home directory.
- The root if your git repo.
- The current directory where you launch aider.
- Or specify a specific file with the --model-metadata-file <filename> switch.

If the files above exist, they will be loaded in that order. Files loaded last will take priority.

The json file should be a dictionary with an entry for each model, as follows:

{
    "deepseek/deepseek-chat": {
        "max_tokens": 4096,
        "max_input_tokens": 32000,
        "max_output_tokens": 4096,
        "input_cost_per_token": 0.00000014,
        "output_cost_per_token": 0.00000028,
        "litellm_provider": "deepseek",
        "mode": "chat"
    }
}

TIP 
Use a fully qualified model name with a provider/ at the front in the .aider.model.metadata.json file. For example, use deepseek/deepseek-chat, not just deepseek-chat. That prefix should match the litellm_provider field.

Contribute model metadata
Aider relies on litellm’s model_prices_and_context_window.json [https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json] file for model metadata.

Consider submitting a PR to that file to add missing models.

Model settings
Aider has a number of settings that control how it works with different models. These model settings are pre-configured for most popular models. But it can sometimes be helpful to override them or add settings for a model that aider doesn’t know about.

Configuration file locations
You can override or add settings for any model by creating a .aider.model.settings.yml file in one of these locations:

- Your home directory.
- The root if your git repo.
- The current directory where you launch aider.
- Or specify a specific file with the --model-settings-file <filename> switch.

If the files above exist, they will be loaded in that order. Files loaded last will take priority.

The yaml file should be a list of dictionary objects for each model.

Global extra params
You can use the special model name aider/extra_params to define extra_params that will be passed to litellm.completion() for all models. Only the extra_params dict is used from this special model name.

For example:

- name: aider/extra_params
  extra_params:
    extra_headers:
      Custom-Header: value
    max_tokens: 8192

These settings will be merged with any model-specific settings, with the aider/extra_params settings taking precedence for any direct conflicts.

Example model settings
Below are all the pre-configured model settings to give a sense for the settings which are supported.

You can also look at the ModelSettings class in models.py [https://github.com/Aider-AI/aider/blob/main/aider/models.py] file for more details about all of the model setting that aider supports.

- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gpt-3.5-turbo
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gpt-3.5-turbo-0125
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gpt-3.5-turbo-1106
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gpt-3.5-turbo-0613
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gpt-3.5-turbo-16k-0613
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: udiff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: true
  name: gpt-4-turbo-2024-04-09
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: udiff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: true
  name: gpt-4-turbo
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: true
  name: openai/gpt-4o
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: true
  name: openai/gpt-4o-2024-08-06
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: true
  name: gpt-4o-2024-08-06
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: true
  name: gpt-4o-2024-11-20
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: true
  name: openai/gpt-4o-2024-11-20
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: true
  name: gpt-4o
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: true
  name: gpt-4o-mini
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: true
  name: openai/gpt-4o-mini
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: openai/gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: udiff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params: null
  lazy: true
  name: gpt-4-0125-preview
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: udiff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: true
  name: gpt-4-1106-preview
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gpt-4-vision-preview
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params: null
  lazy: false
  name: gpt-4-0314
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gpt-4-0613
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gpt-4-32k-0613
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: claude-3-opus-20240229
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: claude-3-5-haiku-20241022
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: openrouter/anthropic/claude-3-opus
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: openrouter/anthropic/claude-3-5-haiku
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: claude-3-sonnet-20240229
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: claude-3-5-haiku-20241022
- cache_control: true
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: claude-3-5-sonnet-20240620
  examples_as_sys_msg: true
  extra_params:
    extra_headers:
      anthropic-beta: prompt-caching-2024-07-31,pdfs-2024-09-25
    max_tokens: 8192
  lazy: false
  name: claude-3-5-sonnet-20240620
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: claude-3-5-haiku-20241022
- cache_control: true
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: anthropic/claude-3-5-sonnet-20240620
  examples_as_sys_msg: true
  extra_params:
    extra_headers:
      anthropic-beta: prompt-caching-2024-07-31,pdfs-2024-09-25
    max_tokens: 8192
  lazy: false
  name: anthropic/claude-3-5-sonnet-20240620
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: anthropic/claude-3-5-haiku-20241022
- cache_control: true
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: anthropic/claude-3-5-sonnet-20241022
  examples_as_sys_msg: true
  extra_params:
    extra_headers:
      anthropic-beta: prompt-caching-2024-07-31,pdfs-2024-09-25
    max_tokens: 8192
  lazy: false
  name: anthropic/claude-3-5-sonnet-20241022
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: anthropic/claude-3-5-haiku-20241022
- cache_control: true
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: bedrock/anthropic.claude-3-5-sonnet-20241022-v2:0
  examples_as_sys_msg: true
  extra_params:
    extra_headers:
      anthropic-beta: prompt-caching-2024-07-31,pdfs-2024-09-25
    max_tokens: 8192
  lazy: false
  name: bedrock/anthropic.claude-3-5-sonnet-20241022-v2:0
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: bedrock/anthropic.claude-3-5-haiku-20241022-v1:0
- cache_control: true
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: anthropic/claude-3-5-sonnet-20241022
  examples_as_sys_msg: true
  extra_params:
    extra_headers:
      anthropic-beta: prompt-caching-2024-07-31,pdfs-2024-09-25
    max_tokens: 8192
  lazy: false
  name: anthropic/claude-3-5-sonnet-latest
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: anthropic/claude-3-5-haiku-20241022
- cache_control: true
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: claude-3-5-sonnet-20241022
  examples_as_sys_msg: true
  extra_params:
    extra_headers:
      anthropic-beta: prompt-caching-2024-07-31,pdfs-2024-09-25
    max_tokens: 8192
  lazy: false
  name: claude-3-5-sonnet-20241022
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: claude-3-5-haiku-20241022
- cache_control: true
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params:
    extra_headers:
      anthropic-beta: prompt-caching-2024-07-31,pdfs-2024-09-25
  lazy: false
  name: anthropic/claude-3-haiku-20240307
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: anthropic/claude-3-haiku-20240307
- cache_control: true
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params:
    extra_headers:
      anthropic-beta: prompt-caching-2024-07-31,pdfs-2024-09-25
  lazy: false
  name: anthropic/claude-3-5-haiku-20241022
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: anthropic/claude-3-5-haiku-20241022
- cache_control: true
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params:
    extra_headers:
      anthropic-beta: prompt-caching-2024-07-31,pdfs-2024-09-25
  lazy: false
  name: bedrock/anthropic.claude-3-5-haiku-20241022-v1:0
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: bedrock/anthropic.claude-3-5-haiku-20241022-v1:0
- cache_control: true
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params:
    extra_headers:
      anthropic-beta: prompt-caching-2024-07-31,pdfs-2024-09-25
  lazy: false
  name: claude-3-5-haiku-20241022
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: claude-3-5-haiku-20241022
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params:
    max_tokens: 4096
  lazy: false
  name: vertex_ai/claude-3-5-haiku@20241022
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: vertex_ai/claude-3-5-haiku@20241022
- cache_control: true
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params:
    extra_headers:
      anthropic-beta: prompt-caching-2024-07-31,pdfs-2024-09-25
  lazy: false
  name: claude-3-haiku-20240307
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: claude-3-haiku-20240307
- cache_control: true
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: openrouter/anthropic/claude-3.5-sonnet
  examples_as_sys_msg: true
  extra_params:
    max_tokens: 8192
  lazy: false
  name: openrouter/anthropic/claude-3.5-sonnet
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: openrouter/anthropic/claude-3-5-haiku
- cache_control: true
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: openrouter/anthropic/claude-3.5-sonnet:beta
  examples_as_sys_msg: true
  extra_params:
    max_tokens: 8192
  lazy: false
  name: openrouter/anthropic/claude-3.5-sonnet:beta
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: openrouter/anthropic/claude-3-5-haiku:beta
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: vertex_ai/claude-3-5-sonnet@20240620
  examples_as_sys_msg: true
  extra_params:
    max_tokens: 8192
  lazy: false
  name: vertex_ai/claude-3-5-sonnet@20240620
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: vertex_ai/claude-3-5-haiku@20241022
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: vertex_ai/claude-3-5-sonnet-v2@20241022
  examples_as_sys_msg: true
  extra_params:
    max_tokens: 8192
  lazy: false
  name: vertex_ai/claude-3-5-sonnet-v2@20241022
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: vertex_ai/claude-3-5-haiku@20241022
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: vertex_ai/claude-3-opus@20240229
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: vertex_ai/claude-3-5-haiku@20241022
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: vertex_ai/claude-3-sonnet@20240229
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: vertex_ai/claude-3-5-haiku@20241022
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: command-r-plus
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: command-r-plus
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: command-r-08-2024
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: command-r-08-2024
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: command-r-plus-08-2024
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: command-r-plus-08-2024
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params: null
  lazy: false
  name: groq/llama3-70b-8192
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: groq/llama3-8b-8192
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params: null
  lazy: false
  name: openrouter/meta-llama/llama-3-70b-instruct
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: openrouter/meta-llama/llama-3-70b-instruct
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gemini/gemini-1.5-pro-002
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gemini/gemini-1.5-flash-002
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff-fenced
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gemini/gemini-1.5-pro
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff-fenced
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gemini/gemini-1.5-pro-latest
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff-fenced
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gemini/gemini-1.5-pro-exp-0827
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gemini/gemini-exp-1206
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gemini/gemini-exp-1114
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gemini/gemini-exp-1121
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff-fenced
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: vertex_ai/gemini-pro-experimental
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gemini/gemini-1.5-flash-exp-0827
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: false
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: gemini/gemini-2.0-flash-exp
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params:
    max_tokens: 8192
  lazy: false
  name: deepseek/deepseek-chat
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: true
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params:
    max_tokens: 8192
  lazy: false
  name: deepseek/deepseek-coder
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params:
    max_tokens: 8192
  lazy: false
  name: deepseek-chat
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: true
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params:
    max_tokens: 8192
  lazy: false
  name: deepseek-coder
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params: null
  lazy: false
  name: openrouter/deepseek/deepseek-coder
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: null
  editor_model_name: null
  examples_as_sys_msg: true
  extra_params: null
  lazy: false
  name: openrouter/deepseek/deepseek-chat
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: null
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: null
  examples_as_sys_msg: false
  extra_params: null
  lazy: true
  name: openrouter/openai/gpt-4o
  reminder: sys
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: openrouter/openai/gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: editor-diff
  editor_model_name: openai/gpt-4o
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: openai/o1-mini
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: false
  use_temperature: false
  weak_model_name: openai/gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: editor-diff
  editor_model_name: azure/gpt-4o
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: azure/o1-mini
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: false
  use_temperature: false
  weak_model_name: azure/gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: editor-diff
  editor_model_name: gpt-4o
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: o1-mini
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: false
  use_temperature: false
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: openai/gpt-4o
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: openai/o1-preview
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: false
  use_temperature: false
  weak_model_name: openai/gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: azure/gpt-4o
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: azure/o1-preview
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: false
  use_temperature: false
  weak_model_name: azure/gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: architect
  editor_edit_format: editor-diff
  editor_model_name: gpt-4o
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: o1-preview
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: false
  use_temperature: false
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: whole
  editor_edit_format: editor-diff
  editor_model_name: openrouter/openai/gpt-4o
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: openrouter/openai/o1-mini
  reminder: user
  send_undo_reply: false
  streaming: false
  use_repo_map: true
  use_system_prompt: false
  use_temperature: false
  weak_model_name: openrouter/openai/gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: openrouter/openai/gpt-4o
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: openrouter/openai/o1-preview
  reminder: user
  send_undo_reply: false
  streaming: false
  use_repo_map: true
  use_system_prompt: false
  use_temperature: false
  weak_model_name: openrouter/openai/gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: openrouter/openai/gpt-4o
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: openrouter/openai/o1
  reminder: user
  send_undo_reply: false
  streaming: false
  use_repo_map: true
  use_system_prompt: true
  use_temperature: false
  weak_model_name: openrouter/openai/gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: openai/gpt-4o
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: openai/o1
  reminder: user
  send_undo_reply: false
  streaming: false
  use_repo_map: true
  use_system_prompt: true
  use_temperature: false
  weak_model_name: openai/gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: gpt-4o
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: o1
  reminder: user
  send_undo_reply: false
  streaming: false
  use_repo_map: true
  use_system_prompt: true
  use_temperature: false
  weak_model_name: gpt-4o-mini
- cache_control: false
  caches_by_default: false
  edit_format: diff
  editor_edit_format: editor-diff
  editor_model_name: openrouter/qwen/qwen-2.5-coder-32b-instruct
  examples_as_sys_msg: false
  extra_params: null
  lazy: false
  name: openrouter/qwen/qwen-2.5-coder-32b-instruct
  reminder: user
  send_undo_reply: false
  streaming: true
  use_repo_map: true
  use_system_prompt: true
  use_temperature: true
  weak_model_name: openrouter/qwen/qwen-2.5-coder-32b-instruct

Model Aliases
Model aliases allow you to create shorthand names for models you frequently use. This is particularly useful for models with long names or when you want to standardize model usage across your team.

Command Line Usage
You can define aliases when launching aider using the --alias option:

aider --alias "fast:gpt-3.5-turbo" --alias "smart:gpt-4"

Multiple aliases can be defined by using the --alias option multiple times. Each alias definition should be in the format alias:model-name.

Configuration File
You can also define aliases in your .aider.conf.yml file [https://aider.chat/docs/config/aider_conf.html]:

alias:
  - "fast:gpt-3.5-turbo"
  - "smart:gpt-4"
  - "hacker:claude-3-sonnet-20240229"

Using Aliases
Once defined, you can use the alias instead of the full model name:

aider --model fast  # Uses gpt-3.5-turbo
aider --model smart  # Uses gpt-4

Built-in Aliases
Aider includes some built-in aliases for convenience:

- 3: gpt-3.5-turbo
- 35-turbo: gpt-3.5-turbo
- 35turbo: gpt-3.5-turbo
- 4: gpt-4-0613
- 4-turbo: gpt-4-1106-preview
- 4o: gpt-4o
- deepseek: deepseek/deepseek-chat
- flash: gemini/gemini-2.0-flash-exp
- haiku: claude-3-5-haiku-20241022
- opus: claude-3-opus-20240229
- sonnet: claude-3-5-sonnet-20241022

Priority
If the same alias is defined in multiple places, the priority is:

1. Command line aliases (highest priority)
2. Configuration file aliases
3. Built-in aliases (lowest priority)

This allows you to override built-in aliases with your own preferences.

Troubleshooting
Below are some approaches for troubleshooting problems with aider.

If you need more help, please check our GitHub issues and file a new issue if your problem isn’t discussed. Or drop into our Discord to chat with us.

When reporting problems, it is very helpful if you can provide:

Aider version
LLM model you are using
Including the “announcement” lines that aider prints at startup is an easy way to share this helpful info.

Aider v0.37.1-dev
Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo
Git repo: .git with 243 files
Repo-map: using 1024 tokens

Use /help <question> to ask for help about using aider, customizing settings, troubleshooting, using LLMs, etc.

File editing problems
Sometimes the LLM will reply with some code changes that don’t get applied to your local files. In these cases, aider might say something like “Failed to apply edit to filename” or other error messages.

This usually happens because the LLM is disobeying the system prompts and trying to make edits in a format that aider doesn’t expect. Aider makes every effort to get the LLM to conform, and works hard to deal with LLM edits that are “almost” correctly formatted.

But sometimes the LLM just won’t cooperate. In these cases, here are some things you might try.

Don’t add too many files
Many LLMs now have very large context windows, but filling them with irrelevant code or conversation can confuse the model.

- Don’t add too many files to the chat, just add the files you think need to be edited. Aider also sends the LLM a map of your entire git repo, so other relevant code will be included automatically.
- Use /drop to remove files from the chat session which aren’t needed for the task at hand. This will reduce distractions and may help the LLM produce properly formatted edits.
- Use /clear to remove the conversation history, again to help the LLM focus.
- Use /tokens to see how many tokens you are using for each message.

Use a more capable model
If possible try using GPT-4o, Claude 3.5 Sonnet or Claude 3 Opus, as they are the strongest and most capable models.

Weaker models are more prone to disobeying the system prompt instructions. Most local models are just barely capable of working with aider, so editing errors are probably unavoidable.

Local models: context window and quantization
Be especially careful about the Ollama context window [https://aider.chat/docs/llms/ollama.html#setting-the-context-window-size] when working with local models. It defaults to be very small and silently discards data if you exceed it.

Local models which have been quantized are more likely to have editing problems because they are not capable enough to follow aider’s system prompts.

Try the whole edit format
Run aider with --edit-format whole if were using a different edit format. You can see which edit format it is using in the announce lines:

Aider v0.50.2-dev
Models: claude-3-5-sonnet-20240620 with ♾️ diff edit format

More help
If you need more help, please check our GitHub issues and file a new issue if your problem isn’t discussed. Or drop into our Discord to chat with us.

When reporting problems, it is very helpful if you can provide:

Aider version
LLM model you are using
Including the “announcement” lines that aider prints at startup is an easy way to share this helpful info.

Aider v0.37.1-dev
Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo
Git repo: .git with 243 files
Repo-map: using 1024 tokens

Model warnings
Unknown context window size and token costs

Model foobar: Unknown context window size and costs, using sane defaults.

If you specify a model that aider has never heard of, you will get this warning. This means aider doesn’t know the context window size and token costs for that model. Aider will use an unlimited context window and assume the model is free, so this is not usually a significant problem.

See the docs on configuring advanced model settings [https://aider.chat/docs/config/adv-model-settings.html] for details on how to remove this warning.

TIP
You can probably ignore the unknown context window size and token costs warning.

Did you mean?
If aider isn’t familiar with the model you’ve specified, it will suggest similarly named models. This helps in the case where you made a typo or mistake when specifying the model name.

Model gpt-5o: Unknown context window size and costs, using sane defaults.
Did you mean one of these?
- gpt-4o

Missing environment variables
You need to set the listed environment variables. Otherwise you will get error messages when you start chatting with the model.

Model azure/gpt-4-turbo: Missing these environment variables:
- AZURE_API_BASE
- AZURE_API_VERSION
- AZURE_API_KEY

Unknown which environment variables are required

Model gpt-5: Unknown which environment variables are required.

Aider is unable verify the environment because it doesn’t know which variables are required for the model. If required variables are missing, you may get errors when you attempt to chat with the model. You can look in the aider’s LLM documentation or the litellm documentation to see if the required variables are listed there.

More help
If you need more help, please check our GitHub issues and file a new issue if your problem isn’t discussed. Or drop into our Discord to chat with us.

When reporting problems, it is very helpful if you can provide:

Aider version
LLM model you are using
Including the “announcement” lines that aider prints at startup is an easy way to share this helpful info.

Aider v0.37.1-dev
Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo
Git repo: .git with 243 files
Repo-map: using 1024 tokens

Token limits
Every LLM has limits on how many tokens it can process for each request:

- The model’s context window limits how many total tokens of input and output it can process.
- Each model has limit on how many output tokens it can produce.

Aider will report an error if a model responds indicating that it has exceeded a token limit. The error will include suggested actions to try and avoid hitting token limits.

Here’s an example error:

Model gpt-3.5-turbo has hit a token limit!

Input tokens: 768 of 16385
Output tokens: 4096 of 4096 -- exceeded output limit!
Total tokens: 4864 of 16385

To reduce output tokens:
- Ask for smaller changes in each request.
- Break your code into smaller source files.
- Try using a stronger model like gpt-4o or opus that can return diffs.

For more info: https://aider.chat/docs/token-limits.html

NOTE 
Aider never enforces token limits, it only reports token limit errors from the API provider. The token counts that aider reports are estimates.

Input tokens & context window size
The most common problem is trying to send too much data to a model, overflowing its context window. Technically you can exhaust the context window if the input is too large or if the input plus output are too large.

Strong models like GPT-4o and Opus have quite large context windows, so this sort of error is typically only an issue when working with weaker models.

The easiest solution is to try and reduce the input tokens by removing files from the chat. It’s best to only add the files that aider will need to edit to complete your request.

- Use /tokens to see token usage.
- Use /drop to remove unneeded files from the chat session.
- Use /clear to clear the chat history.
- Break your code into smaller source files.

Output token limits
Most models have quite small output limits, often as low as 4k tokens. If you ask aider to make a large change that affects a lot of code, the LLM may hit output token limits as it tries to send back all the changes.

To avoid hitting output token limits:

- Ask for smaller changes in each request.
- Break your code into smaller source files.
- Use a strong model like gpt-4o, sonnet or opus that can return diffs.
- Use a model that supports infinite output [https://aider.chat/docs/more/infinite-output.html]. 

Other causes
Sometimes token limit errors are caused by non-compliant API proxy servers or bugs in the API server you are using to host a local model. Aider has been well tested when directly connecting to major LLM provider cloud APIs [https://aider.chat/docs/llms.html]. For serving local models, Ollama is known to work well with aider [https://aider.chat/docs/llms/ollama.html]. 

Try using aider without an API proxy server or directly with one of the recommended cloud APIs and see if your token limit problems resolve.

More help
If you need more help, please check our GitHub issues and file a new issue if your problem isn’t discussed. Or drop into our Discord to chat with us.

When reporting problems, it is very helpful if you can provide:

- Aider version
- LLM model you are using

Including the “announcement” lines that aider prints at startup is an easy way to share this helpful info.

Aider v0.37.1-dev
Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo
Git repo: .git with 243 files
Repo-map: using 1024 tokens

Aider not found
In some environments the aider command may not be available on your shell path. This can occur because of permissions/security settings in your OS, and often happens to Windows users.

You may see an error message like this:

aider: The term ‘aider’ is not recognized as a name of a cmdlet, function, script file, or executable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.

Below is the most fail safe way to run aider in these situations:

python -m aider

You should also consider installing aider using aider-install, uv or pipx [https://aider.chat/docs/install.html]. 

Dependency versions
Aider expects to be installed with the correct versions of all of its required dependencies.

If you’ve been linked to this doc from a GitHub issue, or if aider is reporting ImportErrors it is likely that your aider install is using incorrect dependencies.

Avoid package conflicts
If you are using aider to work on a python project, sometimes your project will require specific versions of python packages which conflict with the versions that aider requires. If this happens, you may see errors like these when running pip installs:

aider-chat 0.23.0 requires somepackage==X.Y.Z, but you have somepackage U.W.V which is incompatible.

Install with aider-install, uv or pipx
If you are having dependency problems you should consider installing aider using aider-install, uv or pipx [https://aider.chat/docs/install.html]. This will ensure that aider is installed in its own python environment, with the correct set of dependencies.

Package managers like Homebrew, AUR, ports
Package managers often install aider with the wrong dependencies, leading to import errors and other problems.

It is recommended to install aider using aider-install, uv or pipx [https://aider.chat/docs/install.html]. 

Dependency versions matter
Aider pins its dependencies and is tested to work with those specific versions. If you are installing aider directly with pip you should be careful about upgrading or downgrading the python packages that aider uses.

In particular, be careful with the packages with pinned versions noted at the end of aider’s requirements.in file [https://github.com/Aider-AI/aider/blob/main/requirements/requirements.in]. These versions are pinned because aider is known not to work with the latest versions of these libraries.

Also be wary of upgrading litellm, as it versions frequently and sometimes introduces bugs or backwards incompatible changes.

Replit
To use aider with pipx on replit, you can run these commands in the replit shell:

pip install pipx
pipx run aider-chat ...normal aider args...

If you install aider with pipx on replit and try and run it as just aider it will crash with a missing libstdc++.so.6 library.

Using /help
Type /help <question> and aider will respond with helpful information. You can ask questions about using aider, customizing settings, troubleshooting, using LLMs, etc.

Behind the scenes, aider has indexed all of its documentation [https://aider.chat/]. It uses the question to find relevant docs and share them with the LLM to do retrieval augmented generation (RAG) The LLM also has the full context of your ongoing aider chat, so it can help with the exact issue you might be facing.

Aider v0.42.1-dev
Models: claude-3-5-sonnet with diff edit format
Repo-map: using 1024 tokens
Use /help <question> to ask for help, run with –help to see cmd line args

/help is the .env file global or for a git repo?
Based on the provided documentation, here’s the answer to your question about the .env file in aider:

The .env file in aider can be both global and specific to a git repository. Aider looks for .env files in multiple locations, with the following priority order:

Your home directory (global)
The root of your git repo (repo-specific)
The current directory
A file specified with the --env-file <filename> parameter
If multiple .env files exist in these locations, they are loaded in the order listed above, with files loaded last taking priority. This means you can have a global .env file in your home directory with general settings, and then override or add to those settings with a repo-specific .env file in your git repository root.

Here are some relevant documentation links that you might find helpful:

https://aider.chat/docs/config.html
https://aider.chat/docs/config/dotenv.html
The ability to use both global and repo-specific .env files allows for flexible configuration, where you can set default values globally and override them on a per-project basis as needed.

/help can i use local LLMs?
Yes, you can use local LLMs with Aider. Here’s a summary of the options:

Ollama: Aider supports using local models through Ollama.

OpenAI-compatible API: Aider can access local models that provide an OpenAI-compatible API.

Other local models: Aider uses the LiteLLM package to connect to various LLM providers, which may include options for running models locally.

However, it’s important to note that Aider works best with more capable models. Less capable models may have difficulty properly returning “code edits,” which could result in Aider not being able to edit your files and commit changes effectively.

For more detailed information on using local LLMs and connecting to various models, you might want to check out these relevant documentation pages:

https://aider.chat/docs/llms.html
https://aider.chat/docs/llms/ollama.html
https://aider.chat/docs/llms/openai-compat.html
Keep in mind that the performance and capabilities of local LLMs may vary depending on the specific model and your hardware resources.

Example chat transcripts
Below are some chat transcripts showing what it’s like to code with aider. In the chats, you’ll see a variety of coding tasks like generating new code, editing existing code, debugging, exploring unfamiliar code, etc.

https://aider.chat/examples/README.html

Hello World Flask App: Start from scratch and have aider create a simple Flask app with various endpoints, such as adding two numbers and calculating the Fibonacci sequence.

Javascript Game Modification: Dive into an existing open-source repo, and get aider’s help to understand it and make modifications.

Complex Multi-file Change with Debugging: Aider makes a complex code change that is coordinated across multiple source files, and resolves bugs by reviewing error output and doc snippets.

Create a Black Box Test Case: Aider creates a “black box” test case without access to the source of the method being tested, using only a high level map of the repository based on ctags.

Honor the NO_COLOR env var: The user pastes the NO_COLOR spec from no-color.org into the chat, and aider modifies the application to conform.

Download, analyze and plot US Census data: Aider downloads census data, suggests some hypotheses to test, tests one and then summarizes and plots a graph of the results.

Semantic Search & Replace: Updating a collection of function calls, which requires dealing with various formatting and semantic differences in the various function call sites.

Pong Game with Pygame: Creating a simple Pong game using the Pygame library, with customizations for paddle size and color, and ball speed adjustments.

CSS Exercise: Animation Dropdown Menu: A small CSS exercise involving adding animation to a dropdown menu.

Automatically Update Docs: Automatically updating documentation based on the latest version of the main() function.

Editing an Asciinema Cast File: Editing escape sequences in an asciinema screencast file.


Can I use aider with multiple git repos at once?
Currently aider can only work with one repo at a time.

There are some things you can try if you need to work with multiple interrelated repos:

You can run aider in repo-A where you need to make a change and use /read to add some files read-only from another repo-B. This can let aider see key functions or docs from the other repo.
You can run aider --show-repo-map > map.md within each repo to create repo maps. You could then run aider in repo-A and use /read ../path/to/repo-B/map.md to share a high level map of the other repo.
You can use aider to write documentation about a repo. Inside each repo, you could run aider docs.md and work with aider to write some markdown docs. Then while using aider to edit repo-A you can /read ../path/to/repo-B/docs.md to read in those docs from the other repo.
In repo A, ask aider to write a small script that demonstrates the functionality you want to use in repo B. Then when you’re using aider in repo B, you can /read in that script.
How do I turn on the repository map?
Depending on the LLM you are using, aider may launch with the repo map disabled by default:

Repo-map: disabled

This is because weaker models get easily overwhelmed and confused by the content of the repo map. They sometimes mistakenly try to edit the code in the repo map. The repo map is usually disabled for a good reason.

If you would like to force it on, you can run aider with --map-tokens 1024.

How do I include the git history in the context?
When starting a fresh aider session, you can include recent git history in the chat context. This can be useful for providing the LLM with information about recent changes. To do this:

Use the /run command with git diff to show recent changes:
/run git diff HEAD~1

This will include the diff of the last commit in the chat history.

To include diffs from multiple commits, increase the number after the tilde:
/run git diff HEAD~3

This will show changes from the last three commits.

Remember, the chat history already includes recent changes made during the current session, so this tip is most useful when starting a new aider session and you want to provide context about recent work.

The /git command will not work for this purpose, as its output is not included in the chat.

How can I run aider locally from source code?
To run the project locally, follow these steps:

# Clone the repository
git clone git@github.com:Aider-AI/aider.git

# Navigate to the project directory
cd aider

# It's recommended to make a virtual environment

# Install aider in editable/development mode, 
# so it runs from the latest copy of these source files
python -m pip install -e .

# Run the local version of aider
python -m aider

Can I change the system prompts that aider uses?
The most convenient way to add custom instructions is to use a conventions file.

But, aider is set up to support different actual system prompts and edit formats in a modular way. If you look in the aider/coders subdirectory, you’ll see there’s a base coder with base prompts, and then there are a number of different specific coder implementations.

If you’re thinking about experimenting with system prompts this document about benchmarking GPT-3.5 and GPT-4 on code editing might be useful background.

While it’s not well documented how to add new coder subsystems, you may be able to modify an existing implementation or use it as a template to add another.

To get started, try looking at and modifying these files.

The wholefile coder is currently used by GPT-3.5 by default. You can manually select it with --edit-format whole.

wholefile_coder.py
wholefile_prompts.py
The editblock coder is currently used by GPT-4o by default. You can manually select it with --edit-format diff.

editblock_coder.py
editblock_prompts.py
The universal diff coder is currently used by GPT-4 Turbo by default. You can manually select it with --edit-format udiff.

udiff_coder.py
udiff_prompts.py
When experimenting with coder backends, it helps to run aider with --verbose --no-pretty so you can see all the raw information being sent to/from the LLM in the conversation.

You can also refer to the instructions for installing a development version of aider.

What LLMs do you use to build aider?
Aider writes a lot of its own code, usually about 70% of the new code in each release. People often ask which LLMs I use with aider, when writing aider. Below is a table showing the models I have used recently, extracted from the public log of my aider analytics.

Model Name	Total Tokens	Percent
deepseek/deepseek-chat	1,422,360	62.0%
claude-3-5-sonnet-20241022	823,708	35.9%
o1	37,290	1.6%
gemini/gemini-2.0-flash-exp	4,827	0.2%
gpt-4o	4,473	0.2%
How are the “aider wrote xx% of code” stats computed?
Aider is tightly integrated with git so all of aider’s code changes are committed to the repo with proper attribution. The stats are computed by doing something like git blame on the repo, and counting up who wrote all the new lines of code in each release. Only lines in source code files are counted, not documentation or prompt files.

Why does aider sometimes stop highlighting code in its replies?
Aider displays the markdown responses that are coming back from the LLM. Usually, the LLM will reply with code in a markdown “code block” with triple backtick fences, like this:

Here's some code:

```
print("hello")
```

But if you’ve added files to the chat that contain triple backticks, aider needs to tell the LLM to use a different set of fences. Otherwise, the LLM can’t safely include your code’s triple backticks inside the code blocks that it returns with edits. Aider will use fences like <source>...</source> in this case.

A side effect of this is that the code that aider outputs may no longer be properly highlighted. You will most often notice this if you add markdown files to you chats that contain code blocks.

Why is the LLM speaking to me in an unexpected language?
Aider goes to some effort to prompt the model to use the language that is configured for your system. But LLMs aren’t fully reliable, and they sometimes decide to speak in an unexpected language. Claude is especially fond of speaking French.

You can explicitly set the language that aider tells the model to use with --chat-language <language>. But the LLM may not comply.

Can I share my aider chat transcript?
Yes, you can now share aider chat logs in a pretty way.

Copy the markdown logs you want to share from .aider.chat.history.md and make a github gist. Or publish the raw markdown logs on the web any way you’d like.

https://gist.github.com/Aider-AI/2087ab8b64034a078c0a209440ac8be0

Take the gist URL and append it to:

https://aider.chat/share/?mdurl=

This will give you a URL like this, which shows the chat history like you’d see in a terminal:

https://aider.chat/share/?mdurl=https://gist.github.com/Aider-AI/2087ab8b64034a078c0a209440ac8be0

Can I edit files myself while aider is running?
Yes. Aider always reads the latest copy of files from the file system when you send each message.

While you’re waiting for aider’s reply to complete, it’s probably unwise to edit files that you’ve added to the chat. Your edits and aider’s edits might conflict.

What is Aider AI LLC?
Aider AI LLC is the company behind the aider AI coding tool. Aider is open source and available on GitHub under an Apache 2.0 license.










