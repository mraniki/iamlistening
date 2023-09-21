# """
# Rocket Chat  🚀

# WIP
# """

# from loguru import logger
# from rocketchat_API.rocketchat import RocketChat
# from .client import ChatClient


# class RocketChatHandler(ChatClient):

#     def __init__(self):
#         """
#         Initialize the RocketChat handler.
#         """
#         super().__init__()


#     async def start(self):
#         """
#         Start the RocketChat handler.
#         """
#         self.logger.debug("RocketChat setup")
#         self.bot = RocketChat(
#             user_id=self.bot_user,
#             auth_token=self.bot_auth_token,
#             server_url=self.bot_hostname
#             )
#         info = self.bot.info()
#         self.logger.debug(info)
