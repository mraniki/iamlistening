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
    """Run main program loop."""
    listener = Listener()
    await listener.start()
    while True:
        try:
            logger.info(f"Info: {listener.get_info_listener()}")
            msg = await listener.handler.get_latest_message()
            if msg:
                logger.info(f"Frasier👂: {msg}")

        except Exception as error:
            logger.error(error)

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
    uvicorn.run(app, host="0.0.0.0", port=8014)
