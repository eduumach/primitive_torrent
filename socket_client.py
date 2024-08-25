#!/usr/bin/env python

import asyncio
from websockets.asyncio.client import connect
from dotenv import load_dotenv, find_dotenv
import os
import msgpack


load_dotenv(find_dotenv())

async def download_file():
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    uri = f"ws://{host}:{port}"
    async with connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"Client >>> {name}")

        with open("video.mpkv", "wb") as file:
            while True:
                try:
                    # Receive chunked data from the server
                    packed_chunk = await websocket.recv()
                    
                    # If no data is received, the transfer is complete
                    if packed_chunk == "finished":
                        break
                    
                    # Unpack the chunk using msgpack
                    chunk = msgpack.unpackb(packed_chunk)
                    
                    # Write the chunk to the file
                    file.write(chunk)

                except Exception as e:
                    print(f"An error occurred: {e}")
                    break

if __name__ == "__main__":
    asyncio.run(download_file())
