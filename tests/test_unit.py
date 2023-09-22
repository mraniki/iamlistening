"""
iamlistening Unit Testing
"""


import pytest

from iamlistening import Listener
from iamlistening.clients import (
    DiscordHandler,
    GuildedHandler,
    MatrixHandler,
    TelegramHandler,
)
from iamlistening.config import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="ial")


@pytest.fixture(name="listener")
def listener():
    return Listener()


@pytest.fixture(name="message")
def message():
    return "hello"


@pytest.mark.asyncio
async def test_listener_fixture(listener):
    assert listener is not None
    assert isinstance(listener, Listener)
    assert listener.platform_info is not None
    assert listener.platform_info[0].platform is not None
    assert listener.platform_info[0].bot_token is not None


@pytest.mark.asyncio
async def test_listener_start(listener, message):
    loop = asyncio.get_running_loop()
    loop.create_task(listener.start())
    for client in listener.platform_info:
        assert isinstance(
            client,
            (
                DiscordHandler,
                TelegramHandler,
                MatrixHandler,
                GuildedHandler,
            ),
        )

        iteration += 1
        await client.handle_message(message)
        msg = await client.get_latest_message()
        assert client.is_connected is not None
        assert client is not None
        assert msg == message
        if iteration >= 1:
            break
