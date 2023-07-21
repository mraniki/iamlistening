"""
Rocket Chat  🚀
"""
from iamlistening.config import settings
from iamlistening.main import Listener
from telethon import TelegramClient, events

class ListenerTelegram(Listener):

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