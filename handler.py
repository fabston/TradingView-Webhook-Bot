# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : vsnz                    #
# File Name             : handler.py              #
# ----------------------------------------------- #

import config
from telegram import Bot
from discord_webhook import DiscordWebhook
import tweepy
import smtplib, ssl
from email.mime.text import MIMEText
    
def send_alert(data):
    if config.telegram:
        try:
            tg_bot = Bot(token=config.tg_token)
            tg_bot.sendMessage(config.channel, data, parse_mode = 'MARKDOWN')
        except Exception as e:
            print(e) 
        
    if config.discord:
        try:
            discord_alert = DiscordWebhook(url=config.discord_webhook, content=data)
            response = discord_alert.execute()
        except Exception as e:
            print(e) 
        
    if config.twitter:
        tw_auth = tweepy.OAuthHandler(config.tw_ckey, config.tw_csecret)
        tw_auth.set_access_token(config.tw_atoken, config.tw_asecret)
        tw_api = tweepy.API(tw_auth)
        try:
            tw_api.update_status(status=data)
        except Exception as e:
            print(e) 
        
    if config.email:
        try:
            email_msg = MIMEText(data)
            email_msg['Subject'] = config.email_subject
            email_msg['From']    = config.email_sender
            email_msg['To']      = config.email_sender
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(config.email_host, config.email_port, context=context) as server:
                server.login(config.email_user, config.email_password)
                server.sendmail(config.email_sender, config.email_receivers, email_msg.as_string())
                server.quit()
        except Exception as e:
            print(e) 