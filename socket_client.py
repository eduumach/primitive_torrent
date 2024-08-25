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

        file_data = await websocket.recv()
        print("File received from the server")

        with open("meme_down.jpg", "wb") as file:
            file.write(file_data)
            print("File saved as 'meme_down.jpg'")

if __name__ == "__main__":
    asyncio.run(download_file())
