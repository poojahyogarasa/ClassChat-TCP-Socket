import socket
import threading
import json
from datetime import datetime

HOST = "127.0.0.1"
PORT = 6000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

username = input("Enter your username: ")
client_socket.send(username.encode())

print("\n" + "#" * 60)
print("               CLASSCHAT CLIENT WINDOW")
print("#" * 60)
print("Format: receiver message")
print("Example: Bob Hello Bob\n")

SEND_SEPARATOR = "-" * 60
RECEIVE_SEPARATOR = "=" * 60


# Receiving Thread
def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                print("\nDisconnected from server")
                break

            message = json.loads(data)

            print("\n" + RECEIVE_SEPARATOR)

            if message["status"] == 1:
                print("INCOMING MESSAGE")
                print(f"FROM   : {message['sender']}")
                print(f"TIME   : {message['time']}")
                print(f"MESSAGE: {message['text']}")

            elif message["status"] == 2:
                print("SERVER ERROR")
                print(f"TIME   : {message['time']}")
                print(f"DETAIL : {message['text']}")

            print(RECEIVE_SEPARATOR)
            print("\n> ", end="", flush=True)

        except:
            break


# Start receiving thread
thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()


# Sending Loop (Main Thread)
while True:
    user_input = input("> ")

    if not user_input:
        continue

    try:
        receiver, text = user_input.split(" ", 1)

        current_time = datetime.now().strftime("%H:%M:%S")

        message = {
            "status": 1,
            "sender": username,
            "receiver": receiver,
            "text": text,
            "time": current_time
        }

        client_socket.send(json.dumps(message).encode())

        print("\n" + SEND_SEPARATOR)
        print("OUTGOING MESSAGE")
        print(f"TO     : {receiver}")
        print(f"TIME   : {current_time}")
        print(f"MESSAGE: {text}")
        print(SEND_SEPARATOR)

    except:
        print("Invalid format! Use: receiver message")