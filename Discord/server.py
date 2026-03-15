import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print("Server started...")

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(conn):
    while True:
        try:
            msg = conn.recv(1024)
            broadcast(msg, conn)
        except:
            clients.remove(conn)
            conn.close()
            break

while True:
    conn, addr = server.accept()
    print("Connected:", addr)

    clients.append(conn)

    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()