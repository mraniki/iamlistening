"""
iamlistening Unit Testing
"""

import pytest
import asyncio
from unittest.mock import Mock
from iamlistening import Listener


@pytest.fixture
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


def test_init(listener):
    assert listener is not None


@pytest.mark.asyncio
async def test_get_latest_message(listener, message):
    # Test that get_latest_message() returns None when no messages have been received
    #assert await listener.get_latest_message() is None

    # Test that get_latest_message() returns the latest message after a message has been received
    await listener.handle_message(message)
    assert await listener.get_latest_message() == message


# @pytest.mark.asyncio
# async def test_handle_message(listener, message):
#     # Test that handle_message() updates the latest message correctly
#     await listener.handle_message(message)
#     assert listener.latest_message == message


# @pytest.mark.asyncio
# async def test_run_forever(listener, message, event_loop):
#     # Test that run_forever() starts the listener and runs it continuously in the background
#     listener.start = Mock(wraps=listener.start)
#     listener.handle_message = Mock(wraps=listener.handle_message)
#     task = event_loop.create_task(listener.run_forever())
#     event_loop.call_soon(listener.handle_message, message)
#     event_loop.call_later(1, event_loop.stop)
#     event_loop.run_forever()
#     assert listener.handle_message.called_with(message)
#     assert listener.start.called_once()
#     assert task.done() and not task.cancelled()
