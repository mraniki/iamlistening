"""
Rocket Chat  🚀

"""

from loguru import logger
from rocketchat_API.rocketchat import RocketChat

from iamlistening.config import settings
from iamlistening.platform.platform_manager import ChatManager


class RocketChatHandler(ChatManager):

    def __init__(self):
        """
        Initialize the RocketChat handler.
        """
        super().__init__()
        

    async def start(self):
        """
        Start the RocketChat handler.
        """
        self.logger.debug("RocketChat setup")
        # rocket = RocketChat(
        #     user_id=settings.bot_user, 
        #     auth_token=settings.bot_auth_token, 
        #     server_url=settings.bot_hostname
        #     )
