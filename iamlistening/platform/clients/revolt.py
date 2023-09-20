"""
Revolt  🇷
"""
import asyncio

import aiohttp
import revolt
from loguru import logger

from .client import ChatClient


class RevoltHandler(ChatClient):
    def __init__(self):
        """
        Initialize the Revolt handler.
        """
        super().__init__()
        session = aiohttp.ClientSession()
        self.bot = revolt.Client(session, self.bot_token)
        self.connected()

    async def start(self):
        """
        Start the Revolt handler.
        """
        logger.debug("Revolt setup")

        await self.bot.start()

        @self.bot.event
        async def on_message(self, message: revolt.Message):
            logger.debug("new message received")
            await self.handle_message(message.content)
