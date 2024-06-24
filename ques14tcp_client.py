import socket

def tcp_client(host, port):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        # Send data to the server
        message = "Hello, Server!"
        client_socket.sendall(message.encode())
        print(f"Sent: {message}")

        # Receive data from the server
        response = client_socket.recv(1024)
        print(f"Received: {response.decode()}")

    finally:
        # Close the socket
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    tcp_client('localhost', 3456)
