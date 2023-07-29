"""
iamlistening Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, patch

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
    assert settings.bot_api_id is not None
    assert listener is not None
    assert isinstance(listener, Listener)
    assert listener.platform is not None
    assert listener.version is not None


@pytest.mark.asyncio
async def test_handler(listener):
    handler = PlatformManager.get_handler(listener.platform)
    logger.debug(handler)
    assert handler is not None

@pytest.mark.asyncio
async def test_handler(listener):
    handler = PlatformManager.get_handler(listener.platform)
    start = AsyncMock()
    await handler.start()
    assert start.assert_awaited_once

