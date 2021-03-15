from utils.commands import commands_handler


def status_handler(status):
    command_stack = commands_handler.get_command_stack(status.text)
    print(command_stack)
