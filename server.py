import socket
from parser import command_parser

HOST = '127.0.0.1'
PORT = 6129

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn :
        print(f"connected by {addr}")
        database = dict()
        while True:
            raw_data = conn.recv(2048)
            str_data = raw_data.decode("utf-8")
            command = str_data.split(" ")
            response = command_parser(command,database)

            print("database logs : ", database)

            if not raw_data:
                break
            conn.sendall(response.encode("utf-8"))