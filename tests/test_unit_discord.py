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
async def test_handler_start(handler, message):
    task = asyncio.create_task(handler.start())
    await handler.handle_message(message)
    msg = await handler.get_latest_message()
    task.cancel()
    assert msg == message


@pytest.mark.asyncio
async def test_listener_library():
    listener_test = Listener()
    print(listener_test)
    assert listener_test is not None
    assert isinstance(listener_test, Listener)
    await listener_test.start()
    await listener_test.handler.handle_message("hello")
    msg = await listener_test.handler.get_latest_message()
    print(msg)
    assert msg == "hello"