# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : vsnz                    #
# File Name             : main.py                 #
# ----------------------------------------------- #

import config
import time
from flask import Flask, request
from handler import *

timestamp = time.strftime("%Y-%m-%d %X")
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        if request.method == 'POST':
            data = request.get_data(as_text=True)
            for whitelisted in config.whitelisted:
                if whitelisted.lower() in data.lower() and config.sec_code in data:
                    print('[✓]', timestamp, 'Alert Received & Sent!\n>', data)
                    send_alert(data)
                    return 'Sent alert', 200
            else:
                print('[✗]', timestamp, 'Alert Received & Refused!\n>', data)
                return 'Refused alert', 400
        else:
            return 'Refused alert', 400
    except Exception as e:
        print('[✘]', timestamp, 'Error:\n>', e)
        return 'Error', 400

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=80)