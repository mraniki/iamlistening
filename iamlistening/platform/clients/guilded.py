"""
Guilded  🟡
"""
import asyncio

import guilded
from loguru import logger

from iamlistening.config import settings
from iamlistening.platform.platform_manager import ChatManager


class GuildedHandler(ChatManager):

    def __init__(self):
        super().__init__()

    async def start(self):
        """Start the Guilded handler."""
        logger.debug("Guilded setup")
        client = guilded.Client()

        @client.event
        async def on_ready():
            logger.info("listener is online")

        @client.event
        async def on_message(message):
            await self.handle_message(message.content)

        client.run(settings.guilded_bot_token)