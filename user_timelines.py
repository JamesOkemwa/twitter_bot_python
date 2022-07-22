import python_tweepy

timeline = python_tweepy.api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

