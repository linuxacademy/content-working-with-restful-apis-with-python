import socket

HOST = "127.0.0.1"
PORT = 57392

# create a socket for ipv4 and tcp
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    # bind the socket
    

    # set socket to listen, we want no more than 1 in queue
    

    # set to accet connection and retrieve the address of the incoming request
    print("Waiting for connection...")
    # write line to accept socket request, use conn and addr
    
    print(b"Connected: ", addr)
    
    # receive data from echo-client, use a variable `name`
    

    # send this message back
    # "Hello Cloud Guru " + name + ".  You are a superstar!    
    


