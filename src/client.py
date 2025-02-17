import socket

# Host address and port numbers 
host_ip_address = "127.0.0.1"
port = 80

#creates the socket
try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket was created")
except socket.error as e:
    print(f"Socket creation encountered error: {e}")