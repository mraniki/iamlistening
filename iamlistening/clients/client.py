import asyncio

from loguru import logger


class ChatClient:

    """Chat Client Base Class"""

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
    ):
        """
        Initialize the chat client.
        """
        self.platform = platform
        self.bot_token = bot_token
        self.bot_channel_id = bot_channel_id
        self.bot_api_id = bot_api_id
        self.bot_api_hash = bot_api_hash
        self.bot_hostname = bot_hostname
        self.bot_user = bot_user
        self.bot_pass = bot_pass
        self.bot_auth_token = bot_auth_token
        self.bot = None
        self.is_connected = True
        self.latest_message = None
        self.lock = asyncio.Lock()
        self.iteration_enabled = iteration_enabled
        self.iteration_limit = iteration_limit
        self.iteration_count = 0

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
                logger.debug("Latest message {}: {}", self.platform, msg)
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
            logger.debug("Frasier👂 on {}: {}", self.platform, message_content)
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
