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


@pytest.mark.asyncio
async def test_listener_start(listener, message):
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
        assert client is not None
        assert msg == message
        if iteration >= 1:
            break

        if isinstance(client, TelegramHandler):
            handle_message = AsyncMock()
            assert callable(client.connected)
            assert callable(client.bot.add_event_handler)
            assert callable(client.handle_message)
            assert client.connected.called_once
            handle_message.assert_awaited_once()
        if isinstance(client, DiscordHandler):
            handle_message = AsyncMock()
            assert callable(client.connected)
            #assert callable(client.bot.add_event_handler)
            assert callable(client.handle_message)
            assert client.connected.called_once
            handle_message.assert_awaited_once()