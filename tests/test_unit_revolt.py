"""
Revolt Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock, patch

import pytest

from iamlistening import Listener
from iamlistening.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingrevolt")

@pytest.mark.asyncio 
async def test_fixture():
    assert settings.VALUE == "On Testing Revolt"

@pytest.fixture(name="listener")
def listener():
    return Listener()

@pytest.fixture(name="message")
def message():
    return "hello"

# @pytest.mark.asyncio
# async def test_listener(listener, message):

#     assert listener is not None
#     assert isinstance(listener, Listener)
#     assert listener.platform is not None
#     await listener.start()
#     await listener.handler.handle_message(message)
#     msg = await listener.handler.get_latest_message()
#     print(msg)
#     assert msg == message
    