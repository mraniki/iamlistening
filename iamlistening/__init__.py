"""
 Versioning
"""
__version__ = "1.1.7"

from iamlistening.config import settings
from iamlistening.main import Listener
from iamlistening.module import (
    ListenerDiscord,
    ListenerMatrix,
    ListenerRocketChat,
    ListenerTelegram,
)
