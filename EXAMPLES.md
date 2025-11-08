# 📚 Usage Examples

Real-world examples of using the Claude Code Assistant.

## 🔍 File Operations

### Reading Files

```
👤 You: Show me the content of main.py

🤖 Assistant: [Displays the file content]
```

```
👤 You: Read the README file

🤖 Assistant: [Displays README.md content]
```

### Listing Files

```
👤 You: List all files in the current directory

🤖 Assistant: [Shows directory contents with emojis]
```

```
👤 You: What files are in the tools folder?

🤖 Assistant: [Lists tools/ directory]
```

### Searching Files

```
👤 You: Find all Python files with 'test' in the name

🤖 Assistant: [Uses search_files tool to find test files]
```

```
👤 You: Search for files containing 'agent'

🤖 Assistant: [Searches and displays matches]
```

### Writing Files

```
👤 You: Create a new file called hello.py with a simple hello world script

🤖 Assistant: [Uses write_file tool to create the file]
```

## 🧪 Testing

### Running Tests

```
👤 You: Run the unit tests

🤖 Assistant: [Executes pytest on the tests directory]
```

```
👤 You: Run tests in verbose mode

🤖 Assistant: [Runs pytest with -v flag]
```

### Test-Driven Development

```
👤 You: The read_file function has a bug when the file doesn't exist

🤖 Assistant: [Runs tests, identifies failing test, suggests fix]
```

## 🔧 Tool Discovery

### Listing Available Tools

```
👤 You: What tools do you have?

🤖 Assistant: [Displays tree of local and MCP tools]
```

```
👤 You: tools

🤖 Assistant: [Shows formatted tool list]
```

## 💻 Code Analysis

### File Information

```
👤 You: Give me details about agent.py

🤖 Assistant: [Uses get_file_info to show size, dates, etc.]
```

### Code Structure

```
👤 You: Show me all the Python files in this project

🤖 Assistant: [Searches for *.py files and lists them]
```

```
👤 You: What's the structure of the tools directory?

🤖 Assistant: [Lists files in tools/ directory]
```

## 🌐 Web Search (with DuckDuckGo MCP)

If you have DuckDuckGo MCP installed:

```
👤 You: Search for "LangGraph StateGraph examples"

🤖 Assistant: [Performs web search and summarizes results]
```

```
👤 You: Find information about Model Context Protocol

🤖 Assistant: [Searches and provides relevant links]
```

## 🐙 GitHub Integration (with GitHub MCP)

If you have GitHub MCP configured:

```
👤 You: Search GitHub for LangGraph projects

🤖 Assistant: [Searches repositories and displays results]
```

```
👤 You: Show me recent issues in langchain-ai/langgraph

🤖 Assistant: [Fetches and displays issues]
```

## 🔄 Multi-Step Workflows

### Analysis and Testing

```
👤 You: Analyze the local_tools.py file and run its tests

🤖 Assistant: 
1. [Reads tools/local_tools.py]
2. [Runs pytest on tests/test_local_tools.py]
3. [Provides summary of code and test results]
```

### File Creation and Verification

```
👤 You: Create a new Python file called calculator.py with add and subtract functions, then create tests for it

🤖 Assistant:
1. [Creates calculator.py with functions]
2. [Creates test_calculator.py with unit tests]
3. [Runs pytest to verify tests pass]
```

### Search and Read

```
👤 You: Find all markdown files and show me the README

🤖 Assistant:
1. [Searches for *.md files]
2. [Reads README.md]
3. [Displays content]
```

## 🎯 Complex Queries

### Codebase Navigation

```
👤 You: Help me understand the project structure. List all directories and their main files.

🤖 Assistant: [Systematically explores and explains the structure]
```

### Debugging Assistance

```
👤 You: The tests are failing. Can you help me debug?

🤖 Assistant:
1. [Runs pytest to see failures]
2. [Analyzes error messages]
3. [Suggests fixes based on test output]
```

### Code Review

```
👤 You: Review the agent.py file and suggest improvements

🤖 Assistant:
1. [Reads agent.py]
2. [Analyzes code structure]
3. [Provides suggestions]
```

## 🎨 Creative Uses

### Documentation Generation

```
👤 You: Create a simple docstring for all functions in local_tools.py

🤖 Assistant: [Analyzes functions and suggests documentation]
```

### Code Refactoring

```
👤 You: The user_input function seems too simple. Should it do more?

🤖 Assistant: [Analyzes code and provides architectural insights]
```

### Learning and Exploration

```
👤 You: Explain how the StateGraph workflow works in this project

🤖 Assistant: [Reads relevant files and explains the architecture]
```

## 💡 Tips for Effective Use

1. **Be Specific**: "Show me agent.py" is better than "show me code"
2. **Multi-Step**: "Read main.py and run the tests" works!
3. **Context**: The assistant remembers the conversation
4. **Tools Command**: Type "tools" to see what's available
5. **Help Command**: Type "help" for quick reference

## 🚫 Limitations

Current limitations to be aware of:

- File operations are limited to the current directory tree
- Large files may be truncated in responses
- Complex git operations require manual intervention
- No direct code execution (use pytest for testing)
- MCP tools require separate installation

## 🔮 Advanced Patterns

### Iterative Development

```
1. "Create a new function in utils.py"
2. "Add tests for that function"
3. "Run the tests"
4. "The tests failed - can you fix the function?"
```

### Research and Implementation

```
1. "Search for best practices on async Python"
2. "Create an example async function based on those practices"
3. "Add it to examples.py"
```

### Code Auditing

```
1. "List all Python files"
2. "Check each one for print statements that should be logging"
3. "Suggest improvements"
```

---

**Experiment and explore!** The assistant is designed to be helpful and proactive. 🚀
