import botometer
import pandas as pd


rapidapi_key = "rapidapi_key"
twitter_app_auth = { 
"consumer_key": "consumer_key" , 
"consumer_secret" : "consumer_secret", 
"access_token" : "access_token",
"access_token_secret" : "access_token_secret",
}


bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key, **twitter_app_auth)

val = input("Enter Twitter handle: ")
result = bom.check_account(val)
botscore = result['display_scores']['english']['overall']
print(botscore)

#df = pd.DataFrame(result, columns = [ 'display_scores'
 #                                          ])
#print(df)



