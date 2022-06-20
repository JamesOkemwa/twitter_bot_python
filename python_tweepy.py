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

# Retweet bot
class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        try:
            client.retweet(tweet.id)
        except Exception as error:
            print(error)


my_stream = MyStream(bearer_token=bearer_token)

rule = tweepy.StreamRule("(#Python OR # programming) (-is:retweet -is:reply)")

my_stream.add_rules(rule, dry_run=True)

my_stream.filter()