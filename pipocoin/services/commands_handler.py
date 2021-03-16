from services.pipocoin_commands import command_list


def execute_command_stack(command_stack, origin):
    if command_stack:
        command = command_list[command_stack.pop(0)]
        command_stack, message = command(command_stack, origin)
    return message
