"""
Provides example for iamlistening package
"""
import logging
import asyncio
import uvicorn
from fastapi import FastAPI
# DEBUG LEVEL
logging.basicConfig(level=logging.DEBUG)

from iamlistening import Listener

async def main():
    """Run main program loop."""
    bot = Listener()
    latest_msg = None
    while True:
        try:
            await bot.start()
            msg = bot.get_latest_message()
            if msg != latest_msg:
                latest_msg = msg
                print(f"Latest message: {latest_msg}")

        except Exception as e:
            print(e)

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
    uvicorn.run(app, host="0.0.0.0", port=8082)
