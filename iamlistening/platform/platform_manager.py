
import asyncio

from loguru import logger


class PlatformManager:
    @staticmethod
    def get_handler(platform):
        """
        Get platform handler.
        """

        handler = None

        if platform == "telegram":
            from .clients.telegram import TelegramHandler
            handler = TelegramHandler()
        elif platform == "matrix":
            from .clients.matrix import MatrixHandler
            handler = MatrixHandler()
        elif platform == "discord":
            from .clients.discord import DiscordHandler
            handler = DiscordHandler()
        elif platform == "rocket_chat":
            from .clients.rocket_chat import RocketChatHandler
            handler = RocketChatHandler()
        elif platform == "guilded":
            from .clients.guilded import GuildedHandler
            handler = GuildedHandler()
        elif platform == "mastodon":
            from .clients.mastodon import MastodonHandler
            handler = MastodonHandler()
        elif platform == "revolt":
            from .clients.revolt import RevoltHandler
            handler = RevoltHandler()
        elif platform == "tinode":
            from .clients.tinode import TinodeHandler
            handler = TinodeHandler()

        if handler is None:
            raise Exception("Platform not supported")

        return handler


class ChatManager():
    def __init__(self):
        """
        Initialize the chat manager.
        """

        self.latest_message = None
        self.lock = asyncio.Lock()


    async def start(self):
        """ 
        Start the chat manager.
        Specific to the client platform
        """
        pass

    async def get_latest_message(self):
        """
        Return the latest message.

        Returns:
            str: The latest message.
        """
        async with self.lock:
            if self.latest_message:
                msg = self.latest_message
                self.latest_message = None
                return msg

        await asyncio.sleep(0.1)

    async def handle_message(self, message_content):
        """
        Handle a new message.

        Args:
            message_content (str): The content of the message.
        """
        self.latest_message = message_content
