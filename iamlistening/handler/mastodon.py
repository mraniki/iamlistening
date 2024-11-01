"""
Mastodon 🐘
"""

import asyncio

from bs4 import BeautifulSoup
from loguru import logger
from mastodon import Mastodon, StreamListener

from ._client import ChatClient


class MastodonHandler(ChatClient):

    def __init__(self, **kwargs):
        """
        Initialize the Handler object

        """

        super().__init__(**kwargs)

    async def start(self):
        """
        Start the Mastodon handler.
        """
        logger.debug("Mastodon setup")
        self.bot = Mastodon(
            api_base_url=self.bot_hostname, access_token=self.bot_auth_token
        )
        self.connected()
        self.streamer = self.bot.stream_public(
            MastoListener(self.broadcast_message), run_async=True
        )

    async def broadcast_message(self, status):
        content = self.remove_html_tags(status)
        await self.handle_message(content)

    def remove_html_tags(self, text):
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text()


class MastoListener(StreamListener):
    def __init__(self, callback):
        """
        Initialize the Mastodon handler.
        """
        super().__init__()
        self.callback = callback

    def on_update(self, status):
        asyncio.run(self.callback(status["content"]))
