import socket 

def start_client():
    s = socket.socket()
    # connect to the server on local computer
    s.connect(("127.0.0.1", 40674))
    s.send(b"Hello server!")
    # receive data from the server
    print(s.recv(1024).decode())

    s.close()

if __name__ == "__main__":
    start_client()