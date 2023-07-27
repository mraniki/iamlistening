"""
Rocket Chat  🚀

"""

from loguru import logger
from rocketchat_API.rocketchat import RocketChat

from iamlistening.config import settings
from iamlistening.platform.platform_manager import ChatManager


class RocketChatHandler(ChatManager):

    def __init__(self):
        super().__init__()


    async def start(self):
        """Start the RocketChat handler."""
        self.logger.debug("RocketChat setup")
        # rocket = RocketChat(
        #     user_id=settings.rocket_chat_user_id, 
        #     auth_token=settings.rocket_chat_auth_token, 
        #     server_url=settings.rocket_chat_server
        #     )
        
        # self.logger.debug(rocket.channels_list())