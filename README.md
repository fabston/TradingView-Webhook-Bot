# TradingView Webhook Bot

![Python3](https://img.shields.io/badge/python-3-blue.svg)
![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

This bot listens to [TradingView](https://tradingview.com) alerts via webhooks and sends them instantly to Telegram and/or Discord. 

## Usage
1. Clone this repository `git clone https://github.com/fabcx/TradingView-Webhook-Bot.git`
2. Create your virtual environment `python3 -m venv TradingView-Webhook-Bot`
3. Activate it `source TradingView-Webhook-Bot/bin/activate`
4. Install all requirements `pip install -r requirements.txt`
5. Edit and update the `config.py` file
6. Setup TradingView alerts as shown [here](https://i.imgur.com/QpAP3wp.png)
    - Your webhook url would be `http://YOUR-IP/webhook`
7. Run the bot `python main.py`

*It is recommended to run flask on a different port like 8080. It is then necessary to forward port 80 to 8080.*

## Donations
BTC: `13VmcVh7U3y7UQiUGp1nnyn6Pz9TPR61a9`
