from utils import commands_util
from services import commands_handler
from configs.tweepy import API


def status_handler(status):
    command_stack = commands_util.get_command_stack(status.text)
    message = commands_handler.execute_command_stack(
        command_stack,
        status.author.id_str
    )
    print(message)
    API.update_status(status=message,
                      in_reply_to_status_id=status.id,
                      auto_populate_reply_metadata=True)
