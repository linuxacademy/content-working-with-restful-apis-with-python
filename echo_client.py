import socket

HOST = "127.0.0.1"
PORT = 57392


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    name = input("What is your name? ")
    sock.sendall(bytes(name, "utf-8"))
    data = sock.recv(1024)

print(data)





