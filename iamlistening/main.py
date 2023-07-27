"""
 IAmListening Main
"""

import asyncio
import threading

from loguru import logger

from iamlistening import __version__

from .config import settings
from .platform.platform_manager import PlatformManager


class Listener:
    """
    Listener Class
    """

    def __init__(self, chat_platform=None):
        """
        Initialize the listener.
        """
        self.logger = logger
        self.version = __version__
        self.platform = chat_platform or settings.chat_platform
        self.handler = None

        if self.platform is None:
            if settings.telethon_api_id:
                self.platform = "telegram"
            elif settings.matrix_hostname:
                self.platform = "matrix"
            elif settings.bot_token:
                self.platform = "discord"

    async def start(self):
        """
        Start the listener.
        """

        self.handler = PlatformManager.get_handler(self.platform)

        if self.handler:
            asyncio.create_task(await self.handler.start())
