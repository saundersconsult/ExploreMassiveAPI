"""Tests for API client."""

import pytest
from unittest.mock import Mock, patch
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def test_api_client_initialization():
    """Test API client initializes with config."""
    with patch.dict(os.environ, {"MASSIVE_API_KEY": "test_key"}):
        from src.api_client import MassiveAPIClient
        client = MassiveAPIClient(api_key="test_key")
        assert client.api_key == "test_key"


def test_api_client_missing_key():
    """Test API client raises error without API key."""
    with patch.dict(os.environ, {}, clear=True):
        from src.api_client import MassiveAPIClient
        with pytest.raises(ValueError):
            MassiveAPIClient()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
