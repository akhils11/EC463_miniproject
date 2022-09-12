import tweepy

consumer_key = "5gmn7aKPH2Auig4IzlfbJFiAL"
consumer_secret = "42eLxX1cJHMiphKJ85UH8RtSm4TWpQeVBmPuDnGztQozeprwqV"
access_token =  "3487626854-WsHEpiyqitzDw3urb2a7jZ8eBCBXq6k538EaOHu"
access_token_secret = "9wdcFRMtJoNW60lQDCkjJTEZmggoeY4eQv1fNHfwxG1E6"

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


