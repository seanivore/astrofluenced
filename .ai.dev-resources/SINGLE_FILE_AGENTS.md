# Single File Agents (SFAs) 
Offer a powerful pattern for building lightweight, purpose-specific AI agents. 

## Key Insights 

1. **SFAs enable self-contained, focused agents**: Each agent exists in a single Python file with embedded dependencies, making them easy to deploy, share, and maintain.

2. **Astral UV is the key enabling technology**: UV is a modern Python package manager that allows for inline dependency declarations in scripts, which is critical for these single-file implementations.

3. **The agentic loop pattern is crucial**: These agents follow a consistent pattern of:
   - Taking user input
   - Planning steps using an LLM
   - Executing tools/functions
   - Processing feedback
   - Continuing or completing the task

4. **SFAs follow best practices from Anthropic's agent design guidelines**: The design pattern uses simple, composable elements rather than complex frameworks, which aligns with Anthropic's recommendations.

### 1. SFA Architecture and Autonomy Features
The SFA pattern has several architectural elements that enable full agent autonomy. 

- **Self-contained execution environment**: All dependencies are declared inline at the top of the file, making deployment simple.
- **Stateful agent loop**: The agent maintains context through its execution loop, enabling complex multi-step tasks.
- **Tool-based action system**: The agent has access to specific functions (tools) that it can call to interact with the environment.
- **Prompt-driven intelligence**: The agent's behavior is guided by a well-structured prompt that defines its purpose, available tools, and success criteria.
- **Closure mechanism**: The agent has a specific way to signal task completion (the "complete_task" function).

### 2. Implementation Requirements
Implementation complexity is relatively low compared to other agent frameworks, great for individual developers. 

- **Python environment with UV installed**: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **API keys for LLM providers**: OpenAI, Anthropic, or Gemini
- **Additional API keys for specific services**: Depending on the agent's purpose (e.g., FireCrawl for the web scraper example)
- **Basic Python knowledge**: To create and modify the agent template files

### 3. Tools for Research and Feedback Tasks
For example, research and feedback tasked SFA would need these tools:

**Research Agent Tools:**
- `browse_webpage`: To scrape and analyze web content
- `search_information`: To query search engines or specific resources
- `extract_key_points`: To identify and summarize important information
- `organize_findings`: To structure research results
- `save_findings`: To store results in specified formats
- `generate_report`: To create summaries of findings

**Feedback Agent Tools:**
- `read_content`: To access content needing feedback
- `analyze_content`: To evaluate content against specific criteria
- `generate_feedback`: To create structured feedback
- `highlight_issues`: To identify specific areas for improvement
- `suggest_improvements`: To offer constructive solutions
- `deliver_feedback`: To format and send feedback to designated locations

Both agent types would also need:
- `read_file`/`write_file`: For file system operations
- `complete_task`: To signal completion
- Possibly tools for API calls to specific services

### 4. Potential Limitations

- **Error handling**: The agent might get stuck in edge cases without proper error recovery
- **Cost management**: Extended agent loops with many LLM calls could become expensive
- **Debugging complexity**: When agents fail, identifying the root cause might be challenging
- **Deployment overhead**: While simpler than alternatives, still requires Python environment setup
- **Maintenance needs**: As APIs change, the agent tools might need updates

----

# Implementation Plan for Single File Agents

## 1. Minimal Viable Research SFA

### Code Structure

