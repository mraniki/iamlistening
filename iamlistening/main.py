"""
 IAmListening Main
"""
__version__ = "0.0.0"

import os
import sys
import asyncio
import logging 

import apprise
from apprise import NotifyFormat
from telethon import TelegramClient, events
import discord
import simplematrixbotlib as botlib

from .config import settings


# 🤖BOT

class Listener:
    """ i am listening class """

    def __init__(
        self,
    ):
        self.logger = logging.getLogger(name="Listener")
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
                await self.event(message.content)
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
                await self.event(message.body)
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
                await self.event(event.message.message)

            await bot.run_until_disconnected()
        else:
            logger.warning("Check settings")
            await asyncio.sleep(7200)

    async def post_init(self):
        return
    async def event(self, event):
        print(event)
        return
# async def listener():
#     """Launch Bot Listener"""
#     try:
#         await load_exchange()
#     except Exception as e:
#         logger.error("exchange: %s", e)
#     try:
#         while True:
#             if settings.discord_webhook_id:
#                 # DISCORD
#                 intents = discord.Intents.default()
#                 intents.message_content = True
#                 bot = discord.Bot(intents=intents)

#                 @bot.event
#                 async def on_ready():
#                     await post_init()

#                 @bot.event
#                 async def on_message(message: discord.Message):
#                     await parse_message(message.content)
#                 await bot.start(settings.bot_token)
#             elif settings.matrix_hostname:
#                 # MATRIX
#                 config = botlib.Config()
#                 config.emoji_verify = True
#                 config.ignore_unverified_devices = True
#                 config.store_path = './config/matrix/'
#                 creds = botlib.Creds(
#                             settings.matrix_hostname,
#                             settings.matrix_user,
#                             settings.matrix_pass
#                             )
#                 bot = botlib.Bot(creds, config)

#                 @bot.listener.on_startup
#                 async def room_joined(room):
#                     await post_init()

#                 @bot.listener.on_message_event
#                 async def on_matrix_message(room, message):
#                     await parse_message(message.body)
#                 await bot.api.login()
#                 bot.api.async_client.callbacks = botlib.Callbacks(
#                                                     bot.api.async_client, bot
#                                                     )
#                 await bot.api.async_client.callbacks.setup_callbacks()
#                 for action in bot.listener._startup_registry:
#                     for room_id in bot.api.async_client.rooms:
#                         await action(room_id)
#                 await bot.api.async_client.sync_forever(
#                                                         timeout=3000,
#                                                         full_state=True
#                                                     )
#             elif settings.telethon_api_id:
#                 # TELEGRAM
#                 bot = await TelegramClient(
#                             None,
#                             settings.telethon_api_id,
#                             settings.telethon_api_hash
#                             ).start(bot_token=settings.bot_token)
#                 await post_init()

#                 @bot.on(events.NewMessage())
#                 async def telethon(event):
#                     await parse_message(event.message.message)

#                 await bot.run_until_disconnected()
#             else:
#                 logger.warning("Check settings")
#                 await asyncio.sleep(7200)

#     except Exception as e:
#         logger.error("Bot not started: %s", e)
        
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

