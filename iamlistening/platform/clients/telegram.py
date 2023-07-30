"""
Telegram 🔵
"""
from loguru import logger
from telethon import TelegramClient, events

from iamlistening.config import settings
from iamlistening.platform.platform_manager import ChatManager


class TelegramHandler(ChatManager):
    """
    Telegram Handler
    """

    def __init__(self):
        """
        Initialize the Telegram handler.

        """
        super().__init__()

    async def start(self):
        """
        Start the Telegram handler
        using Telethon.
        """

        logger.debug("Telegram setup")
        self.bot = await TelegramClient(
                    None,
                    settings.bot_api_id,
                    settings.bot_api_hash
                    ).start(bot_token=settings.bot_token)
        logger.info("listener is online")

        @self.bot.on(events.NewMessage())
        async def telethon(event):
            """
            Handle new messages
            """
            await self.handle_message(event.message.message)

        await self.bot.run_until_disconnected()
