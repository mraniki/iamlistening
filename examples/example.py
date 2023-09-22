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

    # standalone
    # await listener.start()
    # INFO     | listener handler is online on telegram
    # INFO     | listener handler is online on discord
    # DEBUG    | new message received
    # DEBUG    | Frasier👂 on discord: test
    # DEBUG    | iteration count: 1
    # DEBUG    | new message received
    # DEBUG    | Frasier👂 on telegram: test 2
    # DEBUG    | iteration count: 1

    # or in a loop
    loop = asyncio.get_running_loop()
    loop.create_task(listener.start())
    while True:
        for client in listener.platform_info:
            msg = await client.get_latest_message()
            if msg:
                logger.info(f"Frasier👂: {msg}")


# iamlistening.clients.client:handle_message:96 - Frasier👂 on discord: echo
# iamlistening.clients.client:get_latest_message:80 - Latest message discord: echo
# __main__:main:33 - Frasier👂: echo

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
