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

    def __init__(self, platform=None):
        """
        Initialize the listener.
        """
        self.logger = logger
        self.platform = platform
        self.handler = None

        if self.platform is None:
            if settings.telethon_api_id:
                self.platform = "telegram"
            elif settings.matrix_hostname:
                self.platform = "matrix"
            elif settings.bot_token:
                self.platform = "discord"


    async def get_info_listener(self):
        """
        Get information about the listener.

        Returns:
            str: The information about the listener.
        """
        return f"ℹ️ IAmListening v{__version__}\n{self.platform}"


    async def start(self):
        """
        Start the listener.
        """

        self.handler = PlatformManager.get_handler(self.platform)

        if self.handler:
            asyncio.create_task(await self.handler.start())
