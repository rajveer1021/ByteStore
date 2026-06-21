import socket

HOST = '127.0.0.1'
PORT = 6129

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter command: ")
        s.sendall(message.encode("utf-8"))
        data = s.recv(1024)
        print(f"Received {data!r}")