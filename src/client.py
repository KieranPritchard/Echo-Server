import socket
import sys

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
    # Connects to host address and ports
    client_socket.connect((host_ip_address, port))
    print(f"Successfully connected on port: {port}.")

    while True:
        echo_input = input("Please input message to send or quit to exit: ").lower()

        if echo_input != "quit":
            # Sends message to echo
            client_socket.send(echo_input.encode())
            echo_receive = client_socket.recv(1024)
            print(f"Echo Received: {echo_receive}")
        else:
            sys.exit()

except:
    print(f"Error connecting to host on port: {port}.")