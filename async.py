import asyncio 

async def func():
    print("Hello!")
    await asyncio.sleep(2)
    print("World")

asyncio.run(func())

async def task1():
    print("task1 started")
    await asyncio.sleep(3)
    print("task1 finished")

async def task2():
    print("task2 started")
    await asyncio.sleep(3)
    print("task2 finished")
    
#run both tasks together
async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

import aiohttp
async def function():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.facebook.com/") as res:
            data = await res.text()
            print(data[:100])
    
asyncio.run(function())

import aiofiles
async def write():
    async with aiofiles.open(r"/home/Xashe/Downloads/CodeSpace/banana.txt", "w") as f:
        await f.write("hello from asyncio!")

async def read():
    async with aiofiles.open(r"/home/Xashe/Downloads/CodeSpace/banana.txt", "r") as f:
        print(await f.read())

asyncio.run(write())
asyncio.run(read())