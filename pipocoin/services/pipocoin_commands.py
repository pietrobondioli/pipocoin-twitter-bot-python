def create(command_stack, origin):
    message = "create command called"
    return command_stack, message


def transfer(command_stack, origin):
    message = "transfer command called"
    return command_stack, message


def work(command_stack, origin):
    message = "work command called"
    return command_stack, message


command_list = {
    "create": create,
    "transfer": transfer,
    "work": work,
}
