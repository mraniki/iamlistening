"""
 IAmListening Main
"""

import asyncio
import logging
import threading

import discord
from telethon import TelegramClient, events
import simplematrixbotlib as botlib

from .config import settings


class Listener:
    """ 👂 Listener class """

    def __init__(self):
        self.logger = logging.getLogger("Listener")
        self.latest_message = None
        self.loop = asyncio.get_event_loop()
        self.lock = threading.Lock()
        self.stopped = False
    
    async def start(self):
        """start"""

        if settings.telethon_api_id:
            # TELEGRAM
            bot = await TelegramClient(
                        None,
                        settings.telethon_api_id,
                        settings.telethon_api_hash
                        ).start(bot_token=settings.bot_token)
            await self.post_init()

            @bot.on(events.NewMessage())
            async def telethon(event):
                await self.handle_message(event.message.message)

            await bot.run_until_disconnected()

        elif settings.matrix_hostname:
            # MATRIX
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
        elif settings.bot_token:
            # DISCORD
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


    async def run_forever(self):
        """Run the listener forever."""
        while not self.stopped:
            await self.start()

    async def post_init(self):
        return "bot is online"

    def stop(self):
        """Stop the listener."""
        self.stopped = True
