"""
Guilded  🟡
"""
import asyncio

import guilded
from loguru import logger

from iamlistening.config import settings
from iamlistening.platform.chat_manager import ChatManager


class GuildedHandler(ChatManager):
    def __init__(self):
        """
        Initialize the Guilded handler.
        """
        super().__init__()

    async def start(self):
        """
        Start the Guilded handler.
        """
        logger.debug("Guilded setup")
        self.bot = guilded.Client()

        @self.bot.event
        async def on_ready():
            self.connected()

        @self.bot.event
        async def on_message(message):
            logger.debug("new message received")
            await self.handle_message(message.content)

        self.bot.run(settings.bot_token)
