"""
Discord  🚀
"""
import discord

from iamlistening.config import settings
from iamlistening.main import Listener


class ListenerDiscord(Listener):


            self.logger.debug("Discord setup")
            intents = discord.Intents.default()
            intents.message_content = True
            bot = discord.Bot(intents=intents)

            @bot.event
            async def on_ready():
                await self.post_init()

            @bot.event
            async def on_message(message: discord.Message):
                await self.handle_message(message.content)
            await bot.start(settings.bot_token)
