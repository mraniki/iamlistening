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
from iamlistening.platform.clients.discord import DiscordHandler
from iamlistening.platform.platform_manager import PlatformManager


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingdiscord")

@pytest.mark.asyncio
async def test_fixture():
    assert settings.VALUE == "On Testing Discord"

@pytest.fixture(name="handler")
def handler_test():
    return DiscordHandler()

def test_telegram_handler_initialization(handler):
    assert isinstance(handler, DiscordHandler)

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
