"""
Telegram 🔵

"""
from loguru import logger
from telethon import TelegramClient, events

from .client import ChatClient


class TelegramHandler(ChatClient):
    """
    Telegram Handler

    """

    def __init__(self):
        """
        Initialize the Telegram handler.

        :param arg: No arguments
        :return: Initialize the Telegram handler
        """
        super().__init__()
        logger.debug("Telegram setup")

    async def start(self):
        """
        Start the Telegram handler
        using Telethon.
        """

        logger.debug("Telegram start")
        self.bot = await TelegramClient(
            session=None, api_id=self.bot_api_id, api_hash=self.bot_api_hash
        ).start(bot_token=self.bot_token)
        self.connected()
        self.bot.add_event_handler(self.handle_telegram_message, events.NewMessage)
        await self.bot.run_until_disconnected()

    async def handle_telegram_message(self, event):
        """
        Handle new messages
        """
        logger.debug("new message received")
        await self.handle_message(event.message.message)
