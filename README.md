<p align="center"><a href="https://github.com/vsnz/TradingView-Webhook-Bot" target="_blank"><img src="https://i.imgur.com/ubEoI7w.png"></a></p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-380/"><img src="https://img.shields.io/badge/python-3.8-blue.svg?style=plastic" alt="Python version"></a>
    <a href="https://github.com/vsnz/TradingView-Webhook-Bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/vsnz/TradingView-Webhook-Bot?style=plastic" alt="GitHub license"></a>
    <a href="https://github.com/vsnz/TradingView-Webhook-Bot/issues"><img src="https://img.shields.io/github/issues/vsnz/TradingView-Webhook-Bot?style=plastic" alt="GitHub issues"></a>
    <a href="https://github.com/vsnz/TradingView-Webhook-Bot/pulls"><img src="https://img.shields.io/github/issues-pr/vsnz/TradingView-Webhook-Bot?style=plastic" alt="GitHub pull requests"></a>
    <br /><a href="https://github.com/vsnz/TradingView-Webhook-Bot/stargazers"><img src="https://img.shields.io/github/stars/vsnz/TradingView-Webhook-Bot?style=social" alt="GitHub stars"></a>
    <a href="https://github.com/vsnz/TradingView-Webhook-Bot/network/members"><img src="https://img.shields.io/github/forks/vsnz/TradingView-Webhook-Bot?style=social" alt="GitHub forks"></a>
    <a href="https://github.com/vsnz/TradingView-Webhook-Bot/watchers"><img src="https://img.shields.io/github/watchers/vsnz/TradingView-Webhook-Bot?style=social" alt="GitHub watchers"></a>
</p>

<p align="center">
  <a href="#about">About</a>
  •
  <a href="#features">Features</a>
  •
  <a href="#installation">Installation</a>
  •
  <a href="#images">Images</a>
  •
  <a href="#how-can-i-help">Help</a>
</p>

## About
The **TradingView Webhook Bot** ⚙️ listens to [TradingView](https://tradingview.com) alerts via [webhooks](https://www.tradingview.com/support/solutions/43000529348-i-want-to-know-more-about-webhooks/) using [flask](https://flask.palletsprojects.com/en/1.1.x/).
All alerts can be instantly sent to Telegram, Discord, Twitter and/or Email. 

## Features
- Telegram Support using the [Python Telegram](https://github.com/python-telegram-bot/python-telegram-bot) libary
- Discord Support using [webhooks](https://support.discord.com/hc/de/articles/228383668-Webhooks-verwenden)
- Twitter Support using the [tweepy](https://github.com/tweepy/tweepy) libary
- Email Support using [smtplib](https://docs.python.org/3/library/smtplib.html)
- Alert channels can be enabled or disabled in [`config.py`](https://github.com/vsnz/TradingView-Webhook-Bot/blob/master/config.py)
- Whitelisted words can be easily added in [`config.py`](https://github.com/vsnz/TradingView-Webhook-Bot/blob/master/config.py)
- TradingView `{{close}}`, `{{exchange}}` etc. variables support. Read more [here](https://www.tradingview.com/blog/en/introducing-variables-in-alerts-14880/)

> 💡 Got a feature idea? Open an [issue](https://github.com/vsnz/TradingView-Webhook-Bot/issues/new) and I might implement it.

## Installation
> ⚠️ Best to run the bot on a VPS. I can recommend [Hetzner](https://hetzner.cloud/?ref=tQ1NdT8zbfNY).
1. Clone this repository `git clone https://github.com/vsnz/TradingView-Webhook-Bot.git`
1. Create your virtual environment `python3 -m venv TradingView-Webhook-Bot`
1. Activate it `source TradingView-Webhook-Bot/bin/activate && TradingView-Webhook-Bot`
1. Install all requirements `pip install -r requirements.txt`
1. Edit and update [`config.py`](https://github.com/vsnz/TradingView-Webhook-Bot/blob/master/config.py)
1. Setup TradingView alerts as shown [here](https://i.imgur.com/71UYTcu.png)
    - TradingViews variables like `{{close}}`, `{{exchange}}` etc. work as well. More can be found [here](https://www.tradingview.com/blog/en/introducing-variables-in-alerts-14880/)
    - Your webhook url would be `http://<YOUR-IP>/webhook`
1. If you use a firewall be sure to open port the corresponding port
1. Run the bot `python main.py`

*It is recommended to run flask on a different port like 8080. It is then necessary to forward port 80 to 8080.*

## Images
![Webhook Bot](https://i.imgur.com/vZA42cc.png)

## How can I help?
All kinds of contributions are welcome 🙌! The most basic way to show your support is to `⭐️ star` the project, or raise [`🐞 issues`](https://github.com/vsnz/TradingView-Webhook-Bot/issues/new). You can also buy me some [☕️ coffee](https://www.buymeacoffee.com/vsnz) to help keep me productive!

Thanks again for your support, it is much appreciated! 🙏