import socket

HOST = "127.0.0.1"
PORT = 57392

# create a socket for ipv4 and tcp
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    
    # connect the socket
    sock.connect((HOST, PORT))

    # get the user's name
    # used to ease reading of output
    print("\n\n")
    name = input("Please enter your name: ")
    content_length = len(name)

    # formatted header, do not change
    header = """POST / HTTP/1.1 
Host: %s
Content-Type: text/html
Content-Length: %s

""" % (HOST, content_length)


    payload = bytes(header + name, "utf-8")
    # used to ease reading of output
    print("\n\nPayload:")
    print(payload)
    
    # send name to echo-server, remember it is a string
    sock.sendall(payload)

    recv = sock.recv(10000)
    print("\n\nReceived:")
    print(recv)
    print("\n\n")






