"""
iamlistening Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from loguru import logger
from telethon import TelegramClient, events

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
async def test_listener_exception(listener):
    with pytest.raises(Exception):
        with patch(settings.config.chat_platform, ""):
            Listener()


@pytest.mark.asyncio
async def test_listener(listener):
    assert listener is not None
    assert isinstance(listener, Listener)
    assert listener.platform is not None
    assert listener.version is not None


@pytest.mark.asyncio
async def test_listener_start(listener):
    start = AsyncMock(side_effect=[listener])
    with patch('iamlistening.Listener.start', start):
        task = asyncio.create_task(listener.start())
        await asyncio.gather(task, asyncio.sleep(2))
        task.cancel()
        start.assert_awaited
        listener_created = listener
        assert isinstance(listener_created, Listener) 


@pytest.mark.asyncio
async def test_listener_start(listener):
    start = AsyncMock(side_effect=[listener])
    with patch('iamlistening.Listener.start', start):
        task = asyncio.create_task(listener.start())
        await asyncio.gather(task, asyncio.sleep(2))
        task.cancel()
        start.assert_awaited
        listener_created = listener
        assert isinstance(listener_created, Listener) 


@pytest.mark.asyncio
async def test_handler_start(listener, handler_mock, client):
    start = AsyncMock(side_effect=[handler_mock])
    with patch('iamlistening.platform.platform_manager.ChatManager.start', start):
        listener.handler = ChatManager()
        task = asyncio.create_task(listener.handler.start())
        await asyncio.gather(task, asyncio.sleep(2))
        start.assert_awaited
        client.assert_awaited_once
        handler_created = listener.handler
        assert isinstance(handler_created, ChatManager) 
        task.cancel()


@pytest.mark.asyncio
async def test_handler_processing(listener, message):
    handle_message = AsyncMock()
    listener.handler = PlatformManager.get_handler(listener.platform)
    task=asyncio.create_task(listener.handler.start())
    assert listener.handler.latest_message is None
    await listener.handler.handle_message(message)
    assert handle_message.assert_awaited_once
    msg = await listener.handler.get_latest_message()
    task.cancel()
    assert listener.handler is not None
    assert msg == message



@pytest.mark.asyncio
async def test_telegram_handler_start():
    with patch(
        'iamlistening.platform.clients.telegram.TelegramClient'
        ) as telegram_client_mock:
        telegram_client_mock.return_value.start = AsyncMock()
        handler = TelegramHandler()
        await handler.start()

        telegram_client_mock.assert_called_once_with(
            None,
            settings.bot_api_id,
            settings.bot_api_hash
        )
        telegram_client_mock.return_value.start.assert_awaited_once()
