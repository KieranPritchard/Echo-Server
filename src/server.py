import socket
import json

with open("config.json", "r") as file:
    config_data = json.load(file)

# Host address and port numbers.
host_ip = config_data["server"]["host"]
port = config_data["server"]["port"]

# Socket object to create to socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host_ip, port))
server_socket.listen()
print(f"Server started, listening on {host_ip}:{port}")

# Keeps the server program listening for incoming connections
while True:
    # Accepts connections to from client
    client, address = server_socket.accept()
    print(f"Connected to client at: {address}")

    # Handles multiple input from client
    while True:
        try:
            echo_receive = client.recv(1024)

            # Detects client disconnect
            if not echo_receive:
                print(f"Client at {address} disconnected")
                break

            message = echo_receive.decode()
            print(f"Message received from client: {message}")

            # Sends the echo response
            client.send(message.encode())
        except socket.error as e:
            print(f"Error encountered {e}")
    client.close()

    # Sends client echo back
    client.send(echo_receive.encode())

    # Closes the connection
    client.close()