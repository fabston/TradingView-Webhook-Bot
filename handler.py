import config as config
from telegram import Bot
from discord_webhook import DiscordWebhook

tg_bot = Bot(token=config.tg_token)

telegram = config.send_telegram_alerts
discord  = config.send_discord_alerts

def send_buy_order(data):
    if telegram:
        tg_bot.sendMessage(config.channel, config.Buy_Alert)
        print('Alert has been sent to Telegram.')
    else:
        print('INFO: Telegram alerts are disabled.')
    if discord:
        discord_alert = DiscordWebhook(url=config.discord_webhook, content=config.Buy_Alert)
        response = discord_alert.execute()
        print('Alert has been sent to Discord.')
    else:
        print('INFO: Discord alerts are disabled.')
  
def send_sell_order(data): 
    if telegram:
        tg_bot.sendMessage(config.channel, config.Sell_Alert)
        print('Alert has been sent to Telegram.')
    else:
        print('INFO: Telegram alerts are disabled.')
    if discord:
        discord_alert = DiscordWebhook(url=config.discord_webhook, content=config.Sell_Alert)
        response = discord_alert.execute()
        print('Alert has been sent to Discord.')
    else:
        print('INFO: Discord alerts are disabled.')