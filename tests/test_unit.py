"""
iamlistening Unit Testing
"""

import pytest
import asyncio
from unittest.mock import patch, AsyncMock, MagicMock

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


def test_init(frasier):
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
async def test_get_latest_message(frasier, message):
    await frasier.handle_message(message)
    assert await frasier.get_latest_message() == message

@pytest.mark.asyncio
async def test_start_method():
    # Mock the necessary dependencies
    settings = {
        'telethon_api_id': 'your_telethon_api_id',
        'telethon_api_hash': 'your_telethon_api_hash',
        'bot_token': 'your_bot_token'
    }

    bot_client_mock = AsyncMock()
    telegram_client_mock = MagicMock(return_value=bot_client_mock)

    # Replace the post_init method with the mocked implementation
    async def post_init_mock():
        pass

    # Create an instance of the Listener class
    listener = Listener()

    with patch('telethon.TelegramClient', telegram_client_mock):
        with patch('iamlistening.Listener.post_init', post_init_mock):
            # Set the settings before calling the start method
            listener.settings = settings

            # Call the start method
            await listener.start()

    # Assert the expected behavior
    telegram_client_mock.assert_called_with(
        None,
        settings['telethon_api_id'],
        settings['telethon_api_hash']
    )
    bot_client_mock.start.assert_called_with(bot_token=settings['bot_token'])
    post_init_mock.assert_awaited_once()

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