"""
iamlistening Exception Testing
"""

import pytest

from iamlistening import Listener
from iamlistening.config import settings
from iamlistening.platform.platform_manager import PlatformManager


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testingexception")

@pytest.mark.asyncio 
async def test_fixture():
    assert settings.VALUE == "None"

@pytest.mark.asyncio
async def test_listener_exception():
    with pytest.raises(Exception, match="Platform missing"):
        Listener()   


@pytest.mark.asyncio
async def test_listener_exception():
    with pytest.raises(Exception, match="Platform missing"):
        Listener()   

