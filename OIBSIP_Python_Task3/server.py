# server.py
import socket
import threading

HOST = "0.0.0.0"
PORT = 5001

clients = []
nicknames = {}

lock = threading.Lock()

def broadcast(message, sender=None):
    """Send message to all connected clients except the sender."""
    with lock:
        for client in clients:
            if client is not sender:
                try:
                    client.sendall(message)
                except:
                    pass

def handle_client(client, address):
    try:
        client.sendall(b"Enter your nickname:\n")
        nickname = client.recv(1024).decode().strip()
        if not nickname:
            nickname = f"{address[0]}:{address[1]}"

        with lock:
            nicknames[client] = nickname

        broadcast(f"** {nickname} joined the chat **\n".encode())

        while True:
            data = client.recv(4096)
            if not data:
                break
            msg = f"{nickname}: {data.decode().strip()}\n".encode()
            broadcast(msg, sender=client)

    except:
        pass
    finally:
        with lock:
            if client in clients:
                clients.remove(client)
            left_name = nicknames.pop(client, "User")
        broadcast(f"** {left_name} left the chat **\n".encode())
        client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server running on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"Client connected: {addr}")
        with lock:
            clients.append(client)
        threading.Thread(target=handle_client, args=(client, addr), daemon=True).start()

if __name__ == "__main__":
    main()
