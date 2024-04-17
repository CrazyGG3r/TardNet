import socket
import threading

# Function to handle client connections
def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")

    while True:
        # Receive data from client
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            print(f"[DISCONNECTED] {address} disconnected.")
            break

        # Print received message
        print(f"[{address}] {data}")

        # Send a response back to the client
        client_socket.send("Message received".encode("utf-8"))

    # Close client connection
    client_socket.close()

# Set up server
HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

while True:
    # Accept incoming connections
    client_socket, address = server.accept()
    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
