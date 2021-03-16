from utils import commands_util


def status_handler(status):
    command_stack = commands_util.get_command_stack(status.text)
    print(command_stack)
