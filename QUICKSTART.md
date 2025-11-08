# ⚡ Quick Start Guide

Get up and running with Claude Code Assistant in 5 minutes!

## 🎯 Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- Anthropic API key ([get one here](https://console.anthropic.com/))

## 🚀 Installation (3 steps)

### 1. Run the setup script

```bash
./setup.sh
```

### 2. Add your API key

Edit `.env` and add your Anthropic API key:

```bash
ANTHROPIC_API_KEY=sk-ant-xxxxx
```

### 3. Start the assistant

```bash
uv run main.py
```

That's it! 🎉

## 💬 First Conversation

Once the assistant starts, try these commands:

```
👤 You: help

👤 You: tools

👤 You: Show me the content of README.md

👤 You: List all Python files in the current directory

👤 You: Run the unit tests
```

## 🎨 What You'll See

The assistant features a colorful, hacker-style terminal interface:

- **Green panels** 🟢: Tool results
- **Cyan panels** 🔵: Assistant responses
- **Yellow text** 🟡: Tool execution info
- **Red text** 🔴: Errors

## 🛠️ Testing the Tools

### File Operations
```
Read the main.py file
List files in the tools directory
Search for 'agent' in Python files
```

### Testing
```
Run the tests in the tests directory
Run pytest with verbose output
```

### Code Analysis
```
What tools do you have?
Show me information about agent.py
Search for all test files
```

## 🔧 Optional: MCP Servers

For advanced features, install MCP servers:

### Web Search (DuckDuckGo)
```bash
npm install -g @modelcontextprotocol/server-duckduckgo
```

Then try:
```
Search for "Python async best practices"
```

### GitHub Integration
```bash
npm install -g @modelcontextprotocol/server-github
```

Add to `.env`:
```bash
GITHUB_TOKEN=ghp_xxxxx
```

Then try:
```
Search GitHub for LangGraph examples
```

### File System (Desktop Commander)
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

## 🐛 Troubleshooting

### "ANTHROPIC_API_KEY not found"
- Make sure you created `.env` from `.env.example`
- Verify your API key is correct
- Check there are no extra spaces in the `.env` file

### "uv not found"
Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### MCP tools not loading
- MCP tools are optional
- The assistant works fine with just local tools
- Check the console output for specific MCP errors

### Tests failing
```bash
uv run pytest -v
```

## 📊 Viewing Conversation History

All conversations are saved in `checkpoints.db`:

```bash
sqlite3 checkpoints.db "SELECT * FROM writes LIMIT 5"
```

## 🎓 Next Steps

1. **Read the full README.md** for detailed documentation
2. **Customize tools** in `tools/local_tools.py`
3. **Experiment** with different queries
4. **Check the code** to understand how it works

## 🆘 Need Help?

- Type `help` in the assistant for commands
- Type `tools` to see available tools
- Check `README.md` for full documentation
- Look at `tests/` for usage examples

---

**Happy coding! 🚀**
