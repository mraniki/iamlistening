"""
iamlistening Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, patch

import pytest
from loguru import logger

#from telethon import TelegramClient, errors
from iamlistening import Listener
from iamlistening.config import settings

@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")

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
    logger.debug(settings.bot_api_id)
    assert settings.bot_api_id is not None
    assert listener is not None
    assert isinstance(listener, Listener)
    assert listener.platform is not None
    assert listener.version is not None


@pytest.mark.asyncio
async def test_start(listener):
    logger.debug(settings.bot_api_id)
    result = await listener.start()
    assert result is not None


@pytest.mark.asyncio
async def test_listening(listener, message):
    logger.debug(settings.bot_api_id)
    await listener.start()
    await listener.handler.handle_message(message)
    msg = await listener.handler.get_latest_message()
    logger.warning(msg)
    assert msg == message
