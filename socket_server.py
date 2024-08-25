#!/usr/bin/env python

import asyncio
import os
from websockets.asyncio.server import serve
import msgpack

file_path = ""

def read_chunked_binary(file_path, chunk_size=1024):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk

async def send_file(websocket, path, chunk_size=1024):
    try:
        for chunk in read_chunked_binary(path, chunk_size):
            packed_chunk = msgpack.packb(chunk)
            await websocket.send(packed_chunk)
        
        await websocket.send("finished")
        print("File sent successfully")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        await websocket.close() 

async def hello(websocket):
    name = await websocket.recv()
    if name == "finished":
        print("Finished")
        pass
    if name == "file":
        await send_file(websocket, file_path)

async def main():
    async with serve(hello, "0.0.0.0", 8030):
        await asyncio.get_running_loop().create_future()  # run forever

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    asyncio.run(main())
