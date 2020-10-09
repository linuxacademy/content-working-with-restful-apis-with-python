import socket

HOST = "127.0.0.1"
PORT = 57392

# cpmplete with statement to create a socket for ipv4 and tcp named sock
with
    
    # complete to connect the socket
    sock.
    
    # used to ease reading output
    print("\n\n")

    # complete to get the user's name
    name = 
    
    # complete to get content_length; length of name
    content_length = 

    # formatted header, do not change
    header = """POST / HTTP/1.1 
Host: %s
Content-Type: text/html
Content-Length: %s

""" % (HOST, content_length)

    # complete to add the name to the header and convert to bytes
    payload = 

    # used to ease reading of output
    print("\n\nPayload:")
    print(payload)
    
    # complete to send payload to echo-server
    sock.

    # complete to receive response
    response = 


    print("\n\nReceived:")
    print(response)
    print("\n\n")






