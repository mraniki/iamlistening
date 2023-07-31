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


@pytest.fixture(name="handler")
def handler_test():
    return TelegramHandler()


def test_telegram_handler_initialization(handler):
    assert isinstance(handler, TelegramHandler)


@pytest.fixture(name="listener")
def listener():
    return Listener()

@pytest.fixture(name="message")
def message():
    return "hello"


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
    sleep = AsyncMock()
    await handler.handle_message(message)
    msg = await handler.get_latest_message()
    assert msg == message
    sleep.assert_awaited_once

@pytest.mark.asyncio
async def test_handler_start(listener):
    await listener.start()
    await listener.handler.handle_message(message)
    msg = await listener.handler.get_latest_message()
    assert msg == listener


@pytest.mark.asyncio
async def test_handler_handle_message(message, handler):
    handler.handle_message = AsyncMock()
    event = AsyncMock()
    event.message.message = message
    await handler.handle_telegram_message(event)
    handler.handle_message.assert_awaited_once_with(message)
