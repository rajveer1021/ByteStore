# Command parser

from validation import parse_value

def command_parser(raw_data):
    parts = raw_data.split(b" ", 2)
    error = None
    action = parts[0].decode("utf-8")
    if action == "":
        error = "No command provided"
    command = parts[1].decode("utf-8") if len(parts) > 1 else None
    value = None

    if len(parts)>2:
        value_str = parts[2]
        value = parse_value(value_str)

    return action, command, value, error