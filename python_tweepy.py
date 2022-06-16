import tweepy
from decouple import config 

consumer_key = config("CONSUMER_KEY")
consumer_secret = config("CONSUMER_SECRET")
access_token = config("ACCESS_TOKEN")
access_token_secret = config("ACCESS_SECRET")
bearer_token = config("BEARER_TOKEN")

# Authenticate to twitter
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# # create API object
# api = tweepy.API(auth)

# try:
#     api.verify_credentials()
#     print("Authentication Okay")
# except:
#     print("Error occured")

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

# first tweet
# client.create_tweet(text="Hello Twitter")

# like a tweet
client.like(1537429257869090817)