# """
# Telegram 🔵
# """
# from telethon import TelegramClient, events

# from iamlistening.config import settings


# async def start_telegram(listener):
#     """Start the Telegram handler."""

#     bot = await TelegramClient(
#         None,
#         settings.telethon_api_id,
#         settings.telethon_api_hash
#         ).start(bot_token=settings.bot_token)
#     await listener.post_init()

#     @bot.on(events.NewMessage())
#     async def telethon(event):
#         await listener.handle_message(
#             event.message.message)

#     await bot.run_until_disconnected()