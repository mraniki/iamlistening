"""
iamlistening Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, create_autospec, patch

import pytest
from loguru import logger
from telethon import TelegramClient, events

import iamlistening
from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.platform.clients.telegram import TelegramHandler
from iamlistening.platform.platform_manager import ChatManager, PlatformManager


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingtelegram")

@pytest.mark.asyncio 
async def test_fixture():
    assert settings.VALUE == "On Testing"

@pytest.fixture(name="handler_mock")
def handler_mock():
    return AsyncMock()

@pytest.fixture(name="listener")
def listener():
    return Listener()

@pytest.fixture(name="message")
def message():
    return "hello"

@pytest.fixture(name="client")
def client():
    return AsyncMock()

@pytest.mark.asyncio
async def test_start(listener):
       get_handler_mock = MagicMock(return_value=AsyncMock())
       create_task_mock = MagicMock()
       PlatformManager.get_handler = get_handler_mock
       asyncio.create_task = create_task_mock
       result = await listener.start()
       assert result is None
       get_handler_mock.assert_called_once_with(
        listener.platform)
       create_task_mock.assert_called_once_with(
        await listener.handler.start())


@pytest.mark.asyncio
async def test_listener_fixture(listener):
    assert listener is not None
    assert isinstance(listener, Listener)
    assert listener.platform is not None
    assert listener.version is not None


@pytest.mark.asyncio
async def test_listener_start(listener):
    listener.handler = AsyncMock()
    with patch.object(listener, "start"):
        await listener.start()
        listener.handler.assert_called_once


@pytest.mark.asyncio
async def test_handler(listener):
    PlatformManager = AsyncMock()
    PlatformManager.get_handler = MagicMock()
    listener.handler = PlatformManager.get_handler(listener.platform)
    with patch.object(listener, "start"):
        await listener.start()
        PlatformManager.get_handler.assert_called_once


@pytest.mark.asyncio
async def test_chat_manager(message):
    handler = ChatManager()
    assert handler.bot is None
    assert handler.latest_message is None
    assert handler.lock is not None
    await handler.handle_message(message)
    msg = await handler.get_latest_message()
    assert msg == message

# @pytest.mark.asyncio
# async def test_listener_telegram(listener):
#     assert listener is not None
#     assert isinstance(listener, Listener)
#     await listener.start()
#     await listener.handler.handle_message("hello")
#     msg = await listener.handler.get_latest_message()
#     print(msg)
#     assert msg == "hello"


# @pytest.mark.asyncio
# async def test_telegram_handler_start():
#     handler = TelegramHandler()
#     handler.bot = AsyncMock()

#     with patch.object(handler.bot, "start"):
#         task = asyncio.create_task(handler.start())
#         await task
#         handler.bot.start.assert_awaited_once()
#         task.cancel()


# @pytest.mark.asyncio
# async def test_handler_start(listener, handler_mock, client):
#     start = AsyncMock()
#     with patch('iamlistening.platform.clients.telegram.TelegramHandler.start', start):
#         listener.handler = AsyncMock()
#         task = asyncio.create_task(listener.handler.start())
#         await task
#         start.assert_awaited
#         client.assert_awaited_once
#         handler_created = listener.handler
#         assert handler_created is not None
#         task.cancel()


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


# @pytest.mark.asyncio
# async def test_telegram_handler_start():
#     with patch(
#         'iamlistening.platform.clients.telegram.TelegramHandler'
#         ) as telegram_client_mock:
#         telegram_client_mock.return_value.start = AsyncMock()
#         handler = TelegramHandler()
#         task=asyncio.create_task(await handler.start())
#         try:
#             await asyncio.wait_for(task, timeout=10)
#         except asyncio.TimeoutError:
#             task.cancel()
#             await task
#             pytest.skip("Connectivity test only")
#         telegram_client_mock.assert_called_once_with(
#             None,
#             settings.bot_api_id,
#             settings.bot_api_hash
#         )
#         telegram_client_mock.return_value.start.assert_awaited_once()
