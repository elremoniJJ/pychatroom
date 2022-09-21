#client.py

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

def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)

def start():
    answer = input('Would you like to connect ? (yes/no) : ')
    if answer.lower() != 'yes':
        return

    connection = connect()
    while True:
        print("'q' for quit")
        msg = input("Message: ")

        if msg == 'q':
            break

        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)

    time.sleep(1)
    print("Disconnected")

start()
