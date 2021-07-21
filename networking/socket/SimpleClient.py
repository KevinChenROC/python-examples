import socket  # Import socket module

s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Host name for the server
port = 12345  # Port number for the server

s.connect((host, port))  # connect to the server
print(s.recv(1024))
s.close()  # Close the socket when done
