import socket

HOST = '127.0.0.1'
PORT = 6129

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'name rajveer')
    data = s.recv(1024)

print(f"Received {data!r}")