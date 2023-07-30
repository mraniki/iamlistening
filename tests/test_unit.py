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
from iamlistening.platform.platform_manager import PlatformManager
from iamlistening.platform.clients.telegram import TelegramHandler

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
       # Mock the PlatformManager.get_handler function
       get_handler_mock = MagicMock(return_value=AsyncMock())
       # Mock the asyncio.create_task function
       create_task_mock = AsyncMock()
       # Replace the PlatformManager.get_handler 
       # and asyncio.create_task functions
       PlatformManager.get_handler = get_handler_mock
       asyncio.create_task = create_task_mock
       # Call the start function
       result = await listener.start()
       # Check if the result is as expected
       assert result is None
       # Check if the PlatformManager.get_handler function 
       # was called with the correct argument
       get_handler_mock.assert_called_once_with(
        listener.platform)
       # Check if the asyncio.create_task function 
       # was called with the correct argument
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
async def test_telegram_handler(message):
    telegram_handler = TelegramHandler()
    telegram_handler.start():
    msg = await telegram_handler.handle_message(message)
    assert msg == message
