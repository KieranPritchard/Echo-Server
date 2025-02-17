import socket
from ssl import socket_error

#creates the socket
try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket was created")
except socket.error as e:
    print(f"Socket creation encountered error: {e}")