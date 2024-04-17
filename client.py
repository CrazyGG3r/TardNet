import socket

# Set up client
HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    # Send message to server
    message = input("Enter your message: ")
    client.send(message.encode("utf-8"))

    # Receive response from server
    response = client.recv(1024).decode("utf-8")
    print("Server:", response)

