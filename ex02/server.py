import socket
server = socket.socket()
server.bind(("127.0.0.1", 5555))
server.listen(1)
print("Server is waiting for connection...")
conn, addr = server.accept()
print("Connected with", addr)
while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == "exit":
        print("Client disconnected.")
        break
    print("Client:", data)
    msg = input("Server: ")
    conn.send(msg.encode())
conn.close()