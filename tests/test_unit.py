"""
iamlistening Unit Testing
"""

import pytest
import asyncio
from unittest.mock import AsyncMock, patch
from telethon import TelegramClient, errors
from iamlistening import Listener
from iamlistening.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")

@pytest.fixture(name="frasier")
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

@pytest.mark.asyncio
async def test_fixture(frasier):
    assert frasier is not None
    assert settings.VALUE == "On Testing"

# Mock the settings module
@pytest.fixture()
def mock_settings():
    with patch("iamlistening.config.settings") as mock_settings:
        mock_settings.matrix_hostname = True
        mock_settings.telethon_api_id = False
        mock_settings.bot_token = "fake_token"
        yield mock_settings


@pytest.fixture(name="mock_telegram")
def mock_telegram_fixture():
    """Fixture to create an listener object for testing."""
    class Settings:
        settings.telethon_api_id = "123456789"
        settings.telethon_api_hash = "123456789"
        settings.bot_token = "test_bot_token"
        settings.bot_channel_id = "1234567890"
    return Settings()


def test_init(frasier):
    assert listener is not None

def test_telegram(mock_telegram):
    Listener()
    assert listener is not None

@pytest.mark.asyncio
async def test_get_latest_message(frasier, message):
    await frasier.handle_message(message)
    assert await frasier.get_latest_message() == message

@pytest.mark.asyncio
async def test_telegram_function():
    TelegramClient = AsyncMock()
    TelegramClient.run_until_disconnected = AsyncMock()
    listener = Listener()
    assert listener is not None
    assert isinstance(listener, Listener)
    assert TelegramClient.assert_called_once
    assert TelegramClient.run_until_disconnected.assert_called_once


@pytest.mark.asyncio
async def test_listener_telegram():
    listener_test = Listener()
    print(listener_test)
    assert listener_test is not None
    assert isinstance(listener_test, Listener)
    await listener_test.handle_message("hello")
    msg = await listener_test.get_latest_message()
    print(msg)
    assert msg == "hello"


@pytest.mark.asyncio
async def test_listener_run():
    start = AsyncMock()
    listener_test = Listener()
    await listener_test.run_forever(max_iterations=1)
    assert start.assert_awaited_once()


@pytest.mark.asyncio
async def test_listener_run_error():
    with pytest.raises(errors.ApiIdInvalidError):
        start = AsyncMock()
        listener_test = Listener()
        await listener_test.run_forever(max_iterations=1)
        assert start.assert_awaited_once()
