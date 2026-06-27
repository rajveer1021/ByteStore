# Storage 
import json
from config import logger

def db_operation(action, command=None, value=None, database = None):
    if action.lower() == "set":
        if command is None or value is None:
            return "Command and value required for SET"
        database[command] = value
        response = "OK"
    elif action.lower() == "get":
        if command is None:
            return "Command required for GET"
        response = (database.get(command, "Key not found"))
    elif action.lower() == "del":
        if command is None:
            return "Command required for DEL"
        key = command
        if key in database:
            database.pop(key)
            response = "OK"
        else:
            response = "Key not found"
    elif action.lower() == "exists":
        if command is None:
            return "Command required for EXISTS"
        key = command
        if key in database:
            response = "1"
        else:
            response = "0"
    elif action.lower() == "keys":
        if command is None:
            return "Command required for KEYS"
        keys = list(database.keys())
        response = str(keys) if keys else "No keys found"
    elif action.lower() == "db":
        response = str(database)
    elif action.lower() == "incr":
        if command is None:
            return "Command required for INCR"
        if isinstance(database.get(command), int):
            database[command] = database.get(command)+1
            response = "OK"
        else:
            response = "Value error"

    else:
        response = "Unknown Command"

    logger.info(f"database logs : {database}")

    return response

def get_database():
    try:
        with open("database.json", "r") as db:
            database = json.load(db)
            return database
    except FileNotFoundError:
        return dict()
    
def save_database(database):
    with open("database.json", "w+") as file:
        json.dump(database, file)   
    logger.info("Data saved successfully")
