"""
iamlistening Unit Testing
"""

import pytest
import asyncio
from unittest.mock import Mock, AsyncMock, patch, MagicMock

from iamlistening import Listener
from iamlistening.config import settings

@pytest.fixture
def listener():
    return Listener()

@pytest.fixture
def message():
    return "Test message"

@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

# Mock the settings module
@pytest.fixture()
def mock_settings():
    with patch("iamlistening.config.settings") as mock_settings:
        mock_settings.discord_webhook_id = False
        mock_settings.matrix_hostname = True
        mock_settings.telethon_api_id = False
        mock_settings.bot_token = "fake_token"
        yield mock_settings

@pytest.fixture(name="mock_discord")
def mock_discord_fixture():
    """Fixture to create an listener object for testing."""
    class Settings:
        settings.discord_webhook_id = "12345678901"
        settings.discord_webhook_token = "1234567890"
        settings.bot_token = "test_bot_token"
        settings.bot_channel_id = "1234567890"
        settings.ping = "8.8.8.8"
    return Settings()

@pytest.fixture(name="mock_telegram")
def mock_telegram_fixture():
    """Fixture to create an listener object for testing."""
    class Settings:
        settings.telethon_api_id = "123456789"
        settings.telethon_api_hash = "123456789"
        settings.bot_token = "test_bot_token"
        settings.bot_channel_id = "1234567890"
    return Settings()


@pytest.fixture(name="mock_matrix")
def mock_matrix_fixture():
    """Fixture to create an listener object for testing."""
    class Settings:
        settings.matrix_hostname = "123456789"
        settings.matrix_user = "123456789"
        settings.matrix_pass = "123456789"
        settings.bot_token = "test_bot_token"
        settings.bot_channel_id = "1234567890"
    return Settings()


def test_init(listener):
    assert listener is not None

def test_discord(mock_discord):
    Listener()
    assert listener is not None

def test_telegram(mock_telegram):
    Listener()
    assert listener is not None

def test_matrix(mock_matrix):
    Listener()
    assert listener is not None

@pytest.mark.asyncio
async def test_get_latest_message(listener, message):
    await listener.handle_message(message)
    assert await listener.get_latest_message() == message

