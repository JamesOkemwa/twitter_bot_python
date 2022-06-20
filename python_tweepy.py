import tweepy
import time
from decouple import config 

consumer_key = config("CONSUMER_KEY")
consumer_secret = config("CONSUMER_SECRET")
access_token = config("ACCESS_TOKEN")
access_token_secret = config("ACCESS_SECRET")
bearer_token = config("BEARER_TOKEN")

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# first tweet
# client.create_tweet(text="Hello Twitter")

# like a tweet
# client.like(1537429257869090817)

# retweet tweet
# client.retweet(1537429257869090817)

# reply to a tweet
# client.create_tweet(in_reply_to_tweet_id=1537429257869090817, text="Hello user")

# home timeline tweets
# for tweet in api.home_timeline():
#     print(tweet.text)

# fetching a particular user's tweets
# person = client.get_user(username="TechbroJ").data.id
# for tweet in client.get_users_tweets(person).data:
#     print(tweet.text)

# Tweepy stream -> Getting tweets as they're being posted
search_terms = ["python", "programming", "coding"]

class MyStream(tweepy.StreamingClient):
    def on_connect(self):
        """Called after the Streaming API has connected successfully"""
        print("Connected")

    def on_tweet(self, tweet):
        """Called when the API detects a tweet that meets the criteria"""
        if tweet.referenced_tweets == None:
            print(tweet.text)

            # time.sleep(0.2)


stream = MyStream(bearer_token=bearer_token)

for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets"])

        
