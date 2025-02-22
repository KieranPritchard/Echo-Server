import socket
import sys
import json

with open("config.json", "r") as file:
    config_data = json.load(file)

# Host address and port numbers.
host_ip_address = config_data["server"]["host"]
port = config_data["server"]["port"]

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
            if not echo_receive:
                print("The server closed the connection")
                break

            print(f"Echo Received: {echo_receive.decode()}")
        else:
            print("Closing connection...")
            client_socket.close()
            sys.exit()

except:
    print(f"Error connecting to host on port: {port}.")
    client_socket.close()