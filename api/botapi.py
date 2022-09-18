from os import lseek
from api_keys import *
import botometer

rapidapi_key = rapid_api_key
twitter_app_auth = { 
"consumer_key": consumer_key, 
"consumer_secret" : consumer_key_secret, 
"access_token" : access_token,
"access_token_secret" : access_token_secret,
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@clayadavis')

# Check a single account by id
result = bom.check_account(1548959833)

# Check a sequence of accounts
accounts = ['@clayadavis', '@onurvarol', '@jabawack']
for screen_name, result in bom.check_accounts_in(accounts):
    print(screen_name, result)