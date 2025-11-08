# 🚀 Getting Started Checklist

Follow this step-by-step guide to get your Claude Code Assistant running!

## ✅ Prerequisites

- [ ] Python 3.11+ installed
- [ ] `uv` package manager installed ([install here](https://github.com/astral-sh/uv))
- [ ] Anthropic API key ([get one here](https://console.anthropic.com/))
- [ ] Docker installed (optional, for MCP servers)

## 📋 Setup Steps

### 1. Environment Setup

```bash
# Run the setup script
./setup.sh
```

**What this does:**
- Creates `.venv` virtual environment
- Installs all Python dependencies (69 packages)
- Copies `.env.example` to `.env`

### 2. Configure API Key

```bash
# Edit the .env file
nano .env  # or vim, code, etc.
```

**Add your key:**
```bash
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
```

### 3. Verify Installation

```bash
# Run the tests
./run_tests.sh
```

**Expected output:**
```
✅ All tests passed!
```

### 4. Start the Assistant

```bash
# Launch the assistant
uv run main.py
```

**You should see:**
```
╔═══════════════════════════════════════╗
║   🤖  CLAUDE CODE ASSISTANT  🤖      ║
║   ▸ Powered by LangGraph + MCP       ║
╚═══════════════════════════════════════╝
```

## 🎯 First Steps

### Try These Commands

```
help       # See available commands
tools      # List all tools
```

### Example Queries

```
Show me the content of README.md
List all Python files
Run the unit tests
Search for 'agent' in the codebase
What tools do you have?
```

## 🐳 Optional: Docker Setup

### Build Deno MCP (Sandboxed Python)

```bash
docker build -t deno-docker:latest -f ./mcps/deno/Dockerfile ./mcps/deno
```

### Install MCP Servers

```bash
# Web search
npm install -g @modelcontextprotocol/server-duckduckgo

# File operations
npm install -g @modelcontextprotocol/server-filesystem

# GitHub integration (requires GITHUB_TOKEN in .env)
npm install -g @modelcontextprotocol/server-github
```

## 🐛 Troubleshooting

### "uv: command not found"

Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### "ANTHROPIC_API_KEY not found"

1. Make sure `.env` file exists
2. Check that you added the API key
3. Verify no extra spaces or quotes

### Tests failing

```bash
# Clean and reinstall
rm -rf .venv
./setup.sh
./run_tests.sh
```

### Agent crashes on startup

1. Check Python version: `python3 --version` (need 3.11+)
2. Check dependencies: `uv pip list`
3. View error logs carefully

## 📚 Next Steps

### Learn the Architecture

- Read `README.md` for full documentation
- Check `WORKFLOW.md` for visual diagrams
- Study `agent.py` to understand StateGraph

### Customize

- Add custom tools in `tools/local_tools.py`
- Modify UI colors in `agent.py`
- Configure MCP servers in `tools/mcp_tools.py`

### Experiment

```
Create a new file called hello.py
Run pytest on the tests directory
Search for all markdown files
Help me understand the project structure
```

## 🎓 Understanding the Flow

### Basic Workflow

1. **You ask** → User input collected
2. **Claude thinks** → Model processes request
3. **Tools execute** → If needed (file read, web search, etc.)
4. **Response shown** → Results displayed in terminal
5. **Loop continues** → Ready for next query

### Example Session

```
You 👤: Show me the content of main.py

🔧 Executing tool: read_file
Arguments: {'file_path': 'main.py'}

✓ Tool Result: [file contents shown]

🤖 Assistant: Here's the main.py file...
[formatted response]

You 👤: What does it do?

🤖 Assistant: This is the entry point...
[explanation without tools]
```

## 💡 Pro Tips

1. **Be specific** - "Show me agent.py" > "show code"
2. **Chain requests** - "Read main.py and run tests"
3. **Use help** - Type `help` anytime
4. **Check tools** - Type `tools` to see what's available
5. **Conversation memory** - The agent remembers context
6. **Debug mode** - Check `checkpoints.db` with SQLite

## 🔒 Security Notes

- API keys are in `.env` (gitignored)
- MCP servers run in Docker for isolation
- File operations have full access (be careful!)
- No auto-approval for destructive operations yet

## 📊 Resource Usage

- **Startup time**: 1-2 seconds
- **Memory**: ~100-200MB
- **Disk**: ~500MB (including dependencies)
- **Network**: Only for API calls and MCP tools

## 🆘 Getting Help

### In the Assistant

```
help       # Built-in help
tools      # See available tools
exit       # Exit gracefully
```

### Documentation

- `README.md` - Complete guide
- `QUICKSTART.md` - 5-minute setup
- `EXAMPLES.md` - Usage examples
- `DOCKER_SETUP.md` - Docker configuration
- `PROJECT_SUMMARY.md` - Technical overview

### Common Issues

| Issue | Solution |
|-------|----------|
| API key error | Check `.env` file |
| Import errors | Run `uv sync` |
| Tests fail | Run `./setup.sh` again |
| Docker issues | Check Docker daemon running |
| Tool not found | Check tool is installed (npm/uv) |

## ✨ You're Ready!

If all checks pass, you're ready to use your AI coding assistant!

```bash
# Start coding with AI assistance
uv run main.py
```

**Happy coding! 🚀**

---

*Questions? Check the documentation or inspect the code - it's well-commented!*
