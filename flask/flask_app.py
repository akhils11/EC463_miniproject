# import sys
import os
from api.botapi import Bot
from api.twitterapi import Tweepy
from api.google_nlp import NLP

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    json = {}
    username = request.args.get('username')
    if username != None:
        bot     = Bot()
        tweepy  = Tweepy(username, 200, True, False)
        nlp     = NLP(tweepy.get_data())

        json['botometer']   = bot.isBot(username)
        json['tweepy']      = tweepy.get_data()
        json['googlenlp']   = nlp.get_response()

        return json
        

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))