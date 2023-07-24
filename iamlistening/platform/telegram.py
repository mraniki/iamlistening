"""
Telegram 🔵
"""
from loguru import logger
from telethon import TelegramClient, events

from iamlistening.config import settings
from iamlistening.main import ChatManager


class TelegramHandler(ChatManager):

    def __init__(self):
        super().__init__()

    async def start(self):
        """Start the Telegram handler."""
        logger.debug("Telegram setup")
        bot = await TelegramClient(
                    None,
                    settings.telethon_api_id,
                    settings.telethon_api_hash
                    ).start(bot_token=settings.bot_token)
        logger.info("listener is online")

        @bot.on(events.NewMessage())
        async def telethon(event):
            await self.handle_message(event.message.message)

        await bot.run_until_disconnected()
