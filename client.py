import socket

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    message = input("Enter your message: ")
    client.send(message.encode("utf-8"))
    response = client.recv(1024).decode("utf-8")
    print("ServerSorry:", response)

