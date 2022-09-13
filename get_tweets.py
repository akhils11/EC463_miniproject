import tweepy
import datetime 

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
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
  print(tmp)


# Driver code
if __name__ == '__main__':

 # Here goes the twitter handle for the user
 # whose tweets are to be extracted.
 get_tweets("espn")


