"""
Mastodon 🐘
"""
from loguru import logger
from mastodon import Mastodon, StreamListener

from iamlistening.config import settings
from iamlistening.platform.platform_manager import ChatManager


class MastodonHandler(ChatManager):

    def __init__(self):
        super().__init__()

    async def start(self):
        """Start the Mastodon handler."""
        logger.debug("Mastodon setup")
        # bot = Mastodon(
        #     api_base_url="https://mastodon.social" or settings.mastodon_host,
        #     access_token = None or settings.mastodon_access_token)
        # print (bot.timeline(timeline='public',))
        # logger.info("listener is online")

        # async def on_update(StreamListener, status):
        #     await self.handle_message(status)

        # bot.stream_public(
        #     StreamListener(
        #         session_name=self.get_name(),
        #         user_id=self.db["user_id"])
        #         )