```python
# /// script
# dependencies = [
#   "openai>=1.63.0",
#   "anthropic>=0.17.0", 
#   "rich>=13.7.0",
#   "pydantic>=2.0.0",
#   "beautifulsoup4>=4.12.0",
#   "requests>=2.31.0",
#   "python-dotenv>=1.0.0",
# ]
# ///

import os
import sys
import json
import argparse
from typing import List, Dict, Any
from rich.console import Console
from rich.panel import Panel
import requests
from bs4 import BeautifulSoup
import openai
import anthropic
from pydantic import BaseModel, Field
from openai import pydantic_function_tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize rich console for output
console = Console()

# Initialize API clients
openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Define tool schemas
class BrowseWebpageArgs(BaseModel):
    reasoning: str = Field(..., description="Explanation for browsing this webpage")
    url: str = Field(..., description="URL to browse")
    
class ExtractContentArgs(BaseModel):
    reasoning: str = Field(..., description="Explanation for extracting this content")
    html_content: str = Field(..., description="HTML content to extract from")
    
class AnalyzeInformationArgs(BaseModel):
    reasoning: str = Field(..., description="Explanation for analyzing this information")
    content: str = Field(..., description="Content to analyze")
    criteria: str = Field(..., description="Criteria for analysis")
    
class SaveFindingsArgs(BaseModel):
    reasoning: str = Field(..., description="Explanation for saving these findings")
    findings: str = Field(..., description="Research findings to save")
    output_path: str = Field(..., description="Path to save findings")

class CompleteTaskArgs(BaseModel):
    reasoning: str = Field(..., description="Explanation of why the task is complete")

# Create tools list
tools = [
    pydantic_function_tool(BrowseWebpageArgs),
    pydantic_function_tool(ExtractContentArgs),
    pydantic_function_tool(AnalyzeInformationArgs),
    pydantic_function_tool(SaveFindingsArgs),
    pydantic_function_tool(CompleteTaskArgs),
]

# Agent prompt template
AGENT_PROMPT = """<purpose>
    You are a world-class research assistant capable of gathering, analyzing, and summarizing information.
    Your goal is to conduct thorough research on the given topic and provide well-organized findings.
</purpose>

<instructions>
    <instruction>Break down the research question to understand what information is needed.</instruction>
    <instruction>Browse relevant webpages to gather information.</instruction>
    <instruction>Extract key content from pages focusing on what's relevant to the question.</instruction>
    <instruction>Analyze information carefully against provided criteria.</instruction>
    <instruction>Save your findings in a well-structured format.</instruction>
    <instruction>Complete the task when you've gathered sufficient information to answer the question thoroughly.</instruction>
</instructions>

<tools>
    <tool>
        <n>browse_webpage</n>
        <description>Retrieves content from a specified URL</description>
        <parameters>
            <parameter>
                <n>reasoning</n>
                <type>string</type>
                <description>Why we're browsing this webpage</description>
                <required>true</required>
            </parameter>
            <parameter>
                <n>url</n>
                <type>string</type>
                <description>URL to browse</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <n>extract_content</n>
        <description>Extracts relevant content from HTML</description>
        <parameters>
            <parameter>
                <n>reasoning</n>
                <type>string</type>
                <description>Why we're extracting this content</description>
                <required>true</required>
            </parameter>
            <parameter>
                <n>html_content</n>
                <type>string</type>
                <description>HTML content to extract from</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <n>analyze_information</n>
        <description>Analyzes content against specific criteria</description>
        <parameters>
            <parameter>
                <n>reasoning</n>
                <type>string</type>
                <description>Why we're analyzing this information</description>
                <required>true</required>
            </parameter>
            <parameter>
                <n>content</n>
                <type>string</type>
                <description>Content to analyze</description>
                <required>true</required>
            </parameter>
            <parameter>
                <n>criteria</n>
                <type>string</type>
                <description>Criteria for analysis</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <n>save_findings</n>
        <description>Saves research findings to a file</description>
        <parameters>
            <parameter>
                <n>reasoning</n>
                <type>string</type>
                <description>Why we're saving these findings</description>
                <required>true</required>
            </parameter>
            <parameter>
                <n>findings</n>
                <type>string</type>
                <description>Research findings to save</description>
                <required>true</required>
            </parameter>
            <parameter>
                <n>output_path</n>
                <type>string</type>
                <description>Path to save findings</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <n>complete_task</n>
        <description>Signals that the research task is complete</description>
        <parameters>
            <parameter>
                <n>reasoning</n>
                <type>string</type>
                <description>Why the research is now complete</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
</tools>

<research-question>
    {{research_question}}
</research-question>

<output-file-path>
    {{output_file_path}}
</output-file-path>
"""

# Tool implementation functions
def browse_webpage(reasoning: str, url: str) -> str:
    """Browse a webpage and return its HTML content."""
    console.log(f"[blue]Browsing webpage[/blue] - URL: {url} - Reasoning: {reasoning}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        console.log(f"[red]Error browsing webpage: {str(e)}[/red]")
        return f"Error: {str(e)}"

def extract_content(reasoning: str, html_content: str) -> str:
    """Extract relevant content from HTML."""
    console.log(f"[blue]Extracting content[/blue] - Reasoning: {reasoning}")
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove scripts, styles, and other non-content elements
        for script in soup(["script", "style", "meta", "svg", "path"]):
            script.extract()
            
        # Get text
        text = soup.get_text(separator="\n")
        
        # Clean up text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text[:40000]  # Limit to avoid token issues
    except Exception as e:
        console.log(f"[red]Error extracting content: {str(e)}[/red]")
        return f"Error: {str(e)}"

def analyze_information(reasoning: str, content: str, criteria: str) -> str:
    """Analyze content against specific criteria."""
    console.log(f"[blue]Analyzing information[/blue] - Criteria: {criteria} - Reasoning: {reasoning}")
    try:
        # We'll use the OpenAI API for analysis to avoid token limits
        analysis_response = openai_client.chat.completions.create(
            model="o3-mini",  # or gpt-4 if available and needed
            messages=[
                {"role": "system", "content": f"Analyze the following content according to these criteria: {criteria}. Provide a concise analysis."},
                {"role": "user", "content": content[:30000]}  # Limit content to avoid token issues
            ]
        )
        analysis = analysis_response.choices[0].message.content
        return analysis
    except Exception as e:
        console.log(f"[red]Error analyzing information: {str(e)}[/red]")
        return f"Error: {str(e)}"

def save_findings(reasoning: str, findings: str, output_path: str) -> str:
    """Save research findings to a file."""
    console.log(f"[blue]Saving findings[/blue] - Path: {output_path} - Reasoning: {reasoning}")
    try:
        with open(output_path, "w") as f:
            f.write(findings)
        return f"Successfully saved {len(findings)} characters to {output_path}"
    except Exception as e:
        console.log(f"[red]Error saving findings: {str(e)}[/red]")
        return f"Error: {str(e)}"

def complete_task(reasoning: str) -> str:
    """Signal that the research task is complete."""
    console.log(f"[green]Task Complete[/green] - Reasoning: {reasoning}")
    result = "Research task completed successfully"
    console.print(Panel(result, title="[green]Complete[/green]", border_style="green"))
    return result

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Research agent that gathers and analyzes information")
    parser.add_argument("--question", "-q", required=True, help="The research question to investigate")
    parser.add_argument("--output", "-o", default="research_findings.md", help="Path to save the research findings")
    parser.add_argument("--compute-limit", "-c", type=int, default=15, help="Maximum number of agent iterations")
    parser.add_argument("--model", "-m", default="o3-mini", help="OpenAI model to use")
    
    args = parser.parse_args()
    
    # Format the prompt with user arguments
    formatted_prompt = (
        AGENT_PROMPT.replace("{{research_question}}", args.question)
        .replace("{{output_file_path}}", args.output)
    )
    
    # Initialize conversation
    messages = [{"role": "user", "content": formatted_prompt}]
    
    # Agent loop
    iterations = 0
    max_iterations = args.compute_limit
    break_loop = False
    
    while iterations < max_iterations and not break_loop:
        iterations += 1
        console.rule(f"[yellow]Agent Loop {iterations}/{max_iterations}[/yellow]")
        
        try:
            # Get completion from OpenAI
            completion = openai_client.chat.completions.create(
                model=args.model,
                messages=messages,
                tools=tools,
                tool_choice="auto",
            )
            
            response_message = completion.choices[0].message
            
            # Print assistant's response if any
            assistant_content = response_message.content or ""
            if assistant_content:
                console.print(Panel(assistant_content, title="Assistant"))
                
            # Add message to conversation history
            messages.append({
                "role": "assistant",
                "content": assistant_content,
                "tool_calls": response_message.tool_calls
            })
            
            # Process tool calls
            if response_message.tool_calls:
                for tool_call in response_message.tool_calls:
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)
                    
                    # Execute appropriate function
                    result = None
                    if function_name == "BrowseWebpageArgs":
                        result = browse_webpage(**function_args)
                    elif function_name == "ExtractContentArgs":
                        result = extract_content(**function_args)
                    elif function_name == "AnalyzeInformationArgs":
                        result = analyze_information(**function_args)
                    elif function_name == "SaveFindingsArgs":
                        result = save_findings(**function_args)
                    elif function_name == "CompleteTaskArgs":
                        result = complete_task(**function_args)
                        break_loop = True
                    else:
                        result = f"Unknown function: {function_name}"
                        
                    # Add result to conversation
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": function_name,
                        "content": str(result),
                    })
            else:
                console.print("[red]No tool calls found - unexpected behavior[/red]")
                
        except Exception as e:
            console.log(f"[red]Error in agent loop: {str(e)}[/red]")
            console.print_exception()
    
    if iterations >= max_iterations and not break_loop:
        console.print("[yellow]Reached maximum iterations without completion[/yellow]")
    
if __name__ == "__main__":
    main()
```

