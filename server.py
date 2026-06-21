import socket
from parser import command_parser
from storage import storage

HOST = '127.0.0.1'
PORT = 6129

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn :
        print(f"connected by {addr}")
        while True:
            raw_data = conn.recv(2048)
            parser = command_parser(raw_data)
            response = storage(action=parser[0], command=parser[1], value = parser[2])

            if not raw_data:
                break
            conn.sendall(response.encode("utf-8"))