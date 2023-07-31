"""
Guilded Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.platform.clients.guilded import GuildedHandler
from iamlistening.platform.platform_manager import PlatformManager


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingguilded")

@pytest.mark.asyncio
async def test_fixture():
    assert settings.VALUE == "On Testing Guilded"


@pytest.fixture(name="handler")
def handler_test():
    return GuildedHandler()

def test_telegram_handler_initialization(handler):
    assert isinstance(handler, GuildedHandler)

@pytest.fixture(name="listener")
def listener():
    return Listener()

@pytest.fixture(name="message")
def message():
    return "hello"


@pytest.mark.asyncio
async def test_handler_start(listener, message):
    await listener.start()
    await listener.handler.handle_message(message)
    msg = await listener.handler.get_latest_message()
    assert msg == message