## 2. Implementation Steps

### **Step 1: Set Up the Environment**

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a directory for your agents
mkdir -p ~/Development/claud-agents
cd ~/Development/claud-agents

# Create .env file for API keys
echo "OPENAI_API_KEY=your_openai_key_here" > .env
echo "ANTHROPIC_API_KEY=your_anthropic_key_here" >> .env
echo "FIRECRAWL_API_KEY=your_firecrawl_key_here" >> .env
```

### **Step 2: Create the Research Agent**

```bash
# Create the research agent file
touch research_agent.py

# Copy the code from above into research_agent.py
# Edit the file with your preferred editor
```

### **Step 3: Test the Agent**

```bash
# Run the agent on a simple research task
uv run research_agent.py -q "What are the key benefits of Single File Agents for AI development?" -o "sfa_research.md" -c 5

# Check the results
cat sfa_research.md
```

### **Step 4: Create a Feedback Agent**

You can follow the same pattern as the research agent but modify the tools and prompt to focus on feedback tasks:

```bash
# Copy the research agent as a starting point
cp research_agent.py feedback_agent.py

# Edit feedback_agent.py to implement feedback-specific tools and prompts
# Change tool definitions to: read_content, analyze_content, generate_feedback, etc.
```

## 3. Extending the Basic SFA

### Add More Sophisticated Research Capabilities

1. **Add a search engine integration**:
   ```python
   class SearchWebArgs(BaseModel):
       reasoning: str = Field(..., description="Explanation for this search")
       query: str = Field(..., description="Search query")
   ```

2. **Add PDF document analysis**:
   ```python
   class AnalyzePdfArgs(BaseModel):
       reasoning: str = Field(..., description="Explanation for analyzing this PDF")
       pdf_path: str = Field(..., description="Path to the PDF file")
   ```

3. **Add research planning tools**:
   ```python
   class PlanResearchArgs(BaseModel):
       reasoning: str = Field(..., description="Explanation for creating this research plan")
       research_question: str = Field(..., description="Research question to plan for")
   ```

### Add Interactive Feedback Capabilities

1. **Add feedback severity classification**:
   ```python
   class ClassifyFeedbackSeverityArgs(BaseModel):
       reasoning: str = Field(..., description="Explanation for this classification")
       issue: str = Field(..., description="Issue to classify")
       severity_options: List[str] = Field(..., description="Available severity options")
   ```

2. **Add before/after comparison**:
   ```python
   class CompareFeedbackChangesArgs(BaseModel):
       reasoning: str = Field(..., description="Explanation for this comparison")
       before_content: str = Field(..., description="Content before changes")
       after_content: str = Field(..., description="Content after changes")
   ```

## 4. Integration with Existing Workflow

### Shell Aliases for Quick Access

Add these to your `~/.bashrc` or `~/.zshrc`:

```bash
alias research='uv run ~/Development/claud-agents/research_agent.py'
alias feedback='uv run ~/Development/claud-agents/feedback_agent.py'
```

### Integration with Git Hooks

Create a post-commit hook at `.git/hooks/post-commit`:

```bash
#!/bin/bash
# Get changed Markdown files
changed_files=$(git diff-tree --no-commit-id --name-only -r HEAD | grep '\.md$')

