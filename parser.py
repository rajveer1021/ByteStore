# Command parser

def command_parser(raw_data):
    parts = raw_data.split(b" ", 2)

    if len(parts) == 3:
        action_byte, command_byte, value_byte = parts
        action = action_byte.decode("utf-8")
        command = command_byte.decode("utf-8")
        value_str = value_byte.decode("utf-8")
        try:
            if "." in value_str:
                value = float(value_str)
            else:
                value = int(value_str)
        except ValueError:
            value = value_str
    elif len(parts) == 2:
        action_byte, command_byte = parts
        action = action_byte.decode("utf-8")
        command = command_byte.decode("utf-8")
        value = None
    else:
        action_byte = parts[0]
        action = action_byte.decode("utf-8")
        command = None
        value = None

    return action, command, value