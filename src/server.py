import socket

# Host address and port number.
host_ip = "127.0.0.1"
port = 1025

# Socket object to create
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully.")

# Socket bind to host
server_socket.bind((host_ip, port))
print(f"Socket binded to port: {port}.")

# Socket listening for connections
server_socket.listen()
print("Socket is listening")

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