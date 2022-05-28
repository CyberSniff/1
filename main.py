# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import socket



if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 28563
   # host_name = socket.gethostname()
    s_id = "1"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
    print("Binding successful!")
    print(f"This is your IP: { s_id}")
    print("Client's command:\n1. Send message\n2. Get a message \n3. Exit")
    string = "No new messages"
    buffer = []
    while True:
        command = input("Enter command: ")
        if command =="1":
            server.send(bytes(s_id, "utf-8"))
            a_id = input("Enter recipient id: ")
            server.send(bytes(a_id, "utf-8"))
            string = input("Enter message: ")
            server.send(bytes(string, "utf-8"))
        if command == "2":
            server.send(bytes(s_id, "utf-8"))
            #string = input("Enter message: ")
            #server.send(bytes(string, "utf-8"))
            buffer = server.recv(1024)
            buffer = buffer.decode("utf-8")
            print(f"New message: {buffer}")
        if command == "3":
            break