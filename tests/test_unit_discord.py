"""
Discord Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, patch

import pytest
from loguru import logger

import iamlistening
from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.platform.chat_manager import ChatManager


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="ial")

@pytest.mark.asyncio
async def test_fixture():
    assert settings.VALUE == "On Testing Discord"

@pytest.fixture(name="handler")
def handler(listener):
    return listener.chat_manager.get_handler(listener.platform)

@pytest.fixture(name="listener")
def listener():
    return Listener()

@pytest.fixture(name="message")
def message():
    return "hello"

def test_handler(listener, handler):
    assert listener.platform == "discord"
    assert handler is not None

@pytest.mark.asyncio
async def test_get_handler(listener):
    get_handler = AsyncMock()
    with patch.object(listener, "start"):
        await listener.start()
        get_handler.assert_called_once
        
@pytest.mark.asyncio
async def test_listener_start(message):
    handle_iteration_limit = AsyncMock()
    check_connected = AsyncMock()
    listener = Listener()
    await listener.start()
    await listener.handler.handle_message(message)
    msg = await listener.handler.get_latest_message()
    assert listener.handler is not None
    assert listener.handler.connected is not None
    assert listener.platform == "discord"
    handle_iteration_limit.assert_awaited
    check_connected.assert_awaited
    assert msg == message
