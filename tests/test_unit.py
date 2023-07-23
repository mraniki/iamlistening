"""
iamlistening Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, patch

import pytest
from telethon import TelegramClient, errors

from iamlistening import Listener
from iamlistening.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")

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
    assert settings.VALUE == "On Testing"

@pytest.mark.asyncio
async def test_init(listener):
    assert listener is not None
    result = await listener.get_info_listener()
    print("results: ",result)
    result is not None 
    assert "ℹ️" in result
    assert "IAmListening" in result

@pytest.mark.asyncio
async def test_get_latest_message(listener, message):
    await listener.handle_message(message)
    assert await listener.get_latest_message() == message

@pytest.mark.asyncio
async def test_telegram_function():
    TelegramClient = AsyncMock()
    TelegramClient.run_until_disconnected = AsyncMock()
    listener = Listener()
    assert listener is not None
    assert isinstance(listener, Listener)
    assert TelegramClient.assert_called_once
    assert TelegramClient.run_until_disconnected.assert_called_once


@pytest.mark.asyncio
async def test_listener_telegram():
    listener_test = Listener()
    print(listener_test)
    assert listener_test is not None
    assert isinstance(listener_test, Listener)
    await listener_test.handle_message("hello")
    msg = await listener_test.get_latest_message()
    print(msg)
    assert msg == "hello"


# @pytest.mark.asyncio
# async def test_listener_run():
#     start = AsyncMock()
#     listener_test = Listener()
#     await listener_test.run_forever(max_iterations=1)
#     assert start.assert_awaited_once()


@pytest.mark.asyncio
async def test_listener_run_error():
    with pytest.raises(errors.ApiIdInvalidError):
        start = AsyncMock()
        listener_test = Listener()
        await listener_test.run_forever(max_iterations=1)
        assert start.assert_awaited_once()
