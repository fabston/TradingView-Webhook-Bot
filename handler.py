# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : handler.py              #
# ----------------------------------------------- #

import smtplib
import ssl
from email.mime.text import MIMEText
from uuid import uuid4

import requests
import tweepy
from discord_webhook import DiscordEmbed, DiscordWebhook
from slack_webhook import Slack
from telegram import Bot

import config


def format_twitter_status(msg):
    return msg.replace("*", "").replace("_", "").replace("`", "")


def send_tweepy_alert(msg):
    tw_auth = tweepy.OAuthHandler(config.tw_ckey, config.tw_csecret)
    tw_auth.set_access_token(config.tw_atoken, config.tw_asecret)
    tw_api = tweepy.API(tw_auth)
    return tw_api.update_status(status=format_twitter_status(msg))


def send_xquik_alert(msg):
    if not config.xquik_api_key or not config.xquik_account:
        raise ValueError("XQUIK_API_KEY and XQUIK_ACCOUNT are required")

    response = requests.post(
        config.xquik_api_url,
        headers={
            "x-api-key": config.xquik_api_key,
            "Idempotency-Key": "tradingview-" + uuid4().hex,
        },
        json={"account": config.xquik_account, "text": format_twitter_status(msg)},
        timeout=config.xquik_timeout,
    )
    response.raise_for_status()
    return response.json()


def send_twitter_alert(msg):
    backend = config.twitter_backend.strip().lower()
    if backend == "xquik":
        return send_xquik_alert(msg)
    if backend in {"tweepy", "twitter"}:
        return send_tweepy_alert(msg)
    raise ValueError("TWITTER_BACKEND must be 'tweepy' or 'xquik'")


def send_alert(data):
    msg = data["msg"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    if config.send_telegram_alerts:
        tg_bot = Bot(token=config.tg_token)
        try:
            tg_bot.sendMessage(
                data["telegram"],
                msg,
                parse_mode="MARKDOWN",
            )
        except KeyError:
            tg_bot.sendMessage(
                config.channel,
                msg,
                parse_mode="MARKDOWN",
            )
        except Exception as e:
            print("[X] Telegram Error:\n>", e)

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

    if config.send_slack_alerts:
        try:
            slack = Slack(url="https://hooks.slack.com/services/" + data["slack"])
            slack.post(text=msg)
        except KeyError:
            slack = Slack(
                url="https://hooks.slack.com/services/" + config.slack_webhook
            )
            slack.post(text=msg)
        except Exception as e:
            print("[X] Slack Error:\n>", e)

    if config.send_twitter_alerts:
        try:
            send_twitter_alert(msg)
        except Exception as e:
            print("[X] Twitter Error:\n>", e)

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
