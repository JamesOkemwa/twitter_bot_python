import tweepy
from decouple import config 

consumer_key = config("CONSUMER_KEY")
consumer_secret = config("CONSUMER_SECRET")
access_token = config("ACCESS_KEY")
access_secret = config("ACCESS_SECRET")

# Authenticate to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# create API object
api = tweepy.API(auth)

# create a tweet
api.update_status("Hello Tweepy")