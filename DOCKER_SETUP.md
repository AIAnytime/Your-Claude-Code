# 🐳 Docker Setup Guide

Instructions for setting up Docker-based MCP servers.

## Deno MCP (Sandboxed Python)

The Deno MCP server provides safe Python code execution in a WebAssembly sandbox.

### Build the Docker Image

```bash
docker build -t deno-docker:latest -f ./mcps/deno/Dockerfile ./mcps/deno
```

### Usage

The Deno MCP is configured to run on-demand when the assistant needs to execute Python code in a sandbox. No manual container startup is required - the MCP toolkit will spawn the container automatically.

### Verify Installation

```bash
# Check if the image was built
docker images | grep deno-docker
```

## Desktop Commander MCP (Optional)

For enhanced file system operations with Docker isolation:

### Create a test directory

```bash
mkdir -p test_workspace
```

### Run with Desktop Commander

When using the assistant, it will automatically spawn the Desktop Commander MCP with Docker bind mounts restricted to the test directory for safety.

## MCP Server Architecture

```
┌─────────────────┐
│  Main Agent     │
│  (Claude)       │
└────────┬────────┘
         │
         │ Needs Tool
         ▼
┌─────────────────┐
│  MCP Toolkit    │
│  (langchain-mcp)│
└────────┬────────┘
         │
         │ Spawn Container
         ▼
┌─────────────────┐
│  Docker         │
│  Container      │
│  (Deno/Node)    │
└────────┬────────┘
         │
         │ Execute & Return
         ▼
┌─────────────────┐
│  Tool Result    │
│  → Agent        │
└─────────────────┘
```

## Resource Management

- Containers are spawned **on-demand**
- They terminate after task completion
- CPU/Memory usage is minimal and spiky
- No persistent containers running

## Security Considerations

### Sandboxing
- Deno runs Python in WebAssembly (Pyodide)
- No direct system access
- Limited file system access via bind mounts

### File System Isolation
Configure Desktop Commander to only access specific directories:

```bash
# Example: Restrict to test_workspace only
docker run -v $(pwd)/test_workspace:/workspace deno-docker
```

### Network Isolation
By default, MCP containers have limited network access. To disable network entirely:

```bash
docker run --network none deno-docker
```

## Troubleshooting

### Docker not found
```bash
# macOS
brew install docker

# Or install Docker Desktop
https://www.docker.com/products/docker-desktop
```

### Permission denied
```bash
# Add user to docker group (Linux)
sudo usermod -aG docker $USER
# Then log out and back in
```

### Container won't start
```bash
# Check Docker daemon
docker ps

# View logs
docker logs <container_id>

# Clean up old containers
docker system prune
```

### Image build fails
```bash
# Clear build cache
docker builder prune

# Rebuild without cache
docker build --no-cache -t deno-docker:latest -f ./mcps/deno/Dockerfile ./mcps/deno
```

## Advanced Configuration

### Custom Memory Limits

```bash
docker run --memory="512m" --memory-swap="512m" deno-docker
```

### Custom CPU Limits

```bash
docker run --cpus="1.0" deno-docker
```

### Volume Mounts for Development

```bash
docker run -v $(pwd):/app -v $(pwd)/data:/data deno-docker
```

## MCP Server List

Current and potential MCP servers:

- ✅ **Desktop Commander** - File system operations
- ✅ **Deno MCP** - Sandboxed Python execution  
- ✅ **DuckDuckGo** - Web search
- ✅ **GitHub** - Repository management
- 🔄 **PostgreSQL** - Database operations (future)
- 🔄 **Redis** - Cache operations (future)
- 🔄 **AWS** - Cloud operations (future)

## Notes

- **Always** use `uv` to run Python scripts
- **Never** use `python` or `python3` directly
- Docker containers are ephemeral and stateless
- All state is persisted in `checkpoints.db` on the host

---

For more information on MCP, see: https://modelcontextprotocol.io/
