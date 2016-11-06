import tweepy
import keys

class TwitterAPI:
    def __init__(self):
        consumer_key = keys.CONSUMER_KEY
        consumer_secret = keys.CONSUMER_SECRET
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = keys.ACCESS_KEY
        access_token_secret = keys.ACCESS_SECRET
        auth.set_access_token(access_token, access_token_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

# if __name__ == "__main__":
#     twitter = TwitterAPI()
#     twitter.tweet("")