"""
tradingeconomics 🔘
"""

import asyncio
import json
import threading

import tradingeconomics as te
from loguru import logger

from ._client import ChatClient


class TradingeconomicsHandler(ChatClient):

    def __init__(self, **kwargs):
        """
        Initialize the Handler object

        """
        super().__init__(**kwargs)
        te.login()

    async def start(self):
        """
        Start the Tradingeconomics handler.

        """
        logger.debug("Tradingeconomics start")
        loop = asyncio.get_event_loop()
        news_subscriber = NewsSubscriber(self.handle_message, loop)
        news_subscriber.subscribe()


class NewsSubscriber:
    def __init__(self, on_message_callback, loop=None):
        self.on_message_callback = on_message_callback
        self.loop = loop or asyncio.get_event_loop()

    def subscribe(self):
        def on_message(ws, message):
            latest_news = json.loads(message)
            logger.info("Received message: {}", latest_news)
            if self.filter_news(latest_news):
                if self.loop.is_running():
                    asyncio.run_coroutine_threadsafe(
                        self.on_message_callback(latest_news), self.loop
                    )
                else:
                    logger.error("No running event loop to handle the message")

        te.subscribe("news")
        thread = threading.Thread(target=te.run, args=(on_message,))
        thread.start()

    def filter_news(self, latest_news):
        return latest_news.get("topic") != "keepalive"
