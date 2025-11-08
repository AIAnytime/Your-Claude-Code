"""
MCP (Model Context Protocol) tools integration
Supports: Desktop Commander, DuckDuckGo, GitHub, and Sandboxed Python
"""
import os
from typing import List
from langchain_core.tools import BaseTool


async def get_mcp_tools() -> List[BaseTool]:
    """
    Load and return MCP tools.
    
    This function attempts to load various MCP servers:
    - Desktop Commander (file operations)
    - DuckDuckGo (web search)
    - GitHub (repository management)
    - Sandboxed Python (safe code execution)
    
    Returns:
        List of MCP tools
    """
    tools = []
    
    try:
        from langchain_mcp import MCPToolkit
        
        # Desktop Commander MCP (file system operations)
        try:
            # Note: This requires the desktop-commander MCP server to be installed
            # Install with: npm install -g @modelcontextprotocol/server-filesystem
            desktop_toolkit = MCPToolkit(
                server_params={
                    "command": "npx",
                    "args": ["-y", "@modelcontextprotocol/server-filesystem", os.getcwd()],
                }
            )
            desktop_tools = await desktop_toolkit.get_tools()
            tools.extend(desktop_tools)
        except Exception:
            pass  # MCP servers are optional
        
        # DuckDuckGo MCP (web search)
        try:
            ddg_toolkit = MCPToolkit(
                server_params={
                    "command": "npx",
                    "args": ["-y", "@modelcontextprotocol/server-duckduckgo"],
                }
            )
            ddg_tools = await ddg_toolkit.get_tools()
            tools.extend(ddg_tools)
        except Exception:
            pass  # MCP servers are optional
        
        # GitHub MCP
        try:
            github_token = os.getenv("GITHUB_TOKEN")
            if github_token:
                github_toolkit = MCPToolkit(
                    server_params={
                        "command": "npx",
                        "args": ["-y", "@modelcontextprotocol/server-github"],
                        "env": {"GITHUB_TOKEN": github_token}
                    }
                )
                github_tools = await github_toolkit.get_tools()
                tools.extend(github_tools)
        except Exception:
            pass  # MCP servers are optional
        
    except ImportError:
        pass  # MCP is optional
    
    return tools
