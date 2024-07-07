"""
 IAmListening Main
"""

import asyncio
import importlib

from loguru import logger

from iamlistening import __version__
from iamlistening.config import settings


class Listener:
    """
    Listener Class for IAmListening.

    This class provides methods for
    starting and stopping the listener
    for each platform.

    Methods:
        _create_client(self, **kwargs)
        get_all_client_classes(self)
        get_info(self)
        start(self)
        stop(self)

    """

    def __init__(self):
        """
        Initializes the class instance by creating and appending clients
        based on the configuration in `settings.platform`.

        Checks if the module is enabled by looking at `settings.iamlistening_enabled`.
        If the module is disabled, no clients will be created.

        Creates a mapping of library names to client classes.
        This mapping is used to create new clients based on the configuration.

        If a client's configuration exists in `settings.platform` and its "enabled"
        key is truthy, it will be created.
        Clients are not created if their name is "template" or empty string.

        If a client is successfully created, it is appended to the `clients` list.

        If a client fails to be created, a message is logged with the name of the
        client and the error that occurred.

        Parameters:
            None

        Returns:
            None
        """
        # Check if the module is enabled
        self.enabled = settings.iamlistening_enabled
        # Create a mapping of library names to client classes
        self.client_classes = self.get_all_client_classes()
        # logger.debug("client_classes available {}", self.client_classes)

        if not self.enabled:
            logger.info("Module is disabled. No Client will be created.")
            return
        self.clients = []
        # Create a client for each client in settings.iamlistening
        for name, client_config in settings.platform.items():
            if (
                # Skip empty client configs
                client_config is None
                # Skip non-dict client configs
                or not isinstance(client_config, dict)
                # Skip template and empty string client names
                or name in ["", "template"]
                # Skip disabled clients
                or not client_config.get("enabled")
            ):
                continue

            # Create the client
            logger.debug("Creating client {}", name)
            client = self._create_client(**client_config, name=name)
            # If the client has a valid client attribute, append it to the list
            if client and getattr(client, "client", None):
                self.clients.append(client)

        # Log the number of clients that were created
        logger.info(f"Loaded {len(self.clients)} clients")
        if not self.clients:
            logger.warning(
                "No Client were created. Check your settings or disable the module."
            )

    def _create_client(self, **kwargs):
        """
        Create a client based on the given protocol.

        This function takes in a dictionary of keyword arguments, `kwargs`,
        containing the necessary information to create a client. The required
        key in `kwargs` is "library", which specifies the protocol to use for
        communication with the LLM. The value of "platform" must match one of the
        libraries supported by iamlistening.

        This function retrieves the class used to create the client based on the
        value of "library" from the mapping of library names to client classes
        stored in `self.client_classes`. If the value of "library" does not
        match any of the libraries supported, the function logs an error message
        and returns None.

        If the class used to create the client is found, the function creates a
        new instance of the class using the keyword arguments in `kwargs` and
        returns it.

        The function returns a client object based on the specified protocol
        or None if the library is not supported.

        Parameters:
            **kwargs (dict): A dictionary of keyword arguments containing the
            necessary information for creating the client. The required key is
            "platform".

        Returns:
            A client object based on the specified protocol or None if the
            library is not supported.

        """
        library = (
            kwargs.get("library")
            or kwargs.get("platform")
            or kwargs.get("protocol")
            or kwargs.get("parser_library")
            or "telegram"
        )
        cls = self.client_classes.get((f"{library.capitalize()}Handler"))
        return None if cls is None else cls(**kwargs)

    def get_all_client_classes(self):
        """
        Retrieves all client classes from the `iamlistening.protocol` module.

        This function imports the `iamlistening.protocol` module and retrieves
        all the classes defined in it.

        The function returns a dictionary where the keys are the
        names of the classes and the values are the corresponding
        class objects.

        Returns:
            dict: A dictionary containing all the client classes
            from the `iamlistening.protocol` module.
        """
        provider_module = importlib.import_module("iamlistening.handler")
        return {
            name: cls
            for name, cls in provider_module.__dict__.items()
            if isinstance(cls, type)
        }

    async def get_info(self):
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

    async def start(self):
        """
        Asynchronously start the listener.

        This method starts the chat managers for each platform
        and logs the status.

        """
        logger.debug("Listener starting")
        if not self.clients:
            logger.warning("No client to start")
            return
        tasks = [client.start() for client in self.clients]
        await asyncio.gather(*tasks)

    def stop(self):
        """
        Stop the listener.

        This method stops the chat managers for each platform.

        """
        for client in self.clients:
            client.stop()
