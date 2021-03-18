from services.pipocoin_commands import command_list


def execute_command_stack(command_stack, origin):
    if is_command_valid(command_stack):
        command = command_list[command_stack.pop(0)]
        message = command(origin, command_stack)
    else:
        message = "Invalid command."
    return message


def is_command_valid(command_stack):
    if command_stack and command_list[command_stack[0]]:
        return True
    else:
        return False
