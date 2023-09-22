"""
Provides example for iamlistening package
"""
import asyncio
import sys

import uvicorn
from fastapi import FastAPI
from loguru import logger

from iamlistening import Listener

logger.remove()
logger.add(sys.stderr, level="DEBUG")


async def main():
    """
    Run a listener example
    """

    listener = Listener()
    await listener.start()
    for platform in listener.platform_info:
        if platform:
            while platform.handler.connected:
                msg = await platform.handler.get_latest_message()
                if msg:
                    logger.info(f"Frasier👂: {msg}")
                    await platform.handler.handle_iteration_limit()


app = FastAPI()


@app.on_event("startup")
async def start():
    """startup"""
    asyncio.create_task(main())


@app.get("/")
def read_root():
    """root"""
    return {"online"}


@app.get("/health")
def health_check():
    """healthcheck"""
    return {"online"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8015)
