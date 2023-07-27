"""
Revolt  🇷
"""
import asyncio

import revolt
from loguru import logger

from iamlistening.config import settings
from iamlistening.main import ChatManager


class RevoltHandler(ChatManager):

    def __init__(self):
        super().__init__()

    async def start(self):
        """Start the Revolt handler."""
        logger.debug("Revolt setup")
        client = revolt.Client(revolt.utils.client_session(), settings.bot_token)
        await client.start()

        @client.event
        async def on_ready():
            logger.info("listener is online")

        @client.event
        async def on_message(self, message: revolt.Message):
            await self.handle_message(message.content)

