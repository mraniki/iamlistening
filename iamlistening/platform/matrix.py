# """
# Matrix ⚫ 
# """
# import simplematrixbotlib as botlib

# from iamlistening.config import settings


# async def start_matrix(listener):
#     """Start the Matrix handler."""

#     config = botlib.Config()
#     config.emoji_verify = True
#     config.ignore_unverified_devices = True
#     config.store_path = './config/matrix/'
#     creds = botlib.Creds(
#                 settings.matrix_hostname,
#                 settings.matrix_user,
#                 settings.matrix_pass
#                 )
#     bot = botlib.Bot(creds, config)

#     @bot.listener.on_startup
#     async def room_joined(room):
#         await listener.post_init()

#     @bot.listener.on_message_event
#     async def on_matrix_message(room, message):
#         await listener.handle_message(message.body)
#     await bot.api.login()
#     bot.api.async_client.callbacks = botlib.Callbacks(
#         bot.api.async_client, bot
#         )
#     await bot.api.async_client.callbacks.setup_callbacks()
#     for action in bot.listener._startup_registry:
#         for room_id in bot.api.async_client.rooms:
#             await action(room_id)
#     await bot.api.async_client.sync_forever(
#         timeout=3000,
#         full_state=True
#         )