# Run feedback agent on each changed file
for file in $changed_files; do
  feedback -f "$file" -o "${file%.*}_feedback.md"
done
```

### Schedule Regular Research Tasks

Add a crontab entry:

```
# Run daily research on a topic at 7 AM
0 7 * * * cd ~/Development/claud-agents && uv run research_agent.py -q "Latest developments in AI agent architectures" -o "~/Dropbox/Daily_Research/$(date +\%Y-\%m-\%d)_ai_agent_research.md" -c 20
```
----

# Best Practices and Future Considerations for Single File Agents

## Best Practices for SFA Development

### 1. Prompt Engineering Principles

1. **Clear Agent Purpose**: Always include a <purpose> section defining exactly what the agent should do and its boundaries.

2. **Explicit Tool Documentation**: Document each tool thoroughly, including:
   - Clear parameter descriptions
   - Expected output format
   - Example usage
   - Edge cases to handle
   - Error conditions

3. **Reasoning Requirements**: Always require a 'reasoning' parameter for every tool call to improve transparency and debugging.

4. **Completion Criteria**: Define explicitly when a task should be considered complete to avoid endless loops.

5. **Progressive Tools**: Design tools with a logical progression from exploration to action to completion.

### 2. Testing and Debugging Strategies

1. **Incremental Testing**: Start with simplified test cases that exercise only 1-2 tools at a time.

2. **Comprehensive Logging**: 
   - Log all tool calls, inputs, and outputs
   - Use rich formatting to distinguish tool calls from results
   - Save logs for analyzing agent behavior patterns

3. **Controlled Iteration Limits**: Always include maximum iteration limits to prevent runaway execution.

4. **Error Recovery Mechanisms**:
   - Wrap tool functions in try/except blocks
   - Return informative error messages that help the agent correct its approach
   - Consider implementing automatic retries for transient failures

5. **Unit Testing Tools**: Test individual tools separately from the agent to verify they work correctly.

```python
# Example testing code
def test_tools():
    """Test each tool function independently."""
    print("Testing browse_webpage...")
    result = browse_webpage("Testing", "https://example.com")
    assert len(result) > 0, "Failed to retrieve content"
    
    print("Testing extract_content...")
    result = extract_content("Testing", "<html><body><p>Test content</p></body></html>")
    assert "Test content" in result, "Failed to extract content"
    
    # Add more tool tests...
