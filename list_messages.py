#list_messages.py

import socket
import time

PORT = 5050
SERVER = 'localhost' # socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!* Disconnect *!"

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def start():
    connection = connect()
    while True:
        msg = connection.recv(1024).decode(FORMAT)
        print(msg)

start()
