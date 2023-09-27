"""
Matrix ⚫
"""

import simplematrixbotlib as botlib
from loguru import logger

from .client import ChatClient


class MatrixHandler(ChatClient):
    async def start(self):
        """
        Start the Matrix handler.
        """
        logger.debug("Matrix setup")
        config = botlib.Config()
        config.emoji_verify = True
        config.ignore_unverified_devices = True
        config.store_path = "./config/matrix/"
        creds = botlib.Creds(self.bot_hostname, self.bot_user, self.bot_pass)
        self.bot = botlib.Bot(creds, config)

        @self.bot.listener.on_startup
        async def room_joined(room):
            self.connected()

        @self.bot.listener.on_message_event
        async def on_matrix_message(room, message):
            await self.handle_message(message.body)

        await self.bot.api.login()
        self.bot.api.async_client.callbacks = botlib.Callbacks(
            self.bot.api.async_client, self.bot
        )
        await self.bot.api.async_client.callbacks.setup_callbacks()
        for action in self.bot.listener._startup_registry:
            for room_id in self.bot.api.async_client.rooms:
                await action(room_id)
        await self.bot.api.async_client.sync_forever(timeout=3000, full_state=True)
