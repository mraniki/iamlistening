"""
Mastodon Unit Testing
"""


import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.platform.clients.mastodon import MastodonHandler
from iamlistening.platform.platform_manager import PlatformManager


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingmastodon")

@pytest.mark.asyncio
async def test_fixture():
    assert settings.VALUE == "On Testing Mastodon"


@pytest.fixture(name="handler")
def handler_test():
    return MastodonHandler()

def test_handler_initialization(handler):
    assert isinstance(handler, MastodonHandler)

@pytest.fixture(name="listener")
def listener():
    return Listener()

@pytest.fixture(name="message")
def message():
    return "hello"


def test_get_handler(listener):
    assert listener.platform == "mastodon"
    handler = PlatformManager.get_handler(listener.platform)
    assert isinstance(handler, MastodonHandler)


@pytest.mark.asyncio
async def test_handler_start(handler, message):
    task = asyncio.create_task(handler.start())
    await handler.handle_message(message)
    msg = await handler.get_latest_message()
    task.cancel()
    assert msg == message

