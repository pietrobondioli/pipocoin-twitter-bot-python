import tweepy


class PipocoinStreamListener(tweepy.StreamListener):

    def __init__(self, status_handler):
        super(PipocoinStreamListener, self).__init__()
        self.status_handler = status_handler

    def on_status(self, status):
        self.status_handler(status)

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            return False


def start_worker(auth, status_handler, tracked_words, is_Async):
    stream_listener = PipocoinStreamListener(status_handler)
    stream = tweepy.Stream(
        auth=auth,
        listener=stream_listener
    )
    stream.filter(track=tracked_words, is_async=is_Async)