```

### 3. Security, Cost, and Performance Considerations

1. **Security Best Practices**:
   - Validate and sanitize URLs before browsing
   - Set timeouts on all external requests
   - Limit file system access to specific directories
   - Validate file paths to prevent directory traversal
   - Consider implementing content filtering on web scraping

2. **Cost Management**:
   - Track token usage per request and identify optimization opportunities
   - Implement tiered model usage (smaller models for simple tasks)
   - Add hard limits on iterations to prevent runaway costs
   - Consider implementing cost tracking per agent run
   - Cache common requests and analysis to reduce redundant API calls

3. **Performance Optimization**:
   - Use asyncio for concurrent API calls when appropriate
   - Implement content chunking for large documents
   - Consider local embedding models for simple classification tasks
   - Use appropriate timeouts for each external service
   - Add basic rate limiting to prevent API throttling

4. **Reliability Enhancements**:
   - Implement retries with exponential backoff for API calls
   - Add checkpointing to save progress during long-running tasks
   - Consider implementing a "resume from checkpoint" feature
   - Add heartbeat logging for long-running processes

### 4. Progressive Enhancement Strategy

1. **Start Minimal, Expand Thoughtfully**:
   - Begin with the simple research or feedback agent template
   - Add one tool at a time based on actual needs
   - Test thoroughly after each addition

2. **Tool Enhancement Path**:
   - Basic version: Simple web browsing and content extraction
   - Intermediate: Add search capabilities and structured output
   - Advanced: Integrate specialized APIs and complex workflows

3. **Model Upgrade Path**:
   - Start with cost-effective models like OpenAI's "o3-mini"
   - Test performance with more capable models for complex tasks
   - Consider hybrid approaches using different models for different steps

4. **Integration Enhancement**:
   - Start with standalone operation
   - Add output to notification systems (Discord, email)
   - Implement scheduled runs via cron
   - Consider adding simple API endpoints to trigger agents

## Conclusion

### Recommended implementation approach example:

1. Start with the basic research agent template
2. Test on simple research tasks and make incremental improvements
3. Create a feedback agent based on the same pattern
4. Gradually enhance both with additional tools as needed
5. Set up integration with existing workflow (shell aliases, git hooks, etc.)
6. Consider containerization for easier deployment if needed

This approach allows for progressive improvement while delivering immediate value with minimal implementation complexity. The SFA pattern's flexibility will also let you adapt to new LLM capabilities and API changes with minimal disruption.

### The Slight Learning Curve Creates Longevity

1. **Architectural Control**: By understanding and owning the agent implementation, you avoid dependency on third-party frameworks that might change, deprecate features, or even shut down. Your solutions will continue working as long as the basic APIs (OpenAI, Anthropic, etc.) remain available.

2. **Adaptability**: The modular tool-based approach makes it easy to replace or upgrade individual components as technologies evolve. For example, if a better web scraping library becomes available, you only need to update that specific tool function without changing the overall architecture.

3. **Technology Independence**: The core pattern isn't tied to any specific LLM provider. You could switch from OpenAI to Anthropic or even open-source models with minimal changes to the agent structure itself.

4. **Skill Investment**: The Python skills and agent patterns you learn will transfer across many different applications and use cases, making each new agent easier to build than the last.

5. **Progressive Enhancement**: The simplicity of the basic pattern enables a "start simple, grow as needed" approach. You can begin with minimal functionality and expand gradually, ensuring your solution remains maintainable and aligned with your actual needs.

### Summary 

Single File Agents represent an excellent middle ground between complex agent frameworks and simple scripts. They provide the structure for fully autonomous operation while maintaining the simplicity of a single file that can be easily deployed, modified, and shared.

By following the implementation plan outlined above, Sean can quickly create and deploy agents that handle research and feedback tasks autonomously, freeing up time for higher-value activities while maintaining full control over the agent's behavior and capabilities.