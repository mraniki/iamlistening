# """
# Lemmy  🐭
# """
# import asyncio

# from loguru import logger


# from iamlistening.config import settings
# from iamlistening.platform.chat_manager import ChatManager


# class LemmyHandler(ChatManager):

#     def __init__(self):
#         """
#         Initialize the Lemmy handler.

 
#         """
#         super().__init__()

#     async def start(self):
#         """
#         Start the Lemmy handler.
        
#         """

#         lemmy = Lemmy(settings.bot_hostname)
#         lemmy.log_in(settings.bot_user,settings.bot_pass)

#         latest_post = lemmy.post.list()[0]["post"]["id"]
        
#         await self.handle_message(latest_post)


