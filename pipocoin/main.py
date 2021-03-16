from configs.tweepy import API
from workers import pipocoin_stream_worker
from utils import loggers_util
from controllers import status_controller


def main():
    loggers_util.log_authenticated_user(API)
    loggers_util.log_twitter_configuration(API)
    pipocoin_stream_worker.start_worker(
        auth=API.auth,
        status_handler=status_controller.status_handler,
        tracked_words=["$pipo"],
        is_Async=True
    )
