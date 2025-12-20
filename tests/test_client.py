"""Tests for APIVerve client."""

import pytest
from unittest.mock import patch, MagicMock
from langchain_apiverve import APIVerveClient, APIVerveError


def test_client_initialization(mock_api_key):
    """Test client initialization."""
    client = APIVerveClient(api_key=mock_api_key)
    assert client.api_key == mock_api_key
    assert client.base_url == "https://api.apiverve.com/v1"


def test_client_custom_base_url(mock_api_key):
    """Test client with custom base URL."""
    client = APIVerveClient(api_key=mock_api_key, base_url="https://custom.api.com")
    assert client.base_url == "https://custom.api.com"


def test_client_session_headers(mock_api_key):
    """Test client sets correct headers."""
    client = APIVerveClient(api_key=mock_api_key)
    session = client.session
    assert session.headers["x-api-key"] == mock_api_key
    assert "langchain-apiverve" in session.headers["User-Agent"]


def test_client_get_method(mock_api_key):
    """Test GET request method."""
    client = APIVerveClient(api_key=mock_api_key)
    with patch.object(client.session, 'get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "ok"}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = client.call_api("test", {"param": "value"}, method="GET")
        assert result == {"status": "ok"}
        mock_get.assert_called_once()


def test_client_post_method(mock_api_key):
    """Test POST request method."""
    client = APIVerveClient(api_key=mock_api_key)
    with patch.object(client.session, 'post') as mock_post:
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "ok"}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        result = client.call_api("test", {"param": "value"}, method="POST")
        assert result == {"status": "ok"}
        mock_post.assert_called_once()
