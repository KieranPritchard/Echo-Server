import socket

# Host address and port numbers.
host_ip_address = "127.0.0.1"
port = 1025

#creates the socket.
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket was created")
except socket.error as e:
    print(f"Socket creation encountered error: {e}")

# Attempts to connect to the server program.
try:
    client_socket.connect((host_ip_address, port))
    print(f"Successfully connected on port: {port}.")

    while True:
        echo_input = input("Please input message to send: ")
        
        # Sends message to echo
        client_socket.send(echo_input.encode())

except:
    print(f"Error connecting to host on port: {port}.")