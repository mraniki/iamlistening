"""
 IAmListening Main
"""

import asyncio

from loguru import logger

from iamlistening import __version__
from iamlistening.clients import (
    DiscordHandler,
    GuildedHandler,
    LemmyHandler,
    MastodonHandler,
    MatrixHandler,
    RevoltHandler,
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
        try:
            config = settings.platform
            self.clients = []
            for item in config:
                _config = config[item]
                if item in ["", "template"]:
                    continue
                client = self._create_client(
                    platform=_config.get("platform"),
                    bot_token=_config.get("bot_token"),
                    bot_channel_id=_config.get("bot_channel_id"),
                    bot_api_id=_config.get("bot_api_id"),
                    bot_api_hash=_config.get("bot_api_hash"),
                    bot_hostname=_config.get("bot_hostname"),
                    bot_user=_config.get("bot_user"),
                    bot_pass=_config.get("bot_pass"),
                    bot_auth_token=_config.get("bot_auth_token"),
                    iteration_enabled=_config.get("iteration_enabled", True),
                    iteration_limit=_config.get("iteration_limit", -1),
                )
                self.clients.append(client)

        except Exception as e:
            logger.error("init: {}", e)

    async def start(self):
        """
        Asynchronously start the listener.

        This method starts the chat managers for each platform
        and logs the status.

        """
        logger.debug("Listener starting")
        tasks = [client.start() for client in self.clients]
        await asyncio.gather(*tasks)

    def stop(self):
        """
        Stop the listener.

        This method stops the chat managers for each platform.

        """
        for client in self.clients:
            client.stop()

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
        elif platform == "revolt":
            return RevoltHandler(**kwargs)
        else:
            logger.error("Invalid platform specified {}", platform)

    def get_info(self):
        """
        Retrieves information about the exchange
        and the account.

        :return: A formatted string containing
        the exchange name and the account information.
        :rtype: str
        """
        version_info = f"ℹ️ {type(self).__name__} {__version__}\n"
        client_info = "".join(f"👂 {client.platform}\n" for client in self.clients)
        return version_info + client_info.strip()
