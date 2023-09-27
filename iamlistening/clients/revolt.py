"""
Revolt  🇷
"""

import aiohttp
import revolt
from loguru import logger

from .client import ChatClient


class RevoltHandler(ChatClient):
    async def start(self):
        """
        Start the Revolt handler.
        """
        logger.debug("Revolt setup")
        session = aiohttp.ClientSession()
        self.bot = revolt.Client(session, self.bot_token)
        self.connected()
        await self.bot.start()

        @self.bot.event
        async def on_message(self, message: revolt.Message):
            await self.handle_message(message.content)
