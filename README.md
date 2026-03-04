# 💬 ClassChat – TCP Client-Server Chat System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Protocol](https://img.shields.io/badge/Protocol-TCP-green)
![Networking](https://img.shields.io/badge/Concept-Socket%20Programming-orange)
![Status](https://img.shields.io/badge/Type-Academic%20Project-purple)

---

## 📌 Overview

ClassChat is a TCP-based multi-client chat application developed using Python.  
It follows a **Client–Server architecture** and enables multiple users to communicate with each other in real-time through a centralized server.

This project demonstrates practical implementation of:

- TCP socket programming  
- Concurrent client handling using threading  
- JSON-based structured message transmission  
- Real-time client-to-client message routing  
- Server-side client management and validation  

---

## 🏗 System Architecture
## 🧠 How It Works
1. Server starts and listens for connections.
2. Clients connect to the server.
3. Messages are sent in JSON format.
4. Server forwards messages to intended receiver.
5. Multiple clients can communicate simultaneously.

- The **Server** acts as a central controller.
- Clients connect via TCP sockets.
- Messages are routed based on receiver information.
- The server validates whether the receiver is online before forwarding.

---

## 🚀 Features

- ✅ Multi-client concurrent handling  
- ✅ Real-time bidirectional communication  
- ✅ JSON structured messaging format  
- ✅ Active user management  
- ✅ Error handling for offline users  
- ✅ Clean terminal-based interface  

---

## 🧠 How It Works

1. The server starts and listens for incoming client connections.
2. Each client connects using a unique username.
3. Messages are sent in JSON format.
4. The server:
   - Receives the message  
   - Validates the receiver  
   - Forwards it to the intended client  
5. The receiving client displays the formatted message.

---

## 📦 Example JSON Message Format

```json
{
  "status": 1,
  "sender": "Alice",
  "receiver": "Bob",
  "text": "Hi Bob, do you know how TCP works?",
  "time": "23:13:54"
}

````
---

## 🛠 Technologies Used
- Python
- Socket Programming
- Threading
- JSON
- TCP/IP Protocol

---

## ▶️ How to Run the Project
## 1️⃣ Start the Server

Open terminal window and run: python server.py

## 2️⃣ Start the Client

Open another terminal window and run: python client.py
- Enter your username when prompted.

## 3️⃣ Send Messages

Example: Bob Hello Bob

---

## 🔐 Error Handling
- If a receiver is not connected, the server sends an error message.
- If a client disconnects, the server removes it from the active user list.
- The system ensures robust communication handling.

---

## 📚 Academic Context

This project was developed as part of a Networking / Socket Programming coursework assignment.
It covers:
- Basic client-server communication
- Concurrent processing
- Client management
- Message routing logic
- TCP-based communication flow

---

## 📈 Learning Outcomes

Through this project:
- Implemented TCP-based socket communication
- Understood blocking vs concurrent systems
- Applied multithreading for scalability
- Designed structured data transmission using JSON
- Resolved real Git workflow issues during deployment

---
