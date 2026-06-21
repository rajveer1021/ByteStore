# Storage 

def storage(action, command=None, value=None, database = None):
    if action.lower() == "set":
        database[command] = value
        response = "OK"
    elif action.lower() == "get":
        response = (database.get(command, "Key not found"))
    elif action.lower() == "del":
        key = command
        if key in database:
            database.pop(key)
            response = "OK"
        else:
            response = "Key not found"
    elif action.lower() == "exists":
        key = command
        if key in database:
            response = "1"
        else:
            response = "0"
    elif action.lower() == "keys":
        keys = list(database.keys())
        response = str(keys) if keys else "No keys found"
    elif action.lower() == "db":
        response = str(database)
    elif action.lower() == "incr":
        if isinstance(database.get(command), int):
            database[command] = database.get(command)+1
            response = "OK"
        else:
            response = "Value error"

    else:
        response = "Unknown Command"

    print("database logs : ", database)

    return response