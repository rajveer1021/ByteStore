import socket
import threading
from config import logger
from parser import command_parser
from storage import db_operation, get_database, save_database

HOST = '127.0.0.1'
PORT = 6129

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    logger.info(f"Server started on {HOST}:{PORT}")

    def handle_client(conn, addr):
            with conn :
                logger.info(f"connected by {addr}")

                # Load the database from a JSON file
                database = get_database()

                try:
                    while True:
                        raw_data = conn.recv(2048)
                        parser = command_parser(raw_data)
                        if parser[3] is not None:
                            conn.sendall(str(parser[3]).encode("utf-8"))
                            continue
                        response = db_operation(action=parser[0], command=parser[1], value = parser[2], database=database)

                        # Save the database to a JSON file
                        save_database(database)

                        if not raw_data:
                            break
                        conn.sendall(str(response).encode("utf-8"))

                except ConnectionResetError:
                    logger.info(f"Connection reset by {addr}")
                
                except Exception as e:
                    logger.error(f"Error occurred with {addr}: {e}")
            
                finally:
                    # Save the database to a JSON file when the client disconnects
                    save_database(database)
                    logger.info(f"Connection closed by {addr}")

    # Start the server and listen for incoming connections
    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()