# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : handler.py              #
# ----------------------------------------------- #

import smtplib
import ssl
from email.mime.text import MIMEText

import tweepy
from discord_webhook import DiscordEmbed, DiscordWebhook
from slack_webhook import Slack
from telegram import Bot

import config
from logger import logger


def send_alert(data):
    msg = data["msg"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    
    # ---------------- Telegram ---------------- #
    if config.send_telegram_alerts:
        tg_bot = Bot(token=config.tg_token)
        try:
            chat_id = data.get("telegram", config.channel)   # <-- uses .get() instead of try/except KeyError
            tg_bot.sendMessage(chat_id, msg, parse_mode="MARKDOWN")
            logger.info(f"Telegram alert sent to chat_id={chat_id}")   # <-- NEW log for success
        except Exception as e:
            logger.error(f"Telegram Error: {e}", exc_info=True)   # <-- replaces print()


    if config.send_discord_alerts:
        try:
            webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/" + data["discord"]
            )
            embed = DiscordEmbed(title=msg)
            webhook.add_embed(embed)
            webhook.execute()
        except KeyError:
            webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/" + config.discord_webhook
            )
            embed = DiscordEmbed(title=msg)
            webhook.add_embed(embed)
            webhook.execute()
        except Exception as e:
            print("[X] Discord Error:\n>", e)

    # ---------------- Slack ---------------- #
    if config.send_slack_alerts:
        try:
            slack_url = "https://hooks.slack.com/services/" + data.get("slack", config.slack_webhook)  # <-- .get()
            slack = Slack(url=slack_url)
            slack.post(text=msg)
            logger.info("Slack alert sent successfully")   # <-- NEW success log
        except Exception as e:
            logger.error(f"Slack Error: {e}", exc_info=True)   # <-- replaces print()


    # ---------------- Twitter ---------------- #
    if config.send_twitter_alerts:
        try:
            tw_auth = tweepy.OAuthHandler(config.tw_ckey, config.tw_csecret)
            tw_auth.set_access_token(config.tw_atoken, config.tw_asecret)
            tw_api = tweepy.API(tw_auth)
            tw_api.update_status(
                status=msg.replace("*", "").replace("_", "").replace("`", "")
            )
            logger.info("Twitter alert posted successfully")
        except Exception as e:
            logger.error(f"Twitter Error: {e}", exc_info=True)

    if config.send_email_alerts:
        try:
            email_msg = MIMEText(
                msg.replace("*", "").replace("_", "").replace("`", "")
            )
            email_msg["Subject"] = config.email_subject
            email_msg["From"] = config.email_sender
            email_msg["To"] = config.email_sender
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(
                config.email_host, config.email_port, context=context
            ) as server:
                server.login(config.email_user, config.email_password)
                server.sendmail(
                    config.email_sender, config.email_receivers, email_msg.as_string()
                )
                server.quit()
        except Exception as e:
            print("[X] Email Error:\n>", e)
