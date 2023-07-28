"""
iamlistening Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock

import pytest
import simplematrixbotlib as botlib

from iamlistening import Listener
from iamlistening.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingmatrix")


@pytest.mark.asyncio
async def test_fixture():
    assert settings.VALUE == "On Testing Matrix"


@pytest.fixture(name="listener")
def listener():
    return Listener()


@pytest.fixture(name="message")
def message():
    return "hello"


# @pytest.mark.asyncio
# async def test_listener(listener, message):

#     await listener.handler.handle_message(message)
#     msg = await listener.handler.get_latest_message()
#     print(msg)
#     assert msg == message

