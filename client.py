import socket
client = socket.socket()
client.connect(("127.0.0.1", 5555))
print("Connected to server.")
while True:
    msg = input("Client: ")
    client.send(msg.encode())
    if msg.lower() == "exit":
        break
    data = client.recv(1024).decode()
    print("Server:", data)
client.close()