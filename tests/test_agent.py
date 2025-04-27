"""Tests for the agent module."""

import os
import pytest
from unittest.mock import patch
from agent.agent import handle_task, _check_api_key

def test_check_api_key_missing():
    """Test that missing API key raises error."""
    with patch.dict(os.environ, clear=True):
        with pytest.raises(ValueError) as exc:
            _check_api_key()
        assert "OPENAI_API_KEY not found" in str(exc.value)

def test_check_api_key_present():
    """Test that present API key works."""
    with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-test123"}):
        _check_api_key()  # Should not raise

@pytest.mark.integration
def test_handle_task():
    """Integration test for handle_task.
    
    Requires valid OPENAI_API_KEY in environment.
    """
    response = handle_task("List the available tools")
    assert isinstance(response, str)
    assert len(response) > 0 