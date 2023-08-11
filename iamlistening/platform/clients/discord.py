"""
Discord  🟣
"""
import asyncio

import discord
from loguru import logger

from iamlistening.config import settings
from iamlistening.platform.chat_manager import ChatManager


class DiscordHandler(ChatManager):
    def __init__(self):
        """
        Initialize the Discord handler.


        """
        super().__init__()

    async def start(self):
        """
        Start the Discord handler.

        """

        logger.debug("Discord setup")
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = discord.Bot(intents=intents)

        @self.bot.event
        async def on_ready():
            self.connected()

        @self.bot.event
        async def on_message(message: discord.Message):
            logger.debug("new message received")
            await self.handle_message(message.content)

        await self.bot.start(settings.bot_token)
