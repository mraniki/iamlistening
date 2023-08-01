"""
Discord Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, create_autospec, patch

import pytest
from loguru import logger
from telethon import TelegramClient, events

import iamlistening
from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.platform.chat_manager import ChatManager


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingdiscord")

@pytest.mark.asyncio
async def test_fixture():
    assert settings.VALUE == "On Testing Discord"


@pytest.fixture(name="listener")
def listener():
    return Listener()

@pytest.fixture(name="message")
def message():
    return "hello"

@pytest.mark.asyncio
async def test_chat_manager(message, handler):
    assert handler.bot is None
    assert handler.latest_message is None
    assert handler.lock is not None
    sleep = AsyncMock()
    await handler.handle_message(message)
    msg = await handler.get_latest_message()
    assert msg == message
    sleep.assert_awaited_once


@pytest.mark.asyncio
async def test_handler(listener):
    get_handler = AsyncMock()
    with patch.object(listener, "start"):
        await listener.start()
        get_handler.assert_called_once


@pytest.mark.asyncio
async def test_handler_start(handler, message):
    await handler.start()
    await handler.handle_message(message)
    msg = await handler.get_latest_message()
    assert msg == message