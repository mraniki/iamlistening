"""
 IAmListening Main
"""

import asyncio

from loguru import logger

from iamlistening.clients import (
    DiscordHandler,
    GuildedHandler,
    LemmyHandler,
    MastodonHandler,
    MatrixHandler,
    TelegramHandler,
    TwitchHandler,
)
from iamlistening.config import settings


class Listener:
    """
    Listener Class for IAmListening.

    """

    def __init__(self):
        """
        Initialize the listener.

        Raises:
            Exception: Platform missing

        """
        self.platform_info = []
        platforms = settings.platform
        logger.debug("platforms {}", platforms)
        for client in platforms:
            logger.debug("platform {}", client)
            if platforms[client]["platform"] == "":
                logger.warning("Platform missing")
                continue
            client = self._create_client(
                platform=platforms[client]["platform"],
                bot_token=platforms[client]["bot_token"] or None,
                bot_channel_id=platforms[client]["bot_channel_id"] or None,
                bot_api_id=platforms[client]["bot_api_id"] or None,
                bot_api_hash=platforms[client]["bot_api_hash"] or None,
                bot_hostname=platforms[client]["bot_hostname"] or None,
                bot_user=platforms[client]["bot_user"] or None,
                bot_pass=platforms[client]["bot_pass"] or None,
                bot_auth_token=platforms[client]["bot_auth_token"] or None,
                iteration_enabled=platforms[client]["iteration_enabled"] or True,
                iteration_limit=platforms[client]["iteration_limit"] or -1,
            )
            logger.debug("client {} created", client)
            self.platform_info.append(client)
        logger.debug("init completed {}", self.platform_info)

    async def start(self):
        """
        Asynchronously start the listener.

        This method starts the chat managers for each platform
        and logs the status.

        """
        logger.debug("Listener starting")
        logger.debug("Platform info {}", self.platform_info)
        tasks = [client.start() for client in self.platform_info]
        await asyncio.gather(*tasks)

    def stop(self):
        """
        Stop the listener.

        This method stops the chat managers for each platform.

        """
        logger.debug("Listener stopping")

        for client in self.platform_info:
            client.stop()

        logger.debug("Listener stopped")

    def _create_client(self, **kwargs):
        """
        Get the handler object based on the specified platform.

        Returns:
            object: The handler object.
        """
        platform = kwargs["platform"]
        logger.debug("get handler {}", platform)
        if platform == "telegram":
            logger.debug("get telegram handler")
            return TelegramHandler(**kwargs)
        elif platform == "discord":
            return DiscordHandler(**kwargs)
        elif platform == "matrix":
            return MatrixHandler(**kwargs)
        elif platform == "guilded":
            return GuildedHandler(**kwargs)
        elif platform == "mastodon":
            return MastodonHandler(**kwargs)
        elif platform == "lemmy":
            return LemmyHandler(**kwargs)
        elif platform == "twitch":
            return TwitchHandler(**kwargs)
        else:
            logger.error("Invalid platform specified {}", platform)
