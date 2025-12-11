# client.py
import socket
import threading

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(4096).decode()
            if not msg:
                break
            print(msg, end="")
        except:
            break

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((SERVER_HOST, SERVER_PORT))
    except:
        print("Unable to connect to server.")
        return

    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

    nickname = input()
    sock.sendall((nickname + "\n").encode())

    while True:
        try:
            msg = input()
            sock.sendall((msg + "\n").encode())
        except:
            break

if __name__ == "__main__":
    main()
