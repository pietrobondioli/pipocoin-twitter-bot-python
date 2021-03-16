from utils import commands_util
from services import commands_handler


def status_handler(status):
    command_stack = commands_util.get_command_stack(status.text)
    message = commands_handler.execute_command_stack(command_stack, status)
    print(message)
