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

    def __init__(self, chat_platform=None):
        """
        Initialize the listener.

        Args:
            chat_platform (str): The platform to use

        Raises:
            Exception: Platform missing

        """

        self.logger = logger
        self.version = __version__
        self.platform = chat_platform or settings.chat_platform
        self.chat_manager = ChatManager()

        if self.platform == "":
            raise Exception("Platform missing")

    async def start(self):
        """
        Start the listener.

        """

        self.handler = self.chat_manager.get_handler(self.platform)

        if self.handler:
            try:
                asyncio.create_task(self.handler.start())
            except ValueError:
                self.handler = None

