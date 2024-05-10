import socket
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
server = socket.socket()
ip = "localhost"
port = 9999
server.connect((ip, port))
logging.info("Connected to: {}:{}".format(ip,port))
while True:
   m = server.recv(1024).decode()
   print("Server: {}".format(m))
   sm = str(input("Client: "))
   server.send(bytes(sm, "utf-8"))