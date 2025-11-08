#!/usr/bin/env python3
"""
Main entry point for the Claude Code Assistant

A minimalist AI coding assistant using LangGraph and MCP
"""
import asyncio
import os
import sys
from dotenv import load_dotenv
from agent import CodeAssistantAgent
from rich.console import Console

console = Console()


async def main():
    """Main function to run the assistant"""
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    if not os.getenv("ANTHROPIC_API_KEY"):
        console.print("[bold red]❌ Error: ANTHROPIC_API_KEY not found![/bold red]")
        console.print("[yellow]Please set your Anthropic API key in .env file[/yellow]")
        console.print("[yellow]Copy .env.example to .env and add your key[/yellow]")
        sys.exit(1)
    
    # Initialize agent
    agent = CodeAssistantAgent()
    
    try:
        # Async initialization
        await agent.initialize()
        
        # Run the interactive loop
        await agent.run()
        
    except KeyboardInterrupt:
        console.print("\n[bold cyan]👋 Interrupted by user[/bold cyan]")
    except Exception as e:
        console.print(f"[bold red]❌ Fatal error: {e}[/bold red]")
        import traceback
        traceback.print_exc()
    finally:
        # Cleanup
        await agent.cleanup()


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
