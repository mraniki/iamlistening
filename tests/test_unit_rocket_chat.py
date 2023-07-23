"""
iamlistening Unit Testing
"""

import asyncio
from unittest.mock import AsyncMock

import aiohttp
import pytest
from rocketchat_API.rocketchat import RocketChat

from iamlistening import Listener
from iamlistening.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingrocketchat")

# @pytest.fixture(name="listener")
# def listener():
#     return Listener()

# @pytest.fixture
# def message():
#     return "Test message"

# @pytest.fixture
# def event_loop():
#     loop = asyncio.new_event_loop()
#     yield loop
#     loop.close()

# @pytest.mark.asyncio
# async def test_fixture(listener):
#     assert listener is not None
#     assert settings.VALUE == "On Testing RocketChat"

# def test_init(listener):
#     assert listener is not None
