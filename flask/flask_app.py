# import sys
# import os
# SCRIPT_DIR = os.path.dirname(os.path.abspath('/Users/aymane/Flutter/projects/EC463_miniproject/api/botapi.py'))
# sys.path.append(os.path.dirname(SCRIPT_DIR))

from api.botapi import Bot
from api.twitterapi import Tweepy

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    json = {}
    username = request.args.get('username')

    bot     = Bot()
    tweepy  = Tweepy(username, 10, True, False)

    json['botometer']   = bot.isBot(username)
    json['tweepy']      = tweepy.get_data()

    print(username, json)
    return json

app.run(host='0.0.0.0', port=3000)