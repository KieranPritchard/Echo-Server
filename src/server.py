import socket

host_ip = "127.0.0.1"
port = 80

socket = socket.socket()
print("Socket created successfully.")

socket.bind((host_ip, port))
print(f"Socket binded to port: {port}.")

socket.listen()
print("Socket is listening")

while True:

    client, address = socket.accept()
    print(f"Connected to client at: {address}")

    client.send("You have successfully connected.".encode())

    client.close()