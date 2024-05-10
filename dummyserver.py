
import socket
import threading
import select
import logging
import random as r
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

stop = 0
active_clients = []

def start_Server(somethinghere):
    threading.Thread(target=start_server, args=(somethinghere, )).start()
    return

def start_server(somethinghere):
    global stop  
    print(threading.current_thread().name)
    Name = somethinghere[0]
    host = somethinghere[1]
    port = int(somethinghere[2])
    LISTENER_LIMIT = 5
  

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)  # Set server socket to non-blocking mode

    try:
        server.bind((host, port))
        logging.info(f"\t{Name} room running at IP: {host}:{port}")
    except Exception as e:
        server.close()
        logging.info(f"\tUnable to create bind {Name} to host {host} and port {port}: {e}")
        return

    server.listen(LISTENER_LIMIT)

    while True:
        if stop == 1:
            server.close()
            print("Server Stopped")
            return


        ready_to_read, _, _ = select.select([server], [], [], 0.1)  # Timeout of 0.1 seconds

        if ready_to_read:
            client, address = server.accept()
            logging.info(f" Dummy connected from {address[0]}:{address[1]}")
            threading.Thread(target=client_handler, args=(client, )).start()
            
def send_message_to_client(client, message):
    client.sendall(message.encode())


def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)
        
def listen_for_messages(client, username):
     while True:
        # Use select to check if the client socket is ready to be read
        ready_to_read, _, _ = select.select([client], [], [], 0.1)  # Timeout of 0.1 seconds

        if ready_to_read:
            message = client.recv(2048).decode('utf-8')

            if message:
                final_msg = f"{username}~{message}"
                # Send message to all clients (not shown here)
                logging.info(f"{username}: {message}")
            else:
                print(f"The message sent from client {username} is empty")
                break

def client_handler(client):
    # Server will listen for client message that will
    # Contain the username
    while 1:

        # username = client.recv(2048).decode('utf-8')
        username = f"Bot{r.randint(0,1000)}"
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("Client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username, )).start()
