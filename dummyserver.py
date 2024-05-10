
import socket
import threading
import logging 
import select

stop = 0

def start_Server(somethinghere):
    threading.Thread(target=start_server, args=(somethinghere, )).start()
    return

def start_server(somethinghere):
    global stop  # Declare stop as global so it can be modified in the function

    Name = somethinghere[0]
    host = somethinghere[1]
    port = int(somethinghere[2])
    LISTENER_LIMIT = 5
    active_clients = []

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)  # Set server socket to non-blocking mode

    try:
        server.bind((host, port))
        print(f"Running the server on {host} {port}")
    except Exception as e:
        server.close()
        print(f"Unable to bind to host {host} and port {port}: {e}")
        return

    server.listen(LISTENER_LIMIT)

    # Monitor the server socket using select to avoid blocking
    while True:
        if stop == 1:
            server.close()
            print("Server Stopped")
            return

        # Use select to monitor the server socket
        ready_to_read, _, _ = select.select([server], [], [], 0.1)  # Timeout of 0.1 seconds

        if ready_to_read:
            client, address = server.accept()
            print(f"Successfully connected to client {address[0]} {address[1]}")
            

# Rest of your functions and code remain the same

# You can update stop from another thread or main thread when you want to stop the server





active_clients = []
def send_message_to_client(client, message):
    client.sendall(message.encode())


def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)
        
def listen_for_messages(client, username):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)

        else:
            print(f"The message send from client {username} is empty")

