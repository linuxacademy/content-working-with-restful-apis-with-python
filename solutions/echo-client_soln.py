import socket

HOST = "127.0.0.1"
PORT = 57392

# create a socket for ipv4 and tcp
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    
    # connect the socket
    sock.connect((HOST, PORT))

    # get name
    name = input("What is your name? ")

    # send name to echo-server, remember it is a string
    sock.sendall(bytes(name, "utf-8"))

    #receive the data
    data = sock.recv(1024)

print(data)





