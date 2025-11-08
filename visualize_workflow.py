#!/usr/bin/env python3
"""
Generate a Mermaid diagram of the agent workflow
"""

def generate_mermaid_diagram():
    """Generate and display the workflow diagram"""
    diagram = """
# Agent Workflow Diagram

```mermaid
graph TD
    A[👤 User Input] --> B[🤖 Model Response]
    B --> C{Tool Call?}
    C -->|Yes| D[🔧 Tool Execution]
    C -->|No| A
    D --> B
    
    style A fill:#90EE90
    style B fill:#87CEEB
    style C fill:#FFD700
    style D fill:#FFA500
```

## State Flow

```mermaid
stateDiagram-v2
    [*] --> UserInput
    UserInput --> ModelResponse
    ModelResponse --> CheckTool
    CheckTool --> ToolUse: has tool_calls
    CheckTool --> UserInput: no tool_calls
    ToolUse --> ModelResponse
```

## Complete Architecture

```mermaid
graph LR
    subgraph "Agent Core"
        A[StateGraph]
        B[AgentState]
        C[Checkpointer]
    end
    
    subgraph "Tools"
        D[Local Tools]
        E[MCP Tools]
    end
    
    subgraph "LLM"
        F[Claude 3.5 Sonnet]
    end
    
    A --> B
    A --> C
    A --> D
    A --> E
    A --> F
    
    style A fill:#4169E1
    style B fill:#32CD32
    style C fill:#FFD700
    style D fill:#FF6347
    style E fill:#9370DB
    style F fill:#20B2AA
```

## Message Flow

```mermaid
sequenceDiagram
    participant User
    participant Agent
    participant LLM
    participant Tools
    participant DB
    
    User->>Agent: Input Query
    Agent->>DB: Load State
    Agent->>LLM: Process with Context
    
    alt Tool Needed
        LLM->>Agent: Tool Call Request
        Agent->>Tools: Execute Tool
        Tools->>Agent: Tool Result
        Agent->>LLM: Continue with Result
    end
    
    LLM->>Agent: Final Response
    Agent->>DB: Save State
    Agent->>User: Display Response
```
"""
    
    print(diagram)
    
    # Also save to file
    with open("WORKFLOW.md", "w") as f:
        f.write(diagram)
    
    print("\n✓ Workflow diagrams saved to WORKFLOW.md")
    print("  View on GitHub or in a Mermaid-compatible viewer")


if __name__ == "__main__":
    generate_mermaid_diagram()
