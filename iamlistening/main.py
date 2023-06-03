"""
 IAmListening Main
"""

import os
import sys
import asyncio
import logging 
from functools import wraps

import apprise
from apprise import NotifyFormat
from telethon import TelegramClient, events
import discord
import simplematrixbotlib as botlib

from .config import settings


# 🤖BOT

class Listener:
    """ iamlistening class """

    def __init__(self):
        self.logger = logging.getLogger("Listener")
        self.other_class = OtherClass()
    async def start(self):
        # token = settings.bot_token
        # channel = settings.bot_channel_id
        if settings.discord_webhook_id:
            # DISCORD
            intents = discord.Intents.default()
            intents.message_content = True
            bot = discord.Bot(intents=intents)

            @bot.event
            async def on_ready():
                await self.post_init()

            @bot.event
            async def on_message(message: discord.Message):
                await self.event_action(message.content)
            await bot.start(settings.bot_token)
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
                await self.event_action(message.body)
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
        elif settings.telethon_api_id:
            # TELEGRAM
            bot = await TelegramClient(
                        None,
                        settings.telethon_api_id,
                        settings.telethon_api_hash
                        ).start(bot_token=settings.bot_token)
            await self.post_init()

            @bot.on(events.NewMessage())
            async def telethon(event):
                await self.event_action(event.message.message)

            await bot.run_until_disconnected()
        else:
            self.logger.warning("Check settings")
            await asyncio.sleep(7200)

    async def post_init(self):
        return
    @staticmethod
    def handle_event(func):
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            event = args[0]
            if isinstance(event, discord.Message):
                await self.handle_discord_message(event)
            elif isinstance(event, botlib.Message):
                await self.handle_matrix_message(event)
            elif isinstance(event, events.NewMessage):
                await self.handle_telegram_message(event.message.message)
            return await func(self, *args, **kwargs)
        return wrapper

    @handle_event
    async def event_action(self, event):
        print(event)
        return event 
# async def notify(msg):
#     """💬 MESSAGING """
#     if not msg:
#         return
#     apobj = apprise.Apprise()
#     if settings.discord_webhook_id:
#         url = (f"discord://{str(settings.discord_webhook_id)}/"
#                f"{str(settings.discord_webhook_token)}")
#         if isinstance(msg, str):
#             msg = msg.replace("<code>", "`")
#             msg = msg.replace("</code>", "`")
#     elif settings.matrix_hostname:
#         url = (f"matrixs://{settings.matrix_user}:{settings.matrix_pass}@"
#                f"{settings.matrix_hostname[8:]}:443/"
#                f"{str(settings.bot_channel_id)}")
#     else:
#         url = (f"tgram://{str(settings.bot_token)}/"
#                f"{str(settings.bot_channel_id)}")
#     try:
#         apobj.add(url)
#         await apobj.async_notify(body=str(msg), body_format=NotifyFormat.HTML)
#     except Exception as e:
#         logger.error("%s not sent: %s", msg, e)

