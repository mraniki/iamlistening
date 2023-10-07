"""
iamlistening Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest

from iamlistening import Listener
from iamlistening.clients import (
    DiscordHandler,
    GuildedHandler,
    LemmyHandler,
    MastodonHandler,
    MatrixHandler,
    TelegramHandler,
    TwitchHandler,
)
from iamlistening.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="ial")


@pytest.fixture(name="listener")
def listener():
    settings.setenv('ial')
    return Listener()


@pytest.fixture(name="message")
def message():
    return "hello"


@pytest.mark.asyncio
async def test_listener_fixture(listener):
    assert listener is not None
    assert isinstance(listener, Listener)
    assert listener.clients is not None
    assert listener.clients[0].platform is not None
    assert listener.clients[0].bot_token is not None


def test_listener_init_raises_exception():
    with pytest.raises(Exception):
        with settings.setenv('exception'):
            listener = Listener()


@pytest.mark.asyncio
async def test_get_info(listener):
    result = listener.get_info()
    assert result is not None
    assert "ℹ️" in result

@pytest.mark.asyncio
async def test_listener_start(listener, message):
    loop = asyncio.get_running_loop()
    loop.create_task(listener.start())
    iteration = 0
    for client in listener.clients:
        client.connected = MagicMock()
        client.handle_message = AsyncMock()
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

        iteration += 1
        await client.handle_message(message)
        msg = await client.get_latest_message()
        assert callable(client.start)
        assert callable(client.stop)
        assert callable(client.connected)
        assert callable(client.get_latest_message)
        assert callable(client.handle_message)
        assert callable(client.handle_iteration_limit)
        assert callable(client.disconnected)
        assert client.connected.called_once
        assert client.is_connected is not None
        assert client.connected.called_once
        client.handle_message.assert_awaited
        assert client is not None
        assert msg == message
        if iteration >= 1:
            break

        if isinstance(client, TelegramHandler):
            
            run_until_disconnected = AsyncMock()
            run_until_disconnected.assert_awaited

        # if isinstance(client, DiscordHandler):
        #     handle_message = AsyncMock()
        #     assert callable(client.connected)
        #     assert callable(client.handle_message)
        #     assert client.connected.called_once
        #     handle_message.assert_awaited_once()
