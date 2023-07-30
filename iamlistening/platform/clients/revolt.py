"""
Revolt  🇷
"""
import asyncio

import aiohttp
import revolt
from loguru import logger

from iamlistening.config import settings
from iamlistening.platform.platform_manager import ChatManager


class RevoltHandler(ChatManager):

    def __init__(self):
        """
        Initialize the Revolt handler.
        """
        super().__init__()

    async def start(self):
        """
        Start the Revolt handler.
        """
        logger.debug("Revolt setup")
        self.bot = revolt.Client(revolt.utils.client_session(), settings.bot_token)
        logger.debug(self.bot.api_info)
        await self.bot.start()

        # @self.bot.event
        # async def on_ready():
        #     logger.info("listener is online")

        @self.bot.event
        async def on_message(self, message: revolt.Message):
            await self.handle_message(message.content)

