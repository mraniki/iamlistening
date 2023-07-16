"""
iamlistening Unit Testing
"""

import pytest
import asyncio
from unittest.mock import AsyncMock, patch
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
    await listener.handle_message(message)
    assert await listener.get_latest_message() == message


@pytest.mark.asyncio
async def test_listener_run():
    start = AsyncMock()
    listener_test = Listener()
    await listener_test.run_forever(max_iterations=1)
    assert start.assert_awaited_once()

@pytest.mark.asyncio
async def test_listener_run_error():
    with pytest.raises(ValueError):
        start = AsyncMock()
        listener_test = Listener()
        await listener_test.run_forever(max_iterations=1)
        assert start.assert_awaited_once()


@pytest.mark.asyncio
async def test_listener_library():
    listener_test = Listener()
    print(listener_test)
    assert listener_test is not None
    assert isinstance(listener_test, Listener)
    await listener_test.handle_message("hello")
    msg = await listener_test.get_latest_message()
    print(msg)
    assert msg == "hello"