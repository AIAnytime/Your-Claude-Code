# Dockerfile for Deno MCP (Sandboxed Python Execution)
# Based on Pydantic AI's run-python MCP server

FROM denoland/deno:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /app

# Set permissions
RUN chmod -R 755 /app

# Install Pyodide for Python in WebAssembly
RUN deno cache --reload \
    https://deno.land/x/pyodide/mod.ts

# Default command (will be overridden by MCP server params)
CMD ["deno", "run", "--allow-all", "server.ts"]
