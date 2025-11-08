"""
Tests for local tools
"""
import os
import tempfile
import pytest
from tools.local_tools import (
    read_file,
    list_files,
    write_file,
    search_files,
    get_file_info,
)


def test_write_and_read_file():
    """Test writing and reading a file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "test.txt")
        content = "Hello, World!"
        
        # Write file
        write_result = write_file.invoke({"file_path": file_path, "content": content})
        assert "Successfully wrote" in write_result
        
        # Read file
        read_result = read_file.invoke({"file_path": file_path})
        assert content in read_result


def test_list_files():
    """Test listing files in a directory"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create some test files
        open(os.path.join(tmpdir, "file1.txt"), "w").close()
        open(os.path.join(tmpdir, "file2.py"), "w").close()
        os.makedirs(os.path.join(tmpdir, "subdir"))
        
        # List files
        result = list_files.invoke({"directory": tmpdir})
        
        assert "file1.txt" in result
        assert "file2.py" in result
        assert "subdir" in result


def test_search_files():
    """Test searching for files"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files
        open(os.path.join(tmpdir, "test_one.py"), "w").close()
        open(os.path.join(tmpdir, "test_two.py"), "w").close()
        open(os.path.join(tmpdir, "other.txt"), "w").close()
        
        # Search for Python files with 'test' in name
        result = search_files.invoke({
            "pattern": "test",
            "directory": tmpdir,
            "file_extension": ".py"
        })
        
        assert "test_one.py" in result
        assert "test_two.py" in result
        assert "other.txt" not in result


def test_get_file_info():
    """Test getting file information"""
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "info_test.txt")
        
        # Create file
        with open(file_path, "w") as f:
            f.write("test content")
        
        # Get info
        result = get_file_info.invoke({"file_path": file_path})
        
        assert "Size:" in result
        assert "Modified:" in result
        assert "Created:" in result


def test_read_nonexistent_file():
    """Test reading a file that doesn't exist"""
    result = read_file.invoke({"file_path": "/nonexistent/file.txt"})
    assert "Error" in result or "does not exist" in result


def test_write_file_creates_directories():
    """Test that write_file creates parent directories"""
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "subdir", "nested", "file.txt")
        
        result = write_file.invoke({"file_path": file_path, "content": "test"})
        
        assert "Successfully wrote" in result
        assert os.path.exists(file_path)
