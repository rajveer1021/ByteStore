import socket
import json
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
        try :
            with open("database.json", "r") as db:
                database = json.load(db)
                print(f"database: {database}")
                print("db loaded successfully")
        except :
            database = dict()
        
        while True:
            raw_data = conn.recv(2048)
            parser = command_parser(raw_data)
            if parser[3] is not None:
                conn.sendall(str(parser[3]).encode("utf-8"))
                continue
            response = storage(action=parser[0], command=parser[1], value = parser[2], database=database)
    

            if not raw_data:
                json_response = json.dumps(database)
                with open("database.json", "+a") as file:
                    file.write(json_response)
                print("Data saved successfully")
                break
            conn.sendall(str(response).encode("utf-8"))