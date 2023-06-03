"""
Provides example for iamlistening package
"""
import logging
import asyncio
import uvicorn
from fastapi import FastAPI

from iamlistening import Listener



# DEBUG LEVEL
logging.basicConfig(level=logging.DEBUG)


async def main():
    """Run main program loop."""
    listener = Listener()
    task = asyncio.create_task(listener.run_forever())
    while True:
        try:
            msg = await listener.get_latest_message()
            if msg:
                print(f"Frasier👂: {msg}")

        except Exception as error:
            print(error)
    await task

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
