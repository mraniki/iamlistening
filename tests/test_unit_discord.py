"""
iamlistening Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock

import pytest
from discord import errors

from iamlistening import Listener
from iamlistening.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingdiscord")

@pytest.fixture(name="listener")
def listener():
    return Listener()

@pytest.fixture
def message():
    return "Test message"

@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.mark.asyncio
async def test_fixture(listener):
    assert listener is not None
    assert settings.VALUE == "On Testing Discord"

def test_init(listener):
    assert listener is not None

@pytest.mark.asyncio
async def test_get_latest_message(listener, message):
    await listener.start()
    await listener.handler.handle_message(message)
    assert await listener.handler.get_latest_message() == message


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