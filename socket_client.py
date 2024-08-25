#!/usr/bin/env python

import asyncio

from websockets.asyncio.client import connect
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

async def hello():
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    uri = f"ws://{host}:{port}"
    async with connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"Client >>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())
