import asyncio

from loguru import logger


class ChatClient:
    """
    Chat Client Base Class

    Args:
        **kwargs:

    Methods:
        start(self)
        stop(self)
        connected(self)
        disconnected(self)
        get_latest_message(self)
        handle_message(self, message_content)
        handle_iteration_limit(self)
        disconnect(self)

    """

    def __init__(self, **kwargs):
        """
        Initialize the chat client.
        """
        get = kwargs.get
        self.__dict__.update(kwargs)

        self.name = get("name", None)
        self.enabled = kwargs.get("enabled", None)

        self.platform = get("library") or get("platform") or None
        self.bot_token = get("bot_token", None)
        self.bot_channel_id = get("bot_channel_id", None)
        self.bot_api_id = get("bot_api_id", None)
        self.bot_api_hash = get("bot_api_hash", None)
        self.bot_hostname = get("bot_hostname", None)
        self.bot_user = get("bot_user", None)
        self.bot_pass = get("bot_pass", None)
        self.bot_auth_token = get("bot_auth_token", None)
        self.bot = None
        self.is_connected = True
        self.latest_message = None
        self.lock = asyncio.Lock()
        self.iteration_enabled = get("iteration_enabled", None)
        self.iteration_limit = get("iteration_limit", None)
        self.iteration_count = 0
        self.client = self.name

    async def start(self):
        """
        Start the chat client.
        Specific to the client platform
        """

    async def stop(self):
        """
        Stop the chat client.
        Specific to the client platform
        """

    def connected(self):
        """
        Asynchronously checks if
        the listener is connected.

        Returns:
            None
        """
        logger.info("client is online on {}", self.platform)
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
                # logger.debug("Latest message {}: {}", self.platform, msg)
                self.latest_message = None
                return msg

        await asyncio.sleep(0.1)

    async def handle_message(self, message_content):
        """
        Handle a new message.

        Args:
            message_content (str): The content of the message.
        """

        if self.is_connected:
            self.latest_message = message_content
            # logger.debug("Frasier👂 on {}: {}", self.platform, message_content)
            await self.handle_iteration_limit()

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
            logger.debug("iteration limit reached for {}", self.platform)
            await self.disconnected()

        return

    async def disconnected(self):
        """
        Asynchronously disconnect the listener.

        Returns:
            None
        """
        logger.debug("{} Disconnected", self.platform)
        self.is_connected = False
