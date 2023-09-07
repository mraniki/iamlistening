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
        self.is_connected = True

        if self.platform == "":
            raise Exception("Platform missing")

    async def start(self):
        """
        Asynchronously starts the function.

        This function sets the `handler` attribute using the 
        `get_handler` method of the `chat_manager` instance. 
        If a handler is found, it starts the handler using the `start` method. 
        If the handler is not connected, the task is cancelled, 
        the `handler` attribute is set to `None`, 
        and the `is_connected` attribute is set to `False`.

        Parameters:
            None

        Returns:
            None
        """

        self.logger.debug("listener starting")
        self.handler = self.chat_manager.get_handler(self.platform)

        if self.handler:
            self.logger.debug("listener handler is starting")
            task = asyncio.create_task(self.handler.start())
            if not self.handler.is_connected:
                task.cancel()
                self.logger.debug("listener handler stopped")
                self.handler = None
                self.is_connected = False
