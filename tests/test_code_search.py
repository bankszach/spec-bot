"""Tests for the code search tool."""

import subprocess
from unittest.mock import patch, MagicMock
from tools.code_search import code_search

def test_code_search_success():
    """Test successful code search."""
    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = "file1.py:10:def test()\nfile2.py:20:def test()"
    
    with patch('subprocess.run', return_value=mock_result) as mock_run:
        results = code_search("def test", "*.py")
        
        mock_run.assert_called_once()
        assert len(results) == 2
        assert "file1.py:10:def test()" in results
        assert "file2.py:20:def test()" in results

def test_code_search_no_matches():
    """Test code search with no matches."""
    mock_result = MagicMock()
    mock_result.returncode = 1
    mock_result.stdout = ""
    
    with patch('subprocess.run', return_value=mock_result):
        results = code_search("nonexistent", "*.py")
        assert results == []

def test_code_search_error():
    """Test code search with error."""
    mock_result = MagicMock()
    mock_result.returncode = 2
    mock_result.stderr = "Error message"
    
    with patch('subprocess.run', return_value=mock_result):
        results = code_search("pattern", "*.py")
        assert results == ["Error: Error message"]

def test_code_search_ripgrep_not_found():
    """Test code search when ripgrep is not installed."""
    with patch('subprocess.run', side_effect=FileNotFoundError):
        results = code_search("pattern", "*.py")
        assert results == ["Error: ripgrep (rg) not found. Please install it first."] 