"""
Discord  🟣
"""
# import discord

# from iamlistening.config import settings


# async def start_discord(listener):
#     """Start the Discord handler."""

#     intents = discord.Intents.default()
#     intents.message_content = True
#     bot = discord.Bot(intents=intents)

#     @bot.event
#     async def on_ready():
#         await listener.post_init()

#     @bot.event
#     async def on_message(message: discord.Message):
#         await listener.handle_message(message.content)

#         await bot.start(settings.bot_token)