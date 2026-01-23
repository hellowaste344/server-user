import json
import socket
import asyncio


class Authentication:
    def __init__(self, name, age, ip):
        self.name = name
        self.age = age
        self.ip = ip
    
    def user_data(self):
        data = {
            "name": self.name,
            "age": self.age,
            "ip": self.ip
        }
        return data
name = input("name: ")    
age = int(input("age: "))
ip = input("ip:")
u1 = Authentication(name,age,ip)

with open("userinfo.txt", "w") as f:
    json.dump(u1.user_data(), f, indent=3)

# ------------------ SERVER -------------------------
async def handle_client(reader, writer):
    data = await reader.read(1024)
    print("User message:", data.decode())

    writer.write(b"Welcome to my server >.<")
    await writer.drain()
    writer.close()

async def start_server():
    server = await asyncio.start_server(handle_client, ip, 40674)
    async with server:
        await server.serve_forever()

# ------------------- CLIENT -----------------------
async def start_client():
    await asyncio.sleep(1) # wait for server

    reader, writer = await asyncio.open_connection(ip, 40674)

    with open("userinfo.txt", "r") as f:
        content = json.load(f)
    
    writer.write(json.dumps(content).encode())
    await writer.drain()
    data = await reader.read(1024)
    print("client requests:", data.decode())
    writer.close()

# ----------------- MAIN --------------------------
async def main():
    await asyncio.gather(start_server(), start_client())

if __name__ == "__main__":
    asyncio.run(main())