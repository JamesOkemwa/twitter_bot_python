import tweepy
from decouple import config 

consumer_key = config("CONSUMER_KEY")
consumer_secret = config("CONSUMER_SECRET")
access_token = config("ACCESS_TOKEN")
access_token_secret = config("ACCESS_SECRET")
bearer_token = config("BEARER_TOKEN")

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

# first tweet
# client.create_tweet(text="Hello Twitter")

# like a tweet
client.like(1537429257869090817)

# retweet tweet
client.retweet(1537429257869090817)

# reply to a tweet
client.create_tweet(in_reply_to_tweet_id=1537429257869090817, text="Hello user")