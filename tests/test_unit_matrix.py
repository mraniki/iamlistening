"""
Matrix Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.platform.clients.matrix import MatrixHandler
from iamlistening.platform.platform_manager import PlatformManager


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingmatrix")


@pytest.mark.asyncio
async def test_fixture():
    assert settings.VALUE == "On Testing Matrix"


@pytest.fixture(name="handler")
def handler_test():
    return MatrixHandler()

def test_telegram_handler_initialization(handler):
    assert isinstance(handler, MatrixHandler)

@pytest.fixture(name="listener")
def listener():
    return Listener()

@pytest.fixture(name="message")
def message():
    return "hello"


@pytest.mark.asyncio
async def test_telegram_handler_start(listener):
    await listener.start()
    await listener.handler.handle_message(message)
    msg = await listener.handler.get_latest_message()
    assert msg == listener


@pytest.mark.asyncio
async def test_telegram_handler_handle_message(message, handler):
    handler.handle_message = AsyncMock()
    event = AsyncMock()
    event.message.message = message
    await handler.handle_telegram_message(event)
    handler.handle_message.assert_awaited_once_with(message)
