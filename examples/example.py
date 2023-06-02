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
    """Main"""
    while True:
        try:
            bot = Listener()
            print(bot)
            await bot.start()

            await asyncio.sleep(7200)
        except Exception as error:
            print(error)


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
    uvicorn.run(app, host="0.0.0.0", port=8081)
