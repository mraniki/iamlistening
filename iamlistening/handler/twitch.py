"""
Twitch  🟣
"""

from loguru import logger
from twitchio.ext import commands

from ._client import ChatClient


class TwitchHandler(ChatClient):

    def __init__(self, **kwargs):
        """
        Initialize the Handler object

        """

        super().__init__(**kwargs)

    async def start(self):
        """
        Start the Twitch handler.

        """
        self.bot = commands.Bot(token=self.bot_token, prefix="?")
        logger.debug("Twitch setup")

        @self.bot.event
        async def event_ready():
            self.connected()

        @self.bot.event
        async def event_message(self, message):
            logger.debug("new message received")
            await self.handle_message(message.content)

        self.bot.run()
