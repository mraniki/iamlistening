"""
 IAmListening Main
"""

import asyncio
import logging
import threading

import discord
import simplematrixbotlib as botlib
from telethon import TelegramClient, events

from iamlistening import __version__, platform
from iamlistening.platform import RockerChatHandler

from .config import settings



class Listener:
    """ 👂 Listener class """

    def __init__(self):
        self.logger = logging.getLogger("Listener")
        self.latest_message = None
        self.loop = asyncio.get_event_loop()
        self.lock = threading.Lock()
        self.stopped = False
        self.platform = None

    async def get_info_listener(self):
        return (f"ℹ️ {__class__.__name__} {__version__}\n")

    async def start(self):
        """start"""

        if settings.telethon_api_id:
            # TELEGRAM
            self.platform = ListenerTelegram()
        elif settings.matrix_hostname:
            # MATRIX

            self.logger.debug("Matrix setup")
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
                await self.post_init()

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
        elif settings.rocket_chat_server:
            # ROCKET CHAT
            rocket_chat_handler = RockerChatHandler()
            await rocket_chat_handler.start()

        elif settings.bot_token:
            # DISCORD
            self.platform = ListenerMatrix()
        
        self.platform.start_client()
        if self.platform.start_client():
            await self.get_info_listener()
        else:
            self.logger.warning("Check settings")
            await asyncio.sleep(7200)
    

    async def get_latest_message(self):
        """Return the latest message."""
        while True:
            with self.lock:
                if self.latest_message is not None:
                    msg = self.latest_message
                    self.latest_message = None
                    return msg

            await asyncio.sleep(0.1)

    async def handle_message(self, message_content):
        """Handle a new message."""
        self.latest_message = message_content


    async def run_forever(self, max_iterations=None):
        """Run the listener for a specified number of iterations or until stopped."""
        iteration = 0
        while not self.stopped and (
            max_iterations is None or iteration < max_iterations):
            await self.start()
            iteration += 1

    async def post_init(self):
        return "bot is online"

    def stop(self):
        """Stop the listener."""
        self.stopped = True
