"""Pytest configuration and fixtures."""

import pytest
from unittest.mock import MagicMock, patch

from langchain_apiverve import APIVerveClient


# Mock schema data for testing
MOCK_SCHEMAS = {
    "schemas": {
        "emailvalidator": {
            "apiId": "emailvalidator",
            "title": "Email Validator",
            "description": "Validate email addresses",
            "category": "Validation",
            "methods": ["GET"],
            "parameters": [
                {"name": "email", "type": "string", "required": True, "description": "Email to validate"}
            ]
        },
        "dnslookup": {
            "apiId": "dnslookup",
            "title": "DNS Lookup",
            "description": "Lookup DNS records",
            "category": "Lookup",
            "methods": ["GET"],
            "parameters": [
                {"name": "domain", "type": "string", "required": True, "description": "Domain to lookup"},
                {"name": "type", "type": "string", "required": False, "description": "Record type"}
            ]
        }
    },
    "totalAPIs": 2
}


@pytest.fixture
def mock_api_key():
    """Return a mock API key."""
    return "test-api-key-12345"


@pytest.fixture
def mock_client(mock_api_key):
    """Return a mock APIVerve client."""
    with patch.object(APIVerveClient, 'call_api') as mock_call:
        mock_call.return_value = {
            "status": "ok",
            "error": None,
            "data": {"result": "test"}
        }
        client = APIVerveClient(api_key=mock_api_key)
        yield client


@pytest.fixture
def mock_schemas():
    """Return mock API schemas."""
    return MOCK_SCHEMAS
