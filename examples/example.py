"""Provides example for iamlistening package."""
import asyncio
import sys

import uvicorn
from fastapi import FastAPI
from loguru import logger

from iamlistening import Listener

logger.remove()
logger.add(sys.stderr, level="DEBUG")


async def main():
    """Run a listener example."""
    listener = Listener()
    await listener.start()
    # INFO     | iamlistening.clients.client:connected:64 - listener handler is online on telegram
    # INFO     | iamlistening.clients.client:connected:64 - listener handler is online on discord
    # DEBUG    | iamlistening.clients.discord:on_message:29 - new message received
    # DEBUG    | iamlistening.clients.client:handle_message:95 - Frasier👂 on discord: test
    # DEBUG    | iamlistening.clients.client:handle_iteration_limit:108 - iteration count: 1
    # DEBUG    | iamlistening.clients.telegram:handle_telegram_message:36 - new message received
    # DEBUG    | iamlistening.clients.client:handle_message:95 - Frasier👂 on telegram: test 2
    # DEBUG    | iamlistening.clients.client:handle_iteration_limit:108 - iteration count: 1


app = FastAPI()


@app.on_event("startup")
async def start():
    """Startup."""
    asyncio.create_task(main())


@app.get("/")
def read_root():
    """Root."""
    return {"online"}


@app.get("/health")
def health_check():
    """Healthcheck."""
    return {"online"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8015)
