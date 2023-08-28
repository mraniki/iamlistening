import asyncio

from loguru import logger

from iamlistening.config import settings


class ChatManager:
    """
    Chat manager

    Attributes:
        platform (str): The platform to use
        bot (object): The bot
        is_connected (bool): Is the bot connected
        latest_message (str): The latest message
        iteration_limit (int): The iteration limit
        iteration_count (int): The iteration count

    Methods:
        start(self)
        get_handler(self)


    """

    @staticmethod
    def get_handler(platform=None):
        """
        Get platform handler.

        Args:
            platform (str): The platform to use

        Returns:
            PlatformHandler


        """
        handler = None
        if platform == "telegram":
            from .clients.telegram import TelegramHandler

            handler = TelegramHandler()
        elif platform == "discord":
            from .clients.discord import DiscordHandler

            handler = DiscordHandler()
        if platform == "matrix":
            from .clients.matrix import MatrixHandler

            handler = MatrixHandler()
        elif platform == "guilded":
            from .clients.guilded import GuildedHandler

            handler = GuildedHandler()
        elif platform == "mastodon":
            from .clients.mastodon import MastodonHandler

            handler = MastodonHandler()
        elif platform == "lemmy":
            from .clients.lemmy import LemmyHandler

            handler = LemmyHandler()
        elif platform == "twitch":
            from .clients.twitch import TwitchHandler

            handler = TwitchHandler()
        elif platform == "revolt":
            from .clients.revolt import RevoltHandler

            handler = RevoltHandler()

        return handler

    def __init__(self):
        """
        Initialize the chat manager.
        """
        self.platform = settings.chat_platform
        self.bot = None
        self.is_connected = True
        self.latest_message = None
        self.lock = asyncio.Lock()
        self.iteration_limit = settings.iteration_limit or -1
        self.iteration_count = 0

    async def start(self):
        """
        Start the chat manager.
        Specific to the client platform
        """

    def connected(self):
        """
        Asynchronously checks if 
        the listener is connected.

        Returns:
            None
        """
        logger.info(
            "listener handler is online on {}", self.platform)
        self.is_connected = True

    async def get_latest_message(self):
        """
        Return the latest message.

        Args:
            None

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

    async def handle_iteration_limit(self):
        """
        Handle the iteration limit logic.

        Returns:
            None
        """
        if self.iteration_count != self.iteration_limit:
            await asyncio.sleep(0.1)
            self.iteration_count += 1
        else:
            await self.disconnected()

        return

    async def disconnected(self):
        """
        Asynchronously disconnect the listener.

        Returns:
            None
        """
        self.is_connected = False
