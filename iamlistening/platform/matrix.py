"""
Matrix ⚫ 
"""
import asyncio

import simplematrixbotlib as botlib
from loguru import logger

from iamlistening.config import settings
from iamlistening.main import ChatManager


class MatrixHandler(ChatManager):

    def __init__(self):
        super().__init__()

    async def start(self):
        """Start the Matrix handler."""
        logger.debug("Matrix setup")
        config = botlib.Config()
        config.emoji_verify = True
        config.ignore_unverified_devices = True
        config.store_path = './config/matrix/'
        creds = botlib.Creds(
                    settings.matrix_hostname,
                    settings.matrix_user,
                    settings.matrix_pass
                    )
        bot = botlib.Bot(creds, config)
 
        @bot.listener.on_startup
        async def room_joined(room):
            logger.info("listener is online")

        @bot.listener.on_message_event
        async def on_matrix_message(room, message):
            await self.handle_message(message.body)
        await bot.api.login()
        bot.api.async_client.callbacks = botlib.Callbacks(
            bot.api.async_client, bot
            )
        await bot.api.async_client.callbacks.setup_callbacks()
        for action in bot.listener._startup_registry:
            for room_id in bot.api.async_client.rooms:
                await action(room_id)
        await bot.api.async_client.sync_forever(
            timeout=3000,
            full_state=True
            )
