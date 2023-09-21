import asyncio

from loguru import logger

from iamlistening.config import settings
from iamlistening.platform.clients import (
    DiscordHandler,
    GuildedHandler,
    LemmyHandler,
    MastodonHandler,
    MatrixHandler,
    RevoltHandler,
    TelegramHandler,
    TwitchHandler,
)


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

    def __init__(
        self,
        platform=None,
        bot_token=None,
        bot_channel_id=None,
        bot_api_id=None,
        bot_api_hash=None,
        bot_hostname=None,
        bot_user=None,
        bot_pass=None,
        bot_auth_token=None,
        iteration_enabled=True,
        iteration_limit=-1,
        iteration_count=0,
    ):
        """
        Initialize the chat manager.
        """
        logger.debug("init {}", platform)
        self.platform = platform
        self.bot_token = bot_token
        self.bot_channel_id = bot_channel_id
        self.bot_api_id = bot_api_id
        self.bot_api_hash = bot_api_hash
        self.bot_hostname = bot_hostname
        self.bot_user = bot_user
        self.bot_pass = bot_pass
        self.bot_auth_token = bot_auth_token
        self.iteration_enabled = iteration_enabled
        self.iteration_limit = iteration_limit
        self.iteration_count = iteration_count
        self.bot = None
        self.is_connected = True
        self.latest_message = None
        self.lock = asyncio.Lock()
        self.handler = self.get_handler()

    async def start(self):
        """
        Start the chat manager.
        Connect to the platform and handle messages.
        """
        try:
            # Connect to the platform
            await self.handler.start()

            # Start listening for messages
            await self.handler.listen(self.handle_message)
            
        except Exception as e:
            logger.error("Error starting {}: {}", self.platform, e)

    def get_handler(self):
        """
        Get the handler object based on the specified platform.

        Returns:
            object: The handler object.
        """
        logger.debug("get handler {}", self.platform)
        if self.platform == "telegram":
            return TelegramHandler()
        elif self.platform == "discord":
            return DiscordHandler()
        elif self.platform == "matrix":
            return MatrixHandler()
        elif self.platform == "guilded":
            return GuildedHandler()
        elif self.platform == "mastodon":
            return MastodonHandler()
        elif self.platform == "lemmy":
            return LemmyHandler()
        elif self.platform == "twitch":
            return TwitchHandler()
        elif self.platform == "revolt":
            return RevoltHandler()
        else:
            logger.error("Invalid platform specified {}", self.platform)
            # raise ValueError("Invalid platform specified")

    async def handle_message(self, message_content):
        """
        Handle a new message.

        Args:
            message_content (str): The content of the message.
        """
        self.latest_message = message_content
