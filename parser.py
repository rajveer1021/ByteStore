# Commmand parser

def command_parser(command, database):
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
    
    return response
            
