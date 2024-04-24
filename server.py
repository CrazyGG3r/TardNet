import socket
import threading
def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")
    while True:
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            print(f"[DISCONNECTED] {address} disconnected.")
            break
        print(f"[{address}] {data}")
        client_socket.send("Message received".encode("utf-8"))
    client_socket.close()
HOST = "0.0.0.0"
PORT = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
while True:
    client_socket, address = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
