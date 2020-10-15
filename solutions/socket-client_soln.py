import socket

HOST = "127.0.0.1"
PORT = 57392

# create a socket for ipv4 and tcp
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    
    # connect the socket
    sock.connect((HOST, PORT))

    # get the user's name
    name = input("Please enter your name: ")
    content_length = len(name)

    # formatted header, do not change
    header = """POST / HTTP/1.1 
Host: %s
Content-Type: text/html
Content-Length: %s

""" % (HOST, content_length)


    payload = bytes(header + name, "utf-8")
    
    # send name to echo-server, remember it is a string
    sock.sendall(payload)

    response = sock.recv(10000)
    print(response)
    
    #  For Office Use Only, Please Do Not Change Code Below
    expected = b"Hello Cloud Guru " + bytes(name, 'utf-b') + b". I am very glad you are here."

    try:
        assert response == expected
    except AssertionError:
        print("Expected: ", expected)
        print("Response: ", response)
        print("They do not match.")
    else:
        print("Congratulations!  You have completed the lab.")






