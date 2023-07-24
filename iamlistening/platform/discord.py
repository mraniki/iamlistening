"""
Discord  🟣
"""
import asyncio

import discord
from loguru import logger

from iamlistening.config import settings
from iamlistening.main import ChatManager


class DiscordHandler(ChatManager):

    def __init__(self):
        super().__init__()

    async def start(self):
        """Start the Discord handler."""
        logger.debug("Discord setup")
        intents = discord.Intents.default()
        intents.message_content = True
        bot = discord.Bot(intents=intents)

        @bot.event
        async def on_ready():
            logger.info("listener is online")

        @bot.event
        async def on_message(message: discord.Message):
            await self.handle_message(message.content)
    
        await bot.start(settings.bot_token)
