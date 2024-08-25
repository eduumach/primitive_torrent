#!/usr/bin/env python

import asyncio
import os
from websockets.asyncio.server import serve

async def send_file(websocket, path):
    if os.path.exists(path):
        with open(path, 'rb') as file:
            data = file.read()
            await websocket.send(data)
            print(f"Server sent the file: {path}")
    else:
        await websocket.send("File not found")

async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")

    file_path = "meme.jpg"
    await send_file(websocket, file_path)

async def main():
    async with serve(hello, "0.0.0.0", 8030):
        await asyncio.get_running_loop().create_future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
