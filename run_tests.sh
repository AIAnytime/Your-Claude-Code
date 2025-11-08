#!/bin/bash
# Test runner script - uses uv to run pytest

set -e

echo "🧪 Running Claude Code Assistant Tests"
echo "======================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check if .venv exists
if [ ! -d ".venv" ]; then
    echo -e "${YELLOW}⚠ Virtual environment not found. Running setup...${NC}"
    ./setup.sh
fi

echo -e "${CYAN}Running unit tests...${NC}"
echo ""

# Run pytest with uv
uv run pytest -v --tb=short

EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✅ All tests passed!${NC}"
else
    echo -e "${RED}❌ Some tests failed (exit code: $EXIT_CODE)${NC}"
fi

echo ""
echo "For more verbose output, run:"
echo "  ${CYAN}uv run pytest -vv${NC}"
echo ""
echo "To run specific tests:"
echo "  ${CYAN}uv run pytest tests/test_local_tools.py -v${NC}"
echo ""
echo "To see coverage:"
echo "  ${CYAN}uv run pytest --cov=. --cov-report=html${NC}"
echo ""

exit $EXIT_CODE
