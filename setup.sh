#!/bin/bash
# Setup script for Claude Code Assistant

set -e

echo "🚀 Setting up Claude Code Assistant..."
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo -e "${RED}❌ uv is not installed${NC}"
    echo ""
    echo "Please install uv first:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo ""
    exit 1
fi

echo -e "${GREEN}✓ uv found${NC}"

# Check if .env exists
if [ ! -f .env ]; then
    echo -e "${YELLOW}⚠ .env file not found${NC}"
    echo "Creating .env from .env.example..."
    cp .env.example .env
    echo -e "${YELLOW}⚠ Please edit .env and add your ANTHROPIC_API_KEY${NC}"
    echo ""
fi

# Create virtual environment and sync dependencies
echo ""
echo "📦 Installing dependencies..."
uv sync

echo ""
echo -e "${GREEN}✓ Setup complete!${NC}"
echo ""
echo "Next steps:"
echo "  1. Edit .env and add your ANTHROPIC_API_KEY"
echo "  2. Run the assistant:"
echo "     ${GREEN}uv run main.py${NC}"
echo ""
echo "Optional: Install MCP servers for additional features:"
echo "  - Desktop Commander: npm install -g @modelcontextprotocol/server-filesystem"
echo "  - DuckDuckGo: npm install -g @modelcontextprotocol/server-duckduckgo"
echo "  - GitHub: npm install -g @modelcontextprotocol/server-github"
echo ""
echo "📚 See README.md for more information"
echo ""
