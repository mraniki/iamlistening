"""
Tinode 🇹

https://github.com/tinode/chat/blob/master/chatbot/python/chatbot.py

"""

import tinode_grpc
from loguru import logger

from iamlistening.config import settings
from iamlistening.platform.platform_manager import ChatManager


class TinodeHandler(ChatManager):

    def __init__(self):
        super().__init__()

    async def start(self):
        """Start the Tinode handler."""
        logger.debug("Tinode setup")
        # client = 
        logger.info("listener is online")

        # await self.handle_message()
