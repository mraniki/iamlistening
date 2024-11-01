"""
Discord  🟣
"""

import discord
from loguru import logger

from ._client import ChatClient


class DiscordHandler(ChatClient):

    def __init__(self, **kwargs):
        """
        Initialize the Handler object

        """

        super().__init__(**kwargs)

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
            await self.handle_message(message.content)

        await self.bot.start(self.bot_token)
