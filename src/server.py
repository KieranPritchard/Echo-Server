import socket

# Host address and port number.
host_ip = "127.0.0.1"
port = 1025

# Socket object to create to socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host_ip, port))
server_socket.listen()
print(f"Server started, listening on {host_ip}:{port}")

# Keeps the server program listening for incoming connections
while True:
    # Accepts connections to from client
    client, address = socket.accept()
    print(f"Connected to client at: {address}")

    # Receives input from client
    echo_receive = client.recv(1024).decode()
    print(f"Received from client: {echo_receive}")

    # Sends client echo back
    client.send(echo_receive.encode())

    # Closes the connection
    client.close()