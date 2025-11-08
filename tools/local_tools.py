"""
Local tools for file operations and testing
"""
import os
import subprocess
from pathlib import Path
from typing import List
from langchain_core.tools import tool


@tool
def read_file(file_path: str) -> str:
    """
    Read and return the contents of a file.
    
    Args:
        file_path: Path to the file to read (relative or absolute)
    
    Returns:
        File contents as a string
    """
    try:
        # Convert to absolute path if relative
        if not os.path.isabs(file_path):
            file_path = os.path.join(os.getcwd(), file_path)
        
        # Check if file exists
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' does not exist"
        
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return f"Content of {file_path}:\n\n{content}"
    
    except Exception as e:
        return f"Error reading file: {str(e)}"


@tool
def list_files(directory: str = ".") -> str:
    """
    List all files and directories in a given directory.
    
    Args:
        directory: Directory path to list (default: current directory)
    
    Returns:
        List of files and directories
    """
    try:
        # Convert to absolute path
        if not os.path.isabs(directory):
            directory = os.path.join(os.getcwd(), directory)
        
        if not os.path.exists(directory):
            return f"Error: Directory '{directory}' does not exist"
        
        if not os.path.isdir(directory):
            return f"Error: '{directory}' is not a directory"
        
        # List contents
        items = []
        for item in sorted(os.listdir(directory)):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                items.append(f"📁 {item}/")
            else:
                size = os.path.getsize(item_path)
                items.append(f"📄 {item} ({size} bytes)")
        
        return f"Contents of {directory}:\n\n" + "\n".join(items)
    
    except Exception as e:
        return f"Error listing directory: {str(e)}"


@tool
def write_file(file_path: str, content: str) -> str:
    """
    Write content to a file. Creates the file if it doesn't exist.
    
    Args:
        file_path: Path to the file to write
        content: Content to write to the file
    
    Returns:
        Success or error message
    """
    try:
        # Convert to absolute path if relative
        if not os.path.isabs(file_path):
            file_path = os.path.join(os.getcwd(), file_path)
        
        # Create parent directories if they don't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return f"Successfully wrote {len(content)} characters to {file_path}"
    
    except Exception as e:
        return f"Error writing file: {str(e)}"


@tool
def run_pytest(test_path: str = ".", args: str = "-v") -> str:
    """
    Run pytest on specified path with given arguments.
    
    Args:
        test_path: Path to test file or directory (default: current directory)
        args: Additional pytest arguments (default: "-v" for verbose)
    
    Returns:
        Test results
    """
    try:
        # Convert to absolute path if relative
        if not os.path.isabs(test_path):
            test_path = os.path.join(os.getcwd(), test_path)
        
        # Build command
        cmd = ["pytest", test_path] + args.split()
        
        # Run pytest
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        output = result.stdout + result.stderr
        
        if result.returncode == 0:
            return f"✓ All tests passed!\n\n{output}"
        else:
            return f"✗ Some tests failed (exit code {result.returncode})\n\n{output}"
    
    except subprocess.TimeoutExpired:
        return "Error: Test execution timed out (30s limit)"
    except FileNotFoundError:
        return "Error: pytest not found. Make sure pytest is installed."
    except Exception as e:
        return f"Error running tests: {str(e)}"


@tool
def search_files(pattern: str, directory: str = ".", file_extension: str = "") -> str:
    """
    Search for files matching a pattern in a directory.
    
    Args:
        pattern: Search pattern (substring match in filename)
        directory: Directory to search in (default: current directory)
        file_extension: Optional file extension filter (e.g., ".py")
    
    Returns:
        List of matching files
    """
    try:
        # Convert to absolute path
        if not os.path.isabs(directory):
            directory = os.path.join(os.getcwd(), directory)
        
        if not os.path.exists(directory):
            return f"Error: Directory '{directory}' does not exist"
        
        matches = []
        for root, dirs, files in os.walk(directory):
            # Skip hidden directories and common ignore patterns
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules']]
            
            for file in files:
                # Skip hidden files
                if file.startswith('.'):
                    continue
                
                # Check extension if specified
                if file_extension and not file.endswith(file_extension):
                    continue
                
                # Check pattern match
                if pattern.lower() in file.lower():
                    rel_path = os.path.relpath(os.path.join(root, file), directory)
                    matches.append(rel_path)
        
        if matches:
            return f"Found {len(matches)} matching files:\n\n" + "\n".join(f"• {m}" for m in matches)
        else:
            return f"No files matching '{pattern}' found in {directory}"
    
    except Exception as e:
        return f"Error searching files: {str(e)}"


@tool
def get_file_info(file_path: str) -> str:
    """
    Get detailed information about a file.
    
    Args:
        file_path: Path to the file
    
    Returns:
        File information including size, modification time, etc.
    """
    try:
        # Convert to absolute path if relative
        if not os.path.isabs(file_path):
            file_path = os.path.join(os.getcwd(), file_path)
        
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' does not exist"
        
        stat = os.stat(file_path)
        from datetime import datetime
        
        info = [
            f"File: {file_path}",
            f"Size: {stat.st_size} bytes",
            f"Modified: {datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')}",
            f"Created: {datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')}",
            f"Is directory: {os.path.isdir(file_path)}",
        ]
        
        return "\n".join(info)
    
    except Exception as e:
        return f"Error getting file info: {str(e)}"


def get_local_tools() -> List:
    """Return list of all local tools"""
    return [
        read_file,
        list_files,
        write_file,
        run_pytest,
        search_files,
        get_file_info,
    ]
