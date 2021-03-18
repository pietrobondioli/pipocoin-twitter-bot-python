import re

REGEX_GET_COMMAND_STRING = re.compile(r'\-{1}[\.\,\w\s]*\-', re.IGNORECASE)
REGEX_GET_COMMAND_STACK = re.compile(r'\-\s|\s|\-', re.IGNORECASE)


def get_command_stack(status):
    command_string = get_command_string_from_status(status)
    command_stack = get_command_stack_from_command_string(command_string)
    return command_stack


def get_command_string_from_status(text):
    command_string = REGEX_GET_COMMAND_STRING.findall(text)[0]
    return command_string


def get_command_stack_from_command_string(text):
    command_stack = REGEX_GET_COMMAND_STACK.split(text)
    command_stack = filter_empty_commands_from_stack(command_stack)
    return command_stack


def filter_empty_commands_from_stack(stack):
    filtered_stack = list(filter(lambda c: c != '', stack))
    return filtered_stack
