import tweepy
import botometer


rapidapi_key = "6c37f64ed3msh1133a7a0288b8efp14749bjsn53713384b4ff"
twitter_app_auth = { 
"consumer_key": "5gmn7aKPH2Auig4IzlfbJFiAL"
"consumer_secret" : "42eLxX1cJHMiphKJ85UH8RtSm4TWpQeVBmPuDnGztQozeprwqV"
"access_token" : "3487626854-WsHEpiyqitzDw3urb2a7jZ8eBCBXq6k538EaOHu"
"access_token_secret" : "9wdcFRMtJoNW60lQDCkjJTEZmggoeY4eQv1fNHfwxG1E6"
}


bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key, **twitter_app_auth)

result = bom.check_account('@akhil_sehgal1')

print(result)