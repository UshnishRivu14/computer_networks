import socket

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 3456))
server_socket.listen(1)

print("Server is listening on port 3456...")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive data from the client
data = conn.recv(1024)
print(f"Received: {data.decode()}")

# Send a response back to the client
conn.sendall(b"Hello, Client!")

# Close the connection
conn.close()
