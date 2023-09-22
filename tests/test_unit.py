"""
iamlistening Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest
from loguru import logger

import iamlistening
from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.platform.clients import (
    DiscordHandler,
    GuildedHandler,
    # LemmyHandler,
    # MastodonHandler,
    MatrixHandler,
    # RevoltHandler,
    TelegramHandler,
)


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
    assert listener.platform_info is not None
    assert listener.platform_info[0].platform is not None
    assert listener.platform_info[0].bot_token is not None
    assert listener.platform_info[0].bot_channel_id is not None
    assert listener.platform_info[0].bot_api_id is not None
    assert listener.platform_info[0].bot_api_hash is not None
    assert listener.platform_info[0].bot_hostname is not None
    assert listener.platform_info[0].bot_user is not None
    assert listener.platform_info[0].bot_pass is not None
    assert listener.platform_info[0].bot_auth_token is not None


@pytest.mark.asyncio
async def test_listener_start(listener, message):
    await listener.start()

    for client in listener.platform_info:
        assert isinstance(
            client.handler,
            (
                DiscordHandler,
                TelegramHandler,
                MatrixHandler,
                GuildedHandler,
            ),
        )

        await client.handle_message(message)
        msg = await client.get_latest_message()
        assert client.is_connected is not None
        assert client is not None
        assert msg == message
