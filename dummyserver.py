
import socket
import threading
import select
import logging
import random as r
from datetime import datetime

current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_filename = f'.\\server log\\server_{current_time}.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='[%(asctime)s-%(levelname)s]: %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('[%(asctime)s-%(levelname)s]: %(message)s'))
logging.getLogger('').addHandler(console_handler)




start = 0 
stop = 0
active_clients = []
#total thread count:
# Thread 1= server
# Thread 2 = listening client 1
# ... Thread n = client n-1


def start_Server(somethinghere):
    
    threading.Thread(target=start_server, args=(somethinghere, )).start()
    return

def start_server(somethinghere):
    global stop  
    logging.info(f"Thread no.{threading.current_thread().name} for Server started" )
    Name = somethinghere[0]
    host = somethinghere[1]
    port = int(somethinghere[2])
    LISTENER_LIMIT = 5
  

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)  # Set server socket to non-blocking mode

    try:
        server.bind((host, port))
        logging.info(f"{Name} room running at IP: {host}:{port}")
    except Exception as e:
        server.close()
        logging.info(f"\tUnable to create bind {Name} to host {host} and port {port}: {e}")
        return

    server.listen(LISTENER_LIMIT)

    while True:
        if stop == 1:
            server.close()
            logging.info("Server Stopped")
            return


        ready_to_read, _, _ = select.select([server], [], [], 0.1)  # Timeout of 0.1 seconds

        if ready_to_read:
            client, address = server.accept()
            logging.info(f" Dummy connected from {address[0]}:{address[1]}")
            threading.Thread(target=client_handler, args=(client, )).start()
            
def send_message_to_client(client, message):
    client.sendall(message.encode())


def send_messages_to_all(message):
    if active_clients:
        for user in active_clients:
            send_message_to_client(user[1], message)
        
def listen_for_messages(client, username):
     while True:
        # Use select to check if the client socket is ready to be read
        ready_to_read, _, _ = select.select([client], [], [], 0.1)  # Timeout of 0.1 seconds
        try:
            if ready_to_read:
                message = client.recv(2048).decode('utf-8')

                if message:
                    final_msg = f"{username}~{message}"
                    # Send message to all clients (not shown here)
                    logging.info(f"{username}: {message}")
                    send_messages_to_all(message)
                else:
                    logging.info(f"The message sent from client {username} is empty")
                    break
        except:
            logging.info(f"{username} disconnected.")
            return
def client_handler(client):
    
    while 1:

        # username = client.recv(2048).decode('utf-8')
        username = f"Bot{r.randint(0,1000)}"
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            logging.info("Client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username, )).start()
