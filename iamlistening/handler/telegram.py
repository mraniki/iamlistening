"""
Telegram 🔵

"""

from telethon import TelegramClient, events

from ._client import ChatClient


class TelegramHandler(ChatClient):
    """
    Telegram Handler

    """

    def __init__(self, **kwargs):
        """
        Initialize the Handler object

        """

        super().__init__(**kwargs)

    async def start(self):
        """
        Start the Telegram handler
        using Telethon.
        """
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
        await self.handle_message(event.message.message)
