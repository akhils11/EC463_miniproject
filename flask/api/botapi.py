import botometer
from api.api_keys import *

rapidapi_key = rapid_api_key
twitter_app_auth = { 
                    "consumer_key": consumer_key, 
                    "consumer_secret" : consumer_key_secret, 
                    "access_token" : access_token,
                    "access_token_secret" : access_token_secret,
                    }

class Bot:
    def __init__(self):
        self.bom = botometer.Botometer(wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)
        self.result = {}
    '''
    Returns data from  
    @param  {String}        userid:     The user's twitter name
    @return {dict}          self.tweets 
    ''' 
    def isBot(self, user_id):
        self.result = self.bom.check_account(user_id)
        return self.result

if __name__ == "__main__":
    bot = Bot()
    a = bot.isBot('elonmusk')
    print(a)


