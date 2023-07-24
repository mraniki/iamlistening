"""
 IAmListening Main
"""

import asyncio
import threading

import discord
import simplematrixbotlib as botlib

# import logging
from loguru import logger
from telethon import TelegramClient, events

from iamlistening import __version__

from .config import settings

# from .platform.discord import start_discord
# from .platform import discord, matrix, rocket_chat, telegram


class Listener:
    """ 👂 Listener class """

    def __init__(self):
        self.logger = logger
        # logging.getLogger("Listener")
        self.latest_message = None
        self.loop = asyncio.get_event_loop()
        self.lock = threading.Lock()
        self.stopped = False

    async def get_info_listener(self):
        return (f"ℹ️ IAmListening v{__version__}\n")

    async def start(self):
        """Start the listener."""
        if settings.telethon_api_id:
            await self.start_telegram()

        elif settings.matrix_hostname:
            await self.start_matrix()

        elif settings.rocket_chat_server:
            await self.start_rocket_chat()

        elif settings.bot_token:
            await self.start_discord()

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
        """Run the listener for 
        a specified number of iterations or until stopped."""

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

    async def start_discord(self):
        """Start the Discord handler."""
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

    async def start_telegram(self):
        """Start the Telegram handler."""
        self.logger.debug("Telegram setup")
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


    async def start_matrix(self):
        """Start the Matrix handler."""
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

    async def start_rocket_chat(self):
        """Start the RocketChat handler."""
        self.logger.debug("RocketChat setup")
