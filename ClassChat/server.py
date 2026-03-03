import socket
import threading
import json
from datetime import datetime

HOST = "127.0.0.1"
PORT = 6000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("\n" + "#" * 70)
print("                     CLASSCHAT SERVER")
print("#" * 70)
print(f"Server running on {HOST}:{PORT}")
print("#" * 70 + "\n")

clients = {}   # username -> socket

LOG_SEPARATOR = "-" * 70


def handle_client(client_socket):
    username = None
    try:
        # First message from client = username
        username = client_socket.recv(1024).decode()
        clients[username] = client_socket

        print(LOG_SEPARATOR)
        print(f"[CONNECTED] USER : {username}")
        print(f"Active Users  : {list(clients.keys())}")
        print(LOG_SEPARATOR)

        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            message = json.loads(data)

            sender = message["sender"]
            receiver = message["receiver"]
            text = message["text"]
            time = message["time"]
            status = message["status"]

            print(LOG_SEPARATOR)
            print("MESSAGE ROUTING")
            print(f"TIME     : {time}")
            print(f"SENDER   : {sender}")
            print(f"RECEIVER : {receiver}")
            print(f"CONTENT  : {text}")
            print(LOG_SEPARATOR)

            # Forward if receiver exists
            if receiver in clients:
                clients[receiver].send(json.dumps(message).encode())
            else:
                error_msg = {
                    "status": 2,
                    "sender": "Server",
                    "receiver": sender,
                    "text": "User not online!",
                    "time": datetime.now().strftime("%H:%M:%S")
                }
                client_socket.send(json.dumps(error_msg).encode())

                print(LOG_SEPARATOR)
                print(f"[ERROR] Receiver '{receiver}' not online")
                print(LOG_SEPARATOR)

    except Exception as e:
        print(f"[EXCEPTION] {e}")

    finally:
        if username and username in clients:
            del clients[username]

        client_socket.close()

        print(LOG_SEPARATOR)
        print(f"[DISCONNECTED] USER : {username}")
        print(f"Active Users  : {list(clients.keys())}")
        print(LOG_SEPARATOR)


while True:
    client_socket, address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()