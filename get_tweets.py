import tweepy
import datetime 
from google.cloud import language_v1


# Keys 
consumer_key = "5gmn7aKPH2Auig4IzlfbJFiAL"
consumer_secret = "42eLxX1cJHMiphKJ85UH8RtSm4TWpQeVBmPuDnGztQozeprwqV"
access_key = "3487626854-WsHEpiyqitzDw3urb2a7jZ8eBCBXq6k538EaOHu"
access_secret = "9wdcFRMtJoNW60lQDCkjJTEZmggoeY4eQv1fNHfwxG1E6"

# Function to extract tweets
def get_tweets(username):
  
  # Authorization to consumer key and consumer secret
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

  # Access to user's access key and access secret
  auth.set_access_token(access_key, access_secret)

  # Calling api
  api = tweepy.API(auth)

  number_of_tweets=20
  tweets = api.user_timeline(screen_name=username)


  # Empty Array
  tmp=[]

  # create array of tweet information: username,
  # tweet id, date/time, text
  tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
  for j in tweets_for_csv:

   # Appending tweets to the empty array tmp
   tmp.append(j)

  # Printing the tweets
  # print(tmp)

#
# Driver code
if __name__ == '__main__':

 # Here goes the twitter handle for the user
 # whose tweets are to be extracted.
 while True:
    val = input("Enter the username: ")
    store_usernames = []
    store_usernames.append(val)
    get_tweets(val)
# Instantiates a client
    client = language_v1.LanguageServiceClient()
# The text to analyze
    text = "Hello, world!"
    document = language_v1.Document(
    content=get_tweets(val), type_=language_v1.Document.Type.PLAIN_TEXT
    )
# Detects the sentiment of the text
    sentiment = client.analyze_sentiment(
    request={"document": document}
   ).document_sentiment
# print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))


