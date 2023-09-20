# """
# Guilded Unit Testing
# """

# import asyncio
# from unittest.mock import AsyncMock

# import pytest

# from iamlistening import Listener
# from iamlistening.config import settings
# from iamlistening.platform.chat_manager import ChatManager


# @pytest.fixture(scope="session", autouse=True)
# def set_test_settings():
#     settings.configure(FORCE_ENV_FOR_DYNACONF="testingguilded")

# @pytest.mark.asyncio
# async def test_fixture():
#     assert settings.VALUE == "On Testing Guilded"


# @pytest.fixture(name="listener")
# def listener():
#     return Listener()

# @pytest.fixture(name="message")
# def message():
#     return "hello"

# @pytest.mark.asyncio
# async def test_listener_start(message):
#     handle_iteration_limit = AsyncMock()
#     check_connected = AsyncMock()
#     listener = Listener()
#     await listener.start()
#     await listener.handler.handle_message(message)
#     msg = await listener.handler.get_latest_message()
#     assert listener.handler is not None
#     assert listener.handler.connected is not None
#     assert listener.platform == "guilded"
#     handle_iteration_limit.assert_awaited
#     check_connected.assert_awaited
#     assert msg == message