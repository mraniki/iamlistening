"""
Guilded Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.platform.platform_manager import ChatManager, PlatformManager


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingguilded")

@pytest.mark.asyncio
async def test_fixture():
    assert settings.VALUE == "On Testing Guilded"


@pytest.fixture(name="listener")
def listener():
    return Listener()

@pytest.fixture(name="message")
def message():
    return "hello"

@pytest.fixture(name="client")
def client():
    return AsyncMock()

@pytest.fixture(name="handler_mock")
def handler_mock():
    return AsyncMock()


# @pytest.mark.asyncio
# async def test_handler_start(listener, handler_mock, client):
#     start = AsyncMock(side_effect=[handler_mock])
#     with patch('iamlistening.platform.platform_manager.ChatManager.start', start):
#         listener.handler = ChatManager()
#         task = asyncio.create_task(listener.handler.start())
#         await asyncio.gather(task, asyncio.sleep(2))
#         task.cancel()
#         start.assert_awaited
#         client.assert_awaited_once
#         handler_created = listener.handler
#         assert isinstance(handler_created, ChatManager) 


# @pytest.mark.asyncio
# async def test_handler_processing(listener, message):
#     handle_message = AsyncMock()
#     listener.handler = PlatformManager.get_handler(listener.platform)
#     task=asyncio.create_task(listener.handler.start())
#     assert listener.handler.latest_message is None
#     await listener.handler.handle_message(message)
#     assert handle_message.assert_awaited_once
#     msg = await listener.handler.get_latest_message()
#     task.cancel()
#     assert listener.handler is not None
#     assert msg == message
