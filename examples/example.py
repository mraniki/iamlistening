"""Provides example for iamlistening package."""

import asyncio

from iamlistening import Listener


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
        for client in listener.clients:
            msg = await client.get_latest_message()
            if msg:
                print(f"Frasier👂: {msg}")


# iamlistening.clients.client:handle_message:96 - Frasier👂 on discord: echo
# iamlistening.clients.client:get_latest_message:80 - Latest message discord: echo
# __main__:main:33 - Frasier👂: echo


if __name__ == "__main__":
    asyncio.run(main())
