import socket

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
            if command[0].lower() == "set":
                database[command[1]] = command[2]
                response = "OK"
            elif command[0].lower() == "get":
                response = (database.get(command[1], "Key not found"))
            elif command[0].lower() == "del":
                key = command[1]
                if key in database:
                    database.pop(key)
                    response = "OK"
                else:
                    response = "Key not found"
            elif command[0].lower() == "exists":
                key = command[1]
                if key in database:
                    response = "1"
                else:
                    response = "0"
            else:
                response = "Unknown Command"

            print("database", database)

            if not raw_data:
                break
            conn.sendall(response.encode("utf-8"))