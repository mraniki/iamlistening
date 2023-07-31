"""
Revolt Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.platform.clients.revolt import RevoltHandler
from iamlistening.platform.platform_manager import PlatformManager


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingrevolt")

@pytest.mark.asyncio 
async def test_fixture():
    assert settings.VALUE == "On Testing Revolt"


@pytest.fixture(name="handler")
def handler_test():
    return RevoltHandler()

def test_telegram_handler_initialization(handler):
    assert isinstance(handler, RevoltHandler)

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



