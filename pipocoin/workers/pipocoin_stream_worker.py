import tweepy


class PipocoinStreamListener(tweepy.StreamListener):

    def __init__(self, API, status_handler):
        super(PipocoinStreamListener, self).__init__()
        self.API = API
        self.status_handler = status_handler

    def filter_exceptions(self, status):
        if status.retweeted:
            return False
        elif status.author.id_str == self.API.me().id_str:
            return False
        else:
            return True

    def on_status(self, status):
        if self.filter_exceptions(status):
            self.status_handler(status)
        return

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            return False


def start_worker(API, auth, status_handler, tracked_words, is_Async):
    stream_listener = PipocoinStreamListener(API, status_handler)
    stream = tweepy.Stream(
        auth=auth,
        listener=stream_listener
    )
    stream.filter(track=tracked_words, is_async=is_Async)
