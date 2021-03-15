import re


def get_command_stack(status):
    command_string = get_command_string_from_status(status)
    command_stack = get_command_stack_from_command_string(command_string)
    return command_stack


def get_command_string_from_status(text):
    REGEX = re.compile(r'\-{1}[\w\s]*\-', re.IGNORECASE)
    command_string = REGEX.findall(text)[0]
    return command_string


def get_command_stack_from_command_string(text):
    REGEX = re.compile(r'\-\s|\s|\-', re.IGNORECASE)
    command_stack = filter_empty_commands_from_stack(REGEX.split(text))
    return command_stack


def filter_empty_commands_from_stack(stack):
    filtered_stack = list(filter(lambda c: c != '', stack))
    return filtered_stack
