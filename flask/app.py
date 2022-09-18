import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath('api/botapi.py'))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from api.botapi import Bot
from flask import Flask, jsonify, request

app = Flask(__name__)

bot = Bot()

@app.route('/', methods=['GET'])
def index():
    userid = request.args.get('userid')
    result = jsonify(bot.isBot(userid))
    print(userid, result)
    return result

app.run(host='0.0.0.0', port=3000)