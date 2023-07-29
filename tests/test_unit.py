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


@pytest.mark.asyncio
async def test_listener(listener):
    assert listener is not None
    assert isinstance(listener, Listener)
    assert listener.platform is not None
    assert listener.version is not None


@pytest.mark.asyncio
async def test_listener_start(listener):
    
        handler = AsyncMock()
        handler.start.return_value = asyncio.Future()
        get_handler.return_value = handler
        task=asyncio.run(listener.start())
        task.cancel()
        assert handler.start.assert_awaited_once()
        assert listener.handler is not None
        assert listener.handler == handler


@pytest.mark.asyncio
async def test_handler(listener, message):
    listener.handler = PlatformManager.get_handler(listener.platform)
    task=asyncio.create_task(listener.handler.start())
    await listener.handler.handle_message(message)
    msg = await listener.handler.get_latest_message()
    task.cancel()
    assert listener.handler is not None
    assert msg == message
