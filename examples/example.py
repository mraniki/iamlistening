"""
Provides example for iamlistening package
"""

import asyncio
import uvicorn
from fastapi import FastAPI

from iamlistening import Listener as bot


async def main():
    """Main"""
    while True:
        try:
            print(bot)
            await bot.start()

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
    uvicorn.run(app, host="0.0.0.0", port=8080)
