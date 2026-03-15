import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Username: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("Disconnected")
            client.close()
            break

def send():
    while True:
        msg = input("")
        message = f"{name}: {msg}"
        client.send(message.encode())

threading.Thread(target=receive).start()
threading.Thread(target=send).start()