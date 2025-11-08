#!/usr/bin/env python3
"""
Script to inspect messages stored in checkpoints.db
"""
import sqlite3
import json
from datetime import datetime

def inspect_checkpoints():
    """Inspect the checkpoints database"""
    
    try:
        conn = sqlite3.connect('checkpoints.db')
        cursor = conn.cursor()
        
        print("=" * 80)
        print("🔍 CHECKPOINT DATABASE INSPECTION")
        print("=" * 80)
        
        # Get table info
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"\n📊 Tables: {[t[0] for t in tables]}\n")
        
        # Check writes table
        print("=" * 80)
        print("📝 WRITES TABLE (Message History)")
        print("=" * 80)
        
        cursor.execute("""
            SELECT thread_id, checkpoint_ns, checkpoint_id, task_id, idx, channel, type, value
            FROM writes 
            ORDER BY idx DESC 
            LIMIT 10
        """)
        
        writes = cursor.fetchall()
        
        if not writes:
            print("❌ No messages found in database yet.")
            print("💡 Run the agent first: uv run main.py")
        else:
            for i, write in enumerate(writes, 1):
                thread_id, ns, checkpoint_id, task_id, idx, channel, msg_type, value = write
                
                print(f"\n{'─' * 80}")
                print(f"Message #{i}")
                print(f"{'─' * 80}")
                print(f"Thread ID:     {thread_id}")
                print(f"Checkpoint ID: {checkpoint_id[:20]}...")
                print(f"Index:         {idx}")
                print(f"Channel:       {channel}")
                print(f"Type:          {msg_type}")
                
                # Try to parse the value
                try:
                    if value:
                        data = json.loads(value)
                        print(f"\n📦 Message Data:")
                        
                        # Pretty print based on message type
                        if isinstance(data, list):
                            for msg in data:
                                print_message(msg)
                        elif isinstance(data, dict):
                            print_message(data)
                        else:
                            print(f"  {data}")
                except json.JSONDecodeError:
                    print(f"  Raw value: {value[:200]}...")
        
        # Check checkpoints table
        print("\n" + "=" * 80)
        print("💾 CHECKPOINTS TABLE (State Snapshots)")
        print("=" * 80)
        
        cursor.execute("""
            SELECT thread_id, checkpoint_ns, checkpoint_id, parent_checkpoint_id
            FROM checkpoints 
            ORDER BY checkpoint_id DESC 
            LIMIT 5
        """)
        
        checkpoints = cursor.fetchall()
        
        for i, cp in enumerate(checkpoints, 1):
            thread_id, ns, cp_id, parent_id = cp
            print(f"\n{i}. Thread: {thread_id}")
            print(f"   Checkpoint: {cp_id[:30]}...")
            print(f"   Parent:     {parent_id[:30] if parent_id else 'None'}...")
        
        # Statistics
        print("\n" + "=" * 80)
        print("📊 STATISTICS")
        print("=" * 80)
        
        cursor.execute("SELECT COUNT(*) FROM writes")
        write_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM checkpoints")
        checkpoint_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(DISTINCT thread_id) FROM writes")
        thread_count = cursor.fetchone()[0]
        
        print(f"Total Messages:    {write_count}")
        print(f"Total Checkpoints: {checkpoint_count}")
        print(f"Active Threads:    {thread_count}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    except FileNotFoundError:
        print("❌ checkpoints.db not found!")
        print("💡 Run the agent first: uv run main.py")

def print_message(msg):
    """Pretty print a message"""
    if not isinstance(msg, dict):
        print(f"  {msg}")
        return
    
    msg_type = msg.get('type', 'unknown')
    
    if msg_type == 'human':
        content = msg.get('content', '')
        print(f"  👤 USER: {content[:100]}")
    
    elif msg_type == 'ai':
        content = msg.get('content', '')
        tool_calls = msg.get('tool_calls', [])
        
        if isinstance(content, list):
            # Handle content blocks
            text_parts = []
            for block in content:
                if isinstance(block, dict) and 'text' in block:
                    text_parts.append(block['text'])
            content = ' '.join(text_parts)
        
        print(f"  🤖 AI: {content[:100]}")
        
        if tool_calls:
            print(f"  🔧 Tool Calls:")
            for tc in tool_calls:
                if isinstance(tc, dict):
                    name = tc.get('name', 'unknown')
                    args = tc.get('args', {})
                    print(f"     - {name}({args})")
    
    elif msg_type == 'tool':
        content = msg.get('content', '')
        tool_call_id = msg.get('tool_call_id', '')
        print(f"  🔧 TOOL RESULT (id: {tool_call_id[:20]}...)")
        print(f"     {content[:100]}...")
    
    elif msg_type == 'system':
        content = msg.get('content', '')
        print(f"  📋 SYSTEM: {content[:100]}...")
    
    else:
        print(f"  ❓ {msg_type}: {str(msg)[:100]}")

if __name__ == "__main__":
    inspect_checkpoints()
