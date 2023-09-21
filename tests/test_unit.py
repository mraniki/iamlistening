"""
iamlistening Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest
from loguru import logger

# from telethon import TelegramClient, events
import iamlistening
from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.platform.chat_manager import ChatManager
from iamlistening.platform.clients import (
    DiscordHandler,
    # GuildedHandler,
    # LemmyHandler,
    # MastodonHandler,
    MatrixHandler,
    # RevoltHandler,
    TelegramHandler,
)


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="ial")


# @pytest.mark.asyncio
# async def test_fixture():
#     assert settings.VALUE == "On Testing"


@pytest.fixture(name="listener")
def listener():
    return Listener()


@pytest.fixture(name="message")
def message():
    return "hello"


# @pytest.mark.asyncio
# async def test_listener_fixture(listener):
#     assert listener is not None
#     assert isinstance(listener, Listener)
#     assert listener.platform is not None
#     assert listener.version is not None


# @pytest.mark.asyncio
# async def test_listener_start(message):
#     handle_iteration_limit = AsyncMock()
#     check_connected = AsyncMock()
#     connected = MagicMock()
#     listener = Listener()
#     await listener.start()
#     await listener.handler.handle_message(message)
#     msg = await listener.handler.get_latest_message()
#     assert listener.handler is not None
#     assert listener.handler.connected is not None
#     assert listener.platform == "telegram"
#     handle_iteration_limit.assert_awaited
#     check_connected.assert_awaited
#     connected.assert_called
#     assert msg == message


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
    # handle_iteration_limit = AsyncMock()
    check_connected = AsyncMock()
    #connected = MagicMock()
    await listener.start()

    # Check if the handler has been called for each platform
    for platform_info in listener.platform_info:
        #assert platform_info.handler.handle_message.called
        assert isinstance(
            platform_info.handler,
            (DiscordHandler, TelegramHandler, MatrixHandler),
        )

        msg = await listener.platform_info.handler.get_latest_message()
        assert listener.platform_info.handler is not None
        assert listener.platform_info.handler.connected is not None
        assert listener.platform_info.platform is not None
        # handle_iteration_limit.assert_awaited
        check_connected.assert_awaited
        #connected.assert_called
        assert msg == message
