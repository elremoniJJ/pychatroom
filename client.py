#client.py

import socket

PORT = 5050
SERVER = 'localhost' # socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!* Disconnect *!"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


client = connect()
msg = "... Testing..."
send(client, msg)

input()

send(client, DISCONNECT_MESSAGE)
