# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : config.py               #
# ----------------------------------------------- #

import os

# TradingView Example Alert Message:
# {
# "key":"9T2q394M92", "telegram":"-1001298977502", "discord":"789842349670960670/BFeBBrCt-w2Z9RJ2wlH6TWUjM5bJuC29aJaJ5OQv9sE6zCKY_AlOxxFwRURkgEl852s3", "msg":"Long #{{ticker}} at `{{close}}`"
# }

sec_key = (
    ""  # Can be anything. Has to match with "key" in your TradingView alert message
)

# Telegram Settings
send_telegram_alerts = False
tg_token = ""  # Bot token. Get it from @Botfather
channel = 0  # Channel ID (ex. -1001487568087)

# Discord Settings
send_discord_alerts = False
discord_webhook = ""  # Discord Webhook URL (https://support.discordapp.com/hc/de/articles/228383668-Webhooks-verwenden)

# Slack Settings
send_slack_alerts = False
slack_webhook = ""  # Slack Webhook URL (https://api.slack.com/messaging/webhooks)

# Twitter Settings
send_twitter_alerts = False
twitter_backend = os.getenv("TWITTER_BACKEND", "tweepy")
tw_ckey = ""
tw_csecret = ""
tw_atoken = ""
tw_asecret = ""

# Xquik Settings. Used when TWITTER_BACKEND is set to "xquik".
xquik_api_url = "https://xquik.com/api/v1/x/tweets"
xquik_api_key = os.getenv("XQUIK_API_KEY", "")
xquik_account = os.getenv("XQUIK_ACCOUNT", "")
xquik_timeout = 30

# Email Settings
send_email_alerts = False
email_sender = ""  # Your email address
email_receivers = ["", ""]  # Receivers, can be multiple
email_subject = "Trade Alert!"

email_port = 465  # SMTP SSL Port (ex. 465)
email_host = ""  # SMTP host (ex. smtp.gmail.com)
email_user = ""  # SMTP Login credentials
email_password = ""  # SMTP Login credentials
