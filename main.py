# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : vsnz                    #
# File Name             : main.py                 #
# ----------------------------------------------- #

import config
import time
from flask import Flask, request
import json
from handler import *

timestamp = time.strftime("%Y-%m-%d %X")
app = Flask(__name__)

@app.route('/webhook',  methods=['POST'])
def webhook():
    try:
        if request.method == 'POST':
            data = request.get_json()
            key = data['key']
            if key == config.sec_key:
                print(timestamp, 'Alert Received & Sent!')
                send_alert(data)
                return 'Sent alert', 200

            else:
                print('[X]', timestamp, 'Alert Received & Refused! (Wrong Key)')
                return 'Refused alert', 400
                
    except Exception as e:
        print('[X]', timestamp, 'Error:\n>', e)
        return 'Error', 400

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=80)