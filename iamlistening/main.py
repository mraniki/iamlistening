"""
 IAmListening Main
"""

import asyncio
import threading

from loguru import logger

from iamlistening import __version__

from .config import settings


class Listener:
    def __init__(self):
        self.logger = logger
        self.handler = None

    async def get_info_listener(self):
        return (f"ℹ️ IAmListening v{__version__}\n")

    async def start(self):
        """Start the listener."""
        if settings.telethon_api_id:
            from .platform.telegram import TelegramHandler
            self.handler = TelegramHandler()

        elif settings.matrix_hostname:
            from .platform.matrix import MatrixHandler
            self.handler = MatrixHandler()

        elif settings.rocket_chat_server:
            from .platform.rocket_chat import RocketChatHandler
            self.handler = RocketChatHandler()

        elif settings.bot_token:
            from .platform.discord import DiscordHandler
            self.handler = DiscordHandler()
       
        if self.handler:
                asyncio.create_task(self.handler.start())


class ChatManager():
    def __init__(self):
        self.latest_message = None
        self.lock = asyncio.Lock()

    async def start(self):
        pass

    async def get_latest_message(self):
        """Return the latest message."""
        async with self.lock:
            if self.latest_message:
                msg = self.latest_message
                self.latest_message = None
                return msg

        await asyncio.sleep(0.1)

    async def handle_message(self, message_content):
        """Handle a new message."""
        self.latest_message = message_content
