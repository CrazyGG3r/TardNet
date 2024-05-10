import socket
import logging
import select

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

server = socket.socket()
ip = "localhost"
port = 9999

server.connect((ip, port))
logging.info(f"Connected to: {ip}:{port}")

while True:
    # Use select to check if the server socket is ready for reading
    ready_to_read, _, _ = select.select([server], [], [], 0.1)  # Timeout of 0.1 seconds

    if ready_to_read:
        # If the server socket is ready to read, receive data
        m = server.recv(2048).decode()
        logging.info(f"Server: {m}")

    # Prompt user for input and send message
    sm = input("Client: ")
    server.sendall(sm.encode("utf-8"))
