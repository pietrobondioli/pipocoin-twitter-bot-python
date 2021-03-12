from config import tweepy


def main():
    for status in tweepy.API.home_timeline():
        print(status.text)
