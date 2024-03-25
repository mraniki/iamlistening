"""
iamlistening Unit Testing
"""

import asyncio
from unittest.mock import MagicMock

import pytest

from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.protocol import (
    DiscordHandler,
    GuildedHandler,
    LemmyHandler,
    MastodonHandler,
    MatrixHandler,
    TelegramHandler,
    TwitchHandler,
)


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="ial")


@pytest.fixture(name="listener")
def listener():
    settings.setenv("ial")
    return Listener()


@pytest.fixture(name="message")
def message():
    return "hello"


@pytest.mark.asyncio
async def test_listener_fixture(listener):
    assert listener is not None
    assert isinstance(listener, Listener)
    assert listener.clients is not None


def test_listener_init_raises_exception():
    with pytest.raises(Exception):
        with settings.setenv("exception"):
            Listener()


@pytest.mark.asyncio
async def test_get_info(listener):
    result = listener.get_info()
    assert result is not None
    assert "ℹ️" in result


@pytest.mark.asyncio
async def test_listener_start(listener, message, caplog):
    loop = asyncio.get_running_loop()
    loop.create_task(listener.start())
    iteration = 0
    for client in listener.clients:
        client.connected = MagicMock()
        assert isinstance(
            client,
            (
                DiscordHandler,
                TelegramHandler,
                MatrixHandler,
                GuildedHandler,
                MastodonHandler,
                LemmyHandler,
                TwitchHandler,
            ),
        )

        assert client.platform is not None
        assert client.bot_token is not None
        assert client.bot_channel_id is not None
        assert client.iteration_count == 0
        iteration += 1
        await client.handle_message(message)
        msg = await client.get_latest_message()
        assert msg == message
        assert callable(client.start)
        assert callable(client.stop)
        assert callable(client.connected)
        assert callable(client.get_latest_message)
        assert callable(client.handle_message)
        assert callable(client.handle_iteration_limit)
        assert callable(client.disconnected)
        assert client.connected.called_once
        assert client.is_connected is True

        assert "Latest message telegram" in caplog.text
        # assert "been registered as an event" in caplog.text
        assert "client is online on revolt" in caplog.text
        assert "Frasier👂 on telegram:" in caplog.text
        if iteration >= 1:
            break
