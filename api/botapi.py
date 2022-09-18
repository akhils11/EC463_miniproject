from api.api_keys import *
import botometer

rapidapi_key = rapid_api_key
twitter_app_auth = { 
"consumer_key": consumer_key, 
"consumer_secret" : consumer_key_secret, 
"access_token" : access_token,
"access_token_secret" : access_token_secret,
}

class Bot:
    def __init__(self):
        self.bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

    def isBot(self, user_id):
        if user_id[0] != '@':
            user_id = '@' + user_id
        result = self.bom.check_account(user_id)

        return result['cap']['universal']

