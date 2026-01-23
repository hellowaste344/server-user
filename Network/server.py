import socket 

def start_server(ip="", port=40674):
    s = socket.socket()
    print("Socket has been successfully created!")

    # leave the ip empty string
    s.bind((ip, port))
    print("Server started on port: %s" %(port))

    s.listen(5)
    print("socket is listening")

    while True:
        c, addr = s.accept()
        print(f"Got connection from {addr}")

        msg = "thank you for connecting my server >.<"
        c.send(msg.encode())

        c.close()

if __name__ == "__main__":
    start_server()