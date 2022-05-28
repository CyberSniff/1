import socket
import time
from collections import defaultdict
from _thread import start_new_thread


def threaded(c):
    while True:
        # client, address = server.accept()
        command = client.recv(1024)
        command = command.decode("utf-8")
        print(command)
        if command == "1":
            #s_id = client.recv(1024)
            a_id = client.recv(1024)
            a_id = a_id.decode("utf-8")
            print(a_id)
            message = client.recv(1024)
            message_for[a_id].append(message)
            print(a_id)
            print(message_for[a_id])
        if command == "2":
            a_id = client.recv(1024)
            a_id = a_id.decode("utf-8")
            #for i in message_for:
             #   message.join(message_for[a_id])
            print(message_for[a_id])
            message = str(message_for[a_id])
            #message = message.decode("utf-8")
            client.send(bytes(message, "utf-8"))


if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 28563

    all_clents = ["1", "2"]
    message_for = defaultdict(list)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        client, address = server.accept()
        print(f"Connection Establish - {address[1]}, {address[0]}")
        start_new_thread(threaded(client), (client,) )


