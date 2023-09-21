"""
 IAmListening Main
"""

import asyncio
import threading

from loguru import logger

from iamlistening import __version__
from iamlistening.config import settings
from iamlistening.platform.chat_manager import ChatManager


class Listener:
    """
    Listener Class for IAmListening.

    """

    def __init__(self):
        """
        Initialize the listener.

        Raises:
            Exception: Platform missing

        """
        self.platform_info = []
        platforms = settings.platform
        logger.debug("platforms {}", platforms)
        for platform in platforms:
            platform_config = platforms[platform]
            client = ChatManager(**platform_config)
            self.platform_info.append(client)

            if client.platform == "":
                raise Exception("Platform missing")
        logger.debug("init completed {}", self.platform_info)

    async def start(self):
        """
        Asynchronously start the listener.

        This method starts the chat managers for each platform
        and logs the status.

        """
        logger.debug("Listener starting")

        tasks = [platform.start() for platform in self.platform_info]
        await asyncio.gather(*tasks)

        logger.debug("Listener started")

    def stop(self):
        """
        Stop the listener.

        This method stops the chat managers for each platform.

        """
        logger.debug("Listener stopping")

        for platform in self.platform_info:
            platform.stop()

        logger.debug("Listener stopped")
