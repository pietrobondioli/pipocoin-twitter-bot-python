from configs.tweepy import API
from workers import pipocoin_stream_worker
from utils import api_info_logger
from controllers import status_controller

def main():
    api_info_logger.log_authenticated_user(API)
    pipocoin_stream_worker.start_worker(
      auth = API.auth,
      status_handler = status_controller.status_handler,
      tracked_words = ["$pipo"],
      is_Async = True
    )
