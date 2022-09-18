import tweepy
from api_keys import *


class Tweepy:
    '''
    Initializes the tweepy response containing data from last N tweets from User userid
    @param  {String}        screen_name :   The user's twitter name
    @param  {Int}           n           :   Max number of tweets to return
    @param  {Bool}          retweets    :   Include retweets
    @param  {Bool}          replies     :   Exclude replies 
    ''' 
    def __init__(self, screen_name, n, retweets, replies):
        # Initialize Auth
        self.auth           = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api            = tweepy.API(self.auth)

        #Initialize responses
        self.response       = self.api.user_timeline(screen_name=screen_name, count=n, include_rts=retweets, exclude_replies=replies, tweet_mode='extended')
        self.user_response  = self.api.get_user(screen_name=screen_name)

        # Initialize class attributes
        self.name           = screen_name
        self.user_id        = self.user_response.id
        self.image          = self.user_response.profile_image_url_https
        self.banner         = self.user_response.profile_background_image_url_https
        self.tweets         = {'tweets': {}}
    
    '''
    Returns user's data
    @return {dict}          self.tweets 
    ''' 
    def get_last_n_tweets(self):
        
        self.tweets['pinned']   = self.response[0].user.description
        self.tweets['image']    = self.image
        self.tweets['banner']   = self.banner

        for tweets in self.response:
            self.tweets['tweets'][tweets.id_str] = {'text': tweets.full_text, 'time':tweets.created_at, 'language':tweets.lang}

        return self.tweets
    

if __name__ == "__main__":
    tweepy = Tweepy('LarckeningXuruo', 1, True, False)
    a = tweepy.get_last_n_tweets()
    print(a)