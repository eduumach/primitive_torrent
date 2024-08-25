#!/usr/bin/env python

import asyncio
import os
from websockets.asyncio.server import serve
import msgpack

def read_chunked_binary(file_path, chunk_size=1024):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk

async def send_file(websocket, path, chunk_size=1024):
        for chunk in read_chunked_binary(path, chunk_size):
            packed_chunk = msgpack.packb(chunk)
            await websocket.send(packed_chunk)
    
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
