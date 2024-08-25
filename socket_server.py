#!/usr/bin/env python

import asyncio

from websockets.asyncio.server import serve

async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"Server >>> {greeting}")

async def main():
    async with serve(hello, "localhost", 8030):
        await asyncio.get_running_loop().create_future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())


#socket
#protocolo é uma layer em cima do socket
#http é protocolo, tcp é protocolo, udp
#tcp, manda mensagem, client recebe a mensagem, e envia um confirmação ao server que recebeu a mensagem
#udp ele só manda mensagem
# tcp/udp
# 