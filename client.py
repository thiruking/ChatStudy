import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))
print(f"Client connected from: {client_socket.getsockname()}")
server_message = client_socket.recv(1024).decode()
print(f"Received from server: {server_message}")
client_socket.send("Acknowledgement received from the client.".encode())
client_socket.close()