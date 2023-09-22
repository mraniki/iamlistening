"""
Lemmy  🐭

"""

from loguru import logger
from pythorhead import Lemmy

from .client import ChatClient


class LemmyHandler(ChatClient):
    async def start(self):
        """
        Start the Lemmy handler.

        """
        logger.info("Lemmy setup")
        self.bot = Lemmy(self.bot_hostname)
        self.bot.log_in(
            self.bot_user,
            self.bot_pass,
        )

        if self.bot:
            self.connected()
        # getting the first post id
        latest_post = self.bot.post.list(community_name=self.bot_channel_id)[0]["post"][
            "body"
        ]
        logger.debug("latest post: ", latest_post)
        await self.handle_message(latest_post)
