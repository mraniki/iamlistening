"""
Mastodon 🐘
"""
import asyncio

from bs4 import BeautifulSoup
from loguru import logger
from mastodon import Mastodon, StreamListener

from iamlistening.config import settings
from iamlistening.platform.platform_manager import ChatManager


class MastodonHandler(ChatManager):

    def __init__(self):
        """
        Initialize the Mastodon handler.
        """
        super().__init__()
        logger.debug("Mastodon setup")
        self.client = Mastodon(
            api_base_url= settings.mastodon_host,
            access_token = settings.mastodon_access_token)

    async def start(self):
        """
        Start the Mastodon handler.
        """
        logger.info("listener is online")
        self.streamer = self.client.stream_public(
            MastoListener(self.broadcast_message),
            run_async=True)

    async def broadcast_message(self, status):
        content = self.remove_html_tags(status)
        logger.warning(content)
        await self.handle_message(content)

    def remove_html_tags(self, text):
        soup = BeautifulSoup(text, "html.parser")
        cleaned_text = soup.get_text()
        return cleaned_text


class MastoListener(StreamListener):
    def __init__(self,callback):
        """
        Initialize the Mastodon handler.
        """
        super().__init__()
        self.callback = callback

    def on_update(self, status):
        asyncio.run(self.callback(status['content']))
