"""Tests for APIVerveToolkit."""

import pytest
from unittest.mock import patch

from langchain_apiverve import APIVerveToolkit
from langchain_apiverve.toolkit import load_api_schemas


def test_toolkit_requires_api_key():
    """Test toolkit raises error without API key."""
    with pytest.raises(ValueError, match="API key is required"):
        with patch('langchain_apiverve.toolkit.load_api_schemas', return_value={"schemas": {}}):
            APIVerveToolkit()


def test_toolkit_initialization(mock_api_key, mock_schemas):
    """Test toolkit can be initialized with API key."""
    with patch('langchain_apiverve.toolkit.load_api_schemas', return_value=mock_schemas):
        toolkit = APIVerveToolkit(api_key=mock_api_key)
        assert toolkit.api_key == mock_api_key
        assert toolkit.total_apis == 2


def test_get_tools(mock_api_key, mock_schemas):
    """Test getting tools from toolkit."""
    with patch('langchain_apiverve.toolkit.load_api_schemas', return_value=mock_schemas):
        toolkit = APIVerveToolkit(api_key=mock_api_key)
        tools = toolkit.get_tools()
        assert len(tools) == 2


def test_get_tools_by_category(mock_api_key, mock_schemas):
    """Test filtering tools by category."""
    with patch('langchain_apiverve.toolkit.load_api_schemas', return_value=mock_schemas):
        toolkit = APIVerveToolkit(api_key=mock_api_key)
        tools = toolkit.get_tools(categories=["Validation"])
        assert len(tools) == 1
        assert tools[0].name == "emailvalidator"


def test_get_single_tool(mock_api_key, mock_schemas):
    """Test getting a single tool by ID."""
    with patch('langchain_apiverve.toolkit.load_api_schemas', return_value=mock_schemas):
        toolkit = APIVerveToolkit(api_key=mock_api_key)
        tool = toolkit.get_tool("emailvalidator")
        assert tool is not None
        assert tool.name == "emailvalidator"


def test_list_available_apis(mock_api_key, mock_schemas):
    """Test listing available APIs."""
    with patch('langchain_apiverve.toolkit.load_api_schemas', return_value=mock_schemas):
        toolkit = APIVerveToolkit(api_key=mock_api_key)
        apis = toolkit.list_available_apis()
        assert len(apis) == 2


def test_list_categories(mock_api_key, mock_schemas):
    """Test listing categories."""
    with patch('langchain_apiverve.toolkit.load_api_schemas', return_value=mock_schemas):
        toolkit = APIVerveToolkit(api_key=mock_api_key)
        categories = toolkit.list_categories()
        assert "Validation" in categories
        assert "Lookup" in categories


def test_schema_fetch_failure(mock_api_key):
    """Test that toolkit raises error when schemas cannot be fetched."""
    with patch('langchain_apiverve.toolkit.load_api_schemas') as mock_load:
        mock_load.side_effect = RuntimeError("Failed to fetch API schemas")
        with pytest.raises(RuntimeError, match="Failed to fetch"):
            APIVerveToolkit(api_key=mock_api_key)
